## MODIFIED Requirements

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
