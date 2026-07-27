## 1. Verdict tie wording

- [x] 1.1 In `verdict()` (MortgageOfferAnalyzer.html), add local helper that renders one offer's letter as `<strong>` in its accent color; use it in the existing single-winner branch.
- [x] 1.2 After the sort, build the tie set: every entry within $0.50 of `costs[0].cost`.
- [x] 1.3 Branch on tie-set size instead of `costs[1].cost - costs[0].cost`. Size 1 keeps today's "Offer X is cheapest by" output verbatim.
- [x] 1.4 Tie branch: headline lists every tied letter — two joined by "and", three or more comma-separated with ", and" before the last — followed by "cost the same."; amount shows the shared cost.
- [x] 1.5 Confirm the horizon note line still prints in both branches.

## 2. Self-check

- [x] 2.1 Add a tie case to `demo()`: set two offers to identical inputs, run `compute()`, assert both letters appear in `verdictText.innerHTML` and neither reads "cheapest by".
- [x] 2.2 Add a three-way tie case asserting all three letters appear and the separator is ", and " before the last.
- [x] 2.3 Keep the existing distinct-cost assertion (`/>B</` on the winner) passing unchanged.

## 3. Verify

- [x] 3.1 Open `MortgageOfferAnalyzer.html#selftest` in a browser, confirm no throw.
- [x] 3.2 Manual pass at count 4: distinct costs, two-way tie, three-way tie, two-way tie with a costlier third offer, one invalid card. Confirm each named letter carries its card's accent color.
