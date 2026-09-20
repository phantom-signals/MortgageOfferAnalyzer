# page-layout Specification

## Purpose
How the mortgage tool distributes horizontal space: container width, prose line length, offer-card arrangement across the available width, and responsive stacking on small viewports.
## Requirements
### Requirement: Content container fills the viewport
The tool's outer content container SHALL span the full width of the browser window, inset only by the page's responsive body padding. It SHALL NOT impose a fixed maximum width.

#### Scenario: Wide desktop window
- **WHEN** the tool is opened in a browser window 2560px wide
- **THEN** the shared-input card, the offers grid, and the verdict bar each span the window width minus the body padding on each side
- **AND** no horizontal scrollbar appears

#### Scenario: Narrow desktop window
- **WHEN** the browser window is resized to 900px wide
- **THEN** the content container shrinks to fit the window rather than overflowing
- **AND** no horizontal scrollbar appears

### Requirement: Prose spans the full content width
Header subtitle text and footer paragraph text SHALL wrap at the full content-container width. No fixed character-count measure limit SHALL constrain them.

#### Scenario: Subtitle at wide viewport
- **WHEN** the window is wider than the previous 920px container and the header subtitle is rendered
- **THEN** the subtitle text wraps at the container edge, not at approximately one offer-card width

#### Scenario: Footer method and PMI notes at wide viewport
- **WHEN** the window is wider than the previous 920px container and the footer paragraphs are rendered
- **THEN** each footer paragraph wraps at the container edge, not at approximately one offer-card width
- **AND** the total vertical height of the footer is reduced relative to the clamped layout

### Requirement: Offer cards share the available width equally
Offer cards in one row SHALL each occupy an equal share of the container width. Cards SHALL wrap
to further rows when the container is too narrow for each card to keep a 260px minimum width.
With 4 offers, the grid SHALL render 4 columns, 2 columns, or 1 column, and SHALL NOT render 3
columns. With 1 to 3 offers, the grid SHALL render as many columns as fit, up to the offer count.

Each card SHALL take its own content height. A card SHALL NOT stretch to match a taller card in
the same row. When cards span more than one row, each card below the first row SHALL sit one grid
gap below the card above it in the same column, regardless of the height of other cards in that
row. Cards SHALL keep their column; only their vertical position changes.

#### Scenario: Offers widen with the window
- **WHEN** the window is widened on a desktop viewport
- **THEN** cards in each row stay equal width
- **AND** each card grows proportionally with the container

#### Scenario: Single offer at wide viewport
- **WHEN** the offer count is 1 on a desktop viewport
- **THEN** the one offer card spans the full container width, matching the shared-input card above it

#### Scenario: Four offers never leave one card alone
- **WHEN** the offer count is 4 and the offers grid is at least 1094px wide
- **THEN** the four cards render in a single row of 4 equal columns
- **WHEN** the offer count is 4 and the offers grid is narrower than 1094px but wide enough for two 260px columns
- **THEN** the cards render as 2 rows of 2, Offer A and Offer B on the first row
- **AND** no row holds a single card beside empty space

#### Scenario: Three offers at mid width
- **WHEN** the offer count is 3 and the offers grid fits two 260px columns but not three
- **THEN** Offer A and Offer B share the first row and Offer C sits alone on the second row

#### Scenario: No empty column placeholder
- **WHEN** the offer count is changed between 1, 2, 3, and 4 on a desktop viewport
- **THEN** no row reserves an empty column for a card that does not exist

#### Scenario: Folded card beside open card
- **WHEN** two cards share a row and one is folded while the other is expanded
- **THEN** the folded card is only as tall as its heading and summary
- **AND** the expanded card keeps its full height

#### Scenario: Card slides up under a folded card
- **WHEN** the offer count is 4 in a 2-column layout and Offer A is folded while Offer B is expanded
- **THEN** Offer C sits one grid gap below Offer A, in the left column
- **AND** Offer D sits one grid gap below Offer B, in the right column
- **AND** content below the offers grid starts below the taller column and overlaps neither

#### Scenario: Unfolding restores position
- **WHEN** Offer A is expanded again
- **THEN** Offer C moves down to sit one grid gap below Offer A
- **AND** no card changes column

