## Why

Google's favicon crawler reads raw HTML. `<link rel="icon" id="favicon">` ships with no `href`; the inline script fills it at runtime from the `#mark` SVG. Crawler sees an empty icon link, indexes no favicon. Search results show a blank icon.

## What Changes

- `<link rel="icon">` gets a static `href` pointing at a real raster file beside the page. Script keeps overwriting it with the serialized `#mark` data URI at load, so live tabs still get the theme-aware SVG.
- Favicon raster must satisfy Google's stated rule: square, side a multiple of 48px. Current `icon-180.png` is 180, not a multiple of 48. Regenerate at 192 as `favicon.png`; `tools/mkicon.py` `S` changes 180 to 192.
- One file serves both roles: `rel="icon"` and `rel="apple-touch-icon"` both point at `/favicon.png`. iOS scales a 192 touch icon fine; avoids a second raster.
- `_redirects` `apple-touch-icon` rows retarget `/favicon.png`.
- Delete `icon-180.png`.

## Capabilities

### New Capabilities
- `page-icon`: how the page declares its icon — static crawlable raster in markup, runtime SVG upgrade, size rule, touch-icon reuse, and the rule that the `#mark` SVG stays the single definition of the artwork.

### Modified Capabilities

(none)

## Impact

- `MortgageOfferAnalyzer.html`: one `href` added on the `rel="icon"` link, `apple-touch-icon` href changed, head comments updated. Script untouched.
- `tools/mkicon.py`: `S = 192`, output filename.
- `_redirects`: two rows.
- `icon-180.png` removed, `favicon.png` added.
- CSP unchanged: `img-src data: 'self'` already covers a same-origin raster and the data URI.
- `math.html` uses `/icon-180.png` for its icon; retarget to `/favicon.png` or it 404s.
- Offline/standalone copy: static href points at a path that does not exist next to a saved file, but the script rewrites it at load, so a saved copy still shows the mark. Only a JS-disabled saved copy shows no icon — same as today.
