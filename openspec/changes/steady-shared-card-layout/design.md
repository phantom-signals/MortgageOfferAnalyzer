## Context

`MortgageOfferAnalyzer.html` is one self-contained file. Shared-input card:

```css
.shared{display:grid;grid-template-columns:1fr 1fr;gap:16px 24px}
```

Five `.field` children flow row by row, so PMI removal rule (right column, row 2) and PMI premium basis (left column, row 3) split across columns and rows. Home value, which drives PMI, sits in a third place.

Input sizing today:

```css
.inp{font-family:var(--mono);font-size:15px; ... padding:9px 11px}
@media (max-width:640px){ .inp{font-size:16px;padding:12px 12px} }
```

Every input, select, and the `#copyLink` share button carries `class="inp"`, and no other rule sets their font size. Crossing 640px while dragging the window therefore resizes and re-pads every input on the page at once.

Page body scale for reference: hint 11px, label 12px, readout row 13px, subtitle and fold summary 14px. `--mono` is wider per glyph than `--sans`, so 15px mono reads about as large as 16px sans, putting inputs above every other body element.

Constraints: no build step, no framework, no dependency. Script reaches inputs by id (`$("homeValue")`, `$("pmiThresh")`, `$("pmiBasis")`) and styles labels by descendant selector `.field label`, so extra wrapper elements are inert to it. `openspec/specs/page-layout` already requires 16px inputs at 640px and below (mobile focus auto-zoom suppression).

## Goals / Non-Goals

**Goals:**

- PMI removal rule and PMI premium basis render in one column, one above the other, on desktop.
- Home value groups with them, since it drives PMI.
- Input font size never changes with window width.
- Input type size sits level with the page's body scale instead of above it.
- Mobile single-column stacking and field order unchanged.

**Non-Goals:**

- Offer-card field layout, including each card's PMI annual rate input.
- Any change to computation, PMI lock rules, share-link encoding, glossary mapping.
- Other viewport-dependent type (h1 `clamp()`, `.row`, `#costTable`) stays as is.
- Font family of inputs stays `--mono`.

## Decisions

**Two wrapper divs, one per column.** Wrap fields in `<div class="shared-col">`: left holds loan amount and holding period, right holds home value, PMI removal rule, PMI premium basis. `.shared` keeps `grid-template-columns:1fr 1fr` with two children now; each wrapper is `display:flex;flex-direction:column;gap:16px`.

Alternatives rejected:

- `grid-column` on each `.field`. Sparse auto-placement advances the row cursor, so column-pinned items land on rows that depend on placement order; `dense` packing fixes it only by accident. Fragile for a purely visual result.
- `grid-auto-flow:column` plus fixed `grid-template-rows`. Column split then depends on a hard-coded row count that breaks the moment a field is added or removed.
- Two PMI selects inside one grid cell, home value left. Leaves home value away from the PMI group it feeds.

**Mobile unchanged by construction.** At 640px and below `.shared{grid-template-columns:1fr}` already applies; wrappers stack and their children keep document order, which is loan amount, holding period, home value, PMI removal rule, PMI premium basis — the current order. Wrapper gap matches `.shared` row gap (16px), so stacked spacing stays even.

**Input size keyed to pointer type, not window width.** `.inp` base drops to 14px; a `@media (pointer:coarse)` rule raises it to 16px and applies the touch padding. The `.inp` line leaves the `@media (max-width:640px)` block entirely.

```css
.inp{font-family:var(--mono);font-size:14px;padding:9px 11px; ...}
@media (pointer:coarse){.inp{font-size:16px;padding:12px 12px}}
```

Why the split at all: iOS Safari zooms the page when a field whose computed font size is under 16px takes focus, and it stays zoomed. Only touch input hits that, and `pointer:coarse` is the media feature that names it. A desktop window's pointer type does not change when the window is resized, so the size is fixed for the whole session on any given device — the resize complaint is answered without giving up the iOS guard.

Why 14px: dense tool interfaces (GitHub, Linear, admin panels) run 14px inputs; forms-first systems (Bootstrap, Material, GOV.UK) run 16px and up. This page is a calculator with an 11-14px body scale, so 14px mono sits level with the subtitle and fold summary rather than towering over the 13px readout rows.

Alternatives rejected:

- 16px flat everywhere. One size, simplest rule, but grows desktop inputs past every other element on the page and worsens the bulk this change is meant to fix.
- 14px flat everywhere. Constant, but iOS Safari zooms on every field focus and does not zoom back out.
- `maximum-scale=1` in the viewport meta to block the zoom at 14px flat. Blocks pinch-zoom for everyone; accessibility regression for a cosmetic gain.

**Padding follows the font.** The 12px touch padding moves into the same `pointer:coarse` rule. Leaving it at 640px would keep a width-triggered box-height jump after the font stopped jumping, which is the same defect in a different property.

## Risks / Trade-offs

- Wrapper divs make `.shared` no longer a flat grid of fields, so a future field must be added inside the intended wrapper, not as a direct `.shared` child → wrappers carry a comment naming the two groups.
- Column heights now differ (2 fields vs 3), leaving whitespace under the left column at desktop → accepted; grouping was the point.
- Desktop inputs render 1px smaller than today, so long values fit more easily and nothing overflows → no minimum is near; 14px stays above the 13px readout rows.
- A touchscreen laptop reports `pointer:coarse` and gets 16px inputs with a mouse attached → harmless; larger targets on a machine that can be touched.
- A device reporting `pointer:fine` that is nonetheless touched (iPad with trackpad attached, some hybrids) would get 14px and could zoom on focus → accepted; `hover`/`any-pointer` compounds add rules for a rare case.
- `page-layout` mobile scenario asserts 16px at phone width. A narrow desktop window now renders 14px there → delta restates the scenario in terms of a touch device rather than a width.

## Migration Plan

Single-file edit, no state, no persistence. Rollback: revert commit.

## Open Questions

None.
