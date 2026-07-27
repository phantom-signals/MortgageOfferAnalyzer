## Why

All state lives in DOM inputs and dies with the tab. Re-entering four offers to show a spouse or lender wastes minutes and invites typos. Page has no build step and no storage, so URL is the only carrier that survives a reload or a paste into a message.

## What Changes

- Encode every input value (shared fields + each offer's fields) into `location.hash` as URL-encoded key/value pairs keyed by existing element ids.
- On load, restore inputs from hash before first compute. No hash, or unparseable hash: current defaults, unchanged.
- Add "Copy link" control near the verdict/shared card. Writes hash to the address bar, copies full URL to clipboard, gives a short confirmation.
- Keep `#selftest` working: hash equal to `#selftest` still runs `demo()` and never restores state.
- Add one footer line linking to the GitHub repo for questions, bug reports, and requests.
- Extend `demo()` with a round-trip assertion: serialize, mutate inputs, restore, values match.

No breaking change. Existing URLs (bare file path, `#selftest`) behave as today.

## Capabilities

### New Capabilities
- `share-link`: URL hash as the tool's serialized state — what is encoded, how a link restores inputs, precedence against `#selftest`, malformed-hash handling, and the copy-link control's behavior.
- `repo-feedback-link`: footer line pointing questions, bug reports, and requests at the GitHub repo. Same reason as the in-page share disclosure — hosted users never see the README, so the only reachable channel must live in the page.

### Modified Capabilities
<!-- none: offer-set, pmi-input-state, page-layout, term-glossary requirements unchanged -->

## Impact

- `MortgageOfferAnalyzer.html` only — script block and one control in shared-inputs markup.
- Restore path drives `renderOffers()` and `compute()`, already the single entry points, so PMI locking and verdict need no change.
- No dependency added: `URLSearchParams`, `navigator.clipboard`, `location.hash` are native.
- Clipboard write can reject on `file://` in some browsers. Fallback required, not optional — address bar hash is still set, so link is recoverable.
- README gains a short "Share a comparison" line.
