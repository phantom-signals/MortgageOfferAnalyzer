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
place of the figure. The figure SHALL show only while collapsed, where it is the only figure the
card shows, and SHALL be hidden while expanded, where the readout below repeats the same number.
The heading itself — chevron, offer name, steppers — SHALL NOT change size, weight, or color between the collapsed and expanded states.
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
- **AND** the summary figure shows while collapsed and is hidden while expanded

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

## ADDED Requirements

### Requirement: Prose wraps at the full content width
Header subtitle text and footer paragraph text SHALL wrap at the full content-container width. No fixed character-count measure limit SHALL constrain them.

#### Scenario: Subtitle at wide viewport
- **WHEN** the window is wider than the previous 920px container and the header subtitle is rendered
- **THEN** the subtitle text wraps at the container edge, not at approximately one offer-card width

#### Scenario: Footer paragraphs at wide viewport
- **WHEN** the window is wider than the previous 920px container and the footer paragraphs, including those inside an expanded footer section, are rendered
- **THEN** each footer paragraph wraps at the container edge, not at approximately one offer-card width

### Requirement: Verdict bar uses card colors in both schemes

The verdict bar SHALL use the card background and ink text color in both the light and dark color
schemes, so the offer letters it prints sit on the background each scheme's accents were chosen for.
Its border SHALL be the stronger of the page's two border tones in both schemes. No color token SHALL
exist solely to give the verdict bar a scheme-specific look. The chart tooltip and definition popover
SHALL keep their current dark background and light text in both schemes.

#### Scenario: Light scheme verdict

- **WHEN** the tool is opened with two offers in the light color scheme
- **THEN** the verdict bar background matches the offer card background
- **AND** its border is the stronger border tone, not the lighter one the cards use
- **AND** the verdict text uses the ink color
- **AND** the winning offer letter renders in that offer's light-scheme accent color

#### Scenario: Dark scheme verdict matches cards

- **WHEN** the tool is opened with two offers in the dark color scheme
- **THEN** the verdict bar background matches the dark-scheme offer card background
- **AND** its border is the dark-scheme stronger border tone
- **AND** the verdict text uses the dark-scheme ink color
- **AND** the winning offer letter renders in that offer's dark-scheme accent color

#### Scenario: Overlays unchanged

- **WHEN** the reader hovers the cost chart or opens a term definition in either color scheme
- **THEN** the tooltip and popover keep their dark background and light text

### Requirement: Verdict sits between the offers and the charts

The verdict block SHALL render below the offers grid and above the cost bars, so the reader sees
the offers before the conclusion drawn from them. Its "Verdict" title SHALL render outside and above
the verdict card, styled as a section label like the cost-bar and cost-over-time titles. Title and
card SHALL hide together at an offer count of 1. Content and ranking logic SHALL be unchanged.

#### Scenario: Order on a phone

- **WHEN** the tool is viewed at 390px wide with two or more offers
- **THEN** the blocks read in order: shared-input card, offer cards, verdict title, verdict card, cost bars, cost-over-time chart

#### Scenario: Title outside the card

- **WHEN** two offers are entered
- **THEN** the text "Verdict" renders as a section label above the verdict card's border
- **AND** the verdict card contains only the headline, holding-period note, and amount

#### Scenario: Single offer

- **WHEN** the offer count is 1
- **THEN** neither the verdict title nor the verdict card is displayed
- **AND** the offer card is followed directly by the cost-bar section

#### Scenario: Verdict content unchanged

- **WHEN** two offers are entered and a holding period is set
- **THEN** the verdict names the same winning offer and amount it named before the move

### Requirement: Footer sections fold closed by default

Below the footer's license line, the page SHALL render two disclosure sections, in order: "Glossary",
then "Privacy and Terms of Use". Each SHALL be a native `<details>` element, closed on load, whose
summary is styled as a section label and carries a chevron drawn like the offer-card chevron:
pointing one way closed, the other open, in the secondary text tone. Opening one section SHALL NOT
open or close the other.

The footer's "Terms of Use" link SHALL open the "Privacy and Terms of Use" section and scroll it into
view. Following the link SHALL NOT change `location.hash`, since the hash carries share state.

#### Scenario: Closed on load

- **WHEN** the page loads, by any means, including from a share link
- **THEN** the "Glossary" and "Privacy and Terms of Use" sections are collapsed
- **AND** only their summary labels and chevrons are visible

#### Scenario: Toggle a section

- **WHEN** the reader activates a section summary by click, tap, or keyboard
- **THEN** that section expands and its chevron rotates
- **AND** activating it again collapses it

#### Scenario: Terms link opens the fold

- **WHEN** the "Privacy and Terms of Use" section is closed and the reader activates the footer "Terms of Use" link
- **THEN** the section opens and scrolls into view
- **AND** `location.hash` is the same as before the click

#### Scenario: Works without JavaScript

- **WHEN** the file is viewed with JavaScript disabled
- **THEN** each section still expands and collapses from its summary

### Requirement: Label hints sit in parentheses

Visible text SHALL NOT use an em dash as a separator between a label and its hint, or within a
sentence. An input-label or section-label hint SHALL follow the label text after one space,
enclosed in parentheses, with no colon or dash before it. A label whose text already ends in a
parenthesized unit, such as "PMI annual rate (%)", SHALL carry no hint. Sentences, such as the
share-link hint, the `noscript` notice, and glossary definitions, SHALL use colons, commas, or
parentheses where an em dash stood. A lone em dash that stands for an empty value, such as a
blank readout or verdict, SHALL remain.

#### Scenario: Input label hint

- **WHEN** the shared-input card renders
- **THEN** the home value label reads "Home value at purchase (lower of sale price or appraisal)"

#### Scenario: Section-label hint

- **WHEN** the cost-over-time section renders
- **THEN** its label reads "Cost over time (what walking away at any point costs, including payoff of the balance still owed)"

#### Scenario: Unit label carries no hint

- **WHEN** an offer card renders
- **THEN** the PMI rate label reads "PMI annual rate (%)" with no hint and no colon

#### Scenario: Empty placeholder kept

- **WHEN** fewer than two offers compute
- **THEN** the verdict headline and amount each show a lone em dash

## REMOVED Requirements

### Requirement: Prose spans the full content width
**Reason**: Footer method and PMI paragraphs removed; scenario named them. Replaced by "Prose wraps at the full content width".
**Migration**: None. Same wrapping rule.

### Requirement: Verdict bar colors follow color scheme
**Reason**: Dark scheme no longer keeps a dark verdict bar. Replaced by "Verdict bar uses card colors in both schemes".
**Migration**: None.

### Requirement: Verdict sits above the offers
**Reason**: Verdict moved below the offers grid, above the charts; covered by "Verdict sits between the offers and the charts".
**Migration**: None. Verdict content, ranking, and hidden state unchanged.
