## ADDED Requirements

### Requirement: Section headings carry definitions

The cost comparison heading and the cost-over-time heading SHALL expose their glossary definition
as native `title` hover text and SHALL open it in the shared definition popover on click or tap,
dismissing the same way as for readout row labels. The glossary SHALL carry a "Cost over time"
entry whose definition explains that the chart shows what walking away at any point costs,
including payoff of the balance still owed.

The cost comparison heading SHALL carry the definition for the wording it currently shows, through
every flip of the holding-period input. "Cost to term" SHALL resolve to the total cost entry, not
the term entry.

Only these two headings SHALL gain definitions. Other section labels, such as "Verdict",
"Glossary", and "Privacy and Terms of Use", SHALL carry no definition and SHALL open no popover.

#### Scenario: Tap the cost-over-time heading

- **WHEN** the reader taps the "Cost over time" heading
- **THEN** the popover opens showing the cost over time glossary definition

#### Scenario: Tap the cost comparison heading at term

- **WHEN** the holding-period field is blank and the reader taps the "Cost to term" heading
- **THEN** the popover opens showing the total cost definition

#### Scenario: Footer section label stays inert

- **WHEN** the reader clicks the "Privacy and Terms of Use" summary
- **THEN** no definition popover opens
- **AND** the section toggles as before

### Requirement: Holding period definition states unit and blank behavior

The holding period glossary definition SHALL state that the period is in years and that leaving it
blank runs costs to full term, since the input label no longer carries that hint.

#### Scenario: Tap the holding period label

- **WHEN** the reader taps the "Holding period (years)" label
- **THEN** the popover text says the period is in years
- **AND** says a blank field runs costs to full term

## MODIFIED Requirements

### Requirement: Hovering a term shows its definition
Input labels, readout row labels, and the shared card's initial LTV readout SHALL expose their glossary definition as native browser hover text via the `title` attribute. Hover text SHALL NOT replace the glossary; both SHALL be present.

The LTV definition SHALL reach the reader from the shared readout, since no offer readout row carries that term any more.

A readout row that is a section divider rather than a figure — "Through holding period" — resolves like any other row label and MAY therefore carry a definition. This is correct where the entry it resolves to names the divider's own subject, and SHALL NOT be suppressed with an exclusion list.

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
- **WHEN** a label is resolved whose text also contains a more general term, such as "Total interest"
- **THEN** it resolves to the "Total interest" entry, not to the "Interest paid" entry that also matches on "interest"
- **AND** the shared readout resolves to "Initial LTV"

#### Scenario: A prose-only entry cannot capture a label
- **WHEN** a label containing "LTV" is resolved
- **THEN** it never resolves to the general "LTV (loan-to-value)" entry, which carries no match tokens
- **AND** that entry is still rendered in the glossary

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

- **WHEN** the reader taps the "Total interest" row label in an offer readout
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

### Requirement: Label resolution does not depend on entry order
When a label contains match tokens from more than one entry, it SHALL resolve to the entry whose matching token is longest. Entry position in the glossary SHALL NOT decide which definition a label receives, except to break a tie between equal-length matching tokens.

#### Scenario: Specific entry wins though it sorts later
- **WHEN** "Total interest" is resolved while "Interest paid" sorts before "Total interest"
- **THEN** it resolves to the "Total interest" entry

#### Scenario: Specific PMI entry wins over general PMI
- **WHEN** "PMI annual rate (%)" is resolved while "PMI (private mortgage insurance)" sorts before "PMI annual rate"
- **THEN** it resolves to the "PMI annual rate" entry

#### Scenario: Hover text unchanged by reorder
- **WHEN** every input label, readout row label, and shared readout is resolved before and after the reorder
- **THEN** each receives the same definition text as before
