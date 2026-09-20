## Why

Shared-input card flows 5 fields through a 2-column grid row by row, so the two PMI selects land in different columns on different rows: PMI removal rule right column row 2, PMI premium basis left column row 3. PMI parameters read as unrelated. Separately, input font size jumps 15px to 16px when window crosses 640px, so text resizes under the cursor while dragging the window narrower. 15px mono also reads bulky against this page's body scale (hint 11px, label 12px, row 13px, subtitle 14px).

## What Changes

- Shared card splits into two column groups: left holds loan amount and holding period, right holds home value, PMI removal rule, PMI premium basis. All PMI-driving inputs sit in one column, in order.
- Mobile (640px and below) keeps single-column stacking, field order unchanged: loan amount, holding period, home value, PMI removal rule, PMI premium basis.
- Input font size stops depending on window width. Pointer type decides it: 14px on fine pointers (mouse, trackpad), 16px on coarse pointers (touch). Dragging a window narrower never changes it; iOS focus auto-zoom stays suppressed on touch, where it applies.
- Input padding moves to the same pointer rule, so the 640px breakpoint changes nothing about input boxes.
- No change to input ids, values, computation, PMI lock behavior, or share-link encoding.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `page-layout`: shared-input card gains a column-grouping requirement (PMI inputs share one column on desktop, stacked order preserved on mobile). Input font size becomes pointer-dependent (14px fine, 16px coarse) instead of width-dependent.

## Impact

- `MortgageOfferAnalyzer.html`: `.shared` markup gains two wrapper divs; `.shared` / `.inp` CSS and the `@media (max-width:640px)` block edited.
- No script, no dependency, no data change. Offer-card field layout untouched.
