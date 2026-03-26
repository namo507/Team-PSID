# Team-PSID

PSID crisis-module optimization workflow, stakeholder artifacts, and presentation outputs for the final ranked questionnaire design.

## Live Artifacts

- Dashboard: https://namo507.github.io/Team-PSID/PSID_Crisis_Module_Dashboard.html?v=20260326
- Final report: https://namo507.github.io/Team-PSID/PSID_NLP_Optimization_Report_Final.html?v=20260326
- Questionnaire master viewer: https://namo507.github.io/Team-PSID/PSID_Module_Questionnaire_Master.html?v=20260326
- Generic questionnaire demo: https://namo507.github.io/Team-PSID/PSID_Generic_Module_Questionnaire.html?v=20260326
- Crisis-specific questionnaire demo: https://namo507.github.io/Team-PSID/PSID_Crisis_Specific_Questionnaire_Demo.html?v=20260326

## Presentation Outputs

- PDF deck: [PSID_Crisis_Module_Client_Deck.pdf](PSID_Crisis_Module_Client_Deck.pdf)
- PowerPoint deck: [PSID_Crisis_Module_Client_Deck.pptx](PSID_Crisis_Module_Client_Deck.pptx)
- PDF generator: [generate_psid_presentation_pdf.py](generate_psid_presentation_pdf.py)
- PowerPoint generator: [generate_psid_presentation.py](generate_psid_presentation.py)

## Project Goal

This repository builds a compact, deployable PSID crisis questionnaire from a larger cross-source question bank. The workflow ranks candidate items by analytical value relative to respondent burden, then generates synchronized stakeholder artifacts:

- a live dashboard for review and filtering
- a public-facing web report
- questionnaire demo pages for stakeholder walkthroughs
- a final ranked CSV with enhanced scoring fields
- a summary JSON and dashboard data payload
- presentation-ready PDF and PowerPoint decks

## Final Validated Results

The current final artifact set is based on the refreshed Katrina-integrated ranked-question workflow.

| Metric | Value |
| --- | ---: |
| Total ranked questions | 52 |
| Selected module questions | 28 |
| Selected module time | 29.17 min |
| Full corpus time | 68.95 min |
| Average Ri | 2.079 |
| Maximum Ri | 5.667 |
| Average Pi | 2.452 |
| Maximum Pi | 7.809 |
| Generic-core recommendations | 6 |
| Crisis-specific recommendations | 8 |

### Selected Toggle Composition

| Toggle | Selected |
| --- | ---: |
| Pandemic / Disaster | 20 |
| Generic Core | 7 |
| Financial Crisis | 1 |

### Selected Source Contribution

| Source | Selected |
| --- | ---: |
| Hurricane Katrina 2007 | 13 |
| COVID-19 | 8 |
| Govt Shutdown Income | 3 |
| Understanding Society | 3 |
| Govt Shutdown Crisis | 1 |

### Construct Coverage In The Selected Module

| Construct | Count |
| --- | ---: |
| Trauma / Health | 13 |
| Employment | 7 |
| Government Aid | 5 |
| Housing / Shelter | 5 |
| Economic / Income | 4 |
| Financial Coping | 3 |
| Demographics | 3 |

## Methodology

### 1. Build The Integrated Question Bank

Candidate questions are combined across five PSID-related sources:

- Hurricane Katrina 2007
- COVID-19
- Government shutdown income
- Government shutdown crisis
- Understanding Society

The working ranked dataset is [PSID_Ranked_Questions_Final.csv](PSID_Ranked_Questions_Final.csv).

### 2. Parse Keywords And Extract Constructs

The workflow uses [PSID_NLP_Crisis_Module_Structure.py](PSID_NLP_Crisis_Module_Structure.py) to:

- parse and tag crisis-relevant keywords
- extract construct labels from question text
- reuse timing assumptions such as `SECS_PER_WORD`

### 3. Compute Baseline Utility-To-Burden Ranking

Each question receives a baseline ratio:

```text
Ri = Ui / Bi
Bi = max(alpha * Ni + beta * Ci, 0.1)
```

Where:

- `Ui` is utility derived from taxonomy-weighted crisis signals
- `Bi` is burden driven by wording length and question complexity
- `alpha = 0.10`
- `beta = 0.20`

