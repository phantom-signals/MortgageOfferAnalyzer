## Context

`verdict()` in [MortgageOfferAnalyzer.html:537](../../../MortgageOfferAnalyzer.html#L537) sorts computed offers by cost, then branches on `costs[1].cost - costs[0].cost < 0.5`. Tie branch prints a fixed string with no letters. Winner branch already builds a colored letter inline: `<strong style="color:var(--${L.toLowerCase()})">${L}</strong>`. Single file, no build step, no framework.

Two defects in one branch: tie set is never named, and it is never computed — only offer index 1 is inspected, so `costs[2]` tying with `costs[0]` is invisible to any wording that tries to list participants.

## Goals / Non-Goals

**Goals:**
- Tie verdict names every offer within $0.50 of the lowest cost.
- Named letters keep the accent color the winner branch already uses.
- One self-check case covering the tie wording.

**Non-Goals:**
- Comparison basis, tolerance value, PMI math, card readouts — unchanged.
- Gap between a tied group and the next costlier offer. Not asked for, and shared cost already answers "how much".
- Markup or CSS change. `verdictText` accepts HTML today.

## Decisions

**Compute tie set by filter, not by pairwise scan.** After the existing sort, `costs.filter(c => c.cost - costs[0].cost < 0.5)` yields every tied offer in one pass, ordered by letter-sorted cost. Alternative — walk forward while the delta holds — same result, more lines. Sort is already there, so the filter is the higher rung.

**Tolerance stays $0.50, absolute, measured against the cheapest.** Chaining (B within 0.50 of A, C within 0.50 of B, so all three "tie") would make the group depend on ordering and let a $0.99 gap read as a tie. Anchor to `costs[0]` instead. Same threshold the current code uses, so no verdict flips for existing inputs.

**Extract the colored-letter snippet to a local helper.** Both branches need it now. One arrow function inside `verdict()`, not a module-level util — single call site pair, no other consumer.

**Join with Oxford comma: "A, B, and C"; two-item case "A and B".** Plain `join(", ")` reads as a list of ties rather than a set. `Intl.ListFormat` does this natively (rung 4), but it escapes nothing and would need the HTML strings passed through it anyway; a two-branch ternary is shorter than constructing a formatter.

**Headline carries the letters, amount carries the shared cost.** Matches the winner branch's split: `verdictText` says who, `verdictAmount` says how much. No `<small>` sub-line in the tie case — there is no second number to show.

## Risks / Trade-offs

- Long tie list at count 4 wraps the headline → four letters plus separators is ~30 characters; headline already holds "Offer A is cheapest by" at the same size.
- Filter runs on every `compute()` call → at most 4 elements, no measurable cost.
- Self-check asserts on `innerHTML` substrings, so a future wording change breaks it → intended; the check exists to catch silent loss of the letters.
