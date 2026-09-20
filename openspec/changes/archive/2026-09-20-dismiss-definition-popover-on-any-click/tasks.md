## 1. Implementation

- [x] 1.1 In `MortgageOfferAnalyzer.html`, inside the existing `if(defPop.showPopover){ ... }` block, add a `click` listener on `defPop` that calls `defPop.hidePopover()`
- [x] 1.2 Comment it in one line: a press inside an auto popover is not a light dismiss, so the tap on the popover is handled here

## 2. Verification

- [x] 2.1 In the `#selftest` tap-path block, after the popover is confirmed open, assert `pop.click()` leaves `!pop.matches(":popover-open")`
- [x] 2.2 Run `#selftest` headless; all checks pass
- [x] 2.3 Superseded by 3.8, which covers the same taps plus the re-tap
- [x] 2.4 Confirm no layout or style diff at rest and no new element in the DOM

## 3. Re-tap on the same label

- [x] 3.1 Change `#defPop` to `popover="manual"` so light dismiss stops closing the popover on the pointer press
- [x] 3.2 In the delegated document `click` listener, read `same` (popover open and its text equals `el.title`) before hiding, hide unconditionally, and return without reopening when `same`
- [x] 3.3 Drop the now-redundant `#defPop` click listener — the document listener's unconditional hide covers a tap on the popover
- [x] 3.4 Add a `keydown` listener closing on Escape, which `manual` no longer does natively
- [x] 3.5 In `#selftest`, change the `pop.popover === "auto"` assertion to `"manual"` with a message naming the custom dismissal
- [x] 3.6 In `#selftest`, assert a second click on the opening label leaves the popover closed, and that Escape closes an open popover
- [x] 3.7 Run `#selftest` headless; all checks pass
- [x] 3.8 Manual check on device: tap a row label, tap it again — closes; tap another label — text swaps; tap the popover — closes; tap outside — closes; Escape — closes
