# 02_Elias_Veyron_Proof_Verification.md

Reviewer: Elias Veyron  
Review ID: HM-IV-2026-01  
Manuscript: Global loss bounds and one-bit recovery for direction-normalized half-moons  
Author: Meshaal Mouawad  
Review scope: Independent mathematical verification

## Sources and conventions

The controlling text is remote `main` commit `42e857497e4d6988f8e1178a9b91a7e45902dcc6`, `submission/Full_Article/Full_Manuscript.tex` and `Full_Theory.tex`. The identical source copies in `Full_Article_Source.zip`, especially `supplement_theory.tex`, `projection_limit_supplement.tex`, `constructive_global_floor_supplement.tex`, `one_bit.tex`, and `Threshold_Addendum.tex`, supply the complete proofs. Their identities were checked against the standalone source files. The original release supplies frozen experimental records. Earlier review judgments were not used as proof.

Write `d=π₀f₀−π₁f₁`, `d₊=max(d,0)`, `d₋=max(−d,0)`, and `Δ(c)=R*_{T_c}−R*_X`. Priors are positive and sum to one. Unless a result explicitly narrows the class, class densities are Lebesgue densities in `L¹`.

## 1. Model and exact ray cancellation — PASS

For `a=4/5`, `b=6/5`, `m₀=(0,0)`, and `m₁=(1,h)`, the supports are `S₀={a<|x|<b, x₂>0}` and `S₁={a<|x−m₁|<b, x₂<h}`. Each has area `H=π(b²−a²)/2=2π/5`. Therefore `fᵢᴬ=1_{Sᵢ}/H` integrates to one. Independent uniform radius on `(a,b)` and uniform semicircle angle give joint polar density `1/[π(b−a)]`; dividing by the center-based Jacobian `s` gives `fᵢᴿ(x)=1_{Sᵢ}(x)/[π(b−a)|x−mᵢ|]`. Open support boundaries have zero probability under both laws. `T_c(x)=(x−c)/|x−c|` is defined away from `c`; the single exceptional point has zero probability.

With `x=c+r uθ`, planar Lebesgue measure is `r dr dθ`. Thus `qᵢ,c(θ)=∫₀∞ fᵢ(c+r uθ)r dr` is the class-conditional **density per unit angle**, with `∫₀²π qᵢ,c(θ)dθ=1`. It is not the mass of a zero-width ray. Binary zero-one Bayes risk is

`R*_X=∫ min(π₀f₀,π₁f₁)dx=(1−∫|d|dx)/2`,

and the directional risk is

`R*_{T_c}=∫ min(π₀q₀,c,π₁q₁,c)dθ=(1−∫|∫₀∞d(c+r uθ)rdr|dθ)/2`.

Define `A_c(θ)=∫₀∞d₊(c+r uθ)rdr` and `B_c(θ)=∫₀∞d₋(c+r uθ)rdr`. Tonelli applies to the nonnegative integrands, and `d∈L¹` makes both angular densities finite almost everywhere. Because `|d|=d₊+d₋` and the directional signed density is `A_c−B_c`, subtraction gives

`Δ(c)=½∫[A_c+B_c−|A_c−B_c|]dθ=∫min(A_c,B_c)dθ`.

Consequently `Δ(c)=0` precisely when `A_c B_c=0` for almost every angle. A collision on one ray alone has no probability consequence. These steps verify `Full_Theory.tex` lines 8–35 and `supplement_theory.tex` lines 6–50. The identity requires absolute continuity for the displayed ray densities; the signed-pushforward form below extends to other measures with appropriate definitions.

## 2. Finite-origin all-loss geometry — PASS

For `0<h≤√(3/5)`, a possible common point has `0<y<h`. Put `s(y)=√(a²−y²)` and `t(y)=√(b²−y²)`. The two class-0 horizontal bands are `(-t(y),−s(y))` and `(s(y),t(y))`; class 1 has `(1−t(h−y),1−s(h−y))` and `(1+s(h−y),1+t(h−y))`. The function `t(h−y)−s(y)` is increasing, so it is at most `b−s(h)≤1`. The corresponding reversed bound separates the right bands. Concavity of `s` gives `s(y)+s(h−y)≥a+s(h)≥1`, separating the potentially crossing middle pair. The fourth pair is ordered automatically. Equality at `h=√(3/5)` permits boundary contact only, because the supports are open. For `√(3/5)<h<a`, the middle bands overlap for sufficiently small positive `y`; the stated disjoint transition is sharp within that regime.

