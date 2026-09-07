# The math behind the Mortgage Offer Analyzer

A mathematical walkthrough of the tool.

Notation used throughout:

| Symbol | Meaning |
|---|---|
| $P$ | principal — the amount actually borrowed |
| $r$ | quoted annual nominal rate (as a decimal) |
| $m$ | compounding periods per year (12 = monthly) |
| $i = r/m$ | periodic rate |
| $T$ | term in years |
| $n = mT$ | total number of payments |
| $M$ | the fixed periodic payment (principal + interest) |
| $B_k$ | balance still owed after payment $k$ |
| $F$ | upfront fees, paid at closing |
| $V$ | home value at purchase |
| $h$ | holding period in years; $k = mh$ periods |

---

## Part 1 — The loan, and where the payment number comes from

### The rule of the loan

Each period two things happen, in this order: the outstanding balance grows by
the interest factor, then you hand over a fixed payment $M$.

$$B_t = B_{t-1}(1+i) - M, \qquad B_0 = P$$

That is the entire financial content of a mortgage. Everything else on the site
is a consequence of this one line.

### Solving the recurrence

It is a linear first-order recurrence, so unroll it:

$$B_k = P(1+i)^k - M\sum_{j=0}^{k-1}(1+i)^j = P(1+i)^k - M\,\frac{(1+i)^k - 1}{i}$$

The sum is geometric. Two competing terms: your debt compounding upward, and
your accumulated payments compounding upward, racing each other.

### Fixing the payment $M$

A mortgage is *defined* by the condition that the balance reaches zero exactly
at period $n$ — that is what "30-year fixed" means. Set $B_n = 0$ and solve:

$$\boxed{\;M = P\,\frac{i(1+i)^n}{(1+i)^n - 1}\;}$$

Two limits worth checking yourself:

- **$i \to 0$.** Expand $(1+i)^n \approx 1 + ni$, giving $M \to P/n$. No
  interest, so principal splits evenly. The site special-cases this branch in
  `calc()`, where the payment is chosen.
- **$n \to \infty$ with $i > 0$.** $M \to Pi$. A perpetual loan: you pay the
  interest forever and never touch principal. This is the floor no term can go
  below — if $M \le Pi$ the balance never shrinks at all.

### Total interest

Total handed over across the full term is $Mn$. Of that, $P$ is money you
actually borrowed. The rest is interest:

$$\text{total interest} = Mn - P$$

Note this is **not** $P\,r\,T$. That would be interest on the full principal for
the whole term, but the balance is falling the entire time. The true amount is
$i\sum_{k=0}^{n-1} B_k$ — a sum under the decaying balance curve — and the two
expressions agree.

### Effective annual rate

The quoted rate $r$ is a nominal convention: "6% compounded monthly" means 0.5%
applied twelve times, which is not 6% of growth. Actual growth over one year:

$$\text{EAR} = (1+i)^m - 1$$

For $r = 6\%$: $1.005^{12} - 1 = 6.168\%$. This is the site's apples-to-apples
number when two offers compound differently.

### One numerical note

Everything above needs $(1+i)^k - 1$. Computing that as `pow(1+i,k) - 1`
catastrophically cancels for small $i$: you subtract 1 from a number barely
above 1 and lose every significant digit. The site computes it as
$\exp\!\big(k\log(1+i)\big) - 1$ using `expm1`/`log1p`, which are built to hold
precision near zero.

---

## Part 2 — The balance at an arbitrary time, and the shape of that curve

### A cleaner closed form

Part 1 gave $B_k = P(1+i)^k - M\,\frac{(1+i)^k - 1}{i}$. Regroup the terms that
carry $(1+i)^k$:

$$\boxed{\;B_k = \left(P - \frac{M}{i}\right)(1+i)^k + \frac{M}{i}\;}$$

This is the form worth remembering. It says the balance is an exponential
displaced by a constant, and the constant $M/i$ is the whole story.

