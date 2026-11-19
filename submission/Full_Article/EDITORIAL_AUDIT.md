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

- Main full-length article compiled to 31 pages in 12-point, single-column, double-spaced LaTeX.
- Original full-theory displayed mathematical environments and equation labels compared to source and passed an exact-match check.
- Full original one-bit empirical result table matched the verified source (table float placement only changed for improved layout).
- Original main results and planned origin-contrast tables were reused verbatim except placement option.
- Citation keys in the new manuscript are present in the preserved bibliography; this is a key-integrity check, distinct from independent claim-by-claim source auditing.
- Full LaTeX source ZIP passed archive-integrity checks.
- Existing AI declaration wording and original V11 public research-data link were preserved.
- Existing seven-page PRL upload package remained unchanged.
- Temporary build workflows were removed; existing repository has only main.

## Rendered production inspection

The PDF was visually inspected at representative all 31 rendered pages. Both scientific figures were rendered and inspected at pages 7 and 15. The original 15-condition population-versus-neural result table was rendered and inspected. The layout correction moved the result tables adjacent to their explanation and removed repeated theorem-introduction paragraphs. The final 31-page PDF was compiled, its source ZIP rebuilt and extracted independently, and the resulting PDF text matched the repository PDF exactly. The original PRL upload package was not modified.

## Acceptance gates

| Gate | Status |
|---|---|
| Full manuscript rewritten with reader independence | PASS, editorial inspection |
| Frozen displayed theorem equations and labels | PASS, source comparison |
| Frozen one-bit experimental table | PASS, source comparison |
| Bibliography key resolution | PASS |
| Full-length PDF compilation | PASS, 31 pages |
| ZIP archive integrity | PASS |
| Representative page and both figure visual inspections | PASS |
| Exhaustive visual inspection of every one of 31 pages | PASS — all final rendered pages, including figures, equations, tables, bibliography and declarations inspected |
| New experiments or independent external scientific peer-review | NOT PERFORMED |
| Full-length article journal submission | NOT SUBMITTED |
| Original PRL journal package preservation | PASS |

## Venue and submission boundary

The author has not approved a new journal submission. The existing Pattern Recognition Letters manuscript remains in that journal's administrative process. The full-length article is a separate working product suitable for evaluation against full-research-article journal requirements. The repository has not submitted or transferred the paper to any venue. Any subsequent submission must reconcile the existing PRL status first.

## Limitations

The full-length text passed source-preservation, compilation, bibliography, independent ZIP rebuild, and all 31 rendered-page checks. A genuinely independent scientific peer review of the novel theorem and empirical claims remains outstanding; separate passes performed in this editorial workflow are internal, not external peer review. The current manuscript's empirical generality is restricted to its frozen sampled populations, neural architecture, seeds and protocol. The geometric and radial repair results retain exactly the assumptions specified by their original mathematical proofs.

## Final synchronized production receipt — 19 November 2026

- 31-page, 12-point, single-column, double-spaced article compiled from the current authoritative TeX files.
- Final PDF and updated source ZIP published together in a single workflow, followed by independent extraction of the ZIP in a clean directory and full LaTeX rebuild.
- Rebuilt PDF has the same page count and identical `pdftotext -layout` output as the published repository PDF.
- Frozen display equations and original labels match the validated original theory byte-for-byte; original experimental table contents match independently after normalizing LaTeX float placement.
- Four original and supplemental study tables remain readable. Table 2 and Table 4 were repositioned to preserve paragraph continuity and avoid artificial whitespace; no measurement was altered.
- Every page from 1 to 31 was rendered, opened and inspected for readable equations, correct figure labels, table integrity, bibliography, author metadata and disclosure statements.
- The two original research figures are preserved. Figure 1's caption correctly distinguishes the illustrated `h=0` from the experimental negative control `h=-0.25`.
- The final source ZIP contains the standalone build script, main and supplementary LaTeX, bibliography and required figures.
- Published V11 research-data release and all seven existing PRL upload assets remain unchanged.
- GitHub has only the default `main` branch; no additional folder or repository was created.

## Literature and scientific-review gate

- All 17 cited bibliographic identities were audited. Thirteen matched directly in a specialized citation metadata audit; four without machine-resolvable DOI matches were manually cross-checked against original JMLR, NeurIPS and ICLR publication records. No retractions were reported by the citation audit.
- Central *Pattern Recognition Letters* papers by Poblete and colleagues (2026, DOI 10.1016/j.patrec.2026.07.024) and Ahmadian and Lindsten (2025, DOI 10.1016/j.patrec.2025.07.011) were checked against publisher records for the specific tasks they investigated.
- No exact previously published instance of the paper's combined all-origin theorem and same-threshold one-bit half-annulus decoder was identified by the bounded relevant-source search. This is a scoped research-frontier observation, not a verified claim of worldwide firstness.
- An additional autonomous Consensus search returned unrelated surname matches rather than the requested pivotal literature. Its search result was **excluded** from the novelty decision and is not an independent scientific endorsement.
- Original mathematical proofs were **preserved** and their equations checked for identity, but the proof of every general claim was not independently re-derived by a qualified external mathematician. External peer review remains **NOT VERIFIED**.

**Editorial decision:** Full-length rewriting, scientific preservation and production validation are **COMPLETE**. A new external journal submission has not been authorized or performed. The author's outstanding decision is how to resolve the existing active PRL manuscript before choosing a full-length journal.
