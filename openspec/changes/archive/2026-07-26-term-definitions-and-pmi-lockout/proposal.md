## Why

Tool prints jargon with no definitions: PMI, LTV, EAR, points, amortization midpoint, cost to walk away. Reader who does not already know mortgage vocabulary cannot check the numbers. Footer explains method and PMI in prose paragraphs, but a reader scanning a readout row has no way to ask "what is this row". Second problem: PMI rate stays editable when the loan starts at or below 80% LTV, where no PMI is owed. Field accepts 0.55, the math discards it, readout says "PMI none". Input contradicts output.

## What Changes

- Add glossary at bottom of page as static markup: term plus one-sentence definition for every jargon term the tool prints or labels.
- Add hover definitions (native `title` attribute) on shared-input labels, offer-input labels, and readout row labels. Script reads the definitions out of the glossary markup at load, so glossary text is the single source and tooltips cannot drift from it.
- PMI annual rate input is forced to 0 and disabled when initial LTV is at or below 80% (no PMI owed). Re-enabled with its prior value restored when LTV rises back above 80%.
- Disabled-input styling: grayed background, muted text, `not-allowed` cursor, in both color schemes.
- No change to `calc()`, `horizon()`, or any printed number. The PMI lockout mirrors the existing `required = hv>0 && (P/hv) > 0.80` guard in `calc()` into the UI; it does not create a new rule.

Note: user's request read "gray out when initial LTV >= 80%". Confirmed inverted — locked out at LTV **<= 80%**, matching where `calc()` already charges no PMI.

## Capabilities

### New Capabilities
- `term-glossary`: Which terms carry definitions, where the definitions live (footer glossary plus hover text), and the requirement that both come from one source so they cannot drift apart.
- `pmi-input-state`: When the PMI rate input is editable, when it is forced to 0 and disabled, how a previously entered value is preserved and restored, and that locking never changes a computed figure.

### Modified Capabilities
- `offer-set`: Requirement "Changing the count preserves entered values", scenario "New cards get default values", currently states a new card's PMI rate is populated with the tool's default. At LTV <= 80% the new card's PMI rate is 0 and disabled instead. Narrow exception added.

## Impact

- `MortgageAnalysisTool.html` — only file. HTML (footer gains a static glossary block), CSS (`.inp:disabled`, glossary list), script (build definition map from glossary markup, `title` injection in `rowHTML()` and on labels, PMI lock in `compute()`).
- Still single file, dependency free, no build step, opened from disk.
- `noscript` viewers: glossary is static markup, so it still renders. Only the hover tooltips are lost, and the existing `noscript` warning already tells that viewer the file is not computable there.
- `demo()` self-check (`#selftest`) gains cases for the lock, the unlock-and-restore path, and glossary-versus-tooltip coverage.