#### Scenario: Open cards still line up
- **WHEN** every card in a row, and every card above them, is expanded
- **THEN** readout rows line up across the cards in that row

#### Scenario: Result rows stay legible when widened
- **WHEN** an offer card is wider than its content requires
- **THEN** each readout row keeps its label left-aligned and its value right-aligned on the same line
- **AND** values do not wrap mid-number

### Requirement: Shared inputs group PMI parameters in one column

On viewports wider than 640px the shared-input card SHALL render two columns of stacked fields. The left column SHALL hold home value, loan amount, then holding period, in that order. The right column SHALL hold PMI removal rule, PMI premium basis, then the initial LTV readout, in that order, so every control that sets a PMI rule sits in one column beside the ratio those rules are measured against. No PMI control SHALL share a row with another shared input.

Each column SHALL hold three items, so neither column ends in a field-sized run of empty card space.

The two columns are grid tracks of the same height. A shorter column SHALL NOT stretch its fields to fill that height; it SHALL leave the difference as empty space below its last field rather than distributing it between them.

#### Scenario: Desktop shared card

- **WHEN** the tool is opened at 1280px wide
- **THEN** home value, loan amount, and holding period render in the left column, in that order
- **AND** PMI removal rule, PMI premium basis, and the initial LTV readout render in the right column, in that order
- **AND** PMI removal rule and PMI premium basis are horizontally aligned with each other

#### Scenario: Neither column ends in a hole

- **WHEN** the shared card is rendered in two columns
- **THEN** both columns hold three items
- **AND** no column ends with a field-sized run of empty card space above the card's bottom padding

#### Scenario: Narrow desktop window

- **WHEN** the window is resized to 720px wide
- **THEN** the two shared-input columns persist
- **AND** PMI removal rule and PMI premium basis stay in the same column

#### Scenario: Field spacing is even

- **WHEN** the shared card is rendered in two columns
- **THEN** the vertical gap between two items in a column equals the grid row gap used between shared-card rows before this change
- **AND** the readout sits at that same gap below the PMI premium basis field

### Requirement: Input size is independent of viewport width

Input font size and input padding SHALL depend on pointer type, never on viewport width. On a fine pointer (mouse or trackpad) every text, number, and select input SHALL render at 14px. On a coarse pointer (touch) it SHALL render at 16px, the size that stops mobile browsers auto-zooming on focus. Padding SHALL step with the font size under the same condition.

No width-based media query SHALL set input font size or input padding.

#### Scenario: Window dragged narrower

- **WHEN** the window is dragged from 1280px wide down through 640px to 400px on a mouse-driven desktop
- **THEN** the font size of every shared-card input, offer-card input, and the share button stays 14px throughout
- **AND** input padding stays unchanged throughout
- **AND** no input text or input box resizes at the 640px boundary

#### Scenario: Focus on a touch device

- **WHEN** an input is focused on a touch device
- **THEN** the input font size is 16px and the browser does not auto-zoom

#### Scenario: Input type sits within the page scale

- **WHEN** the shared card is rendered on a mouse-driven desktop
- **THEN** input text renders at 14px, matching the header subtitle and the fold summary
- **AND** input text renders no smaller than the readout rows — 13px above 640px, 14px at or below it — and no larger than any heading

### Requirement: Mobile stacking is preserved
At viewport widths of 640px and below, the existing single-column layout SHALL continue to apply unchanged, for any offer count. The shared-input card SHALL stack its items in document order: home value, loan amount, holding period, PMI removal rule, PMI premium basis, initial LTV readout. Column grouping SHALL NOT change that order.

#### Scenario: Phone-width viewport
- **WHEN** the tool is viewed at 390px wide
- **THEN** the shared-input grid renders as one column
- **AND** the shared items appear in order: home value, loan amount, holding period, PMI removal rule, PMI premium basis, initial LTV readout
- **AND** the offers grid renders as one column with the offer cards stacked in order, Offer A first
- **AND** on a touch device the input font size is 16px so mobile browsers do not auto-zoom on focus

### Requirement: Calculation behavior is unchanged
The layout change SHALL NOT alter any computed value, input, control, or script behavior.

