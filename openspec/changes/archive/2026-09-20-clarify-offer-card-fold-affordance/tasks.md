## 1. Remove the dot

- [x] 1.1 Confirm nothing reads `.dot` in card scope: grep `MortgageOfferAnalyzer.html` for `dot` and check every hit is either the card's dot rule, the dot span in the Offer A heading, or the chart's circle-marker code.
- [x] 1.2 Delete `<span class="dot"></span>` from the Offer A heading. Leave `<span class="name">Offer A</span>` in place; the clone rewrite matches `">Offer A<"` and depends on that text.
- [x] 1.3 Delete the `.offer h2 .dot` rule.
- [x] 1.4 Load the file, confirm four cards render with no dot and the heading row reads chevron, name, steppers.

## 2. Chevron weight and color

- [x] 2.1 In `.offer h2::before`, raise `width`/`height` from 6px to 8px and `border-width` from `0 1.5px 1.5px 0` to `0 2px 2px 0`.
- [x] 2.2 Change that rule's `border` color from `var(--accent)` to `var(--slate)`.
- [x] 2.3 Update the comment above that rule so it states the chevron is control chrome in the secondary text tone, not accent. Do not leave the old claim sitting above the new declaration.

## 3. Hover feedback

- [x] 3.1 Add, beside the `.fold summary` rules, a `@media (hover:hover)` block setting `.fold summary:hover h2::before{border-color:var(--accent)}`. Section 6 later adds the card-border rule to this same block.
- [x] 3.2 Verify on desktop: hovering any card heading turns that card's chevron its accent color, moving off restores slate, and no fold state changes.
- [x] 3.3 Verify the existing `:focus-visible` outline still shows on keyboard Tab to the heading, and that Enter and Space still toggle the fold.
- [x] 3.4 Verify the steppers still do not toggle the fold on click or keyboard; the stepper guard should be untouched.

## 4. Evaluation checkpoint — decide chevron color

Stop here and hand the screenshots to the user. Do not proceed to section 5 until they choose.

- [x] 4.1 Capture headless screenshots of the slate build at 4 offers: light scheme desktop 1280px, dark scheme desktop 1280px, light scheme phone 390px.
- [x] 4.2 Temporarily set the chevron back to `var(--accent)`, keeping the 8px size, and capture the same three screenshots.
- [x] 4.3 Present both sets side by side. Name what each one costs: slate separates control from identity and holds 5.83:1 light and 6.96:1 dark; accent keeps the four-card color rhythm at 4.50:1 and 5.33:1.
- [x] 4.4 Ask the user which resting color ships. Record the answer in `design.md` under Open Questions, replacing the open item with the decision and its one-line reason.
- [x] 4.5 Not applicable; slate was chosen. If the user picks accent, revert task 2.2, then replace the hover rule from 3.1: the chevron can no longer shift to accent because it already rests there. Use a faint row tint instead — add `margin-inline:-20px;padding-inline:20px` to the base `.fold summary` rule so the tint reaches the card edges, and set `background:color-mix(in srgb,var(--accent) 7%,transparent)` inside the `@media (hover:hover)` hover rule. Re-run 3.2.
- [x] 4.6 If the user picks slate, leave sections 2 and 3 as built and move on.

## 5. Verify and update specs

- [x] 5.1 Run `#selftest` headless and confirm the page title reads `selftest passed`. No new assertion needed; this change adds no logic, and the existing suite catches a broken clone path.
- [x] 5.2 Check the fold's collapsed default still holds: load at 390px, cards start collapsed; load at 1280px, cards start expanded; resize after load changes neither.
- [x] 5.3 Not applicable; slate was chosen, so the delta specs already match. If the user picked accent in 4.4, update the two delta specs in `specs/` to match: the chevron-color paragraph and the `Desktop load`, `Heading responds to hover`, and `Heading keeps its type in both states` scenarios in `specs/page-layout/spec.md` all name the secondary tone today.
- [x] 5.4 Run `openspec validate clarify-offer-card-fold-affordance --strict` and fix anything it reports.

## 6. Card border on hover

- [x] 6.1 Add `transition:border-color .15s,box-shadow .15s` to the `.offer` rule, plus a resting `inset 0 0 0 0 transparent` second shadow so the hover ring animates instead of snapping.
- [x] 6.2 Extend the `@media (hover:hover)` block so `.offer:has(> .fold > summary:hover)` takes `border-color:var(--accent)` plus `inset 0 0 0 1px var(--accent)` alongside the existing card shadow. Use child combinators so a card's heading lights only its own border, and hovering an input lights nothing.
- [x] 6.3 Verify the selector resolves: `.offer:has(> .fold > summary)` matches every rendered card, the computed transition property covers `border-color` and `box-shadow`, and the resting shadow list carries the zero-width inset placeholder so the ring animates.
- [x] 6.4 Render the hovered state headlessly by swapping `:hover` for a stand-in class in a scratch copy, and confirm in both color schemes that the hovered card shows a full accent border while its neighbours do not.
- [x] 6.5 Re-run `#selftest` and `openspec validate clarify-offer-card-fold-affordance --strict`.
- [x] 6.6 Compare ring weights at 1px, 2px and 3px inset in rendered shots and confirm the chosen weight with the user. 1px inset ships: 2px sides read as hover, while matching the 3px top bar read as selected.
