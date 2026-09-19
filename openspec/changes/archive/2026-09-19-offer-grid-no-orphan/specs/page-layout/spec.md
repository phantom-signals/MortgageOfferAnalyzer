## MODIFIED Requirements

### Requirement: Offer cards share the available width equally
Offer cards in one row SHALL each occupy an equal share of the container width. Cards SHALL wrap
to further rows when the container is too narrow for each card to keep a 260px minimum width.
With 4 offers, the grid SHALL render 4 columns, 2 columns, or 1 column, and SHALL NOT render 3
columns. With 1 to 3 offers, the grid SHALL render as many columns as fit, up to the offer count.

Each card SHALL take its own content height. A card SHALL NOT stretch to match a taller card in
the same row.

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

#### Scenario: Open cards still line up
- **WHEN** every card in a row is expanded
- **THEN** readout rows line up across the cards in that row

#### Scenario: Result rows stay legible when widened
- **WHEN** an offer card is wider than its content requires
- **THEN** each readout row keeps its label left-aligned and its value right-aligned on the same line
- **AND** values do not wrap mid-number
