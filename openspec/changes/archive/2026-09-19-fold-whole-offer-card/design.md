## Context

Offer card today: `h2` heading, five `.field` inputs, then `details.fold` holding `summary#sumN` and `.readout#outN`. Summary prints payment incl. PMI plus headline total (walk-away or to-term). Offer A markup is clone source for B–D via `card0HTML`; initial `open` set on Offer A once at load, clones inherit.

## Goals / Non-Goals

**Goals:**
- Collapsed card = heading + one-line payment summary.
- Keep native `<details>`; no new JS state.

**Non-Goals:**
- Changing default open rule (phone collapsed, desktop expanded).
- Per-offer remembered state across reloads or in share link.
- "Collapse all" control.

## Decisions

- **Move `<details class="fold">` up to wrap all five `.field`s and `.readout`.** `h2` stays outside so steppers and name stay visible and clickable without toggling. Alternative: second `<details>` for inputs. Rejected: two toggles per card, more to explain, no gain.
- **Summary = payment only.** Keep existing text: `money2(res.M + res.pmiFirst)` + "per period" / "incl. PMI". Payments-per-year input can be non-12, so "per period" stays accurate; "monthly" would lie at freq 26. Invalid input still prints "Enter valid inputs" — needed now, since collapsed inputs hide the error source.
- **Summary styling when open.** Existing `.fold[open] summary` rule shrinks summary to slate small text. Keep: when open, readout row already shows payment.
- **Inputs hidden while collapsed stay in form.** `<details>` keeps closed content in DOM; `$("rateN")` reads, share-link load, PMI lock all keep working. No code change there.

## Risks / Trade-offs

- [Share link loads values into collapsed cards on phone; reader cannot see inputs until expand] → Summary payment reflects loaded values; one tap reveals inputs. Accept.
- [PMI lock toggles `disabled` on hidden input] → Invisible while closed, visible on open. No figure changes. Accept.
- [Focus inside card when closing] → Native `<details>` handles; closed content not focusable.

## Open Questions

- Should desktop start collapsed too, now that fold hides more? Default here: no, keep current rule. Say so if wanted.
