## 1. Markup and style

- [x] 1.1 In Offer A markup, move `<details class="fold">` + `<summary id="sum0">` up to directly after `</h2>`, so it wraps all five `.field` blocks and `#out0`; keep `h2` outside
- [x] 1.2 Update `.fold` CSS: fold spacing sits under heading (margin/border fit new position); add gap between summary and first `.field` when open; keep `.readout` spacing
- [x] 1.3 Update fold comments (CSS comment line 149, HTML comment above `details`, init comment near `card0HTML`) to say fold covers inputs and readout

## 2. Summary

- [x] 2.1 In `compute()`, drop headline-total span from `sum` innerHTML; keep payment span and "Enter valid inputs" branch

## 3. Check

- [x] 3.1 Browser at 390px: every card shows heading + payment only; expand shows inputs + readout; edit keeps open state; steppers work while collapsed
- [x] 3.2 Browser at 1280px: cards load expanded, rows align across columns
- [x] 3.3 Existing in-page self-tests still pass (PMI lock, share link restore into collapsed cards)
