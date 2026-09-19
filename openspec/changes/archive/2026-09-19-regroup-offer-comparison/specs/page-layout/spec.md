## ADDED Requirements

### Requirement: Verdict sits above the offers

The verdict block SHALL render above the offers grid, below the shared-input card, so the
conclusion is reached before any per-offer detail. It SHALL keep its content, ranking logic, and
hidden state at an offer count of 1.

#### Scenario: Verdict reached first on a phone

- **WHEN** the tool is viewed at 390px wide with two or more offers
- **THEN** the verdict is the first block below the shared-input card
- **AND** the offer cards, the cost bars, and the cost-over-time chart all follow it

#### Scenario: Single offer

- **WHEN** the offer count is 1
- **THEN** the verdict block is hidden, as before
- **AND** the shared-input card is followed directly by the offer card

#### Scenario: Verdict content unchanged

- **WHEN** two offers are entered and a holding period is set
- **THEN** the verdict names the same winning offer and amount it named before the move

### Requirement: Card readouts fold on small viewports

Each card's readout SHALL sit inside a disclosure control. At 640px and below the readout SHALL
start collapsed. Above 640px it SHALL start expanded, so cards stay directly comparable across
columns on desktop.

The summary SHALL always show two figures for that offer: payment including PMI for the first
period, and the headline total — cost to walk away with a holding period set, total cost to term
without.

Expanding or collapsing SHALL change no figure. The reader's open or closed choice SHALL survive
the re-render that follows any input edit.

#### Scenario: Phone-width load

- **WHEN** the tool is opened at 390px wide
- **THEN** each offer card shows its inputs and a collapsed readout summary
- **AND** the summary shows that offer's payment including PMI and its headline total

#### Scenario: Desktop load

- **WHEN** the tool is opened at 1280px wide
- **THEN** each offer card's readout is expanded
- **AND** the rows line up across the offer columns as before

#### Scenario: Open state survives an edit

- **WHEN** the reader expands Offer B's readout at 390px wide
- **AND** then edits any input
- **THEN** Offer B's readout is still expanded after the readout re-renders

#### Scenario: Summary follows the holding period

- **WHEN** the holding-period field is cleared
- **THEN** each card's summary shows total cost to term in place of cost to walk away

#### Scenario: Folding changes no figure

- **WHEN** a readout is collapsed and expanded again
- **THEN** every row shows the same value it showed before
