## 1. Verdict

- [x] 1.1 Wrap verdict in `<div id="verdict" hidden>` holding `<p class="section-label">Verdict</p>` and `<div class="verdict">`; drop the in-card `<p class="label">Verdict</p>`
- [x] 1.2 Delete `.verdict[hidden]` and `.verdict .label` rules; move top spacing from `.verdict` to the section label
- [x] 1.3 Delete `--banner-bg`, `--banner-fg`, `--banner-line` in both schemes and the "verdict bar only" comment; point `.verdict` at `--card`, `--ink`, `--line-strong`

## 2. Footer folds

- [x] 2.1 Wrap "Definitions" label and `<dl id="glossary">` in `<details>`; summary `class="section-label"`, text "Glossary"; keep the glossary source comment
- [x] 2.2 Wrap combined Privacy and Terms content in `<details id="terms">`; summary `class="section-label"`, text "Privacy and Terms of Use"
- [x] 2.3 CSS: footer summary as flex row, `list-style:none`, hide `::-webkit-details-marker`, `cursor:pointer`, visible `:focus-visible` outline in `--slate`
- [x] 2.4 CSS: add `footer summary::before` to the offer chevron selector and `footer details[open] > summary::before` to the rotated selector
- [x] 2.5 JS: click on `a[href="#terms"]` calls `preventDefault()`, sets `$("terms").open = true`, `scrollIntoView()`
- [x] 2.6 Selftest: Terms link click opens `#terms` and leaves `location.hash` unchanged; close it again after

## 3. Punctuation

- [x] 3.1 Input label hints: home value and holding period wrap hint in parentheses inside `.hint`; PMI premium basis and PMI annual rate drop their hints, leaving "PMI annual rate (%)" with no colon
- [x] 3.2 Section-label hints (cost to walk away, cost over time): hint wrapped in parentheses inside `.hint`, no colon
- [x] 3.3 Share hint and `noscript` notice: em dash becomes colon
- [x] 3.4 Glossary: rewrite 4 em dash asides (offer, payments per year, interest through holding period, MIP) with colons or parentheses, wording otherwise unchanged
- [x] 3.5 LTV readout tail: `pct + " (" + tail + ")"`; update the two selftest expectations to `88.889% (PMI required)` and `80.00% (no PMI required)`
- [x] 3.6 Confirm the only remaining `&mdash;` and `—` are lone empty-value placeholders

## 4. Dead code

- [x] 4.1 Delete `.notice` rule and its comment; keep `.sub a` color as its own rule
- [x] 4.2 Delete `.refs`, `.tap-hint`, its `@media (hover:none)` rule, and `.sub+.sub`
- [x] 4.3 Remove stray blank line with trailing spaces after `</footer>`

## 5. Verify

- [x] 5.1 Run `#selftest` headless; all pass
- [x] 5.2 Screenshot light and dark at 390px and desktop: verdict title outside card, card matches offer cards, both footer folds closed with chevrons
- [x] 5.3 `openspec validate footer-folds-and-verdict-cleanup`

## 6. Offer card summary

- [x] 6.1 Hide the summary payment figure while a card is expanded: `.fold[open] summary .sum{display:none}`
- [x] 6.2 Cost-bars section hint: glossary definition up to its first colon; selftest pins both hint strings
- [x] 6.3 Input labels open the definition popover and suppress focus (Popover API only); selftest covers open, no focus, re-tap close
