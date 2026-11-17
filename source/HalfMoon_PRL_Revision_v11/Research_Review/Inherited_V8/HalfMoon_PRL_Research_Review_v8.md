---
title: "Half-Moon V8: Contribution Review and Scientific Extension"
author: "Research and production record for Dr. Meshaal Mouawad"
date: "14 November 2026"
fontsize: 10pt
geometry: margin=23mm
colorlinks: false
---

## Decision

**Scientific revision complete.** The manuscript now distinguishes its moving-origin guarantees and restricted radial repair from general decision sufficiency and predictive compression. A new, proved result gives the exact operating interval of the existing two-rule decoder. The main article remains seven pages. Submission administration remains open as specified below.

The authoritative baseline is `HalfMoon_PRL_Revision_v7.zip`. Its 225 entries pass the ZIP integrity check and all 224 manifest hashes match. The task follows the author's *Mouawad Methodology—Research Gap Discovery*: start with the target journal's recent conversation, challenge the candidate gap against other venues, distinguish author statements from our inference, then revise the supported contribution. The original mathematical and empirical review closures are reused where their source files remain unchanged.

## A. Target-journal frontier and coverage

The review starts from Pattern Recognition Letters studies published or available online in 2026, followed by 2025 and contextual screening in 2024. The consequential themes are fixed-representation geometry, normalization and magnitude, projection selection, representation-induced risk, and task-aware compression. Exact-title follow-up searches and primary publisher, proceedings and author-version records then challenge the proposed gap across Pattern Recognition, JMLR, Signal Processing, Entropy, IEEE TPAMI, NeurIPS, ICML and the geometric literature.

The retained record comprises **21 inherited manuscript references, two additional pivotal predecessors and one contextual screening record**. Six inherited central records received fresh focused checks at the access levels stated in `Source_Ledger_v8.json`. These counts describe retained records, not 24 newly read full papers. The source ledger keeps prior full-text work separate from new abstract, selected-section and metadata checks. The new manuscript contains 23 cited references.

**2026: classifier compatibility in fixed representations.** Poblete et al. compare four rules on frozen embeddings; their eight-dataset analysis relates classifier behavior to class-centered geometry. The remaining issue for this paper is how changing the origin of the input map changes the information retained, rather than which classifier best uses a fixed embedding. This is our inferred distinction between questions, not an author-declared failure. Source: DOI 10.1016/j.patrec.2026.07.024; publisher-indexed abstract and introduction.

**2025: normalization and projection design.** Ahmadian and Lindsten examine contrastive time-series OOD scoring with radial kernels and context quantization. Oh develops generalized-mean trace-ratio feature learning. These are relevant precedents for magnitude and geometry affecting decisions. The present study instead seeks a population guarantee over an unbounded family of radial origins. Sources: DOI 10.1016/j.patrec.2025.07.011 and DOI 10.1016/j.patrec.2025.04.026; publisher-indexed summaries and selected exposed method sections, with detailed earlier records retained.

**2024: learned norm handling and decision sufficiency.** The author repository associated with norm-contraction work was screened as target-journal context; its inaccessible final paper is not counted as a new full-text comparison. The much closer external theoretical reference is Silva et al., JMLR 25(291), which establishes operational sufficiency under weaker information requirements. That result already addresses the general possibility of discarding information while retaining classification performance. Our claimed advance must therefore be the specified geometry, uniformity and constructive code, rather than that general possibility.

## B. Closest-predecessor challenge and research lineage

**General risk preservation is established.** Silva and Narayanan (Pattern Recognition, 2012) and Silva et al. (JMLR, 2024; Signal Processing, 2025) provide the representation-risk and sufficiency framework already credited by the paper. Györfi, Linder and Walk (Entropy, 2023) additionally characterize universal losslessness through conditional independence and derive information-based excess-risk upper bounds. Their final publisher record and selected author-version sections were checked. The new citation closes a material comparison gap in V7.

