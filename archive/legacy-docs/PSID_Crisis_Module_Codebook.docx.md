# PSID Crisis Module Codebook

Technical documentation for the refreshed PSID crisis-module ranking pipeline.

Prepared for Tom and Mike  
Updated: April 2026

## Table of Contents

1. Purpose and scope
2. Files and workflow roles
3. End-to-end pipeline design
4. Core functions and what they do
5. Scoring formulas and calculation logic
6. Binary Generic vs Specific categorization
7. Demographic interaction notes
8. Output schema and client-facing deliverables
9. Refreshed benchmark results
10. References

## 1. Purpose and Scope

This codebook documents the current production pipeline used to evaluate, rank, categorize, and package crisis-module questions for PSID. It is intended to be technical enough for internal review, but still readable by non-engineering stakeholders.

The current revision makes four structural changes that matter for client delivery:

1. The final category model is now binary: `Generic` or `Specific`.
2. The previous separate `Financial Crisis` module label is no longer used as a final category.
3. The binary threshold rule is applied on a normalized Ri scale so the requested `0.7` cutoff is mathematically meaningful.
4. The final CSV is now rebuilt from the raw integrated source before every artifact refresh, rather than treating the previously written final CSV as the only input.

## 2. Files and Workflow Roles

| File | Role | Notes |
| --- | --- | --- |
| `PSID_Ranked_Questions_Katrina_Integrated.csv` | Raw integrated source bank | 52 historical questions with precomputed keywords and baseline fields. |
| `PSID_NLP_Crisis_Module_Structure.py` | Reusable scoring helpers | Holds constants, keyword parsing, taxonomy tagging, burden logic, threshold helpers, and time-budget selection. |
| `generate_psid_artifacts.py` | Production rebuild script | Rebuilds the ranked dataset, writes the final CSV, summary JSON, dashboard payload, and figures. |
| `PSID_Ranked_Questions_Final.csv` | Final scored output | The authoritative ranked table used by the notebook and client deliverables. |
| `PSID_NLP_Crisis_Module_Final.ipynb` | Validation notebook | Documents the production workflow and refresh path. |
| `psid_artifact_summary.json` | Benchmark summary | Stores the headline counts and scoring metrics from the latest rebuild. |
| `psid_dashboard_data.js` | Dashboard payload | Browser-ready data bundle written from the same final dataframe. |

## 3. End-to-End Pipeline Design

The current production sequence is:

```text
PSID_Ranked_Questions_Katrina_Integrated.csv
    -> normalize_ranked_questions()
    -> parse_keywords()
    -> tag_keywords()
    -> extract_constructs()
    -> compute_utility()
    -> compute_burden()
    -> Ri calculation
    -> assign_binary_categories()
    -> compute_augmented_scores()
    -> select_for_time_budget()
    -> PSID_Ranked_Questions_Final.csv
    -> summary JSON, dashboard JS, figures, questionnaires, PDFs
```

This structure removes an important source of drift: the final output is no longer assumed to be already correct. It is regenerated from the raw integrated file each time.

## 4. Core Functions and What They Do

### 4.1 Functions in `PSID_NLP_Crisis_Module_Structure.py`

| Function | Purpose | Output |
| --- | --- | --- |
| `normalize_ranked_questions()` | Restores canonical column names from the integrated CSV. | Clean dataframe with `question_text`, `toggle_category`, `word_count`, and related fields. |
| `parse_keywords()` | Converts stored keyword strings into Python lists. | `list[str]` |
| `tag_keywords()` | Maps parsed keywords to the project taxonomy and construct weights. | List of `{keyword, construct, weight}` records. |
| `extract_constructs()` | Collapses tagged keywords to unique construct labels. | Ordered list of construct names. |
| `compute_word_count()` | Counts words in the question text. | Integer token count. |
| `compute_complexity()` | Estimates linguistic complexity from named entities and clause markers. | Float complexity score. |
| `compute_utility()` | Sums keyword weights to produce `Ui`. | Utility score. |
| `compute_burden()` | Computes `Bi` from word count and complexity. | Burden score. |
| `min_max_scale()` | Min-max scales a numeric series. | Normalized series in `[0, 1]`. |
| `assign_binary_categories()` | Applies the binary threshold rule using normalized `Ri`. | `ri_threshold_score` and final `toggle_category`. |
| `select_for_time_budget()` | Greedy selection under the 30-minute limit. | Updated `selected_for_module` flag. |

### 4.2 Functions in `generate_psid_artifacts.py`

