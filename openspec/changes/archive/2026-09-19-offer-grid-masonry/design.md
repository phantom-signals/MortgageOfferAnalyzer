## Context

`.offers` is a CSS grid with `align-items:start`. A 4-offer container query forces 2 columns in the 3-column band. Row height is set by the tallest card, so a folded card leaves a gap below it. Native masonry (`display:grid-lanes`) is not supported in Chrome 153 stable, so CSS alone can't close the gap.

Code assumes cards are direct children of `.offers`: `card0HTML`, the stepper handler, `renderOffers()`, `removeOffer()`, the per-card loop in `compute()`, and the selftests.

## Goals / Non-Goals

**Goals:**
- A card below the first row sits one gap under the card above it in its column.
- Cards never change column.

**Non-Goals:**
- Shortest-column placement. It moves cards sideways on fold.
- Animation. Add `transition:margin-top` later if the snap feels abrupt; the `prefers-reduced-motion` rule already covers it.
- Native `grid-lanes` enhancement. Add it once Chrome ships it.

## Decisions

**Negative `margin-top` on cards below row 1, grid and markup untouched.**

```js
function stackCards(){
  const cs = [...offers.children];
  cs.forEach(c => c.style.marginTop = "");
  const s = getComputedStyle(offers);
  const cols = s.gridTemplateColumns.split(" ").filter(t => parseFloat(t) > 0).length;
  const gap = parseFloat(s.rowGap);
  cs.forEach((c, i) => {
    if(i < cols) return;
    const above = cs[i - cols];
    c.style.marginTop = (above.offsetTop + above.offsetHeight + gap - c.offsetTop) + "px";
  });
}
```

- Grid auto-placement keeps DOM order, so column assignment is fixed: card i sits under card i − cols.
- A grid item's negative top margin shrinks its row's contribution, so the grid's own height, and everything below it, follows the taller column. No overlap with the cost bars.
- Margins are reset before measuring, so a stale margin never feeds the next pass. Cards are processed in order, so reading `offsetTop` after an earlier write sees rows above already placed.
- `auto-fit` reports collapsed tracks as `0px`; filtering them gives the real column count. At 1 column every margin comes out 0.
- Alternatives:
  - Per-column wrapper `<div>`s: break every direct-child assumption listed above.
  - CSS `columns`: fills top to bottom, so the order becomes A,B | C,D.
  - `grid-lanes`: unsupported in Chrome.

**`ResizeObserver` on each card triggers `stackCards`.**

- Fold toggle, width change, readout rows appearing, and font load all change card size, so one observer covers them all without a `toggle`, `resize`, or `compute()` hook.
- `renderOffers()` observes each new card; `observe()` on an already-observed card is a no-op, so observing every child after the add loop is fine. The first observation fires the callback, which covers count changes.
- Margin writes don't change a card's border box, so the callback doesn't retrigger itself.

## Risks / Trade-offs

- [Card removal where no remaining card resizes] With 2 columns at every count, stacking of the remaining cards is unchanged, so the margins stay correct. Calling `stackCards()` at the end of `renderOffers()` removes the case entirely at no cost.
- [Readout rows misalign across a row after a fold above] Intended. Comparison is per row, and a fold above already breaks it.
- [Script-driven layout] A JS error before `stackCards` runs leaves today's gapped layout. Acceptable degradation.
