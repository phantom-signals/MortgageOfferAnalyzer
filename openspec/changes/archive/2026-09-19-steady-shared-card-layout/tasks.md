## 1. Shared card columns

- [x] 1.1 In `MortgageOfferAnalyzer.html`, wrap the five `.shared` fields in two `<div class="shared-col">` elements: first holds `amount` and `horizon`, second holds `homeValue`, `pmiThresh`, `pmiBasis` in that order. Comment names the two groups.
- [x] 1.2 Add `.shared-col{display:flex;flex-direction:column;gap:16px}` beside the `.shared` rule; `.shared` keeps `grid-template-columns:1fr 1fr` and its `16px 24px` gap.
- [x] 1.3 Confirm the `@media (max-width:640px)` `.shared{grid-template-columns:1fr}` rule still stacks all five fields in document order; no new mobile rule unless spacing breaks.

## 2. Input size keyed to pointer, not width

- [x] 2.1 Change `.inp` `font-size:15px` to `font-size:14px`; padding stays `9px 11px`.
- [x] 2.2 Delete the whole `.inp` line from `@media (max-width:640px)`, so that block no longer touches inputs.
- [x] 2.3 Add `@media (pointer:coarse){.inp{font-size:16px;padding:12px 12px}}` near the `.inp` rule, carrying the comment that 16px stops mobile browsers auto-zooming on focus.

## 3. Verify

- [x] 3.1 Load the page at 1280px: PMI removal rule sits directly above PMI premium basis in the right column, under home value; left column holds loan amount above holding period.
- [x] 3.2 Drag the window from 1280px through 640px to 400px with a mouse: input text and input box height never change; at 400px fields stack as loan amount, holding period, home value, PMI removal rule, PMI premium basis.
- [x] 3.3 In device emulation with touch enabled (or on a phone), confirm inputs render 16px with the roomier padding, and focusing a field does not zoom the page.
- [x] 3.4 Run the page self-test (`#selftest`) and confirm every figure, the PMI rate lock at 80% LTV, and the glossary label mapping are unchanged.