**Predictive compression is established.** Oehler and Gray (IEEE TPAMI, 1995) optimize quantization with classification objectives. Dubois et al. (NeurIPS, 2021) study compression for invariant predictive tasks and explicitly identify label encoding as the unrestricted single-task case. This second new citation makes the encoder restriction essential: exact direction remains available and the added symbol is only a comparison of radius with one common threshold.

**Geometric ingredients have predecessors.** Hurtado et al. provide wedge-separation geometry; Orponen discusses radial projections and their relation to orthogonal projections. Those ingredients are credited. The manuscript's proof obligation is the probability-risk statement: uniform convergence at distant origins, its combination with finite-origin positivity, and an explicit lower certificate. The V7 proof record is retained; no new claim of inventing radial projection geometry is made.

The resulting lineage is:

1. Decision sufficiency specifies what must survive a representation.
2. Radial geometry determines which opposing decisions can merge.
3. Uniform convergence to projection risks controls the unbounded origin search.
4. Signed-density cores turn that control into positive numerical certificates.
5. A constrained radial bit restores decisions for the specified half-moon geometry.
6. The added threshold proposition characterizes exactly when the same decoder continues to work.

The full comparative matrix is in `Closest_Work_Comparison_v8.csv`; source identities, access and evidence locations are in `Source_Ledger_v8.json`.

## C. Gap register and ranking

**Candidate 1 — “Normalization can discard useful magnitude.” ALREADY ADDRESSED.** Existing normalization and representation research establishes this broad premise. It supplies motivation rather than the paper's central novelty claim.

**Candidate 2 — “A compressed representation can preserve classification.” ALREADY ADDRESSED.** Decision-sufficiency and predictive-compression theory establish that possibility. A generic one-bit encoding of a binary prediction does not resolve the constrained geometric problem studied here.

**Candidate 3 — “An origin-independent quantitative obstruction for radial normalization.” CONFIRMED WITHIN VERIFIED SEARCH SCOPE; primary contribution.** The examined predecessors do not supply the specific combination of a uniform distant-origin Bayes-risk limit, whole-plane positivity criterion, signed-density certificates and half-annular application established by the supplied proofs. The distinction is an inferred knowledge-connection and uniformity gap. It explains why a center search cannot be assumed to repair discarded decision information.

**Candidate 4 — “Minimal repair by one common radius comparison.” CONFIRMED WITHIN VERIFIED SEARCH SCOPE; linked constructive contribution.** The radial code is constrained before it reaches the decoder. Geometric inequalities establish that this measurement, jointly with exact direction, preserves every support label. The zero-bit obstruction supplies minimality of the additional radial budget.

**Candidate 5 — “The exact threshold interval for the fixed decoder.” RESOLVED BY THE NEW ANALYTICAL EXTENSION.** V7 establishes one threshold. V8 derives both endpoints and proves sharpness for the same angular rules. This adds a verifiable design interval instead of additional classifier fits or a larger sample count.

Unrelated benchmark expansion, a new acronym and broad “better normalization” claims were rejected as ways to strengthen the central argument. They do not answer the selected scientific question.

## D. Contribution and evidence map

The study establishes when radial normalization suffers unavoidable classification loss across every origin, including origins receding without bound, and gives a minimal geometric repair for the half-moon population. Uniform Bayes-risk convergence and signed-density cores supply the global criterion and computable lower certificates. At displacement 0.5, a shared radius bit selects two angular decisions; the new proposition identifies its entire valid threshold interval for that decoder. Fixed-protocol neural studies then locate learned error relative to the representation's attainable risk.

The evidence remains separated by function:

- **Population claims:** the existing general limit theorem, geometric proofs and constructive certificate derivations.
- **Concrete lower values:** the preserved numerical certificates; these are lower bounds on global loss, not claims that the bound is the optimal risk.
- **Minimal bit:** the all-origin zero-bit obstruction plus the explicit support-wide one-bit decoder.
- **New interval:** an analytic proof with exact algebraic endpoints and open-set counterexamples outside them.
- **Learning behavior:** the unchanged 500 candidate fits and 250 validation-selected evaluations. The repair experiment's three errors in 500,000 observations remain exactly as reported.

