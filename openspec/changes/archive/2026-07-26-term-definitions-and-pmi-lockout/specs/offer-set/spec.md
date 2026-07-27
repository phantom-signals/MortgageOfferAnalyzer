## MODIFIED Requirements

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

#### Scenario: New card added while PMI is locked
- **WHEN** a new offer card is added and the shared inputs give an initial LTV at or below 80%
- **THEN** the new card's rate, term, payments per year, and upfront fees are populated with the tool's default values
- **AND** its PMI rate reads 0 and is disabled, matching every other card
- **AND** raising the LTV above 80% restores the card's default PMI rate

#### Scenario: Lowering the count drops trailing cards
- **WHEN** the offer count is 3 and the user lowers it to 2
- **THEN** Offer C is removed
- **AND** Offer A and Offer B keep their entered values and readouts

#### Scenario: Lowered card values are not restored
- **WHEN** the count is lowered from 2 to 1 and then raised back to 2
- **THEN** the new Offer B is populated with default values, not the previously entered ones
