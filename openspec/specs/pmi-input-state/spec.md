# pmi-input-state Specification

## Purpose
When the PMI rate input is editable and when it is forced to 0 and disabled, how a previously entered value is preserved and restored, how a locked field looks and behaves, and the rule that locking never changes a computed figure.

## Requirements
### Requirement: PMI rate input is locked when no PMI is owed
Each offer card's PMI annual rate input SHALL be set to 0 and disabled whenever the shared inputs give an initial LTV at or below 80%, because the tool charges no PMI in that case. The lock condition SHALL be the same test `calc()` already uses to decide whether PMI is required: PMI is owed only when a valid home value and loan amount give loan divided by home value strictly greater than 80%.

#### Scenario: Loan starts at 80% LTV
- **WHEN** the loan amount is 360000 and the home value at purchase is 450000 (LTV exactly 80%)
- **THEN** every offer card's PMI annual rate input reads 0
- **AND** every offer card's PMI annual rate input is disabled

#### Scenario: Loan starts below 80% LTV
- **WHEN** the loan amount is 300000 and the home value at purchase is 450000 (LTV 66.7%)
- **THEN** every offer card's PMI annual rate input reads 0 and is disabled

#### Scenario: Loan starts above 80% LTV
- **WHEN** the loan amount is 400000 and the home value at purchase is 450000 (LTV 88.9%)
- **THEN** every offer card's PMI annual rate input is enabled and editable
- **AND** it holds its entered or default value

#### Scenario: Home value missing or zero
- **WHEN** the home value at purchase is blank, zero, or not a number
- **THEN** the PMI annual rate input is 0 and disabled, matching the readout, which already shows PMI as none because LTV cannot be assessed

#### Scenario: Loan amount not yet valid
- **WHEN** the loan amount is blank or not a number
- **THEN** the PMI annual rate input is 0 and disabled
- **AND** entering a valid loan amount above 80% LTV re-enables it in the same edit session

### Requirement: A locked value is preserved and restored
Locking SHALL stash the value the user had entered. Unlocking SHALL restore that stashed value, per offer card, so the lock never destroys typed input.

#### Scenario: Value returns after unlock
- **WHEN** Offer A's PMI rate is 0.72, then the loan amount is lowered so LTV falls to 75%, then raised again so LTV returns to 88.9%
- **THEN** Offer A's PMI rate reads 0.72 again
- **AND** the readout's PMI figures match what they were before the lock

#### Scenario: Per-card stash
- **WHEN** the offer count is 3 with PMI rates 0.55, 0.72, and 0.40, and the inputs are locked and then unlocked
- **THEN** each card restores its own value: 0.55, 0.72, and 0.40 respectively

#### Scenario: No stash on first load in locked state
- **WHEN** the file is opened with shared inputs that give LTV at or below 80% and the PMI input is never enabled
- **THEN** the PMI input reads 0
- **AND** unlocking restores the card's default PMI rate rather than a blank value

### Requirement: Locked input is visibly non-editable
A locked PMI input SHALL read as unavailable rather than merely empty: grayed background, muted text, and a `not-allowed` cursor, in both the light and dark color schemes. The reason SHALL be available to the reader.

#### Scenario: Locked appearance
- **WHEN** the PMI input is locked
- **THEN** it renders with a grayed background and muted text distinguishable from an enabled empty input
- **AND** hovering it shows text stating that PMI does not apply at or below 80% LTV

#### Scenario: Dark scheme
- **WHEN** the browser reports a dark color scheme and the PMI input is locked
- **THEN** the grayed styling still reads as disabled against the dark card background

#### Scenario: Keyboard traversal
- **WHEN** the user tabs through an offer card whose PMI input is locked
- **THEN** focus skips the locked input
- **AND** the field's label remains visible and readable

### Requirement: Locking changes no computed figure
The lock SHALL only mirror a decision `calc()` already makes. No payment, effective annual rate, LTV, PMI total, total cost, holding-period figure, or verdict SHALL differ from what the tool prints today for the same shared and offer inputs.

#### Scenario: Results identical at LTV above 80%
- **WHEN** the loan amount is 400000, the home value is 450000, and Offer A holds its default inputs
- **THEN** the payment, total interest, total PMI, PMI end period, and total cost equal the values the tool prints today

#### Scenario: Results identical at LTV at or below 80%
- **WHEN** the LTV is at or below 80% and the PMI input is locked to 0
- **THEN** the readout shows PMI as none, exactly as it does today when a nonzero PMI rate is entered at the same LTV
- **AND** the total cost is unchanged by the lock
