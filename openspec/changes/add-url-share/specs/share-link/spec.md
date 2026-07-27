## ADDED Requirements

### Requirement: Entered state serializes into the URL hash
The tool SHALL encode the current value of every input control — the shared fields (offer count, loan amount, holding period, home value, PMI removal rule, PMI premium basis) and every displayed offer's fields (rate, term, payments per year, fees, PMI rate) — as URL-encoded key/value pairs in `location.hash`, keyed by each control's element id. Computed output SHALL NOT be encoded.

#### Scenario: Hash contains every displayed field
- **WHEN** three offers are displayed with values entered and the user activates the copy-link control
- **THEN** the hash contains a key/value pair for each shared field and for `rate0` through `pmi2`
- **AND** it contains no pair for cards that are not displayed
- **AND** it contains no pair for readout, verdict, or glossary elements

#### Scenario: Values survive encoding
- **WHEN** a field holds a value needing escaping in a URL
- **THEN** the value is percent-encoded in the hash
- **AND** decoding it returns the original string exactly

### Requirement: A link restores the state it encodes
On load, when `location.hash` carries encoded state, the tool SHALL apply those values to the matching controls before the first computation, and SHALL then render and compute exactly as if the values had been typed.

#### Scenario: Round trip
- **WHEN** a link produced from a given set of inputs is opened in a fresh page load
- **THEN** every input control reads the value it held when the link was produced
- **AND** every readout and the verdict show the same figures as before

#### Scenario: Offer cards exist before their fields are assigned
- **WHEN** a link encoding four offers is opened
- **THEN** four offer cards are rendered
- **AND** each card's rate, term, payments per year, fees, and PMI rate hold the encoded values, not the card-A defaults

#### Scenario: No hash
- **WHEN** the file is opened with no hash
- **THEN** the tool loads with its existing default values and one offer card, unchanged from today

### Requirement: Malformed or unknown hash content is ignored, never executed
The tool SHALL treat hash content as untrusted input. It SHALL assign a value only when the key names an existing input control, SHALL insert no hash-derived content as markup, and SHALL leave the page fully usable when the hash is unparseable.

#### Scenario: Unknown key
- **WHEN** a hash contains a key that matches no input control
- **THEN** the key is ignored
- **AND** all other keys in that hash still restore
- **AND** no error surfaces to the user

#### Scenario: Key naming a non-input element
- **WHEN** a hash contains a key naming a page element that is not an input control, such as the verdict or glossary container
- **THEN** no write to that element occurs

#### Scenario: Garbage hash
- **WHEN** a hash contains arbitrary text that is not encoded state
- **THEN** the page loads with default values
- **AND** inputs, computation, and the verdict work normally

#### Scenario: Out-of-range or non-numeric value
- **WHEN** a hash encodes a negative, zero, or non-numeric value for a numeric field
- **THEN** the existing input and calculation guards apply unchanged
- **AND** that offer's readout renders as it does today for invalid input, with no crash and no effect on the other offers

### Requirement: Self-test invocation takes precedence over restore
The `#selftest` hash SHALL continue to run the self-check exactly as it does today, and SHALL NOT be interpreted as encoded state. A hash carrying encoded state SHALL NOT run the self-check.

#### Scenario: Self-test hash
- **WHEN** the file is opened with `#selftest`
- **THEN** the self-check runs
- **AND** the page title becomes `selftest passed`, or `SELFTEST FAILED: <reason>` on failure
- **AND** no restore is attempted

#### Scenario: State hash
- **WHEN** the file is opened with a hash carrying encoded state
- **THEN** the state restores
- **AND** the self-check does not run
- **AND** the page title is unchanged

### Requirement: Copy-link control publishes the current state
The tool SHALL provide a control that writes the current state into `location.hash` and copies the resulting full URL to the clipboard, reporting the outcome to the user. When the clipboard write is unavailable or rejected, the hash SHALL still be set so the link remains recoverable from the address bar. The page SHALL state next to that control that the link embeds the entered figures, since the tool is used as a hosted page where no repository documentation is visible.

#### Scenario: Copy succeeds
- **WHEN** the user activates the copy-link control
- **THEN** the address bar hash holds the current state
- **AND** the clipboard holds the full URL
- **AND** the control briefly confirms the copy

#### Scenario: Clipboard unavailable
- **WHEN** the clipboard write rejects, as it can on a `file://` origin
- **THEN** the address bar hash still holds the current state
- **AND** the control reports that the link is in the address bar
- **AND** no error dialog or console-only failure leaves the user without feedback

#### Scenario: Link content is disclosed in the page
- **WHEN** the copy-link control is displayed
- **THEN** adjacent text in the page states that the link embeds the entered figures
- **AND** that text is visible without hovering, opening a dialog, or reading any file outside the page

#### Scenario: State changes after copying
- **WHEN** the user edits a field after copying a link
- **THEN** the previously copied link still encodes the earlier state
- **AND** activating the control again produces a link encoding the current state

### Requirement: Self-check covers the round trip
The file's `#selftest` self-check SHALL assert that serializing the current state and restoring it from that string reproduces every input value and the same computed readout.

#### Scenario: Round-trip assertion
- **WHEN** the self-check runs
- **THEN** it serializes a known multi-offer state, changes every field, restores from the serialized string, and asserts each input and the resulting total-cost readout match the originals
- **AND** it performs this without writing to `location.hash`
- **AND** it restores the page to its pre-test state when finished
