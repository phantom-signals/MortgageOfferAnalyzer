## Why

Tie verdict reads "The cheapest offers cost the same." Never says which offers. With 3 or 4 cards up, user must eyeball totals to find the tied pair. Single-winner verdict already names its offer by letter and accent color; tie path dropped that.

## What Changes

- Tie verdict names every offer tied for cheapest, by letter, each in its own accent color: "Offers **A** and **C** cost the same." Two-way uses "and", three-or-more uses comma list with final "and".
- Tie set = all offers within $0.50 of lowest cost, not only the second-cheapest. Today's check compares `costs[1].cost - costs[0].cost`, so a three-way tie is detected but still unnamed, and a near-tie further down the list is invisible.
- Shared cost keeps showing in verdict amount. No change to comparison basis, math, or single-winner path.
- Self-check gets one tie case asserting named letters appear in verdict text.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `offer-set`: "Verdict ranks every displayed offer" — tie scenario changes from "states that the cheapest offers cost the same" to naming the tied offers. Adds three-way-tie scenario. "Each offer card is visually distinguishable" — accent-color rule extends to every named letter in a tie, not only a single winner.

## Impact

- `MortgageOfferAnalyzer.html`: `verdict()` tie branch (~line 544), `demo()` self-check.
- No new files, no dependencies, no markup change — `verdictText` and `verdictAmount` already carry inline HTML.
