## Context

Single-file tool, no build step, no framework. Offer count has two controls today: the `#offerCount`
select in the shared-inputs card, and per-card `[−]`/`[+]` steppers in each card heading. The select
also does hidden work — it is a `select.inp`, so `serialize()` writes it into the hash and `restore()`
reads it back to decide how many cards to render before per-card ids exist.

Folding is a native `<details class="fold">`. The heading sits outside it, so steppers stay operable
while collapsed. The disclosure chevron is `.fold summary::before`: 6px, `var(--slate)`, on a summary
row that renders at 12px grey once expanded. That row reads as a caption, so desktop readers do not
discover that cards fold.

## Goals / Non-Goals

**Goals:**

- One offer-count control, on the cards.
- Fold affordance legible in the expanded state on desktop.
- Old share links keep restoring.

**Non-Goals:**

- Folded state in the hash. Explicitly rejected — the sender's fold is not the reader's concern.
- Changing what `[−]` and `[+]` do, or the 1..4 range.
- Any change to calculation, verdict, charts, or readout content.
- A text label on `[+]` at count 1. The header subtitle already says "1 to 4 offers".

## Decisions

### Heading moves inside `<summary>`; chevron becomes `h2::before`

Putting the chevron in the heading row requires the heading to be the disclosure trigger. Two ways:

1. Native — move `<h2>` inside `<summary>`. Whole heading row toggles. Keyboard, `aria-expanded`,
   and the open/closed state come from `<details>` unchanged.
2. JS — keep the heading outside and add a chevron button that sets `details.open`, plus
   `aria-expanded` upkeep, plus suppression of the now-duplicate summary chevron.

Native wins: less code, and the hit area grows to the full heading row rather than a 24px button.

The chevron stays a pseudo-element, moved from `.fold summary::before` to `.offer h2::before`, in
`var(--accent)` so it reads as part of the card's color key next to the dot. Rotation on
`.fold[open]` is unchanged.

Consequence: `.fold[open] summary{font-size:12px;font-weight:400;color:var(--slate)}` currently
restyles the whole summary when expanded. With the heading inside, that rule would shrink the
heading too, so it must be scoped to the payment line. The payment line therefore becomes an inner
element carrying `id="sum<i>"`, which leaves `compute()`'s `$("sum"+i).innerHTML` write untouched.

### Steppers cancel the fold toggle with `preventDefault()`

Steppers now live inside `<summary>`, so a press would also toggle the disclosure. The existing
delegated listener on `.offers` already intercepts `[data-step]` clicks; one `e.preventDefault()`
there cancels the toggle. The default action runs after dispatch completes, so cancelling during
bubbling is enough, and it covers keyboard activation since Enter and Space on a button fire `click`.

Alternative rejected: `pointer-events` or a nested `<div>` outside the summary. Both fight the
layout to avoid a single line of JS.

### `[+]` inserts after its own card, on every card

`[+]` appeared only on the last card, because it appended at the tail: a `[+]` on Offer A would have
added a card at the far end, acting somewhere other than where it was pressed. With the dropdown
gone the steppers are the only count control, so hiding the control on every card but one makes the
affordance scarce exactly where a reader looks for it.

Instead `[+]` now fills the position it names — the mirror of `[−]`, which already removes the card it
sits in — and appears on every card. `renderOffers()` still only adds at the tail, so `insertOffer()`
appends the clone, reads that clone back for the default values, then shifts the displaced rows down
by position. This reuses `removeOffer()`'s idiom, including `getVal`/`setVal`, so a locked PMI field
moves through its stash rather than through the "0" it displays.

The ceiling moves from `.offer.d .step-plus` to `.offers:has(> .offer:nth-child(4)) .step-plus`,
which hides the control on every card at four offers rather than on the fourth card alone.

### Card count is inferred from the encoded `rate<i>` keys

With `#offerCount` gone, `restore()` needs the count before per-card ids exist. Derive it from the
highest `rate<i>` key in the parsed params, plus one:

- Old links carry `rate0..rateN` contiguously, so they infer correctly. Their `offerCount` key falls
  through the existing unknown-key path, which drops it silently and is already specified.
- A hand-crafted hash with gaps (`rate3` only) renders four cards, and `rate3` lands on the card it
  names. Counting keys instead of taking the maximum would render one card and drop the value.
- A hash carrying no `rate<i>` key at all names no offer, so it leaves the rendered cards alone:
  the inferred count floors at the number of cards already on the page. Every link the tool
  produces carries `rate0`, so this case is only ever a hand-typed or corrupted hash, and the
  guarantee that an unrecognized key changes nothing extends to the card count. At boot the markup
  holds one card, so the floor is 1 and the boot path is unaffected.
- `renderOffers()`'s existing clamp handles anything above 4. No new validation.

Boot default of 2 offers needs no new code: `DEFAULT_STATE = "rate1=5.75&fees1=11000"` already goes
through `restore()`, and it carries `rate1`, which infers 2. The count default now lives in one place
instead of being split between the markup's `selected` attribute and `DEFAULT_STATE`.

### Specs are corrected to a default of 2 offers

`offer-set` and `share-link` both describe a boot default of 1 offer. Shipped behavior is 2 and is
correct. Both drifted scenarios sit inside requirements this change already modifies, so the deltas
restate them. No behavior change, no separate drift-fix change.

## Risks / Trade-offs

- Accidental collapse — a reader clicking the heading to select "Offer A" collapses the card →
  The heading holds only the dot, the name, and the steppers; steppers are cancelled; a stray
  collapse costs one click to undo and loses no input value.
- Text selection in the heading gets awkward under `cursor:pointer` → Accepted. Nobody selects an
  offer label.
- Crafted hash with sparse `rate<i>` keys renders more cards than the link filled → Those cards hold
  markup defaults and compute normally. Same as any partially specified link today.
- Loss of the dropdown hint "1 analyzes a single offer; 2 or more compares them" → Accepted; the
  header subtitle covers the range, and the verdict's appearance at 2 teaches the rest.
- Self-check teardown currently resets through `#offerCount` → Replaced by
  `offers.innerHTML = card0HTML; restore(DEFAULT_STATE);`, which restores the true post-boot state
  rather than the single card it leaves behind today.
