## MODIFIED Requirements

### Requirement: Single offer is the default analysis mode
With exactly one offer, the tool SHALL present itself as an analyzer of that offer and SHALL NOT present comparison output.

#### Scenario: Verdict hidden at count 1
- **WHEN** the offer count is 1
- **THEN** the verdict bar is not displayed
- **AND** the single offer's readout still shows payment, effective annual rate, total interest, PMI figures, and total cost
- **AND** the initial LTV is not among them; it is shown once in the shared-input card

#### Scenario: Holding period at count 1
- **WHEN** the offer count is 1 and a holding period is entered
- **THEN** the single card's readout includes the through-holding-period rows (payments made, interest paid, PMI paid, remaining balance, cost to walk away)

#### Scenario: Verdict returns above count 1
- **WHEN** the offer count is raised from 1 to 2
- **THEN** the verdict bar is displayed
- **AND** it compares the two offers on the same basis used today (full-term total cost, or cost to clear when a holding period is set)

