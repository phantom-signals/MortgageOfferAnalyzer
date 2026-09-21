## Context

All work in `MortgageOfferAnalyzer.html`. Definitions come from footer glossary `<dt data-match>`/`<dd>` pairs. `defFor(text)` returns the `<dd>` whose longest token is a substring of the text. `annotate(root)` sets `title` on `.field label, .row .k, #costTable .k, .shared .readout`, skipping any element that already has a `title`. A delegated click handler opens `#defPop` for the same selector list.

Current state:
- Input hints on Home value and Holding period already removed in the working tree.
- `#barsHead` text flips "Cost to walk away" / "Cost to term" in `drawBars`. `#barsHint` gets the lowercased lead clause of `defFor("cost to walk away" | "total cost")`.
- "Cost over time" heading is bare text plus a static `.hint` span. No glossary entry.
- Row labels are plain text in `.row .k` (flex item) and `#costTable th.k`. Headless probe at 320px showed four row labels breaking inside the parenthetical.

## Goals / Non-Goals

**Goals:**
- Headings define themselves through the existing popover, no parenthetical hints.
- Trailing parentheticals move to their own line as a unit when a label wraps.
- One definition source kept.

**Non-Goals:**
- Popover positioning or styling changes.
- Definitions for other section labels (Verdict, footer summaries).
- Break handling for cost-table segment labels. None has a parenthetical today.

## Decisions

**Break before "(" via `display:inline-block` span.** Wrap each trailing parenthetical in `<span class="paren">`. An inline-block is atomic in the line, so the only break opportunity is the space before it. Alternatives: `white-space:nowrap` overflows when the parenthetical is wider than the column; `text-wrap:balance` evens lines but can still split inside the parenthetical; `<wbr>` adds a break point without removing others. The span leaves `textContent` unchanged, so `defFor`, `annotate`, and the `textContent` self-tests are unaffected. The popover click still resolves through `closest()`.

**One helper for generated labels, hand edits for static ones.** `paren(s)` replaces a trailing ` (…)` with ` <span class="paren">(…)</span>`, called in `rowHTML` and on the cost-table total string. Static input labels and glossary `<dt>`s get the span in markup (about twelve spots). A load-time pass over the DOM would cover both, but it is more machinery than twelve edits.

**Headings targeted by id, not `.section-label`.** Add `#barsHead` and a new `#chartHead` span to the `annotate()` and click selectors. A blanket `.section-label` selector would give "Privacy and Terms of Use" the Term definition through the `term` token, and would make the footer summaries open popovers.

**`drawBars` sets `#barsHead.title` itself.** `annotate()` skips titled elements, so after the first flip the heading would keep the old definition. `drawBars` already writes the heading text, so it writes `title = defFor(text)` on the same line. Removes `#barsHint`, the `split(":")[0]` lead clause, and the lowercasing.

**`cost to term` token on the Total cost entry.** It lets `defFor("Cost to term")` resolve by the heading text, beating the shorter `term` token. No other printed label contains "cost to term", so no other label changes resolution.

**Holding period label keeps its unit.** "Holding period (years)" follows the "Term (years)" pattern. The blank-means-full-term instruction moves into the `<dd>`, since only the popover can carry it now.

## Risks / Trade-offs

- [Paren span added inside `#costTable .k div`, which is `display:flex`, would become a separate flex item and form a column] → helper applied only to the total row, which has no flex wrapper. Segment labels have no parentheticals. A future segment label with one needs its text wrapped in a single span first.
- [Heading tap target is 11px uppercase text] → same size as today's heading. No visible marker, per the existing "no visible marker" requirement.
- [Removing hints hides the explanation until the reader taps] → header already says "Click on any term for its definition".
