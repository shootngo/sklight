# Builds Jeanie app icons from icons/jeanie-src.jpg (900x900 crop of the round painting).
from PIL import Image, ImageDraw
k = 900 / 976
src = Image.open('icons/jeanie-src.jpg').convert('RGB')
# Square inscribed in the painted circle, so no white corners
box = tuple(round((v - 22) * k) for v in (175, 190, 845, 860))
sq = src.crop(box)
for s in (192, 512):
    sq.resize((s, s), Image.LANCZOS).save(f'icons/icon-{s}.png', optimize=True)
sq.resize((180, 180), Image.LANCZOS).save('icons/apple-touch-icon.png', optimize=True)
sq.resize((96, 96), Image.LANCZOS).save('icons/logo-96.png', optimize=True)
# Maskable: whole round painting at 80% on a dusk background (inside the safe zone)
D = src.size[0]
m = Image.new('L', (D * 4, D * 4), 0)
ImageDraw.Draw(m).ellipse([12, 12, D * 4 - 13, D * 4 - 13], fill=255)
m = m.resize((D, D), Image.LANCZOS)
for s in (192, 512):
    bg = Image.new('RGB', (s, s), (26, 24, 48))
    d = int(s * 0.80)
    bg.paste(src.resize((d, d), Image.LANCZOS), ((s - d) // 2, (s - d) // 2), m.resize((d, d), Image.LANCZOS))
    bg.save(f'icons/maskable-{s}.png', optimize=True)
print('icons built')
