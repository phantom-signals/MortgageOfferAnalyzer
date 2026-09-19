## Why

Light-mode verdict bar clashes. Near-black slab (`--verdict-bg:#161a1d`) sits on pale page, and offer letters inside render in light-mode accents, tuned for white background, so teal and dark red fight black. Dark mode pairs lightened accents with dark bar and looks right; leave it alone.

## What Changes

- Light mode: verdict bar moves to light surface (card background, ink text, card border), so offer letters sit on background their accents were chosen for.
- Dark mode: verdict bar unchanged.
- Chart tooltip and definition popover keep dark `--verdict-bg` in both schemes; only verdict bar changes.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `page-layout`: add requirement for verdict bar colors per color scheme.

## Impact

- `MortgageOfferAnalyzer.html`: CSS tokens in `:root` and dark `@media` block, `.verdict` rule.
- No JS change. Verdict text, amount, letter coloring logic unchanged.