| Function | Purpose | Output |
| --- | --- | --- |
| `build_ranked_dataset()` | Rebuilds the final dataframe from the raw integrated source. | Scored dataframe with `Ri`, `Pi`, categories, wording, and selection flags. |
| `compute_augmented_scores()` | Computes IDF, redundancy, construct bonus, portability bonus, `augmented_utility`, and `Pi`. | Enhanced scoring fields. |
| `suggest_deployable_wording()` | Rephrases historical questions into deployable client wording. | Portable question text. |
| `build_variable_names()` | Creates deterministic `GEN_...` and `SPC_...` identifiers. | `variable_name` column. |
| `write_ranked_csv()` | Writes the refreshed final CSV. | `PSID_Ranked_Questions_Final.csv` |
| `build_summary()` | Writes global benchmark counts and metrics. | `psid_artifact_summary.json` |
| `write_dashboard_data()` | Writes the browser-ready payload. | `psid_dashboard_data.js` |
| `plot_top_ranked()` and related plot functions | Generate the analysis figures. | PNG artifacts. |
| `build_all()` | Runs the supported end-to-end rebuild. | Synchronized outputs across the repo. |

## 5. Scoring Formulas and Calculation Logic

### 5.1 Utility

The baseline utility score is the sum of taxonomy weights attached to matched keywords.

```text
Ui = sum(weight_k for matched keyword k)
```

Example: `Lost earnings because of the pandemic`

| Keyword | Construct | Weight |
| --- | --- | ---: |
| `earnings` | Economic / Income | 0.80 |
| `lost earnings` | Economic / Income | 0.80 |
| `pandemic` | Trauma / Health | 0.90 |
| `the pandemic` | Trauma / Health | 0.90 |

```text
Ui = 0.80 + 0.80 + 0.90 + 0.90 = 3.40
```

### 5.2 Burden

```text
Bi = max(0.10 * word_count + 0.20 * complexity, 0.1)
```

Example: `Any financial difficulties`

```text
word_count = 3
complexity = 0.0
Bi = max(0.10 * 3 + 0.20 * 0.0, 0.1)
   = max(0.30, 0.1)
   = 0.30
```

### 5.3 Baseline Rank Index

```text
Ri = Ui / Bi
```

Example: `Any financial difficulties`

```text
Ri = 1.70 / 0.30 = 5.667
```

### 5.4 Time Estimate

```text
minutes = (word_count * 7) / 60
```

Example: `Any financial difficulties`

```text
minutes = (3 * 7) / 60 = 0.35
```

### 5.5 Enhanced Priority Score

```text
Pi = augmented_utility / [Bi * (1 + 0.65 * redundancy_scaled)]
```

Where:

```text
augmented_utility = Ui * (1 + 0.32 * idf_scaled + 0.24 * construct_scaled + 0.12 * richness_scaled + portability_bonus)
```

### 5.6 Worked Example

Example question: `Lost earnings because of the pandemic`

| Field | Value | Calculation |
| --- | ---: | --- |
| `Ui` | 3.400 | `0.80 + 0.80 + 0.90 + 0.90` |
| `Bi` | 0.600 | `0.10 * 6 + 0.20 * 0.0` |
| `Ri` | 5.667 | `3.40 / 0.60` |
| `ri_threshold_score` | 1.000 | `(5.667 - 0.818) / (5.667 - 0.818)` |
| Category | `Generic` | `ri_threshold_score >= 0.70` |
| `Pi` | 7.860 | Computed from `augmented_utility`, burden, and redundancy penalty |

## 6. Binary Generic vs Specific Categorization

### 6.1 Requested threshold and implementation detail

The client request specified a binary category rule:

```text
If RI >= 0.7 -> Generic
Else -> Specific
```

Applied directly to raw `Ri`, this rule is not usable on the current corpus because raw `Ri` is not bounded between 0 and 1.

Observed raw distribution on the refreshed corpus:

| Measure | Value |
| --- | ---: |
| Minimum raw `Ri` | 0.818 |
| Maximum raw `Ri` | 5.667 |
| Rows with raw `Ri >= 0.7` | 52 of 52 |

That would collapse the final category split and make the requested binary model meaningless.

### 6.2 Operational rule used in production

To preserve the requested `0.7` cutoff while keeping the split interpretable, the pipeline applies the threshold to a min-max normalized `Ri` value:

```text
ri_threshold_score = (Ri - min(Ri)) / (max(Ri) - min(Ri))

If ri_threshold_score >= 0.70 -> Generic
Else -> Specific
```

