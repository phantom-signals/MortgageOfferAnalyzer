## MODIFIED Requirements

### Requirement: Readout states whether PMI applies

The readout SHALL append a tail naming whether the loan owes mortgage insurance: "PMI required" when the loan starts above 80% LTV, "no PMI required" otherwise. The tail SHALL follow the percentage after one space, enclosed in parentheses, with no em dash.

The tail SHALL be derived from the same predicate that locks the per-offer PMI annual rate inputs, so the readout and the locked inputs can never disagree.

#### Scenario: Loan above the threshold

- **WHEN** home value is 450000 and loan amount is 400000, an initial LTV of 88.889%
- **THEN** the readout reads "88.889% (PMI required)"
- **AND** the PMI annual rate input on every offer card is editable

#### Scenario: Loan at or below the threshold

- **WHEN** home value is 500000 and loan amount is 400000, an initial LTV of 80%
- **THEN** the readout reads "80.00% (no PMI required)"
- **AND** the PMI annual rate input on every offer card is locked at 0

#### Scenario: Tail flips with the inputs

- **WHEN** the loan amount is raised so the ratio crosses above 80% of home value
- **THEN** the tail changes from "no PMI required" to "PMI required"
- **AND** the PMI annual rate inputs unlock in the same update
