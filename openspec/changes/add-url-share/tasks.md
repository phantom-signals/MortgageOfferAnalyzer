## 1. Serialize and restore

- [x] 1.1 In the script block, add `serialize()` returning `new URLSearchParams([...document.querySelectorAll(".inp")].map(el => [el.id, el.value])).toString()`
- [x] 1.2 Add `restore(str)`: parse with `URLSearchParams`, set `offerCount` first, call `renderOffers(+value)`, then assign remaining keys only when the id resolves to an element carrying class `inp`, then call `compute()`
- [x] 1.3 Drop unknown keys silently in `restore()`; no throw, no markup insertion, no attribute writes
- [x] 1.4 Replace the boot lines: run `restore(location.hash.slice(1))` when the hash contains `=`, else keep `renderOffers(+$("offerCount").value)`; leave the `location.hash === "#selftest"` check byte-identical and after it

## 2. Copy-link control

- [x] 2.1 Add a "Copy analysis link" button, id `copyLink`, in its own centered block placed after `<div class="verdict">` and before `<footer>` — a sibling of the verdict, never a child of it, since `.verdict` is hidden at one offer and a single-offer link must still be shareable
- [x] 2.1a Below the button, centered, add the hint stating the link embeds the entered figures (loan amount, home value, rates) — visible without hover, since the hosted page never shows the README
- [x] 2.1b Add the block's CSS: centered text, intrinsic-width button reusing the `.inp` border, radius, padding, and focus ring. The button no longer carries class `inp` (centering wants intrinsic width, `.inp` forces `width:100%`); keep `serialize()`'s `input.inp, select.inp` selector as-is
- [x] 2.2 On click: set `location.hash = serialize()` first, then `navigator.clipboard.writeText(location.href)`
- [x] 2.3 On resolve, swap the button label to a confirmation and restore it after ~2s; on reject, swap to a short label pointing at the address bar ("In the address bar", not a sentence)
- [x] 2.3a Read the original label once from `textContent` when the handler is bound and restore that, so the label is not hardcoded a second time in the `setTimeout` and cannot drift from the markup
- [x] 2.3b Give the button a `min-width` sized to the longest swapped label, so an intrinsic-width centered button does not jump when the label changes
- [x] 2.4 Confirm the click handler does not collide with the delegated `input` listener that routes `offerCount` to `renderOffers` and everything else to `compute`

## 3. Self-check

- [x] 3.1 In `demo()`, add a round-trip block: `renderOffers(3)`, set known distinct values across shared and per-offer fields, capture `serialize()` and `$("out0")` total-cost text
- [x] 3.2 Mutate every field, call `restore(saved)`, assert each input matches its captured value and the total-cost readout matches
- [x] 3.3 Assert `restore("garbage")` and `restore("nosuchkey=1")` leave the page computing, and that `restore()` never writes `location.hash`
- [x] 3.4 Reset state at the end of the block, matching the existing cleanup at the tail of `demo()`

## 4. Footer feedback link

- [x] 4.1 Add one `<p>` at the end of `<footer>`, after the existing disclaimer paragraph: questions, requests, and bug reports go to `<a href="https://github.com/phantom-signals/MortgageOfferAnalyzer">`, `rel="noopener"`
- [x] 4.2 No new CSS — `footer p` and `footer a` rules already cover size, color, and hover underline

## 5. Verify

- [x] 5.1 Open with `#selftest`, confirm title reads `selftest passed` — the existing "every label and readout row has a definition" assertion must not trip on the new footer text
- [x] 5.2 Manual: 4 offers with distinct values, copy link, open in a fresh tab, confirm inputs, readouts, and verdict match
- [x] 5.3 Manual: open a link built at above-80% LTV and one at or below, confirm PMI fields lock or unlock as they do on typed input
- [x] 5.4 Confirm no-hash load still shows one offer at current defaults
- [x] 5.5 Confirm the disclosure hint renders under the copy button at desktop and 640px-and-below widths, unhovered
- [x] 5.6 Confirm the footer link is below the fold on desktop, tab-focusable, and works from `file://`
- [x] 5.7 Add a "Share a comparison" line to README (secondary; page hint is the one users see)
- [x] 5.8 Confirm the copy control is visible at one offer, when the verdict bar is hidden, and stays centered at 1 through 4 offers and at 640px and below
- [x] 5.9 Click the control and confirm the button box does not resize through the confirmation label and back, and that the restored label matches the markup
