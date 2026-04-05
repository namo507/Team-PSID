# PSID Crisis Module Final Report

Simplified stakeholder-facing report for the refreshed crisis-module package.

Prepared for Elliot, Tom, and Mike  
Updated: April 2026

## Table of Contents

1. Executive summary
2. Background and objective
3. Methodology overview
4. Results
5. Discussion of skew and the financial-question issue
6. Deliverables for client use
7. Conclusion and next steps
8. References

## 1. Executive Summary

This project refreshed the PSID crisis-module pipeline so the final package is easier to explain, easier to deploy, and more transparent about how questions move from the historical archive into a clean client-facing instrument.

The current production run starts with 52 historical crisis questions and produces a final 28-question selected module. The ranking engine still uses the core utility-to-burden logic, but the client-facing category model has been simplified to only two labels:

- `Generic`
- `Specific`

This revision also removes the old practice of treating `Financial Crisis` as a separate final module category. Financial items now compete inside the broader `Specific` bank together with disaster and pandemic items.

### Headline results from the refreshed run

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
| Generic rows | 3 |
| Specific rows | 49 |

The most important interpretation point is this: the final package now uses a conservative binary split, a cleaner questionnaire output, and a clearer explanation of why some financial items rank highly while the broader financial block does not dominate the final module.

## 2. Background and Objective

PSID has accumulated a large amount of crisis-relevant content through modules tied to events such as the federal government shutdown, Hurricane Katrina, and COVID-19. The practical challenge is not whether useful items exist. The challenge is which ones should be retained in a short deployable module without overwhelming respondents.

The objective of this refresh was to produce a package that meets four client expectations:

1. Keep the categorization simple enough to explain in one sentence.
2. Preserve the numerical ranking logic so the shortlist is defensible.
3. Produce a deployable questionnaire that uses standardized wording rather than historical event phrasing.
4. Address the perception that the previous outputs were skewed toward financial material or overly dependent on demographics.

## 3. Methodology Overview

### 3.1 Data ingestion

The refreshed production build starts from `PSID_Ranked_Questions_Katrina_Integrated.csv`, which contains 52 historical questions from the integrated source bank. Those rows are normalized and rebuilt into a final ranked dataset rather than relying on the previously written final CSV as the only source of truth.

### 3.2 Keyword extraction and construct mapping

The current build reuses the precomputed keyword lists present in the integrated source file. Those keywords are matched against the project taxonomy and then collapsed into higher-level constructs such as:

- Economic / Income
- Employment
- Financial Coping
- Housing / Shelter
- Government Aid
- Trauma / Health
- Demographics

This step matters because the model does not rank questions only by wording length or source. It ranks them by the kind of crisis signal they provide.

### 3.3 Ranking logic

The baseline ranking score is the utility-to-burden ratio:

```text
Ri = Ui / Bi
```

Where burden is defined as:

```text
Bi = max(0.10 * word_count + 0.20 * complexity, 0.1)
```

The enhanced score used for richer prioritization is:

```text
Pi = augmented_utility / [Bi * (1 + 0.65 * redundancy_scaled)]
```

This second score is useful because it rewards distinctive wording and better construct coverage while penalizing repetition.

### 3.4 Binary category model

The client asked for a binary rule:

```text
If Ri >= 0.7 -> Generic
Else -> Specific
```

On the raw corpus, that rule is not workable because raw `Ri` is not naturally bounded between 0 and 1. In the refreshed run, the minimum raw `Ri` is `0.818`, so all 52 of 52 rows satisfy a raw `Ri >= 0.7` rule. That would effectively erase the distinction between Generic and Specific.

To preserve the requested threshold while keeping the result interpretable, the production pipeline applies the `0.7` cutoff to a min-max normalized `Ri` score:

```text
ri_threshold_score = (Ri - min(Ri)) / (max(Ri) - min(Ri))
```

The operational client-facing rule is therefore:

```text
If ri_threshold_score >= 0.70 -> Generic
Else -> Specific
```

This keeps the raw `Ri` ordering unchanged while producing a real binary category split.

## 4. Results

### 4.1 Category counts

| Category | Rows | Selected rows |
| --- | ---: | ---: |
| Generic | 3 | 3 |
| Specific | 49 | 25 |

### 4.2 Source composition of the selected module

| Source | Selected rows |
| --- | ---: |
| Hurricane Katrina 2007 | 14 |
| COVID-19 | 8 |
| Govt Shutdown Income | 3 |
| Understanding Society | 2 |
| Govt Shutdown Crisis | 1 |

### 4.3 Top Generic questions after the refresh

