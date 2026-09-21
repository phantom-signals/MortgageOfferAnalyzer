## Context

Single file, `MortgageOfferAnalyzer.html`. Owner already staged hand edits: header trimmed to one `.sub` line, `.notice` block deleted, verdict moved below offers, footer rewritten (Verify / Calculations / License lines, then "Definitions" list, then combined "Privacy and Terms of Use"). Those edits left dead CSS, a dangling `<a href="#terms">` (no element carries `id="terms"` now), and em dash separators the owner wants gone.

Constraints:
- `location.hash` carries share state; boot restores from it. Any in-page anchor that writes the hash clobbers a loaded analysis.
- Glossary is the single source for tooltips and popover (`#glossary dt/dd`, read via `querySelectorAll`).
- Offer cards already use `<details class="fold">` with a CSS chevron on `.offer h2::before`.
- Selftests (`#selftest`) assert on `$("verdict").hidden` and the LTV readout text.

## Goals / Non-Goals

**Goals:**
- Footer: two closed `<details>` sections, Glossary then Privacy and Terms of Use.
- Terms link opens its fold without touching the hash.
- Verdict title outside card; card neutral in both schemes.
- Parentheses replace em dash separators in label hints; LTV tail in parentheses.
- Remove CSS left dead by staged edits.

**Non-Goals:**
- Results section labels (verdict, cost bars, cost over time) stay unfolded.
- Lone em dash placeholders for empty values stay.
- No change to glossary wording beyond dash punctuation. No change to Terms or Privacy wording.
- No restoring the removed "tap any label" hint; popover stays a quiet feature.
- No fix for other in-page anchors; `#terms` is the only one.

## Decisions

**Verdict wrapper carries the id.** Wrap label and card: `<div id="verdict" hidden><p class="section-label">Verdict</p><div class="verdict">…</div></div>`. JS toggles `$("verdict").hidden` unchanged, selftests unchanged, title and card hide together. Wrapper is block, so UA `[hidden]` works and `.verdict[hidden]{display:none}` goes. Alternative: `.section-label:has(+ .verdict[hidden])` hides a loose label; rejected, two elements to keep in sync by CSS trick instead of by structure. Old `.verdict .label` rule and `<p class="label">` inside the card are deleted; top margin moves from card to section label.

**Verdict colors: delete tokens, not override.** `--banner-bg/fg/line` exist only to give dark scheme a dark bar. Removing only the dark override leaves three aliases of `--card`, `--ink`, `--line-strong`. Delete all three, point `.verdict` at the base tokens. `--verdict-bg/fg` stay; tooltip and popover use them.

**Footer folds: native `<details>`, reuse offer chevron.** Markup: `<details id="glossarySection"><summary class="section-label">Glossary</summary><dl class="glossary" id="glossary">…</dl></details>` and `<details id="terms"><summary class="section-label">Privacy and Terms of Use</summary>…</details>`. Chevron: extend existing selector lists, `.offer h2::before, footer summary::before` and `.fold[open] h2::before, footer details[open] > summary::before`. Summary needs `list-style:none`, `::-webkit-details-marker{display:none}`, `cursor:pointer`, and flex row so chevron sits left of text. Do not put `.fold` class on footer details: `.fold` focus ring uses `var(--accent)`, undefined outside offer cards. Alternative: JS accordion; rejected, native element works without script and keeps keyboard handling free.

**Terms link handler.** One delegated-free listener on the single `a[href="#terms"]`: `preventDefault()`, set `$("terms").open = true`, `scrollIntoView()`. Keeps `href="#terms"` so no-JS still jumps (hash write there is harmless: no script, no share state). Alternative: rely on browser auto-expand of closed `<details>` on fragment navigation; rejected, support uneven and hash still clobbered.

**Hint placement.** Parentheses go inside `.hint`, so they stay slate with the hint text: `Home value at purchase <span class="hint">(lower of…)</span>`. Section labels: `<span id="barsHead">Cost to walk away</span> <span class="hint">(<span id="barsHint"></span>)</span>`. A label already ending in a unit, "PMI annual rate (%)", drops its hint rather than stacking two parenthesized groups; PMI premium basis also drops its hint. Colons were tried first and rejected by owner. Sentences (share hint, noscript, glossary asides) keep colons or parentheses.

**LTV tail.** JS line ~905: `pct(P/hv) + " (" + (pmiRequired ? "PMI required" : "no PMI required") + ")"`. Placeholder `"—"` unchanged. Two selftest strings updated.

## Risks / Trade-offs

- [Find-in-page misses closed glossary text in some browsers] Accepted; popover and hover still deliver each definition.
- [Glossary label matching depends on label `textContent`, which now includes ":" instead of "—"] Tokens are substrings like "home value at purchase"; punctuation outside tokens. Selftest "every label resolves to a definition" catches a miss.
- [Removing Feedback line drops the only "report a bug" wording] Owner decision; header "open source" link still reaches the repository.
- [`#terms` jump without JS still writes hash] No script, no share state to lose.
