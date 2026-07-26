## Why

The mortgage comparison tool is locked to a 920px column, and its prose blocks are clamped tighter still (`.sub` at `60ch`, `footer p` at `70ch`) — roughly the width of a single offer card. On a wide monitor the page leaves most of the window empty while the explanatory text and the two offer cards stay cramped, forcing extra scrolling to read the method and PMI notes.

## What Changes

- Remove the `max-width:920px` cap on `.wrap` so the whole tool fills the browser window, bounded only by the existing responsive body padding.
- Remove the `max-width:60ch` clamp on the header subtitle (`.sub`) and the `max-width:70ch` clamp on footer paragraphs so prose spans the full content width.
- Shared-input grid, offers grid, verdict bar, and footer all widen with the viewport; the two offer cards remain side by side and grow together.
- No change to the mobile breakpoint behavior at `max-width:640px` (single-column stacking is preserved).
- No change to calculation logic, inputs, outputs, or any JavaScript.

## Capabilities

### New Capabilities
- `page-layout`: How the mortgage tool distributes horizontal space across the viewport — container width, prose line-length policy, offer-card arrangement, and responsive stacking.

### Modified Capabilities
<!-- None. openspec/specs/ is empty; this is the first capability captured for this project. -->

## Impact

- `MortgageAnalysisTool.html` — CSS block only (`.wrap`, `.sub`, `footer p`). Single-file tool, no build step, no dependencies.
- Readability tradeoff: on very wide monitors, unclamped prose produces long measure lines. Accepted per explicit user decision to make everything full window.
- Distribution unaffected — the file is still a self-contained HTML document opened directly from disk (including the no-JavaScript email-attachment path).
