# term-glossary Specification

## Purpose
Which jargon terms the tool defines, how the definitions reach the reader (a footer glossary, hover text on labels, and a tap-to-open popover on readout rows), and the requirement that all of them come from one source so they cannot drift apart.
## Requirements
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

### Requirement: Hovering a term shows its definition
Input labels, readout row labels, and the shared card's initial LTV readout SHALL expose their glossary definition as native browser hover text via the `title` attribute. Hover text SHALL NOT replace the glossary; both SHALL be present.

The LTV definition SHALL reach the reader from the shared readout, since no offer readout row carries that term any more.

A readout row that is a section divider rather than a figure — "Through holding period" — resolves like any other row label and MAY therefore carry a definition. This is correct where the entry it resolves to names the divider's own subject, and SHALL NOT be suppressed with an exclusion list.

#### Scenario: Hover the shared LTV readout
- **WHEN** the pointer rests over the initial LTV readout in the shared card
- **THEN** the browser shows the initial LTV definition as hover text
- **AND** the text matches the glossary entry for initial LTV

#### Scenario: Hover a readout row label
- **WHEN** the pointer rests over the "Effective annual rate" row label in an offer readout
- **THEN** the browser shows the effective annual rate definition as hover text

#### Scenario: Hover an input label
- **WHEN** the pointer rests over the "PMI annual rate (%)" label
- **THEN** the browser shows the PMI definition as hover text

#### Scenario: Hover text on cloned offer cards
- **WHEN** the offer count is raised so Offer B, C, or D is rendered
- **THEN** the labels on the added cards carry the same hover definitions as Offer A's labels

#### Scenario: Existing select hover text is preserved
- **WHEN** the pointer rests over the PMI removal rule or PMI premium basis control, or over one of their options
- **THEN** the existing detailed hover text on those controls still appears, unchanged

#### Scenario: Specific term still beats the general one
- **WHEN** a label is resolved whose text also contains a more general term, such as "Total interest (to term)"
- **THEN** it resolves to the "Total interest" entry, not to the "Interest paid" entry that also matches on "interest"
- **AND** the shared readout resolves to "Initial LTV"

#### Scenario: A prose-only entry cannot capture a label
- **WHEN** a label containing "LTV" is resolved
- **THEN** it never resolves to the general "LTV (loan-to-value)" entry, which carries no match tokens
- **AND** that entry is still rendered in the glossary

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

### Requirement: Tapping a readout row label shows its definition

Readout row labels that carry a definition SHALL open that definition on click or tap. The shared card's initial LTV readout SHALL open its definition the same way, so touch readers keep tap-to-define for LTV after the per-offer row is removed. The definition SHALL be shown in a single shared element using the native HTML Popover API, so it renders in the top layer.

An open popover SHALL close on a click or tap anywhere on the page: outside it, on the popover itself, and on the label that opened it. A click on a different label carrying a definition SHALL replace the text rather than close. Escape SHALL still close an open popover. The popover SHALL carry no visible close control, and its appearance SHALL be unchanged.

The popover SHALL work on every offer card, including cards added after load, and SHALL survive the re-render that follows any input change. The shared readout SHALL keep its definition through every re-render of its value.

#### Scenario: Tap the shared LTV readout

- **WHEN** the reader taps the initial LTV readout in the shared card
- **THEN** a popover opens showing the initial LTV definition
- **AND** the definition text matches the glossary entry

#### Scenario: Shared readout keeps its definition after an edit

- **WHEN** the reader changes the loan amount, causing the readout value to update
- **AND** the reader then taps the readout
- **THEN** the popover still opens with the initial LTV definition

#### Scenario: Tap a readout row label

- **WHEN** the reader taps the "Total interest (to term)" row label in an offer readout
- **THEN** a popover opens showing the total interest definition
- **AND** the definition text matches the glossary entry for total interest

#### Scenario: Tap a row label on an added offer card

- **WHEN** the offer count is raised so Offer B, C, or D is rendered
- **AND** the reader taps a readout row label on the added card
- **THEN** the popover opens with that row's definition

#### Scenario: Popover survives re-render

