## 1. Input labels and glossary text

- [x] 1.1 Remove `.hint` spans from the Home value and Holding period labels (already in working tree)
- [x] 1.2 Change Holding period label to "Holding period (years)"
- [x] 1.3 Extend the Holding period `<dd>` to state the period is in years and that a blank field runs costs to full term
- [x] 1.4 Add `cost to term` to the Total cost `<dt>` `data-match`
- [x] 1.5 Add a "Cost over time" glossary entry (`data-match="cost over time"`) in alphabetical position, holding the old section hint text as a sentence

## 2. Section headings

- [x] 2.1 Remove the `.hint`/`#barsHint` span from the cost comparison heading
- [x] 2.2 Replace the "Cost over time" hint with `<span id="chartHead">Cost over time</span>`
- [x] 2.3 In `drawBars`, set `$("barsHead").title = defFor(heading text)` beside the text swap; delete the `#barsHint` lead-clause code and its comment
- [x] 2.4 Add `#barsHead, #chartHead` to the `annotate()` selector and the popover click selector
- [x] 2.5 Delete the `.section-label .hint` CSS rule

## 3. Break before "("

- [x] 3.1 Add `.paren{display:inline-block}` CSS
- [x] 3.2 Add `paren(s)` helper wrapping a trailing ` (…)` in `<span class="paren">`; call it in `rowHTML` and on the cost-table total label
- [x] 3.3 Wrap parentheticals in static input labels and glossary `<dt>`s in `<span class="paren">`

## 4. Self-tests and verification

- [x] 4.1 Replace the `#barsHint` checks with `#barsHead.title` checks for both modes, plus a flip back to walk-away
- [x] 4.2 Add `#barsHead, #chartHead` to the "every label resolves to a definition" check; assert the "Privacy and Terms of Use" summary carries no `title`
- [x] 4.3 Run `#selftest` headless; confirm `selftest passed`
- [x] 4.4 Re-run the 320/375/414px line-break probe; confirm every wrapped label breaks before "("
