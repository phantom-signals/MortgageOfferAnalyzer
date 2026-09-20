## Why

Removing the offer-count dropdown left the shared-input card with three fields in the left column and two in the right, so the card carries a field-sized hole at bottom right. Separately, "Initial LTV" prints once per offer card, but it derives from loan amount over home value — both shared — so every card shows the same number. One figure fills the hole and ends the duplication.

## What Changes

- Add a read-only "Initial LTV" readout as the last item in the shared card's right column. Shows the ratio as a percent, plus a tail naming whether PMI applies.
- Remove the per-offer "Initial LTV" readout row. Its value was identical across cards.
- Readout reads shared inputs directly in `compute()`, not `res.initialLTV`, so it holds a value even when an offer's own fields are blank or invalid.
- Readout is a `div`, never `input.inp`, so `serialize()` and `restore()` never see it.
- PMI tail reuses `pmiOwed(P, hv)`, the same predicate that locks the per-card PMI rate inputs, so readout and lock can never disagree.
- Extend the definition-popover delegate to `.shared .readout`, so touch readers keep tap-to-define for LTV after the row leaves the cards.
- No down-payment figure. `homeValue - amount` is not reliably a down payment (second lien, seller concessions), and the page makes no such inference elsewhere.
- Correct drift in `page-layout`: the spec still describes home value in the right column and the left column as loan amount then holding period. Code has held the current arrangement since commit ef78bde.

## Capabilities

### New Capabilities
- `shared-ltv-readout`: content, placement, PMI tail, empty-input behavior, and exclusion from the share hash for the shared card's LTV readout.

### Modified Capabilities
- `page-layout`: shared-card column contents gain the readout as the right column's last item; mobile stacking order gains it as the final entry.
- `term-glossary`: LTV hover and tap witnesses move from the offer readout row to the shared readout; the readout is neither a row label nor an input label, so its definition access needs stating.
- `offer-set`: the count-1 readout inventory no longer lists initial LTV; the figure moves to the shared card.

No `share-link` delta. Its existing requirement already forbids hash keys for readout elements, and a `div` satisfies it.

## Impact

- `MortgageOfferAnalyzer.html`: shared-card markup, one `.readout` CSS rule, `compute()` (set readout), `render()` (drop row), `annotate()` selector, popover delegate selector, self-test at the LTV tooltip assertion.
- Self-test `#selftest` asserts the LTV tooltip by querying `#out0 .row .k`. Must repoint at the shared readout or it fails.
- Glossary needs no edit. The `initial ltv` entry and the specific-before-general ordering against `ltv` stay as they are.
