## ADDED Requirements

### Requirement: Comparison table shows every offer side by side

The tool SHALL render one comparison table below the cost bars, inside the same chart container.
Each displayed offer that computes SHALL occupy one column, in offer order, headed by its letter in
that offer's accent color. Each cost component SHALL occupy one row, in the order bar segments are
drawn. A total row SHALL close the table.

Component rows SHALL be interest, PMI, upfront fees, remaining balance, principal. A component row
SHALL be omitted when its amount is zero for every displayed offer, so columns stay aligned.

#### Scenario: Two offers compared

- **WHEN** two offers are entered with valid terms
- **THEN** the table renders a column for Offer A and a column for Offer B
- **AND** each component row shows both offers' amounts on one line
- **AND** the total row shows each offer's total

#### Scenario: Component absent from every offer

- **WHEN** no displayed offer carries PMI, because every loan starts at or below 80% LTV
- **THEN** the PMI row is not rendered
- **AND** every remaining row still shows one value per offer column

#### Scenario: Offer count changes

- **WHEN** the offer count is changed between 1, 2, 3, and 4
- **THEN** the table renders exactly that many value columns
- **AND** no empty column is left behind

#### Scenario: Invalid offer

- **WHEN** one displayed offer has inputs that do not compute
- **THEN** that offer has no column in the table
- **AND** the offers that do compute keep their columns

#### Scenario: No offer computes

- **WHEN** no displayed offer has valid inputs
- **THEN** the table is not rendered
- **AND** the existing empty-state message is shown in its place

### Requirement: Section follows the holding-period input

Heading, section hint, total row label, and table figures SHALL follow the shared holding-period
input. The section hint SHALL define the headline figure, taking its text from the glossary entry
for that figure, so no second copy of the definition exists.

With a holding period entered, the heading SHALL read "Cost to walk away", the total row SHALL read
"Cost to walk away (incl. fees + PMI)", and component rows SHALL show interest paid, PMI paid,
upfront fees, remaining balance, and principal repaid through that period.

With the holding period blank, the heading SHALL read "Cost to term", the total row SHALL read
"Total cost (to term, incl. fees + PMI)", and component rows SHALL show total interest, total PMI,
upfront fees, and principal — remaining balance being zero at term.

#### Scenario: Holding period entered

- **WHEN** the holding period is set to 8 years
- **THEN** the section heading reads "Cost to walk away"
- **AND** the section hint gives the glossary definition of cost to walk away
- **AND** the total row label reads "Cost to walk away (incl. fees + PMI)"
- **AND** the remaining balance row is present

#### Scenario: Holding period cleared

- **WHEN** the holding-period field is cleared
- **THEN** the section heading reads "Cost to term"
- **AND** the section hint gives the glossary definition of total cost
- **AND** the total row label reads "Total cost (to term, incl. fees + PMI)"
- **AND** the remaining balance row is not rendered

### Requirement: Table totals agree with the bars and the card readouts

Each column's component amounts SHALL sum to that column's total. The total SHALL equal cost to
walk away when a holding period is set, total cost to term when it is not. Table figures SHALL come
from the same computation that draws the bar segments, so no figure can disagree with the bar above
it or the readout row inside the card.

#### Scenario: Column sums to its total

- **WHEN** any offer's column is read
- **THEN** its component amounts sum to the printed total, to the dollar

#### Scenario: Table agrees with the card

- **WHEN** a holding period is set and Offer A's card readout is compared with Offer A's column
- **THEN** interest paid, PMI paid, and remaining balance match between the two

#### Scenario: Table agrees with the bar

- **WHEN** a bar segment's hover text is compared with the same component's table cell
- **THEN** both show the same amount

### Requirement: Table carries the bars' color key

Each component row label SHALL carry a color swatch matching that component's bar segment. This
table SHALL be the page's only color key for the bars. No per-offer key SHALL be rendered inside
the offer cards.

Bar segment shading SHALL stay consistent across offers — same component, same ramp position —
with each bar tinted in its own offer's accent. The key column SHALL render in Offer A's accent.

#### Scenario: Key present once

- **WHEN** four offers are displayed
- **THEN** exactly one color key is rendered on the page
- **AND** it is the comparison table's label column

#### Scenario: Card carries no key

- **WHEN** an offer card's readout is inspected
- **THEN** it contains no color swatches

### Requirement: Four offers fit a 390px viewport

At 640px and below, component amounts SHALL be abbreviated to thousands (for example `$252.5k`), so
four offer columns plus the label column fit a 390px viewport without horizontal scrolling. The
total row SHALL keep exact dollars at every width.

Where the table is still wider than its container, it SHALL scroll horizontally inside that
container with the label column held in place, and the page SHALL NOT gain a horizontal scrollbar.

Exact component figures SHALL remain available at every width in the card readouts and in the bar
segments' hover text, so abbreviation never removes a figure from the page.

#### Scenario: Four offers on a phone

- **WHEN** four offers are displayed at 390px wide
- **THEN** component amounts read in abbreviated form
- **AND** the total row reads in exact dollars
- **AND** the page has no horizontal scrollbar

#### Scenario: Desktop width

- **WHEN** the same four offers are displayed at 1280px wide
- **THEN** every amount, component rows included, reads in exact dollars

#### Scenario: Table wider than its box

- **WHEN** the table cannot fit its container at the current width
- **THEN** the table scrolls horizontally within its own container
- **AND** the label column stays visible while the value columns scroll
- **AND** the page does not scroll horizontally

### Requirement: Comparison rendering changes no computed value

The comparison table SHALL be presentation only. No input, control, calculation, or computed figure
SHALL change.

#### Scenario: Results identical before and after

- **WHEN** the same inputs are entered before and after this change
- **THEN** the payment, effective annual rate, LTV, PMI figures, total cost, holding-period
  figures, and verdict are identical
