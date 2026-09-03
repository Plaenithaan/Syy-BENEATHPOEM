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
    print("Usage: python gen_img_text.py <path-to-ttf-font>")
    sys.exit(1)

# ========== CONFIG ==========
WIDTH, HEIGHT = 1024, 1024
MARGIN = 8
HEADLINE_SIZE = 64
GREY_HEADLINE_SIZE = 32
DCENX_SIZE = 64
BODY_SIZE = 32
LINE_SPACING = 26
TEXTBOX_WIDTH = WIDTH - 2 * MARGIN

# ========== TEXT CONTENT ==========
grey_headline = "No Bold, No Italic, N̸o̸ h̸i̸n̸t̸, No Perfect Kerning. etc"
headline = "JUST A             STUPID FONT."
dcenx = "（○╹◡╹○）"
paragraphs = [
    "The quick brown fox jumps over the lazy dog. Lí hó! Guá sī Hio̍h ",
    "เป็นมนุษย์สุดประเสริฐเลิศคุณค่า กว่าบรรดาฝูงสัตว์เดรัจฉาน      Tshuì-lân--la!",
    "จงฝ่าฟันพัฒนาวิชาการ       อย่าล้างผลาญฤๅเข่นฆ่าบีฑาใคร    Zażółć gęślą ",
    "ไม่ถือโทษโกรธแช่งซัดฮึดฮัดด่า หัดอภัยเหมือนกีฬาอัชฌาสัย jaźń. Под южно дърво",
    "ปฏิบัติประพฤติกฎกำหนดใจ    พูดจาให้จ๊ะๆ จ๋าๆ น่าฟังเอยฯ цъфтящо в синьо,",
    "นายสังฆภัณฑ์ เฮงพิทักษ์ฝั่ง ผู้เฒ่าซึ่งมีอาชีพเป็นฅนขายฃวด бягаще малко пухкаво",
    "ถูกตำรวจปฏิบัติการจับฟ้องศาลฐานลักนาฬิกาคุณหญิงฉัตรชฎา   зайче. Ξεσκεπάζω ",
    "ฌานสมาธิ๐๑๒๓๔๕๖๗๘๙๏๛๚ก๎๎ัจ๎๎ัอ๎๎ัห๎๎นห๎๎มอ๎๎ยญ๎๎ญพ๎๎รพ๎๎ร๎๎ญ   την ψυχοφθόρα σας",
    "พี่ฎูปู่นู๋เป่าปี่ aผ่ผ้ผ๊ผ๋ผีผี่ผี้ผี๊ผี๋ผี์ฝ่ฝ้ฝ๊ฝ๋ฝ์ฝีฝี่ฝี้ฝี๊ฝี๋ฝี์บับั่บั้บั๊บั๋ปัปั่ปั้ปั๊ปั๋ปัํปั์ปั็์ปีปี้ປີປີ້    βδελυγμία.",
    "ก ผํผํ่ผํ้ผํ๊ผํ๋ปํปํ่ปํ้ปํ๊ปํ๋ ผำผ่ำผ้ำผ๊ำผ๋ำฝำฝ่ำฝ้ำฝ๊ำฝ๋ำ จุฬานาฬิกา กิกิํกึกึํ ຊາຕລາວຕັ້ງແຕ່ເດີມມາ",
    "b ผํผํ่ผํ้ผํ๊ผํ๋ปํปํ่ปํ้ปํ๊ปํ๋ ผำผ่ำผ้ำผ๊ำผ๋ำฝำฝ่ำฝ้ำฝ๊ำฝ๋ำ จุฬานาฬิกา กิกิํกึกึํ   ຂື້ນຊື່ລືຊາຢູ່ໃນອາຊີ",
    "ด้านบนคือ ถ้าเรนเดอร์เฟล ไม่แยกอำให้แต่ต้น เช่นในเทอร์มินัล   ຊາວລາວຜູກພັນໄມຕຣີ",
    "ກຂ຃ຄ຅ຆງຈຉຊຌຎຏຐຑຒຓດຕຖທຘນບປຜຝພຟຠມຍຢຣ຤ລ຦ວຨຩສຫຬອຮໞໟໜໝ໠໡໢໣",
    "ສະບາຍດີຜູ້ໃຊ້ທັງຫຼາຽພາກັນເຂົ້າເຫຼົ້າเหຼู้าปุ่ปุีปุี่ปุีํปุี็บ๎บิ๎ป๎ปิ๎บุ๎ปุ๎ดู̱กู้̱ก้̱a̱ชรฺู  ຮ່ວມສາມັຄຄີຮັກຫໍ່ໂຮມກັນ",
    "ຮ່ວມຊ່ວຽກັນສ້າງ ກ່ກ້ກ໊ກ໋ກ໌ກໍກ໎ ໑໒໓໔໕໖໗໘໙໐ໆຯ໚໏໛ ຜຼູ້ປຼູ້ເຫຼູົ້າງູ້    ຮັກຊາຕຮັກປະເທສເຮົາ",
    "Trường quê em do bố của em xây kỹ nên sạch và đẹp lắm. ญู̱ญ้̱ญู้̱",
    "¹‍²‍³‍̶‍₁‍₂‍₃ ¹‍̶‍₁ ¹‍²‍̶‍₃ ¹‍₁‍̲ ¹‍²‍₁‍₂‍̲ ¹‍²‍³‍₁‍₂‍₃‍̲ ¹‍²‍³‍̶‍₁‍₂‍₃‍̲ ₁‍₂‍₃‍̲ ₁‍₂‍̲ ★☆♡♥ ❤ 💔 ❥ ",
    "ຮັກເຈົ້າປົກເກສເກສາ ໂຮມຮັກຮ່ວມສາສນາ ແຕ່ບູຮານມາຮັກສາດິນແດນ ບໍ່ໃຫ້ຊາຕໃດມາລວນ",
    "ຣາວີຣົບກວນຍາດແຍ່ງຊີງເອົາ ໃຜຂືນເຂົ້າມາລູ່ວຸ່ນວາຽ ສູ້ຈົນຕົວຕາຽຕ້ານທານສັຕຼູ ─━│┃┄┅┆┇┈┉",
    "ຊ່ວຍເຊີດຊູເລືອດເນື້ອເຊື້ອເຜົ່າ ຟື້ນຟູກູ້ເອົາບັນເທົາທຸກຂ໌ກັນ ┊┋┌┍┎┏┐┑┒┓└┕┖┗┘┙┚┛├┝┞┟"
]

