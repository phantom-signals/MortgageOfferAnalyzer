## 1. Markup

- [ ] 1.1 Re-suffix Offer A's ids from letter to index: `rateA`→`rate0`, `termA`→`term0`, `freqA`→`freq0`, `feesA`→`fees0`, `pmiA`→`pmi0`, `outA`→`out0`, updating each matching `for=` attribute
- [ ] 1.2 Delete the hardcoded Offer B card block
- [ ] 1.3 Add the offer-count control to the `.shared` grid: `<select class="inp" id="offerCount">` with options 1 to 4, default 1, and a label plus hint explaining 1 = analyze one offer
- [ ] 1.4 Add `hidden` to the verdict element's initial markup (count starts at 1)
- [ ] 1.5 Update `<title>`, `h1`, and the `.sub` paragraph to analyzer wording that covers one or many offers

## 2. Styles

- [ ] 2.1 Add `--c` and `--d` accent variables to the light `:root` block and to the `prefers-color-scheme: dark` block, lightened in dark to match the existing `--a`/`--b` treatment
- [ ] 2.2 Add `.offer.c{--accent:var(--c)}` and `.offer.d{--accent:var(--d)}`
- [ ] 2.3 Remove `grid-template-columns:1fr 1fr` from `.offers` (set from script instead)
- [ ] 2.4 Add `!important` to `grid-template-columns:1fr` in the `max-width:640px` `.offers` rule so the inline column count does not override mobile stacking

## 3. Script — card rendering

- [ ] 3.1 Capture card 0's `outerHTML` once at startup, before any user edits, as the clone source
- [ ] 3.2 Write `cardHTML(i)`: rewrite `(id|for)="<name>0"` to index `i`, swap `class="offer a"` to the letter class for `i`, swap the `Offer A` heading text to the letter for `i`
- [ ] 3.3 Write `renderOffers(n)`: clamp `n` to 1..4, append clones while card count is under `n`, remove trailing cards while over `n`, set `.offers` inline `gridTemplateColumns` to `repeat(n,1fr)`, toggle the verdict element's `hidden` attribute (hidden when `n === 1`), then call `compute()`
- [ ] 3.4 Delete the 15-entry `ids` array and its `addEventListener` loop; replace with delegated `input` and `change` listeners that call `compute()`
- [ ] 3.5 Call `renderOffers(+offerCount.value)` on `offerCount` change and once at startup

## 4. Script — compute and verdict

- [ ] 4.1 Rewrite `compute()` to loop over the rendered cards: read `rate{i}`/`term{i}`/`freq{i}`/`fees{i}`/`pmi{i}`, call the unchanged `calc()` and `horizon()`, write into `out{i}` via the unchanged `render()`
- [ ] 4.2 Build the active-cost list per offer (`totalCost`, or `costToClear` when a holding period is set), dropping offers whose `calc()` returned null
- [ ] 4.3 Rewrite the verdict: no valid offers → em dash headline and amount; cheapest tied within $0.50 → "cost the same" plus that cost; otherwise name the cheapest offer in its accent color, show the gap to the second-cheapest, and show the cheapest offer's own total
- [ ] 4.4 Keep the horizon note text and its full-term/holding-period basis wording working for any offer count

## 5. Self-check

- [ ] 5.1 Add `demo()` guarded by `location.hash === "#selftest"`, throwing on failed assertions
- [ ] 5.2 Assert `calc()` with the current default inputs returns today's payment, total interest, and total cost
- [ ] 5.3 Assert `renderOffers(4)` produces 4 cards and that `rate3` and `out3` exist in the DOM
- [ ] 5.4 Assert a value written into `rate0` survives `renderOffers(4)` followed by `renderOffers(2)`, and that the re-added card 1 reads the default rate
- [ ] 5.5 Assert verdict ranking over a 3-cost array picks the minimum and reports the gap to the second-lowest

## 6. Verify

- [ ] 6.1 Open the file: exactly one card, no verdict bar, readout matches the current tool's Offer A output for identical inputs
- [ ] 6.2 Step the count 1→2→3→4→2→1, confirming column count follows, entered values persist in surviving cards, new cards start at defaults, and no card is orphaned
- [ ] 6.3 Set count 2 with today's Offer A and Offer B inputs and confirm the verdict names the same winner and gap as the current tool
- [ ] 6.4 Blank a required input on one card at count 3 and confirm that card shows the invalid-input message while the verdict ranks the other two
- [ ] 6.5 Check 390px width at count 4 (single column, 16px inputs) and a wide desktop window at count 1 (card spans full container)
- [ ] 6.6 Check dark mode: all four accents distinct and legible on the dark card background
- [ ] 6.7 Open `#selftest` and confirm no assertion fires
- [ ] 6.8 Open with JavaScript disabled: `noscript` warning renders and card 0's inputs are visible
