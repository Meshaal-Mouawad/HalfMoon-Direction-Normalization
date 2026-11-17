# Publisher template recovery, 9 November 2026

## Recovered files

The unchanged `elsarticle.zip` was downloaded from the link currently exposed on Elsevier's official LaTeX instructions page:
https://www.elsevier.com/researcher/author/policies-and-guidelines/latex-instructions

The archive was extracted under `elsarticle/`. `elsarticle.cls` was generated with the archive's `elsarticle.ins` and `elsarticle.dtx` through pdfLaTeX/DocStrip. The generated class SHA-256 is 01addb492c5d075b320636ac3a30d8a5762fa937220dea07a5e107042d25384d. Both dtx and ins are byte-identical to the previously retained 2024-copyright sources. The numeric bibliography style is also copied unchanged from this archive. The separate `elsevier-logo-3p.pdf` comes from the official LaTeX page's publisher asset link.

`prletters.sty` is an unchanged 2013 Elsevier-copyright, LPPL-licensed style from the public shachen/PLDS repository. Its internal version is 0.1, dated 2013/05/13. The associated `elsevier-logo.eps` was retrieved from that same repository. `elsevier-logo.pdf` is a Ghostscript vector conversion with EPS cropping. These are archival mirror assets, not a claimed current publisher download. Exact URLs and hashes are in `template_provenance.json`.

## Keyword behavior

Direct source inspection confirms that the old style saves keywords in `keybox` and defines `articleinfobox`, yet neither its final `MaketitleBox` nor `pprintMaketitle` calls `articleinfobox` or otherwise prints `keybox`. Thus the style omits the keyword block. An explicit keyword line in the manuscript after frontmatter can display the required terms without editing or renaming the publisher's archived style. Any such workaround must be documented and checked in the rendered PDF. A source-level patch should not be described as the publisher's updated `prletter.sty`.

## Unresolved publisher access

The accessible official journal PDF at https://legacyfileshare.elsevier.com/promis_misc/patrec-authorship-and-formatting.pdf specifies `elsarticle.cls` plus `prletter.sty`, a maximum 200-word abstract, seven pages inclusive, and separate 3–5 highlights of at most 85 characters. It uses the singular `prletter` filename.

The live ScienceDirect Guide for Authors returned 403 through research retrieval; the cloud browser displayed “Site Unavailable / Unable to access this site.” Known legacy publisher template ZIP URLs and the direct legacy style endpoint returned the same 195-byte HTML unavailable page. No current singular `prletter.sty` was recovered, and the old plural style was not renamed to impersonate it. The precise current journal-template requirement therefore remains an external verification item. The official general LaTeX page remains accessible and requires all Editorial Manager source files at one folder level.