# ========== OUTPUT PATH ==========
font_path = sys.argv[1]
output_path = f"documentation/images/{os.path.basename(font_path).replace('.ttf', '')}_text.png"

# Read font metadata
ttfont = TTFont(font_path)

def get_name_record(ttfont, nameID):
    for record in ttfont["name"].names:
        if record.nameID == nameID:
            try:
                return record.toUnicode()
            except:
                return record.string.decode('utf-8', errors='ignore')
    return "Unknown"

font_name = get_name_record(ttfont, 1)
font_weight = get_name_record(ttfont, 2)
font_version = get_name_record(ttfont, 5)
version_text = f"{font_name} {font_weight} {font_version}"

# ========== CAIRO + HARFBUZZ SETUP ==========
with open(font_path, "rb") as f:
    fontdata = f.read()

hb_face = hb.Face(fontdata)
hb_font = hb.Font(hb_face)
upem = hb_face.upem
hb_font.scale = (upem, upem)
scale = lambda size: size / upem

glyph_order = ttfont.getGlyphOrder()
glyphset = ttfont.getGlyphSet()

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, WIDTH, HEIGHT)
ctx = cairo.Context(surface)
ctx.set_source_rgb(1, 1, 1)
ctx.paint()
ctx.set_source_rgb(0, 0, 0)

# Helper function to shape and draw text with Cairo
def draw_shaped_text(text_lines, x, y, max_width, font_path, font_size, line_spacing, gray):
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
            ctx.scale(scale(font_size), -scale(font_size))
            glyphset[name].draw(pen)

            ctx.fill()
            ctx.restore()
            ctx.translate(pos.x_advance * scale(font_size), -pos.y_advance * scale(font_size))
        ctx.restore()
        ctx.translate(0, line_spacing)
    ctx.restore()
    return y + line_spacing * len(text_lines)


# ========== GREY HEADLINE ==========
grey_headline_y = 32 +30
draw_shaped_text([grey_headline], MARGIN, grey_headline_y, TEXTBOX_WIDTH, font_path, GREY_HEADLINE_SIZE, LINE_SPACING, 0.5)

# ========== BLACK HEADLINE ==========
black_headline_y = grey_headline_y + GREY_HEADLINE_SIZE + 40
draw_shaped_text([headline], MARGIN, black_headline_y, TEXTBOX_WIDTH, font_path, HEADLINE_SIZE, LINE_SPACING, 0)

# ========== SOM DCENX ==========
dcenx_y = black_headline_y + 20 
draw_shaped_text([dcenx], MARGIN + 220, dcenx_y, TEXTBOX_WIDTH, font_path, DCENX_SIZE, LINE_SPACING, 0)

# ========== BODY TEXT ==========
body_start_y = dcenx_y + 32 + LINE_SPACING
for para in paragraphs:
    lines = [para]
    draw_shaped_text(lines, MARGIN, body_start_y, TEXTBOX_WIDTH, font_path, BODY_SIZE, LINE_SPACING, 0)
    body_start_y += LINE_SPACING + LINE_SPACING // 2

# ========== VERSION INFO ==========
ctx.set_source_rgb(0, 0, 0)

buf = hb.Buffer()
buf.add_str(version_text)
buf.guess_segment_properties()
hb.shape(hb_font, buf)

if all(info.codepoint != 0 for info in buf.glyph_infos):
    draw_shaped_text([version_text], MARGIN, HEIGHT - 8, TEXTBOX_WIDTH, font_path, 16, 0, 0)
else:
    ctx.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    ctx.set_font_size(16)
    ctx.move_to(MARGIN, HEIGHT - 8)
    ctx.show_text(version_text)

# ========== SAVE ==========
os.makedirs(os.path.dirname(output_path), exist_ok=True)
surface.write_to_png(output_path)
print(f"║  💾 Image saved to {output_path}", end="")

# ========== PNGQUANT ==========
if shutil.which("pngquant"):
    subprocess.run(["pngquant", "--force", "--output", output_path, "--", output_path])
    print(" — 🗜 Compressed")
else:
    print(" — ⚠️ pngquant not found, skipped")
