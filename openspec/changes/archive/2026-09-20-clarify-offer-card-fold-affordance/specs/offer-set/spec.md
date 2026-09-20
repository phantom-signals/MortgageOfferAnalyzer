## MODIFIED Requirements

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
