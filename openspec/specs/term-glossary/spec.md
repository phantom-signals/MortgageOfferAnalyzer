# term-glossary Specification

## Purpose
Which jargon terms the tool defines, where the definitions live (a footer glossary plus hover text on labels), and the requirement that both come from one source so they cannot drift apart.

## Requirements
### Requirement: Page carries a glossary of every term it prints
The tool SHALL render a glossary at the bottom of the page listing each jargon term it uses as an input label or a readout row label, paired with a one-sentence plain-language definition. Every abbreviation SHALL be expanded in its own entry.

The glossary SHALL cover at minimum: PMI, LTV, principal, effective annual rate, term, payments per year, upfront fees and points, amortization, amortization midpoint, holding period, home value at purchase (original value), PMI removal rule, PMI premium basis, HPA, total interest, total cost, remaining balance, cost to walk away, payment (P&I), escrow, MIP.

#### Scenario: Glossary present on load
- **WHEN** the file is opened in a browser
- **THEN** a glossary section is rendered at the bottom of the page, below the existing method and PMI footer paragraphs
- **AND** each entry shows a term and its definition

#### Scenario: Every printed label is defined
- **WHEN** the glossary is compared against the labels the tool renders
- **THEN** each shared-input label, each offer-input label, and each readout row label maps to a glossary entry
- **AND** no glossary entry is orphaned — every entry corresponds to a term the tool actually uses

#### Scenario: Abbreviation expanded
- **WHEN** the reader looks up PMI, LTV, EAR, HPA, or MIP
- **THEN** the entry gives the full expansion before the definition

#### Scenario: Glossary survives without JavaScript
- **WHEN** the file is viewed with JavaScript disabled
- **THEN** the glossary still renders with all terms and definitions

### Requirement: Hovering a term shows its definition
Input labels and readout row labels SHALL expose their glossary definition as native browser hover text via the `title` attribute. Hover text SHALL NOT replace the glossary; both SHALL be present.

#### Scenario: Hover a readout row label
- **WHEN** the pointer rests over the "Initial LTV" row label in an offer readout
- **THEN** the browser shows the LTV definition as hover text

#### Scenario: Hover an input label
- **WHEN** the pointer rests over the "PMI annual rate (%)" label
- **THEN** the browser shows the PMI definition as hover text

#### Scenario: Hover text on cloned offer cards
- **WHEN** the offer count is raised so Offer B, C, or D is rendered
- **THEN** the labels on the added cards carry the same hover definitions as Offer A's labels

#### Scenario: Existing select hover text is preserved
- **WHEN** the pointer rests over the PMI removal rule or PMI premium basis control, or over one of their options
- **THEN** the existing detailed hover text on those controls still appears, unchanged

### Requirement: Definitions have a single source
Glossary text and hover text SHALL be derived from one definition source in the file. Editing a definition once SHALL change both the glossary entry and every hover tooltip for that term.

#### Scenario: Definition edited once
- **WHEN** a definition's wording is changed in the source
- **THEN** the glossary entry and every hover tooltip for that term both show the new wording
- **AND** no second copy of the text exists in the file

### Requirement: Adding definitions changes no computed value
The glossary and hover text SHALL be presentation only. No input, control, calculation, or rendered figure SHALL change.

#### Scenario: Results identical before and after
- **WHEN** the same inputs are entered before and after this change
- **THEN** the payment, effective annual rate, LTV, PMI figures, total cost, holding-period figures, and verdict are identical

#### Scenario: Readout row layout unchanged
- **WHEN** a readout row carries hover text
- **THEN** the row still renders its label left-aligned and its value right-aligned on the same line
- **AND** no visible marker is added that shifts the row's layout