**What $M/i$ is.** It is the principal of a loan whose interest exactly equals
the payment — the perpetuity from Part 1, the balance that would sit still
forever. Call it the *equilibrium* $B^\ast = M/i$. Then

$$B_k = B^\ast - (B^\ast - P)(1+i)^k$$

and $B^\ast$ is a repelling fixed point of the recurrence $B \mapsto B(1+i)-M$.
Start below it and you are pushed away downward, faster and faster. Start above
it and the balance runs away upward — that is a loan that never amortizes. A
real mortgage always has $P < B^\ast$, and the gap $B^\ast - P$ is the seed of
the exponential.

*(Worked case used throughout: $P = \$400{,}000$, $r=6.5\%$, 30 years. Then
$M = \$2{,}528.27$ and $B^\ast = \$466{,}758$. The loan starts only 17% below
its own runaway point — which is why the early years feel like nothing is
happening.)*

### Treating $k$ as continuous

Write $\delta = \ln(1+i)$, the continuously-compounded equivalent of $i$ (in
finance, the *force of interest*). Then $(1+i)^k = e^{\delta k}$ and

$$B(k) = B^\ast - (B^\ast - P)e^{\delta k}$$

$$B'(k) = -\,\delta\,(B^\ast - P)\,e^{\delta k}, \qquad
  B''(k) = -\,\delta^2 (B^\ast - P)\,e^{\delta k}$$

Both derivatives are negative for the whole term. So the balance curve is
**decreasing and concave**: it falls slowly at first and the fall accelerates,
lying above the straight line from $(0,P)$ to $(n,0)$ the entire way. Nothing
about a mortgage is linear, and this is where the intuition breaks for most
people.

Concavity has a blunt consequence. Setting $B(k) = P/2$:

$$k_{1/2} = \frac{1}{\delta}\,\ln\!\frac{B^\ast - P/2}{B^\ast - P}$$

For the worked case: $k_{1/2} = 256$ payments $= 21.4$ years. You are **21 years
into a 30-year loan** before you have repaid half the principal.

### How each payment splits

Payment $t$ is a fixed $M$, but it is doing two jobs. Interest owed that period
is $i B_{t-1}$; whatever is left knocks down principal:

$$\underbrace{i B_{t-1}}_{\text{interest}} + \underbrace{\big(M - i B_{t-1}\big)}_{\text{principal}} = M$$

The principal portion has an exact structure. Let $p_t = M - iB_{t-1}$. Then

$$p_{t+1} = M - iB_t = M - i\big(B_{t-1}(1+i) - M\big) = (1+i)\big(M - iB_{t-1}\big) = (1+i)\,p_t$$

**The principal portion grows by exactly the factor $(1+i)$ every single
period** — a clean geometric sequence, $p_t = p_1 (1+i)^{t-1}$, with
$p_1 = M - iP$. The interest portion is its mirror image, $M - p_t$, decaying
toward zero.

In the worked case, payment 1 is \$2,166.67 interest and \$361.61 principal —
86% of your money evaporating. Payment 360 is \$13.62 interest and \$2,514.65
principal. Same \$2,528.27 either way.

### What the site computes at a holding horizon

If you sell or refinance after $h$ years, that is $k = mh$ periods. The site
needs three numbers:

$$B_k = \left(P - \frac{M}{i}\right)(1+i)^k + \frac{M}{i}$$

$$\text{paid} = Mk$$

$$\text{interest paid} = Mk - \underbrace{(P - B_k)}_{\text{principal retired}}$$

The last one is just conservation: of the $Mk$ dollars handed over, exactly
$P - B_k$ went to principal, so the remainder was interest.

`horizon()` evaluates these. Two details: it clamps $k \le n$, since holding
past the term is just holding to the term, and it carries the same $i = 0$
branch as `calc()`, where the balance degenerates to $\max(P - Mk,\;0)$.

