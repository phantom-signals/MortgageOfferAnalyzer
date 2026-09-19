## Context

`--verdict-bg` / `--verdict-fg` drive three things: `.verdict` bar, `.tip` chart tooltip, `#defPop` definition popover. Light: `#161a1d` on `#f4f5f2`. Dark: `#0c0e10` on `#e8eaec`. `verdict()` colors offer letters with `var(--a..d)`, which are light-scheme accents in light mode (contrast-checked against `--card` white).

## Goals / Non-Goals

**Goals:**
- Light-mode verdict harmonizes with page; offer letters readable in own accent.
- Dark mode pixel-identical.

**Non-Goals:**
- Restyling tooltip or popover.
- New accent palette.
- Theme toggle.

## Decisions

- **New tokens `--banner-bg`, `--banner-fg`, `--banner-line` used only by `.verdict`.** Light: `var(--card)`, `var(--ink)`, `var(--line-strong)`. Dark: `var(--verdict-bg)`, `var(--verdict-fg)`, `transparent`. Alternative: change `--verdict-bg` itself. Rejected: drags tooltip and popover light too; they read fine dark as overlays.
- **Light bar = card surface + 1px `--line-strong` border.** Matches cards, so verdict reads as part of page, not foreign slab. Emphasis kept by size/weight of headline and amount, already bold. Alternative: tinted fill (e.g. `--good` 8%). Rejected for now: adds color competing with offer letters, the thing user disliked.
- **Letters keep `var(--a..d)`.** On white those accents already meet offer-set contrast requirement; no JS change.

## Risks / Trade-offs

- [Light verdict less prominent than black slab] → Placement above offers (page-layout spec) plus bold 22px amount carry it. If too quiet, add left accent border later.
- [`opacity:.65` label/note on white may drop below comfortable contrast] → Check `--ink` at .65 on white in light mode; fall back to `color:var(--slate)` if weak.

## Open Questions

- Tinted fill or plain card surface? Default: plain card. Say if want tint.
