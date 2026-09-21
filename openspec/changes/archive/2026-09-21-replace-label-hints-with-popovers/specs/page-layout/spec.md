## REMOVED Requirements

### Requirement: Label hints sit in parentheses

**Reason**: Input-label and section-label hints are removed; their text now reaches the reader through the definition popover. The em-dash rule and unit-label rule it carried move to the two requirements added below.
**Migration**: Hint text moves into the matching glossary definition. See "Labels carry no hints" and "Visible text avoids em dash separators".

## ADDED Requirements

### Requirement: Visible text avoids em dash separators

Visible text SHALL NOT use an em dash as a separator between a label and a parenthetical, or within
a sentence. Sentences, such as the share-link hint, the `noscript` notice, and glossary definitions,
SHALL use colons, commas, or parentheses where an em dash stood. A lone em dash that stands for an
empty value, such as a blank readout or verdict, SHALL remain.

#### Scenario: No em dash in a label

- **WHEN** any input label, readout row label, or section heading renders
- **THEN** it contains no em dash

#### Scenario: Empty placeholder kept

- **WHEN** fewer than two offers compute
- **THEN** the verdict headline and amount each show a lone em dash

### Requirement: Labels carry no hints

Input labels and section headings SHALL carry no explanatory hint text. An explanation a label needs
SHALL live in its glossary definition, which reaches the reader through hover text and the
definition popover. A label MAY end in a parenthesized unit, such as "PMI annual rate (%)" or
"Holding period (years)". Readout and table row labels MAY keep a parenthetical that qualifies the
figure, such as "(first period)" or "(incl. fees + PMI)".

#### Scenario: Home value label

- **WHEN** the shared-input card renders
- **THEN** the home value label reads "Home value at purchase"

#### Scenario: Holding period label

- **WHEN** the shared-input card renders
- **THEN** the holding period label reads "Holding period (years)"

#### Scenario: Section headings

- **WHEN** the cost comparison and cost-over-time sections render
- **THEN** their headings read "Cost to walk away" (or "Cost to term") and "Cost over time", with no parenthetical after either

#### Scenario: Unit label

- **WHEN** an offer card renders
- **THEN** the PMI rate label reads "PMI annual rate (%)" with no hint and no colon

### Requirement: Wrapped labels break before a parenthetical

Where an input label, readout row label, comparison table total label, or glossary term ends in a
parenthetical and does not fit on one line, the line SHALL break before the opening "(", so the
parenthetical starts a line. A parenthetical wider than its container SHALL wrap within itself
rather than overflow. Labels that fit on one line SHALL render unchanged. The label's text content
SHALL be unchanged, so definition lookup and hover text are unaffected.

#### Scenario: Readout row at phone width

- **WHEN** an offer readout renders in a 320px-wide viewport
- **THEN** the "Payment incl. PMI (first period)" label breaks as "Payment incl. PMI" then "(first period)"
- **AND** the "Total cost (incl. fees + PMI)" label wraps with its second line starting "("

#### Scenario: Table total at phone width

- **WHEN** the comparison table renders in a 320px-wide viewport with a holding period set
- **THEN** the "Cost to walk away (incl. fees + PMI)" label, if it wraps, breaks before "("

#### Scenario: Label fits

- **WHEN** a label with a parenthetical fits its container on one line
- **THEN** it renders on one line

#### Scenario: Definition lookup unchanged

- **WHEN** a row label's parenthetical is wrapped for line breaking
- **THEN** the label carries the same hover definition it carried before