Each `Sᵢ` is open and connected. Its convex hull is the open outer half-disk. The class-0 point `(1,h/2)` has radius `√(1+h²/4)∈(a,b)` and is interior to `conv(S₁)`; reflection about `(1/2,h/2)` gives the reverse intrusion. The winner regions have opposite signs because the supports are disjoint, so `R*_X=0` for all positive priors and positive-a.e. support densities.

The geometric lemma is independently checked as follows. For an open connected winner set `U`, its directional image from `c` is open and connected on the circle; if `c∈U` it is the entire circle. Suppose two images were disjoint. Both must then be arcs, and one arc has length at most `π`. The positive cone over that arc is convex and contains the translated convex hull of its winner set. A point of the opposite winner set inside that convex hull would have a direction in both images, contradiction. Therefore the images overlap in a nonempty open angular arc. Each ray in that arc meets open intervals of both signs, giving `A_c,B_c>0` for almost every angle there by polar Fubini and positivity almost everywhere. The ray identity yields `Δ(c)>0`, including origins inside a support, on its boundary, and outside both supports. This is a universal geometric argument; the numerical origin search in report 03 is only a diagnostic.

For `h=1`, `(9/10,1/10)` has squared distance `82/100` from both centers, so an open overlap has positive raw Bayes risk. To prove **additional** loss, use the exclusive connected backbones `K₀,K₁` of `supplement_theory.tex` lines 119–154. Their radius-`1/20` open neighborhoods remain in opposite exclusive support regions. The four clearance cases are checked in report 04. The identity `v₁=(7/38)w₁+(7/38)w₂+(12/19)w₃` has positive coefficients and noncollinear `wᵢ`, placing `v₁` inside `conv(K₀)`; reflection supplies reverse intrusion. The same angular lemma gives `R*_{T_c}>R*_X>0` for every finite `c`, for any positive priors and densities positive almost everywhere on the supports. For `h≤0`, origins with `h≤c₂≤0` preserve the label by the sign of the vertical direction; this is a valid boundary control.

## 3. Uniform projection limit and global criterion — PASS

For any measurable representation `F`, let `F#d` be the pushed signed measure and use the norm `||F#d||TV` equal to its total variation mass. Then `R*_F=(1−||F#d||TV)/2`, and `||F#(d−g)||TV≤||d−g||₁`. This verifies the risk and contraction formulas in `projection_limit_supplement.tex` lines 7–14.

First take `g∈C∞_c(B(p,M))`, `R>M`, and coordinates `x=p+s e+t` with `t⊥e`. Every observed direction lies in the hemisphere `e·u<0`. The invertible slope coordinate `z=−R P_eu/(e·u)` equals `t/(1−s/R)`. With `k=n−1` and `a_s=1−s/R>0`, its signed pushforward density is `Q_Rg(z)=∫a_s^k g(p+s e+a_s z)ds`; orthogonal projection has density `Q_∞g(z)=∫g(p+s e+z)ds`. The slope and direction are measurably bijective on this hemisphere, hence have equal signed total variation.

For `D_a w(z)=a^k w(az)`, differentiation in `log a` and change of variables yield `||D_a w−w||₁≤|log a| ||kw+t·∇w||₁`. On the support, `|s|,|t|≤M` and `|log(1−s/R)|≤M/(R−M)`. Integrating over `s` gives the **direction-independent** bound

`||Q_Rg−Q_∞g||₁ ≤ M[(n−1)||g||₁+M||∇g||₁]/(R−M)`.

For arbitrary `d∈L¹`, choose one smooth compactly supported `g` with `||d−g||₁<η`, independently of `e`. The two pushforward contractions add at most `2η` to the difference of total-variation norms. Taking the supremum over `e`, then `R→∞`, then `η→0`, proves the displayed uniform risk limit. No bounded support, differentiability, or bounded variation is needed for this qualitative theorem; **absolute continuity**, `n≥2`, and integrable class densities are the operative assumptions. Pointwise convergence was not substituted for uniform convergence.

Finite-origin continuity follows by translating `d` in `L¹` before applying the fixed direction map, then using contraction. Projection-risk continuity in `e` follows by rotating `d` in `L¹`; the scalar norm is independent of the chosen orthonormal basis of `e⊥`. Under `c−p↦(c−p)/(1+|c−p|)`, finite origins fill the open unit ball and directions at infinity fill its boundary. The uniform limit makes the risk loss continuous on the closed ball. Compactness then proves `inf_c Δ(c)>0` iff every finite-origin loss and every limiting projection loss is positive. The finite origins are dense, so their infimum equals the completed minimum. This verifies Theorems S1 and S2.

