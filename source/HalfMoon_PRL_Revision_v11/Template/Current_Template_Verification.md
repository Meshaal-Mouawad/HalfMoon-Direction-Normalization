# Independent verification of the journal-linked CAS template

Date: 9 November 2026. Scope: template identity, publisher provenance, and the technical basis for resolving M4 through the current journal-linked template. No manuscript content was edited in this verification.

## Finding

**The double-column CAS template is directly supported by the recovered current Pattern Recognition Letters Guide for Authors and by the publisher's freshly downloaded template bundle.** Selecting `cas-dc` therefore follows an explicit journal-provided LaTeX route. The resolution does not require inventing a singular `prletter.sty`, renaming a historical file, or asserting that every earlier journal-format document was revoked.

## Verified evidence chain

1. The preserved 8 November 2026 current-guide browser capture has SHA-256 `310dd2f6df83835dfa590ad75ed646b76bc358ec247b329cdc408c3424ba6a51`, exactly matching its contemporaneous requirements record. The source is the journal's Guide for Authors: https://www.sciencedirect.com/journal/pattern-recognition-letters/publish/guide-for-authors .
2. Capture line 396 encourages the journal's linked LaTeX template. Its captured link record at line 1020 resolves that specific anchor to the publisher asset `els-cas-templates.zip`. The same guide requires a double-column manuscript of no more than seven pages at line 932.
3. The exact captured publisher URL was downloaded again on 9 November 2026: https://assets.ctfassets.net/o78em1y1w4i4/5uFmLZJTPDMAUjFnHRpjj8/6f19a979146eb93263763d87a894ab0d/els-cas-templates.zip . The 3,305,507-byte archive has SHA-256 `36d97da01c6bbd134f315bff6c3de553735e2550444a6ddd4f869ddc67a20757`, identical to the preserved 8 November publisher download.
4. The archive README defines `cas-dc.cls` as the double-column class and describes acceptance of these classes in Elsevier's submission systems. Its required `cas-common.sty` and the class both match the prior publisher originals byte-for-byte. Machine-readable hashes and comparisons accompany this report.
5. The executable class declaration identifies `cas-dc`, version 2.4, dated 2024/05/04, with double-column flags enabled. The opening comment in the genuine publisher file incorrectly names `cas-sc.cls`; that comment does not define the class. This resolves the apparent source-identity discrepancy without modifying the official file.

## M4 resolution to apply

Use the exact journal-linked `cas-dc.cls` and `cas-common.sty`, preserve their original bytes, build the seven-page manuscript, and verify its rendered layout. Keep the revised abstract below 200 words so that it satisfies both the earlier journal form and the recovered current guide. Supply the required separate highlights, graphical abstract, editable sources, supplement, and authorship materials. Report the template as the current guide-linked CAS double-column option. Record the source identity as `cas-dc`, irrespective of the erroneous comment.

The appropriate final evidence statement is: “The manuscript uses the double-column CAS template linked by the journal's current Guide for Authors; the publisher archive and class files were independently re-downloaded and hash-verified.” This is narrower and better supported than a claim that the older journal-specific style was formally superseded.

## Evidence boundaries

The full current guide could not be freshly retrieved on 9 November: research retrieval returned HTTP 403 and the cloud browser displayed an unavailable page. Its content and links are supported by the preserved 8 November browser capture and contemporaneous hash record; the linked publisher archive was freshly retrieved. The guide also directs authors to follow the older Authorship & Formats form, which names `elsarticle` plus singular `prletter`; no publisher statement explicitly resolving that naming inconsistency was recovered. The current guide's positive CAS recommendation supplies the basis for this template choice. A third-party 2026 author repository reports use of plural `prletters` after an editorial technical check; it is not publisher authorization and is not used as the basis of this finding.
