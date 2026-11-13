"""Make the one-color white footer badge (Family of Brands row) from the full-color badge.

Colored areas become solid white; white areas (lettering cut into the outer band, the center
background) and the transparent background become transparent. Same style as the Broker and
Funder footer badges.

Usage: python3 src/make-white-badge.py vendor-badge.png family-of-brands/secure-vendor-badge.png
"""
import sys
from PIL import Image

src, dst = sys.argv[1], sys.argv[2]
im = Image.open(src).convert('RGBA')
out = Image.new('RGBA', im.size, (255, 255, 255, 0))
px, po = im.load(), out.load()
for y in range(im.height):
    for x in range(im.width):
        r, g, b, a = px[x, y]
        # 1.0 for clearly colored pixels, 0.0 for white/near-white, smooth in between (keeps edges anti-aliased)
        ink = max(0.0, min(1.0, (245 - min(r, g, b)) / 120))
        po[x, y] = (255, 255, 255, round(a * ink))
out.thumbnail((240, 240), Image.LANCZOS)
out.save(dst)
