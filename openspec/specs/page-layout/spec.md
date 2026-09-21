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

### Requirement: Visible text avoids em dash separators

Visible text SHALL NOT use an em dash as a separator between a label and a parenthetical, or within
a sentence. Sentences, such as the share-link hint, the `noscript` notice, and glossary definitions,
SHALL use colons, commas, or parentheses where an em dash stood. A lone em dash that stands for an
empty value, such as a blank readout or verdict, SHALL remain.

#### Scenario: No em dash in a label

- **WHEN** any input label, readout row label, or section heading renders
- **THEN** it contains no em dash

#### Scenario: Empty placeholder kept

- **WHEN** fewer than two offers compute
- **THEN** the verdict headline and amount each show a lone em dash

### Requirement: Labels carry no hints

Input labels and section headings SHALL carry no explanatory hint text. An explanation a label needs
SHALL live in its glossary definition, which reaches the reader through hover text and the
definition popover. A label MAY end in a parenthesized unit, such as "PMI annual rate (%)" or
"Holding period (years)". Readout and table row labels MAY keep a parenthetical that qualifies the
figure, such as "(first period)" or "(incl. fees + PMI)".

#### Scenario: Home value label

- **WHEN** the shared-input card renders
- **THEN** the home value label reads "Home value at purchase"

#### Scenario: Holding period label

- **WHEN** the shared-input card renders
- **THEN** the holding period label reads "Holding period (years)"

#### Scenario: Section headings

- **WHEN** the cost comparison and cost-over-time sections render
- **THEN** their headings read "Cost to walk away" (or "Cost to term") and "Cost over time", with no parenthetical after either

#### Scenario: Unit label

- **WHEN** an offer card renders
- **THEN** the PMI rate label reads "PMI annual rate (%)" with no hint and no colon

### Requirement: Wrapped labels break before a parenthetical

Where an input label, readout row label, comparison table total label, or glossary term ends in a
parenthetical and does not fit on one line, the line SHALL break before the opening "(", so the
parenthetical starts a line. A parenthetical wider than its container SHALL wrap within itself
rather than overflow. Labels that fit on one line SHALL render unchanged. The label's text content
SHALL be unchanged, so definition lookup and hover text are unaffected.

#### Scenario: Readout row at phone width

- **WHEN** an offer readout renders in a 320px-wide viewport
- **THEN** the "Payment incl. PMI (first period)" label breaks as "Payment incl. PMI" then "(first period)"
- **AND** the "Total cost (incl. fees + PMI)" label wraps with its second line starting "("

#### Scenario: Table total at phone width

- **WHEN** the comparison table renders in a 320px-wide viewport with a holding period set
- **THEN** the "Cost to walk away (incl. fees + PMI)" label, if it wraps, breaks before "("

#### Scenario: Label fits

- **WHEN** a label with a parenthetical fits its container on one line
- **THEN** it renders on one line

#### Scenario: Definition lookup unchanged

- **WHEN** a row label's parenthetical is wrapped for line breaking
- **THEN** the label carries the same hover definition it carried before

### Requirement: Share disclosure text is left-aligned
The disclosure text accompanying the copy-link control SHALL render its lines left-aligned, not centered, at every viewport width. The copy-link control itself SHALL stay horizontally centered, and the disclosure text block SHALL stay horizontally centered under it with its existing measure limit; only the alignment of the lines inside that block changes. The text SHALL NOT be justified.

#### Scenario: Wrapped disclosure on a narrow viewport
- **WHEN** the viewport is narrow enough that the disclosure text under the copy-link control wraps to more than one line
- **THEN** every line of that text starts at the same left edge
- **AND** the line ends are ragged, with no stretched word spacing

#### Scenario: Control stays centered
- **WHEN** the copy-link control and its disclosure text are rendered at any viewport width
- **THEN** the control remains horizontally centered in the content container
- **AND** the disclosure text block remains horizontally centered under the control

