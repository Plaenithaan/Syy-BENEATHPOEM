import sys
import shutil
import subprocess
import os
import uharfbuzz as hb
import cairocffi as cairo
from fontTools.ttLib import TTFont
from fontTools.pens.cairoPen import CairoPen


if len(sys.argv) < 2:
    print("Usage: python gen_img_dia.py <path-to-ttf-font> [-0|-1|-2|...]")
    sys.exit(1)


WIDTH, HEIGHT = 578, 152
MARGIN = 32
BODY_SIZE = 32
LINE_SPACING = 26
TEXTBOX_WIDTH = WIDTH - 2 * MARGIN


paragraph_sets = [
    [
        "* ยินดีต้อนรับสู่รีโปฟอนต์สือภายใต้อาขยาน!",
        "* แม่น พวกเรารู้อยู่แล้ว",
        "* เกมมันไม่ได้มีชื่อไทยแบบนี้หรอก"
    ],
    [
        "* มันเขียนว่า ‘โหลดไปใช้ดูสิ’",
        "* ดาวน์โหลดฟอนต์ไปใช้ไหม?",
        "       ♥ โหลด      ไม่โหลด"
    ],
]


font_path = sys.argv[1]

if len(sys.argv) >= 3:
    try:
        set_index = int(sys.argv[2])
    except ValueError:
        print(f"Invalid text set: {sys.argv[2]}")
        sys.exit(1)
else:
    set_index = 0


if set_index < 0:
    set_index = len(paragraph_sets) + set_index


if set_index < 0 or set_index >= len(paragraph_sets):
    print(f"Text set out of range: {sys.argv[2]}")
    print(f"Available sets: 0-{len(paragraph_sets) - 1}")
    sys.exit(1)


paragraphs = paragraph_sets[set_index]

font_name = os.path.splitext(os.path.basename(font_path))[0]
output_path = f"documentation/images/{font_name}_dialog.png"


ttfont = TTFont(font_path)


def get_name_record(ttfont, nameID):
    for record in ttfont["name"].names:
        if record.nameID == nameID:
            try:
                return record.toUnicode()
            except:
                return record.string.decode("utf-8", errors="ignore")
    return "Unknown"


font_name = get_name_record(ttfont, 1)
font_weight = get_name_record(ttfont, 2)
font_version = get_name_record(ttfont, 5)
version_text = f"{font_name} {font_weight} {font_version}"


with open(font_path, "rb") as f:
    fontdata = f.read()


hb_face = hb.Face(fontdata)
hb_font = hb.Font(hb_face)

upem = hb_face.upem
hb_font.scale = (upem, upem)

scale = lambda size: size / upem

glyph_order = ttfont.getGlyphOrder()
glyphset = ttfont.getGlyphSet()


surface = cairo.ImageSurface(
    cairo.FORMAT_RGB24,
    WIDTH,
    HEIGHT
)

ctx = cairo.Context(surface)


# Black background
ctx.set_source_rgb(0, 0, 0)
ctx.paint()


# White 6px border
ctx.set_source_rgb(1, 1, 1)
ctx.set_line_width(6)
ctx.rectangle(3, 3, WIDTH - 6, HEIGHT - 6)
ctx.stroke()


def draw_shaped_text(
    text_lines,
    x,
    y,
    max_width,
    font_path,
    font_size,
    line_spacing,
    gray
):
    ctx.save()
    ctx.translate(x, y)
    ctx.set_source_rgb(gray, gray, gray)

    for line in text_lines:
        buf = hb.Buffer()
        buf.add_str(line)
        buf.guess_segment_properties()

        hb.shape(hb_font, buf)

        infos = buf.glyph_infos
        positions = buf.glyph_positions

        ctx.save()

        for info, pos in zip(infos, positions):
            gid = info.codepoint

            if gid >= len(glyph_order):
                continue

            name = glyph_order[gid]

            pos_x = pos.x_offset * scale(font_size)
            pos_y = -pos.y_offset * scale(font_size)

            ctx.save()
            ctx.translate(pos_x, pos_y)

            pen = CairoPen(glyphset, ctx)

            ctx.scale(
                scale(font_size),
                -scale(font_size)
            )

            glyphset[name].draw(pen)

            ctx.fill()
            ctx.restore()

            ctx.translate(
                pos.x_advance * scale(font_size),
                -pos.y_advance * scale(font_size)
            )

        ctx.restore()
        ctx.translate(0, line_spacing)

    ctx.restore()

    return y + line_spacing * len(text_lines)


body_start_y = 16 + LINE_SPACING


for para in paragraphs:
    lines = [para]

    draw_shaped_text(
        lines,
        MARGIN,
        body_start_y,
        TEXTBOX_WIDTH,
        font_path,
        BODY_SIZE,
        LINE_SPACING,
        1
    )

    body_start_y += LINE_SPACING + LINE_SPACING // 2


os.makedirs(
    os.path.dirname(output_path),
    exist_ok=True
)

surface.write_to_png(output_path)

print(
    f"║  💾 Image saved to {output_path}",
    end=""
)


if shutil.which("pngquant"):
    subprocess.run([
        "pngquant",
        "--force",
        "--output",
        output_path,
        "--",
        output_path
    ])

    print(" — 🗜 Compressed")
else:
    print(" — ⚠️ pngquant not found, skipped")