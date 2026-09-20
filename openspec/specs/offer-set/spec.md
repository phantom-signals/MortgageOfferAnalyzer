# offer-set Specification

## Purpose
How many mortgage offers the tool holds at once: how the count is chosen, how cards are added and removed, how entered values survive a count change, how the verdict behaves at each count, and what stays shared across every offer.
## Requirements
### Requirement: Offer count is set by per-card steppers
The tool SHALL provide add and remove controls in each offer card's heading that set how many offers
are displayed. The controls SHALL hold the count within the integer range 1 to 4. No offer-count
control SHALL appear in the shared-inputs card.

The remove control SHALL remove the card it sits in. The add control SHALL insert one card directly
after the card it sits in, holding a copy of that card's current values; the offers after that
position SHALL keep their own values, shifted one position later. Every displayed card SHALL offer an
add control. The remove control SHALL be unavailable when one offer is displayed, and the add control
SHALL be unavailable on every card when four offers are displayed.

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
- **AND** the new card is the second card, holding a copy of the first card's values
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

### Requirement: Single offer is the default analysis mode
With exactly one offer, the tool SHALL present itself as an analyzer of that offer and SHALL NOT present comparison output.

#### Scenario: Verdict hidden at count 1
- **WHEN** the offer count is 1
- **THEN** the verdict bar is not displayed
- **AND** the single offer's readout still shows payment, effective annual rate, total interest, PMI figures, and total cost
- **AND** the initial LTV is not among them; it is shown once in the shared-input card

#### Scenario: Holding period at count 1
- **WHEN** the offer count is 1 and a holding period is entered
- **THEN** the single card's readout includes the through-holding-period rows (payments made, interest paid, PMI paid, remaining balance, cost to walk away)

#### Scenario: Verdict returns above count 1
- **WHEN** the offer count is raised from 1 to 2
- **THEN** the verdict bar is displayed
- **AND** it compares the two offers on the same basis used today (full-term total cost, or cost to clear when a holding period is set)

### Requirement: Changing the count preserves entered values
Adding or removing an offer SHALL NOT discard input values in the cards that remain. A card added
through an add control SHALL take the position directly after the card whose control was used and
SHALL be populated with a copy of that card's current values, covering rate, term, payments per year,
upfront fees, and PMI rate; the offers after that position SHALL keep their values, shifted one
position later. Removing a card SHALL remove the offer whose remove control was used; the offers
after it SHALL keep their values, shifted one position earlier.

A card whose PMI rate is locked by the shared LTV SHALL copy the rate held for it while locked, not
the zero it displays, so that unlocking shows the source card's rate on both cards.

Cards rendered by a path other than the add control — a restored share link, or any other change of
the rendered count — SHALL be populated with the tool's default values.

#### Scenario: Adding keeps the cards already displayed
- **WHEN** the user edits Offer A's rate to 5.5, then presses Offer A's add control
- **THEN** Offer A's rate still reads 5.5
- **AND** every other Offer A input keeps its entered value

#### Scenario: New card copies the card it was added from
- **WHEN** the user sets Offer A's rate to 5.5, term to 15, payments per year to 26, upfront fees to 4100, and PMI rate to 0.63, then presses Offer A's add control
- **THEN** the new card reads rate 5.5, term 15, payments per year 26, upfront fees 4100, and PMI rate 0.63
- **AND** its readout computes immediately without further input
- **AND** its readout matches Offer A's readout value for value

#### Scenario: New card added while PMI is locked
- **WHEN** the shared inputs give an initial LTV at or below 80%, the source card holds a PMI rate of 0.42 behind the lock, and the user presses that card's add control
- **THEN** the new card's rate, term, payments per year, and upfront fees copy the source card's values
- **AND** its PMI rate reads 0 and is disabled, matching every other card
- **AND** raising the LTV above 80% shows 0.42 on both the source card and the new card

#### Scenario: Card rendered outside the add control gets default values
- **WHEN** a card is rendered by a restored share link that carries no value for it
- **THEN** its rate, term, payments per year, upfront fees, and PMI rate are populated with the tool's default values

#### Scenario: Removing drops the card whose control was used
- **WHEN** three offers are displayed and the user presses Offer B's remove control
- **THEN** two offer cards are rendered
- **AND** Offer A keeps its entered values
- **AND** the offer that was Offer C holds its own values, now as Offer B

