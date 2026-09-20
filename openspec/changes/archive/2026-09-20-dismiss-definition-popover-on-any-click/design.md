## Context

`#defPop` is a native auto popover, filled and opened by one delegated `click` listener on `document` (`MortgageOfferAnalyzer.html`, near the `DEFS` block). Auto popovers light-dismiss on an outside pointer press and on Escape; a press inside the popover is not a dismissal, so today the popover ignores taps on itself.

Light dismiss runs on pointer press, before the `click` event reaches the document listener. That is why the existing handler calls `hidePopover()` before `showPopover()` — by click time an outside press has already closed it.

## Goals / Non-Goals

**Goals:**

- Tap on the popover closes it.
- Keep outside-click and Escape dismissal exactly as the browser provides them.
- No visual change, no new element, no new state.

**Non-Goals:**

- Close button or any visible dismissal affordance.
- A close button or any other visible control.
- Any change to which labels open a definition, or to the definition text.

## Decisions

**Popover becomes `manual`; the existing delegated `click` listener owns every dismissal.** The listener hides the popover first, then reopens it only for a label that is not the one already showing:

```js
const same = el && defPop.matches(":popover-open") && defPop.textContent === el.title;
defPop.hidePopover();
if(!el || !el.title || same) return;
```

Auto light dismiss has to go, because it is what makes the same-label re-tap impossible to detect: it closes the popover on the pointer press, so by the time the `click` event reaches the listener `:popover-open` is already false and the press is indistinguishable from a first open. With `manual`, nothing closes the popover except this listener, so its own read of `:popover-open` is the truth. Outside clicks are covered by the unconditional `hidePopover()` at the top; a click on the popover itself reaches the same line, so the separate `#defPop` listener is dropped.

`manual` also drops the native Escape close request, so one `keydown` listener restores it. Alternatives:

- Keep `auto`, track the last-opened element in a variable — Escape and scroll dismissal leave the variable stale, so the next tap on that label would refuse to open. Fixing that needs a timestamp heuristic to guess whether the in-flight press was the dismissal. Rejected: guesswork in a path that has a deterministic answer.
- `closedby="closerequest"` on an `auto` popover — exactly the right semantics (Escape yes, light dismiss no), but it is a 2025 addition; where it is unsupported the attribute is ignored and light dismiss silently comes back, taking the re-tap fix with it. `manual` plus one line works wherever the Popover API does.
- Close button in the popover — adds a visible control the existing spec forbids ("no visible marker").

**`same` compares definition text, not element identity.** Two labels sharing one definition render an identical popover, so treating a tap on the second as a re-tap closes a popover showing exactly the text the reader would otherwise get again. Saves tracking an element.

**Selftest extended in place.** The existing tap-path block in `#selftest` opens the popover already; assert that a click on `pop` closes it, next to the scroll-dismiss assertion.

## Risks / Trade-offs

- Text selection inside the popover — a drag to select a definition ends in a `click`, which now closes the popover. Mitigation: definitions are one sentence and also live in the footer glossary, which is selectable; not worth a `getSelection()` guard.
- Future interactive content in the popover (a link) would be closed by the same listener. Mitigation: none needed now — the popover holds plain text only; add a `closest("a")` bail if a link is ever added.
- Dismissal is now custom code, so a path that bypasses the document listener leaves the popover stuck. Mitigation: the listener is on `document` and hides unconditionally; Escape and scroll keep their own listeners; `#selftest` asserts the popover is `manual` and covers outside-tap, popover-tap, re-tap, Escape, and scroll.
