## Context

Offer card heading is a `<summary>` holding `h2::before` (chevron), `span.dot`, `span.name`, and the
stepper buttons, all in `MortgageOfferAnalyzer.html`.

Every glyph in that row is `var(--accent)`:

```
┌─ 3px accent top border ──────────────────┐
│  ▸  ●  OFFER A            [−] [+]        │   chevron, dot, title, steppers: all accent
│  $1,234.56 / mo                          │
└──────────────────────────────────────────┘
```

Chevron is 6px with a 1.5px border; dot is 9px solid, 8px away. Two accent marks of near-equal
weight sitting adjacent read as one ornament, so neither states "this row toggles".

`.fold summary` has `cursor:pointer` and a `:focus-visible` outline, no `:hover`. Pointer users get
no resting-state feedback at all.

Single-file tool, no build step, no framework. Every change here is CSS plus deleting one span.

## Goals / Non-Goals

**Goals:**

- Fold affordance readable at a glance, on desktop where cards load expanded.
- One mark, not two, at the left of the heading row.
- Pointer feedback that the row is a control.
- Chevron color decision made by looking at it, not by argument.

**Non-Goals:**

- Adding a text label ("Show details") or a bordered button around the chevron. Chevron plus hover
  carries it; a label adds weight to a row already holding two steppers.
- Animating the fold open or closed. The chevron's rotation transition already exists.
- Touching the chart's circle markers. Separate mark, separate purpose.
- Changing accent hues, the fold's breakpoint default, or anything in the summary figure.

## Decisions

### Delete the dot rather than the chevron

Accent identity survives on four carriers without it: 3px top border, heading text, stepper glyphs,
focused-input outline. Chevron is the only mark that encodes state, so it is the one that stays.

Alternative considered: keep the dot, drop the chevron, rotate the dot into a triangle on open. Costs
more CSS and leaves the collapsed state ambiguous, since a dot at rest states nothing about folding.

Alternative considered: keep both, separate them with the offer name between. Splits the row into
three zones on a card that already holds steppers at the right. Rejected on clutter.

The dot's only argument was legend consistency with the chart. Weak: the cost table's key is a 10px
rounded square (`.sw`), chart markers are circles carrying letters, and the heading already
spells the offer name in words. Card heading matched neither key.

### Chevron in `--slate`

Resting chevron moves from `var(--accent)` to `var(--slate)`. Rationale: accent means "which offer
this is"; the chevron means "what this row does". Painting a control in identity color is what let it
blend into the dot in the first place.

Contrast supports it. Light: `--slate` `#5d6670` on `--card` `#ffffff` is 5.83:1, against `--a`
`#0081a2` at 4.50:1. Dark: `--slate` `#a3acb5` on `#1e2226` is 6.96:1, against `--a` `#33a1bf` at
5.33:1. Slate is the higher-contrast choice in both schemes, not a compromise for taste. Both clear
the 3:1 floor for a non-text graphical object either way, so this is headroom, not a fix.

Counter-argument worth a look: the four accent chevrons give a row of cards a color rhythm that four
gray ones lose, and the comment this change replaces said accent there was deliberate. So both were
built and screenshotted in both schemes before locking. Slate won. Accent turned out viable once the
dot was gone — a chevron reads as directional where the dot read as decoration — but slate keeps the
chevron's hover tell and carries more contrast. Reverting is still one declaration; nothing else in
the change reads the chevron's color.

### Hover tell follows from the chevron color

Heading text already rests at accent, so the chevron is the only thing in the row that can move:
slate at rest, accent under a hovering pointer. Reads as the row previewing its own identity color.

```
rest    ▸(slate)  OFFER A(accent)
hover   ▸(accent) OFFER A(accent)
```

That tell only exists while the chevron rests at slate — resting it at accent would have left hover
with nowhere to go and cost a separate signal, which is one more reason slate won.

On its own the chevron turned out too fine to notice moving. The card-border decision below is what
actually carries the hover; the chevron only confirms it.

Gate the whole hover block in `@media (hover:hover)` so a tap on a phone leaves no stuck color.

### Card border carries the hover, the chevron only confirms it

An 8px chevron with a 2px stroke is a small target to notice moving. Hover also draws the whole
card's border in the accent, which is a surface large enough to catch peripheral vision.

Trigger is the heading row, not the card. `.offer:has(> .fold > summary:hover)` keeps the child
combinators tight so only a card's own heading lights its own border. Hovering a rate input must not
light the border, because clicking an input does not fold anything, and a border that responds to
the whole card would promise a control the card does not have.

Alternative considered: `.offer:hover`. One selector shorter, wrong signal.

The card already sets `border:1px solid var(--line)` with `border-top:3px solid var(--accent)`, so a
single `border-color` declaration lights all four sides. That alone leaves the sides at 1px, too thin
to read as a change, so hover also lays an `inset 0 0 0 1px` ring inside the border box, doubling the
sides to 2px.

Weight was picked by rendering 1px, 2px and 3px rings and looking. 2px sides match the 3px top bar
exactly and make the hovered card one unbroken outline, which turned out to be too much: the card
reads as selected rather than passed over. 1px stays visibly under the top bar, so the top bar keeps
its job as the identity mark and hover stays a transient state.

The ring is a shadow, not a wider border: widening the border would reflow the card's contents and
nudge its neighbours on every hover. Inset shadows paint inside the border box and cost no layout.
The resting rule carries a second, zero-width transparent shadow so both states hold the same shadow
count and the ring can animate rather than snap. `transition` covers border-color and box-shadow at
the .15s the steppers already use.

Alternative considered: `outline` with a negative offset. Equivalent result, but the file already
uses `outline` for the summary's focus ring, and reusing it for hover would blur which state a ring
means.

### Chevron 6px to 8px

Border-width 1.5px to 2px with it, keeping the stroke proportional. It carries the affordance alone
now, and 6px next to 24px stepper buttons reads as a stray tick. 8px stays smaller than the 9px dot
it replaces, so the row's metrics barely move.

## Risks / Trade-offs

- Slate chevron reads dull across four cards, flattening the color rhythm. Checked by building both
  and comparing in each scheme; slate held up. Revert is one declaration.
- Removing the dot weakens identity at a glance on a narrow phone, where cards stack and the accent
  top border is the main tell. Checked at 390px with 4 offers: the top border is 3px and full card
  width, a bigger accent surface than a 9px dot.
- Hover-only feedback would strand touch and keyboard readers. Mitigation: hover is additive; chevron
  and the existing `:focus-visible` outline stay the real affordances, and a scenario pins that.
- The clone path rewrites `">Offer A<"` per card. Deleting a sibling span does not touch that
  substring, and no JavaScript queries `.dot`. Low risk, verified by grep before editing.

## Migration Plan

None. Presentation only. No stored state, no share-link parameter, no computed figure changes.
Rollback is `git revert`.

## Open Questions

None. Chevron color is settled: `--slate`. Both variants were built and screenshotted at four
offers, light and dark at 1280px and light at 390px. Accent turned out viable once the dot was gone,
since a chevron reads as directional where the dot read as decoration — but slate keeps the hover
tell, which accent would have had to buy back with a row tint, and it carries more contrast in both
schemes.