#### Scenario: Identical results before and after
- **WHEN** the same inputs are entered before and after the layout change
- **THEN** the payment, effective annual rate, LTV, PMI, total cost, holding-period figures, and verdict are identical

#### Scenario: JavaScript-disabled viewer
- **WHEN** the file is opened in a context with JavaScript disabled, such as an email attachment preview
- **THEN** the `noscript` warning block still renders and remains readable within the full-window container

### Requirement: Verdict sits above the offers

The verdict block SHALL render above the offers grid, below the shared-input card, so the
conclusion is reached before any per-offer detail. It SHALL keep its content, ranking logic, and
hidden state at an offer count of 1.

#### Scenario: Verdict reached first on a phone

- **WHEN** the tool is viewed at 390px wide with two or more offers
- **THEN** the verdict is the first block below the shared-input card
- **AND** the offer cards, the cost bars, and the cost-over-time chart all follow it

#### Scenario: Single offer

- **WHEN** the offer count is 1
- **THEN** the verdict block is hidden, as before
- **AND** the shared-input card is followed directly by the offer card

#### Scenario: Verdict content unchanged

- **WHEN** two offers are entered and a holding period is set
- **THEN** the verdict names the same winning offer and amount it named before the move

### Requirement: Card readouts fold on small viewports

Each card's inputs and readout SHALL sit together inside one disclosure control. The card heading
(disclosure chevron, dot, offer name, add/remove steppers) SHALL be the disclosure control's summary,
so the whole heading row toggles the fold and stays visible and operable while the card is collapsed.
At 640px and below the disclosure SHALL start collapsed. Above 640px it SHALL start expanded, so
cards stay directly comparable across columns on desktop. This default SHALL be decided once, at
load, from the width then in effect, and cards added later SHALL inherit it; a later resize or
rotation SHALL NOT re-fold or re-open a card, since by then the fold state may be the reader's.

The heading SHALL show a chevron, left of the color dot, in that card's accent color, which points
one way while collapsed and the other while expanded. The chevron SHALL be visible in both states, so
the fold is discoverable on desktop where cards start expanded.

The summary SHALL show exactly one figure for that offer: payment including PMI for the first
period. When the offer's inputs are invalid, the summary SHALL show the invalid-input message in
place of the figure. The figure SHALL change type treatment between states: prominent while
collapsed, where it is the only figure the card shows, and reduced to a quiet secondary line while
expanded, where the readout below repeats the same number. The heading itself — chevron, dot, offer
name, steppers — SHALL NOT change size, weight, or color between states.

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
- **AND** each heading shows its accent-colored chevron in the expanded orientation
- **AND** the rows line up across the offer columns as before

#### Scenario: Heading row toggles the fold

- **WHEN** the reader activates an expanded card's heading, by pointer or by keyboard
- **THEN** that card collapses to its heading and summary figure
- **AND** activating the heading again expands it

#### Scenario: Heading keeps its type in both states

- **WHEN** a card is expanded and then collapsed
- **THEN** the offer name renders at the same size, weight, and color in both states
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

### Requirement: Verdict bar colors follow color scheme

In the light color scheme the verdict bar SHALL use the card background and ink text color, so the
offer letters it prints sit on the background their light-scheme accents were chosen for. Its border
SHALL be the stronger of the page's two border tones, so the bar still reads as a banner rather than
as one more card. In the dark color scheme the verdict bar SHALL keep its current dark background
and light text. The chart tooltip and definition popover SHALL keep their current colors in both
schemes.

#### Scenario: Light scheme verdict

- **WHEN** the tool is opened with two offers in the light color scheme
- **THEN** the verdict bar background matches the offer card background
- **AND** its border is the stronger border tone, not the lighter one the cards use
- **AND** the verdict text uses the ink color
- **AND** the winning offer letter renders in that offer's light-scheme accent color

#### Scenario: Dark scheme verdict unchanged

- **WHEN** the tool is opened with two offers in the dark color scheme
- **THEN** the verdict bar background, text color, and letter colors are identical to before this change

#### Scenario: Overlays unchanged

- **WHEN** the reader hovers the cost chart or opens a term definition in the light color scheme
- **THEN** the tooltip and popover keep their dark background and light text

