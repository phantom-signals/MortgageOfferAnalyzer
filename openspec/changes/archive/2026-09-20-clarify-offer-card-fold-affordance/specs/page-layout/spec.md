## MODIFIED Requirements

### Requirement: Card readouts fold on small viewports

Each card's inputs and readout SHALL sit together inside one disclosure control. The card heading
(disclosure chevron, offer name, add/remove steppers) SHALL be the disclosure control's summary,
so the whole heading row toggles the fold and stays visible and operable while the card is collapsed.
At 640px and below the disclosure SHALL start collapsed. Above 640px it SHALL start expanded, so
cards stay directly comparable across columns on desktop. This default SHALL be decided once, at
load, from the width then in effect, and cards added later SHALL inherit it; a later resize or
rotation SHALL NOT re-fold or re-open a card, since by then the fold state may be the reader's.

The heading SHALL show a chevron, leftmost in the row, which points one way while collapsed and the
other while expanded. The chevron SHALL be visible in both states, so the fold is discoverable on
desktop where cards start expanded. No color dot SHALL sit beside it; the chevron is the only mark
left of the offer name, so nothing competes with it for the reader's read of what the row does.

The chevron SHALL be drawn in the page's secondary text tone rather than the card's accent color, so
control chrome reads as distinct from offer identity, and SHALL be large enough to carry the fold
affordance on its own. It SHALL meet the same contrast against the card background in both light and
dark color schemes.

Under a pointer that supports hover, hovering the heading row SHALL shift the chevron to the card's
accent color and SHALL draw that card's full border in the same accent color, confirming the row is a
control. The chevron's stroke is too fine to carry the signal alone, so the card border is what makes
the hover visible at a glance. The hovered border SHALL be heavier than its resting weight and SHALL
stay lighter than the card's accent top border, so the top border remains the card's identity mark
and the hover reads as a passing state. Lighting it SHALL NOT shift the card's contents or its
neighbours' positions. The offer name already rests in that accent color and SHALL NOT change
on hover.

Only the heading row SHALL trigger this. Hovering a card's inputs or readout SHALL NOT light the
border, since those do not toggle the fold and SHALL NOT suggest they do. This hover styling SHALL
apply only on devices whose primary pointer can hover, so a touch tap leaves no stuck hover state.
Hover SHALL be additive: the chevron alone, without hover, remains the affordance for touch and
keyboard readers.

The summary SHALL show exactly one figure for that offer: payment including PMI for the first
period. When the offer's inputs are invalid, the summary SHALL show the invalid-input message in
place of the figure. The figure SHALL change type treatment between states: prominent while
collapsed, where it is the only figure the card shows, and reduced to a quiet secondary line while
expanded, where the readout below repeats the same number. The heading itself — chevron, offer
name, steppers — SHALL NOT change size, weight, or color between the collapsed and expanded states.
The hover shift above is keyed to pointer state, not fold state, and SHALL be identical in both.

Pressing an add or remove stepper SHALL NOT toggle the fold, by pointer or by keyboard.

Expanding or collapsing SHALL change no figure and no input value. The reader's open or closed
choice SHALL survive the re-render that follows any input edit.

#### Scenario: Phone-width load

- **WHEN** the tool is opened at 390px wide
- **THEN** each offer card shows its heading and a collapsed summary
- **AND** no rate, term, payments-per-year, fees, or PMI input is visible
- **AND** the summary shows that offer's payment including PMI and no other figure

#### Scenario: Desktop load

- **WHEN** the tool is opened at 1280px wide
- **THEN** each offer card's inputs and readout are expanded
- **AND** each heading shows its chevron in the expanded orientation, drawn in the secondary text tone
- **AND** the rows line up across the offer columns as before

#### Scenario: No color dot in the heading

- **WHEN** any offer card is rendered, collapsed or expanded, at any viewport width
- **THEN** the heading row contains a chevron, the offer name, and the add and remove steppers, in that order
- **AND** no color dot appears between the chevron and the offer name

#### Scenario: Heading responds to hover

- **WHEN** the reader hovers an offer card's heading row with a pointer that supports hover
- **THEN** that card's chevron shifts from the secondary text tone to the card's accent color
- **AND** that card's full border is drawn in the same accent color, heavier than its resting weight
- **AND** no input, readout row, or neighbouring card moves by any amount
- **AND** the offer name stays in the accent color it already rests in
- **AND** no other card's border changes
- **AND** moving the pointer off the row returns the chevron and the border to their resting colors
- **AND** no fold state changes

#### Scenario: Hovering a card's body does not signal the fold

- **WHEN** the reader hovers a card's rate input or its readout, away from the heading row
- **THEN** that card's border stays in its resting color
- **AND** that card's chevron stays in the secondary text tone

#### Scenario: Hover styling is pointer-gated

- **WHEN** the tool is used on a touch device whose primary pointer cannot hover
- **THEN** tapping an offer card's heading leaves no persistent hover coloring on that heading
- **AND** the chevron alone still shows which way the card folds

#### Scenario: Heading row toggles the fold

- **WHEN** the reader activates an expanded card's heading, by pointer or by keyboard
- **THEN** that card collapses to its heading and summary figure
- **AND** activating the heading again expands it

#### Scenario: Heading keeps its type in both states

- **WHEN** a card is expanded and then collapsed, with no pointer over the heading
- **THEN** the offer name renders at the same size, weight, and color in both states
- **AND** the chevron renders at the same size and color in both states, differing only in orientation
- **AND** only the summary figure changes its type treatment

#### Scenario: Resize does not re-decide the fold
- **WHEN** the tool is loaded at 1280px wide and the window is then dragged below 640px
- **THEN** the cards stay expanded
- **AND** a card added after the resize is expanded too, matching the others

#### Scenario: Open state survives an edit

- **WHEN** the reader expands Offer B at 390px wide
- **AND** then edits any input
- **THEN** Offer B's inputs and readout are still expanded after the readout re-renders

#### Scenario: Summary ignores the holding period

- **WHEN** the holding-period field is set or cleared
- **THEN** each card's summary shows only payment including PMI
- **AND** neither cost to walk away nor total cost to term appears in the summary

#### Scenario: Invalid inputs while collapsed

- **WHEN** a card's inputs are invalid and the card is collapsed
- **THEN** the summary shows the invalid-input message

#### Scenario: Steppers work while collapsed

- **WHEN** Offer A is collapsed and the reader presses its add-offer stepper
- **THEN** a new offer card is added
- **AND** Offer A stays collapsed

#### Scenario: Steppers do not toggle the fold

- **WHEN** the reader presses an expanded card's remove or add stepper
- **THEN** the count changes as specified
- **AND** no card's fold state changes

#### Scenario: Folding changes no figure

- **WHEN** a card is collapsed and expanded again
- **THEN** every input holds the value it held before
- **AND** every readout row shows the same value it showed before
