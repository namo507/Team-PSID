#!/usr/bin/env zsh
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/../../.." && pwd)"
SRC_DIR="$ROOT_DIR/docs/latex/codebook_visuals"
FIGURES_DIR="$ROOT_DIR/figures"
OUT_DIR="$ROOT_DIR/deliverables/Client_1_Technical_Codebook_Visuals"

mkdir -p "$OUT_DIR"

cp -f "$FIGURES_DIR/fig_top_ranked_questions.png" "$OUT_DIR/"
cp -f "$FIGURES_DIR/fig_toggle_comparison.png" "$OUT_DIR/"
cp -f "$FIGURES_DIR/fig_utility_vs_burden.png" "$OUT_DIR/"
cp -f "$FIGURES_DIR/fig_construct_heatmap.png" "$OUT_DIR/"
cp -f "$FIGURES_DIR/fig_time_budget.png" "$OUT_DIR/"

for name in workflow_pipeline_diagram function_pipeline_map scoring_algorithm_anatomy; do
  latexmk -cd -pdf -interaction=nonstopmode -halt-on-error -outdir="$OUT_DIR" "$SRC_DIR/$name.tex"
  sips -s format png -s dpiWidth 220 -s dpiHeight 220 "$OUT_DIR/$name.pdf" --out "$OUT_DIR/$name.png" >/dev/null
done

cat > "$OUT_DIR/README.md" <<'EOF'
# Client 1 Technical Codebook Visuals

This folder contains the updated visual assets used by the technical codebook.

Included assets:

- `fig_top_ranked_questions.png`
- `fig_toggle_comparison.png`
- `fig_utility_vs_burden.png`
- `fig_construct_heatmap.png`
- `fig_time_budget.png`
- `workflow_pipeline_diagram.pdf`
- `workflow_pipeline_diagram.png`
- `function_pipeline_map.pdf`
- `function_pipeline_map.png`
- `scoring_algorithm_anatomy.pdf`
- `scoring_algorithm_anatomy.png`

The PNG plots are copied from `figures/`.
The three workflow diagrams are exported from standalone LaTeX/TikZ sources in `docs/latex/codebook_visuals/`.
EOF

latexmk -cd -c -outdir="$OUT_DIR" "$SRC_DIR/workflow_pipeline_diagram.tex"
latexmk -cd -c -outdir="$OUT_DIR" "$SRC_DIR/function_pipeline_map.tex"
latexmk -cd -c -outdir="$OUT_DIR" "$SRC_DIR/scoring_algorithm_anatomy.tex"