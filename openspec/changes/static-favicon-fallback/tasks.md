## 1. Raster

- [x] 1.1 In `tools/mkicon.py`, change `S` from 180 to 192 and the `save()` filename to `favicon.png`; update the module docstring's filename mention
- [x] 1.2 Run `tools/mkicon.py` in the `webdev` conda env from the repo root; confirm `favicon.png` written
- [x] 1.3 Verify `file favicon.png` reports `192 x 192`, and open it to confirm the house outline and three ascending bars render clean at that size
- [x] 1.4 Delete `icon-180.png`

## 2. Markup

- [x] 2.1 In `MortgageOfferAnalyzer.html`, add `href="/favicon.png"` to `<link rel="icon" id="favicon">`
- [x] 2.2 Update the comment above that link: it no longer says the href is left empty; it says the static file is what a crawler reads and the script upgrades it to the SVG at load
- [x] 2.3 Point `<link rel="apple-touch-icon">` at `/favicon.png` and change `sizes="180x180"` to `sizes="192x192"`
- [x] 2.4 Leave the script line that overwrites `$("favicon").href` unchanged
- [x] 2.5 In `tools/mkmath.js`, retarget both head icon links to `/favicon.png` and update the touch icon's `sizes`
- [x] 2.6 Run `npm run build:math`; confirm `math.html` now references `/favicon.png` and nothing references `icon-180.png` (`grep -rn "icon-180" . --exclude-dir=node_modules --exclude-dir=.git`)

## 3. Routing

- [x] 3.1 In `_redirects`, retarget the `/apple-touch-icon.png` and `/apple-touch-icon-precomposed.png` rows to `/favicon.png`
- [x] 3.2 Confirm `.assetsignore` does not exclude `favicon.png`

## 4. Verify

- [x] 4.1 Open `MortgageOfferAnalyzer.html` with `#selftest`; confirm title reads `selftest passed`
- [x] 4.2 In a loaded page, confirm `document.getElementById("favicon").getAttribute("href")` is the static path in the raw source and `document.getElementById("favicon").href` after load is the `data:image/svg+xml,` URI
- [x] 4.3 Confirm no Content Security Policy violation in the console on load, hosted and from `file://`
- [x] 4.4 Open a saved `file://` copy; confirm the tab icon still shows the mark and no visible error appears
- [ ] 4.5 After deploy, confirm `/favicon.png`, `/apple-touch-icon.png`, `/apple-touch-icon-precomposed.png` each return 200
