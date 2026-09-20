## Why

Pressing [+] on an offer card inserts a card at the tool's defaults, discarding the work already done on the card the control sits in. Comparing variants of one offer — same rate and term, different fees, or same everything with a shorter term — is the common case, and today it costs a full re-entry of five fields.

## What Changes

- The add control copies the source card's current values into the inserted card instead of the tool's defaults. All five per-offer fields move: rate, term, payments per year, upfront fees, PMI rate.
- A locked PMI field copies its stashed rate, not its displayed `0`, so an unlock restores the source card's rate on both cards.
- Cards after the insert point keep shifting one position later; removal behavior unchanged.
- **BREAKING** for `offer-set`: the spec today requires the inserted card to hold default values. That requirement inverts.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `offer-set`: the add control's inserted card takes the source card's values, not the tool's defaults. Affects the offer-count stepper requirement and the value-preservation requirement, plus their scenarios.

## Impact

- `MortgageOfferAnalyzer.html`: `insertOffer()` only. `renderOffers()`, `removeOffer()`, `getVal`/`setVal`, and share-link restore stay as they are.
- `#selftest`: the assertion `"inserted card not at defaults"` inverts, plus one new case covering the locked-PMI stash copy.
- No new markup, no new state, no share-link format change.
