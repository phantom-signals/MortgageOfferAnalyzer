# term-glossary Specification

## Purpose
Which jargon terms the tool defines, how the definitions reach the reader (a footer glossary, hover text on labels, and a tap-to-open popover on readout rows), and the requirement that all of them come from one source so they cannot drift apart.

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

### Requirement: Tapping a readout row label shows its definition

Readout row labels that carry a definition SHALL open that definition on click or tap. The definition SHALL be shown in a single shared element using the native HTML Popover API, so it renders in the top layer, dismisses on outside click, and dismisses on Escape without custom code.

The popover SHALL work on every offer card, including cards added after load, and SHALL survive the re-render that follows any input change.

#### Scenario: Tap a readout row label

- **WHEN** the reader taps the "Initial LTV" row label in an offer readout
- **THEN** a popover opens showing the LTV definition
- **AND** the definition text matches the glossary entry for LTV

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

#### Scenario: Row label with no definition

- **WHEN** the reader taps a readout row label that has no glossary match
- **THEN** no popover opens
- **AND** no error is raised

### Requirement: Input labels keep their native control behaviour

Input labels SHALL NOT open the definition popover. Clicking or tapping an input label SHALL continue to focus its associated control, unchanged. Input labels SHALL keep their `title` hover text.

#### Scenario: Tap an input label

- **WHEN** the reader taps the "PMI annual rate (%)" label
- **THEN** the PMI input receives focus
- **AND** no definition popover opens

#### Scenario: Input label hover text preserved

- **WHEN** the pointer rests over an input label on a pointer device
- **THEN** the browser still shows the definition as native hover text

### Requirement: Definition access adds no visible marker

The tap-to-open path SHALL add no visible affordance to any label — no underline, no icon, no colour change, no cursor change, no change to spacing or alignment. Rendered output SHALL be pixel-identical to the version before this change until a popover is opened.

#### Scenario: Readout row unchanged at rest

- **WHEN** a readout row carries a definition
- **THEN** the row renders exactly as before: label left-aligned, value right-aligned, same line, same weight and colour
- **AND** no marker, icon, or underline is present

#### Scenario: Desktop appearance unchanged

- **WHEN** the page is viewed on a pointer device
- **THEN** the layout and styling are identical to the version before this change

### Requirement: Touch pointers get one hint

The page SHALL carry one short sentence telling touch readers that row labels are tappable. It SHALL appear only where the primary pointer cannot hover, SHALL sit inside the existing intro paragraph rather than in a section of its own, and SHALL be static text — no dismissal control, no first-run logic, no stored state.

#### Scenario: Hint shown on a touch device

- **WHEN** the page is opened on a device whose primary pointer cannot hover
- **THEN** the intro prose includes a sentence pointing at tappable row labels

#### Scenario: Hint hidden on a pointer device

- **WHEN** the page is opened on a device with a hovering pointer
- **THEN** the hint sentence is not rendered visibly
- **AND** the intro prose reads exactly as it did before this change

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
