## Why

Top and bottom text of page grown long and noisy: disclaimer notice, method and PMI paragraphs, feedback line, full legal text and glossary all expanded. Staged hand edits already trimmed header and footer, moved verdict below offers, merged Privacy and Terms of Use. Specs and leftover markup, CSS, and punctuation now lag those edits; `#terms` link points at nothing.

## What Changes

- Remove disclaimer `.notice` block and its CSS; footer line "Verify against your official Loan Estimate..." replaces it.
- Remove footer method paragraph, PMI paragraph, cross-check refs, Canadian compounding note, and Feedback line. **BREAKING** for `repo-feedback-link` spec: capability dropped; header "open source" link remains only path to repository.
- Verdict renders after offers grid, before cost bars (staged, intentional).
- Verdict title moves out of card into a `section-label` above it, same as cost bars and cost-over-time chart. Title hides with card at one offer.
- Verdict card uses card background, ink text, strong border in both color schemes. Dark-scheme dark banner dropped. Tooltip and popover unchanged.
- Footer ends with two collapsed `<details>` folds, chevron styled like offer-card chevron: "Glossary" (renamed from "Definitions"), then "Privacy and Terms of Use".
- Footer "Terms of Use" link opens its fold and scrolls to it without touching `location.hash`, which holds share state.
- Input-label and section-label hints wrap in parentheses after the label instead of following an em dash. PMI premium basis and PMI annual rate hints dropped.
- Em dashes inside sentences (share hint, noscript text, glossary definitions) replaced with colons, commas, or parentheses.
- LTV readout tail changes from `88.889% — PMI required` to `88.889% (PMI required)`.
- Lone em dash placeholders for empty readouts and verdict stay.
- Offer card summary payment figure hides while card is expanded, instead of shrinking to a quiet line; readout below repeats it.
- Cost-bars section hint shows only the lead clause of its glossary definition, e.g. "what the loan costs if you leave at the end of the holding period"; breakdown after the colon dropped, since the table lists it.
- Tapping an input label opens its definition popover instead of focusing the input. Touch hint sentence (already removed from header) dropped from spec.
- Dead CSS removed: `.notice`, `.refs`, `.tap-hint`, `.sub+.sub`, `--banner-*` tokens, `.verdict[hidden]`.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `page-layout`: offer-card summary figure hidden while expanded; verdict placement (below offers, above charts) and title outside card; verdict colors identical across schemes; footer prose scenario no longer names method and PMI notes; new requirement for collapsed footer sections and Terms link; new requirement for parenthesized label hints.
- `cost-comparison`: section hint uses lead clause of glossary definition only.
- `term-glossary`: glossary section named "Glossary", sits in collapsed footer fold above Privacy and Terms of Use; definitions free of em dashes; tooltips and popover work while fold closed; input labels open the popover without focusing their input; touch-hint requirement removed.
- `shared-ltv-readout`: PMI tail rendered in parentheses after percentage.
- `repo-feedback-link`: all requirements removed.

## Impact

- `MortgageOfferAnalyzer.html` only: header and footer markup, verdict markup, CSS tokens and rules, LTV readout string (line ~905), Terms link click handler, selftests for LTV tail (lines ~1359, ~1362).
- No computed figure, share-link format, or glossary lookup changes.
- `math.html`, `MATH.md`, `README.md` untouched.
