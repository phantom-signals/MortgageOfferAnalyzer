## 1. Verdict placement

- [x] 1.1 Move `#verdict` markup below the shared-input card, above the offers grid; leave `verdict()` and its `hidden` handling untouched
- [x] 1.2 Check spacing at 390px and 1280px: verdict reads as the answer, not as a card header

## 2. Card readout fold

- [x] 2.1 In the Offer A template, wrap `#out0` in `<details class="fold"><summary>…</summary></details>`; `cardHTML()`'s id rewrite must carry the summary id to B/C/D
- [x] 2.2 Set default state at card creation in `renderOffers()`: open above 640px, closed at 640px and below, one `matchMedia("(max-width:640px)")` read; mark the no-re-decide-on-rotate ceiling with a `ponytail:` comment
- [x] 2.3 Fill the summary in `compute()`: payment incl. PMI (first period) and headline total — `costToClear` with a holding period, `totalCost` without
- [x] 2.4 Style `summary` and the fold marker: readable collapsed, unobtrusive when open

## 3. Component labels and formatting

- [x] 3.1 Give `SEGS` a second label for no-horizon mode (`{k, kTerm}`, fall back to `k`): "Total interest", "Total PMI", "Upfront fees", "Principal"
- [x] 3.2 Add `moneyK()` beside `money()`: thousands form (`$252.5k`), component cells only, 640px and below

## 4. Comparison table

- [x] 4.1 Add `<div id="costTable">` inside the bars' `.chart-wrap` below `#bars`; give the section heading an id so `drawBars()` can set its text
- [x] 4.2 In `drawBars()`, emit the table from the `rows[]` it already builds: header of offer letters in `accentOf(i)`, one row per component, total row last
- [x] 4.3 Skip a component row when `rows.every(r => !(r.amts[j] > 0))`, so columns stay aligned across offers
- [x] 4.4 Put the swatch in each component label cell from `SEGS[j].c` against offer A's accent; delete `breakdownHTML()`, its call site, and the `.breakdown` CSS, keeping `.sw`
- [x] 4.5 Drive heading text, total row label, and component labels from `useHorizon`: "Cost to walk away" / "Cost to term"
- [x] 4.6 Rewrite the section hint as the glossary definition of the headline figure (cost to walk away / total cost), set in `drawBars()` via `defFor()` alongside the heading
- [x] 4.7 Clear `#costTable` and the heading on the existing empty-state path when no offer computes

## 5. Fitting a phone

- [x] 5.1 Use `moneyK()` for component cells at 640px and below, `money()` for the total row at every width
- [x] 5.2 Wrap the table in an `overflow-x:auto` container, make label cells `position:sticky; left:0`
- [x] 5.3 Verify at 390px with 4 offers: no horizontal page scrollbar, label column stays put, total row exact

## 6. Glossary reach

- [x] 6.1 Widen the `annotate()` selector and the tap-popover delegation from `.row .k` to `.row .k, #costTable .k`
- [x] 6.2 Call `annotate($("costTable"))` in `compute()` after the table is written
- [x] 6.3 Confirm every label the table prints resolves through `defFor()` in both modes, flipped to-term wording included

## 7. Self-test

- [x] 7.1 Replace the `.breakdown .sw` assertion: `#costTable .sw` exists, one value column per displayed offer, Offer A's total cell equals `money(hData.costToClear)` for the test inputs
- [x] 7.2 Assert `#out0` no longer contains "Cost to walk away", and that a component row disappears when its amount is zero for every offer
- [x] 7.3 Run the page, confirm the in-page self-test passes

## 8. Verification pass

- [x] 8.1 Same inputs before and after: payment, EAR, LTV, PMI figures, total cost, holding-period figures, verdict all identical
- [x] 8.2 Toggle the holding-period field: heading, total label, component rows flip both directions
- [x] 8.3 Offer count 1 to 4: columns appear and vanish with no empty placeholder; verdict hides at 1
- [x] 8.4 Hover a bar segment against its table cell; tap a table label for the definition popover
