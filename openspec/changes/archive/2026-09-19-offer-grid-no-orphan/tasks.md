## 1. Style

- [x] 1.1 Add `align-items:start` to `.offers` rule (`MortgageOfferAnalyzer.html:116`)
- [x] 1.2 Add `container-type:inline-size` to `body` rule
- [x] 1.3 Add `@container (816px <= width < 1094px)` rule setting `.offers:has(> .offer:nth-child(4))` to `repeat(2,1fr)`; comment ties 816/1094 to 260px minimum and 18px gap
- [x] 1.4 Update `.offers` comment to mention 4-offer override

## 2. Check

- [x] 2.1 Browser, 4 offers: resize 700–1400px wide; see 2×2 through old 3+1 band, 4 columns once grid ≥1094px, never 3+1
- [x] 2.2 Browser, 3 offers: 2+1 at mid width, 3 columns when wide
- [x] 2.3 Browser, fold one card beside open one: folded card short, open card full height; all open: rows line up
- [x] 2.4 Browser at 390px: single column, cards stacked A first, unchanged
- [x] 2.5 `#selftest` still passes
