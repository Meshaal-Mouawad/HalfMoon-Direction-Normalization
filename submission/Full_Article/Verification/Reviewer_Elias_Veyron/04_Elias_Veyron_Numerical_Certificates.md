# 04_Elias_Veyron_Numerical_Certificates.md

Reviewer: Elias Veyron  
Review ID: HM-IV-2026-01  
Manuscript: Global loss bounds and one-bit recovery for direction-normalized half-moons  
Author: Meshaal Mouawad  
Review scope: Independent mathematical verification

## Certificate construction and exact assumptions

`constructive_global_floor_supplement.tex` lines 4–56 proves that compact connected cores with opposite signed-density margins `κ₊,κ₋` on open radius-`ρ` neighborhoods, mutual convex-hull intrusion, common convex-hull disk `B(p,δ)`, and extent `M` satisfy, for every `C>M`,

`inf_c Δ(c) ≥ κ min{√3ρ³/[2(C+M)], 4ρδ(1−M/C)}`, where `κ=min(κ₊,κ₋)`.

The first term covers every `|c−p|≤C`, including origins within a core. The second covers every `|c−p|>C`. It follows from a positive angular interval of simultaneous signed ray mass; no origin grid enters the proof. Equality of the two terms gives

`C*=[√3ρ²+√(3ρ⁴+256δ²M²)]/(16δ)`.

The exact arithmetic and source geometry were checked independently as follows.

### Disjoint geometry, `h=1/2`

Take `ρ=δ=1/8`, `p=(1/2,1/4)`, `M=43/40+√5/4`, `K₀={a+ρ≤|x|≤b−ρ, x₂≥ρ}`, and `K₁=(1,1/2)−K₀`. Each open radius-`ρ` disk about `Kᵢ` stays inside its support: its center is at least `ρ` above the diameter and at least `ρ` from either radial boundary; strict support inequalities hold throughout the open disk. The cores are compact and connected. Their convex hulls are the outer circular caps of radius `b−ρ=43/40` and opposing half-plane heights. The disk `B(p,1/8)` lies inside both: its heights are between `1/8` and `3/8`, while `|p|+δ=√5/4+1/8<43/40`. Every core point is within `M` of `p`. `(1,1/4)∈K₀∩int conv(K₁)`, and reflection supplies the reverse intrusion. The supports are disjoint, so the signed margins have no opposing contribution.

### Overlapping geometry, `h=1`

Take `ρ=1/20`, `δ=1/8`, `p=(1/2,1/2)`, `M=11/10+1/√2`, and the reflected connected backbones in `supplement_theory.tex` lines 119–154. On the right radial segment, squared distance to the other center decreases from `9/16`, so its open radius-`1/20` disk remains inside the other class's inner hole of radius `4/5`. On the right circular branch below height `21/20`, squared distance is at most `321/100−11/√17<9/16`, giving the same clearance. On the central arc at height at least `21/20`, the disk stays above the other class's diameter. On the left branch below that height, horizontal separation from the other center exceeds `1+√43/20>5/4=b+ρ`. The left radial segment is farther still. Every backbone center has own-class radius between `√401/20` and `11/10` and height at least `1/20`, so its open disk stays in the own support. These cases verify a strict exclusive neighborhood for each sign, despite the original support overlap.

The triangle with vertices `w₁=(1,1/4)`, `w₂=(−1,1/20)`, `w₃=(0,11/10)` contains `p` with barycentric weights `(45,7,24)/76`. Its three edge distances from `p` are `3/√101`, `7/(2√689)`, and `45/58`, all greater than `1/8`; hence the common disk is inside both reflected convex hulls. The barycentric identity for the opposite point has coefficients `(7/38,7/38,12/19)`, all positive. Backbone extent is at most `M` by the triangle inequality. Thus all hypotheses of the whole-plane proposition hold.

## Density margins and certified values

For equal-prior area sampling, `κ=(1/2)/H=5/(4π)`. For equal-prior radius-uniform sampling, `fᵢᴿ≥1/[π(b−a)b]` on its support, giving `κ=25/(24π)`. Both statements use probability densities per unit area. The four global values below are **loss probabilities**. Multiplication by 100 converts each to percentage points of excess risk.

| `h` | Law | `M` | `C*` | Independently enclosed whole-plane loss probability | Manuscript downward bound | Verdict |
|---|---|---:|---:|---:|---:|---|
| `1/2` | Area | `1.63401699437494742410…` | `1.64760466959097963498…` | `[0.0002050842462841467794946942559205943292380, 0.0002050842462841467794946942559205943292381]` | `0.0002050842462841` | PASS |
| `1/2` | Radius | same | same | `[0.0001709035385701223162455785466004952743650, 0.0001709035385701223162455785466004952743651]` | `0.0001709035385701` | PASS |
| `1` | Area | `1.80710678118654752440…` | `1.80927314165819333798…` | `[0.00001191041065202725492361730933657512437245, 0.00001191041065202725492361730933657512437246]` | `0.0000119104106520` | PASS |
| `1` | Radius | same | same | `[0.000009925342210022712436347757780479270310380, 0.000009925342210022712436347757780479270310381]` | `0.0000099253422100` | PASS |

The calculation used exact rational arithmetic, 48-place outward rational square-root bounds, and alternating-series rational bounds on `π=16 atan(1/5)−4 atan(1/239)`. The program records the exact interval operations and the output intervals in reports 05–06. For `h=1/2`, the area bound is `0.0205084246284147…` percentage points and the radius bound is `0.0170903538570122…` percentage points. For `h=1`, they are `0.0011910410652027…` and `0.0009925342210023…` percentage points. The manuscript's “exceed `0.0205` pp” and “exceed `0.00119` pp” statements are numerically correct. These conservative bounds do not estimate the minimizing origin or equal a fixed-origin Bayes risk.

## Threshold and radius-error certificates

Direct substitution of the two geometric boundary optimizers gives

`α=√221/20 ∈ [0.7433034373659252761306004106965698325724, 0.7433034373659252761306004106965698325725]`,

`β=√[(29761+440√1671)/72400] ∈ [0.8120914733576410044336209653271520549372, 0.8120914733576410044336209653271520549373]`.

The `β` optimizer is `x*=(63−2√1671)/181`, `y*=(350+9√1671)/905`, lying on the excluded inner circle and near-score boundary. The `α` optimizer `(6/5,0)` lies on the excluded outer circle and diameter. These facts make both threshold endpoints admissible and sharp for the fixed decoder. The exact-radius experimental threshold `0.8` lies strictly between them.

The maximum robust tolerance at `t=0.8` is `β−0.8=0.01209147335764100443…` coordinate units. The unique tolerance-maximizing threshold is `t*=(α+β)/2=0.77769745536178314028…`, with `ε*=(β−α)/2=0.03439401799585786415…` coordinate units. Report 06 stores floating diagnostic values as well as certified endpoint enclosures; the rounded float values are not substituted for the exact identities.

## Fixed-origin numerical comparison

The independent deterministic area-law ray integration gives at `h=1/2`: `Δ(0,0)=0.1185767084`, `Δ(1/2,1/4)=0.1074792622`, and `Δ(0,3)=0.2115091712`, within `0.0001` probability of the published directional risks. For `h=1`, independent horizontal overlap integration gives `R*_X=0.06715749549`; adding the independently integrated cancellation loss reproduces the three published area-law directional risks within `0.0001` probability. These integrations are numerical diagnostics, not certified bounds. The rigor of the all-origin certificate comes from the geometric hypotheses and interval-enclosed formula above.