This yields a stable binary category without changing the underlying `Ri` ordering itself.

### 6.3 Refreshed category counts

| Category | Rows | Selected rows |
| --- | ---: | ---: |
| Generic | 3 | 3 |
| Specific | 49 | 25 |

### 6.4 Traceability

The final CSV keeps both:

- `toggle_category`: the new binary output (`Generic` or `Specific`)
- `historical_toggle_category`: the previous source-derived label such as `Generic Core`, `Toggle: Pandemic / Disaster`, or `Toggle: Financial Crisis`

That preserves traceability while meeting the new client-facing classification requirement.

## 7. Demographic Interaction Notes

The current corpus contains two clean groups:

1. demographics-only items
2. non-demographic crisis items

No mixed demographic-plus-crisis items appear in the refreshed final table.

Observed interaction summary:

| Demographic flag | Non-demographic flag | Rows | Average Ri | Average Pi |
| --- | --- | ---: | ---: | ---: |
| `False` | `True` | 49 | 2.253 | 2.584 |
| `True` | `False` | 3 | 1.354 | 2.189 |

Interpretation:

- Demographic-only items receive lower average `Ri` because they are short but carry limited direct crisis signal.
- Non-demographic items score higher because they activate substantive constructs such as Trauma / Health, Housing / Shelter, Government Aid, Employment, and Financial Coping.
- This is why the refreshed binary model does not keep demographics in the deployable questionnaire even though they remain in the master questionnaire for internal traceability.

## 8. Output Schema and Client-Facing Deliverables

### 8.1 Final CSV schema highlights

The refreshed final CSV now includes these fields that matter for client-facing documentation:

| Field | Purpose |
| --- | --- |
| `variable_name` | Stable identifier used across documents and questionnaires |
| `toggle_category` | Final binary category (`Generic` or `Specific`) |
| `historical_toggle_category` | Legacy category retained for traceability |
| `ri_threshold_score` | Normalized Ri used for binary classification |
| `recommended_wording` | Deployable client-facing wording |
| `Ri`, `Pi` | Baseline and enhanced ranking metrics |
| `selected_for_module` | Final time-budget selection flag |

### 8.2 Deliverables built from the refreshed dataset

| Deliverable | Purpose |
| --- | --- |
| `Master_Questionnaire.xlsx` | Internal comprehensive question list including demographics and traceability fields |
| `Deployable_Questionnaire.pdf` | Clean deployable instrument using rephrased wording and excluding demographics |
| `Codebook.pdf` | Technical PDF version of this codebook |
| `Final_Report.pdf` | Simplified client-facing report |

## 9. Refreshed Benchmark Results

Latest production rebuild from `generate_psid_artifacts.py`:

| Metric | Value |
| --- | ---: |
| Total ranked questions | 52 |
| Selected questions | 28 |
| Selected minutes | 29.98 |
| Full corpus minutes | 68.60 |
| Average Ri | 2.201 |
| Maximum Ri | 5.667 |
| Average Pi | 2.561 |
| Maximum Pi | 7.860 |
| Generic recommendations | 6 |
| Specific recommendations | 8 |

Top Generic questions by refreshed binary model:

| Variable | Recommended wording | Ri | Pi |
| --- | --- | ---: | ---: |
| `GEN_LOSE_EARNINGS_PANDEMIC` | Did you lose earnings because of the pandemic? | 5.667 | 7.860 |
| `GEN_EXPERIENCED_FINANCIAL_DIFFICULTIES_C` | Have you experienced any financial difficulties because of the crisis? | 5.667 | 7.187 |
| `GEN_RECEIVE_STIMULUS_PAYMENT_OTHER` | Did you receive a stimulus payment or other emergency government support? | 4.667 | 6.328 |

## 10. References

1. Panel Study of Income Dynamics (PSID): Main Interview, 2021. ICPSR 39190.
2. Fifty Years of the Panel Study of Income Dynamics: Past, Present, and Future.
3. Technical Report: 2021 PSID Longitudinal Individual and Family Weights.
4. User Guide for the 2019 Interviewing Year.
5. User Guide for the 2023 Interviewing Year.
6. User Guide for the 2021 Interviewing Year.
7. PSID COVID-19 Measures documentation.
8. NBER evidence on Economic Impact Payments and household spending during the pandemic.
9. Evidence on the economic impacts of COVID-19 using private-sector data.
10. Internal source file: `PSID Data Modeling Report Prompt Generation.md`.
