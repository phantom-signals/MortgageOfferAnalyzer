All work lands in `MortgageOfferAnalyzer.html`. Verify with `#selftest` (title reads
`selftest passed`) plus the manual checks in group 5.

## 1. Count inference replaces the dropdown

- [x] 1.1 In `restore()`, derive the card count from the highest `rate<i>` key in the parsed params
      plus one, defaulting to 1 when no such key is present, and pass it to `renderOffers()` in place
      of `+$("offerCount").value`. Existing clamp handles anything above 4.
- [x] 1.2 Delete the menu-mirror line `$("offerCount").value = n;` from `renderOffers()`.
- [x] 1.3 Drop the `#offerCount` branch from the document `input` listener, leaving `compute()` as
      the sole handler.
- [x] 1.4 Delete the `#offerCount` field — label, hint, and `<select>` — from the `.shared` card.
- [x] 1.5 Confirm the boot default is still two cards: `DEFAULT_STATE` carries `rate1`, so no
      explicit count call is needed. Add none.

## 2. Heading becomes the fold trigger

- [x] 2.1 Move `<h2>` inside `<summary>` in the Offer A markup, ahead of the summary figure. Keep
      the steppers in the heading. Update the comment above `<details class="fold">`, which still
      says the heading stays outside.
- [x] 2.2 Wrap the summary figure in its own element and move `id="sum0"` onto it, so
      `$("sum"+i).innerHTML` in `compute()` keeps working untouched.
- [x] 2.3 Move the chevron from `.fold summary::before` to a pseudo-element on the heading, left of
      `.dot`, colored `var(--accent)`; keep the rotation rule on `.fold[open]`.
- [x] 2.4 Scope `.fold[open] summary{font-size:12px;font-weight:400;color:var(--slate)}` to the
      summary figure only, so the heading keeps its size, weight, and accent color in both states.
- [x] 2.5 Re-check `card0HTML` still captures the card before any edit, and that clones carry the
      boot fold state.

## 3. Steppers stop toggling the fold

- [x] 3.1 Add `e.preventDefault()` to the delegated `[data-step]` handler on `.offers`, before it
      adds or removes a card.
- [x] 3.2 Verify by keyboard as well as pointer: Tab to a stepper, press Enter and Space, confirm the
      count changes and the fold does not.

## 4. Self-check

- [x] 4.1 Remove the `$("offerCount").value` assertions from the stepper test and keep the card-count
      and value-shift assertions.
- [x] 4.2 Replace `$("offerCount").value = "3"; renderOffers(3);` and the later
      `$("offerCount").value = "1"; renderOffers(1);` in the round-trip test with direct
      `renderOffers()` calls.
- [x] 4.3 Add an assertion that restoring a hash carrying an `offerCount` key alongside `rate0`
      through `rate2` renders three cards and ignores the stale key.
- [x] 4.4 Add an assertion that a hash with a sparse per-offer key (`rate3` and no `rate1`/`rate2`)
      renders four cards and lands the value on card D.
- [x] 4.5 Add an assertion that clicking a stepper leaves the card's `.fold` `open` state unchanged.
- [x] 4.6 Replace the teardown's `$("offerCount").value = "1"; … renderOffers(+$("offerCount").value)`
      with `offers.innerHTML = card0HTML; restore(DEFAULT_STATE);` so the page returns to its
      post-boot state.
- [x] 4.7 Run `#selftest` and confirm the title reads `selftest passed`.

## 5. Manual verification

- [x] 5.1 At 1280px: two cards on load, each heading shows an accent chevron, clicking the heading
      folds and unfolds, heading type does not change between states.
- [x] 5.2 At 390px: cards load collapsed, heading and payment figure visible, steppers operable.
- [x] 5.3 Open a link produced before this change (one containing `offerCount`) and confirm it
      restores the same card count and values.
- [x] 5.4 Confirm the shared card reads correctly with the dropdown gone and no gap in the grid.

## 6. Add control inserts where it is pressed

- [x] 6.1 Replace `.offer:not(:last-child) .step-plus` and `.offer.d .step-plus` with a single
      `.offers:has(> .offer:nth-child(4)) .step-plus` rule, so `[+]` shows on every card and is
      unavailable only at four offers.
- [x] 6.2 Add `insertOffer(i)` beside `removeOffer(i)`, appending the clone, reading its defaults
      back, then shifting the displaced rows down through `getVal`/`setVal`.
- [x] 6.3 Point the delegated `[data-step]` handler at `insertOffer(i)` with the pressed card's
      index, replacing `renderOffers(offers.children.length + 1)`.
- [x] 6.4 Update the add button's `aria-label` to name the position it fills.
- [x] 6.5 Add assertions that `[+]` on the first of three cards renders four, lands the new card
      second at its defaults, shifts the rest down, and that `[+]` is hidden on every card at four
      offers and visible on every card below four.
- [x] 6.6 Run `#selftest` and confirm the title reads `selftest passed`.
