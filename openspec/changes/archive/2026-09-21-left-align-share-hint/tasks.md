## 1. Style

- [x] 1.1 In `MortgageOfferAnalyzer.html`, add `text-align:left` to the existing `.share .hint` rule (line ~267). Leave `.share{text-align:center}` and `.share .inp` untouched.

## 2. Self-check

- [x] 2.1 In the `#selftest` block, add one `ok()` asserting the computed `textAlign` of the share hint is `"left"`, with a failure message naming the value read.

## 3. Verify

- [x] 3.1 Run `#selftest` headless and confirm it passes with no new failures.
- [x] 3.2 Screenshot the share block at a narrow viewport (~390px) and confirm the disclosure lines share a left edge while the button and the text block stay centered.
