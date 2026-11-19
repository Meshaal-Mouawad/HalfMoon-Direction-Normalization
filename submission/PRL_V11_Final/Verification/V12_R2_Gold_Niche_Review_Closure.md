# PRLETTERS-D-26-03032 — V12 R2 Gold Niche review closure
Date: 2026-11-19
Source: "Independent Gold Niche Review — Revised Half-Moon Manuscript" (user-supplied review, 19 November 2026).
Baseline: GitHub main commit 83d4a4dd98f503049bc8b1abfcbd07a326a8d522.
Action: Targeted editorial correction; no new experiment, theorem, figure, author or journal submission.

## Finding-to-change register
| ID | Diagnosis verified in baseline | Targeted correction | Scientific boundary |
|---|---|---|---|
| M01 | Introductory illustration did not use two points in different actual half-moon supports | At h=0.5, use x0=(1,0.25) in S0 and x1=(2,0.25) in S1; midpoint c=(0.5,0.25) gives same unit direction (1,0) and radii 0.5/1.5 | Constructed illustration only; the theorem establishes positive probability |
| M02 | Motivation for direction normalization was compressed | Explain why orientation-based, scale-invariant representation is used and when losing distance matters | No new claim of practical benefit |
| M03 | Related work was compressed to citations | Explain Poblete's fixed-feature rule comparison and Ahmadian–Lindsten's normalization-sensitive novelty-detection ablations; state specific remaining origin-wide Bayes question | Do not imply prior studies proved all-origin loss |
| M04 | Individual zero-width ray called a probability mass | Identify A_c(theta), B_c(theta) as signed decision-mass densities per angle; excess risk only after angular integration | Protect exact ray-risk equation |
| M05 | Conservative all-origin certificate conflated with fixed midpoint error | Distinguish inf_c Δ(c)>0.0205 percentage points from fixed-midpoint 10.7479% direction-only Bayes risk at h=0.5 | Retain both source numbers |
| M06 | Radius-noise tolerance at experimental threshold unclear | Explicitly report tolerance 0.0120914734 units at t=0.8 versus maximum 0.0343940180 at t*=0.7776974554 | Exact direction and fixed decoder; neural test uses no noisy radius |
| M07 | Same hidden-layer width inaccurately implied equal parameter counts | State two-input=257 and three-input=321 trainable parameters; distinguish population-information effect from model-dependent fit | Protect training protocol and results |
| M08 | Geometry/control and second sampling law not connected | State h=-0.25 preserving-origin control, h=0.5 disjoint-all-origin failure, h=1 overlapping case; distinguish area-uniform neural data from radius-uniform analytical sensitivity | Same original three conditions, two source sampling laws |
| M09 | Discussion repeated measurements and underdeveloped literature interpretation | Remove repeated counts; compare to Poblete, Ahmadian–Lindsten, and decision-preservation foundations; interpret one-bit proof versus neural evaluation | No stronger empirical claim |
| M10 | Public data locator not visible as direct address in PDF | Print exact release URL and name Threshold_Addendum.pdf in revision archive | Preserve existing publicly released research archive and link |

## Mathematical checks
The constructed points satisfy sqrt(1^2+0.25^2)=sqrt(1^2+(-0.25)^2)=1.0307764064, between 0.8 and 1.2. Their midpoint distances are 0.5 and 1.5; for threshold 0.8 the near/far bits differ.
α=sqrt(221)/20=0.7433034373659253; β=sqrt((29761+440 sqrt(1671))/72400)=0.812091473357641.
At fixed t=0.8 the sharp guaranteed radius-error tolerance is min(t-α,β-t)=0.012091473357641 units.
The maximizing theoretical threshold (α+β)/2=0.7776974553617831 has tolerance (β-α)/2=0.034394017995858 units.

## Protected-content policy
Retain exact mathematical display environments, numerical certificates, theorem labels and proof references, tables (including uncertainty/denominators), original figures, 500 candidate fits/250 evaluations, AI declaration, author and date metadata, source release assets, and a single existing GitHub main branch. Text edits are editorial explanations only. Do not touch existing author-signed journal form.

## Verification status
Source corrections M01–M10 implemented; the compilation, final seven-page limit, LaTeX ZIP rebuilding, and visual page inspection remain separate production gates until an actual build confirms them.
