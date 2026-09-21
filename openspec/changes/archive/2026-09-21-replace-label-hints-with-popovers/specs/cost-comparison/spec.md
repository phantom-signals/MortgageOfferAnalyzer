## MODIFIED Requirements

### Requirement: Section follows the holding-period input

Heading, heading definition, total row label, and table figures SHALL follow the shared
holding-period input. The heading SHALL carry no parenthetical hint. Instead the heading SHALL expose
the glossary definition of the headline figure as `title` hover text and in the shared definition
popover, taken from the glossary entry so no second copy of the definition exists. The heading's
definition SHALL change with the heading wording.

Component row labels SHALL be bare nouns naming the component. The row sits under a heading that
already names the period, so the card readout's "... paid" phrasing would repeat it once per row;
the table and the card therefore label the same figure differently by design.

With a holding period entered, the heading SHALL read "Cost to walk away" and carry the cost to walk
away definition, the total row SHALL read "Cost to walk away (incl. fees + PMI)", and component rows
SHALL read "Interest", "PMI", "Upfront fees", "Remaining balance", and "Principal", each measured
through that period.

With the holding period blank, the heading SHALL read "Cost to term" and carry the total cost
definition, not the term definition, the total row SHALL read "Total cost (incl. fees +
PMI)", and component rows SHALL read "Total interest", "Total PMI", "Upfront fees", and "Principal",
remaining balance being zero at term. Only the two rows that would otherwise be ambiguous across the
two modes take a distinct to-term label.

#### Scenario: Holding period entered

- **WHEN** the holding period is set to 8 years
- **THEN** the section heading reads "Cost to walk away" with no parenthetical after it
- **AND** the heading's hover text is the glossary definition for cost to walk away
- **AND** the total row label reads "Cost to walk away (incl. fees + PMI)"
- **AND** the interest row is labelled "Interest", not "Interest paid"
- **AND** the remaining balance row is present

#### Scenario: Holding period cleared

- **WHEN** the holding-period field is cleared
- **THEN** the section heading reads "Cost to term" with no parenthetical after it
- **AND** the heading's hover text is the glossary definition for total cost
- **AND** the total row label reads "Total cost (incl. fees + PMI)"
- **AND** the interest row is labelled "Total interest"
- **AND** the remaining balance row is not rendered

#### Scenario: Heading definition follows a second flip

- **WHEN** the holding-period field is cleared and then set to 8 years again
- **THEN** the heading's hover text is the glossary definition for cost to walk away
