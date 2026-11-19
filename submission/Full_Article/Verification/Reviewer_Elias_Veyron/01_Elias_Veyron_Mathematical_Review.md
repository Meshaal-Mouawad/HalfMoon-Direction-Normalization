# 01_Elias_Veyron_Mathematical_Review.md

Reviewer: Elias Veyron  
Review ID: HM-IV-2026-01  
Manuscript: Global loss bounds and one-bit recovery for direction-normalized half-moons  
Author: Meshaal Mouawad  
Review scope: Independent mathematical verification

## Overall mathematical evaluation

**Mathematical verdict: PASS for the independently derived principal theorems and numerical whole-plane certificate.** No counterexample or invalid inference was demonstrated. The exact signed-ray identity, all-finite-origin geometry, uniform projection limit, compactified global-loss criterion, constructive lower bound, fixed one-bit decoder, sharp threshold interval, and bounded-radius-error guarantee follow under their stated assumptions. The proof and calculation details are in reports 02–04. This verdict does not substitute the finite origin search for universal proof.

The controlling manuscript is remote `main` commit `42e857497e4d6988f8e1178a9b91a7e45902dcc6`, `submission/Full_Article/Full_Manuscript.tex`; `Full_Theory.tex` and the exact-matching contents of `Full_Article_Source.zip` provide the mathematical source. The local `main` checkout was older (`83d4a4dd98f503049bc8b1abfcbd07a326a8d522`), so the authoritative remote source was read in disposable temporary storage. The original V11 research release was inspected directly. No earlier favorable review served as proof evidence.

## Exact theorem findings

| Claim and source | Required assumptions | Verdict | Independent finding |
|---|---|---|---|
| Binary model and ray-cancellation identity, `Full_Theory.tex` lines 8–35; `supplement_theory.tex` lines 6–50 | Two positive priors summing to one; planar integrable class densities; measurable direction map away from its null center point. | PASS | Polar Jacobian `r`, class angular densities, signed decomposition and `min` identity give `Δ(c)=∫min(A_c,B_c)dθ`. `A_c,B_c` are per-angle densities, not single-ray probabilities. |
| Disjoint range and finite-origin loss, `Full_Theory.tex` lines 37–52; `supplement_theory.tex` lines 52–112 | Open half-annuli with `a=0.8`, `b=1.2`, `0<h≤√(3/5)`; positive priors and positive-a.e. support densities. | PASS | Horizontal slices are disjoint through the endpoint; connected opposite-sign regions mutually intrude into convex hulls, forcing positive angular cancellation from every finite origin. Raw risk is zero. |
| Overlapping `h=1` finite-origin result, `supplement_theory.tex` lines 114–158 | Same half-annuli, `h=1`, positive priors and positive-a.e. support densities. | PASS | An open raw overlap gives `R*_X>0`. Cleared, connected exclusive backbones satisfy mutual hull intrusion and give `Δ(c)>0` for every finite origin. |
| Uniform distant-origin projection limit, `projection_limit_supplement.tex` lines 7–60 | Absolutely continuous binary population on `ℝⁿ`, `n≥2`, with `L¹` class densities and fixed positive priors. | PASS | A smooth compact-support dilation estimate is uniform in direction; one direction-independent `L¹` approximation and pushforward contraction extend it to all `L¹` signed densities. |
| Exact positive global-floor criterion and half-moon corollary, `projection_limit_supplement.tex` lines 62–89 | Previous theorem plus finite and projected positive-loss hypotheses; half-moon corollary uses planar connected open winner regions with mutual interior hull intrusion. | PASS | Translation/rotation continuity and uniform boundary convergence extend loss to a compact closed ball. Projection intervals overlap in every direction, giving strictly positive loss at every boundary point. |
| Constructive global floor and four constants, `constructive_global_floor_supplement.tex` lines 4–91 | Connected opposite-sign cores with `ρ` clearance, `κ` margins, common hull disk `δ`, extent `M`, and mutual hull intrusion; specified study laws for numerical values. | PASS | Compact and exterior ray-mass estimates cover the whole plane. Exact rational interval evaluation reproduces all four downward-rounded loss-probability certificates. |
| One-bit recovery and minimal added radial bit, `Full_Theory.tex` lines 99–108; `one_bit.tex`; `Threshold_Addendum.tex` | `h=0.5`, midpoint `(0.5,0.25)`, exact direction, fixed near/far angular rules, open supports; minimality among additional finite-valued radial codes. | PASS | Support inequalities put every near-rule error beyond `β` and every far-rule error below `α`. A one-bit threshold in `[α,β]` is exact; zero added radial bits retain positive direction-only loss. |
| Sharp threshold interval and radius-error tolerance, `Threshold_Addendum.tex` lines 20–112 | Same fixed decoder and origin; additive radius error bounded by `ε`; exact direction. | PASS | Both excluded boundary optimizers and open strict counterexamples establish `α≤t≤β` and `α+ε≤t≤β−ε` as sharp. The stated experimental and maximum-tolerance thresholds reproduce. |
| Finite preservation arrangement, radial primitives, density-ratio comparison and BV truncation lemmas, `supplement_theory.tex` lines 237–486 | The specified circle/line geometry and study laws; compact support and BV where stated. | PASS | Event directions preserve sign patterns between cells; primitive differentiation, `5/6`–`5/4` density ratio, and variation-based midpoint error bounds check algebraically. |

## Numerical and experimental reproducibility

The independent standard-library program executed **24 checks with no failures**. Its exact rational enclosures verify the four whole-plane values; 138,240 constructed open-support points yielded 829,440 decoder evaluations without error. Finite area-law origin searches included origins inside supports, on boundaries, outside, and as far as 1,000 units from the population. These searches do not establish the universal theorems.

The V11 release archive passed ZIP integrity inspection. The ten frozen one-bit test arrays contain **500,000 observations**, all inside their declared class supports. Direct decoder replay at six thresholds produced zero errors. Direct comparison of the saved prediction arrays with labels reproduced `54,362` midpoint direction-only network errors, `3` one-bit network errors, `0` raw-coordinate network errors, `0` full-radius network errors, and `0` saved analytic-decoder errors, matching the archived summary and the manuscript's reported totals. Independent approximate area-ray integration matched the published fixed-origin risks within `0.0001` probability, and horizontal integration matched the `h=1` raw area risk.

The full 500-fit training procedure and all 18 original Arb fixed-origin enclosures were **NOT VERIFIED by fresh execution**. The available Python environment lacks `numpy`, `torch`, and `python-flint`; installing them would create permanent files outside the nine-file destination. The archived evidence was checked directly, and the principal whole-plane constants were independently certified using standard-library rational arithmetic. This separates frozen-record consistency from fresh model or Arb reproduction.

## Literature, contribution and production assessment

The eight specified scholarly works were checked against publisher, proceedings, or author full-text records. They establish relevant precedents in decision sufficiency, excess risk, invariant compression, radial projection geometry, wedge separation, and normalization-sensitive empirical behavior. The manuscript's contribution is the verified combination of a moving-origin ray-loss identity, uniform Bayes-risk projection limit, all-origin half-moon geometry, explicit whole-plane certificates, and a sharp fixed one-bit decision repair. Report 07 gives the paper-by-paper comparison and its limits.

The supplied full PDF opens as a 31-page A4 document; the standalone `Full_Manuscript.tex` and `Full_Theory.tex` bytes match their copies in the source ZIP. These checks establish package identity and basic renderability. A complete visual typography, figure, and production inspection was not performed. No original manuscript, proof, experiment, table, figure, reference, or archived result was changed.