These three are not yet the cost of holding for $h$ years. Two components have
not appeared: mortgage insurance, derived in Part 3, and the upfront fees $F$,
which Part 4 folds in alongside the payoff of $B_k$.

---

## Part 3 — Mortgage insurance, the one piecewise part of the model

Everything so far has been one smooth exponential. Mortgage insurance is where
that stops.

### What it is

If you borrow more than 80% of what the home is worth, the lender requires
**private mortgage insurance (PMI)**, a policy insuring the lender against your
default. It protects the lender, not you, and you pay for it on top of $M$,
until the loan is small enough relative to the home that the lender stops
demanding it.

Three new inputs: the home's value at purchase $V$, an annual premium rate $q$,
and a choice of removal rule $\theta$.

### Loan-to-value

$$\mathrm{LTV}_k = \frac{B_k}{V}$$

$V$ here is the value **at purchase**, and it never moves. Not the current
market value, not an appraisal you order later. That is not a modeling
shortcut: the federal Homeowners Protection Act (HPA) defines termination against the
[original value](https://www.law.cornell.edu/uscode/text/12/4901) — "the lesser
of the sales price ... or the appraised value at the time at which the subject
residential mortgage transaction was consummated" (12 U.S.C. § 4901(12)) — so a
rising market does not shorten this schedule.

The only moving part in the ratio is the numerator $B_k$, falling along the
Part 2 curve. That fall is the whole mechanism by which PMI ends.

### Is it owed at all?

Only if the loan starts above 80% LTV:

$$\text{PMI required} \iff \frac{P}{V} > 0.80$$

`pmiOwed()` tests this. It compares against $0.80 + \varepsilon$ with
$\varepsilon = 10^{-12}$, so a loan sitting exactly at 80% — $P = \$360{,}000$
on a $\$450{,}000$ home — is not dragged over the line by binary rounding.

### The premium

Charged per period at rate $q/m$, against one of two bases the lender picks:

$$\text{prem}_t = \frac{q}{m} \times
\begin{cases}
B_{t-1} & \text{declining basis}\\[2pt]
P & \text{fixed basis}
\end{cases}$$

Note the balance used is $B_{t-1}$, the balance *before* payment $t$. Under the
declining basis the premium shrinks along the amortization curve; under the
fixed basis it is a constant dollar amount. Both conventions are in real use,
which is why it is an input rather than an assumption.

### When it stops

Two rules, both from [12 U.S.C. § 4902](https://www.law.cornell.edu/uscode/text/12/4902).
PMI ends at whichever fires first.

**1. The LTV threshold.** Premiums stop once the balance reaches $\theta V$. The
site offers the two HPA exit points: $\theta = 0.80$ (you may request
cancellation in writing) and $\theta = 0.78$ (the servicer must terminate
automatically).

Setting $B(k) = \theta V$ in the Part 2 closed form:

$$k_\theta = \frac{1}{\delta}\,\ln\frac{B^\ast - \theta V}{B^\ast - P}$$

**2. The amortization midpoint.** § 4902(c) forbids the requirement "beyond the
first day of the month immediately following ... the midpoint of the
amortization period", regardless of balance. This binds only when the loan
amortizes too slowly to reach $\theta V$ in half the term — a high initial LTV,
a long term, or both.

$$t_{\text{end}} = \min\big(\lceil k_\theta \rceil,\; \lfloor n/2 \rfloor\big)$$

*(Worked case: $P=\$400{,}000$ at 6.25%, 30 years, $V=\$450{,}000$,
$\theta=0.78$. Then $k_\theta = 98.997$, the midpoint is 180, so the threshold
binds and $t_{\text{end}} = 99$ — PMI runs 8.25 years. The site reports period
99.)*

### Note: Prepayment effects are not modeled

The site has no extra-payment input: it models the scheduled balance of Part 2
and nothing else, so scheduled and actual coincide and $k_\theta$ is the answer
for either threshold.

If you do pay extra, the two thresholds diverge, and the statute is explicit
about it. The 80% *cancellation date* is, at your option, the date the balance
"based solely on **actual payments**, reaches 80 percent of the original value"
(§ 4901(2)(A)(ii)) — prepayment pulls it in. The 78% *termination date* is fixed
"based solely on the initial amortization schedule ... and **irrespective of the
outstanding balance**" (§ 4901(18)(A)) — prepayment does not move it, and
neither does it move the midpoint.

So under prepayment the site's PMI figure stays exact for $\theta = 0.78$ and
becomes an upper bound for $\theta = 0.80$.

### Accumulated PMI

The site carries the running total

$$\mathrm{cumPMI}_k = \sum_{t=1}^{k}\text{prem}_t$$

so it can be read off at any horizon. Under the fixed basis this is trivially
linear, $\frac{qP}{m}\min(k, t_{\text{end}})$. Under the declining basis, sum
the Part 2 closed form for $k \le t_{\text{end}}$:

$$\sum_{t=1}^{k} B_{t-1} = \sum_{j=0}^{k-1}\Big[B^\ast - (B^\ast - P)(1+i)^j\Big]
= kB^\ast - (B^\ast - P)\frac{(1+i)^k - 1}{i}$$

and recognize the second term: from Part 2, $P - B_k = (B^\ast - P)[(1+i)^k-1]$,
so the sum is $kB^\ast - (P - B_k)/i$. Substituting $B^\ast = M/i$ and
multiplying by $q/m = qi/r$, since $i=r/m$:

$$\boxed{\;\mathrm{cumPMI}_k = \frac{q}{r}\Big[Mk - (P - B_k)\Big] = \frac{q}{r}\times\text{interest paid through }k\;}$$

**Declining-basis PMI is a fixed fraction $q/r$ of the interest paid over the
same window.** Which makes sense once you see it: both are the same balance
integral, one scaled by $q/m$ and the other by $i = r/m$. In the worked case
$q/r = 0.0055/0.0625 = 8.8\%$, interest through period 99 is $\$194{,}822$, and
$8.8\%$ of that is $\$17{,}144$ — exactly the total PMI the site reports.

The site does not use this identity; `calc()` accumulates the sum in a loop and
stores it. The stored array makes `horizon()` an $O(1)$ lookup, and the chart
calls it hundreds of times per offer to draw a line — cheaper than recomputing
logarithms at every sample. And the loop is the specification: its per-period
test is the termination rule transcribed, where the closed form is a derivation
whose rounding has to be kept in agreement with it.

### Why the cost curve has no jump at $t_{\text{end}}$

$\mathrm{cumPMI}_k$ is a *running total*, so it is continuous everywhere. PMI
ending removes a rate, not a level: the sequence $\text{prem}_t$ drops to zero,
which is a discontinuity in the increment. In the sum, only the slope inherits
that discontinuity; the value stays continuous. Formally $\mathrm{cumPMI}$ is
$C^0$ and not $C^1$ at $t_{\text{end}}$.

Part 5 quantifies how small that slope discontinuity is on screen.

---

## Part 4 — Total cost, and the cost to walk away

Parts 1-3 produced pieces. This part adds upfront fees, assembles everything
into the two totals that decide which offer is cheaper, and states what those
totals leave out.

### Fees

$F$ is the upfront cost of taking the loan: origination, points, and the rest of
the closing charges. It is paid in cash at closing and **not** rolled into $P$,
so it never accrues interest and never amortizes. In the model it is a constant,
added once.

It is also the only quantity so far that is large at $k=0$ and never grows. That
asymmetry is what makes the comparison interesting: a lower rate bought with
points is a fixed cost now against a slowly accumulating saving later.

### Cost to term

If you hold the loan to the end:

$$\boxed{\;C_{\text{term}} = \underbrace{Mn}_{\text{all payments}} + F + \mathrm{cumPMI}_n\;}$$

### Cost to walk away

If you sell or refinance at $h$ years, $k = mh$ periods, you stop paying $M$ and
must clear the remaining balance in one lump:

$$\boxed{\;C_{\text{clear}}(k) = \underbrace{Mk}_{\text{payments made}} + \mathrm{cumPMI}_k + F + B_k\;}$$

Note: PMI enters as $\mathrm{cumPMI}_k$, the premiums actually paid through $k$,
and nothing more. Paying off $B_k$ ends the loan, and premiums that would have
been charged between $k$ and $t_{\text{end}}$ are never incurred.

The two agree where they should. At $k = n$: $B_n = 0$, $\mathrm{cumPMI}_n$ is
the full total, and $C_{\text{clear}}(n) = C_{\text{term}}$.

### The five-component decomposition

The site draws both totals as a stacked bar. The components are chosen to
partition the total exactly — they sum to it, with no overlap and no remainder:

| Component | At horizon $k$ | To term |
|---|---|---|
| Interest paid | $Mk - (P - B_k)$ | $Mn - P$ |
| PMI | $\mathrm{cumPMI}_k$ | $\mathrm{cumPMI}_n$ |
| Upfront fees | $F$ | $F$ |
| Remaining balance | $B_k$ | $0$ |
| Principal retired | $P - B_k$ | $P$ |

To see that they sum correctly, add interest paid and principal retired. The
$(P - B_k)$ subtracted from the first is exactly the second, so it cancels:

$$\big[Mk - (P - B_k)\big] + (P - B_k) = Mk$$

which is every payment you made. Adding the remaining balance, PMI, and fees
gives $C_{\text{clear}}(k)$. The same cancellation at $k = n$ gives
$C_{\text{term}}$.

### Inflation and equity are not modeled

Two modeling choices are worth stating plainly, because both affect how you
should read the comparison.

**No time value of money.** Every term above is a nominal dollar, and dollars
from different years are added as equals. There is no discounting, no assumed
inflation, no return on the cash you did not spend on points. A dollar of fees
at closing counts the same as a dollar of interest in year 28, even though the
first is unambiguously more expensive.

**Not your net financial position.** $C_{\text{clear}}$ is the total cash the
*loan* consumes. The house is not credited back — no sale price, no
appreciation, no selling costs, no tax treatment of interest. Notice this makes
the "principal retired" component misleading if read alone: that money was not
lost, it became equity. It appears in the total because the total is cash out,
not net worth.

These choices are made because the tool is designed to compare offers on the
same house. Every omitted term — the house's value, the appreciation, the
sale costs — is identical across offers and cancels in the difference. What
survives is exactly what the offers differ on: $M$, $F$, and the PMI schedule.

The consequence is that the *differences* between offers are trustworthy and the
*absolute* totals are not a forecast of your finances.

---

## Part 5 — The cost-over-time chart

The chart plots $C_{\text{clear}}$ from Part 4 as a function of how long you
hold, one curve per offer, $j$:

$$y_j(h) = C^{(j)}_{\text{clear}}(mh), \qquad h \in [0, T]$$

Everything interesting about it follows from one derivative.

### The slope

Take the difference of $C_{\text{clear}}$ over one period. The payment $M$ and
the change in balance are both in there, and they nearly cancel:

$$\Delta C_k = \underbrace{M}_{\text{payment}} + \underbrace{\text{prem}_k}_{\text{PMI}} + \underbrace{(B_k - B_{k-1})}_{\text{balance change}}
= M + \text{prem}_k + \big(iB_{k-1} - M\big)$$

$$\boxed{\;\Delta C_k = i B_{k-1} + \text{prem}_k\;}$$

**Holding the loan one more period costs exactly the interest accrued plus the
premium charged.** The payment cancels completely. This is the Part 4 point in
derivative form: principal is a transfer, not a cost, so the portion of $M$ that
retires principal moves money from your pocket into your equity and nets to zero
here. Only interest and insurance leave.

Three consequences, all visible in the chart:

- **It is strictly increasing.** $iB_{k-1} + \text{prem}_k > 0$ for the whole
  term. Holding longer always costs more in nominal dollars.
- **It is concave.** The slope is proportional to $B_{k-1}$, which falls on the
  Part 2 curve, so the curve flattens as the loan amortizes. Early years are the
  expensive ones.
- **It starts at $P + F$.** At $k = 0$ nothing is paid, no premium is charged,
  and $B_0 = P$. Walking away on day one means repaying the principal and eating
  the fees. The vertical spread between curves at $h = 0$ is purely the
  difference in fees.

### The PMI slope discontinuity, quantified

Under the declining basis $\text{prem}_k = \frac{q}{m}B_{k-1}$, so while PMI runs

$$\Delta C_k = B_{k-1}\left(i + \frac{q}{m}\right)$$

and afterwards it is $B_{k-1}\,i$. Comparing the two at the same balance, the
slope falls by

$$\frac{q/m}{\,i + q/m\,} = \frac{q}{r + q}$$

**independent of principal, balance, term, and time.** For a typical
$q = 0.6\%$ against $r = 6.5\%$, that is $0.006/0.071 = 8.5\%$.

Under the fixed basis $\text{prem}_k = \frac{q}{m}P$, a constant, so the slope
falls by that constant amount. The relative drop is not universal — it depends
on how far the loan has amortized by $t_{\text{end}}$:

$$\frac{q P/m}{\,i B_{t_{\text{end}}} + q P/m\,}
= \frac{q\lambda}{\,r\theta + q\lambda\,}, \qquad \lambda = \frac{P}{V}$$

where the second form uses $B_{t_{\text{end}}} \approx \theta V$, valid when the
threshold rule binds rather than the midpoint. It is always the larger of the
two, since the fixed premium never shrank while the balance did. With
$\lambda = 0.91$ and $\theta = 0.80$ on the same rates, $9.5\%$ against $8.5\%$.

That is the whole answer to why $t_{\text{end}}$ is invisible on screen. The
value is continuous (Part 3), so there is no step; the slope changes by under
ten percent at a single point, on a curve that climbs tens of thousands of
dollars across the plot. A few pixels of bend.

### Break-evens

A break-even is **not** where two curves cross. With four offers, two also-ran
curves can cross each other and nothing about the recommendation changes. What
matters is where the winner changes, so the site tracks the pointwise argmin:

$$\text{lead}(k) = \arg\min_j \, y_j(k)$$

and records the $k$ where $\text{lead}$ changes value. Between the two samples
that bracket a change, the gap $d = y_{\text{prev}} - y_{\text{cur}}$ is
interpolated linearly to place the crossing:

$$h^\ast = h_{k-1} + \frac{d_{k-1}}{d_{k-1} - d_k}\,(h_k - h_{k-1})$$

Two filters keep the result honest. A lead change is ignored unless the new
leader is ahead by more than half a dollar, so floating-point noise is not
reported as a crossing — the same tie window the verdict text uses. And a
leader must hold the lead for at least 2% of the plotted range to be labeled:
when two offers differ mainly in fees, the curves are nearly coincident at the
start and the argmin can flicker between them many times before settling.

Economically the picture is simple. At $h = 0$ the ranking is by fees alone. As
$h$ grows the rate difference accumulates against that fixed head start, and the
break-even is where it has been repaid.

### Sampling

`horizon()` rounds its argument to a whole number of periods,
$k = \mathrm{round}(mh)$. Sampling the curve on an evenly spaced pixel grid
would therefore land many adjacent samples on the same $k$ and produce a visible
staircase. The site instead places a vertex at every scheduled payment,
$h = t/m$, which is the natural grid for a function that is only defined there.
For long terms it strides to keep the vertex count bounded.

The break-even search uses a separate uniform grid, since it is looking for
sign changes in a difference rather than drawing a shape.
