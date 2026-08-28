#!/usr/bin/env python3
import sys
import re
from fontTools.ttLib import TTFont

if len(sys.argv) < 3:
    print("Usage: python fix_uni25cc_liga.py input.ttf output.ttf")
    sys.exit(1)

infile = sys.argv[1]
outfile = sys.argv[2]

font = TTFont(infile)
pattern = re.compile(r"^uni25CC\.\d+$")  # matches uni25CC.1, uni25CC.2, etc.

def fix_substitutions(lookup):
    if not hasattr(lookup, "SubTable"):
        return
    for subtable in lookup.SubTable:

        # SingleSubst mappings
        if hasattr(subtable, "mapping"):
            new_map = {}
            for k, v in subtable.mapping.items():
                if k == "uni25CC" and isinstance(v, str) and pattern.match(v):
                    continue
                if isinstance(v, str) and pattern.match(v):
                    v = "uni25CC"
                elif isinstance(v, list):
                    v = ["uni25CC" if pattern.match(x) else x for x in v]
                new_map[k] = v
            subtable.mapping = new_map

        # LigatureSubst (liga)
        if hasattr(subtable, "ligatures"):
            new_ligatures = {}
            for first_glyph, lig_list in subtable.ligatures.items():
                # rename first glyph if needed
                if pattern.match(first_glyph):
                    first_glyph_new = "uni25CC"
                else:
                    first_glyph_new = first_glyph

                # rename inside each ligature
                for lig in lig_list:
                    lig.Component = [c if not pattern.match(c) else "uni25CC" for c in lig.Component]
                    if pattern.match(lig.LigGlyph):
                        lig.LigGlyph = "uni25CC"

                new_ligatures[first_glyph_new] = lig_list

            subtable.ligatures = new_ligatures

# Fix GSUB
if "GSUB" in font:
    gsub = font["GSUB"].table
    if gsub.LookupList:
        for lookup in gsub.LookupList.Lookup:
            fix_substitutions(lookup)

font.save(outfile)
print(f"✅ Fixed font saved as {outfile}")
