# V7 Manuscript Enhancement and Verification

**Manuscript:** Global loss bounds and one-bit recovery for direction-normalized half-moons  
**Author:** Meshaal Mouawad  
**Target:** Pattern Recognition Letters (Elsevier)  
**Revision date:** 14 November 2026  
**Baseline:** HalfMoon_PRL_Submission_v6.zip  
**Baseline SHA-256:** `dbe0787a48aa3dff928b7394e6fde9bb5e1ea29e7a6e26b814f33ebd704c5836`

## 1. Decision and scientific contribution

**MANUSCRIPT ENHANCEMENT COMPLETE — Route A, strengthen the existing study.** V7 improves the explanation and integration of the existing results. It retains the seven-page article, the exact V6 supplement PDF and the established mathematical and experimental record. No new training, journal submission or public repository operation was performed.

Direction normalization discards distance from the chosen origin. The study establishes when every origin incurs a positive classification-loss floor, quantifies this loss through constructive lower certificates, and identifies an exact one-bit radial repair at h=0.5. The uniform distant-origin theorem connects radial views to projection risks and closes the unbounded origin search. The controlled neural studies then measure learned errors relative to these representation-specific population limits. This is the contribution maintained throughout V7.

The before-revision decision is preserved as `Scientific_Decision_Before_Revision.md`. The supplied M1-M4 scientific/template closures and V6 P1 correction are carried forward. Current editorial passes are not described as new independent peer review.

## 2. Substantive changes

### 1. Abstract; Introduction

**Issue:** The operation and research questions appeared after compressed technical claims.

**Change:** Explain retained direction and discarded radius; explicitly ask whether recentering can preserve decisions and how much radial information restores them.

**Scientific record:** Same contribution, geometric conditions and reported results.

### 2. Background and related work

**Issue:** The links among sufficiency, origin geometry, magnitude and quantization required reader inference.

**Change:** Explain each research stream through its decision question and connect it to the global criterion or exact repair.

**Scientific record:** All 21 bibliography records retained; no added priority claim.

### 3. Theory, before Theorem 2

**Issue:** Pointwise positive loss and a positive global infimum could be conflated.

**Change:** Explain why escaping origins must be controlled before a global floor follows.

**Scientific record:** The theorem, assumptions and formal mathematics are unchanged.

### 4. Theory, one-bit recovery paragraph

**Issue:** The construction lacked an explicit Figure 2 callout.

**Change:** Connect the near/far radial indicator to its two angular decision rules.

**Scientific record:** The decoder, threshold, support inequalities and figure are unchanged.

### 5. Experimental methods

**Issue:** Candidate-fit totals and the statistical inference unit were compressed.

**Change:** State 420 original final candidates separately from 48 development fits; name the paired seed as the inference unit.

**Scientific record:** The 80/40 repair counts and all data remain unchanged.

### 6. Tables 1 and 2 captions

**Issue:** Input abbreviations could not all be interpreted from the tables alone.

**Change:** Define raw, direction-only, direction-plus-radius and origin subscripts in captions.

**Scientific record:** All five tabular source bodies, including supplementary macros, match byte-for-byte.

### 7. Discussion; Conclusion

**Issue:** The relation among global certificates, fixed-origin risks and learned excess was underdeveloped.

**Change:** Explain their separate roles, one-bit selection of an angular rule and how the controlled benchmark distinguishes representation loss from learned excess.

**Scientific record:** No new numerical result, experimental outcome or generalization claim.

### 8. Typesetting in main/theory/repair source

**Issue:** A two-line definition and its lead-in could split across pages; a confidence-interval sentence overflowed.

**Change:** Keep short aligned expressions together, keep the support-definition lead-in with its display, and split the interval sentence.

**Scientific record:** No font replacement, class modification, equation change or reduced type size.

## 3. Claim-to-evidence and measurement audit