The decision is **Route A: strengthen the supported study**, with a focused analytical extension. No additional neural training is scientifically required to establish the stated population contribution. The added computation replays existing arrays and checks constructed geometric points; it does not increase the count of independent experimental replicates.

## E. New mathematical result

For the midpoint $c=(1/2,1/4)$ at displacement $h=1/2$, write $r=\|x-c\|$ and retain $q_t=\mathbf1\{r>t\}$. Keep the existing near rule $9u_1+10u_2>0$ and far rule $u_2-u_1>0$ for class 0. The decoder correctly classifies every support point exactly for

$$
\frac{\sqrt{221}}{20}\leq t\leq
\sqrt{\frac{29761+440\sqrt{1671}}{72400}}.
$$

The endpoints are approximately **0.7433034374 and 0.8120914734**. Every threshold in the convenient inner interval **[0.75, 0.81]** is therefore valid. The existing experiment's threshold 0.8 lies inside it.

The proof finds the greatest radius among points where the far rule can err and the least radius among points where the near rule can err. The former extremum occurs at the outer semicircle's boundary point (1.2, 0); the latter at the inner semicircle's intersection with $9x+10y=7$. Both extrema lie on excluded support boundaries, making equality at both threshold endpoints safe. Reflection transfers the proof to class 1. Strictly erroneous interior points exist beyond each endpoint, which proves sharpness for the specified decoder.

Executed checks in `threshold_verification.json` include ten exact symbolic identities/inequalities, six threshold evaluations on 482,482 constructed interior points, six replays of the same 500,000 existing observations, and strict counterexamples just outside both endpoints. The in-interval checks return zero errors. The continuous-support result follows from the proof, with these computations serving as implementation diagnostics.

The three-page `Threshold_Addendum.tex/pdf` contains the full statement, proof and computational interpretation. It is a separate supplement so the previously approved 18-page supplement stays byte-identical.

## F. Manuscript and submission changes

The introduction now asks whether recentering can preserve the raw-coordinate decision and whether a single shared radius comparison can repair the loss. It identifies the general origin-family criterion before presenting the half-moon construction.

Related work now explicitly compares universal losslessness and predictive compression. The description of the recent PRL embedding study uses the directly accessible ranking and class-centered geometry findings rather than retaining an unnecessary narrower hypothesis interpretation. The two added sources are credited in the bibliography; all 21 existing entries remain unchanged.

The main theory section retains its entire original text byte for byte, followed by one paragraph introducing the certified threshold interval. The abstract, discussion, conclusion and limitations are synchronized with that addition. The main text refers to the new addendum by name and proposition number. Every existing result table and figure remains unchanged.

The cover letter is updated to describe the exact interval. Highlights now contain five items of 76, 72, 70, 78 and 74 characters. The approved AI declaration remains unchanged and appears once. The author-supplied journal guide and administrative checklist are retained as evidence, separate from upload files.

## G. Verification and gates

The baseline archive check verifies all 224 listed hashes. **Nine proof/experiment/supplement TeX files are byte-identical**, the entire prior main-theory fragment is retained as an identical prefix, all five checked table bodies are unchanged, and all 15 figure assets are byte-identical. Both publisher class/style files are unchanged. The existing bibliography is preserved as an identical prefix with two appended entries.

The delivered main article has **7 pages**, the original supplement **18 pages**, and the new addendum **3 pages**. The main abstract contains 170 whitespace-delimited source tokens, below the journal's 250-word maximum; six keywords are retained. The fresh source-ZIP build regenerates both bibliographies and all document outputs. All **28 pages** match the delivery PDFs in extracted text and 108-dpi rendered pixels. Final logs contain zero missing-character or unresolved-reference/citation diagnostics. No PDF text spans extend beyond page bounds.

