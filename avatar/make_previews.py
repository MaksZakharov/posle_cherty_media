"""Аватары «После черты»: avatar_N.png 1024x1024, превью в круге 200 px и лист сравнения (PIL).
Обрезка ближе к главному объекту, чтобы читалось в маленьком круге."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
NAMES = {1: "okno_zhenshchina", 2: "porog_so_spiny", 3: "chashka_i_klyuch", 4: "dver_i_svet"}
CROPS = {1: (180, 60, 960, 840), 2: (60, 70, 1000, 1010), 3: (0, 0, 1024, 1024), 4: (90, 60, 1000, 970)}
def circ(im, s):
    im = im.resize((s, s), Image.LANCZOS)
    m = Image.new("L", (s*4, s*4), 0); ImageDraw.Draw(m).ellipse((0, 0, s*4-1, s*4-1), fill=255)
    out = Image.new("RGBA", (s, s), (0, 0, 0, 0)); out.paste(im, (0, 0), m.resize((s, s), Image.LANCZOS)); return out
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
CW = 280; sh = Image.new("RGB", (CW*4, 400), (245, 242, 236)); d = ImageDraw.Draw(sh)
for i in range(1, 5):
    im = Image.open(f"_raw/{i}.jpg").convert("RGB").crop(CROPS[i]).resize((1024, 1024), Image.LANCZOS)
    im.save(f"avatar_{i}_{NAMES[i]}.png")
    c = circ(im, 200); bg = Image.new("RGB", (240, 240), (245, 242, 236)); bg.paste(c, (20, 20), c); bg.save(f"preview_circle_200_{i}.png")
    x = (i-1)*CW
    for size, pos in ((200, (x+40, 15)), (64, (x+50, 235)), (32, (x+150, 251))):
        cc = circ(im, size); sh.paste(cc, pos, cc)
    d.rectangle((x+10, 320, x+CW-10, 375), fill=(30, 30, 30))
    for size, pos in ((40, (x+20, 327)), (24, (x+70, 335))):
        cc = circ(im, size); sh.paste(cc, pos, cc)
    d.text((x+110, 336), f"вариант {i}", fill="white", font=font)
sh.save("avatars_comparison.png")
# резкость: дисперсия лапласиана на 1024
import statistics
for i in range(1, 5):
    g = Image.open(f"avatar_{i}_{NAMES[i]}.png").convert("L").filter(ImageFilter.FIND_EDGES)
    print(i, "edge_mean", round(statistics.mean(g.getdata()), 1), Image.open(f"avatar_{i}_{NAMES[i]}.png").size)
