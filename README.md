# Mortgage Offer Analyzer

Compare up to four mortgage offers on the same loan amount and see which one
actually costs least. One self-contained HTML file — no build, no dependencies,
no network. Open it from disk.

## Use

Download [`MortgageOfferAnalyzer.html`](MortgageOfferAnalyzer.html) and open it
in a browser. That's the whole setup.

Enter a shared loan amount and home value, then each offer's rate, term,
payment frequency, fees, and PMI rate. Results update as you type: monthly
payment, total interest, PMI paid, and total cost, with the cheapest offer
called out. Set a holding period to truncate costs at the point you expect to
sell or refinance instead of running to full term.

Every input and result label has a hover definition, and the footer carries the
full glossary.

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

## Not modeled

Property taxes, homeowners insurance, and escrow are excluded — this compares
loan cost, not total housing cost. PMI assumes scheduled amortization only;
extra principal or appreciation can end it sooner, and cancellation at 80% must
be requested in writing. FHA mortgage insurance (MIP) follows different rules
and is not modeled. Adjustable rates are not modeled — each offer is a fixed
rate for its full term.

This is a modeling tool, not financial advice. Cross-check anything that
matters against your lender's own figures or a calculator from
[Bankrate](https://www.bankrate.com/mortgages/amortization-calculator/),
[Fannie Mae](https://yourhome.fanniemae.com/calculators-tools/mortgage-calculator),
or [SmartAsset](https://smartasset.com/mortgage/mortgage-calculator).

## Self-test

Open the file with `#selftest` appended to the URL. It asserts the payment,
interest, PMI, and total-cost figures against pinned values, checks PMI
termination timing, and exercises the offer-card rendering, verdict ranking,
PMI input locking below 80% LTV, and hover definitions.

On success the page title becomes `selftest passed`; on failure it becomes
`SELFTEST FAILED: <reason>` and the error is logged to the console. The title
is readable from a headless run (`--dump-dom`), so it works in CI.

## License

MIT — see [LICENSE](LICENSE).
