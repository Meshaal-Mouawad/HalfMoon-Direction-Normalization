# 03_Elias_Veyron_Counterexample_Tests.md

Reviewer: Elias Veyron  
Review ID: HM-IV-2026-01  
Manuscript: Global loss bounds and one-bit recovery for direction-normalized half-moons  
Author: Meshaal Mouawad  
Review scope: Independent mathematical verification

## Finite-origin searches

The following tests use equal priors and the area-uniform law, with the exact open supports `a<radius<b` and strict diameter inequalities. Each number is an independently integrated **excess Bayes-risk probability** `Δ(c)`, using 8,192 deterministic midpoint angular cells and exact circle/diameter intersections on each representative ray. These are finite numerical searches; the proof that **every** origin has positive loss is in report 02.

| Geometry and origin `c` | Origin category | Observed `Δ(c)` | Attempted counterexample outcome and interpretation |
|---|---|---:|---|
| `h=0.5`, `(1,0.25)` | Inside class-0 support | `0.1012897866` | No zero-loss origin found; the direction at `c` itself is immaterial because it has zero probability. |
| `h=0.5`, `(2,0.25)` | Inside class-1 support | `0.1008443236` | No zero-loss origin found. |
| `h=0.5`, `(0.8,0)` | On class-0 inner-circle/diameter boundary | `0.0985409711` | No zero-loss origin found; open-boundary membership was applied. |
| `h=0.5`, `(0,0)` | Outside both supports, class center | `0.1185767084` | No zero-loss origin found; agrees with the preserved fixed-origin risk within the stated numerical tolerance. |
| `h=0.5`, `(0.5,0.25)` | Outside both supports, midpoint | `0.1074792622` | No zero-loss origin found; this is the one-bit construction's direction-only baseline. |
| `h=0.5`, `(0,3)` | Outside both supports, upper origin | `0.2115091712` | No zero-loss origin found. |
| `h=0.5`, `(0.5,10.25)` | Distant origin | `0.2228036538` | Positive loss persists in this sampled view. |
| `h=0.5`, `(0.5,100.25)` | More distant origin | `0.2236859750` | Positive loss persists; this does not prove uniform convergence. |
| `h=0.5`, `(0.5,1000.25)` | Most distant sampled origin | `0.2236934887` | Positive loss persists; the limiting theorem is proved separately. |
| `h=1`, `(1,0.25)` | Inside a class-exclusive support region | `0.1323660064` | No zero-additional-loss origin found, despite positive raw overlap risk. |
| `h=1`, `(0.8,0)` | On support boundary | `0.1489079696` | No zero-additional-loss origin found. |
| `h=1`, `(0,0)` | Outside both open supports | `0.1501397367` | No zero-additional-loss origin found. |
| `h=1`, `(0.5,0.5)` | Midpoint, outside both supports | `0.1413908639` | No zero-additional-loss origin found. |
| `h=1`, `(0,3)` | Upper external origin | `0.1388320425` | No zero-additional-loss origin found. |
| `h=1`, `(0.5,10.5)` | Distant origin | `0.1561216768` | Positive additional loss persists. |
| `h=1`, `(0.5,100.5)` | More distant origin | `0.1565320437` | Positive additional loss persists. |

The `h=1` values exclude the independently recalculated raw overlap risk `R*_X=0.06715749549`; the directional risk is their sum. The `h=0.5` raw risk is zero. The far-origin integration narrows its angular domain using a ball containing both supports, avoiding a coarse full-circle grid. None of these finitely many values certifies a global minimum.

## Configuration and support-boundary challenges

| Parameters and assumptions | Test and result | Mathematical interpretation |
|---|---|---|
| `h=0.78>√(3/5)≈0.7745966692`, `x=(0.81,0.0001)` | Strict membership checks place `x` in both open supports. | The manuscript's disjoint upper limit is locally sharp; it cannot be extended to this larger `h`. |
| `h=1`, `x=(0.9,0.1)` | Squared radii from both centers equal `0.82∈(0.64,1.44)` and the height inequalities hold. | A positive-area neighborhood overlaps, so the raw Bayes risk is strictly positive under positive-a.e. densities. |
| `h=0.5`, `x₀=(1,0.25)∈S₀`, `x₁=(2,0.25)∈S₁`, `c=(0.5,0.25)` | Both normalized directions are `(1,0)`, at radii `0.5` and `1.5`. | This is a valid collision but alone has zero population probability; the angular-overlap proof is needed. |
| `h=0.5`, `(6/5,0)` and `(x*,y*)` | Both are excluded by strict support inequalities; `x*=(63−2√1671)/181`, `y*=(350+9√1671)/905`. | Their exclusion permits equality at the sharp threshold endpoints. |
| `h=−0.25`, origins `(0,0)` and `(0.5,−0.125)` | Calculated cancellation loss is exactly zero at the sampled angular cells. | This matches the separate vertical-sign preservation proof and prevents extending the positive-loss claim to nonpositive displacement. |

## Fixed-decoder and radius-error adversarial tests

The code checked 138,240 distinct open-support points on a deterministic midpoint polar grid, reflected across the class midpoint. Six thresholds—`α`, `0.75`, `t*`, `0.8`, `0.81`, and `β`—produced 829,440 decoder evaluations and zero errors. This grid supports implementation consistency only; the complete continuous-support verdict rests on the inequalities in report 02.

| Attempt | Parameters and strict membership | Actual result | Interpretation |
|---|---|---|---|
| Below `α` | `t=α−10⁻⁴≈0.7432034374`, class-0 point `(1.1999999,10⁻⁷)∈S₀`, radius `0.7433033096>t` | Far rule returns class 1. | A strict counterexample exists to any claim that this fixed decoder works below `α`. Its inequalities persist on an open neighborhood. |
| Above `β` | `t=β+10⁻⁴≈0.8121914734`, class-0 point `(-0.1036307711,0.7932595193)∈S₀`, radius `0.8120966772<t` | Near rule returns class 1. | A strict counterexample exists above `β`, again with an open erroneous neighborhood. |
| Radius error exceeding lower margin at `t=0.8` | Use the below-`α` point and constant `e=0.8−(α−10⁻⁴)` | The measured bit selects the erroneous far rule. | The `t−α` side of the robust tolerance condition is sharp. |
| Radius error exceeding upper margin at `t=0.8` | Use the above-`β` point and constant `e=0.8−(β+10⁻⁴)` | The measured bit selects the erroneous near rule. | The `β−t` side is sharp. |

For `t=α` or `t=β`, the source optimizers lie on excluded support boundaries and the proof shows strict safety at every included point. The perturbation guarantee concerns worst-case additive error in radius with exact direction; the numerical tests do not replace that universal argument.
