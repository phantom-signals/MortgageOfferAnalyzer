## 1. Implementation

- [x] 1.1 In `insertOffer()` in `MortgageOfferAnalyzer.html`, splice `rows[i].slice()` into position `i + 1` instead of reading the appended clone with `fieldsOf(offers.lastElementChild).map(getVal)`
- [x] 1.2 Update the comment above `insertOffer()` — it currently says the clone is "read back for its default values", which stops being true

## 2. Self-test

- [x] 2.1 In the `#selftest` insert case, invert the `"inserted card not at defaults"` assertion: with `rate0` at 6.1, pressing card 0's plus makes `rate1` read 6.1, and the shift assertion on `rate0`/`rate2`/`rate3` stays as it is
- [x] 2.2 Extend that case to assert every field copies, not just the rate: set `term0`, `freq0`, `fees0`, `pmi0` before the press, assert the inserted card matches on all five
- [x] 2.3 Add a locked-PMI case: lock PMI via `homeValue`, set the source card's `dataset.prev`, press its plus, assert the inserted card's stash carries the source rate and its displayed value is `0`; unlock and assert both cards show the source rate
- [x] 2.4 Confirm the existing `renderOffers()` default-value assertion at `"rate1 not default"` still passes untouched — it covers the non-add-control path the spec still requires to be defaults

## 3. Verify

- [x] 3.1 Run `#selftest` headless and confirm every check passes
- [x] 3.2 Run `openspec validate clone-offer-on-insert --strict`
