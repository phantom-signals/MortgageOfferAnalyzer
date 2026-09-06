## Why

Definitions reach the reader through the `title` attribute set by `annotate()` on input labels and readout row labels. `title` needs hover. Touch devices have no hover, so on phones every definition is unreachable at the point of use — the reader must scroll to the footer glossary and lose their place. Definitions already exist and are already wired; only delivery fails on touch.

## What Changes

- Tapping a readout row label that carries a definition opens that definition in a popover.
- Popover uses native HTML Popover API — one shared element, top layer, native light dismiss and Escape. No positioning library, no per-label markup, no new dependency.
- Popover text is read from the `title` `annotate()` already set, so definitions keep their single source in the footer glossary.
- Input labels (`.field label`) stay out of scope. A `<label for=...>` click focuses its control; opening a popover there would fight the keyboard on mobile. Input labels already carry inline `.hint` prose, and every one of their terms also appears in a readout row or the glossary.
- No visible marker. No dotted underline, no icon, no layout change. Desktop hover behaviour unchanged.
- One touch-only hint sentence appended to the existing intro paragraph, hidden on pointer devices. Static text, no dismissal state, no storage.

## Capabilities

### New Capabilities

None. Definition delivery already belongs to `term-glossary`.

### Modified Capabilities

- `term-glossary`: gains tap-to-open delivery on readout rows, an explicit no-marker guarantee, and a touch-only hint. Existing hover requirement unchanged — this adds a second path, it does not replace one.

## Impact

- `MortgageOfferAnalyzer.html` only. Single file, no build step, no dependency.
- CSS: one popover ruleset, one touch-only hint rule.
- Markup: one `<div popover>`, one `<span>` inside the existing intro paragraph.
- JavaScript: one delegated click listener on `document`. Readout rows re-render on every input change, so the listener must be delegated, not per-element. `annotate()` unchanged.
- No input, control, calculation, or rendered figure changes.
- Browser floor: Popover API is Baseline — Chrome 114, Safari 17, Firefox 125. Older browsers keep hover-only behaviour plus the footer glossary; nothing breaks.
