## MODIFIED Requirements

### Requirement: Entered state serializes into the URL hash
The tool SHALL encode the current value of every input control — the shared fields (loan amount,
holding period, home value, PMI removal rule, PMI premium basis) and every displayed offer's fields
(rate, term, payments per year, fees, PMI rate) — as URL-encoded key/value pairs in `location.hash`,
keyed by each control's element id. Offer count SHALL NOT be encoded as a field of its own; the
displayed offers' own keys carry it. Computed output and fold state SHALL NOT be encoded.

#### Scenario: Hash contains every displayed field
- **WHEN** three offers are displayed with values entered and the user activates the copy-link control
- **THEN** the hash contains a key/value pair for each shared field and for `rate0` through `pmi2`
- **AND** it contains no pair for cards that are not displayed
- **AND** it contains no pair for readout, verdict, or glossary elements

#### Scenario: Offer count carries no key of its own
- **WHEN** the user activates the copy-link control at any offer count
- **THEN** the hash contains no offer-count key
- **AND** the number of offers is recoverable from the encoded per-offer keys alone

#### Scenario: Fold state is not encoded
- **WHEN** a card is collapsed and the user activates the copy-link control
- **THEN** the hash contains no key describing any card's collapsed or expanded state

#### Scenario: Values survive encoding
- **WHEN** a field holds a value needing escaping in a URL
- **THEN** the value is percent-encoded in the hash
- **AND** decoding it returns the original string exactly

### Requirement: A link restores the state it encodes
On load, when `location.hash` carries encoded state, the tool SHALL apply those values to the
matching controls before the first computation, and SHALL then render and compute exactly as if the
values had been typed. The number of offer cards to render SHALL be derived from the highest
per-offer key index present in the hash, and SHALL be clamped to the supported range. A hash
carrying no per-offer key SHALL leave the rendered offer count unchanged.

#### Scenario: Round trip
- **WHEN** a link produced from a given set of inputs is opened in a fresh page load
- **THEN** every input control reads the value it held when the link was produced
- **AND** every readout and the verdict show the same figures as before

#### Scenario: Offer cards exist before their fields are assigned
- **WHEN** a link encoding four offers is opened
- **THEN** four offer cards are rendered
- **AND** each card's rate, term, payments per year, fees, and PMI rate hold the encoded values, not the card-A defaults

#### Scenario: Link made before the offer-count key was dropped
- **WHEN** a link containing an offer-count key alongside `rate0` through `rate2` is opened
- **THEN** three offer cards are rendered
- **AND** each card holds the encoded values
- **AND** the offer-count key is ignored without an error

#### Scenario: Sparse per-offer keys
- **WHEN** a hash carries a per-offer key for a later card but none for an earlier one
- **THEN** enough cards are rendered for the highest index present
- **AND** the card named by that key holds its encoded value
- **AND** the cards with no encoded values hold the tool's defaults and compute normally

#### Scenario: Hash names no offer
- **WHEN** a hash carries only keys that name no offer field
- **THEN** the rendered offer count is unchanged
- **AND** no input control's value is changed

#### Scenario: No hash
- **WHEN** the file is opened with no hash
- **THEN** the tool loads with its existing default values and two offer cards, unchanged from today