#### Scenario: Removed card values are not restored
- **WHEN** a card is removed and the user then presses another card's add control
- **THEN** the new card copies the card whose control was used, not the removed card's values

### Requirement: Verdict ranks every displayed offer
With two or more offers, the verdict SHALL name the cheapest offer on the active comparison basis and SHALL state the gap between it and the next-cheapest offer. When two or more offers tie for cheapest, the verdict SHALL name every tied offer by its letter instead of stating a gap.

Offers SHALL count as tied when the gap between them is strictly under half a dollar. The window exists because float noise, not a real difference, is what separates two offers costing the same to the cent; a gap of exactly half a dollar is a real difference and SHALL NOT be treated as a tie.

#### Scenario: Three offers, distinct costs
- **WHEN** the offer count is 3 and the three offers have distinct total costs
- **THEN** the verdict names the cheapest offer
- **AND** the amount shown is the difference between the cheapest and the second-cheapest offer
- **AND** the cheapest offer's own total cost is shown alongside the difference

#### Scenario: Two offers tie for cheapest
- **WHEN** two offers' costs differ by less than half a dollar
- **THEN** the verdict names both offers by letter, joined by "and"
- **AND** states that they cost the same
- **AND** shows that shared cost as the amount

#### Scenario: Three or more offers tie for cheapest
- **WHEN** three or more offers' costs differ from the lowest by less than half a dollar
- **THEN** the verdict names every tied offer by letter, comma-separated with "and" before the last
- **AND** shows the shared cost as the amount

#### Scenario: Tie among cheapest with a costlier offer present
- **WHEN** the offer count is 3, two offers' costs differ by less than half a dollar, and the third costs more
- **THEN** the verdict names only the two tied offers
- **AND** the costlier offer is not named

#### Scenario: Near-tie is not a tie
- **WHEN** the cheapest and second-cheapest offers differ by exactly half a dollar or more
- **THEN** the verdict names one cheapest offer and states the gap, as it does for distinct costs

#### Scenario: One offer has invalid inputs
- **WHEN** the offer count is 3 and one card's inputs are incomplete or invalid
- **THEN** that card's readout shows the existing invalid-input message
- **AND** the verdict ranks only the offers that computed successfully

#### Scenario: No offer computes
- **WHEN** no displayed offer has valid inputs
- **THEN** the verdict headline and amount both show an em dash, as they do today

### Requirement: Each offer card is visually distinguishable
Every displayed offer card SHALL carry a distinct accent color applied to its top border, heading, stepper glyphs, focused-input outline, and its full border while its heading row is hovered, in both light and dark color schemes. Every offer letter printed in the verdict SHALL be rendered in that offer's accent color. No color dot SHALL carry the accent in the card heading; the marks listed above are what identify the card.

#### Scenario: Four offers displayed
- **WHEN** the offer count is 4
- **THEN** the four cards use four different accent colors
- **AND** each color meets the contrast used by the existing Offer A and Offer B accents against the card background in the active color scheme

#### Scenario: Accent carriers after the dot is gone
- **WHEN** any offer card is rendered
- **THEN** its accent color appears on its top border, its heading text, and its stepper glyphs
- **AND** focusing one of its inputs draws that input's outline in the same accent color
- **AND** hovering its heading row draws its full border in the same accent color
- **AND** no color dot appears in the heading

#### Scenario: Verdict names a winner by color
- **WHEN** the verdict names the cheapest offer
- **THEN** the offer letter in the verdict is rendered in that offer's accent color

#### Scenario: Verdict names tied offers by color
- **WHEN** the verdict names two or more tied offers
- **THEN** each named letter is rendered in that offer's own accent color

### Requirement: Shared inputs and per-offer math are unchanged
Loan amount, holding period, home value, PMI removal rule, and PMI premium basis SHALL remain single shared inputs applied identically to every offer. The per-offer payment, effective annual rate, PMI schedule, total cost, and holding-period figures SHALL be computed by the existing formulas without modification.

#### Scenario: Shared input propagates to all offers
- **WHEN** the offer count is 4 and the loan amount is changed
- **THEN** all four readouts recompute against the new loan amount

#### Scenario: Single-offer results match today's Offer A
- **WHEN** the offer count is 1 and the shared inputs and offer inputs are set to the values that Offer A shows today
- **THEN** every value in the readout is identical to the value the current two-offer tool prints for Offer A

