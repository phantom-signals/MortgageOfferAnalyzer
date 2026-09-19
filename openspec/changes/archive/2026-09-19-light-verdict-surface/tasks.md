## 1. Tokens

- [x] 1.1 In light `:root`, add `--banner-bg:var(--card)`, `--banner-fg:var(--ink)`, `--banner-line:var(--line-strong)`
- [x] 1.2 In dark `@media` `:root`, add `--banner-bg:var(--verdict-bg)`, `--banner-fg:var(--verdict-fg)`, `--banner-line:transparent`

## 2. Verdict style

- [x] 2.1 `.verdict` rule: use `--banner-bg` / `--banner-fg`, add `border:1px solid var(--banner-line)`
- [x] 2.2 Leave `.tip` and `#defPop` on `--verdict-bg` / `--verdict-fg`

## 3. Check

- [x] 3.1 Light scheme, 2–4 offers: bar matches cards, letters readable in accent, label and horizon note legible (swap `opacity` for `--slate` if weak)
- [x] 3.2 Dark scheme: verdict looks identical to before
- [x] 3.3 Light scheme: chart tooltip and definition popover still dark
- [x] 3.4 `#selftest` still passes
