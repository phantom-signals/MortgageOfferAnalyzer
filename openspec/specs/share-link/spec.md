# share-link Specification

## Purpose
How an entered comparison travels between people and page loads: which input values are encoded into the URL hash, how a link restores them before the first computation, how untrusted hash content is refused, how the copy-link control and its disclosure behave, and how the self-check proves the round trip.

## Requirements
### Requirement: Entered state serializes into the URL hash
The tool SHALL encode the current value of every input control — the shared fields (loan amount,
holding period, home value, PMI removal rule, PMI premium basis) and every displayed offer's fields
(rate, term, payments per year, fees, PMI rate) — as URL-encoded key/value pairs in `location.hash`,
keyed by each control's element id. Offer count SHALL NOT be encoded as a field of its own; the
displayed offers' own keys carry it. Computed output and fold state SHALL NOT be encoded.

For a PMI rate input locked because its loan starts at or below 80% LTV, the encoded value SHALL be
the rate the user entered — which the lock holds in that field's stash — and not the `0` the locked
field displays. Restoring such a key SHALL write to the stash rather than to the visible field. The
displayed `0` is not authoritative for a locked field: it is re-asserted on every computation, so
encoding it would discard the entered rate at the first link and contradict the readout on restore.

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

#### Scenario: Locked PMI rate survives a round trip
- **WHEN** a PMI rate is entered, the loan is then lowered so the field locks and displays 0, and a
  link is produced
- **THEN** the hash carries the entered rate, not `0`
- **AND** opening that link leaves the field locked and displaying `0`
- **AND** raising the loan back above 80% LTV shows the entered rate again

#### Scenario: Values survive encoding
- **WHEN** a field holds a value needing escaping in a URL
- **THEN** the value is percent-encoded in the hash
- **AND** decoding it returns the original string exactly

### Requirement: A link restores the state it encodes
On load, when `location.hash` carries encoded state, the tool SHALL apply those values to the
matching controls before the first computation, and SHALL then render and compute exactly as if the
values had been typed. The number of offer cards to render SHALL be the greater of the count
already rendered and one more than the highest index carried by a `rate<i>` key, clamped to the
supported range. Only `rate<i>` keys raise the count: every link the tool produces carries `rate0`,
so a hash naming no rate leaves the rendered cards alone, and a restore never removes a card.

When the hash carries no encoded state, the tool SHALL seed the page from a fixed opening state
rather than leaving the markup defaults in place, so a first visit opens on two offers that contrast
with each other. A hash SHALL count as encoded state when, and only when, it contains an `=`; that
is what separates a state hash from `#selftest` and from any other bare fragment.

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
- **WHEN** a hash carries `rate3` but no `rate1` or `rate2`
- **THEN** four cards are rendered
- **AND** the fourth card holds the encoded rate
- **AND** the cards with no encoded values hold the tool's defaults and compute normally

#### Scenario: Per-offer key that is not a rate
- **WHEN** a hash carries `fees2` but no `rate2`
- **THEN** the rendered offer count is unchanged
- **AND** `fees2` restores only if a third card is already displayed

#### Scenario: Restore does not shrink the offer set
- **WHEN** four cards are displayed and a hash carrying only `rate0` and `rate1` is restored
- **THEN** four cards remain displayed
- **AND** the first two hold the encoded rates

#### Scenario: Hash names no offer
- **WHEN** a hash carries only shared-field keys and no `rate<i>` key
- **THEN** the rendered offer count is unchanged
- **AND** the shared fields restore
- **AND** no offer card's fields change

#### Scenario: No hash
- **WHEN** the file is opened with no hash
- **THEN** the tool loads with two offer cards
- **AND** the fixed opening state is applied, so Offer B opens at a lower rate and higher upfront
  fees than Offer A rather than as a copy of it

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
- **WHEN** a hash contains arbitrary text with no `=`
- **THEN** it is not treated as encoded state, and the fixed opening state is applied instead
- **AND** inputs, computation, and the verdict work normally

#### Scenario: Garbage hash containing an equals sign
- **WHEN** a hash contains arbitrary text that happens to contain an `=`
- **THEN** it is parsed as encoded state, and every key in it is dropped for naming no input control
- **AND** the opening state is therefore not applied, so the page loads on the markup defaults
- **AND** inputs, computation, and the verdict work normally, with no error

#### Scenario: Out-of-range or non-numeric value
- **WHEN** a hash encodes a negative, zero, or non-numeric value for a numeric field
- **THEN** the existing input and calculation guards apply unchanged
- **AND** that offer's readout renders as it does today for invalid input, with no crash and no effect on the other offers

### Requirement: The self-test hash is never read as state
The `#selftest` hash SHALL run the self-check and SHALL NOT be interpreted as encoded state.
Carrying no `=`, it seeds the opening state like any other non-state hash, and the self-check then
runs against that state. A hash carrying encoded state SHALL NOT run the self-check.

#### Scenario: Self-test hash
- **WHEN** the file is opened with `#selftest`
- **THEN** the opening state is applied first, `#selftest` carrying no `=`
- **AND** the self-check runs against it
- **AND** the page title becomes `selftest passed`, or `SELFTEST FAILED: <reason>` on failure
- **AND** no part of the hash is assigned to any input control

#### Scenario: State hash
- **WHEN** the file is opened with a hash carrying encoded state
- **THEN** the state restores
- **AND** the self-check does not run
- **AND** the page title is unchanged

### Requirement: Copy-link control publishes the current state
The tool SHALL provide a control that writes the current state into `location.hash` and copies the resulting full URL to the clipboard, reporting the outcome to the user. When the clipboard write is unavailable or rejected, the hash SHALL still be set so the link remains recoverable from the address bar. The page SHALL state next to that control that the link embeds the entered figures, since the tool is used as a hosted page where no repository documentation is visible. The control SHALL be reachable at every offer count the tool supports, including counts at which the comparison verdict is not displayed.

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

#### Scenario: Control available with a single offer
- **WHEN** one offer is displayed and the comparison verdict is therefore hidden
- **THEN** the copy-link control and its disclosure text are still displayed
- **AND** activating it produces a link that restores that single offer

#### Scenario: Control available at every offer count
- **WHEN** the offer count is changed to any supported value
- **THEN** the copy-link control remains displayed and in the same position relative to the offers

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
- **AND** it restores the page to the opening state when finished
