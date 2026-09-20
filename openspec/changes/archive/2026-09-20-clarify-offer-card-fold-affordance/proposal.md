## Why

Offer card heading carries five accent-colored marks: top border, chevron, dot, title text, stepper
glyphs. Chevron and dot sit adjacent, same color, near-same size, and read as one ornament instead of
"control plus label". Fold affordance diluted by the decoration next to it.

Summary row has `cursor:pointer` and a focus outline but no hover state, so a pointer user gets no
feedback that the heading is live. That gap costs more discoverability than the dot does.

## What Changes

- Remove color dot from offer card heading. Accent identity still carried by top border, title text,
  stepper glyphs, focused-input outline.
- Add a hover state to the heading row: the chevron shifts to the card's accent and the card's border
  lights in the same accent, one weight heavier than resting. The title already rests at accent and
  does not change. Only the heading triggers it, not the card body. Hover is additive and gated to
  pointers that hover; the chevron stays the touch-and-keyboard affordance.
- Enlarge chevron from 6px, since it carries the affordance alone once the dot is gone.
- Recolor chevron from card accent to `--slate`, separating control chrome from offer identity.
  Evaluated against accent in both color schemes before locking; slate won, and reverting would still
  be one declaration.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `page-layout`: fold requirement drops the dot from the heading contents, sets chevron color to a
  neutral tone rather than the card accent, and adds a pointer-gated hover state that lights both the
  chevron and the card's border from the heading row only.
- `offer-set`: visual-distinction requirement drops the dot from the list of accent carriers.

## Impact

- `MortgageOfferAnalyzer.html` only: the offer-card heading's CSS and markup, the card's border and
  shadow rules, and a hover block beside the existing fold-summary rules.
- The clone path rewrites `">Offer A<"` per card; the `.name` span stays, so it keeps working.
- The chart's circle markers are a separate thing and are untouched.
- No JavaScript reads `.dot`. No share-link state, no computed figure, no test assertion depends on it.
