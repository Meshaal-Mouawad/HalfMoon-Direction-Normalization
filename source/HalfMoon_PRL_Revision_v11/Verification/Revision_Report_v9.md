# Half-Moon V9 revision and verification

15 November 2026 | Pattern Recognition Letters

## Completed revision

V9 integrates the requested literature corrections and a proved sharp radius-measurement-error guarantee. The main article has seven pages; the preserved mathematical/experimental supplement has 18 pages; the revised Threshold Addendum has three pages. V8 remains an unchanged baseline.

The manuscript retains the question of classification loss across every normalization origin and the restricted one-bit repair. Its opening continues to explain the retained direction and discarded radius before presenting the research questions and mathematical response.

## Literature corrections

The Poblete comparison now preserves the unsupported general directional hypothesis and distinguishes the class-centered geometric descriptor from the centroid-based classifier. The primary article's Table 5 and Figure 5, PDF pages 14-15, confirm the strongest association was opposite to the prediction. The CPC comparison separates normalization and quantization: Table 3 gives normalized AUROC 61.6/68.2 and unnormalized RBF-without-quantization AUROC 74.6/83.4 on HAR/KU-HAR. Its information-loss explanation is attributed to the authors. The Dubois comparison now connects unit direction as a scaling invariant to the conditional-label invariance required by their task definition. Existing sufficiency and projection comparisons are retained.

Research_Review/V9_Source_Ledger.json records exact source locations, access levels and the changes supported. The bibliography retains all 23 entries.

## Sharp radius-error result

For exact direction, the fixed midpoint and decoder at h=0.5, V8 proves the valid threshold interval [alpha,beta]. Corollary 1 now proves that every support label is retained for every radius-error function bounded by epsilon exactly when alpha+epsilon <= t <= beta-epsilon. The proof applies the threshold proposition pointwise to t-e(x); constant extreme errors and the existing endpoint constructions establish necessity.

The guaranteed tolerance is min(t-alpha,beta-t). Its unique maximum is attained at t_star=(alpha+beta)/2 = 0.7776974553617831..., with epsilon_star=(beta-alpha)/2 = 0.03439401799585786.... At the unchanged experimental threshold 0.8, tolerance is 0.0120914733576410.... Units are the coordinate units of radius. The full corollary and proof appear together on addendum page 3; the main theory, abstract, introduction, discussion and conclusion now explain this consequence.

## Fresh analytical checks

The V9 script verifies four exact identities/order checks. For 482,482 constructed interior points at seven thresholds, it tests every near/far bin reachable under the specified bounded error; no admissible bin gives a wrong decision. Eight strictly interior counterexamples verify failure beyond the lower and upper margins at four thresholds. The V8 threshold script was also rerun: ten symbolic checks, the 482,482-point grid at six thresholds and both endpoint witnesses pass. These diagnostics support the implementation of the separately proved results.

The preserved V8 record of replay on 500,000 existing observations is included and identified as inherited. V9 performed no neural fitting and no fresh saved-observation replay.

## Preservation and production

Nine proof/experiment/supplement source files match V8 byte for byte. The original main-theory source before its threshold paragraph is unchanged; the original threshold proposition and proof are intact. All five checked table bodies, all 15 figure assets, the bibliography and the approved preparation declaration are preserved; the declaration appears once. The delivered original supplement PDF is byte-identical to V8.

Both bibliographies were regenerated. The final logs contain no missing-character or unresolved-citation/reference diagnostics. The authentic CAS files are unmodified. All seven main-article pages and all three addendum pages were inspected as rendered pages. The corollary begins on a new page to keep its statement and proof together.

A fresh extraction of the source ZIP is rebuilt separately; Clean_Source_Build_v9.json records page, text and rendered-pixel comparisons for the article and addendum. The unchanged supplement rebuild has identical normalized text on all 18 pages. The original PDF is delivered to preserve its exact bytes. Source changes are in Verification/V8_to_V9_Source.diff; protected-content checks are in Verification/Protected_Content_v9.json. The cover letter, five highlights and submission mapping are updated.

## Limitations and author finalization

The failed attachment Half_Moon_Sources(1).zip was not inspected. A separately stored primary Poblete PDF and V8 revision archive were recovered. CPC verification used indexed primary methods/Table 3 excerpts because direct PDF retrieval timed out. The other source-access levels are recorded individually. V9 does not claim a new external independent peer review or a fresh audit of every predecessor proof. The error corollary concerns the fixed midpoint, exact direction, specified geometry and existing angular decoder.

The live journal guide returned HTTP 403 on 15 November; the established CAS format and archived publisher evidence were retained. The inherited CAS zero-width title/keyword-box warning remains; the rendered block is unclipped. Supplement rebuilding can change PDF bytes and a small number of raster pixels across installations; the delivered V8 supplement is untouched and its source/text checks pass. Author signatures, funding/competing-interest confirmations, submission attestations and the repository-link step remain in the checklist. No journal submission or public deposit was made.
