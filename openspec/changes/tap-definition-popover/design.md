## Context

`MortgageOfferAnalyzer.html` is one self-contained file — no build step, no dependencies, runs from `file://`. Definitions live once, in the footer `<dl class="glossary">`. `DEFS` reads them back out (line ~589) and `annotate(root)` (line ~602) copies the matching text into `el.title` for `.field label` and `.row .k`.

`title` needs hover. Touch devices do not hover. On a phone the footer glossary is the only path to a definition, several screens away from the row that raised the question.

Constraints:

- Minimalist visual design is the point of the tool. Any persistent marker on labels is a regression, per the user.
- Readout rows are rebuilt via `innerHTML` on every input change (`render()` line ~702, `annotate($("out"+i))` line ~800). Any listener bound to a row element dies on the next keystroke.
- Existing `term-glossary` spec already guarantees no visible marker shifts row layout. Keep it.

## Goals / Non-Goals

**Goals:**

- Definition reachable at the point of use on touch.
- Zero visual change at rest.
- Definitions keep one source.
- Smallest diff that holds: no library, no dependency, no new file.

**Non-Goals:**

- Replacing hover. Desktop keeps `title`, unchanged.
- Input labels. Out of scope, see decision below.
- Dismissal state, "seen the hint" persistence, onboarding flow.
- Anchoring the popover to the tapped element. Centred is fine and costs nothing.

## Decisions

### Native Popover API over a hand-rolled tooltip

`<div popover>` plus `showPopover()` gives top layer, light dismiss on outside click, and Escape dismiss with no code. A hand-rolled panel needs z-index management against `.card`, `.chart-wrap`, and `overflow` contexts, plus outside-click and Escape handlers.

Alternatives rejected:

- Reuse the existing `.tip` element (line ~187). It is `position:absolute` inside `.chart-wrap` and `white-space:nowrap`. Definitions are sentences. Reworking it risks the chart crosshair tooltip that already works.
- CSS anchor positioning to pin the popover to the tapped label. Not Baseline — Chrome only at time of writing. Centred popover needs no anchor.
- `<details>`/`<summary>` per row. Adds a disclosure triangle to every row. That is the marker the user rejected.
- Anchor link to the glossary entry. Scrolls the page away from the readout and loses the reader's place.

Browser floor: Popover API is Baseline (Chrome 114, Safari 17, Firefox 125). Guard with `if(!pop.showPopover) return;` so older browsers fall back to hover plus the footer glossary.

### One delegated listener on `document`

Rows are re-rendered constantly. Per-element listeners would have to be re-bound inside `annotate()` on every render. One `document` click listener with `e.target.closest(".row .k")` binds once and survives every re-render for free.

Handler shape:

```js
const el = e.target.closest(".row .k");
if (!el || !el.title || !pop.showPopover) return;
pop.textContent = el.title;
pop.hidePopover();       // no-op when closed; resets so a second tap re-anchors
pop.showPopover();
```

`hidePopover()` before `showPopover()` handles the "tap a second label while one is open" scenario without tracking state.

### Read from `el.title`, not from `DEFS`

`annotate()` already resolved the term for that element. Calling `defFor()` again in the click handler would re-run the substring scan and duplicate the matching rule. Reading `el.title` reuses the resolution and keeps the single source intact through one hop.

### Readout rows only; input labels excluded

A `<label for="pmi0">` click focuses its input. On mobile that opens the numeric keyboard. Opening a popover in the same gesture puts a panel and a keyboard on screen at once, both fighting for a small viewport. `preventDefault()` would fix the collision by breaking tap-to-focus, a worse trade.

Input labels are also the ones already explained: most carry inline `.hint` prose (`Holding period — years until you sell/refinance`), and their terms all reappear in readout rows or the glossary. Readout rows carry the dense, unexplained jargon — effective annual rate, amortization midpoint, cost to walk away — and are non-interactive, so there is no gesture to collide with.

### One static hint, touch-only, inside existing prose

`@media (hover:none)` on a `<span>` appended to the existing intro `<p class="sub">`. Default `display:none`, shown only under the media query, so pointer devices render exactly what they render today.

Rejected: `localStorage` "hint seen" flag. State, a write, and a dismissal control, to hide one sentence. The sentence is small enough to live there permanently.

## Risks / Trade-offs

- **No affordance means some readers never discover it.** → The hint sentence on touch, plus the footer glossary as the path that always worked. Accepted: an always-visible marker is the thing being avoided.
- **Reading `el.title` couples the popover to `annotate()` running first.** → Both are driven by the same render path; `annotate($("out"+i))` runs at line ~800 immediately after `render()`. Handler no-ops harmlessly if `title` is empty.
- **Centred popover is not anchored to the tapped row.** → Acceptable on phones, where a centred sheet is the native pattern anyway. Anchor positioning can be layered on when Baseline.
- **Popover overlays content while open.** → Light dismiss closes on any outside tap; no trap, no state to get stuck in.
- **Desktop click on a readout label now opens a popover too.** → Harmless; readout labels have no other click behaviour, and it gives touch-laptop users the same path. Hover text still fires first for mouse users.

## Migration Plan

Single file, no data, no deploy step beyond publishing the HTML. Rollback is reverting the commit.

## Open Questions

None blocking. Anchoring the popover to the tapped row is deferred until CSS anchor positioning is Baseline.
