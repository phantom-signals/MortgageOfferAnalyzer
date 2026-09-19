## MODIFIED Requirements

### Requirement: Card readouts fold on small viewports

Each card's inputs and readout SHALL sit together inside one disclosure control. The card heading
(dot, offer name, add/remove steppers) SHALL stay outside the disclosure control and SHALL remain
visible and operable while the card is collapsed. At 640px and below the disclosure SHALL start
collapsed. Above 640px it SHALL start expanded, so cards stay directly comparable across columns
on desktop.

The summary SHALL show exactly one figure for that offer: payment including PMI for the first
period. When the offer's inputs are invalid, the summary SHALL show the invalid-input message in
place of the figure.

Expanding or collapsing SHALL change no figure and no input value. The reader's open or closed
choice SHALL survive the re-render that follows any input edit.

#### Scenario: Phone-width load

- **WHEN** the tool is opened at 390px wide
- **THEN** each offer card shows its heading and a collapsed summary
- **AND** no rate, term, payments-per-year, fees, or PMI input is visible
- **AND** the summary shows that offer's payment including PMI and no other figure

#### Scenario: Desktop load

- **WHEN** the tool is opened at 1280px wide
- **THEN** each offer card's inputs and readout are expanded
- **AND** the rows line up across the offer columns as before

#### Scenario: Open state survives an edit

- **WHEN** the reader expands Offer B at 390px wide
- **AND** then edits any input
- **THEN** Offer B's inputs and readout are still expanded after the readout re-renders

#### Scenario: Summary ignores the holding period

- **WHEN** the holding-period field is set or cleared
- **THEN** each card's summary shows only payment including PMI
- **AND** neither cost to walk away nor total cost to term appears in the summary

#### Scenario: Invalid inputs while collapsed

- **WHEN** a card's inputs are invalid and the card is collapsed
- **THEN** the summary shows the invalid-input message

#### Scenario: Steppers work while collapsed

- **WHEN** Offer A is collapsed and the reader presses its add-offer stepper
- **THEN** a new offer card is added
- **AND** Offer A stays collapsed

#### Scenario: Folding changes no figure

- **WHEN** a card is collapsed and expanded again
- **THEN** every input holds the value it held before
- **AND** every readout row shows the same value it showed before
