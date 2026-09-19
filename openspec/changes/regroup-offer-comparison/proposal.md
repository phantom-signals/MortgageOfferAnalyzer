## Why

Bar chart left every figure printed twice per card: readout rows, then swatch list repeating
interest, PMI, remaining balance right under them. Worse on phone, where cards stack: comparing 4
offers means scrolling past 4 walls of ~13 rows before first side-by-side view. Verdict — answer
page exists to give — sits last, below both charts.

Regroup page around comparison: verdict first, per-offer detail folded, one table under bars.

## What Changes

- Verdict block moves above offers grid, under shared-input card. Same element, same `verdict()`,
  same `hidden` at offer count 1.
- Card readout collapses into `<details>` fold. Summary carries payment incl. PMI (first period)
  and headline total — cost to walk away with holding period, total cost to term without. Open
  above 640px, closed at 640px and below.
- Per-card swatch list (`breakdownHTML`) removed. Its job — color key for bars — moves to shared
  table.
- New table under bars: components as rows, offers as columns, swatch in label column, total row
  last. Sums already computed by `drawBars`.
- Heading and total row follow holding-period input: "Cost to walk away" when set, "Cost to term"
  when blank.
- Table fits 4 offers at 390px: component values abbreviate to `$252.5k` at 640px and below, total
  row exact, label column sticky, box scrolls instead of page.
- Card keeps its rows, exact figures included. Card-table repetition deliberate: card is one offer
  in full, table is all offers side by side.

## Capabilities

### New Capabilities
- `cost-comparison`: section under bars — table, shared color key, walk-away vs to-term mode, how
  it fits 4 offers on a phone.

### Modified Capabilities
- `page-layout`: verdict above offers grid; readouts fold at 640px and below; no horizontal page
  scrollbar when table overflows.
- `term-glossary`: definitions reach table labels, hover and tap, same as readout rows.

## Impact

- `MortgageOfferAnalyzer.html` only. Single file, no build step, no dependencies.
- Touched: `render()`, `breakdownHTML()` (deleted), `drawBars()`, `annotate()`, tap-popover
  delegation, card template, `.breakdown` CSS, verdict markup position.
- `calc`, `horizon`, `segAmounts`, `verdict` untouched. No computed value changes.
- In-page self-test asserts `.breakdown .sw`. That assertion gets replaced.
