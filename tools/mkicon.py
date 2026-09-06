"""Trace the page's #mark SVG into icon-180.png, the bookmark and home-screen icon.
Mobile browsers fetch icons over the network and ignore data: URIs, so the mark needs
a real file beside the page. The SVG stays the definition; this copy is synced by hand."""
import io
from PIL import Image, ImageDraw

S, SS = 180, 4                            # output size, supersample factor
n = S * SS
k = n / 32.0                              # viewBox "0 0 32 32" -> pixels
INK, BG = (31, 81, 98), (244, 245, 242)   # .mark-b fill, --paper

img = Image.new("RGB", (n, n), BG)
d = ImageDraw.Draw(img)
pts = lambda *xy: [(x * k, y * k) for x, y in xy]

# .mark-h. Starts mid-edge and closes one segment past the start so the roof apex
# falls on a round joint instead of the seam between the two endpoints.
d.line(pts((3, 13.9), (16, 3.4), (29, 13.9), (29, 28.6), (3, 28.6), (3, 13.9), (16, 3.4)),
       fill=INK, width=round(2.6 * k), joint="curve")
for x, y in ((9, 20), (14, 17), (19, 14)):        # .mark-b bars
    d.rounded_rectangle([x * k, y * k, (x + 4) * k, 25.6 * k], radius=k, fill=INK)

img.resize((S, S), Image.LANCZOS).quantize(colors=16).save(
    "icon-180.png", optimize=True)
