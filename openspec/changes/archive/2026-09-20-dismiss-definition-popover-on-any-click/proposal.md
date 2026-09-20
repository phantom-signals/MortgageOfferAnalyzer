## Why

Definition popover opens on tapping a term label, but neither a tap on the popover itself nor a second tap on the label that opened it closes it. Reader must find empty page space to dismiss. The popover and the label are the two things the reader is looking at and pointing at, so they are the first places they tap — the current behaviour reads as a stuck popup.

## What Changes

- Clicking or tapping the definition popover itself closes it.
- Clicking or tapping the label that opened the popover closes it, instead of reopening it unchanged.
- Clicking a different label still swaps the text rather than closing.
- Popover becomes `manual`, so native light dismiss no longer closes it on the pointer press — that press is what made the re-tap undetectable. Outside-click dismissal moves into the existing click handler; Escape gets one `keydown` listener.
- Result: a click anywhere closes an open definition popover.
- No visual change: no close button, no cursor change, no marker.

## Capabilities

### New Capabilities

- none

### Modified Capabilities

- `term-glossary`: "Tapping a readout row label shows its definition" — dismissal is no longer "outside tap only, handled natively". Any click closes, including on the popover and on the opening label, and the requirement now states that dismissal is the page's own, with Escape still closing.

## Impact

- `MortgageOfferAnalyzer.html` — the `#defPop` element's `popover` attribute, the delegated definition click handler, a new Escape `keydown` listener, plus the `#selftest` block covering the tap path.
- Dismissal is now custom code rather than browser behaviour, so `#selftest` carries its cases: outside tap, popover tap, re-tap, different label, Escape, scroll.
- No computed value, layout, or style affected.
