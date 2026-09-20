## MODIFIED Requirements

### Requirement: Offer count is user-selectable
The tool SHALL provide add and remove controls in each offer card's heading that set how many offers
are displayed. The controls SHALL hold the count within the integer range 1 to 4. No offer-count
control SHALL appear in the shared-inputs card.

The remove control SHALL remove the card it sits in. The add control SHALL insert one card directly
after the card it sits in, holding the tool's default values; the offers after that position SHALL
keep their own values, shifted one position later. Every displayed card SHALL offer an add control.
The remove control SHALL be unavailable when one offer is displayed, and the add control SHALL be
unavailable on every card when four offers are displayed.

#### Scenario: Control default on load
- **WHEN** the file is opened in a browser with no prior interaction
- **THEN** exactly two offer cards are rendered, labeled Offer A and Offer B
- **AND** no offer-count control appears in the shared-inputs card

#### Scenario: User raises the count
- **WHEN** the user presses the add control on the last card until three cards are displayed
- **THEN** three offer cards are rendered, labeled Offer A, Offer B, and Offer C
- **AND** each card computes and displays its own readout

#### Scenario: Add from a card that is not the last
- **WHEN** three offers are displayed and the user presses the add control on the first card
- **THEN** four offer cards are rendered
- **AND** the new card is the second card, holding the tool's default values
- **AND** the offers that followed the first card hold their own values, each one position later

#### Scenario: Out-of-range value
- **WHEN** a count below 1 or above 4 is requested through any path, including a restored link
- **THEN** the rendered offer count is clamped to the nearest allowed value (1 or 4)
- **AND** no card is left in a partially rendered state

#### Scenario: Bounds are unreachable through the controls
- **WHEN** one offer is displayed
- **THEN** that card's remove control is not available
- **WHEN** fewer than four offers are displayed
- **THEN** every card offers an available add control
- **WHEN** four offers are displayed
- **THEN** no card offers an available add control

### Requirement: Changing the count preserves entered values
Adding or removing an offer SHALL NOT discard input values in the cards that remain. A card added
through an add control SHALL take the position directly after the card whose control was used; the
offers after that position SHALL keep their values, shifted one position later. Removing a card
SHALL remove the offer whose remove control was used; the offers after it SHALL keep their values,
shifted one position earlier.

#### Scenario: Adding keeps the cards already displayed
- **WHEN** the user edits Offer A's rate to 5.5, then presses Offer A's add control
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

#### Scenario: Removing drops the card whose control was used
- **WHEN** three offers are displayed and the user presses Offer B's remove control
- **THEN** two offer cards are rendered
- **AND** Offer A keeps its entered values
- **AND** the offer that was Offer C holds its own values, now as Offer B

#### Scenario: Removed card values are not restored
- **WHEN** a card is removed and another is then added
- **THEN** the new card is populated with default values, not the removed card's values
