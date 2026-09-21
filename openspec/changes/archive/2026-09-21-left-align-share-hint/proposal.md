## Why

Disclosure text under the copy-link control inherits `text-align:center` from `.share`. On a narrow viewport it wraps to three or four lines, each centered, producing a ragged-both-edges block that reads worse than the footer prose beside it. Centered alignment suits a one-line caption, not a wrapped paragraph.

## What Changes

- Left-align the share disclosure text while the copy-link button stays centered.
- The text block itself stays horizontally centered under the button (`max-width:52ch; margin:6px auto 0` unchanged); only the alignment of lines inside it changes.
- Justified alignment rejected: at 52ch and narrower it stretches word gaps and opens rivers on mobile, worse than the ragged right it replaces.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `page-layout`: add a requirement that wrapped prose under the copy-link control is left-aligned, with the control itself still centered. Sits with the other text-presentation requirements in that spec; `share-link` keeps owning the control's behavior and the fact that disclosure text exists.

## Impact

- `MortgageOfferAnalyzer.html`, `.share .hint` rule in the inline stylesheet. One declaration.
- No script, no state, no serialization. Copy-link behavior unchanged.
- `math.html` unaffected; it carries no `.share` block.
