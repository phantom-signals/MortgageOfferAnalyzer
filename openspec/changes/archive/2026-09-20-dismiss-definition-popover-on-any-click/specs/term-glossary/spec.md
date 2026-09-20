## MODIFIED Requirements

### Requirement: Tapping a readout row label shows its definition

Readout row labels that carry a definition SHALL open that definition on click or tap. The shared card's initial LTV readout SHALL open its definition the same way, so touch readers keep tap-to-define for LTV after the per-offer row is removed. The definition SHALL be shown in a single shared element using the native HTML Popover API, so it renders in the top layer.

An open popover SHALL close on a click or tap anywhere on the page: outside it, on the popover itself, and on the label that opened it. A click on a different label carrying a definition SHALL replace the text rather than close. Escape SHALL still close an open popover. The popover SHALL carry no visible close control, and its appearance SHALL be unchanged.

The popover SHALL work on every offer card, including cards added after load, and SHALL survive the re-render that follows any input change. The shared readout SHALL keep its definition through every re-render of its value.

#### Scenario: Tap the shared LTV readout

- **WHEN** the reader taps the initial LTV readout in the shared card
- **THEN** a popover opens showing the initial LTV definition
- **AND** the definition text matches the glossary entry

#### Scenario: Shared readout keeps its definition after an edit

- **WHEN** the reader changes the loan amount, causing the readout value to update
- **AND** the reader then taps the readout
- **THEN** the popover still opens with the initial LTV definition

#### Scenario: Tap a readout row label

- **WHEN** the reader taps the "Total interest (to term)" row label in an offer readout
- **THEN** a popover opens showing the total interest definition
- **AND** the definition text matches the glossary entry for total interest

#### Scenario: Tap a row label on an added offer card

- **WHEN** the offer count is raised so Offer B, C, or D is rendered
- **AND** the reader taps a readout row label on the added card
- **THEN** the popover opens with that row's definition

#### Scenario: Popover survives re-render

- **WHEN** the reader edits any input, causing the readouts to re-render
- **AND** the reader then taps a readout row label
- **THEN** the popover still opens with that row's definition

#### Scenario: Tap a second label while one is open

- **WHEN** a popover is open for one row label
- **AND** the reader taps a different row label
- **THEN** the popover shows the second row's definition

#### Scenario: Dismiss by tapping away

- **WHEN** a popover is open
- **AND** the reader taps outside it
- **THEN** the popover closes

#### Scenario: Dismiss by tapping the popover

- **WHEN** a popover is open
- **AND** the reader taps the popover text itself
- **THEN** the popover closes

#### Scenario: Dismiss by tapping the label that opened it

- **WHEN** a popover is open for a row label
- **AND** the reader taps that same row label again
- **THEN** the popover closes
- **AND** it does not reopen

#### Scenario: Dismiss with Escape

- **WHEN** a popover is open
- **AND** the reader presses Escape
- **THEN** the popover closes

#### Scenario: Popover shows no close control

- **WHEN** a popover is open
- **THEN** it renders the definition text only
- **AND** no close button, icon, or dismissal instruction is added

#### Scenario: Row label with no definition

- **WHEN** the reader taps a readout row label that has no glossary match
- **THEN** no popover opens
- **AND** no error is raised