For planar connected open winner regions with mutual interior convex-hull intrusion, each orthogonal projection is an open interval. Projecting an intrusion point places it in both intervals, hence their intersection contains an open interval. Fubini and almost-everywhere strict signs give opposing signed line masses for almost every coordinate in that interval, so each projection loss is positive. Combining this with the finite-origin lemma and compactification proves the positive global infimum for each fixed `0<h≤√(3/5)` and for `h=1`. The positive bound depends on the chosen priors and densities; no uniform lower bound over all such populations is asserted.

The separate explicit rate in `projection_limit_supplement.tex` lines 90–106 additionally assumes compact support in `B(p,M)` and finite total variation `|Dd|(ℝⁿ)`. Mollification preserves the required variation bound and gives the stated `M/[2(R−M)]` risk estimate. For area-uniform half-annuli, the perimeter calculation gives `|Dd|≤5+2/π` and `||d||₁≤1`; the bound is valid though conservative.

## 4. Constructive whole-plane floor — PASS

The proposition's assumptions are two compact connected cores with opposite signed-density margins on radius-`ρ` neighborhoods, mutual convex-hull intrusion, a common radius-`δ` disk in both convex hulls, and extent at most `M` from `p`. Mutual intrusion forces one positive ray through both cores for every finite origin. If its two core points are at radii `rᵢ`, their opposite-sign neighborhood disks are disjoint, so `D=max rᵢ≥2ρ`. On the angular interval `|φ|≤asin(√3ρ/(2D))`, each disk contributes at least `κᵢρ²/2` signed mass per unit angle. Integrating its minimum gives `Δ(c)≥√3κρ³/(2D)`, and hence the compact-region term for `|c−p|≤C`.

For `t=|c−p|>C>M`, connectedness and strict separation make each core's angular image equal to its convex hull's image. Every ray through the common disk crosses both cores. Its angular width is `2asin(δ/t)`; at a core crossing of radius `rᵢ≥t−M`, the disk's radial integral is at least `2κᵢρrᵢ`, including the case `rᵢ<ρ`. Therefore `Δ(c)≥4κρ(t−M)asin(δ/t)≥4κρδ(1−M/t)`. The two regions cover the plane. Equating their lower terms yields the displayed `C*`. The hypotheses and four evaluated constants are checked in report 04.

## 5. One-bit recovery and sharp error tolerance — PASS

At `h=1/2`, `c=(1/2,1/4)`, reflection `x↦(1,1/2)−x` exchanges the open supports, preserves `r=|x−c|`, and reverses both linear scores. It suffices to prove strict positive scores for class 0. The near score is `9(x−1/2)+10(y−1/4)=9x+10y−7`; the far score is `(y−1/4)−(x−1/2)=y−x+1/4`.

If a class-0 point has nonpositive near score, write `x=s(cosθ,sinθ)`, `4/5<s<6/5`, `0<θ<π`. The squared midpoint radius is `F=s²+5/16−s(cosθ+sinθ/2)`. Since `∂F/∂s≥8/5−√5/2>0`, move to `s=4/5`. The feasible angular boundary solves `9cosθ+10sinθ=35/4`, and monotonicity of `cosθ+sinθ/2` on the feasible arc makes its minimum radius the boundary point

`x*=(63−2√1671)/181`, `y*=(350+9√1671)/905`.

Substitution gives `r²≥(29761+440√1671)/72400=β²`. Because the inner circle is excluded, every **support** point with nonpositive near score has `r>β`. Thus a threshold `t≤β`, with near bin `r≤t`, cannot assign it to the near rule.

If a class-0 point has nonpositive far score, then `x−y≥1/4`. On the closed cap `{y≥0, x−y≥1/4, x²+y²≤36/25}`, the convex function `|x−c|²` reaches its maximum on the outer arc or vertices. On the arc `x=(6/5)(cosθ,sinθ)`, `0≤θ<π/4`, one has `cosθ+sinθ/2≥1` and `r²≤221/400=α²`, with equality only at `(6/5,0)`. The straight segments have no larger value. That unique equality point is excluded from `S₀`; hence every support point with nonpositive far score has `r<α`. For `t≥α`, the far bin `r>t` cannot contain such a point. Reflection proves both rules for class 1, including ties and both threshold endpoints.

