## Why

Collapsed offer card still shows five inputs plus two summary figures. Stacked on phone, four offers still eat whole screens. Collapsed card should shrink to heading plus one number: payment.

## What Changes

- Disclosure control moves up: wraps card's inputs and readout, not readout alone.
- Collapsed card shows heading (dot, name, steppers) and summary line only.
- Summary drops headline total. Only figure left: payment including PMI for first period.
- Initial open/closed rule unchanged: collapsed at 640px and below, expanded above.
- Open state still survives re-render after input edit.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `page-layout`: requirement "Card readouts fold on small viewports" changes. Fold covers inputs too; summary shows payment only.

## Impact

- `MortgageOfferAnalyzer.html`: offer card markup (`details.fold` placement), `.fold` CSS, summary render in `compute()`.
- Clone path (`card0HTML`) unaffected in shape; clones inherit new structure.
- Verdict, charts, cost table, share link, shared inputs: unchanged.
