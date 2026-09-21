## ADDED Requirements

### Requirement: Share disclosure text is left-aligned
The disclosure text accompanying the copy-link control SHALL render its lines left-aligned, not centered, at every viewport width. The copy-link control itself SHALL stay horizontally centered, and the disclosure text block SHALL stay horizontally centered under it with its existing measure limit; only the alignment of the lines inside that block changes. The text SHALL NOT be justified.

#### Scenario: Wrapped disclosure on a narrow viewport
- **WHEN** the viewport is narrow enough that the disclosure text under the copy-link control wraps to more than one line
- **THEN** every line of that text starts at the same left edge
- **AND** the line ends are ragged, with no stretched word spacing

#### Scenario: Control stays centered
- **WHEN** the copy-link control and its disclosure text are rendered at any viewport width
- **THEN** the control remains horizontally centered in the content container
- **AND** the disclosure text block remains horizontally centered under the control
