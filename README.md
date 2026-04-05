# Team-PSID

PSID crisis-module optimization workflow for the maintained final client package.

The repository root is intentionally limited to the live rebuild code, the current validation notebook, the README, and the structured output folders. Legacy demos, presentation decks, old Office exports, superseded ranked datasets, alias outputs, and temporary files belong in `archive/`.

## Current Outputs

### Final client deliverables

- [deliverables/Master_Questionnaire.xlsx](deliverables/Master_Questionnaire.xlsx)
- [deliverables/Deployable_Questionnaire.pdf](deliverables/Deployable_Questionnaire.pdf)
- [deliverables/Codebook.pdf](deliverables/Codebook.pdf)
- [deliverables/Final_Report.pdf](deliverables/Final_Report.pdf)

### Client markdowns

- [docs/client 1.md](docs/client%201.md): technical codebook
- [docs/client 2.md](docs/client%202.md): deployable questionnaire
- [docs/client 3.md](docs/client%203.md): stakeholder final report

### Supporting reference

- [docs/reference/PSID Data Modeling Report Prompt Generation.md](docs/reference/PSID%20Data%20Modeling%20Report%20Prompt%20Generation.md): analytical note used during refinement

### Live scored assets

- [data/PSID_Ranked_Questions_Katrina_Integrated.csv](data/PSID_Ranked_Questions_Katrina_Integrated.csv)
- [data/PSID_Ranked_Questions_Final.csv](data/PSID_Ranked_Questions_Final.csv)
- [data/psid_artifact_summary.json](data/psid_artifact_summary.json)
- [data/psid_dashboard_data.js](data/psid_dashboard_data.js)

### Live figures

- [figures/fig_top_ranked_questions.png](figures/fig_top_ranked_questions.png)
- [figures/fig_toggle_comparison.png](figures/fig_toggle_comparison.png)
- [figures/fig_utility_vs_burden.png](figures/fig_utility_vs_burden.png)
- [figures/fig_construct_heatmap.png](figures/fig_construct_heatmap.png)
- [figures/fig_time_budget.png](figures/fig_time_budget.png)

## Root Files That Drive The Package

- [generate_psid_artifacts.py](generate_psid_artifacts.py): rebuilds the scored dataset, summary payload, dashboard data bundle, and figures
- [generate_client_documents.py](generate_client_documents.py): builds the spreadsheet and final PDFs
- [PSID_NLP_Crisis_Module_Structure.py](PSID_NLP_Crisis_Module_Structure.py): shared scoring and selection helpers
- [PSID_NLP_Crisis_Module_Final.ipynb](PSID_NLP_Crisis_Module_Final.ipynb): validation notebook for the current binary-model workflow

## Validated Metrics

| Metric | Value |
| --- | ---: |
| Total ranked questions | 52 |
| Selected scored questions | 28 |
| Deployable questions | 26 |
| Selected scored minutes | 29.98 |
| Full corpus minutes | 68.60 |
| Average Ri | 2.201 |
| Maximum Ri | 5.667 |
| Average Pi | 2.561 |
| Maximum Pi | 7.860 |
| Generic rows | 3 |
| Specific rows | 49 |

## Repository Layout

```text
Team-PSID/
├── data/               live ranked CSVs and summary payloads
├── deliverables/       final spreadsheet and PDFs
├── docs/               client markdown deliverables and supporting notes
├── figures/            current analytical PNGs
├── archive/            legacy demos, presentations, aliases, superseded notes
├── generate_psid_artifacts.py
├── generate_client_documents.py
├── PSID_NLP_Crisis_Module_Structure.py
└── PSID_NLP_Crisis_Module_Final.ipynb
```

## Refresh Workflow

From the repository root:

```bash
/usr/bin/python3 generate_psid_artifacts.py
/usr/bin/python3 generate_client_documents.py
```

That refresh path updates the live files under `data/`, `figures/`, and `deliverables/`.

## Archive Policy

- Keep only current package inputs, generators, notebook validation, figures, and client deliverables outside `archive/`.
- Move demos, superseded notebooks, deck files, old Office exports, aliases, and temporary files into `archive/`.
- Do not add new root-level outputs unless they are part of the maintained final package.