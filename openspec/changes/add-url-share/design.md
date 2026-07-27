## Context

`MortgageOfferAnalyzer.html` is one self-contained file, no build, no dependencies, no network, opened from disk or served static from Cloudflare Workers. All state already lives in DOM controls: shared ids `offerCount`, `amount`, `horizon`, `homeValue`, `pmiThresh`, `pmiBasis`, and per offer `i` in 0..3 the ids `rate{i}`, `term{i}`, `freq{i}`, `fees{i}`, `pmi{i}`. Every control carries class `inp`.

Two entry points already own all state flow: `renderOffers(n)` clones or trims cards then calls `compute()`, and `compute()` reads every field, enforces PMI locking, renders readouts, calls `verdict()`. Boot is one line, `renderOffers(+$("offerCount").value)`, followed by the `location.hash === "#selftest"` check that runs `demo()`.

`location.hash` is the only carrier available: no storage, no server, no build.

## Goals / Non-Goals

**Goals:**
- Round-trip every input through a URL and back with identical rendered results.
- Restore path reuses `renderOffers()` and `compute()`, so PMI locking, verdict, tooltips need no new code.
- `#selftest` keeps working, unchanged invocation.
- Malformed or hostile hash never breaks the page and never reaches the DOM as markup.

**Non-Goals:**
- Shortening the link (no compression, no base64, no default-value omission).
- Live hash update while typing.
- Persisting to `localStorage`, server-side storage, or link shorteners.
- Restoring computed output — output is derived, recomputed on restore.

## Decisions

**Encode as `URLSearchParams` keyed by element id.**
`new URLSearchParams(...)` over `[...document.querySelectorAll(".inp")].map(el => [el.id, el.value])` serializes; `for (const [k,v] of new URLSearchParams(hash.slice(1)))` restores. Native, no parser to write, handles escaping both ways.
Alternatives rejected: JSON plus base64 — opaque in the address bar, longer, needs try/catch around two more calls. Positional CSV — shortest string, but any future field shifts every position and silently mis-assigns old links.

**Serialize all fields, not only non-defaults.**
Diffing against defaults saves ~40 characters and costs a defaults table that must stay in sync with the markup. Not worth it.

**Restore order: `offerCount` first, then `renderOffers(n)`, then remaining keys, then `compute()`.**
Per-offer ids `rate1`..`pmi3` do not exist until their cards are cloned. Assigning before the clone silently drops offers B through D. Card 0 is present in static markup, so a 1-offer link works either way — order still matters for every count above 1.

**Reject unknown keys at the boundary.**
Hash is untrusted input; a link can be crafted by anyone. Restore assigns only to elements matching `document.querySelector('.inp#' + id)`-equivalent lookup — element exists, and carries class `inp`. Never `innerHTML`, never `eval`, never attribute writes. Consequence: `id` collisions with non-input elements (`verdict`, `glossary`, `out0`) cannot be written; unknown keys are dropped silently rather than throwing, so a link from a future version still restores the fields it shares.

Value sanity is left to the existing math: `compute()` runs every field through `parseFloat`, and `calc()` already returns `null` for non-finite or non-positive inputs, which renders as the current empty readout. Number inputs also reject non-numeric strings on assignment (`el.value = "abc"` yields `""`). No separate validation layer.

**`#selftest` wins by exact match, restore requires a `=`.**
Existing check `location.hash === "#selftest"` stays byte-identical. Restore triggers only when the hash contains `=`, so `#selftest` never enters the restore path and a restore hash never runs `demo()`.

**Hash written on explicit "Copy link" only.**
Writing the hash on every `input` event churns the address bar and pollutes history while the user types. Button click sets `location.hash` and copies `location.href`. Cost: a link is stale until clicked again — acceptable, the button is the share gesture.

**Disclosure lives in the page, not the README.**
Deployment is a static Cloudflare page; the repo README is not part of the served experience, so a privacy note there reaches nobody who actually clicks share. The copy-link control carries a `<span class="hint">` reading that the link embeds the entered figures — same hint element every field label already uses, so no new styling. Rejected: a confirm dialog before copying (one gesture becomes two for a non-secret), and a one-time dismissible banner (needs persistence the file has no storage for).

**Clipboard: `navigator.clipboard.writeText(location.href)` with a fallback.**
`file://` origins are not a secure context in every browser, and the promise rejects. On rejection the button label reports that the link is in the address bar — the hash is set before the copy is attempted, so the link is always recoverable by hand. No `document.execCommand("copy")` shim, no hidden textarea.

**Check: extend `demo()` with one round-trip assertion.**
Set known values across 3 offers, serialize, mutate every field, restore from the serialized string, assert values match and that a restored total-cost readout equals the pre-serialize one. `demo()` already resets state at its end; the new block follows the same pattern.

## Risks / Trade-offs

- Link carries loan amount, home value, and rates in plaintext, and URLs land in chat logs, browser history, and referer headers. → Disclosure sits in the page next to the copy control, not in the README: the tool is served as a static Cloudflare page, where nobody sees the repo. README note stays as secondary.
- PMI fields locked at or below 80% LTV serialize as `0`, losing each card's `dataset.prev` stash. → Restored link at the same LTV re-locks to `0` and displays identically; only the stashed pre-lock rate is lost. Round-trip of what is displayed is exact. Preserving the stash means encoding shadow state for a value the math discards.
- Long hash (~150 characters at 4 offers) can be truncated by chat clients that linkify greedily. → Nothing to do inside a static file; compression only shifts the threshold. Note it if it is ever reported.
- Restore silently ignores unknown keys, so a typo in a hand-edited link is invisible. → Preferred over throwing on a shared link. The visible readout is the feedback.
- `demo()`'s round-trip block writes to `location.hash` if it uses the real address bar. → Serialize and restore take a string argument so the test never touches `location`.
