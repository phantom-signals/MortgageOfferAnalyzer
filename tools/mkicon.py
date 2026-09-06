"""Trace the page's #mark SVG as the apple-touch-icon and print the <link> tag to
paste back in. The SVG stays the definition; this raster copy is synced by hand."""
import base64, io
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

buf = io.BytesIO()
img.resize((S, S), Image.LANCZOS).quantize(colors=16).save(buf, "PNG", optimize=True)
print(f'<link rel="apple-touch-icon icon" href="data:image/png;base64,'
      f'{base64.b64encode(buf.getvalue()).decode()}">')
