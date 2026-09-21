## MODIFIED Requirements

### Requirement: Section follows the holding-period input

Heading, section hint, total row label, and table figures SHALL follow the shared holding-period
input. The section hint SHALL define the headline figure in parentheses after the heading, taking its
text from the lead clause of the glossary entry for that figure (the text before its first colon),
so no second copy of the definition exists. The component breakdown after the colon SHALL NOT
appear in the hint, since the table below lists those components.

Component row labels SHALL be bare nouns naming the component. The row sits under a heading that
already names the period, so the card readout's "... paid" phrasing would repeat it once per row;
the table and the card therefore label the same figure differently by design.

With a holding period entered, the heading SHALL read "Cost to walk away", the total row SHALL read
"Cost to walk away (incl. fees + PMI)", and component rows SHALL read "Interest", "PMI", "Upfront
fees", "Remaining balance", and "Principal", each measured through that period.

With the holding period blank, the heading SHALL read "Cost to term", the total row SHALL read
"Total cost (to term, incl. fees + PMI)", and component rows SHALL read "Total interest", "Total
PMI", "Upfront fees", and "Principal" — remaining balance being zero at term. Only the two rows
that would otherwise be ambiguous across the two modes take a distinct to-term label.

#### Scenario: Holding period entered

- **WHEN** the holding period is set to 8 years
- **THEN** the section heading reads "Cost to walk away"
- **AND** the section hint reads "what the loan costs if you leave at the end of the holding period"
- **AND** the total row label reads "Cost to walk away (incl. fees + PMI)"
- **AND** the interest row is labelled "Interest", not "Interest paid"
- **AND** the remaining balance row is present

#### Scenario: Holding period cleared

- **WHEN** the holding-period field is cleared
- **THEN** the section heading reads "Cost to term"
- **AND** the section hint reads "what the loan costs to full term"
- **AND** the total row label reads "Total cost (to term, incl. fees + PMI)"
- **AND** the interest row is labelled "Total interest"
- **AND** the remaining balance row is not rendered
