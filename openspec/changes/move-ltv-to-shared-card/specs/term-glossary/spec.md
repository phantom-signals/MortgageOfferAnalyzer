## MODIFIED Requirements

### Requirement: Hovering a term shows its definition
Input labels, readout row labels, and the shared card's initial LTV readout SHALL expose their glossary definition as native browser hover text via the `title` attribute. Hover text SHALL NOT replace the glossary; both SHALL be present.

The LTV definition SHALL reach the reader from the shared readout, since no offer readout row carries that term any more.

#### Scenario: Hover the shared LTV readout
- **WHEN** the pointer rests over the initial LTV readout in the shared card
- **THEN** the browser shows the initial LTV definition as hover text
- **AND** the text matches the glossary entry for initial LTV

#### Scenario: Hover a readout row label
- **WHEN** the pointer rests over the "Effective annual rate" row label in an offer readout
- **THEN** the browser shows the effective annual rate definition as hover text

#### Scenario: Hover an input label
- **WHEN** the pointer rests over the "PMI annual rate (%)" label
- **THEN** the browser shows the PMI definition as hover text

#### Scenario: Hover text on cloned offer cards
- **WHEN** the offer count is raised so Offer B, C, or D is rendered
- **THEN** the labels on the added cards carry the same hover definitions as Offer A's labels

#### Scenario: Existing select hover text is preserved
- **WHEN** the pointer rests over the PMI removal rule or PMI premium basis control, or over one of their options
- **THEN** the existing detailed hover text on those controls still appears, unchanged

#### Scenario: Specific term still beats the general one
- **WHEN** the shared readout's definition is resolved from its label text
- **THEN** it resolves to the "Initial LTV" entry, not the general "LTV (loan-to-value)" entry

### Requirement: Tapping a readout row label shows its definition

Readout row labels that carry a definition SHALL open that definition on click or tap. The shared card's initial LTV readout SHALL open its definition the same way, so touch readers keep tap-to-define for LTV after the per-offer row is removed. The definition SHALL be shown in a single shared element using the native HTML Popover API, so it renders in the top layer, dismisses on outside click, and dismisses on Escape without custom code.

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

#### Scenario: Row label with no definition

- **WHEN** the reader taps a readout row label that has no glossary match
- **THEN** no popover opens
- **AND** no error is raised
