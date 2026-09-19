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
The displayed offer cards SHALL remain side by side in a single row on non-mobile viewports and SHALL each occupy an equal share of the widened container, for any offer count from 1 to 4.

#### Scenario: Offers widen with the window
- **WHEN** the window is widened on a desktop viewport
- **THEN** all displayed offer cards remain in a single row of equal-width columns
- **AND** each card grows proportionally with the container

#### Scenario: Single offer at wide viewport
- **WHEN** the offer count is 1 on a desktop viewport
- **THEN** the one offer card spans the full container width, matching the shared-input card above it

#### Scenario: Column count follows offer count
- **WHEN** the offer count is changed between 1, 2, 3, and 4 on a desktop viewport
- **THEN** the offers grid renders exactly that many equal columns
- **AND** no empty column placeholder is left behind

#### Scenario: Result rows stay legible when widened
- **WHEN** an offer card is wider than its content requires
- **THEN** each readout row keeps its label left-aligned and its value right-aligned on the same line
- **AND** values do not wrap mid-number

### Requirement: Mobile stacking is preserved
At viewport widths of 640px and below, the existing single-column layout SHALL continue to apply unchanged, for any offer count.

#### Scenario: Phone-width viewport
- **WHEN** the tool is viewed at 390px wide
- **THEN** the shared-input grid renders as one column
- **AND** the offers grid renders as one column with the offer cards stacked in order, Offer A first
- **AND** input font size remains 16px so mobile browsers do not auto-zoom on focus

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

Each card's readout SHALL sit inside a disclosure control. At 640px and below the readout SHALL
start collapsed. Above 640px it SHALL start expanded, so cards stay directly comparable across
columns on desktop.

The summary SHALL always show two figures for that offer: payment including PMI for the first
period, and the headline total — cost to walk away with a holding period set, total cost to term
without.

Expanding or collapsing SHALL change no figure. The reader's open or closed choice SHALL survive
the re-render that follows any input edit.

#### Scenario: Phone-width load

- **WHEN** the tool is opened at 390px wide
- **THEN** each offer card shows its inputs and a collapsed readout summary
- **AND** the summary shows that offer's payment including PMI and its headline total

#### Scenario: Desktop load

- **WHEN** the tool is opened at 1280px wide
- **THEN** each offer card's readout is expanded
- **AND** the rows line up across the offer columns as before

#### Scenario: Open state survives an edit

- **WHEN** the reader expands Offer B's readout at 390px wide
- **AND** then edits any input
- **THEN** Offer B's readout is still expanded after the readout re-renders

#### Scenario: Summary follows the holding period

- **WHEN** the holding-period field is cleared
- **THEN** each card's summary shows total cost to term in place of cost to walk away

#### Scenario: Folding changes no figure

- **WHEN** a readout is collapsed and expanded again
- **THEN** every row shows the same value it showed before