- **WHEN** the reader edits any input, causing the readouts to re-render
- **AND** the reader then taps a readout row label
- **THEN** the popover still opens with that row's definition

#### Scenario: Tap a second label while one is open

- **WHEN** a popover is open for one row label
- **AND** the reader taps a different row label
- **THEN** the popover shows the second row's definition

#### Scenario: Dismiss by tapping away

- **WHEN** a popover is open
- **AND** the reader taps outside it
- **THEN** the popover closes

#### Scenario: Dismiss by tapping the popover

- **WHEN** a popover is open
- **AND** the reader taps the popover text itself
- **THEN** the popover closes

#### Scenario: Dismiss by tapping the label that opened it

- **WHEN** a popover is open for a row label
- **AND** the reader taps that same row label again
- **THEN** the popover closes
- **AND** it does not reopen

#### Scenario: Dismiss with Escape

- **WHEN** a popover is open
- **AND** the reader presses Escape
- **THEN** the popover closes

#### Scenario: Popover shows no close control

- **WHEN** a popover is open
- **THEN** it renders the definition text only
- **AND** no close button, icon, or dismissal instruction is added

#### Scenario: Row label with no definition

- **WHEN** the reader taps a readout row label that has no glossary match
- **THEN** no popover opens
- **AND** no error is raised

### Requirement: Definition access adds no visible marker

The tap-to-open path SHALL add no visible affordance to any label — no underline, no icon, no colour change, no cursor change, no change to spacing or alignment. Rendered output SHALL be pixel-identical to the version before this change until a popover is opened.

#### Scenario: Readout row unchanged at rest

- **WHEN** a readout row carries a definition
- **THEN** the row renders exactly as before: label left-aligned, value right-aligned, same line, same weight and colour
- **AND** no marker, icon, or underline is present

#### Scenario: Desktop appearance unchanged

- **WHEN** the page is viewed on a pointer device
- **THEN** the layout and styling are identical to the version before this change

### Requirement: Popover text comes from the single definition source

Popover text SHALL be derived from the same definition source as the glossary and the hover text. No third copy of any definition SHALL exist in the file.

#### Scenario: Definition edited once

- **WHEN** a definition's wording is changed in the footer glossary
- **THEN** the glossary entry, the hover text, and the popover text all show the new wording

### Requirement: Popover degrades where the API is absent

Where the browser does not support the Popover API, the page SHALL continue to work: hover text and the footer glossary SHALL remain available, and tapping a row label SHALL raise no error.

#### Scenario: Browser without Popover API

- **WHEN** the page is opened in a browser that does not support `showPopover`
- **AND** the reader taps a readout row label
- **THEN** no error is raised
- **AND** the footer glossary still renders every term and definition

### Requirement: Comparison table labels carry definitions

Component and total row labels in the cost comparison table SHALL expose their glossary definition
the way readout row labels do: as native `title` hover text, and as the shared popover on click or
tap. Definitions SHALL come from the same single source as the glossary and the readout rows, so no
third copy of any definition text exists.

Labels SHALL keep their definitions through the re-render that follows any input edit, and through
the change of wording when the holding-period input is set or cleared.

#### Scenario: Hover a table row label

- **WHEN** the pointer rests over the "Remaining balance" label in the comparison table
- **THEN** the browser shows the remaining balance definition as hover text
- **AND** the text matches the glossary entry

#### Scenario: Tap a table row label

- **WHEN** the reader taps the "Cost to walk away (incl. fees + PMI)" label in the comparison table
- **THEN** the popover opens showing the cost to walk away definition

#### Scenario: Definitions survive re-render

- **WHEN** the reader edits any input, causing the table to re-render
- **AND** the reader then taps a table row label
- **THEN** the popover still opens with that label's definition

#### Scenario: Definitions follow the mode flip

- **WHEN** the holding-period field is cleared and the rows change to their to-term wording
- **THEN** the new labels carry the definitions for the terms they now name

#### Scenario: Table label with no definition

- **WHEN** the reader taps a table label that has no glossary match
- **THEN** no popover opens
- **AND** no error is raised

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
