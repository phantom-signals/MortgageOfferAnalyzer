# shared-ltv-readout Specification

## Purpose
TBD - created by archiving change move-ltv-to-shared-card. Update Purpose after archive.
## Requirements
### Requirement: Shared card prints initial LTV once

The shared-input card SHALL render one read-only readout showing the initial loan-to-value ratio: loan amount divided by home value at purchase, formatted as a percent. It SHALL carry the label "Initial LTV".

The ratio SHALL be computed from the shared loan amount and home value inputs, never from any offer's computed result, so the readout holds a value whenever both shared inputs are valid, regardless of what any offer card contains.

The readout SHALL update on every input edit, together with the offer readouts.

#### Scenario: Readout shows the ratio

- **WHEN** home value is 450000 and loan amount is 400000
- **THEN** the shared card shows "Initial LTV" with the value 88.889%

#### Scenario: Readout survives an invalid offer

- **WHEN** both shared inputs are valid
- **AND** every offer card has its annual interest rate cleared, so no offer computes
- **THEN** the shared card still shows the initial LTV for the entered loan amount and home value

#### Scenario: Readout follows an edit

- **WHEN** the loan amount is changed
- **THEN** the initial LTV updates to the new ratio without a page reload

### Requirement: Readout states whether PMI applies

The readout SHALL append a tail naming whether the loan owes mortgage insurance: "PMI required" when the loan starts above 80% LTV, "no PMI required" otherwise.

The tail SHALL be derived from the same predicate that locks the per-offer PMI annual rate inputs, so the readout and the locked inputs can never disagree.

#### Scenario: Loan above the threshold

- **WHEN** home value is 450000 and loan amount is 400000, an initial LTV of 88.889%
- **THEN** the readout tail reads "PMI required"
- **AND** the PMI annual rate input on every offer card is editable

#### Scenario: Loan at or below the threshold

- **WHEN** home value is 500000 and loan amount is 400000, an initial LTV of 80%
- **THEN** the readout tail reads "no PMI required"
- **AND** the PMI annual rate input on every offer card is locked at 0

#### Scenario: Tail flips with the inputs

- **WHEN** the loan amount is raised so the ratio crosses above 80% of home value
- **THEN** the tail changes from "no PMI required" to "PMI required"
- **AND** the PMI annual rate inputs unlock in the same update

### Requirement: Readout is blank when the ratio cannot be computed

When home value is blank, zero, or not a number, or loan amount is blank or not a number, the readout SHALL show an em dash and SHALL show no PMI tail. It SHALL NOT show 0%, "no PMI required", or an error.

#### Scenario: Home value cleared

- **WHEN** the home value field is cleared
- **THEN** the initial LTV readout shows an em dash
- **AND** no PMI tail is shown

#### Scenario: Loan amount cleared

- **WHEN** the loan amount field is cleared
- **THEN** the initial LTV readout shows an em dash
- **AND** no PMI tail is shown

#### Scenario: No error on invalid input

- **WHEN** either shared input holds a value that is not a number
- **THEN** the readout shows an em dash
- **AND** no script error is raised

### Requirement: Readout is output, never input

The readout SHALL be a non-interactive element. It SHALL NOT be an `input` or `select`, SHALL NOT carry the `inp` class, and SHALL NOT be focusable or editable.

It SHALL NOT appear in the share hash, and a hash key naming it SHALL have no effect.

#### Scenario: Readout absent from a copied link

- **WHEN** the user activates the copy-link control
- **THEN** the hash contains no key for the initial LTV readout

#### Scenario: Readout cannot be typed into

- **WHEN** the reader clicks the readout value
- **THEN** no text cursor appears and the value cannot be edited

### Requirement: Per-offer readouts no longer repeat the ratio

Offer card readouts SHALL NOT include an "Initial LTV" row. The ratio derives from shared inputs alone, so every card printed the same figure.

Every other readout row SHALL remain unchanged in wording, order, and value.

#### Scenario: No LTV row on any card

- **WHEN** four offers are displayed with valid inputs
- **THEN** no offer card readout contains a row labelled "Initial LTV"

#### Scenario: Remaining rows unchanged

- **WHEN** the same inputs are entered before and after this change
- **THEN** each offer readout shows the same rows in the same order as before, minus the initial LTV row
- **AND** every remaining row shows the same value as before