The full seven-row matrix is in `Claim_Evidence_Matrix_v7.csv`. Mathematical statements and proof sources retain their established assumptions. Statistical estimates are tied to per-seed records, not to the pooled number of test observations.

The original final experiment contains 420 candidate fits and 210 selected evaluations. The separate repair experiment contains 80 candidate fits and 40 selected evaluations. Their sums are 500 final candidate fits and 250 selected evaluations. The earlier 48 development fits and 24 selections remain separate.

From the archived per-model test records, V7 verification recomputed all 15 main-condition means and sample standard deviations, all six primary paired contrasts and simultaneous intervals, all four repair means/standard deviations and error counts, and both primary repair simultaneous intervals. Each value agrees with the archived analysis within the checked floating-point tolerance.

For the repair experiment, direction-only error is 10.8724% (54,362 errors in 500,000 observations); one-bit error is 0.0006% (three errors); the raw and full-radius networks have zero observed errors. The one-bit minus direction-only mean is -10.8718 percentage points, with simultaneous 95% interval [-10.9691225796, -10.7744774204]. The one-bit minus full-radius mean is 0.0006 percentage points, with interval [-0.0010110065, 0.0022110065]. The inference unit is the paired dataset/initialization seed, with ten seeds, nine degrees of freedom, and the recorded multiplicity family.

The exact decoder's population zero-risk statement and neural test outcomes remain separate evidential claims. No test observation was added, no trained model was changed, and no retraining was needed for this revision. See `Baseline_and_Numeric_Recheck.json` and the executable `audit_baseline_recorded.py`.

## 4. Literature and gap assessment

The supplied 21-source comparison was reused, including three Pattern Recognition Letters records. Its per-source access descriptions and evidence locations are preserved in `Published_Research_Comparison_v7.csv`. Six pivotal sources received a bounded primary-source refresh. The refresh is not represented as a new full reading of all 21 publications or an exhaustive priority search.

### Silva2024: Studying the Interplay between Information Loss and Operation Loss in Representations for Classification

Source: https://www.jmlr.org/papers/v25/21-1551.html

**Access:** Official abstract and selected relevant sections in the final JMLR PDF; not a new complete 71-page reading.

**Evidence:** Abstract; decision sufficiency and digital-encoder sections of the final article.

**Verified or preserved contribution:** Preserving the optimal classification decision can require less information than preserving the complete statistical representation.

**Relationship to this manuscript:** The manuscript uses that decision criterion and derives a uniform, quantitative criterion across an unbounded family of normalization origins.

### Orponen2019: On the dimension and smoothness of radial projections

Source: https://msp.org/apde/2019/12-5/apde-v12-n5-p06-s.pdf

**Access:** Publisher PDF parsed text; selected introductory material and Remark 1.14 inspected.

**Evidence:** Remark 1.14, published page 1277.

**Verified or preserved contribution:** Orthogonal projections are identified geometrically with radial projections from points at infinity.

**Relationship to this manuscript:** The existing geometric antecedent is credited; this manuscript adds the corresponding uniform convergence of binary Bayes risks.

### Ahmadian2025: Improved Contrastive Predictive Coding for Time Series Out-Of-Distribution Detection Applied to Human Activity Data

Source: https://liu.diva-portal.org/smash/get/diva2%3A1994850/FULLTEXT01.pdf

**Access:** Institutional version-of-record PDF text; relevant methods, results and normalization discussion inspected.

**Evidence:** CPC-vMF versus CPC-RBF methods/results and the discussion of spherical normalization.

**Verified or preserved contribution:** Unit-normalized and radial-scoring variants differ on human-activity out-of-distribution detection; the authors discuss information loss as an explanation.

**Relationship to this manuscript:** This motivates isolating radial removal, whereas the half-moon analysis determines the population decision loss and an exact repair.

### Poblete2026: Decision-rule alignment in generative latent spaces: The role of radial compatibility

Source: https://www.sciencedirect.com/science/article/pii/S0167865526002540

