import sys
import shutil
import subprocess
import os
import uharfbuzz as hb
import cairocffi as cairo
from fontTools.ttLib import TTFont
from fontTools.pens.cairoPen import CairoPen

# Check CLI argument
if len(sys.argv) < 2:
    print("Usage: python gen_glyph_grid.py <path-to-font.ttf>")
    sys.exit(1)

# ========= CONFIG =========
FONT_SIZE = 32
LABEL_FONT_SIZE = 16
GLYPHS_PER_ROW = 16
CELL_WIDTH = 32
CELL_HEIGHT = 40
MARGIN_LEFT = 64
MARGIN_TOP = 32
LINE_SPACING = 8

UNICODE_BLOCKS = [
    0x0E00,
    0x0E10,
    0x0E20,
    0x0E30,
    0x0E40,
    0x0E50,
    0x0E80,
    0x0E90,
    0x0EA0,
    0x0EB0,
    0x0EC0,
    0x0ED0,
    0xE130,
    0xE140,
    0xF700,
    0xF710,
    0xF720,
    0xF880,
]

# ========= FONT INPUT =========
font_path = sys.argv[1]
font_filename = os.path.splitext(os.path.basename(font_path))[0]
output_path = f"documentation/images/{font_filename}_grid.png"

ttfont = TTFont(font_path)
glyph_order = ttfont.getGlyphOrder()
glyphset = ttfont.getGlyphSet()

# Get name string metadata
def get_name_record(name_table, nameID):
    for record in name_table.names:
        if record.nameID == nameID:
            try:
                return record.toUnicode()
            except:
                return record.string.decode('utf-8', errors='ignore')
    return "Unknown"

name_table = ttfont["name"]
font_family = get_name_record(name_table, 1)
font_subfamily = get_name_record(name_table, 2)
font_version = get_name_record(name_table, 5)
version = f"{font_family} {font_subfamily} {font_version}"

# Load font for shaping
with open(font_path, "rb") as f:
    fontdata = f.read()
hb_face = hb.Face(fontdata)
hb_font = hb.Font(hb_face)
upem = hb_face.upem
hb_font.scale = (upem, upem)
def scale(size): return size / upem

# ========= DRAW GLYPH =========
def draw_glyph(char, x, y, font_size):
    buf = hb.Buffer()
    buf.add_str(char)
    buf.guess_segment_properties()
    hb.shape(hb_font, buf)
    infos = buf.glyph_infos
    positions = buf.glyph_positions

    ctx.save()
    ctx.translate(x, y + font_size)
    for info, pos in zip(infos, positions):
        gid = info.codepoint
        if gid >= len(glyph_order):
            continue
        name = glyph_order[gid]
        ctx.save()
        ctx.translate(pos.x_offset * scale(font_size), -pos.y_offset * scale(font_size))
        ctx.scale(scale(font_size), -scale(font_size))
        pen = CairoPen(glyphset, ctx)
        glyphset[name].draw(pen)
        ctx.fill()
        ctx.restore()
        ctx.translate(pos.x_advance * scale(font_size), -pos.y_advance * scale(font_size))
    ctx.restore()

# ========= DRAW TEXT (LABELS, VERSION, HEADERS) =========
def draw_text(text, x, y, font_size):
    buf = hb.Buffer()
    buf.add_str(text)
    buf.guess_segment_properties()
    hb.shape(hb_font, buf)
    infos = buf.glyph_infos
    positions = buf.glyph_positions

    ctx.save()
    ctx.translate(x, y + font_size)
    for info, pos in zip(infos, positions):
        gid = info.codepoint
        if gid >= len(glyph_order):
            continue
        name = glyph_order[gid]
        ctx.save()
        ctx.translate(pos.x_offset * scale(font_size), -pos.y_offset * scale(font_size))
        ctx.scale(scale(font_size), -scale(font_size))
        pen = CairoPen(glyphset, ctx)
        glyphset[name].draw(pen)
        ctx.fill()
        ctx.restore()
        ctx.translate(pos.x_advance * scale(font_size), -pos.y_advance * scale(font_size))
    ctx.restore()

# ========= CALCULATE CANVAS SIZE =========
rows = len(UNICODE_BLOCKS)
WIDTH = MARGIN_LEFT + GLYPHS_PER_ROW * CELL_WIDTH + 32
HEIGHT = MARGIN_TOP + rows * CELL_HEIGHT + 32

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

# Background white
ctx.set_source_rgb(1, 1, 1)
ctx.paint()
ctx.set_source_rgb(0, 0, 0)

# ========= HEADER ROW =========
for i in range(GLYPHS_PER_ROW):
    label = f"_{i:X}"
    x = MARGIN_LEFT + i * CELL_WIDTH + 16
    draw_text(label, x, MARGIN_TOP - 28, LABEL_FONT_SIZE)

# ========= DRAW BLOCK ROWS =========
for row_index, base in enumerate(UNICODE_BLOCKS):
    row_y = MARGIN_TOP + row_index * CELL_HEIGHT

    # Row label like FAA7_
    label = f"{(base >> 4):05X}_"
    draw_text(label, 2, row_y + FONT_SIZE / 2, LABEL_FONT_SIZE)

    # Draw glyphs
    for col in range(GLYPHS_PER_ROW):
        codepoint = base + col
        try:
            char = chr(codepoint)
        except:
            continue
        x = MARGIN_LEFT + col * CELL_WIDTH + 16
        draw_glyph(char, x, row_y, FONT_SIZE)

# ========= DRAW FONT VERSION =========
draw_text(version, 20, HEIGHT - 24, LABEL_FONT_SIZE)

# ========= SAVE PNG =========
os.makedirs(os.path.dirname(output_path), exist_ok=True)
surface.write_to_png(output_path)
print(f"║  💾 Image saved to {output_path}", end="")

# ========= PNGQUANT =========
if shutil.which("pngquant"):
    subprocess.run(["pngquant", "--force", "--output", output_path, "--", output_path])
    print(" — 🗜 Compressed")
else:
    print(" — ⚠️ pngquant not found, skipped")
