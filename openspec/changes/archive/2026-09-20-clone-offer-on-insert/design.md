## Context

`insertOffer(i)` in `MortgageOfferAnalyzer.html` already does the hard part: it snapshots every card's values into `rows`, grows the card count, splices a row into position `i + 1`, then writes all rows back by position. The only reason the new card carries defaults is the row it splices in:

```js
const rows = [...offers.children].map(c => fieldsOf(c).map(getVal));
renderOffers(rows.length + 1);
rows.splice(i + 1, 0, fieldsOf(offers.lastElementChild).map(getVal));
rows.forEach((row, c) => fieldsOf(offers.children[c]).forEach((el, j) => setVal(el, row[j])));
```

Line 3 reads the fresh clone `renderOffers()` just appended, which is the card markup at its default attributes. `rows[i]` — the source card, snapshotted on line 1, before anything moved — is the row wanted instead.

## Goals / Non-Goals

**Goals:**
- The add control produces a copy of the card it sits in, across all five per-offer fields.
- The locked-PMI case copies the stashed rate, not the displayed `0`.

**Non-Goals:**
- Changing `renderOffers()`. Cards it appends on its own — share-link restore, any programmatic count change — keep their default values.
- Any UI affordance distinguishing "add blank" from "duplicate". One control, one behavior.
- Changing `removeOffer()`, the share-link format, or any math.

## Decisions

**Splice `rows[i]` instead of reading the appended clone.** `rows` is captured before `renderOffers()` runs, so `rows[i]` is the source card's state at the moment of the press, unaffected by the render. This deletes a DOM read rather than adding code, and the default-values path stays intact in `renderOffers()` for every other caller.

Alternative considered: copy the source card's DOM node directly and re-id it. Rejected — `cardHTML()` already owns letter and id rewriting, and a second rewriting path would drift.

**Copy the row array, not its reference** (`rows[i].slice()`). `setVal` only reads from the row, so sharing the array is harmless today; the copy costs seven characters and removes the aliasing footgun if the write-back loop ever mutates.

**PMI lock needs no special case.** `getVal` already returns `dataset.prev` for a disabled field and `setVal` already writes to the stash for one, which is exactly how `removeOffer()` shifts locked PMI values today. The copied row carries the stash, so unlocking shows the source rate on both cards. The spec scenario exists to pin this, not because code is needed for it.

**Bound check unchanged.** The early `if(offers.children.length >= LETTERS.length) return;` still guards the four-card ceiling.

## Risks / Trade-offs

- **Users who wanted a blank card now get a filled one, and must clear fields to start fresh.** → Accepted: this is the requested behavior, and the values are five editable fields, not a hidden state. No "add blank" escape hatch until someone asks for one.
- **A duplicated card is identical to its source, so the verdict reports a tie until the user edits it.** → Already correct behavior: the tie path names both letters and shows the shared cost. No change needed.
- **Existing share links are unaffected**, since the hash carries explicit per-offer values and `restore()` never routes through `insertOffer()`.
