## Context

Single-file tool, no build step, no dependencies. `MortgageOfferAnalyzer.html` holds markup, CSS, and script.

Current state of the pieces this change touches:

- `.shared` is `display:grid` with `grid-template-columns:1fr 1fr` and two `.shared-col` flex children ([:99-104](../../../MortgageOfferAnalyzer.html#L99-L104)). Left holds three fields, right holds two. The card's height is the taller column, so the right column ends in a field-sized run of empty card.
- `compute()` already parses `P` and `hv` at the top and calls `pmiOwed(P, hv)` before the offer loop ([:877-890](../../../MortgageOfferAnalyzer.html#L877-L890)).
- `pmiOwed = (P,hv) => hv>0 && P>0 && P/hv > 0.80 + 1e-12` ([:619](../../../MortgageOfferAnalyzer.html#L619)) is the single source for "does this loan owe PMI", read by both `calc()` and the input lock.
- `render()` prints `Initial LTV` per offer from `res.initialLTV` ([:793](../../../MortgageOfferAnalyzer.html#L793)), computed as `P/hv` inside `calc()` ([:745](../../../MortgageOfferAnalyzer.html#L745)). `P` and `hv` are shared, so all cards print the same number.
- `annotate(root)` sets `title` from the footer glossary on `.field label, .row .k, #costTable .k`, skipping anything that already has a `title` ([:679-686](../../../MortgageOfferAnalyzer.html#L679-L686)). `annotate(document)` runs from `renderOffers()` ([:833](../../../MortgageOfferAnalyzer.html#L833)), so shared-card elements are already covered.
- The popover delegate matches `.row .k, #costTable .k` ([:691](../../../MortgageOfferAnalyzer.html#L691)). Input labels are excluded on purpose: clicking one focuses its control.
- `INPUTS = "input.inp, select.inp"` drives both `serialize()` and `restore()` ([:622-626](../../../MortgageOfferAnalyzer.html#L622-L626)).

## Goals / Non-Goals

**Goals:**

- Fill the shared card's bottom-right hole with a figure worth the space.
- Print initial LTV once, from the inputs that define it.
- Keep hover and tap definitions for LTV after the per-offer row is gone.
- Make the PMI lock self-explanatory: say why the rate inputs read 0 and refuse edits.

**Non-Goals:**

- No down-payment or equity figure. `homeValue - amount` is not reliably a down payment.
- No new LTV math. `P/hv` and `pmiOwed` already exist; reuse both.
- No change to `calc()`. `res.initialLTV` stays on the result object; only its rendering moves.
- No restyling of the card, columns, gaps, or any input.

## Decisions

### Readout is a `div`, not a disabled input

A disabled `input.inp` would look consistent for free, but `INPUTS` sweeps every `.inp` into the share hash and `restore()` writes any matching key back. A readout in the hash is junk state that a crafted link could target.

Markup sits as the last child of the right `.shared-col`:

```html
<div class="field readout">
  <span class="lbl">Initial LTV</span>
  <div class="val" id="ltvOut">&mdash;</div>
</div>
```

`.field` is reused for the label-over-value stack and its 6px gap, so column rhythm matches the inputs above with no new layout rule. `.lbl` copies the `.field label` type rules; `.val` is mono at 14px with no border or background, so it reads as output rather than an empty input.

Alternatives: `<output>` (correct semantics, but it carries form-association baggage and needs the same styling work); reusing the `.row` readout style from the cards (borrows a grid meant for label-left/value-right rows, wrong shape in a column of stacked fields).

### Value is written in `compute()`, from shared inputs

One line in `compute()`, after `pmiRequired` is computed and before the offer loop:

```js
const ltv = hv > 0 && P > 0 ? pct(P/hv) + " — " + (pmiRequired ? "PMI required" : "no PMI required") : "—";
```

Sourcing from shared inputs, not `res.initialLTV`, means the readout survives an offer with a blank rate — `calc()` returns `null` there and the card prints "Enter valid inputs", but LTV is still well defined. Reusing `pmiRequired` rather than re-testing the ratio guarantees the tail and the input lock agree; they are the same boolean.

`pct()` already formats 2 to 3 decimals ([:703](../../../MortgageOfferAnalyzer.html#L703)), so 400000/450000 reads 88.89%.

The guard is `hv > 0 && P > 0`, matching `pmiOwed`'s own guard. `NaN > 0` is false, so blank and non-numeric inputs fall to the em dash without a separate `Number.isFinite` check.

### Definition access: extend two selectors

`annotate()` gains `.shared .readout` in its selector list, so the whole readout block takes the `title`. Matching on the block rather than the label means hovering the value works too, and the title survives every value re-write because only `#ltvOut`'s text changes, never the block's attributes.

`defFor()` lowercases and substring-matches, so the block's text "Initial LTV 88.89% — PMI required" hits the `initial ltv` entry. That entry precedes `ltv|loan-to-value` in the glossary, and first match wins ([:481](../../../MortgageOfferAnalyzer.html#L481)), so ordering already holds — no glossary edit.

The popover delegate gains `.shared .readout` for the same reason. The existing exclusion of `.field label` is about labels that focus a control; the readout has no control to focus, so tapping it has no native behavior to preserve.

### Per-offer row deleted, `res.initialLTV` kept

Delete only the `render()` line. `initialLTV` stays on the result object: it costs one division already performed, and stripping it from `calc()` would touch the math for no gain.

### Self-test repointed

[:1291-1292](../../../MortgageOfferAnalyzer.html#L1291-L1292) locates the tooltip witness by scanning `#out0 .row .k` for "Initial LTV" — the row this change removes, so the test fails until repointed at `.shared .readout`. Two assertions to add beside it, both cheap and both guarding a trap above: the readout's text tracks the PMI lock state of `#pmi0`, and `serialize()` yields no key for the readout.

## Risks / Trade-offs

- Readout text feeding `defFor()` by substring is order-sensitive: a future label containing "ltv" before the specific entry would resolve wrong. → Already the documented contract at [:481](../../../MortgageOfferAnalyzer.html#L481); the self-test asserts the resolved title, so a regression fails loudly.
- Extending the popover delegate to a non-row element widens what a tap can open. → Delegate still requires a `title`; an element without a glossary match opens nothing, unchanged.
- The tail states a model conclusion ("PMI required") in the input area rather than the results. → Wording names the 80% LTV threshold condition only, which is what `pmiOwed` tests; the footer PMI paragraph and the glossary carry the HPA rules and their caveats, and neither is touched.
- The corrected `page-layout` column wording changes a requirement that code already satisfies, so the delta looks larger than the diff. → Called out in the proposal; no code moves for it.
- Columns balance at three items each only while both hold three. → Stated as a requirement so a future field addition has to pick a column deliberately; the markup comments already direct new fields into a group.

## Migration Plan

Single file, no state, no persistence. Ship in one edit; revert is `git revert`. Old share links keep working: no key is added or removed, and an ignored unknown key was already the defined behavior.

## Open Questions

None.
