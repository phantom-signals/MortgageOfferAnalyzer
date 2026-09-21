## Context

Footer `#glossary` `<dl>` is single source for printed definitions and hover/popover text. Script builds `DEFS` from `dt[data-match]` in DOM order; `defFor` returns first entry with any token contained in label. So DOM order doubles as match priority: "Total interest" must precede "Interest paid", "PMI annual rate" must precede "PMI". Alphabetical order violates both.

## Goals / Non-Goals

**Goals:**
- Glossary reads alphabetically, with or without JavaScript.
- Every label keeps resolving to same definition as today.

**Non-Goals:**
- No wording change to any term or definition.
- No change to which entries carry `data-match` tokens.
- No grouping, letter headings, or search box.

## Decisions

**Sort in markup, not in script.** Reorder `<dt>`/`<dd>` pairs by hand. Spec requires glossary work without JavaScript; a runtime sort would leave no-JS readers with old order. Static order also costs zero code.

**Priority = longest matching token.** `defFor` picks, across all entries, the token contained in label with greatest length; entry order only breaks ties. Longer token is more specific phrase ("total interest" beats "interest", "pmi annual rate" beats "pmi"). Alternatives:
- Separate priority attribute (`data-priority`): extra bookkeeping per entry, easy to get wrong. Rejected.
- Build `DEFS` in hidden priority list separate from glossary: breaks single source. Rejected.
- Script-side sort of `DEFS` by longest token of entry: wrong on entries with mixed-length tokens (e.g. "interest paid|interest"). Per-label longest match is correct.

**Sort key.** `localeCompare` on `dt` text with `{sensitivity: "base"}`. Punctuation sorts before letters, so "PMI (private mortgage insurance)" leads PMI group and "Payment, P&I" precedes "Payments per year". Selftest checks order with same comparator.

## Risks / Trade-offs

- [Two entries with equal-length tokens both contained in one label] Tie falls back to DOM order, now alphabetical, which could pick wrong entry. Mitigation: no such label exists today; selftest compares every rendered label's definition before/after during apply.
- [Future entry added out of order] Mitigation: selftest asserts sorted order.

## Header link

Glossary link reuses Terms of Use click handler, generalized to both anchors: `preventDefault`, open nearest `<details>` of target, `scrollIntoView`. Plain fragment navigation rejected: it overwrites share-state hash, and a closed fold hides target in browsers that do not auto-expand `<details>` on fragment navigation.

Wording "any term" is broader than what opens a popover (field labels, readout rows, shared readout). Kept: terms reader sees are those labels; prose terms are not expected to be clickable.
