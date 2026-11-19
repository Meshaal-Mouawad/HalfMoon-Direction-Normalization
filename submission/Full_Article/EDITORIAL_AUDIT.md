# Full-length Half-Moon manuscript — editorial and scientific audit

Date: 19 November 2026
Author: Meshaal Mouawad
Title: Global loss bounds and one-bit recovery for direction-normalized half-moons
Study status: Full-length research manuscript drafted and compiled; not externally submitted
Authoritative source: submission/Full_Article/Full_Manuscript.tex and Full_Theory.tex
Prior submitted PRL manuscript: PRLETTERS-D-26-03032 (sent back for an administrative authorship form)
Version handling: one existing GitHub repository and main branch, no extra branch; prior PRL Journal_Upload retained unchanged

## Scientific argument

- Problem: Discarding radius by direction normalization may merge observations requiring different optimal class decisions.
- Prior capabilities: spatial signs and normalized feature classification, Bayes decision-sufficiency criteria, projection geometry and decision-aware quantization; recent PRL studies investigate rule–geometry alignment and normalization-sensitive novelty detection.
- Research question: What origin-dependent Bayes-risk loss does direction-only representation impose for the specified continuous half-moon class supports, can any finite or distant origin eliminate it, and what minimal radial measurement repairs it in a proved case?
- Mathematical response: ray-cancellation identity, all-origin geometric obstruction, uniform projection limit at distant origins, constructive whole-plane certificates, and a one-bit near/far decoder with an exact threshold and radius-error guarantee.
- Empirical evidence: 420 main candidate fits / 210 selected evaluations and 80 independent one-bit repair candidate fits / 40 selected evaluations; frozen protocols and matched population-risk controls.
- Principal empirical finding: 54,362 direction-only errors versus three errors using the additional bit across the same 500,000 test observations per representation in the repair study.
- Contribution: an analytical separation between representation-induced classification error and learned excess, together with a minimal decision-recovery code for the proved disjoint half-moon geometry.

## Rewrite performed

The original seven-page compressed PRL manuscript was rejected by the author for insufficient explanation. A new full-length article was written from the validated research record, not lengthened merely by changing typesetting. It provides:

1. Reader-first Introduction explaining the task, why normalization is used, how two actual class-support points collapse to one direction, and the distinct questions of Bayes loss and neural learning.
2. Research-context section organizing the closest literature by normalized feature geometry, Bayes decision sufficiency, projection limits, and decision-aware radial coding.
3. Study-design section explaining all three geometric conditions and both sampling laws before using their technical specifications.
4. Expanded mathematical narrative around the protected equations: why a ray-cancellation identity is required, how finite and distant origins differ, why global certificates are conservative, how fixed-origin risk is computed, and how one bit restores the decision.
5. Neural methodology documenting independent seeds, fixed sample sizes, input controls, parameter counts, optimizer protocol, validation selection and the separate development and final evaluation stages.
6. Results that interpret each geometry relative to its source-space and representation-specific population floor, with seed-paired inference and diagnostic comparisons.
7. Separate one-bit empirical evaluation distinguishing the continuous-support decoder theorem from learned network behavior.
8. Discussion synthesizing findings against the closest prior scholarship, a single consolidated Limitations section and an evidence-bounded Conclusion.

## Technical validation

- Main full-length article compiled to 32 pages in 12-point, single-column, double-spaced LaTeX.
- Original full-theory displayed mathematical environments and equation labels compared to source and passed an exact-match check.
- Full original one-bit empirical result table matched the verified source (table float placement only changed for improved layout).
- Original main results and planned origin-contrast tables were reused verbatim except placement option.
- Citation keys in the new manuscript are present in the preserved bibliography; this is a key-integrity check, distinct from independent claim-by-claim source auditing.
- Full LaTeX source ZIP passed archive-integrity checks.
- Existing AI declaration wording and original V11 public research-data link were preserved.
- Existing seven-page PRL upload package remained unchanged.
- Temporary build workflows were removed; existing repository has only main.

## Rendered production inspection

The PDF was visually inspected at representative pages 1, 5, 7, 12, 15, 20, 27 and 32. Both scientific figures were rendered and inspected at pages 7 and 15. The original 15-condition population-versus-neural result table was rendered and inspected. The layout correction moved the result tables adjacent to their explanation and removed repeated theorem-introduction paragraphs. The final 32-page PDF was compiled again after those edits.

## Acceptance gates

| Gate | Status |
|---|---|
| Full manuscript rewritten with reader independence | PASS, editorial inspection |
| Frozen displayed theorem equations and labels | PASS, source comparison |
| Frozen one-bit experimental table | PASS, source comparison |
| Bibliography key resolution | PASS |
| Full-length PDF compilation | PASS, 32 pages |
| ZIP archive integrity | PASS |
| Representative page and both figure visual inspections | PASS |
| Exhaustive visual inspection of every one of 32 pages | NOT VERIFIED |
| New experiments or independent external scientific peer-review | NOT PERFORMED |
| Full-length article journal submission | NOT SUBMITTED |
| Original PRL journal package preservation | PASS |

## Venue and submission boundary

The author has not approved a new journal submission. The existing Pattern Recognition Letters manuscript remains in that journal's administrative process. The full-length article is a separate working product suitable for evaluation against full-research-article journal requirements. The repository has not submitted or transferred the paper to any venue. Any subsequent submission must reconcile the existing PRL status first.

## Limitations

The full-length text has passed source-preservation, compilation, citation-key, and representative-page tests. A page-by-page final proofreading pass and a genuinely independent scientific review of the full new narrative remain open; the separate review passes done during drafting are internal editorial checks. The current manuscript's empirical generality is restricted to its frozen sampled populations, neural architecture, seeds and protocol. The geometric and radial repair results retain exactly the assumptions specified by their original mathematical proofs.
