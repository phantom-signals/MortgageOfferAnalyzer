## Context

`MortgageAnalysisTool.html` is a single self-contained HTML file — no build step, no dependencies, no external assets — designed to be opened straight from disk or read as an email attachment. All layout lives in one `<style>` block in the head.

Three CSS rules produce the reported problem:

| Rule | Current value | Effect |
| --- | --- | --- |
| `.wrap` | `max-width:920px;margin:0 auto` | Centers everything in a 920px column regardless of window width |
| `.sub` | `max-width:60ch` | Header subtitle wraps at ~60 characters |
| `footer p` | `max-width:70ch` | Method and PMI paragraphs wrap at ~70 characters |

At the 14px/12px sizes in use, `60ch` and `70ch` land near 420–460px — almost exactly one offer-card column inside the 920px grid. That is why the prose appeared to widen only to "the width of one offer."

The user chose full-window for everything, not just prose: container cap and measure clamps both go.

## Goals / Non-Goals

**Goals:**
- Content fills the browser window at any width, bounded only by the existing `clamp(16px,4vw,48px)` body padding.
- Header subtitle and footer paragraphs wrap at the container edge.
- Offer cards stay side by side and grow together.
- Mobile behavior at `max-width:640px` is untouched.
- File stays single-file, dependency-free, and functional with JavaScript disabled.

**Non-Goals:**
- No change to calculation code, inputs, outputs, or the `<script>` block.
- No new breakpoints, no multi-column prose, no reflowing offers into more than two columns on ultrawide displays.
- No restructuring of the HTML or splitting the file into modules.
- No change to typography scale, colors, or the dark-mode palette.

## Decisions

### Remove `max-width` from `.wrap` rather than raising it

`.wrap` becomes a pass-through: `margin:0 auto` can stay (harmless with no cap) or the rule can be dropped to `.wrap{}`. Body padding already provides the viewport inset, so no new spacing rule is needed.

*Alternative considered:* raising the cap to a large fixed value such as `1600px`. Rejected — it re-creates the same complaint one monitor size up and adds an arbitrary number to maintain.

*Alternative considered:* `max-width:100%` plus explicit horizontal padding on `.wrap`. Rejected — duplicates the body padding that already exists and would double the inset.

### Remove the `ch` clamps outright instead of widening them

`.sub` drops `max-width:60ch`; `footer p` drops `max-width:70ch`. Both then inherit the container width.

*Alternative considered:* widening to `100ch` / `120ch` as a readability compromise. Rejected — the user explicitly asked for full window after being shown the prose-only option. A measure clamp is the exact thing being removed.

### Leave the offers grid untouched

`.offers{grid-template-columns:1fr 1fr}` already produces two equal fluid columns; it inherits the new full width for free. Same for `.shared{grid-template-columns:1fr 1fr}`.

### Verify `.row` behavior at large widths

Readout rows use `display:flex;justify-content:space-between`, so widening pushes the label and value to opposite edges of a much wider card. `.row .v` already carries `white-space:nowrap`, so numbers will not break. This is cosmetic stretch, not breakage — the spec pins the behavior so it gets checked rather than assumed.

## Risks / Trade-offs

- **Long measure lines on ultrawide monitors hurt prose readability** (a 3440px window yields ~400-character lines) → Accepted deliberately: the user was shown the prose-only alternative and chose full window. Reversible by restoring one `max-width` line if it reads badly in practice.
- **Label/value pairs in readout rows separate by a wide gap on very large screens** → Verify visually during implementation; if unacceptable, the fix is scoped to `.row` and does not affect this change's container decisions.
- **Regression in the `noscript` email-attachment path** → That block uses inline styles and no width constraint, so it inherits the container; confirm it still renders during verification.
- **Unnoticed calculation regression** → The change is CSS-only. Verification compares the full readout for the default inputs before and after.

## Migration Plan

Single-file edit, no deploy step. Rollback is restoring the three `max-width` declarations. Verification is manual browser inspection at four widths (~2560px, ~1440px, 900px, 390px) plus a before/after value comparison with default inputs.

## Open Questions

None. The one material ambiguity — whether "full window" meant prose only or the entire tool — was resolved with the user before writing this design.
