## ADDED Requirements

### Requirement: Comparison table labels carry definitions

Component and total row labels in the cost comparison table SHALL expose their glossary definition
the way readout row labels do: as native `title` hover text, and as the shared popover on click or
tap. Definitions SHALL come from the same single source as the glossary and the readout rows, so no
third copy of any definition text exists.

Labels SHALL keep their definitions through the re-render that follows any input edit, and through
the change of wording when the holding-period input is set or cleared.

#### Scenario: Hover a table row label

- **WHEN** the pointer rests over the "Remaining balance" label in the comparison table
- **THEN** the browser shows the remaining balance definition as hover text
- **AND** the text matches the glossary entry

#### Scenario: Tap a table row label

- **WHEN** the reader taps the "Cost to walk away (incl. fees + PMI)" label in the comparison table
- **THEN** the popover opens showing the cost to walk away definition

#### Scenario: Definitions survive re-render

- **WHEN** the reader edits any input, causing the table to re-render
- **AND** the reader then taps a table row label
- **THEN** the popover still opens with that label's definition

#### Scenario: Definitions follow the mode flip

- **WHEN** the holding-period field is cleared and the rows change to their to-term wording
- **THEN** the new labels carry the definitions for the terms they now name

#### Scenario: Table label with no definition

- **WHEN** the reader taps a table label that has no glossary match
- **THEN** no popover opens
- **AND** no error is raised
