# 09_Elias_Veyron_Final_Decision.md

Reviewer: Elias Veyron  
Review ID: HM-IV-2026-01  
Manuscript: Global loss bounds and one-bit recovery for direction-normalized half-moons  
Author: Meshaal Mouawad  
Review scope: Independent mathematical verification

## 1. Overall Mathematical Verdict

**PASS.** The independently checked principal mathematical claims follow from the stated assumptions. The ray-cancellation identity, all-finite-origin loss in both evaluated geometries, uniform projection limit, compactified positive global-loss criterion, constructive whole-plane certificate, one-bit support decoder, sharp threshold interval, and bounded-radius-error guarantee have valid derivations. No demonstrated mathematical failure or counterexample appears in the completed scope. Mathematical correctness is distinct from the status of full experimental retraining and manuscript production inspection below.

## 2. Verified Theorems

| Theorem or calculation | Verdict | Decisive basis |
|---|---|
| Binary Bayes-risk ray-cancellation identity and class-density model | PASS | Polar Jacobian, signed-density pushforward, and binary `min` identity independently derive `Δ(c)=∫min(A_c,B_c)dθ`. |
| Disjoint support transition `0<h≤√(3/5)` and positive loss at every finite origin | PASS | Horizontal interval inequalities prove disjointness; connected opposite-sign regions with mutual convex-hull intrusion force positive angular cancellation. |
| `h=1` positive raw overlap and positive additional loss at every finite origin | PASS | An open common-support neighborhood gives raw risk; cleared connected exclusive backbones satisfy the same intrusion criterion. |
| Uniform projection-risk limit for absolutely continuous binary populations in `ℝⁿ`, `n≥2` | PASS | Uniform smooth-support dilation estimate plus a direction-independent `L¹` approximation and signed-pushforward contraction. |
| Exact global-floor criterion and half-moon global positivity | PASS | Finite-origin continuity, projection-direction continuity, and uniform convergence at the compactified boundary; every projected pair of winner regions overlaps on an interval. |
| Constructive global lower-bound proposition and four evaluated certificates | PASS | Compact and exterior lower estimates cover every origin; exact rational interval computation reproduces the downward-rounded area and radius values at `h=0.5` and `h=1`. |
| Fixed one-bit decision recovery at `h=0.5`, midpoint origin | PASS | Strict support inequalities exclude wrong angular-rule assignment on both radial bins; reflection handles class 1. |
| Sharp threshold interval `[α,β]` and bounded-radius-error guarantee | PASS | Exact excluded boundary optimizers prove endpoint values; strict open-support error sets outside the interval establish necessity; effective-threshold argument establishes robustness. |
| One additional radial bit is minimal for this exact-direction geometry | PASS | Every zero-bit direction-only origin has positive risk, while the displayed bit has zero risk. |
| Supplementary finite preservation test, radial primitives, density-ratio and BV truncation bounds | PASS | Event-cell sign constancy, direct differentiation, pointwise density comparison, and variation-based midpoint bounds. |

## 3. Failed Theorems or Calculations

None demonstrated. The issue register has no rows.

## 4. Unverified Claims

The archived 500 candidate neural fits and 250 selected evaluations were not freshly trained; **fresh training reproducibility is NOT VERIFIED**. The original 18 Arb fixed-origin integrations and two Arb raw-risk enclosures were not rerun with Arb; **fresh execution of those historical enclosures is NOT VERIFIED**. Their frozen records were inspected and the area-law fixed-origin values were independently approximated, but those checks do not reproduce the full certified Arb pipeline. The global constructive certificate was independently recalculated and is PASS.

## 5. Computational Reproduction Results

The independent program completed **24 deterministic checks, zero failures**, with no random seed. Exact rational interval arithmetic reproduced the four whole-plane loss-probability certificates:

| `h` | Area lower bound | Radius lower bound |
|---|---:|---:|
| `0.5` | `0.0002050842462841` | `0.0001709035385701` |
| `1` | `0.0000119104106520` | `0.0000099253422100` |

It enclosed `α=0.743303437365925276…` and `β=0.812091473357641004…`, verified the sharp outside-threshold counterexamples, and evaluated 829,440 grid decoder cases without error. The research archive passed ZIP integrity. All 500,000 frozen one-bit observations satisfied their declared open supports. Replaying the fixed decoder at six thresholds gave zero errors; saved prediction-array comparisons reproduced `54,362` direction-only, `3` one-bit network, `0` raw-coordinate, `0` full-radius, and `0` analytic-decoder errors. Finite origin searches were positive at every sampled disjoint and overlapping geometry point, including interior, boundary, exterior, and increasingly distant origins. Their role is diagnostic; the universal verdict rests on proof.

## 6. Literature and Contribution Assessment

The eight required works were checked against scholarly primary records. General decision sufficiency and excess-risk theory precede this manuscript; geometric wedge separation, radial-projection viewpoints, invariant compression, and normalization-sensitive empirical results are also established contexts. The source-verified scientific distinction is the combined moving-origin binary ray identity, uniform total-variation risk limit, all-origin half-moon theorem, constructive whole-plane bounds, and sharp one-bit fixed-decoder recovery. The comparison supports this **scoped** contribution statement and does not assert exhaustive novelty over all literature.

## 7. Required Corrections

No correction to a theorem, equation, numerical whole-plane certificate, support definition, or fixed decoder was demonstrated. No scientific source was edited.

## 8. Final Publication Readiness Decision

**NOT VERIFIED overall.** Mathematical correctness of the checked theorems and whole-plane constants is **PASS**; frozen experimental-record consistency is **PASS**. Complete fresh neural-training reproduction, the historical Arb runs, and full visual production inspection remain **NOT VERIFIED**. The source package and compiled 31-page PDF passed identity and basic renderability checks. These separate statuses prevent a broader publication-readiness PASS from being inferred from the mathematical verdict alone.

## 9. Verification Limitations

The available runtime lacks `numpy`, `torch`, and `python-flint`, which the original training and Arb workflows require. The frozen arrays and summary were read directly and replayed with a standard-library implementation, but the complete fitting procedure and Arb ball sums were not run. The literature assessment covers the eight specified works with direct records; it is not an exhaustive field survey. Numerical angular grids, including distant-origin values, do not prove continuous-support or whole-plane statements. The PDF identity and page count were checked, but every figure and page layout was not visually inspected.
