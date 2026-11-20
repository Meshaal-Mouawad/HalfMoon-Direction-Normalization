#!/usr/bin/env bash
# Build the supplement first, regenerate its labels, then build the main article.
# BIBTEX=/path/to/bibtex may be supplied to select a particular installation.
set -euo pipefail
cd "$(dirname "$0")"
for tool in pdflatex python3; do
  command -v "$tool" >/dev/null 2>&1 || { echo "Required tool not found: $tool" >&2; exit 1; }
done
if [[ -z "${BIBTEX:-}" ]]; then
  if command -v bibtex >/dev/null 2>&1; then
    BIBTEX="$(command -v bibtex)"
  elif command -v bibtex.original >/dev/null 2>&1; then
    BIBTEX="$(command -v bibtex.original)"
  else
    echo "BibTeX was not found. Install it or set BIBTEX to its executable path." >&2
    exit 1
  fi
fi
for stem in Supplement Manuscript; do
  pdflatex -interaction=nonstopmode -halt-on-error -file-line-error "$stem.tex"
  "$BIBTEX" "$stem"
  pdflatex -interaction=nonstopmode -halt-on-error -file-line-error "$stem.tex"
  pdflatex -interaction=nonstopmode -halt-on-error -file-line-error "$stem.tex"
  if grep -Ei 'Missing character:|Undefined control sequence|LaTeX Error:|There were undefined (references|citations)' "$stem.log"; then
    echo "Build verification failed: inspect $stem.log." >&2
    exit 1
  fi
  if [[ "$stem" == "Supplement" ]]; then
    python3 export_supplement_labels.py
  fi
done
echo "Built Manuscript.pdf and Supplement.pdf with regenerated bibliographies."
echo "Inspect the rendered mathematics after changes to the TeX installation."

# Additional mathematical result; its proof is self-contained and has no bibliography.
for pass in 1 2; do
  pdflatex -interaction=nonstopmode -halt-on-error -file-line-error Threshold_Addendum.tex
done
if grep -Ei 'Missing character:|Undefined control sequence|LaTeX Error:|There were undefined (references|citations)' Threshold_Addendum.log; then
  echo "Threshold addendum verification failed." >&2; exit 1
fi
echo "Built Threshold_Addendum.pdf."
