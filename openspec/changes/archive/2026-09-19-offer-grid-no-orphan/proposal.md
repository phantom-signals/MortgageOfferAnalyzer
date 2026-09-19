## Why

Offers grid uses `repeat(auto-fit,minmax(260px,1fr))`, which counts widths, not cards. At 4 offers and mid-desktop widths (~816–1094px of grid), grid renders 3+1: Offer D alone on second row. Grid items also stretch to row height, so folded card beside open card becomes tall empty box.

## What Changes

- 4 offers render 4 columns or 2×2, never 3+1. At grid widths where auto-fit would pick 3 columns, 4-offer grid uses 2.
- 1–3 offers keep current auto-fit wrapping. 3 offers at mid widths may render 2+1; accepted.
- Phone layout (≤640px) unchanged. Landscape phone above 640px follows desktop rules, so 4 offers render 2×2.
- Offer cards take own content height (`align-items:start`). Folded card no longer stretches to match open neighbor. Gap below short card in mixed row accepted.
- No card reordering. CSS `order` grouping of folded cards is noted fallback, out of scope.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `page-layout`: "Offer cards share the available width equally" rewritten. Cards wrap by width; 4 offers skip 3-column arrangement; cards keep own height. "Column count follows offer count" scenario replaced. New scenario for folded-card height.

## Impact

- `MortgageOfferAnalyzer.html` CSS only: `.offers` rule plus one container query. No markup, no script, no computed-value change.
