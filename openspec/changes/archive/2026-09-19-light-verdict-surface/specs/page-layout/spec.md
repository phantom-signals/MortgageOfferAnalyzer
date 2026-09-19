## ADDED Requirements

### Requirement: Verdict bar colors follow color scheme

In the light color scheme the verdict bar SHALL use the card background, ink text color, and a
card-style border, so the offer letters it prints sit on the background their light-scheme accents
were chosen for. In the dark color scheme the verdict bar SHALL keep its current dark background
and light text. The chart tooltip and definition popover SHALL keep their current colors in both
schemes.

#### Scenario: Light scheme verdict

- **WHEN** the tool is opened with two offers in the light color scheme
- **THEN** the verdict bar background matches the offer card background
- **AND** the verdict text uses the ink color
- **AND** the winning offer letter renders in that offer's light-scheme accent color

#### Scenario: Dark scheme verdict unchanged

- **WHEN** the tool is opened with two offers in the dark color scheme
- **THEN** the verdict bar background, text color, and letter colors are identical to before this change

#### Scenario: Overlays unchanged

- **WHEN** the reader hovers the cost chart or opens a term definition in the light color scheme
- **THEN** the tooltip and popover keep their dark background and light text
