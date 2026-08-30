import fontforge

font = fontforge.activeFont()

VS15 = 0xFE0E

chars = [
    0x2194,  # ↔
    0x2195,  # ↕
    0x2196,  # ↖
    0x2197,  # ↗
    0x2198,  # ↘
    0x2199,  # ↙
    0x21A9,  # ↩
    0x21AA,  # ↪
    0x26A0,  # ⚠
    0x1F494, # 💔
]

for cp in chars:
    slot = font.findEncodingSlot(cp)

    if slot == -1:
        print("Missing:", hex(cp))
        continue

    glyph = font[slot]

    # Keep existing alternate Unicode mappings
    altuni = list(glyph.altuni or ())

    entry = (cp, VS15, 0)

    if entry not in altuni:
        altuni.append(entry)
        glyph.altuni = tuple(altuni)

    print("Added VS15:", hex(cp), "->", glyph.glyphname)

print("DONE")