The endpoints are sharp for this fixed decoder. Interior points approaching `(6/5,0)` from `S₀` have far-rule error and radii approaching `α` from below; any `t<α` admits an open erroneous subset. Interior points approaching `(x*,y*)` from radius `s>4/5` and larger `θ` have near-rule error and radii approaching `β` from above; any `t>β` admits an open erroneous subset. The excluded boundary points explain why **closed** threshold endpoints are valid despite the sharpness. The exact formulas, numerical values, and adversarial points are in reports 03–04.

For a measured radius `r+e(x)` with `|e(x)|≤ε`, the effective pointwise threshold is `t−e(x)`. Every admissible error function keeps it inside `[α,β]` exactly when `α+ε≤t≤β−ε`. If either inequality fails, a constant admissible error shifts the effective threshold beyond the corresponding sharp endpoint, producing an open error set. The maximum guaranteed tolerance is `min(t−α,β−t)`, uniquely maximized at `(α+β)/2`. At the experimental `t=0.8` it is `β−0.8`. This result assumes exact direction and only additive bounded error in radius.

Direction alone has positive risk at this geometry for every origin, while the displayed bit and decoder have zero risk. Thus the minimum **additional radial** code size at the specified geometry, among finite-valued radial codes appended to exact direction, is one bit. The result does not assert a global optimum among arbitrary alternative measurements, angular decoders, centers, or other geometries.

## 6. Supplementary calculation lemmas — PASS

The finite necessary-and-sufficient preservation test in `supplement_theory.tex` lines 237–273 is valid for the two stated sampling laws. The arrangement includes four circle boundaries, both diameter lines, all tangencies, pairwise intersections, and line-parallel directions. Between consecutive event directions, positive root count and radial order cannot change, so one interior ray has the same sign pattern as every ray in that open angular cell. Event directions themselves are finite and have zero angular measure. For area sampling the overlap sign is `sign(π₀−π₁)`. For radius sampling, multiplying the positive comparison `π₀/|x−m₀|−π₁/|x−m₁|` by positive distances and squaring shows its sign is the sign of `π₀²|x−m₁|²−π₁²|x−m₀|²`; the extra Apollonius boundary is therefore necessary. The event maxima `40`, `52`, and `54` follow from the listed pair counts, with coincident events merged. The test is about **positive versus zero loss** at a fixed origin; it is not a numerical risk evaluation.

The radial primitives in `supplement_theory.tex` lines 293–363 differentiate correctly: a class-support interval `[ℓ,u]` contributes `(u²−ℓ²)/(2H)` for area sampling. For radius sampling, with `z=u·(c−mᵢ)` and `k²=|c−mᵢ|²−z²`, the derivative of `√((r+z)²+k²)−z asinh((r+z)/k)` is `r/√((r+z)²+k²)`. The stated logarithmic collinear expression has derivative `r/|r+z|` on either side of the excluded center. The horizontal primitive differentiates to the displayed reciprocal radial density. The area raw-risk formula is overlap area times `min(π₀,π₁)/H`; the equal-prior radius raw-risk symmetry follows by reflecting the two centers and splitting at the perpendicular bisector.

The density-ratio result in lines 364–393 follows algebraically: `fᵢᴿ/fᵢᴬ=(a+b)/(2|x−mᵢ|)∈[5/6,5/4]`. Monotonicity of `min` gives the two-sided risk bounds. Under equal priors, the area signed density vanishes on support overlap, while the radius signed density on exclusive regions retains each sign with magnitude at least `5/6` times the area magnitude. The ray cancellation identity therefore gives `Δ_R(c)≥(5/6)Δ_A(c)` even at `h=1`. The stated upper bound adds the total absolute signed overlap mass; this is a valid bound on how much overlap can raise each ray's cancellation.

The bounded-variation midpoint truncation lemma in lines 395–486 is valid under its stated compact-support and BV assumptions. Angular differentiation uses the rotation field `J(x−c)`; its divergence is zero and its tangency to circles centered at `c` removes the radial cutoff flux. BV pushforward contraction bounds angular variation. Integrating the variation from each cell midpoint gives error at most `(cell length/2)·TV_cell`, and summing equal cells yields `π/N` times the weighted class-variation bounds. The horizontal argument is the same one-dimensional variation inequality. The perimeter and density-gradient terms in the displayed area and radius variation bounds reproduce by direct arc, diameter, and interior integration. The historic Arb ball enclosures themselves were inspected for consistency with the independently evaluated area risks, but their 18 full original computations were not rerun; that numerical scope is distinguished in reports 01 and 09.
