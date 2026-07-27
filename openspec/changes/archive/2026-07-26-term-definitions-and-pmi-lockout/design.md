## Context

`MortgageAnalysisTool.html` is one self-contained file: inline CSS, inline IIFE, no build step, no dependencies, opened from disk or an email attachment. Offer A's markup is the clone template for B through D (`card0HTML`), so anything added to a card must survive `renderOffers()` re-cloning.

Two existing facts drive this change:

- `calc()` already decides PMI applicability: `const required = hv>0 && (P/hv) > 0.80 + 1e-12;`. When false, `totalPMI` is 0 and the readout prints "PMI none" no matter what the PMI rate input holds. The input and the output disagree today.
- The two shared selects (`pmiThresh`, `pmiBasis`) already carry long `title` text on the control and on each option. Native `title` is the established tooltip mechanism in this file. Nothing new needs inventing.

## Goals / Non-Goals

**Goals:**
- Every jargon term the tool prints has a written definition on the page.
- Hovering an input label or a readout row label shows that definition.
- PMI rate input is 0 and disabled exactly when the tool charges no PMI.
- Definition text exists once in the file.
- Zero change to any computed figure.

**Non-Goals:**
- No custom tooltip widget, popover, or definition-on-click UI.
- No glossary search, filtering, anchor links, or per-term deep links.
- No change to `calc()`, `horizon()`, `render()` math, or the PMI schedule.
- No new PMI rule. The lock mirrors the rule `calc()` already applies.
- No lockout of any other input.

## Decisions

### Glossary is static markup, tooltips are derived from it

Glossary goes in the footer as a plain `<dl id="glossary">`. Each entry:

```html
<dt data-match="PMI|mortgage insurance">PMI &mdash; private mortgage insurance</dt>
<dd>Insurance the lender requires while the loan is large relative to the home's value; it protects the lender, not you, and is charged on top of principal and interest.</dd>
```

Script builds the tooltip map by walking that `<dl>` once at load. `data-match` is a `|`-separated list of snippets that identify the term inside a label; it sits next to the definition it belongs to, so a new term is one markup block with nothing to update elsewhere.

Alternative rejected: a `DEFS` object in the script rendering the glossary at runtime. Same line count, but the glossary disappears for JavaScript-disabled viewers — and this file is explicitly opened as an email attachment where scripts are blocked. Static markup keeps the definitions readable in exactly the case where the numbers are not.

Alternative rejected: `title` written by hand on every label. Duplicates each definition two-to-four times across Offer A's labels and the readout rows; drifts on first edit.

### Tooltips applied by one DOM pass

`annotate(root)` sets `title` on every `.field label` and every `.row .k` inside `root` that has no `title` yet, using the first glossary entry whose `data-match` token appears in the element's `textContent` (case-insensitive). Called after `renderOffers()` (covers cloned cards' labels) and after each readout `innerHTML` write in `compute()`.

Matching runs against `textContent`, not the HTML string, so entity-encoded labels such as `Payment, P&amp;I (per period)` compare as the decoded text. First-match-wins in document order, so the glossary is ordered specific-before-general (an "amortization midpoint" entry precedes "amortization"). This is a naive substring scan over roughly 20 entries times roughly 20 rows per card — irrelevant at this size, and it keeps the mapping declarative.

The two shared selects already carry richer hand-written `title` text; `annotate` skips any element that already has one, so that text is preserved.

### PMI lock lives in `compute()`, next to the value it mirrors

`compute()` already parses `P` and `hv`. It gains the same predicate `calc()` uses:

```js
const pmiRequired = hv > 0 && P > 0 && (P/hv) > 0.80 + 1e-12;
```

and, at the top of the per-offer loop, before the PMI rate is read:

```js
const pmiEl = $("pmi"+i);
if(!pmiRequired && !pmiEl.disabled){
  pmiEl.dataset.prev = pmiEl.value;   // survives lock; restored on unlock
  pmiEl.value = "0";
  pmiEl.disabled = true;
  pmiEl.title = LOCK_NOTE;
} else if(pmiRequired && pmiEl.disabled){
  pmiEl.value = pmiEl.dataset.prev ?? pmiEl.value;
  pmiEl.disabled = false;
  pmiEl.removeAttribute("title");
}
```

Placing the lock before the `parseFloat($("pmi"+i).value)` read keeps input and readout consistent within a single pass — no second compute, no flicker of a stale figure.

The stash needs no initialization step. A card that loads or clones into a locked state stashes the value the markup gave it (`0.55`), so the first unlock restores the default rather than the zero the lock wrote. Duplicating the predicate in `compute()` rather than returning it from `calc()` is deliberate: `calc()` is called once per offer with per-offer arguments, while the lock is a property of the shared inputs alone, and the predicate is one line. If a third caller ever needs it, hoist it then.

### Disabled styling is a CSS rule, not a class

```css
.inp:disabled{background:var(--line);color:var(--slate);cursor:not-allowed;opacity:1}
```

`--line` and `--slate` are already defined per color scheme, so dark mode is covered with no second rule. `opacity:1` overrides the WebKit/Blink default that washes out disabled controls, which would otherwise make the grayed field illegible on the dark card background. The native `disabled` attribute also removes the field from tab order, which a class alone would not.

## Risks / Trade-offs

- Native `title` does not appear on touch devices and has a browser-controlled delay on desktop. Mitigation: the footer glossary is the primary artifact and is always visible; hover is the convenience path, not the only path.
- Substring matching can attach the wrong definition if a new label happens to contain an earlier entry's token. Mitigation: glossary ordered specific-before-general, and the self-check asserts a fixed set of label-to-definition pairs, so a bad match fails loudly rather than silently.
- Locking on `P` or `hv` being blank means a user mid-retype of the loan amount sees the PMI field gray briefly. Mitigation: the value is stashed and restored on the next valid keystroke, so nothing is lost; the alternative (a separate "inputs incomplete" state) adds a branch to prevent a transient that self-heals.
- Disabled input value is forced to 0, so a printed or saved page shows 0 rather than the user's earlier PMI rate. Accepted: 0 is the rate the tool actually applies at that LTV, and the readout already said so.
- Glossary lengthens the footer. Accepted: the page already spans full window width, so the definition list wraps wide and stays short vertically.

## Migration Plan

Single file, no persisted state, no deploy target. Rollback is `git checkout` of `MortgageAnalysisTool.html`. Verification is the existing `#selftest` hash, extended with the lock and tooltip cases; the pinned math assertions in `demo()` must pass unchanged, which is the guard that no computed figure moved.

## Open Questions

None. The one ambiguity — the request read "gray out when initial LTV >= 80%" while `calc()` charges PMI above 80% — was resolved to lock at LTV **<= 80%**.
