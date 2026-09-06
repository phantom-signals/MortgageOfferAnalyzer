## 1. Markup

- [ ] 1.1 Add one `<div id="defPop" popover>` near the end of `<body>`, before the `<script>`. No content — the handler fills it.
- [ ] 1.2 Append a touch-only hint `<span class="tap-hint">` to the existing intro `<p class="sub">` that describes the results, wording it so it points at readout row labels.

## 2. Styles

- [ ] 2.1 Add a `#defPop` ruleset: top-layer popover styled to match `.tip` colours (`--verdict-bg` / `--verdict-fg`), `border-radius:8px`, `font-size:13px`, readable line-height, `max-width` around `40ch`, sentence wrapping (no `nowrap`), and the same shadow as `.tip`.
- [ ] 2.2 Reset the UA popover defaults the design does not want — `border:0`, `padding` set explicitly, and `margin:auto` so it centres in the top layer.
- [ ] 2.3 Add `.tap-hint{display:none}` and show it only inside `@media (hover:none)`.
- [ ] 2.4 Confirm no rule touches `.row .k` or `.field label` appearance. No underline, no cursor change, no colour change.

## 3. Behaviour

- [ ] 3.1 Add one delegated `click` listener on `document` that resolves `e.target.closest(".row .k")`.
- [ ] 3.2 Bail early when there is no match, when `el.title` is empty, or when `pop.showPopover` is undefined.
- [ ] 3.3 Set `pop.textContent = el.title`, call `pop.hidePopover()` then `pop.showPopover()` so tapping a second label while one is open swaps the text.
- [ ] 3.4 Do not bind anything inside `annotate()` or `render()` — the listener binds once and must survive readout re-renders.
- [ ] 3.5 Verify `.field label` never opens the popover and still focuses its control.

## 4. Checks

- [ ] 4.1 Add a self-test asserting a readout row label click opens `#defPop` with text equal to that row's `title`.
- [ ] 4.2 Add a self-test asserting a `.field label` click leaves `#defPop` closed.
- [ ] 4.3 Add a self-test asserting the popover text for a known term matches its glossary `<dd>`, proving the single source holds through the new path.
- [ ] 4.4 Re-run the existing self-test block and confirm every prior assertion still passes, including the tooltip assertions near lines 1154-1160.

## 5. Manual verification

- [ ] 5.1 On a touch device or emulated touch: tap a readout row label, confirm the popover opens, tap outside, confirm it closes.
- [ ] 5.2 Raise the offer count to 4, edit an input to force a re-render, then tap a row label on the added card and confirm the popover still opens.
- [ ] 5.3 On a pointer device: confirm the page is visually unchanged, the hint sentence is absent, and hover text still appears on labels.
- [ ] 5.4 Confirm computed figures — payment, effective annual rate, LTV, PMI, total cost, verdict — are identical before and after the change for the same inputs.

## 6. Spec sync

- [ ] 6.1 Run `openspec validate tap-definition-popover` and confirm it passes.
- [ ] 6.2 Archive the change so the `term-glossary` delta folds into `openspec/specs/term-glossary/spec.md`.
