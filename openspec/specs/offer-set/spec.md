# offer-set Specification

## Purpose
How many mortgage offers the tool holds at once: how the count is chosen, how cards are added and removed, how entered values survive a count change, how the verdict behaves at each count, and what stays shared across every offer.

## Requirements
### Requirement: Offer count is user-selectable
The tool SHALL provide a control in the shared-inputs card that sets how many offers are displayed. The control SHALL accept the integer values 1, 2, 3, and 4, and SHALL reject values outside that range.

#### Scenario: Control default on load
- **WHEN** the file is opened in a browser with no prior interaction
- **THEN** the offer-count control reads 1
- **AND** exactly one offer card is rendered

#### Scenario: User raises the count
- **WHEN** the user sets the offer-count control to 3
- **THEN** three offer cards are rendered, labeled Offer A, Offer B, and Offer C
- **AND** each card computes and displays its own readout

#### Scenario: Out-of-range value
- **WHEN** a value below 1 or above 4 is submitted through the control
- **THEN** the rendered offer count is clamped to the nearest allowed value (1 or 4)
- **AND** no card is left in a partially rendered state

### Requirement: Single offer is the default analysis mode
With exactly one offer, the tool SHALL present itself as an analyzer of that offer and SHALL NOT present comparison output.

#### Scenario: Verdict hidden at count 1
- **WHEN** the offer count is 1
- **THEN** the verdict bar is not displayed
- **AND** the single offer's readout still shows payment, effective annual rate, initial LTV, total interest, PMI figures, and total cost

#### Scenario: Holding period at count 1
- **WHEN** the offer count is 1 and a holding period is entered
- **THEN** the single card's readout includes the through-holding-period rows (payments made, interest paid, PMI paid, remaining balance, cost to walk away)

#### Scenario: Verdict returns above count 1
- **WHEN** the offer count is raised from 1 to 2
- **THEN** the verdict bar is displayed
- **AND** it compares the two offers on the same basis used today (full-term total cost, or cost to clear when a holding period is set)

### Requirement: Changing the count preserves entered values
Changing the offer count SHALL NOT discard input values in the cards that remain. Cards SHALL be added and removed only at the end of the list.

#### Scenario: Raising the count keeps earlier cards
- **WHEN** the user edits Offer A's rate to 5.5, then raises the count from 1 to 2
- **THEN** Offer A's rate still reads 5.5
- **AND** every other Offer A input keeps its entered value

#### Scenario: New cards get default values
- **WHEN** a new offer card is added
- **THEN** its rate, term, payments per year, upfront fees, and PMI rate are populated with the tool's default values
- **AND** its readout computes immediately without further input

#### Scenario: Lowering the count drops trailing cards
- **WHEN** the offer count is 3 and the user lowers it to 2
- **THEN** Offer C is removed
- **AND** Offer A and Offer B keep their entered values and readouts

#### Scenario: Lowered card values are not restored
- **WHEN** the count is lowered from 2 to 1 and then raised back to 2
- **THEN** the new Offer B is populated with default values, not the previously entered ones

### Requirement: Verdict ranks every displayed offer
With two or more offers, the verdict SHALL name the cheapest offer on the active comparison basis and SHALL state the gap between it and the next-cheapest offer.

#### Scenario: Three offers, distinct costs
- **WHEN** the offer count is 3 and the three offers have distinct total costs
- **THEN** the verdict names the cheapest offer
- **AND** the amount shown is the difference between the cheapest and the second-cheapest offer
- **AND** the cheapest offer's own total cost is shown alongside the difference

#### Scenario: Tie for cheapest
- **WHEN** two or more offers tie for the lowest cost within half a dollar
- **THEN** the verdict states that the cheapest offers cost the same
- **AND** shows that shared cost

#### Scenario: One offer has invalid inputs
- **WHEN** the offer count is 3 and one card's inputs are incomplete or invalid
- **THEN** that card's readout shows the existing invalid-input message
- **AND** the verdict ranks only the offers that computed successfully

#### Scenario: No offer computes
- **WHEN** no displayed offer has valid inputs
- **THEN** the verdict headline and amount both show an em dash, as they do today

### Requirement: Each offer card is visually distinguishable
Every displayed offer card SHALL carry a distinct accent color applied to its top border, heading, dot, and focused-input outline, in both light and dark color schemes.

#### Scenario: Four offers displayed
- **WHEN** the offer count is 4
- **THEN** the four cards use four different accent colors
- **AND** each color meets the contrast used by the existing Offer A and Offer B accents against the card background in the active color scheme

#### Scenario: Verdict names a winner by color
- **WHEN** the verdict names the cheapest offer
- **THEN** the offer letter in the verdict is rendered in that offer's accent color

### Requirement: Shared inputs and per-offer math are unchanged
Loan amount, holding period, home value, PMI removal rule, and PMI premium basis SHALL remain single shared inputs applied identically to every offer. The per-offer payment, effective annual rate, PMI schedule, total cost, and holding-period figures SHALL be computed by the existing formulas without modification.

#### Scenario: Shared input propagates to all offers
- **WHEN** the offer count is 4 and the loan amount is changed
- **THEN** all four readouts recompute against the new loan amount

#### Scenario: Single-offer results match today's Offer A
- **WHEN** the offer count is 1 and the shared inputs and offer inputs are set to the values that Offer A shows today
- **THEN** every value in the readout is identical to the value the current two-offer tool prints for Offer A
