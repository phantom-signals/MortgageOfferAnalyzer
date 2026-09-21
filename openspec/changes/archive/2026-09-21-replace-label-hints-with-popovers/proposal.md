## Why

Labels and section headings with parentheticals wrap mid-parenthetical on phones. At 320px: "Payment incl. PMI (first ⏎ period)", "Total cost (to term, incl. ⏎ fees + PMI)", "Holding period (years until you ⏎ sell/refinance; leave blank for full term)". Long parenthetical hints duplicate text the definition popover already shows, and make the worst breaks.

## What Changes

- Remove parenthetical hints from the Home value and Holding period input labels (removal already made in the working tree). Holding period label becomes "Holding period (years)". The Holding period glossary definition gains the blank-means-full-term instruction the hint carried.
- Remove parenthetical hints from the "Cost to walk away" / "Cost to term" and "Cost over time" section headings. Each heading instead opens its glossary definition as hover text and in the shared popover, like readout row labels.
- New glossary entry "Cost over time", holding the old section hint text.
- "Cost to term" heading resolves to the Total cost entry, not Term.
- Labels, readout row labels, the cost-table total label, and glossary terms that wrap SHALL break before the opening "(" of a trailing parenthetical, keeping the parenthetical together where it fits.
- Remove `#barsHint`, its lead-clause extraction, and the `.section-label .hint` style.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `cost-comparison`: section heading carries its definition as hover/popover instead of a parenthetical section hint.
- `page-layout`: "Label hints sit in parentheses" replaced; labels carry no hints (units only), em-dash rule kept, new break-before-parenthetical rule.
- `term-glossary`: section headings carry definitions; new "Cost over time" entry; Holding period definition states unit and blank behavior.

## Impact

- `MortgageOfferAnalyzer.html` only: label markup, glossary entries, `rowHTML`, `drawBars`, `annotate()` and popover click selectors, CSS, `#selftest` checks for the section hint.
- Specs: `cost-comparison`, `page-layout`, `term-glossary`.
- No computed value changes. No new dependencies.
