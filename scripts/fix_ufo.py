import os
import plistlib
import sys
import re
import xml.etree.ElementTree as ET

def parse_sfd(sfd_path):
    data = {
        "weight": None,
        "pfm_family": None,
        "use_typo_metrics": None,
        "stdhw": None,
        "stdvw": None,
        "variation_sequences": {}
    }

    with open(sfd_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if line.startswith("Weight:"):
            data["weight"] = line.split(":", 1)[1].strip()
        elif line.startswith("PfmFamily:"):
            try:
                data["pfm_family"] = int(line.split(":", 1)[1].strip())
            except ValueError:
                pass
        elif line.startswith("OS2_UseTypoMetrics:"):
            data["use_typo_metrics"] = line.split(":", 1)[1].strip() == "1"
        elif "StdHW" in line:
            match = re.search(r"StdHW\s+\d+\s+\[(\d+)\]", line)
            if match:
                data["stdhw"] = int(match.group(1))
        elif "StdVW" in line:
            match = re.search(r"StdVW\s+\d+\s+\[(\d+)\]", line)
            if match:
                data["stdvw"] = int(match.group(1))
        elif line.startswith("AltUni2:"):
            parts = line.strip().split(":")[1].split(".")
            if len(parts) >= 2:
                base_unicode = parts[0].upper().lstrip("0") or "0"
                variation_selector = parts[1].upper().lstrip("0") or "0"
                if i >= 2 and lines[i - 2].startswith("StartChar:"):
                    glyph_name = lines[i - 2].split(":")[1].strip()
                    if variation_selector not in data["variation_sequences"]:
                        data["variation_sequences"][variation_selector] = {}
                    data["variation_sequences"][variation_selector][base_unicode] = glyph_name

    return data


def get_glyph_names(glyphs_dir):
    glyphs = []
    
    # Sort directory listing first to ensure consistent processing order
    for fname in sorted(os.listdir(glyphs_dir)):  # Ensure consistent fallback order
        if not fname.endswith(".glif"):
            continue
        
        path = os.path.join(glyphs_dir, fname)
        try:
            tree = ET.parse(path)
            root = tree.getroot()
            
            # Get glyph name from XML attribute or filename
            glyph_name = root.attrib.get("name", fname[:-5])  # Remove '.glif'
            
            # Try to get Unicode codepoint
            unicode_elem = root.find("unicode")
            if unicode_elem is not None and "hex" in unicode_elem.attrib:
                try:
                    unicode_val = int(unicode_elem.attrib["hex"], 16)
                except ValueError:
                    unicode_val = None  # Invalid hex value, treat as None
            else:
                unicode_val = None  # No Unicode element or no hex attribute
            
            # Only add if the glyph name is valid (not empty)
            if glyph_name and not glyph_name.startswith("_"):  # Skip private use glyphs if needed
                glyphs.append((unicode_val, glyph_name))
                
        except Exception as e:
            print(f"║  Warning: Failed to parse {fname}: {e}")

    # Sort strictly by Unicode codepoint first, then by name for consistency
    # None values are sorted after all valid codepoints
    glyphs.sort(key=lambda x: (x[0] is not None, x[0] if x[0] is not None else float('inf'), x[1]))

    return [name for _, name in glyphs]



def write_plists(ufo_path, glyph_order, variation_sequences=None):
    glyphs_dir = os.path.join(ufo_path, "glyphs")
    lib_path = os.path.join(ufo_path, "lib.plist")
    contents_path = os.path.join(glyphs_dir, "contents.plist")

    # Build glyph name -> filename mapping from existing contents.plist
    with open(contents_path, "rb") as f:
        contents = plistlib.load(f)

    # Reorder contents.plist according to glyph_order
    ordered_contents = {}

    for glyph_name in glyph_order:
        if glyph_name in contents:
            ordered_contents[glyph_name] = contents[glyph_name]

    # Keep any glyphs not found in glyph_order
    for glyph_name, filename in contents.items():
        if glyph_name not in ordered_contents:
            ordered_contents[glyph_name] = filename

    with open(contents_path, "wb") as f:
        plistlib.dump(ordered_contents, f, sort_keys=False)

    print(f"║  Wrote contents.plist with {len(ordered_contents)} glyphs")

    # Write lib.plist
    lib_data = {
        "public.glyphOrder": glyph_order
    }

    if variation_sequences:
        filtered = {
            k: v for k, v in variation_sequences.items()
            if k.upper() != "FFFFFFFF"
        }

        if filtered:
            lib_data["public.unicodeVariationSequences"] = filtered
            print("║  Added variation sequences to lib.plist")

    with open(lib_path, "wb") as f:
        plistlib.dump(lib_data, f, sort_keys=False)

    print(f"║  Wrote lib.plist with {len(glyph_order)} glyphs")


def main(ufo_path):
    fontinfo_path = os.path.join(ufo_path, "fontinfo.plist")
    lib_path = os.path.join(ufo_path, "lib.plist")
    glyphs_dir = os.path.join(ufo_path, "glyphs")

    folder = os.path.dirname(ufo_path)
    ufo_name = os.path.splitext(os.path.basename(ufo_path))[0]
    sfd_path = os.path.join(folder, f"{ufo_name}.sfd")

    if not os.path.exists(sfd_path):
        print(f"║  Error: No matching .sfd file found for '{ufo_name}' in folder.")
        return
    if not os.path.exists(fontinfo_path):
        print(f"║  Error: fontinfo.plist not found at {fontinfo_path}")
        return
    if not os.path.exists(glyphs_dir):
        print(f"║  Error: glyphs directory not found at {glyphs_dir}")
        return

    sfd_data = parse_sfd(sfd_path)
    print(f"║  {sfd_data}")

    # === Modify fontinfo.plist ===
    with open(fontinfo_path, "rb") as f:
        fontinfo = plistlib.load(f)

    # === Clean up familyName ===
    if "familyName" in fontinfo:
        original = fontinfo["familyName"]
        # remvoe prefix ตัวเลข + dash e.g., "2509280116-SyyUDT"
        modified = re.sub(r"^\d+-", "", original).strip()
        if modified != original:
            fontinfo["familyName"] = modified
            print(f"║  Updated familyName: '{original}' -> '{modified}'")

    # === Clean up Weight ===
    remove_weights = [
        "Thin", "ExtraLight", "Light", "Regular", "Medium",
        "SemiBold", "Bold", "ExtraBold", "Black"
    ]

    if "styleMapFamilyName" in fontinfo:
        original = fontinfo["styleMapFamilyName"]
        modified = original

        for w in remove_weights:
            modified = modified.replace(w, "")

        modified = re.sub(r"\s+", " ", modified).strip()

        if modified != original:
            fontinfo["styleMapFamilyName"] = modified
            print(f"║  Updated styleMapFamilyName: '{original}' -> '{modified}'")

    # always update styleMapStyleName (weight-based, lowercase)
    if "postscriptWeightName" in fontinfo:
        weight = fontinfo["postscriptWeightName"].lower()
        original = fontinfo.get("styleMapStyleName")
        fontinfo["styleMapStyleName"] = weight

        if original != weight:
            if original is None:
                print(f"║  Added styleMapStyleName: '{weight}'")
            else:
                print(f"║  Updated styleMapStyleName: '{original}' -> '{weight}'")

    # === Extra settings from SFD ===
    if sfd_data["pfm_family"] == 49:
        fontinfo["postscriptIsFixedPitch"] = True
        print("║  Set 'postscriptIsFixedPitch' to true.")

    if sfd_data["use_typo_metrics"]:
        fontinfo["openTypeOS2Selection"] = [7]
        print("║  Set 'openTypeOS2Selection' to [7].")

    if sfd_data["stdhw"] is not None:
        fontinfo["postscriptStemSnapH"] = [sfd_data["stdhw"]]
        print(f"║  Set 'postscriptStemSnapH' to [{sfd_data['stdhw']}].")

    if sfd_data["stdvw"] is not None:
        fontinfo["postscriptStemSnapV"] = [sfd_data["stdvw"]]
        print(f"║  Set 'postscriptStemSnapV' to [{sfd_data['stdvw']}].")

    # === Add Typographic Family/Subfamily (English/US) === 
    if "familyName" in fontinfo:
        fam = fontinfo["familyName"]
        fontinfo["openTypeNamePreferredFamilyName"] = fam
        print(f"║  Set openTypeNamePreferredFamilyName[en] = '{fam}'")
        
    if "styleMapStyleName" in fontinfo:
        subfam = fontinfo["styleMapStyleName"].capitalize()
        fontinfo["openTypeNamePreferredSubfamilyName"] = subfam
        print(f"║  Set openTypeNamePreferredSubfamilyName[en] = '{subfam}'")

    with open(fontinfo_path, "wb") as f:
        plistlib.dump(fontinfo, f)

    # === Write lib.plist ===
    glyph_order = get_glyph_names(glyphs_dir)
    write_plists(
        ufo_path,
        glyph_order,
        sfd_data.get("variation_sequences")
    )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python fix_ufo.py sources/SyyUDT-Regular.ufo (note: `*.ufo` , not `*.ufo/` )")
    else:
        main(sys.argv[1])
