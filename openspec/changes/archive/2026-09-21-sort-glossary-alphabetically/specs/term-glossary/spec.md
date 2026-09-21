## ADDED Requirements

### Requirement: Glossary entries are alphabetical
Glossary entries SHALL render in alphabetical order of their term text, compared case-insensitively, so reader can find a term by scanning. Order SHALL be fixed in markup, not applied by script, so it holds with JavaScript disabled. Reordering SHALL NOT change any term or definition wording.

#### Scenario: Entries sorted on load
- **WHEN** the glossary section is expanded
- **THEN** each term sorts at or after the term above it, compared case-insensitively
- **AND** "Amortization" appears before "Amortization midpoint" and "Upfront fees and points" appears last

#### Scenario: Sorted without JavaScript
- **WHEN** the file is viewed with JavaScript disabled and the glossary is expanded
- **THEN** entries appear in the same alphabetical order

### Requirement: Label resolution does not depend on entry order
When a label contains match tokens from more than one entry, it SHALL resolve to the entry whose matching token is longest. Entry position in the glossary SHALL NOT decide which definition a label receives, except to break a tie between equal-length matching tokens.

#### Scenario: Specific entry wins though it sorts later
- **WHEN** "Total interest (to term)" is resolved while "Interest paid" sorts before "Total interest"
- **THEN** it resolves to the "Total interest" entry

#### Scenario: Specific PMI entry wins over general PMI
- **WHEN** "PMI annual rate (%)" is resolved while "PMI (private mortgage insurance)" sorts before "PMI annual rate"
- **THEN** it resolves to the "PMI annual rate" entry

#### Scenario: Hover text unchanged by reorder
- **WHEN** every input label, readout row label, and shared readout is resolved before and after the reorder
- **THEN** each receives the same definition text as before

### Requirement: Header points reader to definitions
The header SHALL carry a line under the subtitle reading "Click on any term to see its definition, or check the glossary.", with "glossary" a link to the footer glossary. Following the link SHALL open the glossary's fold and scroll to it without changing the URL hash, since the hash holds share state.

#### Scenario: Line present on load
- **WHEN** the file is opened in a browser
- **THEN** the header shows the definitions line below the subtitle

#### Scenario: Glossary link opens fold
- **WHEN** the reader follows the glossary link while the glossary fold is closed
- **THEN** the glossary fold opens and scrolls into view
- **AND** the URL hash is unchanged
