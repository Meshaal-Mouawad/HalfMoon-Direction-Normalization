#!/usr/bin/env bash
# V12 journal package build: one Mac folder, one repo, one main branch.
set -euo pipefail

ROOT="$HOME/Documents/Research/HalfMoon-Direction-Normalization"
BASE="$ROOT/submission/PRL_V11_Final"
EDIT="$BASE/Editable_LaTeX"
UP="$BASE/Journal_Upload"
VER="$BASE/Verification"
REPO="Meshaal-Mouawad/HalfMoon-Direction-Normalization"
STAMP="$(date +%Y%m%d-%H%M%S)"

cd "$ROOT"
test "$(git branch --show-current)" = "main"
test "$(git remote get-url origin)" = "https://github.com/$REPO.git" || {
  echo "STOP: unexpected origin"; exit 1;
}
test -z "$(git status --porcelain)" || {
  echo "STOP: uncommitted changes"; git status --short; exit 1;
}
git pull --ff-only origin main
for bin in pdflatex bibtex python3 pdfinfo zip unzip rsync shasum git; do
  command -v "$bin" >/dev/null || { echo "STOP: missing $bin"; exit 1; }
done

# Preserve prior submitted PDF and source files outside tracked Git content.
mkdir -p "$ROOT/archive/V11_before_V12_$STAMP" "$VER"
cp -p "$UP/Manuscript.pdf" "$UP/Supplement.pdf" \
  "$UP/Threshold_Addendum.pdf" "$UP/LaTeX_Source.zip" \
  "$ROOT/archive/V11_before_V12_$STAMP/"

echo "=== CLEAN BUILD OF V12 SOURCE ==="
(
  cd "$EDIT"
  bash build.sh > "$VER/V12_Build.log" 2>&1
) || {
  tail -100 "$VER/V12_Build.log"
  echo "STOP: LaTeX build failed. Prior journal files unchanged."
  exit 1
}

pages() { pdfinfo "$EDIT/$1.pdf" | awk '/^Pages:/ {print $2}'; }
MAIN="$(pages Manuscript)"
SUPP="$(pages Supplement)"
ADD="$(pages Threshold_Addendum)"
echo "Main: $MAIN pages; Supplement: $SUPP; Threshold Addendum: $ADD"
if [ "$MAIN" -gt 7 ]; then
  echo "STOP: main article exceeds seven-page PRL initial limit."
  echo "Prior journal files unchanged. Inspect V12_Build.log."
  exit 1
fi
test "$MAIN" -ge 6 && test "$SUPP" -ge 18 && test "$ADD" -ge 3

echo "=== SYNCHRONIZE SUBMISSION PDFS ==="
for name in Manuscript Supplement Threshold_Addendum; do
  cp "$EDIT/$name.pdf" "$UP/$name.pdf"
  cmp "$EDIT/$name.pdf" "$UP/$name.pdf"
done

echo "=== REPACKAGE LATEX WITH SIBLING FIGURES ==="
TMP="$(mktemp -d /tmp/HalfMoonV12.XXXXXX)"
trap 'rm -rf "$TMP"' EXIT
mkdir -p "$TMP/Manuscript" "$TMP/Figures"
rsync -a \
  --exclude='*.aux' --exclude='*.log' --exclude='*.blg' \
  --exclude='*.abs' --exclude='*.pdf' --exclude='*.out' \
  --exclude='*.synctex*' "$EDIT/" "$TMP/Manuscript/"
rsync -a "$BASE/Figures/" "$TMP/Figures/"
rm -f "$UP/LaTeX_Source.zip"
(
 cd "$TMP"
 zip -q -r "$UP/LaTeX_Source.zip" Manuscript Figures
)
unzip -tq "$UP/LaTeX_Source.zip" >/dev/null

echo "=== CHECKSUM AND PRODUCTION RECORD ==="
(
  cd "$UP"
  find . -maxdepth 1 -type f -print0 |
     sort -z | xargs -0 shasum -a 256
) > "$VER/SHA256SUMS.txt"
cat > "$VER/V12_Production_Results.txt" <<EOF
V12 clean build: PASS
Main pages: $MAIN (limit 7)
Supplement pages: $SUPP
Threshold addendum pages: $ADD
Rebuilt source ZIP: PASS
Upload PDFs equal compiled PDFs: PASS
Submitted original V11 files preserved under archive/V11_before_V12_$STAMP/
Visual page inspection: REQUIRED
Editorial resubmission: NOT PERFORMED
EOF
cat > "$BASE/FINAL_STATUS.txt" <<EOF
Half-Moon manuscript PRLETTERS-D-26-03032
V12 reader-first revision build: PASS
Manuscript: $MAIN pages
Supplement: $SUPP pages
Threshold Addendum: $ADD pages
Journal PDFs and LaTeX source ZIP synchronized.
Public V11 research data release preserved.
Signed Authorship Confirmation: upload under Cover letter.
Next: inspect final PDF and approve revised submission in Editorial Manager.
EOF

# One-time cloud workflow can be removed after a successful local build.
if git ls-files --error-unmatch .github/workflows/v12-prl-one-time-build.yml >/dev/null 2>&1; then
  git rm -f .github/workflows/v12-prl-one-time-build.yml
fi

git add -A submission/PRL_V11_Final
git diff --cached --quiet && {
  echo "STOP: No updated files staged"; exit 1;
}
git commit -m "Compile and verify V12 PRL manuscript and submission source"
git push origin main
test -z "$(git status --porcelain)"
test "$(git ls-remote --heads origin | wc -l | tr -d ' ')" = "1"

echo "PASS: V12 $MAIN-page manuscript and source ZIP synchronized."
echo "PASS: One Mac research folder; one GitHub repository; one main branch."
echo "NEXT: visually check PDFs; upload signed form and revised files."
open "$UP"
