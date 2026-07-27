## Context

`MortgageAnalysisTool.html` is one self-contained file — no build, no dependencies, opened from disk or previewed as an email attachment. Today it hardcodes two offer cards (`.offer.a`, `.offer.b`) with suffixed ids (`rateA`/`rateB`, `termA`/`termB`, ...), binds a fixed `ids` array of 15 elements to `compute()`, and `compute()` calls `calc()` twice, renders into `outA`/`outB`, then diffs the two costs for the verdict.

Everything two-ness lives in three places:

- markup: two `.offer` blocks, two accent variables `--a` / `--b`
- script: the `ids` array, the two `calc()` calls, the two-arm verdict
- CSS: `.offers{grid-template-columns:1fr 1fr}`

`calc()` and `horizon()` are already per-offer pure functions taking explicit arguments. They need no change — the change is entirely about how many times they are called and where results land.

Constraint from the existing spec: `page-layout` requires cards side by side and equal width on desktop, single column at 640px and below.

## Goals / Non-Goals

**Goals:**

- Offer count of 1 to 4, default 1.
- Count changes preserve values in surviving cards; new cards start at defaults.
- Verdict hidden at count 1, ranks all offers at count 2 or more.
- `calc()` and `horizon()` untouched; identical numbers for a given offer.
- Still one file, no dependencies, still usable (inputs visible) with JavaScript disabled.

**Non-Goals:**

- Per-offer loan amount, home value, or PMI rule — those stay shared.
- Persisting inputs across reloads (no URL hash, no localStorage).
- Restoring values of a card removed by lowering the count.
- More than 4 offers. Accent palette and desktop column width both degrade past that.
- Amortization tables, charts, or export.

## Decisions

### Card 0 stays in HTML; cards 1 to 3 are cloned from it

Offer A's markup remains hardcoded with index-suffixed ids (`rate0`, `term0`, `freq0`, `fees0`, `pmi0`, `out0`). Extra cards are produced by taking card 0's `outerHTML` and rewriting the id/for/class suffixes:

```js
function cardHTML(i){
  return card0.outerHTML
    .replace(/(id|for)="(\w+?)0"/g, `$1="$2${i}"`)
    .replace(/class="offer a"/, `class="offer ${LETTERS[i].toLowerCase()}"`)
    .replace(/>Offer A</, `>Offer ${LETTERS[i]}<`);
}
```

Two properties fall out of this for free:

- **New cards carry default values.** `outerHTML` serializes the `value` *attribute*, not the live `.value` property, so a clone of an edited card 0 still reads 6.25 / 30 / 12 / 3000 / 0.55. That is exactly the "new cards get default values" requirement, with no defaults table to maintain.
- **JavaScript-disabled viewers still see a full offer card**, because card 0 is real markup, not a `<template>`.

*Alternative considered:* a `<template id="offerTpl">` with `__i__` placeholders. Rejected — `<template>` contents do not render, so the no-JavaScript path would show zero inputs, and card 0's markup would be duplicated in the file.

*Alternative considered:* generating all cards from a JS string. Same no-JavaScript regression, plus the markup leaves HTML entirely and becomes harder to edit.

*Trade-off accepted:* the rewrite is string surgery over the tool's own markup. It breaks if a future edit adds an id not ending in a digit-suffixable name, or changes the heading text. Guarded by the self-check below, which asserts the cloned card exposes `rate1`, `term1`, `freq1`, `fees1`, `pmi1`, `out1`.

### Rebuild only the tail of the card list on count change

`renderOffers(n)` clamps `n` to 1..4, appends clones while there are fewer than `n` cards, and removes trailing cards while there are more. Cards that already exist are never touched, so their live `.value` properties survive — no read-back-and-restore step.

*Alternative considered:* wipe the container and re-render all cards from a values array held in JS. Rejected — that adds a state mirror of the DOM and a serialize/restore path to preserve what the DOM already holds correctly.

### Event delegation instead of a rebuilt `ids` array

The current per-id `addEventListener` loop cannot survive cards appearing after load. Replace it with two listeners on a stable ancestor:

```js
document.addEventListener("input", compute);
document.addEventListener("change", compute);
```

Both events bubble, so new cards are live the moment they are inserted, and the 15-entry `ids` array is deleted outright.

*Alternative considered:* re-binding listeners on each newly created card. Rejected — more code, and it re-introduces a list to keep in sync.

### `<select>` for the count, plus a clamp in the render path

Count control is `<select id="offerCount">` with options 1 to 4, default 1, placed in the `.shared` grid. A `<select>` cannot produce an out-of-range value through the UI, so no input validation code is needed for user interaction; `renderOffers()` still clamps its argument so a programmatic call cannot render 0 or 9 cards.