**Access:** Publisher-indexed abstract/introductory text refreshed; direct full-page access returned 403. Detailed H2 attribution is carried from the supplied full-text audit.

**Evidence:** Fresh indexed abstract; inherited audit of Sections 3.2.1, 3.4, 5.4/Table 5 and 6.2.

**Verified or preserved contribution:** Four decision rules are compared on frozen representations across eight datasets. The inherited full-text record reports that the proposed directional association was unsupported.

**Relationship to this manuscript:** Holding a population fixed while changing its normalization origin separates preprocessing information loss from the performance of a fitted rule.

### Oh2025: Maximizing generalized mean of trace ratios for discriminative feature learning

Source: https://www.sciencedirect.com/science/article/pii/S0167865525001679

**Access:** Publisher-indexed abstract and method excerpts; detailed full-text interpretation carried from the archived audit.

**Evidence:** Generalized-mean trace-ratio objective and Gaussian projection illustration.

**Verified or preserved contribution:** Linear feature learning is formulated using generalized means of scatter-ratio criteria and compared with projected decision behavior.

**Relationship to this manuscript:** Its optimization variable is a linear subspace. The present variable is the origin of a nonlinear direction map.

### Ni2024: On the Nonlinearity of Layer Normalization

Source: https://proceedings.mlr.press/v235/ni24b.html

**Access:** Official proceedings abstract and bibliographic record.

**Evidence:** Abstract statement about an LN-Net fitting arbitrary labels on m samples.

**Verified or preserved contribution:** Compositions of affine and layer-normalization operations can classify arbitrary finite samples with the stated network size.

**Relationship to this manuscript:** The half-moon question concerns preservation over an entire continuous population, rather than fitting a finite sample.

The revised synthesis credits decision sufficiency, the geometric projection-at-infinity observation and classification-aware quantization to their predecessors. It centers the present contribution on the uniform Bayes-risk boundary, all-origin bound, and exact constrained one-bit construction. The examined refresh provides no reason to change that framing or add experiments. Source-access details and the bounded assessment are recorded in `Literature_Refresh_v7.json`.

## 5. Scientific-content preservation

Eight of the twelve previously tracked scientific fragment/bibliography files remain byte-identical. Four fragments contain authorized explanatory or caption edits; the main entry point contains abstract, conclusion and layout changes. The exact five-file source diff is supplied. This is a prose revision, so the whole-source 12/12 identity claimed for the earlier production-only change is not claimed for V7.

All 70 extracted formal mathematical spans in the main theory fragment match V6 exactly; its proof-sketch passage also matches. All five checked tabular source bodies are byte-identical. Every supplementary proof source, the bibliography file, all 15 figure assets, authentic publisher class/style files, title/author metadata and approved AI declaration are preserved. The declaration occurs once. Both bibliographies regenerated by BibTeX match V6 byte-for-byte.

All 18 freshly rebuilt supplement pages matched the V6 supplement in extracted text and rendered pixels at 108 dpi. The delivered supplement was then restored from V6 to preserve the exact original PDF bytes. The separate experimental reproducibility archive remains unchanged and is referenced rather than duplicated inside the revision archive.

## 6. Build, render and package verification

The structured source and a fresh extraction of the final flat source ZIP were built with pdfLaTeX and regenerated BibTeX bibliographies. Before the flat test, cached PDFs, bibliography outputs, auxiliary files and exported supplement labels were removed. The build used pdfTeX 1.40.26 / TeX Live 2025/dev/Debian, with STIX present and Charis absent, retaining the environment relevant to P1.

The final article is seven pages; its abstract contains 169 whitespace-separated TeX tokens. The supplement is 18 pages. Final logs contain no missing-character warnings or undefined citations/references. All seven article pages were rendered and visually inspected for equations, percentages, table alignment, figure labels, captions and page transitions. No off-page text spans were detected. The final source ZIP rebuild matches all 25 delivered pages in extracted text and pixels at 108 dpi. The delivered supplement remains byte-identical to V6.

