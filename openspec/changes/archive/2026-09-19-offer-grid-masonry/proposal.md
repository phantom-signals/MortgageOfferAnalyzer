## Why

Offer cards now take their own height, but grid rows still size to the tallest card. In 2-column layouts (4 offers as 2×2, 3 offers as 2+1), a folded card leaves a gap before the card below it. Comparison only makes sense within a row, and a folded card already breaks that row's comparison, so the gap buys nothing.

## What Changes

- In multi-row layouts, each card sits directly under the card above it in the same column, one grid gap below it. Cards slide up; they never change column.
- Column assignment stays DOM order: A and C on the left, B and D on the right at 2 columns.
- Readout rows line up across a row only when every card in that row, and every card above them, is expanded.
- No animation; the slide snaps.
- Single-row and single-column layouts are unchanged.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `page-layout`: "Offer cards share the available width equally" gains a slide-up scenario. "Open cards still line up" is narrowed to rows where every card above is also expanded.

## Impact

- `MortgageOfferAnalyzer.html`: one small layout function plus a `ResizeObserver`, and a one-line hook in `renderOffers()`. First script used for layout. One selftest check.
