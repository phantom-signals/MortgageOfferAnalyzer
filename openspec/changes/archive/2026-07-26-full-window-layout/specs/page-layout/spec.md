## ADDED Requirements

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
The two offer cards SHALL remain side by side on non-mobile viewports and SHALL each occupy an equal share of the widened container.

#### Scenario: Offers widen with the window
- **WHEN** the window is widened on a desktop viewport
- **THEN** Offer A and Offer B remain in a single row of two equal-width columns
- **AND** each card grows proportionally with the container

#### Scenario: Result rows stay legible when widened
- **WHEN** an offer card is wider than its content requires
- **THEN** each readout row keeps its label left-aligned and its value right-aligned on the same line
- **AND** values do not wrap mid-number

### Requirement: Mobile stacking is preserved
At viewport widths of 640px and below, the existing single-column layout SHALL continue to apply unchanged.

#### Scenario: Phone-width viewport
- **WHEN** the tool is viewed at 390px wide
- **THEN** the shared-input grid renders as one column
- **AND** the offers grid renders as one column with Offer A above Offer B
- **AND** input font size remains 16px so mobile browsers do not auto-zoom on focus

### Requirement: Calculation behavior is unchanged
The layout change SHALL NOT alter any computed value, input, control, or script behavior.

#### Scenario: Identical results before and after
- **WHEN** the same inputs are entered before and after the layout change
- **THEN** the payment, effective annual rate, LTV, PMI, total cost, holding-period figures, and verdict are identical

#### Scenario: JavaScript-disabled viewer
- **WHEN** the file is opened in a context with JavaScript disabled, such as an email attachment preview
- **THEN** the `noscript` warning block still renders and remains readable within the full-window container
