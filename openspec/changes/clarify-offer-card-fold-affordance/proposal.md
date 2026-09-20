## Why

Offer card heading carries five accent-colored marks: top border, chevron, dot, title text, stepper
glyphs. Chevron and dot sit adjacent, same color, near-same size, and read as one ornament instead of
"control plus label". Fold affordance diluted by the decoration next to it.

Summary row has `cursor:pointer` and a focus outline but no hover state, so a pointer user gets no
feedback that the heading is live. That gap costs more discoverability than the dot does.

## What Changes

- Remove color dot from offer card heading. Accent identity still carried by top border, title text,
  stepper glyphs, focused-input outline.
- Add hover state to fold summary: chevron and title shift, so the row reads as a control under a
  pointer. Hover is additive only; chevron stays the touch-and-keyboard affordance.
- Enlarge chevron from 6px, since it carries the affordance alone once the dot is gone.
- Recolor chevron from card accent to `--slate`, separating control chrome from offer identity.
  Reversible: an evaluation step compares slate against accent at both color schemes before the
  choice is locked. Accent wins, revert that one declaration; nothing else in the change depends on it.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `page-layout`: fold requirement drops the dot from the heading contents, sets chevron color to a
  neutral tone rather than the card accent, sets a hover state on the summary row.
- `offer-set`: visual-distinction requirement drops the dot from the list of accent carriers.

## Impact

- `MortgageOfferAnalyzer.html` only. CSS at lines 143-149 and 176-184, markup at line 418.
- Clone path at line 832 rewrites `">Offer A<"` per card; `.name` span stays, so it keeps working.
- Chart circles at lines 1102-1190 are a separate thing and are untouched.
- No JavaScript reads `.dot`. No share-link state, no computed figure, no test assertion depends on it.
