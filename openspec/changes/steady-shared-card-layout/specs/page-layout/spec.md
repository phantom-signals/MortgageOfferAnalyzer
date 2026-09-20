## ADDED Requirements

### Requirement: Shared inputs group PMI parameters in one column

On viewports wider than 640px the shared-input card SHALL render two columns of stacked fields. The left column SHALL hold loan amount then holding period. The right column SHALL hold home value, PMI removal rule, then PMI premium basis, in that order, so every input that drives PMI sits in one column. No PMI input SHALL share a row with another shared input.

Columns SHALL each keep their own height. A shorter column SHALL NOT stretch its fields to match the taller column.

#### Scenario: Desktop shared card

- **WHEN** the tool is opened at 1280px wide
- **THEN** loan amount and holding period render in the left column, loan amount above holding period
- **AND** home value, PMI removal rule, and PMI premium basis render in the right column, in that order
- **AND** PMI removal rule and PMI premium basis are horizontally aligned with each other

#### Scenario: Narrow desktop window

- **WHEN** the window is resized to 720px wide
- **THEN** the two shared-input columns persist
- **AND** PMI removal rule and PMI premium basis stay in the same column

#### Scenario: Field spacing is even

- **WHEN** the shared card is rendered in two columns
- **THEN** the vertical gap between two fields in a column equals the grid row gap used between shared-card rows before this change

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
- **AND** input text renders larger than the 13px readout rows and no larger than any heading

## MODIFIED Requirements

### Requirement: Mobile stacking is preserved
At viewport widths of 640px and below, the existing single-column layout SHALL continue to apply unchanged, for any offer count. The shared-input card SHALL stack its fields in document order: loan amount, holding period, home value, PMI removal rule, PMI premium basis. Column grouping SHALL NOT change that order.

#### Scenario: Phone-width viewport
- **WHEN** the tool is viewed at 390px wide
- **THEN** the shared-input grid renders as one column
- **AND** the shared inputs appear in order: loan amount, holding period, home value, PMI removal rule, PMI premium basis
- **AND** the offers grid renders as one column with the offer cards stacked in order, Offer A first
- **AND** on a touch device the input font size is 16px so mobile browsers do not auto-zoom on focus
