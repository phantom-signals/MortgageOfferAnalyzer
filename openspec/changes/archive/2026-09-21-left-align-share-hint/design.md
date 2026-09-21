## Context

`MortgageOfferAnalyzer.html` is one self-contained file: inline stylesheet, inline script, no build. The share block is three rules:

```css
.share{text-align:center;margin:18px 0 6px}
.share .inp{width:auto;min-width:14em;background:var(--card);cursor:pointer}
.share .hint{display:block;max-width:52ch;margin:6px auto 0}
```

`text-align:center` on `.share` does two jobs at once. It centers the inline-level button, and it inherits into the hint, centering each wrapped line of the disclosure sentence. The hint is already a centered block (`max-width` plus `margin:…auto`); the inherited alignment is what centers the lines inside that block.

Every other prose block on the page wraps left-aligned. The hint is the only multi-line paragraph rendering centered, and at mobile widths it wraps to three or four lines.

## Goals / Non-Goals

**Goals:**

- Lines of the disclosure text start at a common left edge.
- Button stays centered. Hint block stays centered under it, same measure.

**Non-Goals:**

- No change to copy-link behavior, hash serialization, or clipboard handling.
- No change to the hint's wording, font size, color, measure, or margins.
- No new alignment scheme for other `.hint` elements; the popover and label hints elsewhere are unaffected.

## Decisions

**Override alignment on the hint, keep it on `.share`.** Add `text-align:left` to the existing `.share .hint` rule. One declaration in a rule that already exists, and the button keeps the centering it relies on.

Alternative: drop `text-align:center` from `.share` and center the button some other way (`.share .inp{display:block;margin-inline:auto}` or making `.share` a centered flex column). Larger diff, touches the button's layout to fix the text's, and the button is currently inline-level so the change is not free. Rejected.

**Left, not justified.** The measure is 52ch and on a phone the real line length is narrower still. Justification at that width stretches inter-word space unevenly, the classic river artifact, and CSS gives no hyphenation control worth relying on here. Ragged right reads better at short measures and matches every other paragraph on the page.

**One assertion in `#selftest`.** The file's self-check already reads computed styles (`.step-plus` visibility, grid `rowGap`). Add one `ok()` asserting the hint's computed `textAlign` is `left`. That is the exact regression the inherited-center rule would reintroduce.

## Risks / Trade-offs

- Someone later restructures `.share` into flex and drops the hint rule, re-inheriting center → the `#selftest` assertion fails and names the cause.
- Left-aligned text under a centered button is a mild asymmetry → intended; the block stays centered, so the asymmetry is limited to the ragged right edge, same as the footer paragraphs above it.
- Long words could still overflow at very small widths → unchanged from today, alignment does not affect it.
