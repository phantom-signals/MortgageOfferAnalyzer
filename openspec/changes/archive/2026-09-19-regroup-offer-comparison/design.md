## Context

Single file, `MortgageOfferAnalyzer.html`, no build step, no dependencies. Every input event runs
one `compute()`: per offer `calc()`, optionally `horizon()`, `render()` into `#out<i>`, then
`drawBars()`, `drawChart()`, `verdict()`.

Two facts drive this design:

- `render()` replaces `#out<i>.innerHTML` on every keystroke. Anything stateful inside that string
  dies on each edit.
- `drawBars()` already computes per offer `amts` (from `segAmounts()`) and `total`. Table is that
  same array rendered second way. No new computation, no second source of truth.

Pieces already present: `SEGS` (component colors and labels), `accentOf(i)`, `money()`,
`defFor()`/`annotate()`, and a resize handler that redraws graphics.

## Goals / Non-Goals

**Goals:**

- Verdict before detail, comparison before per-offer walls.
- One color key on page, not one per card.
- 4 offers legible at 390px, no horizontal page scroll.
- No computed figure changes.

**Non-Goals:**

- No change to `calc()`, `horizon()`, `segAmounts()`, `verdict()`, cost-over-time chart.
- No transposed mobile table. 5 money columns do not fit 390px, and transposed restates bar
  geometry.
- No removal of card readout rows. Card and table repeat by design.
- No new dependency, no build step, no framework.

## Decisions

### Fold wrapper in card template, not in `render()` output

`<details>` wraps `#out<i>`, both in markup `cardHTML()` clones. `render()` keeps writing rows into
`#out<i>` only. Disclosure element never re-created by an edit, so open/closed state survives
re-render free. No state stash, no `dataset` bookkeeping.

Rejected: emit `<details>` from `render()`, restore `open` from a stash each keystroke. More code,
fights browser for state browser already holds.

### Native `<details>`, open state decided once at card creation

`matchMedia("(max-width:640px)").matches` at creation decides whether element gets `open`. No JS
toggling, no CSS hack to force `open`. Widget is native and keyboard-accessible, needs no script.

Ceiling, marked with `ponytail:` comment: rotating a phone after load does not re-decide the
default. Rare, reader can tap. Upgrade path is one line in existing resize handler.

Rejected: CSS-only forcing above 640px. Depends on `::details-content` support, fights UA behavior,
gains nothing over one `matchMedia` read.

### Table built inside `drawBars()`

`drawBars()` already builds `rows[] = {o, amts, total}` and knows `useHorizon`. Emits SVG into
`#bars`, now also table into sibling `#costTable`, and sets heading text. One function owns the
section, one pass over data, existing empty-state path covers both.

Table is real `<table>`: header row of offer letters, one `<tr>` per surviving component, total row
last. Row survives when `rows.some(r => r.amts[j] > 0)` — across offers, not per card, so columns
stay aligned.

### Mode flip from one flag

`useHorizon` already reaches `drawBars()`. Selects heading text, total row label, and which label
each component row carries. `SEGS` entries gain second label for blank holding period
(`{k, kTerm}`, fall back to `k`), so "Interest paid" reads "Total interest" at term. Exact labels
also keep glossary matches working.

### Abbreviation at 640px and below, total row always exact

New `moneyK()`: `$252.5k` for component cells when `matchMedia("(max-width:640px)").matches`. Total
row keeps `money()`. Existing resize handler already redraws graphics, so width changes
re-evaluate this. No new listener.

Arithmetic: 390px viewport leaves ~326px inside the chart box. Exact dollars need ~95px per column,
so 4 offers plus label column overflow. Abbreviated cells need ~60-70px, which fits. Exact figures
stay one tap away in card readouts and bar hover text, so no figure leaves the page.

### Sticky label column, scroll inside box

`overflow-x:auto` on a wrapper, `position:sticky; left:0` on label cells. Covers widths
abbreviation does not. Keeps page free of horizontal scrollbar, which `page-layout` requires at
every width.

### Color key uses offer A's ramp

Bar segments are tinted per offer: `SEGS` colors express against `var(--accent)`, each bar row sets
it to its own accent. One shared key cannot match 4 bars, so key column renders with offer A's
accent. Same component, same ramp position in every bar, so the mapping is self-evident; no caveat
text.

### Section hint defines the figure

Hint under the heading gives the glossary definition of the headline figure — cost to walk away,
or total cost at term — read through `defFor()` and set in `drawBars()` with the heading. "Cost to
term" would match the Term entry, so the to-term lookup uses "total cost".

Rejected: neutral gray ramp. Matches no bar, and gray reads as a sixth component.

### Glossary reaches table by widening one selector

`annotate()` and tap-popover delegation both select `.row .k`. Both become
`.row .k, #costTable .k`, and `compute()` calls `annotate($("costTable"))` after the table is
written. Every term the table prints already has a `data-match` entry, so no definition text is
added or duplicated.

### Verdict move is DOM-only

`#verdict` element moves above offers grid in markup. `verdict()`, ranking, and `hidden` at offer
count 1 untouched.

## Risks / Trade-offs

- Folded readouts hide figures desktop readers expect → fold defaults open above 640px, desktop
  view unchanged, summary always carries payment and headline total.
- Abbreviated cells read as the tool's precision → total row exact, exact component figures stay in
  card readouts and bar hover text at every width.
- One key cannot match 4 tinted bars → component order and ramp position are identical in every
  bar, which is what the key encodes; the per-offer tint reads as self-evident.
- Card and table print the same numbers → accepted deliberately, both read `segAmounts()`, cannot
  drift.
- Self-test asserts `.breakdown .sw`, which this change deletes → assertion replaced in same
  commit, so the test never passes against a half-done state.
- Phone rotation does not re-decide fold default → named as `ponytail:` comment with one-line
  upgrade path.
