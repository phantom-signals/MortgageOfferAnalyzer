## MODIFIED Requirements

### Requirement: Verdict ranks every displayed offer
With two or more offers, the verdict SHALL name the cheapest offer on the active comparison basis and SHALL state the gap between it and the next-cheapest offer. When two or more offers tie for cheapest, the verdict SHALL name every tied offer by its letter instead of stating a gap.

#### Scenario: Three offers, distinct costs
- **WHEN** the offer count is 3 and the three offers have distinct total costs
- **THEN** the verdict names the cheapest offer
- **AND** the amount shown is the difference between the cheapest and the second-cheapest offer
- **AND** the cheapest offer's own total cost is shown alongside the difference

#### Scenario: Two offers tie for cheapest
- **WHEN** two offers tie for the lowest cost within half a dollar
- **THEN** the verdict names both offers by letter, joined by "and"
- **AND** states that they cost the same
- **AND** shows that shared cost as the amount

#### Scenario: Three or more offers tie for cheapest
- **WHEN** three or more offers tie for the lowest cost within half a dollar
- **THEN** the verdict names every tied offer by letter, comma-separated with "and" before the last
- **AND** shows the shared cost as the amount

#### Scenario: Tie among cheapest with a costlier offer present
- **WHEN** the offer count is 3, two offers tie for the lowest cost within half a dollar, and the third costs more
- **THEN** the verdict names only the two tied offers
- **AND** the costlier offer is not named

#### Scenario: Near-tie is not a tie
- **WHEN** the cheapest and second-cheapest offers differ by more than half a dollar
- **THEN** the verdict names one cheapest offer and states the gap, as it does for distinct costs

#### Scenario: One offer has invalid inputs
- **WHEN** the offer count is 3 and one card's inputs are incomplete or invalid
- **THEN** that card's readout shows the existing invalid-input message
- **AND** the verdict ranks only the offers that computed successfully

#### Scenario: No offer computes
- **WHEN** no displayed offer has valid inputs
- **THEN** the verdict headline and amount both show an em dash, as they do today

### Requirement: Each offer card is visually distinguishable
Every displayed offer card SHALL carry a distinct accent color applied to its top border, heading, dot, and focused-input outline, in both light and dark color schemes. Every offer letter printed in the verdict SHALL be rendered in that offer's accent color.

#### Scenario: Four offers displayed
- **WHEN** the offer count is 4
- **THEN** the four cards use four different accent colors
- **AND** each color meets the contrast used by the existing Offer A and Offer B accents against the card background in the active color scheme

#### Scenario: Verdict names a winner by color
- **WHEN** the verdict names the cheapest offer
- **THEN** the offer letter in the verdict is rendered in that offer's accent color

#### Scenario: Verdict names tied offers by color
- **WHEN** the verdict names two or more tied offers
- **THEN** each named letter is rendered in that offer's own accent color