The original supplement delivery is byte-identical to V7. A fresh source build of that supplement was also compared page by page and matches its text and pixels on all 18 pages. The experimental reproducibility archive is read only; its SHA-256 remains `78df38a57ab07921029ac025c709ca69d2c565692640a30d7a47003ca107ead5`.

**J1–J5:** PASS within the documented search/access scope: recent target-journal context, cross-venue challenge, explicit separation of author statements and inference, consequential question, and comparison with the strongest located predecessors. **J6–J8:** PASS for the stated contribution: appropriate proof/evaluation design, traceable evidence and reader-level explanation. **J9:** PASS for the new pivotal claims at the recorded source-access levels; inherited source checks are not relabeled as fresh full-text reading. **J10:** PASS against the author-supplied PRL scope, which includes statistical pattern recognition and concise methodological findings. The prior M1–M4/P1 closures are carried forward only for preserved material.

## Submission administration

The main article is a **new-submission working package for Pattern Recognition Letters** according to the recorded author workflow. No external submission or public data upload was performed. The seven-page main article, editable source, institutional email, five highlights, existing graphical abstract and both supplements are available.

Before the author submits, the official Authorship and Formats Form must be completed in the required publisher form and uploaded under Cover Letter; the competing-interest declaration must be finalized; funding and author attestations must be confirmed; and a data repository link or an applicable explanation must be supplied. No signature, disclosure response or repository identifier was invented. The data-availability text describes the supplied research package and must be synchronized with the actual repository record when deposited.

Upload the **main manuscript alone** under Manuscript, and the 18-page supplement and three-page Threshold Addendum as separate supplementary items. The complete research revision ZIP also contains editorial records and is not the file to upload wholesale to the journal.

## Limitations and access boundaries

This was a bounded literature challenge and sequential analytical/computational review, not a new external independent peer review or an exhaustive systematic review. Several publisher full pages returned HTTP 403 or rate limits; accessible primary indexed text, selected final/author-version sections and earlier verified records are distinguished in the ledger. Public PDF screenshot requests returned cache misses, so those paper checks rely on parsed text rather than a new visual inspection of their figures. No inaccessible full paper is counted as newly read. The new threshold result is maximal for the stated decoder, center and geometry; it does not establish optimal thresholds for all alternative decoders or robustness to noisy coordinates. The inherited CAS title-construction overfull-box warning remains, with the title visually unclipped; the supplement and addendum have no overfull-box warnings. External submission administration remains the author's action.

## Primary references for the new comparison

Györfi, L., Linder, T., and Walk, H. (2023). *Lossless Transformations and Excess Risk Bounds in Statistical Inference*. Entropy 25(10), 1394. DOI: 10.3390/e25101394. Author version: <https://arxiv.org/pdf/2307.16735>.

Dubois, Y., Bloem-Reddy, B., Ullrich, K., and Maddison, C. J. (2021). *Lossy Compression for Lossless Prediction*. Advances in Neural Information Processing Systems 34. <https://proceedings.neurips.cc/paper_files/paper/2021/hash/7535bbb91c8fde347ad861f293126633-Abstract.html>.

Poblete, V., Aillapi, J., Duarte, C., Veas, L., and Otondo, F. (2026). *Decision-rule alignment in generative latent spaces: The role of radial compatibility*. Pattern Recognition Letters. DOI: 10.1016/j.patrec.2026.07.024.

Ahmadian, A., and Lindsten, F. (2025). *Improved Contrastive Predictive Coding for Time Series Out-Of-Distribution Detection Applied to Human Activity Data*. Pattern Recognition Letters 197, 132–138. DOI: 10.1016/j.patrec.2025.07.011.

Oh, J. (2025). *Maximizing generalized mean of trace ratios for discriminative feature learning*. Pattern Recognition Letters 194, 26–31. DOI: 10.1016/j.patrec.2025.04.026.

Silva, J. F., Tobar, F., Vicuña, M., and Cordova, F. (2024). *Studying the Interplay between Information Loss and Operation Loss in Representations for Classification*. JMLR 25(291), 1–71. <https://www.jmlr.org/papers/v25/21-1551.html>.
