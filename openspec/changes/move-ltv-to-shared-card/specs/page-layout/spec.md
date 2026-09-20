## MODIFIED Requirements

### Requirement: Shared inputs group PMI parameters in one column

On viewports wider than 640px the shared-input card SHALL render two columns of stacked fields. The left column SHALL hold home value, loan amount, then holding period, in that order. The right column SHALL hold PMI removal rule, PMI premium basis, then the initial LTV readout, in that order, so every control that sets a PMI rule sits in one column beside the ratio those rules are measured against. No PMI control SHALL share a row with another shared input.

Each column SHALL hold three items, so neither column ends in empty card space.

Columns SHALL each keep their own height. A shorter column SHALL NOT stretch its fields to match the taller column.

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

### Requirement: Mobile stacking is preserved
At viewport widths of 640px and below, the existing single-column layout SHALL continue to apply unchanged, for any offer count. The shared-input card SHALL stack its items in document order: home value, loan amount, holding period, PMI removal rule, PMI premium basis, initial LTV readout. Column grouping SHALL NOT change that order.

#### Scenario: Phone-width viewport
- **WHEN** the tool is viewed at 390px wide
- **THEN** the shared-input grid renders as one column
- **AND** the shared items appear in order: home value, loan amount, holding period, PMI removal rule, PMI premium basis, initial LTV readout
- **AND** the offers grid renders as one column with the offer cards stacked in order, Offer A first
- **AND** on a touch device the input font size is 16px so mobile browsers do not auto-zoom on focus