This baseline score is the core ranking signal used to surface concise, high-value items.

### 4. Compute Enhanced Priority For Deployability

The workflow then adds an augmented priority score:

```text
Pi = U* / [Bi * (1 + 0.65 * redundancy_scaled)]
U* = Ui * (1 + 0.32 * idf_scaled + 0.24 * construct_scaled + 0.12 * richness_scaled + portability_bonus)
```

This second layer improves selection and recommendation quality by incorporating:

- TF-IDF rarity
- cosine-similarity redundancy penalty
- construct richness and construct priority
- portable wording bonus

### 5. Apply Construct Priorities

The enhanced workflow uses the following construct weights:

| Construct | Weight |
| --- | ---: |
| Trauma / Health | 0.58 |
| Housing / Shelter | 0.55 |
| Government Aid | 0.48 |
| Financial Coping | 0.45 |
| Employment | 0.42 |
| Economic / Income | 0.40 |
| Demographics | 0.14 |

### 6. Select The Final Module Under A Hard Time Cap

The final benchmark module is chosen under a 30-minute deployment ceiling using:

- `SECS_PER_WORD = 7`
- `MAX_SECONDS = 1800`

This yields the current 28-question benchmark at 29.17 minutes.

### 7. Generate Synchronized Stakeholder Artifacts

The maintained generator writes synchronized outputs so the dashboard, report, notebook, and demos all reflect the same ranked-question file.

## Key Output Files

### Core Workflow

- [generate_psid_artifacts.py](generate_psid_artifacts.py): main artifact generator and scoring pipeline
- [PSID_NLP_Crisis_Module_Final.ipynb](PSID_NLP_Crisis_Module_Final.ipynb): final notebook entry point
- [PSID_NLP_Crisis_Module_Structure.py](PSID_NLP_Crisis_Module_Structure.py): shared parsing, tagging, construct extraction, and timing helpers

### Ranked Data And Summary Payloads

- [PSID_Ranked_Questions_Final.csv](PSID_Ranked_Questions_Final.csv): authoritative ranked dataset with enhanced fields
- [psid_artifact_summary.json](psid_artifact_summary.json): headline validated metrics
- [psid_dashboard_data.js](psid_dashboard_data.js): dashboard payload with rows, summary, and recommendations

### Web Artifacts

- [PSID_Crisis_Module_Dashboard.html](PSID_Crisis_Module_Dashboard.html): interactive dashboard
- [PSID_NLP_Optimization_Report_Final.html](PSID_NLP_Optimization_Report_Final.html): formatted final report
- [PSID_Module_Questionnaire_Master.html](PSID_Module_Questionnaire_Master.html): unified questionnaire viewer
- [PSID_Generic_Module_Questionnaire.html](PSID_Generic_Module_Questionnaire.html): expanded generic baseline demo
- [PSID_Crisis_Specific_Questionnaire_Demo.html](PSID_Crisis_Specific_Questionnaire_Demo.html): crisis-specific demo

### Figures

- [fig_top_ranked_questions.png](fig_top_ranked_questions.png)
- [fig_toggle_comparison.png](fig_toggle_comparison.png)
- [fig_utility_vs_burden.png](fig_utility_vs_burden.png)
- [fig_construct_heatmap.png](fig_construct_heatmap.png)
- [fig_time_budget.png](fig_time_budget.png)

## Recommendation Layer

The current workflow includes documentation-backed recommendation generation and deployable wording cleanup.

- 6 generic-core recommendations
- 8 crisis-specific recommendations
- portable wording cleanup for historically source-specific questions
- recommendation support scoring driven by top-matching Pi-ranked items

## Refresh Workflow

From the repository root:

```bash
python3 generate_psid_artifacts.py
python3 generate_psid_presentation.py
python3 generate_psid_presentation_pdf.py
```

This refreshes:

- the ranked CSV
- summary JSON
- dashboard payload
- figure PNGs
- dashboard-linked reporting assets
- presentation files

## Notes On GitHub Pages Links

The live HTML artifact links above include `?v=20260326` to avoid stale cached pages during review. If GitHub Pages has already refreshed in your browser, the base `.html` paths should also resolve normally.