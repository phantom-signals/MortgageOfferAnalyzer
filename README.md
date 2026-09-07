# Mortgage Offer Analyzer

Compare up to four mortgage offers on the same loan amount and see which costs
least. One self-contained HTML file — no build, no dependencies, no network
calls. Open it from disk, or serve it as a static site.

A companion page, [`math.html`](math.html), derives every formula the analyzer
uses from first principles. It is generated from [`MATH.md`](MATH.md); see
[Building the math page](#building-the-math-page).

## Use

Download [`MortgageOfferAnalyzer.html`](MortgageOfferAnalyzer.html) and open it
in a browser. That's the whole setup. To host it instead, use the included
Cloudflare static-asset config ([`wrangler.jsonc`](wrangler.jsonc)), which
serves the page at the root.

Pick how many offers to compare: one analyzes a single loan, two or more rank
them. The `+`/`−` buttons on each card add and remove offers. Enter a shared
loan amount and home value, then each offer's rate, term, payment frequency,
fees, and PMI rate. Results update as you type — payment per period, total
interest, PMI paid, total cost, and a verdict naming the cheapest offer. Set a
holding period to cut the costs off at the year you expect to sell or
refinance, instead of running them to full term.

Two charts sit under the offers. **Cost breakdown** stacks interest, PMI, fees,
principal, and any remaining balance on one scale shared by every offer.
**Cost over time** plots what walking away in any year costs, payoff of the
balance included, and marks the year the lead changes hands.

Every input and result label carries a definition: hover with a pointer, tap
the label on a touch screen. The footer holds the full glossary, the method,
the PMI rules, the privacy statement, and the terms of use.

## Share a comparison

**Copy analysis link** writes every entered value into the URL and copies it.
Opening that URL restores the offers exactly, so you can bookmark a comparison
or send it to someone. The figures ride in the link in plain text — loan
amount, home value, rates, fees — so treat a shared link the way you would
treat the numbers themselves. The page uploads nothing; the link is the only
copy.

## What it computes

Payment is the standard amortization formula:

```
M = P·i·(1+i)ⁿ / [(1+i)ⁿ − 1]
```

where `i` = rate ÷ payments-per-year and `n` = term × payments-per-year.

- **Total to term** — `M×n + fees + PMI`
- **Over a holding period** — payments made + PMI paid + fees + remaining balance still owed
- **PMI** — charged while the *scheduled* balance exceeds the selected share of
  the home's original value (78% automatic termination or 80% on written
  request), and never past the amortization midpoint. Premiums can be
  recalculated on the declining balance or fixed on the original loan amount.
  A loan starting at or below 80% LTV owes no PMI, and its PMI input locks at 0.

## The math

[`MATH.md`](MATH.md) is the full derivation, in five parts: the amortization
recurrence and the payment formula, the balance curve and its shape, the PMI
schedule and its termination rules, the two cost totals and what they leave
out, and the cost-over-time chart. It is written for a reader who knows
math but not finance.

[`math.html`](math.html) is that document as a web page, linked from the
analyzer's Method footnote. The math is MathML rendered natively by the
browser, so the page fetches nothing and needs no script — the same
`default-src 'none'` posture as the analyzer itself.

### Building the math page

The analyzer needs no build. The math page does, since Markdown and TeX have to
become HTML and MathML:

```
npm install          # markdown-it + @vscode/markdown-it-katex, dev-only
npm run build:math   # MATH.md -> math.html
```

Edit `MATH.md`, never `math.html` — the latter is generated and overwritten.

## Not modeled

This page ignores property taxes, homeowners insurance, and escrow: it compares
loan cost, not total housing cost. PMI assumes scheduled amortization only —
extra principal or appreciation can end it sooner, and you must ask in writing
for cancellation at 80%. FHA mortgage insurance (MIP) follows different rules
and is out of scope. So are adjustable rates: every offer is a fixed rate for
its full term.

This is a modeling tool, not financial advice. Check anything that matters
against your lender's own figures, or against a calculator from
[Bankrate](https://www.bankrate.com/mortgages/amortization-calculator/),
[Fannie Mae](https://yourhome.fanniemae.com/calculators-tools/mortgage-calculator),
or [SmartAsset](https://smartasset.com/mortgage/mortgage-calculator).

## Self-test

Open the file with `#selftest` appended to the URL. It pins the payment,
interest, PMI, and total-cost figures against known values and checks when PMI
terminates. It then exercises the offer cards, the verdict ranking and its tie
wording, the PMI input lock at or below 80% LTV, the share link's round trip,
the definitions, and the chart's agreement with the verdict across a
break-even.

On success the page title becomes `selftest passed`; on failure it becomes
`SELFTEST FAILED: <reason>`, and the error goes to the console. A headless run
(`--dump-dom`) can read the title, so it works in CI.

## License

MIT — see [LICENSE](LICENSE).
