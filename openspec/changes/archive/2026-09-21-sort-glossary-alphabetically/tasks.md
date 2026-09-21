## 1. Matcher

- [x] 1.1 Change `defFor` in `MortgageOfferAnalyzer.html` to return entry whose contained token is longest (DOM order breaks ties)
- [x] 1.2 Update glossary markup comment and `DEFS` comment: drop "Order specific before general — first match wins", state longest token wins

## 2. Reorder

- [x] 2.1 Before reorder, record `title` of every annotated label (headless run, 4 offers shown) as baseline
- [x] 2.2 Reorder `<dt>`/`<dd>` pairs in `#glossary` alphabetically (case-insensitive `localeCompare`), no wording change
- [x] 2.3 Confirm every annotated label's `title` matches baseline

## 3. Check

- [x] 3.1 Add selftest assert: `#glossary dt` texts are sorted by `localeCompare(…, undefined, {sensitivity: "base"})`
- [x] 3.2 Add selftest assert: `defFor("PMI annual rate (%)")` returns PMI annual rate definition
- [x] 3.3 Run `#selftest` headless; all existing and new checks pass

## 4. Header link

- [x] 4.1 Add header line under subtitle: "Click on any term to see its definition, or check the <a href="#glossary">glossary</a>."
- [x] 4.2 Generalize Terms link click handler to `a[href="#terms"], a[href="#glossary"]`: open nearest `<details>` of target, scroll to it, keep hash
- [x] 4.3 Add selftest assert: glossary link opens its fold without writing hash
- [x] 4.4 Run `#selftest` headless; all checks pass
