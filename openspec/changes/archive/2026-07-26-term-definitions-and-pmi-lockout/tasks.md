## 1. Glossary markup

- [x] 1.1 Add `<dl id="glossary">` to the footer of `MortgageAnalysisTool.html`, after the existing method, PMI, and refs paragraphs, under a `.section-label` heading reading "Definitions".
- [x] 1.2 Write one `<dt>`/`<dd>` pair per term, ordered specific before general (amortization midpoint before amortization; initial LTV before LTV): PMI, LTV, initial LTV, principal / loan amount, effective annual rate (EAR), term, payments per year, upfront fees and points, amortization, amortization midpoint, holding period, home value at purchase (original value), PMI removal rule, PMI premium basis, HPA, payment (P&I), total interest, total cost, remaining balance, cost to walk away, escrow, MIP.
- [x] 1.3 Expand every abbreviation in its own `<dt>` (PMI, LTV, EAR, HPA, MIP, P&I).
- [x] 1.4 Give each `<dt>` a `data-match` attribute listing the `|`-separated label snippets that term should attach to; check each snippet against the actual label strings the file renders (shared input labels, offer input labels, and every `rowHTML()` label in `render()`).
- [x] 1.5 Add CSS for the glossary list: `dt` in the label style already used by `.field label`, `dd` in `.refs` size and color, indented, no bullet, comfortable wrapping at full container width.

## 2. Hover definitions

- [x] 2.1 Add `buildDefs()` in the script: walk `#glossary dt`, build a list of `{tokens: dt.dataset.match.toLowerCase().split("|"), text: dt.nextElementSibling.textContent}` in document order. Run it once at startup.
- [x] 2.2 Add `annotate(root)`: for every `.field label` and `.row .k` under `root` that has no `title`, find the first entry whose token appears in the element's lowercased `textContent`, and set `title` to that entry's text.
- [x] 2.3 Call `annotate` on the whole document at the end of `renderOffers()` so cloned card labels are covered, and on each readout container right after `$("out"+i).innerHTML = render(res, h)` in `compute()`.
- [x] 2.4 Verify the hand-written `title` text on `pmiThresh`, `pmiBasis`, and their `<option>` elements is untouched (the skip-if-already-titled guard covers the controls; options are never selected by `annotate`).

## 3. PMI input lockout

- [x] 3.1 Add `const LOCK_NOTE` in the script: one sentence stating PMI does not apply at or below 80% initial LTV, so the rate is fixed at 0.
- [x] 3.2 In `compute()`, after `hv` is parsed, add `const pmiRequired = hv > 0 && P > 0 && (P/hv) > 0.80 + 1e-12;` — the same test `calc()` uses.
- [x] 3.3 At the top of the per-offer loop in `compute()`, before the PMI rate is read: when not required and not already disabled, stash `value` into `dataset.prev`, set `value = "0"`, set `disabled = true`, set `title = LOCK_NOTE`; when required and currently disabled, restore `dataset.prev` (falling back to current value), clear `disabled`, remove `title`.
- [x] 3.4 Add `.inp:disabled{background:var(--line);color:var(--slate);cursor:not-allowed;opacity:1}` to the stylesheet; confirm legibility in both color schemes.

## 4. Self-check

- [x] 4.1 Confirm the existing pinned math assertions in `demo()` still pass unchanged (payment, total interest, total PMI, PMI end period, total cost) — the guard that no computed figure moved.
- [x] 4.2 Add lock assertions: set loan 360000 / home value 450000 (LTV exactly 80%), `compute()`, assert `$("pmi0").disabled === true` and `$("pmi0").value === "0"`; set loan 300000, assert still locked; set loan 400000, assert unlocked.
- [x] 4.3 Add restore assertion: with LTV above 80%, set `pmi0` to `"0.72"`, drop LTV to 75%, raise it back, assert `$("pmi0").value === "0.72"`.
- [x] 4.4 Add per-card stash assertion at offer count 3 with distinct PMI rates, and an assertion that a card cloned while locked restores `0.55` on unlock.
- [x] 4.5 Add tooltip assertions: after `renderOffers(2)`, assert the "PMI annual rate (%)" label on card 1 has a non-empty `title`, and that an "Initial LTV" readout row's `.k` has a `title` containing "loan-to-value".
- [x] 4.6 Add coverage assertion: every rendered `.field label` and `.row .k` resolves to a definition, so a new label with no glossary entry fails the self-check.
- [x] 4.7 Restore the pre-`demo()` state at the end of the self-check as it does today (`offers.innerHTML = card0HTML`), and reset the shared inputs the lock tests changed (`amount`, `homeValue`) to their default values.

## 5. Verify

- [x] 5.1 Open the file with `#selftest`; confirm the page title reads "selftest passed".
- [x] 5.2 Open the file normally at defaults (loan 400000, home value 450000): PMI input editable, readout PMI figures unchanged from before the change.
- [x] 5.3 Lower the loan amount to 350000: PMI input grays out, reads 0, readout shows "PMI none"; raise it back and confirm the entered rate returns.
- [x] 5.4 Hover a readout row label and an input label in both light and dark scheme; confirm definitions appear and the row layout does not shift.
- [x] 5.5 Open the file with JavaScript disabled; confirm the glossary still renders and the `noscript` warning is unchanged.
- [x] 5.6 Check the 640px breakpoint: glossary readable in one column, disabled input styling intact.
