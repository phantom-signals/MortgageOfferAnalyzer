## Why

Two controls set the offer count: the `Offers` dropdown in the shared-inputs card and the per-card
`[−]`/`[+]` steppers. Steppers sit where the cards are and cover every count the dropdown covers, so
the dropdown is redundant surface in the card a reader meets first.

Separately, the fold control is missed on desktop. The chevron lives on the summary row, which
renders as 12px grey caption text under the heading once the card is expanded — it reads as a label,
not a control, so readers do not learn that cards collapse.

## What Changes

- Remove the `Offers` dropdown (`#offerCount`) and its hint from the shared-inputs card. Per-card
  steppers become the only offer-count control.
- Move the fold chevron into the card heading, left of the color dot, in the accent color. Heading
  moves inside `<summary>`, so the whole heading row is the fold trigger.
- Steppers stay adjacent, right side of the heading. `[−]` removes the card it sits in, unchanged.
  `[+]` now inserts a card directly after the card it sits in, rather than appending at the tail, and
  appears on every card instead of only the last. No third button — `[−]` already is the remove
  control.
- **BREAKING (link format, tolerated):** the hash no longer carries `offerCount`. Restore infers the
  card count from the highest `rateN` key present. Links made before this change still restore
  correctly, since they carry `rate0..rateN`; their `offerCount` key drops through the existing
  unknown-key path.
- Boot default stays 2 offers, with no new code: `DEFAULT_STATE` carries `rate1`, so the inference
  above yields 2. The count default stops being split between the markup and `DEFAULT_STATE`.
- Folded state stays out of the hash, unchanged.
- Corrects spec drift: `offer-set` and `share-link` both describe a boot default of 1 offer. Shipped
  behavior is 2 and is correct. Both drifted scenarios sit inside requirements this change already
  modifies, so the deltas restate them at 2. No behavior change.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `offer-set`: "Offer count is user-selectable" — the control moves from a shared-inputs dropdown to
  per-card steppers. Range stays 1..4. Clamping now comes from stepper bounds, not from a rejected
  menu value.
- `offer-set`: "Changing the count preserves entered values" — cards are no longer added and
  removed only at the tail. Add fills the position after the card pressed; remove drops the card
  pressed. Scenarios that drove the count through the dropdown are restated on the steppers.
- `page-layout`: "Card readouts fold on small viewports" — the heading moves inside the disclosure
  control instead of outside it, and the heading row becomes the fold trigger. Steppers must still
  operate while collapsed, now without toggling the fold.
- `share-link`: "Entered state serializes into the URL hash" — offer count leaves the shared-field
  list. "A link restores the state it encodes" — count is inferred from the encoded offer fields.

## Impact

Single file: `MortgageOfferAnalyzer.html`.

- Markup: `#offerCount` field deleted from `.shared`; `<h2>` moves inside `<summary>`; chevron moves
  from `.fold summary::before` to the heading.
- CSS: chevron rules move to the heading and take `var(--accent)`; summary keeps the payment line.
- Script: drop the `#offerCount` branch in the input listener and the menu-mirror line in
  `renderOffers()`; add `preventDefault()` on stepper clicks so they do not toggle the fold; boot
  `restore()` derives the count from `rateN` keys, which also carries the boot default.
- Self-check: menu-sync assertions go; add a restore-without-`offerCount` assertion and a
  stepper-does-not-toggle-fold assertion.

Lost: the dropdown hint "1 analyzes a single offer; 2 or more compares them". The header subtitle
already says "the terms for 1 to 4 offers". Accepted, no replacement text.