*Alternative considered:* `<input type="number" min="1" max="4">`. Rejected — `min`/`max` do not block typed values without form validation, so it would need the clamp *and* a correction path that fights the user mid-typing.

### Grid columns set from the count

`.offers` gets `style.gridTemplateColumns = "repeat(" + n + ",1fr)"` inside `renderOffers()`; the static `1fr 1fr` rule is removed. The existing `max-width:640px` media query keeps `grid-template-columns:1fr` and wins by source order plus specificity — inline style beats it, so the media-query rule needs `!important`, or the inline style must be skipped on mobile. Use `!important` in the mobile rule: one word, no viewport logic in JS.

*Alternative considered:* `repeat(auto-fit,minmax(280px,1fr))`, no JS at all. Rejected — it wraps 4 cards onto two rows on a ~1000px window, violating the "single row on non-mobile viewports" requirement, and it makes the rendered column count depend on window width rather than the user's choice.

### Verdict ranks by sorting the computed costs

`compute()` builds `results[]` (one entry per rendered card, `null` for invalid inputs), picks the active cost per offer exactly as today (`totalCost`, or `costToClear` when a holding period is set), drops nulls, and sorts ascending. Cheapest and second-cheapest give the headline and the gap. Tie handling keeps the existing `< 0.5` dollar epsilon. At count 1 the verdict element gets the `hidden` attribute; at count 2 or more the attribute is removed.

*Alternative considered:* keeping the pairwise A-vs-B branch and only comparing the first two cards. Rejected — silently ignores offers C and D, which is the whole point of the change.

### Palette extends to four accents

Add `--c` and `--d` to both the light `:root` block and the `prefers-color-scheme: dark` block, following the existing pattern (dark variants lightened for contrast on the dark card). Add `.offer.c{--accent:var(--c)}` and `.offer.d{--accent:var(--d)}`. Everything downstream — top border, heading, dot, focus ring via `color-mix` — already reads `--accent`, so no other CSS changes.

### One self-check behind `#selftest`

Non-trivial new logic here is the clone rewrite, the add/remove tail logic, and the verdict ranking. Guard it with a `demo()` that runs only when `location.hash === "#selftest"`, using plain `console.assert`-style throws:

- `calc()` with the current defaults still returns today's payment, total interest, and total cost (pins "math unchanged")
- `renderOffers(4)` yields 4 cards exposing `rate3` and `out3`; a value typed into card 0 survives `renderOffers(4)` then `renderOffers(2)`
- verdict ranking picks the minimum of a 3-cost array and reports the gap to the second-lowest

Opening `MortgageAnalysisTool.html#selftest` runs it; normal opens skip it entirely. No framework, no second file.

### Wording

Title and `h1` change from "Two-offer cost comparison" to analyzer wording that covers one or many offers; the `.sub` paragraph drops "then the terms of each offer" phrasing that assumes two. Footer method and PMI text is unchanged — the math it describes is unchanged.

## Risks / Trade-offs

- **String-rewrite cloning breaks on future markup edits** → self-check asserts the cloned ids exist; failure is loud and immediate rather than a silently dead input.
- **Four cards at a ~900px desktop window are cramped (~200px each)** → accepted; the count is the user's choice and mobile stacking still handles small screens. If it reads badly, the fix is a second breakpoint, scoped to CSS.
- **Inline `grid-template-columns` overriding the mobile rule** → mitigated with `!important` on the mobile declaration; verify at 390px with count 4 during implementation.
- **Default of 1 changes what returning users see on open** → intended and requested; the count control is in the shared card, one click from two-offer behavior.
- **Verdict semantics shift from "A vs B" to "cheapest vs next-cheapest"** → at count 2 the two readings are identical, so no regression for existing use.
- **Cloned readout markup carries card 0's stale rows for one frame** → `compute()` runs at the end of `renderOffers()`, so the stale rows never paint; clearing the clone's readout is a one-line belt-and-braces if it does.

## Migration Plan

Single-file edit, no deploy. Rollback is `git checkout MortgageAnalysisTool.html`. Verification: open the file, confirm one card and no verdict; step the count 1 to 4 and back, confirming values persist and columns follow; compare card 0's readout against the current tool's Offer A readout with identical inputs; check 390px width at count 4; open `#selftest` and confirm no failure.

## Open Questions

None. Count ceiling of 4, defaults-on-new-card, and no value restoration on re-add are design calls recorded above; any of them is a one-line change if the user wants otherwise.
