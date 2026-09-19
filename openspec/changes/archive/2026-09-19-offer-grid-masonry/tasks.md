## 1. Layout script

- [x] 1.1 Add `stackCards()` near `renderOffers()`: reset card margins, count non-zero grid tracks, set `margin-top` so each card below row 1 sits one row gap under the card above it
- [x] 1.2 Create one `ResizeObserver` calling `stackCards`; in `renderOffers()` observe every card after the add loop and call `stackCards()` at the end

## 2. Check

- [x] 2.1 Selftest: force `.offers` to 2 columns with 4 cards, fold Offer A, run `stackCards()`; assert Offer C's top equals Offer A's bottom plus the row gap and Offer C's left equals Offer A's left; restore state
- [x] 2.2 Browser, 4 offers at 2×2: fold A, then B, then both; C and D slide up under their own column; unfold restores; cost bars never overlap
- [x] 2.3 Browser, 3 offers at 2+1: fold A; C slides up under A
- [x] 2.4 Browser at 1 row (wide) and 1 column (phone): no margin applied, layout unchanged
- [x] 2.5 `#selftest` passes