One inherited CAS title-construction overfull-box diagnostic remains (123.62721 pt at the title command). Inspection of the rendered title found no clipping or overlap. The revised body has no overfull-box diagnostic. No type-size reduction or modification of the publisher's class was used.

Exact package counts and checksum results are written after packaging to the separate `HalfMoon_PRL_V7_Package_Verification.json`. The archive contains its own SHA-256 manifest excluding the manifest itself. Editorial verification files are kept outside manuscript prose and outside the flat LaTeX source upload.

## 7. Requirement coverage and current status

**Pre-Stage 0 / Stage 6 truth gate — PASS.** V6 hash baseline; before-revision Route A decision; seven-row claim/evidence matrix; newly recomputed record-level statistics.

**Stage 0 section architecture — PASS.** Title, abstract, research questions, proofs, neural evaluation, discussion and conclusion retain one contribution.

**Stages 1.1 / 1.2 — PASS.** Revised operation-first introduction and explicit origin/recovery questions; same investigated population and results.

**Stages 2.1 / 2.2 — PASS.** Connected explanations; unnecessary inference removed; changes recorded rather than a wholesale rewrite.

**Stage 3 literature — PASS within recorded access scope.** 21-record comparison reused; six pivotal primary-source checks refreshed; genuine source relations and access limits recorded.

**Stage 4 integrated revision — PASS.** Five changed source files; exact diff and preservation audit; source/PDF synchronization tested.

**Stage 5 visual explanation — PASS.** All 15 scientific figure assets retained; Figure 2 linked to its mechanism; main captions made self-contained; rendered article inspected.

**Stage 6 experiment decision — Route A.** Existing proofs and experiment records support the revised contribution; no new training or test observations required.

**Production and final artifact — PASS.** Seven-page article; locked 18-page supplement; fresh source ZIP build; all 25 pages match text and pixels.

**New independent review — NOT PERFORMED.** Current checks are editorial self-review and executable verification. Prior independent closures are retained, not relabeled as new.

**Live journal instructions — NOT VERIFIED.** Official guide returned HTTP 403; preserved publisher guide and authentic CAS provenance reused.

## 8. Delivered files

- `HalfMoon_PRL_Manuscript_v7.pdf`: enhanced seven-page article.
- `HalfMoon_PRL_Supplement_v7.pdf`: exact V6 supplement bytes, unchanged.
- `HalfMoon_PRL_LaTeX_Source_v7.zip`: flat editable source and matching PDFs, separately clean-built.
- `HalfMoon_PRL_Revision_v7.zip`: structured manuscript, figures, unchanged submission materials, previous evidence records, current editorial audit and release manifest.
- `HalfMoon_PRL_Revision_Report_v7.pdf` / `.md`: current revision report.
- `V6_to_V7_Manuscript.diff`: exact manuscript-source changes.

V7 supersedes V6 as the enhanced working manuscript. The original V6 archive remains untouched. No repository was edited and no manuscript was submitted. Existing cover letter, highlights and author-finalization materials remain unchanged because the title, contribution and experimental findings remain the same.

## Limitations and outstanding checks

The live Pattern Recognition Letters guide and aims/scope pages returned HTTP 403. The archived 8 November publisher instructions and authentic CAS provenance were used for the established seven-page double-column format; current live policy changes were not verified. Public-PDF screenshot retrieval failed for the external primary texts, so fresh source inspection relied on parsed text and the explicitly preserved earlier access records. Direct full-text refresh was unavailable for some references; those attributions retain their documented baseline support.

Current scientific verification is record-level recomputation plus protected-source comparison and prior reviewed proof/certificate closures. It is not a new external independent review, full model retraining, or fresh replay of every prediction archive. The inspected source set is bounded. Font testing covers the stated STIX-present, Charis-absent environment; the inherited CAS title diagnostic is documented above. Author-only submission administration remains in the unchanged finalization record. These items are separated from the completed manuscript-enhancement and source/PDF-verification task.
