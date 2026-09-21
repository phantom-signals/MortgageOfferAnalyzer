# cost-comparison Specification

## Purpose
The section under the cost bars: one table comparing every offer's cost components side by side, the page's single color key for the bars, how it follows the holding-period input, and how it fits four offers on a phone.
## Requirements
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

Heading, heading definition, total row label, and table figures SHALL follow the shared
holding-period input. The heading SHALL carry no parenthetical hint. Instead the heading SHALL expose
the glossary definition of the headline figure as `title` hover text and in the shared definition
popover, taken from the glossary entry so no second copy of the definition exists. The heading's
definition SHALL change with the heading wording.

Component row labels SHALL be bare nouns naming the component. The row sits under a heading that
already names the period, so the card readout's "... paid" phrasing would repeat it once per row;
the table and the card therefore label the same figure differently by design.

With a holding period entered, the heading SHALL read "Cost to walk away" and carry the cost to walk
away definition, the total row SHALL read "Cost to walk away (incl. fees + PMI)", and component rows
SHALL read "Interest", "PMI", "Upfront fees", "Remaining balance", and "Principal", each measured
through that period.

With the holding period blank, the heading SHALL read "Cost to term" and carry the total cost
definition, not the term definition, the total row SHALL read "Total cost (incl. fees +
PMI)", and component rows SHALL read "Total interest", "Total PMI", "Upfront fees", and "Principal",
remaining balance being zero at term. Only the two rows that would otherwise be ambiguous across the
two modes take a distinct to-term label.

#### Scenario: Holding period entered

- **WHEN** the holding period is set to 8 years
- **THEN** the section heading reads "Cost to walk away" with no parenthetical after it
- **AND** the heading's hover text is the glossary definition for cost to walk away
- **AND** the total row label reads "Cost to walk away (incl. fees + PMI)"
- **AND** the interest row is labelled "Interest", not "Interest paid"
- **AND** the remaining balance row is present

#### Scenario: Holding period cleared

- **WHEN** the holding-period field is cleared
- **THEN** the section heading reads "Cost to term" with no parenthetical after it
- **AND** the heading's hover text is the glossary definition for total cost
- **AND** the total row label reads "Total cost (incl. fees + PMI)"
- **AND** the interest row is labelled "Total interest"
- **AND** the remaining balance row is not rendered

#### Scenario: Heading definition follows a second flip

- **WHEN** the holding-period field is cleared and then set to 8 years again
- **THEN** the heading's hover text is the glossary definition for cost to walk away

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
- **THEN** the interest, PMI, and remaining balance amounts match between the two, though the card
  and the table label them differently

#### Scenario: Table agrees with the bar

- **WHEN** a bar segment's hover text is compared with the same component's table cell
- **THEN** both show the same amount

### Requirement: Table carries the bars' color key

Each component row label SHALL carry a color swatch matching that component's bar segment. This
table SHALL be the page's only key for the bar segments. No per-offer key SHALL be rendered inside
the offer cards. The cost-over-time chart's legend keys offers to their accents, not components to
their segments, and SHALL NOT count against this.

Bar segment shading SHALL stay consistent across offers — same component, same ramp position —
with each bar tinted in its own offer's accent. The key column SHALL render in Offer A's accent.

#### Scenario: Key present once

- **WHEN** four offers are displayed
- **THEN** exactly one key for the bar segments is rendered on the page
- **AND** it is the comparison table's label column
- **AND** the chart legend is the page's only other color key, and it names offers, not components

#### Scenario: Card carries no key

- **WHEN** an offer card's readout is inspected
- **THEN** it contains no color swatches

### Requirement: Four offers fit a 390px viewport

At 640px and below, component amounts SHALL be abbreviated in compact notation to one decimal —
`$252.5K`, and `$1.3M` once an amount reaches a million — so four offer columns plus the label
column fit a 390px viewport without horizontal scrolling. The
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

