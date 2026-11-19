# Half-Moon V12 — Reader-First Editorial Change Register
Date: 2026-11-19
Manuscript: PRLETTERS-D-26-03032
Journal: Pattern Recognition Letters
Author: Meshaal Mouawad
Baseline source: commit a04514342a1df0fe34fcf2c534fe2a920b191dd5
Submission state: Sent back for administrative authorship form; scientific rewrite requested by author before resubmission.

## Scientific object and question
Two half-annular supports provide a continuous classification task. The question is whether a direction-only representation can preserve optimal classification under any normalization origin, and how little radial information suffices to repair the decision in a proved geometry. The analytical response derives ray-cancellation risk, all-origin and distant-origin bounds, numerical certificates, and a minimal radial bit. Frozen neural studies distinguish Bayes floors from learned errors.

## Changes and rationale
| Location | Baseline issue | V12 edit | Source/constraint |
|---|---|---|---|
| Abstract | Advanced mathematical claim before clear data object or metric | Explicit normalization, half-moon populations, Bayes-risk meaning, experiments and measured counts | 178 words, 200-word official template limit |
| Introduction | Only brief definition of the research geometry and Bayes risk | Define half-moon bands, show illustrative same-ray collision, define attainable error and origin search, then contributions | Universal Writing Protocol: first-time reader |
| Background | Citation-dense sequences, insufficient synthesis | Theme-based explanation of representation, decision sufficiency, radial retention and distant-origin geometry | Existing citations retained |
| Theory opening | Announces loss and certificates before presenting data and mechanism | Half-annular class model and ray collision before risk integrals and theorems | Protected equations/labels unchanged |
| Theorem 1 | All-origin result not adequately motivated | Explain finite-origin question and convex-hull obstruction | Complete proof preserved in supplement |
| Theorem 2 | Distant origins and projection limit difficult to visualize | Explain near-parallel rays and projected information before the uniform-risk formula | Formula and domain unchanged |
| Constructive risk | A certificate was described before its practical purpose | Explain why a positive floor needs a numerical lower bound | Certified result unchanged |
| One-bit repair | Decoder rule given without gating intuition | Explain near/far bit selecting two angular separators before algebra | Explicit decoder, threshold and error bounds unchanged |
| Main experiments | Lists input codes and training parameters before the evaluation question | Explain distinction between attainable and learned errors; define all input controls; clarify seed as inference unit | Frozen protocols and results unchanged |
| Repair experiment | Neural evaluation blended with constructive proof | Separate ideal decoder existence from learnability and report matched error counts | Frozen counts and table unchanged |
| Discussion and conclusion | Theorem restatement and compressed interpretation | Differentiate source error, representation floor, and learned excess; interpret minimal bit and error tolerance | Existing scientific claims retained |
| Supplement and addendum | Weak orientation to proof scope | Introduce reader-facing objectives before mathematical details | Detailed proofs and mathematical blocks unchanged |

## Preservation tests already executed on current source
- TeX brace scans: 7 edited files balanced.
- Main theory: 10 math environments byte-identical to the source baseline; 11 labels preserved.
- Main manuscript: 2 figure environments unchanged; approved AI declaration and data URL retained.
- Main neural results tables: unchanged byte-for-byte.
- Repair results table: unchanged byte-for-byte.
- Threshold Addendum: 9 mathematical/proposition/corollary blocks unchanged.
- All 24 distinct related-work citation keys in narrative_sections.tex retained.
- Source files belong to the existing repository and single main branch.

## Evidence and closest-work check
Verified records on 2026-11-19:
- Poblete et al. (2026), *Decision-rule alignment in generative latent spaces: The role of radial compatibility*, Pattern Recognition Letters, DOI 10.1016/j.patrec.2026.07.024.
- Ahmadian and Lindsten (2025), *Improved Contrastive Predictive Coding for Time Series Out-Of-Distribution Detection Applied to Human Activity Data*, Pattern Recognition Letters, DOI 10.1016/j.patrec.2025.07.011.
- Silva and Narayanan (2012), *On signal representations within the Bayes decision framework*, Pattern Recognition, DOI 10.1016/j.patcog.2011.11.015.
- Official journal template states seven pages initially and up to eight after revision, with abstract at most 200 words.
The revision uses current claims already supported by these cited works; it does not announce novelty beyond the manuscript's verified theory.

## Remaining production gates
- Recompile with final sources; confirm main paper at most seven pages (editorial return is an administrative correction, not scientific reviewer revision).
- Verify supplement, threshold addendum, all cross-references and citations.
- Inspect rendered PDFs for text overflow, font problems, figures and tables.
- Synchronize the edited source ZIP and journal-upload PDFs.
- Recheck author form and editor portal before approval.

## Source access note
The uploaded Universal Writing Protocol, GOLD Niche standard and Mouawad Gap Discovery prompt were inspected directly. The Academic Writing Prompts.zip was materialized, but the file-execution environment could not unpack it in this session; its internal components are only corroborated through the earlier implementation inventory. Direct ZIP-wide compliance remains NOT VERIFIED.

No new experiments, results, mathematical statements, authors or preprint claims were introduced. This file records an editorial revision, not editor approval or journal resubmission.

## Page-limit correction — 19 November 2026

The first V12 Mac and GitHub Actions builds produced eight main-article pages (supplement 18, addendum 3). A diagnostic PDF text extract established that page 8 contained only bibliography entries [16]–[25]. The overflow arose from the reference list, not a missing explanation or experimental figure.

The bibliography was refocused on directly relevant research. Eight peripheral citation keys were removed from the main-text background: `Yang2026Compression`, `Meng2026`, `Ding2026`, `Scholkemper2025`, `September2024`, `Zhuang2026`, `Shen2025`, and `Ni2024`. Their entries remain in the preserved `references.bib`; no bibliographic source file or empirical/theoretical source was modified. The removed sentence on explanation-preserving image compression addressed a different outcome from classification Bayes risk. The grouped citations about attention, graph centering, discriminant analysis, and layer normalization did not establish the paper's particular all-origin or one-bit claim. The replacement paragraph directly connects decision-aware quantization to the shared-threshold question, preserving the reader's explanatory progression.

The central sources on spatial signs, Bayes decision preservation, recent PRL normalization/feature geometry, orthogonal projection, planar separability, and Bayes-aware quantization are retained. Frozen equations, numerical estimates, tables, figures, algorithm/code, authorship, AI declaration, and public data URL are unchanged.

The source spelling error `emph{can}` in `one_bit_experiment.tex` was corrected to `\\emph{can}` (TeX emphasis command).

**Production gate:** recompile and verify at most seven main pages before publishing the revised journal files. Visual inspection is still mandatory after successful build.
