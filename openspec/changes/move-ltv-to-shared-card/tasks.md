## 1. Markup and style

- [ ] 1.1 Add `<div class="field readout">` with a `.lbl` reading "Initial LTV" and a `.val` with id `ltvOut` defaulting to an em dash, as the last child of the right `.shared-col` in `MortgageOfferAnalyzer.html`
- [ ] 1.2 Add `.readout .lbl` and `.readout .val` rules beside the existing `.field` rules: label matches `.field label` type, value is mono 14px, no border, no background, no `inp` class anywhere in the block
- [ ] 1.3 Confirm the readout renders with the em dash and no script errors with JavaScript disabled

## 2. Value and PMI tail

- [ ] 2.1 In `compute()`, after `pmiRequired` and before the offer loop, write `#ltvOut` from `P` and `hv`: `pct(P/hv)` plus " — PMI required" or " — no PMI required" taken from `pmiRequired`
- [ ] 2.2 Guard with `hv > 0 && P > 0` so blank and non-numeric inputs give an em dash with no tail
- [ ] 2.3 Remove the `Initial LTV` row from `render()`; leave `res.initialLTV` on the result object and `calc()` untouched

## 3. Definitions

- [ ] 3.1 Add `.shared .readout` to the `annotate()` selector list
- [ ] 3.2 Add `.shared .readout` to the popover delegate's `closest()` selector
- [ ] 3.3 Verify the resolved title is the "Initial LTV" glossary entry, not the general "LTV (loan-to-value)" entry; make no glossary edit

## 4. Self-test

- [ ] 4.1 Repoint the LTV tooltip assertion from `#out0 .row .k` to the shared readout, keeping the `/loan-to-value/i` check on its title
- [ ] 4.2 Assert no offer readout contains a row labelled "Initial LTV"
- [ ] 4.3 Assert the readout tail agrees with the lock state of `#pmi0` at 400000/450000 (PMI required, input editable) and at 400000/500000 (no PMI required, input locked at 0)
- [ ] 4.4 Assert `serialize()` produces no key for the readout
- [ ] 4.5 Assert a cleared home value gives an em dash with no tail
- [ ] 4.6 Run `#selftest` and confirm every assertion passes

## 5. Layout check

- [ ] 5.1 At 1280px, confirm three items per column and no field-sized empty run at the bottom of either column
- [ ] 5.2 At 390px, confirm the single-column order: home value, loan amount, holding period, PMI removal rule, PMI premium basis, initial LTV readout
- [ ] 5.3 Confirm readout spacing below PMI premium basis matches the gap between the fields above it
