## MODIFIED Requirements

### Requirement: Page carries a glossary of every term it prints
The tool SHALL render a glossary at the bottom of the page listing each jargon term it uses as an input label or a readout row label, paired with a one-sentence plain-language definition. Every abbreviation SHALL be expanded in its own entry. The glossary SHALL be titled "Glossary" and SHALL sit inside a footer disclosure section that is closed on load, placed below the license line and above the "Privacy and Terms of Use" section. Definitions SHALL NOT use em dashes; asides SHALL use colons, commas, or parentheses.

The glossary SHALL cover at minimum: PMI, LTV, principal, effective annual rate, term, payments per year, upfront fees and points, amortization, amortization midpoint, holding period, home value at purchase (original value), PMI removal rule, PMI premium basis, HPA, total interest, total cost, remaining balance, cost to walk away, payment (P&I), escrow, MIP.

An entry SHALL carry label-match tokens only where the tool prints a label that should resolve to it. An entry that exists to explain a term the page uses in its prose rather than in a label — LTV on its own, "offer", HPA, escrow, MIP — SHALL carry none, so it cannot capture a label meant for a more specific entry. A token-free entry is not an orphan.

#### Scenario: Glossary present on load
- **WHEN** the file is opened in a browser
- **THEN** a collapsed section titled "Glossary" is rendered in the footer, below the license line and above the "Privacy and Terms of Use" section
- **AND** expanding it shows each entry with a term and its definition

#### Scenario: Every printed label is defined
- **WHEN** the glossary is compared against the labels the tool renders
- **THEN** each shared-input label, each offer-input label, and each readout row label maps to a glossary entry
- **AND** no glossary entry is orphaned — every entry corresponds to a term the tool actually uses

#### Scenario: Abbreviation expanded
- **WHEN** the reader looks up PMI, LTV, EAR, HPA, or MIP
- **THEN** the entry gives the full expansion before the definition

#### Scenario: No em dash in definitions
- **WHEN** the glossary definitions are read
- **THEN** none contains an em dash

#### Scenario: Glossary survives without JavaScript
- **WHEN** the file is viewed with JavaScript disabled
- **THEN** the glossary section still expands to show all terms and definitions

## ADDED Requirements

### Requirement: Definitions reach the reader while the glossary is closed
Hover text on labels and the tap-to-open definition popover SHALL work identically whether the glossary section is open or closed. Opening a definition SHALL NOT open the glossary section.

#### Scenario: Popover with glossary closed
- **WHEN** the glossary section is closed and the reader taps a readout row label
- **THEN** the popover shows that label's glossary definition
- **AND** the glossary section stays closed

#### Scenario: Hover with glossary closed
- **WHEN** the glossary section is closed and the pointer rests over an input label
- **THEN** the browser shows that label's glossary definition as hover text

### Requirement: Tapping an input label shows its definition
Where the Popover API is supported, clicking or tapping an input label that carries a definition SHALL open the definition popover with that label's glossary definition, and SHALL NOT move focus to the associated control, so a touch keyboard does not open over the popover. The reader focuses the control by tapping the control itself. The popover SHALL dismiss the same way as for readout row labels: any click or tap, including a re-tap on the same label, Escape, or scroll. An input label with no definition SHALL keep native label behaviour. Where the Popover API is absent, input labels SHALL keep native label behaviour. Input labels SHALL keep their `title` hover text and SHALL gain no visible marker.

#### Scenario: Tap an input label
- **WHEN** the reader taps the "Annual interest rate (%)" label on an offer card
- **THEN** the definition popover opens with that label's glossary definition
- **AND** the rate input does not receive focus

#### Scenario: Re-tap closes
- **WHEN** the popover is open from an input label and the reader taps the same label again
- **THEN** the popover closes

#### Scenario: Control still takes focus
- **WHEN** the reader taps the rate input box itself
- **THEN** the input receives focus
- **AND** any open popover closes

#### Scenario: No Popover API
- **WHEN** the browser does not support `showPopover` and the reader taps an input label
- **THEN** the associated control receives focus, as native labels do
- **AND** no error is raised

## REMOVED Requirements

### Requirement: Input labels keep their native control behaviour
**Reason**: Input labels now open the definition popover; covered by "Tapping an input label shows its definition".
**Migration**: Tap the input box itself to focus it.

### Requirement: Touch pointers get one hint
**Reason**: Owner removed the touch hint sentence from the header; tap-to-define is an unannounced feature.
**Migration**: None. Hover text and the footer glossary still expose every definition.
