## Why

Tool hardcodes exactly two offers. Every user starts in comparison mode even when analyzing a single loan — Offer B's rate, term, fees, and PMI must be filled or ignored, and the verdict bar always claims a winner. Most sessions start with one offer in hand; comparison comes later, if at all. Tool should analyze one offer by default and compare only when asked.

## What Changes

- **BREAKING** (user-visible default): default offer count becomes 1, not 2. Opening the file shows one offer, no comparison.
- Add offer-count control in shared inputs: pick 1 to 4 offers.
- Offer A stays hardcoded in HTML as card index 0 with indexed ids (`rate0`, `term0`, `freq0`, `fees0`, `pmi0`). Offer B's hardcoded markup is removed; cards 1 to 3 are cloned from card 0 when the count is raised.
- Raising count adds cards with default values; lowering count drops trailing cards. Values in surviving cards are preserved across count changes.
- Verdict bar hides at count 1 (nothing to compare). At count 2 or more it names the cheapest offer and the gap to the next-cheapest.
- Accent colors extend from two (`--a`, `--b`) to four; each offer card keeps a distinct accent.
- Page title and heading change from "Two-offer cost comparison" to analyzer wording covering both modes.
- No change to calculation math: `calc()`, `horizon()`, PMI schedule, and shared inputs (loan amount, holding period, home value, PMI rule, PMI basis) are untouched.

## Capabilities

### New Capabilities
- `offer-set`: How many offers the tool holds, how the count is chosen, how cards are added and removed, how existing input values survive a count change, and how the verdict behaves at each count.

### Modified Capabilities
- `page-layout`: Requirement "Offer cards share the available width equally" currently pins exactly two side-by-side cards. Becomes a variable-count grid — 1 to 4 equal columns on desktop, single column at mobile breakpoint.

## Impact

- `MortgageAnalysisTool.html` — only file. HTML (offers markup replaced by empty container plus count control), CSS (`.offers` grid template, accent variables), script (id list, card generation, `compute()` loop over offers, verdict over N).
- Still single-file, dependency-free, no build step, opened from disk. `noscript` block unaffected.
- JavaScript-disabled viewers still see card 0's inputs (hardcoded) and the existing `noscript` warning; they lose only the removed Offer B card, which was never computable there anyway.
- Preserved: math output for a given offer is bit-identical to today's Offer A path.
