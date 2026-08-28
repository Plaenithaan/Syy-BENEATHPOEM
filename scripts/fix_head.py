#!/usr/bin/env python3
import sys
from fontTools.ttLib import TTFont

if len(sys.argv) < 3:
    print("Usage: python fix_head.py input.ttf output.ttf")
    sys.exit(1)

infile = sys.argv[1]
outfile = sys.argv[2]

font = TTFont(infile)

# Read name table version string for platformID=3, encodingID=1
version_name = None
for record in font["name"].names:
    if record.nameID == 5 and record.platformID == 3 and record.platEncID == 1:
        version_name = str(record.toUnicode())
        break

if version_name:
    # Extract the numeric version from the string (e.g., "Version 50.00; …")
    import re
    m = re.search(r"Version (\d+(\.\d+)?)", version_name)
    if m:
        ver_num = float(m.group(1))
        print(f"Setting head.fontRevision = {ver_num} (from name table)")
        font["head"].fontRevision = ver_num
    else:
        print("⚠️ Could not parse numeric version from name table")
else:
    print("⚠️ Version string not found in name table")

font.save(outfile)
print(f"✅ Font saved as {outfile}")
