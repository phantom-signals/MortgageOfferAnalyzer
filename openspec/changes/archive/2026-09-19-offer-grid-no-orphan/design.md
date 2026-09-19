## Context

`.offers` at `MortgageOfferAnalyzer.html:116`:

```css
.offers{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(260px,100%),1fr));gap:18px}
```

Column count from auto-fit, by grid width W:

- W < 538: 1 column
- 538 ≤ W < 816: 2 columns
- 816 ≤ W < 1094: 3 columns (4 offers give 3+1)
- W ≥ 1094: 4 columns

(`n×260 + (n−1)×18`.) Only 4 offers in the 816–1094 band are wrong. Everything else is already right.

`.offers` is a direct child of `body`. Body padding is `clamp(16px,4vw,48px)` (14px at ≤640px), so a viewport media query can't hit the grid-width breakpoints exactly.

Grid default `align-items:stretch` makes a folded card as tall as the tallest card in its row.

## Goals / Non-Goals

**Goals:**
- 4 offers never render 3+1.
- Folded cards take their own height.

**Non-Goals:**
- Reordering or masonry packing. Fallback if gaps annoy: `.offer:has(> .fold:not([open])){order:1}`.
- 3 offers at mid width (2+1 accepted).
- Fixing the existing mismatch where viewports around 566–640px get 2 columns despite the spec's phone single-column wording. Real phones are narrower. Untouched.

## Decisions

**Container query on `body`, range 816–1094px only.**

```css
body{container-type:inline-size}
@container (816px <= width < 1094px){
  .offers:has(> .offer:nth-child(4)){grid-template-columns:repeat(2,1fr)}
}
```

- Body content box equals the `.offers` width, so the breakpoints are exact. No padding math.
- One override band. auto-fit already gives 4 columns above the band and 2 or 1 below it.
- `:has(> :nth-child(4))` detects the card count with no JS. `renderOffers()` needs no class toggle.
- Alternatives:
  - Viewport media query: the breakpoint drifts with `4vw` padding.
  - A wrapper `<div>` as container: an extra markup change for no gain.
  - JS `data-count` attribute: needs a script edit, and CSS already covers it.
- `container-type:inline-size` on `body` adds inline-size and style containment only, not layout containment. `position:fixed` and the `#defPop` popover (top layer) are unaffected. Body width already comes from the viewport, not its content.

**`align-items:start` on `.offers`.** One declaration. Folded cards shrink to heading plus summary. Open cards stay equal height because readout rows drop only when no offer has them (`compute()` near line 921), so rows still line up.

## Risks / Trade-offs

- [Gap below folded card in a mixed row] Accepted. Option A (`order`) is the fallback.
- [`:has()` / container query support] Supported in current Safari, Chrome, and Firefox. On an older browser the rule is ignored and the grid falls back to today's 3+1. Acceptable degradation.
- [Breakpoints hardcode 260/18] If the card minimum or gap changes, the 816/1094 values must change too. Comment next to the query says so.
