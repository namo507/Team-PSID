#!/usr/bin/env zsh
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
SRC_DIR="$ROOT_DIR/docs/latex"
OUT_DIR="$ROOT_DIR/deliverables"

mkdir -p "$OUT_DIR"

latexmk -cd -pdf -interaction=nonstopmode -halt-on-error -outdir="$OUT_DIR" "$SRC_DIR/client_1_technical_codebook.tex"
latexmk -cd -pdf -interaction=nonstopmode -halt-on-error -outdir="$OUT_DIR" "$SRC_DIR/client_2_deployable_questionnaire.tex"
latexmk -cd -pdf -interaction=nonstopmode -halt-on-error -outdir="$OUT_DIR" "$SRC_DIR/client_3_final_report.tex"

mv -f "$OUT_DIR/client_1_technical_codebook.pdf" "$OUT_DIR/Client_1_Technical_Codebook.pdf"
mv -f "$OUT_DIR/client_2_deployable_questionnaire.pdf" "$OUT_DIR/Client_2_Deployable_Questionnaire.pdf"
mv -f "$OUT_DIR/client_3_final_report.pdf" "$OUT_DIR/Client_3_Final_Report.pdf"

latexmk -cd -c -outdir="$OUT_DIR" "$SRC_DIR/client_1_technical_codebook.tex"
latexmk -cd -c -outdir="$OUT_DIR" "$SRC_DIR/client_2_deployable_questionnaire.tex"
latexmk -cd -c -outdir="$OUT_DIR" "$SRC_DIR/client_3_final_report.tex"