| Variable | Recommended wording | Ri | Pi |
| --- | --- | ---: | ---: |
| `GEN_LOSE_EARNINGS_PANDEMIC` | Did you lose earnings because of the pandemic? | 5.667 | 7.860 |
| `GEN_EXPERIENCED_FINANCIAL_DIFFICULTIES_C` | Have you experienced any financial difficulties because of the crisis? | 5.667 | 7.187 |
| `GEN_RECEIVE_STIMULUS_PAYMENT_OTHER` | Did you receive a stimulus payment or other emergency government support? | 4.667 | 6.328 |

### 4.4 What the selected module emphasizes

The construct profile of the selected module is led by:

- Trauma / Health
- Employment
- Housing / Shelter
- Government Aid
- Economic / Income

This is important because the current selected bank is not simply a financial hardship instrument. It is a broader crisis-impact instrument with strong direct-exposure and wellbeing content.

## 5. Discussion of Skew and the Financial-Question Issue

### 5.1 Why the previous outputs looked skewed

The earlier workflow used multiple final category labels, including a separate `Financial Crisis` bucket. That made it easy to read the outputs as if finance-related items were their own dominant module, even when many of those questions were actually competing with broader disruption, aid, housing, and trauma questions.

The refreshed workflow solves that interpretive problem by collapsing the final category model to just `Generic` and `Specific`.

### 5.2 Why financial items appear fewer in the final package

Financial questions appear fewer for three reasons.

First, the historical question bank contains a large amount of Katrina disaster content. That means direct exposure, housing damage, displacement, and trauma questions contribute many competitive specific items.

Second, a number of financial questions are close variants of one another. Once redundancy is penalized, several finance-related items lose rank relative to shorter, cleaner, and more distinctive questions.

Third, once the final category model is simplified, finance-specific items no longer sit inside their own labeled destination bucket. They are absorbed into `Specific` and must compete against pandemic and disaster questions on the same scale.

### 5.3 What still remains financially important

The refresh does not remove the financial signal. Instead, it concentrates it.

The final package still retains high-value items that capture:

- financial strain
- earnings loss
- government support receipt
- business interruption
- coping behavior under hardship

In other words, the financial material is still present, but it is no longer allowed to dominate the structure simply because it was previously given its own visible module label.

### 5.4 How demographics affect weighting

Demographic-only rows remain in the internal master questionnaire for traceability, but they do not carry the same crisis signal as substantive event items.

Observed averages in the refreshed corpus:

| Group | Rows | Average Ri | Average Pi |
| --- | ---: | ---: | ---: |
| Demographics only | 3 | 1.354 | 2.189 |
| Non-demographic crisis items | 49 | 2.253 | 2.584 |

That difference is expected. Demographic items provide useful context, but they do not usually encode the direct shock, aid exposure, housing instability, or trauma response that the crisis module is trying to measure.

## 6. Deliverables for Client Use

The refreshed package now includes four principal outputs for review and deployment.

| Deliverable | Use |
| --- | --- |
| `Master_Questionnaire.xlsx` | Internal review file listing all historical questions with variable names, source, universe, question type, traceability fields, and scores |
| `Deployable_Questionnaire.pdf` | Clean deployable instrument using standardized wording and excluding demographics |
| `Codebook.pdf` | Technical explanation of the pipeline, formulas, functions, threshold logic, and schema |
| `Final_Report.pdf` | Simplified client-facing report focused on logic, results, and interpretation |

These are designed to separate audiences cleanly:

- technical detail stays in the codebook
- deployment wording stays in the questionnaire
- narrative interpretation stays in the final report

## 7. Conclusion and Next Steps

The refreshed PSID crisis-module package is more coherent than the earlier version for three reasons.

First, the pipeline is now explicit about how it rebuilds the final scored dataset from the raw integrated source.

Second, the final classification logic is simplified to a binary `Generic` versus `Specific` model, which is much easier to explain to stakeholders.

Third, the package now clearly distinguishes between technical documentation, deployable wording, and stakeholder reporting.

Recommended next steps:

1. Review the three Generic items and confirm whether the client wants an even smaller always-on core or whether one pandemic-specific Generic item should be manually demoted for policy reasons.
2. Review the deployable questionnaire wording with Tom’s template side by side and confirm any universe wording changes before final sign-off.
3. Treat the figures and dashboard as supplemental analytical materials rather than part of the required client package unless explicitly requested.

## 8. References

1. Panel Study of Income Dynamics (PSID): Main Interview, 2021. ICPSR 39190.
2. Fifty Years of the Panel Study of Income Dynamics: Past, Present, and Future.
3. User Guide for the 2019 Interviewing Year.
4. User Guide for the 2021 Interviewing Year.
5. User Guide for the 2023 Interviewing Year.
6. PSID COVID-19 Measures documentation.
7. Economic Impact Payments and Household Spending During the Pandemic. NBER.
8. The Economic Impacts of COVID-19: Evidence from a New Public Database Built Using Private Sector Data.
9. Internal analytical source: `PSID Data Modeling Report Prompt Generation.md`.
