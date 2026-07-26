## 1. Baseline

- [x] 1.1 Open `MortgageAnalysisTool.html` in a browser and record the full readout for both offers with the default inputs (loan 400000, home value 450000, A 6.25%/30yr/12/3000/0.55, B 5.99%/30yr/12/6500/0.72) plus a run with holding period 5 — this is the before/after comparison set

## 2. CSS Changes

- [x] 2.1 Remove `max-width:920px` from the `.wrap` rule so the container fills the window; keep `margin:0 auto` or reduce the rule to nothing if it becomes empty
- [x] 2.2 Remove `max-width:60ch` from the `.sub` rule
- [x] 2.3 Remove `max-width:70ch` from the `footer p` rule
- [x] 2.4 Confirm no other `max-width` remains in the stylesheet that would still cap page width

## 3. Visual Verification

- [x] 3.1 At a window ~2560px wide: shared inputs, offers grid, verdict bar, and footer all span the window minus body padding; no horizontal scrollbar
- [x] 3.2 At ~2560px: header subtitle and both footer paragraphs wrap at the container edge, not near one offer-card width
- [x] 3.3 At ~1440px and ~900px: layout shrinks to fit with no horizontal overflow; Offer A and Offer B stay side by side as equal columns
- [x] 3.4 At ~390px (below the 640px breakpoint): shared inputs and offers each stack to one column, Offer A above Offer B, input font size still 16px
- [x] 3.5 Inspect readout rows on a widened offer card — labels left, values right, no mid-number wrapping; note any spacing that looks unacceptable

## 4. Behavior Verification

- [x] 4.1 Re-enter the task 1.1 inputs and confirm every computed figure and the verdict match the baseline exactly
- [x] 4.2 Confirm PMI rows, the "PMI ends" period, and holding-period rows still render correctly
- [x] 4.3 Open the file with JavaScript disabled and confirm the `noscript` warning block renders and reads correctly in the full-window container
- [x] 4.4 Check both light and dark color schemes for any layout artifact introduced by the widening
