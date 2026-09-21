## Why

Glossary entries sit in match-priority order (specific before general), not reading order. Reader scanning for a term has no way to find it except reading whole list. Alphabetical order makes lookup trivial. Nothing near top of page tells reader definitions exist; glossary sits in closed footer fold.

## What Changes

- Reorder `<dt>`/`<dd>` pairs in footer `#glossary` alphabetically by term (case-insensitive).
- Decouple hover-text matching from DOM order: label resolves to entry whose matching `data-match` token is longest, not first entry in markup. Today order doubles as priority ("Order specific before general — first match wins"); alphabetical order would break it (e.g. "Interest paid" would capture "Total interest (to term)", general "PMI" would capture "PMI annual rate").
- Update markup and script comments that describe order-as-priority.
- Selftest asserts glossary is sorted, so future entries land in place.
- Header gains line under subtitle: "Click on any term to see its definition, or check the glossary." with "glossary" linking to footer glossary.
- Glossary link opens its fold in place and leaves URL hash alone (hash holds share state), same as existing Terms of Use link.

## Capabilities

### New Capabilities

### Modified Capabilities
- `term-glossary`: glossary entries SHALL render alphabetically; specific-beats-general resolution SHALL come from longest matching token instead of entry order. Header SHALL point reader to definitions and glossary.

## Impact

- `MortgageOfferAnalyzer.html`: glossary markup (reorder only, no wording change), `defFor` matcher, header line, Terms link handler (now shared with glossary link), selftest.
- No change to definitions text, computed figures, or share-link keys. Header grows by one line.
