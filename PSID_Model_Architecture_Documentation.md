# PSID Crisis Module Model Architecture Documentation

This document explains, in plain language, how the PSID crisis-module workflow turns a large bank of candidate questions into a short, deployable questionnaire. It is designed as a companion to:

-   [PSID_Model_Architecture_Documentation.pdf](PSID_Model_Architecture_Documentation.pdf)
-   [PSID_NLP_Crisis_Module_Final.ipynb](PSID_NLP_Crisis_Module_Final.ipynb)
-   [generate_psid_artifacts.py](generate_psid_artifacts.py)
-   [PSID_NLP_Crisis_Module_Structure.py](PSID_NLP_Crisis_Module_Structure.py)

The goal is not just to show formulas. The goal is to explain what each function does, what each weight means, and how those pieces combine to produce the final numbers used in the dashboard, report, and questionnaire artifacts.

## 1. What This Project Is Doing

The project starts with a question bank collected from several PSID-related crisis sources. It then uses a scoring workflow to answer three practical questions:

1.  Which questions are most useful for understanding crisis impact?
2.  Which questions are short enough and clear enough to keep respondent burden low?
3.  Which questions should stay in the always-on Generic Core and which should remain crisis-specific toggles?

The final workflow does not just rank questions by keyword relevance. It uses a two-layer scoring system:

-   `Ri`: a baseline utility-to-burden ratio
-   `Pi`: an enhanced priority score that also considers rarity, construct importance, construct richness, portability, and redundancy

The current validated final outputs are:

| Metric | Value | Calculation / rule |
|----------------------|----------------------------:|----------------------|
| Total ranked questions | 52 | `rows = len(df) = 52` |
| Selected questions | 28 | `selected_rows = len(df[df["selected"]]) = 28` |
| Selected minutes | 29.17 | `selected_minutes = sum(word_count * 7 / 60 for selected rows) = 29.17` |
| Full corpus minutes | 68.95 | `all_minutes = sum(word_count * 7 / 60 for all 52 rows) = 68.95` |
| Average Ri | 2.079 | `avg_ri = mean(Ri across all rows) = 2.079` |
| Maximum Ri | 5.667 | `max_ri = max(Ri across all rows) = 5.667` |
| Average Pi | 2.452 | `avg_pi = mean(Pi across all rows) = 2.452` |
| Maximum Pi | 7.809 | `max_pi = max(Pi across all rows) = 7.809` |

## 2. The Main Files And What They Do

### [PSID_NLP_Crisis_Module_Final.ipynb](PSID_NLP_Crisis_Module_Final.ipynb)

This notebook is the guided explanation and validation layer.

It does four main things:

1.  Loads the authoritative ranked CSV.
2.  Summarizes the final selected module.
3.  Reviews the highest-ranked questions and the linked stakeholder-facing artifacts.
4.  Runs the supported refresh path through `build_all()`.

The notebook is important because it helps explain the workflow in steps, but it is not a separate scoring system. It uses the same functions as the production artifact pipeline.

### [PSID_NLP_Crisis_Module_Structure.py](PSID_NLP_Crisis_Module_Structure.py)

This file contains the lower-level helpers and constants used by the scoring workflow.

It provides:

-   burden constants such as `ALPHA`, `BETA`, `SECS_PER_WORD`, and `MAX_SECONDS`
-   keyword parsing
-   keyword tagging against the project taxonomy
-   construct extraction from tagged keywords

### [generate_psid_artifacts.py](generate_psid_artifacts.py)

This is the main production generator.

It:

-   loads the final ranked CSV
-   computes the enhanced scoring fields
-   writes the refreshed ranked CSV
-   writes the summary JSON
-   writes the dashboard JavaScript bundle
-   regenerates figures
-   keeps the dashboard, report, and demo pages synchronized

## 3. Workflow Architecture In Plain Language

The workflow can be understood as a sequence of stages:

1.  Start with the ranked CSV of candidate questions.
2.  Parse and tag the keywords in each question.
3.  Convert tagged keywords into higher-level constructs such as Employment, Housing / Shelter, or Trauma / Health.
4.  Compute a baseline score that asks: how much useful information do we get per unit of burden?
5.  Compute an enhanced score that asks: after we account for rarity, construct importance, construct richness, portability, and redundancy, which questions are still the strongest?
6.  Select the final module under a hard time limit.
7.  Write the outputs used by the notebook, dashboard, report, and demos.

This is why the notebook emphasizes `build_all()` as the supported refresh path. One function refreshes all downstream outputs from the same ranked-question source of truth.

## 4. Key Functions And What They Do

### Functions in [PSID_NLP_Crisis_Module_Structure.py](PSID_NLP_Crisis_Module_Structure.py)

| Function | What it does | Why it matters |
|------------------------|------------------------|------------------------|
| `parse_keywords()` | Converts the stored keyword text into a clean Python list. | Without this step, the scoring code cannot work with the keyword field consistently. |
| `tag_keywords()` | Matches each keyword to the project taxonomy and assigns a construct and weight. | This is how the model turns raw terms into meaningful crisis concepts. |
| `extract_constructs()` | Pulls out the construct labels from the tagged keywords. | This gives each question a structured construct profile used later in scoring. |

### Functions in [generate_psid_artifacts.py](generate_psid_artifacts.py)

| Function | What it does | Why it matters |
|------------------------|------------------------|------------------------|
| `load_dataset()` | Reads the final CSV, parses keywords, tags them, extracts constructs, derives `selected`, computes minutes, and then calls the enhanced scoring logic. | This is the entry point for the whole scoring pipeline. |
| `compute_augmented_scores()` | Adds rarity, redundancy, construct bonus, portability bonus, augmented utility, and final `Pi`. | This is where the enhanced ranking model actually happens. |
| `construct_bonus()` | Combines rarity, priority, and richness into one construct-level bonus term. | This is the main bridge between the construct dictionary and final scoring. |
| `portability_bonus()` | Rewards wording that is reusable across crisis types. | This helps the model prefer deployable, generalizable question wording. |
| `suggest_deployable_wording()` | Rewrites source-specific wording into more portable and stakeholder-friendly question text. | This helps move from historical items to field-ready prompts. |
| `build_design_recommendations()` | Uses high-Pi evidence to build recommendation sets for generic-core and crisis-specific wording. | This turns scoring into a design-support layer rather than just a ranking table. |
| `build_summary()` | Writes the summary metrics used by the report and dashboard. | This is where the headline numbers come from. |
| `write_dashboard_data()` | Writes the browser-ready JavaScript payload used by the dashboard. | This keeps the dashboard aligned with the latest scored data. |
| `plot_*()` functions | Regenerate the main figure outputs. | These create the charts used in the report and presentation materials. |
| `build_all()` | Runs the full refresh path in order. | This is the supported end-to-end artifact refresh path. |

## 5. The Baseline Formula: Ri

The baseline ranking score is:

``` text
Ri = Ui / Bi
```

Where burden is defined as:

``` text
Bi = max(0.10 * word_count + 0.20 * complexity, 0.1)
```

### What this means in simple language

-   `Ui` is the information value of the question.
-   `Bi` is the burden of asking it.
-   A question gets a high `Ri` if it tells us something important without being too long or too complex.

### Where these constants come from

In [PSID_NLP_Crisis_Module_Structure.py](PSID_NLP_Crisis_Module_Structure.py), the workflow defines:

-   `ALPHA = 0.10`
-   `BETA = 0.20`
-   `SECS_PER_WORD = 7`
-   `MAX_SECONDS = 30 * 60`

These are workflow design parameters, not regression-estimated coefficients.

## 6. The Enhanced Formula: Pi

The enhanced priority score is:

``` text
Pi = augmented_utility / [Bi * (1 + 0.65 * redundancy_scaled)]
```

Where augmented utility is:

``` text
augmented_utility = Ui * (1 + 0.32 * idf_scaled + 0.24 * construct_scaled + 0.12 * richness_scaled + portability_bonus)
```

### What this means in simple language

`Pi` is a more practical ranking score than `Ri`.

It still starts with utility and burden, but it also asks:

-   Is this wording rare enough to add something distinctive?
-   Does this question cover important constructs?
-   Does it cover more than one important construct?
-   Is the wording reusable outside one historical event?
-   Is the question too similar to other questions already in the bank?

That is why `Pi` is the better score for final selection and recommendation design.

### How the scaled terms are calculated

The enhanced model uses min-max scaling for several intermediate fields. In the current scored dataset, the ranges are:

| Scaled field | Min input | Max input | Calculation / rule |
|-----------------|------------------:|------------------:|-----------------|
| `idf_scaled` | 2.7805 | 4.2771 | `(idf_strength - 2.7805) / (4.2771 - 2.7805)` |
| `redundancy_scaled` | 0.0000 | 1.0000 | `(redundancy_penalty - 0.0) / (1.0 - 0.0)` |
| `construct_scaled` | 2.1457 | 17.8633 | `(construct_bonus - 2.1457) / (17.8633 - 2.1457)` |
| `richness_scaled` | 1 | 2 | `(construct_count - 1) / (2 - 1)` |

## 7. The Construct-Priority Weights

The workflow defines the following construct weights in `CONSTRUCT_PRIORITY`:

These weights are fixed design constants inside the code. They are not learned from the data. The calculation column shows the exact rule by which each value enters the scoring workflow.

| Construct | Weight | Calculation / rule |
|----------------------|----------------------------:|----------------------|
| Trauma / Health | 0.58 | Direct constant assignment: `CONSTRUCT_PRIORITY["Trauma / Health"] = 0.58`; if this is the only construct on a question, then `priority = 0.58`. |
| Housing / Shelter | 0.55 | Direct constant assignment: `CONSTRUCT_PRIORITY["Housing / Shelter"] = 0.55`; used inside `priority = mean(weights for included constructs)`. |
| Government Aid | 0.48 | Direct constant assignment: `CONSTRUCT_PRIORITY["Government Aid"] = 0.48`; used inside `priority = mean(weights for included constructs)`. |
| Financial Coping | 0.45 | Direct constant assignment: `CONSTRUCT_PRIORITY["Financial Coping"] = 0.45`; used inside `priority = mean(weights for included constructs)`. |
| Employment | 0.42 | Direct constant assignment: `CONSTRUCT_PRIORITY["Employment"] = 0.42`; used inside `priority = mean(weights for included constructs)`. |
| Economic / Income | 0.40 | Direct constant assignment: `CONSTRUCT_PRIORITY["Economic / Income"] = 0.40`; used inside `priority = mean(weights for included constructs)`. |
| Demographics | 0.14 | Direct constant assignment: `CONSTRUCT_PRIORITY["Demographics"] = 0.14`; used inside `priority = mean(weights for included constructs)`. |

### Why these weights matter

These weights tell the model that not all constructs are equally important.

-   Trauma / Health and Housing / Shelter are weighted highly because they capture direct crisis impact.
-   Government Aid and Financial Coping are also important because they capture how households respond and recover.
-   Demographics are still useful, but they provide context rather than direct crisis impact, so they receive less weight.

## 8. Construct Bonus Explained In Detail

The construct bonus combines three ideas:

1.  Rarity
2.  Priority
3.  Richness

In code, the logic is:

``` text
rarity = mean(1 / construct_frequency) * N
priority = mean(CONSTRUCT_PRIORITY[name])
richness = number of unique constructs
construct_bonus = rarity + priority + 0.08 * richness
```

### 8.1 Rarity

Rarity gives more credit to constructs that do not appear everywhere.

Why? Because if a construct is less common across the question bank, a question that captures it may be adding distinctive information.

Example:

-   If a construct appears in many questions, its rarity contribution is smaller.
-   If a construct appears in fewer questions, its rarity contribution is larger.

### 8.2 Priority

Priority is the average of the construct weights attached to that question.

Example:

-   A question covering `Economic / Income` and `Trauma / Health` receives the average of `0.40` and `0.58`, which is `0.49`.

That lets the model distinguish between questions that cover more important crisis dimensions and questions that only provide background context.

### 8.3 Richness

Richness counts how many unique constructs the question covers.

The model then adds:

``` text
0.08 * richness
```

This means a question covering two important constructs gets a larger bonus than a question covering only one, as long as the wording is still compact enough.

## 9. Portability Bonus Explained

The portability bonus rewards wording that can be reused across crises.

The current logic is:

| Scenario | Bonus | Calculation / rule |
|----------------------|----------------------------:|----------------------|
| Generic Core and no source-specific term | 0.16 | If `toggle_category == "Generic Core"` and `_contains_source_specific_term(question_text) == False`, return `0.16`. |
| Generic Core and source-specific term | 0.03 | If `toggle_category == "Generic Core"` and `_contains_source_specific_term(question_text) == True`, return `0.03`. |
| Toggle item and no source-specific term | 0.08 | If `toggle_category != "Generic Core"` and `_contains_source_specific_term(question_text) == False`, return `0.08`. |
| Toggle item and source-specific term | 0.02 | If `toggle_category != "Generic Core"` and `_contains_source_specific_term(question_text) == True`, return `0.02`. |

### Why this matters

The model is not only looking for historically strong questions. It is also looking for wording that can be carried forward into new field instruments.

For example:

-   “Did you receive a stimulus payment?” is useful, but tied to a specific program.
-   “Did you receive emergency government support?” is more portable across different crisis types.

## 10. Redundancy Penalty Explained

The model computes cosine similarity between TF-IDF representations of question text.

This gives a redundancy score that answers:

How similar is this question to the other questions already in the bank?

If a question is too similar to many other questions, it gets penalized in the denominator of `Pi`.

Why? Because a short module should not waste time asking multiple versions of the same thing.

## 11. Worked Examples From The Actual Dataset

These examples come directly from the current scored dataset.

### Example A: Generic Core question

Question:

> Any financial difficulties

Recommended wording:

> Have you experienced any financial difficulties because of the crisis?

Values and calculations:

| Metric | Value | Calculation / rule |
|----------------------|----------------------------:|----------------------|
| `Ui` | 1.700 | `0.85 + 0.85 = 1.70` from tagged keywords `any financial difficulties` and `financial difficulties` |
| `Bi` | 0.300 | `0.10 * 3 + 0.20 * 0.0 = 0.30` |
| `Ri` | 5.667 | `1.70 / 0.30 = 5.667` |
| `idf_strength` | 3.776 | `average_idf(question_text) = 3.7758`, then rounded to `3.776` |
| `idf_scaled` | 0.665 | `(3.7758 - 2.7805) / (4.2771 - 2.7805) = 0.665` |
| `construct_bonus` | 17.863 | `17.333 + 0.450 + 0.08 * 1 = 17.863` |
| `construct_scaled` | 1.000 | `(17.8633 - 2.1457) / (17.8633 - 2.1457) = 1.000` |
| `construct_count` | 1 | `len(set(["Financial Coping"])) = 1` |
| `richness_scaled` | 0.000 | `(1 - 1) / (2 - 1) = 0.000` |
| `portability_bonus` | 0.160 | `Generic Core` and no source-specific term, so the rule returns `0.16` |
| `redundancy_penalty` | 0.418 | `max cosine similarity to another question = 0.4179`, then rounded to `0.418` |
| `redundancy_scaled` | 0.418 | `(0.4179 - 0.0) / (1.0 - 0.0) = 0.418` |
| `augmented_utility` | 2.742 | `1.70 * (1 + 0.32*0.665 + 0.24*1.000 + 0.12*0.000 + 0.16) = 2.742` |
| `Pi` | 7.187 | `2.742 / [0.30 * (1 + 0.65*0.418)] = 7.187` |

#### Ri calculation

``` text
Ri = Ui / Bi
Ri = 1.7 / 0.3 = 5.667
```

#### Construct bonus breakdown

-   rarity component = `17.333`
-   priority component = `0.450`
-   richness count = `1`
-   richness contribution = `0.08 * 1 = 0.08`

So:

``` text
construct_bonus = 17.333 + 0.450 + 0.080 = 17.863
```

#### Pi calculation

``` text
augmented_utility = 1.7 * (1 + 0.32*0.665 + 0.24*1.000 + 0.12*0.000 + 0.16)
                  = 1.7 * 1.6128
                  = 2.742

Pi = 2.742 / [0.3 * (1 + 0.65*0.418)]
   = 2.742 / 0.3815
   = 7.187
```

Why it scores highly:

-   it is very short
-   it is highly portable
-   it captures a strong crisis construct cleanly

### Example B: Pandemic / Disaster question

Question:

> Lost earnings because of the pandemic

Recommended wording:

> Did you lose earnings because of the pandemic?

Values and calculations:

| Metric | Value | Calculation / rule |
|----------------------|----------------------------:|----------------------|
| `Ui` | 3.400 | `0.80 + 0.80 + 0.90 + 0.90 = 3.40` from tagged keywords `earnings`, `lost earnings`, `pandemic`, and `the pandemic` |
| `Bi` | 0.600 | `0.10 * 6 + 0.20 * 0.0 = 0.60` |
| `Ri` | 5.667 | `3.40 / 0.60 = 5.667` |
| `idf_strength` | 4.196 | `average_idf(question_text) = 4.1961`, then rounded to `4.196` |
| `idf_scaled` | 0.946 | `(4.1961 - 2.7805) / (4.2771 - 2.7805) = 0.946` |
| `construct_bonus` | 7.893 | `7.243 + 0.490 + 0.08 * 2 = 7.893` |
| `construct_scaled` | 0.366 | `(7.8929 - 2.1457) / (17.8633 - 2.1457) = 0.366` |
| `construct_count` | 2 | `len(set(["Economic / Income", "Trauma / Health"])) = 2` |
| `richness_scaled` | 1.000 | `(2 - 1) / (2 - 1) = 1.000` |
| `portability_bonus` | 0.020 | Toggle item with a source-specific term, so the rule returns `0.02` |
| `redundancy_penalty` | 0.170 | `max cosine similarity to another question = 0.1700`, then rounded to `0.170` |
| `redundancy_scaled` | 0.170 | `(0.1700 - 0.0) / (1.0 - 0.0) = 0.170` |
| `augmented_utility` | 5.203 | `3.40 * (1 + 0.32*0.946 + 0.24*0.366 + 0.12*1.000 + 0.02) = 5.203` |
| `Pi` | 7.809 | `5.203 / [0.60 * (1 + 0.65*0.170)] = 7.809` |

#### Construct bonus breakdown

-   constructs = `Economic / Income`, `Trauma / Health`
-   rarity component = `7.243`
-   priority component = `0.490`
-   richness count = `2`
-   richness contribution = `0.08 * 2 = 0.16`

So:

``` text
construct_bonus = 7.243 + 0.490 + 0.160 = 7.893
```

#### Pi calculation

``` text
augmented_utility = 3.4 * (1 + 0.32*0.946 + 0.24*0.366 + 0.12*1.000 + 0.02)
                  = 3.4 * 1.5306
                  = 5.203

Pi = 5.203 / [0.6 * (1 + 0.65*0.170)]
   = 5.203 / 0.6663
   = 7.809
```

Why it scores highly:

-   it captures a strong economic shock
-   it also touches a broader crisis construct profile
-   it gains a richness bonus without becoming too burdensome

### Example C: Financial Crisis toggle question

Question:

> How did you/your family manage any financial difficulties due to the shutdown - sell your belongings?

Recommended wording:

> How did your household manage financial difficulties caused by the shutdown or crisis?

Values and calculations:

| Metric | Value | Calculation / rule |
|----------------------|----------------------------:|----------------------|
| `Ui` | 5.950 | `0.85 + 0.75 + 0.70 + 0.85 + 0.75 + 0.65 + 0.65 + 0.75 = 5.95` from the eight tagged keywords on this item |
| `Bi` | 1.600 | `0.10 * 16 + 0.20 * 0.0 = 1.60` |
| `Ri` | 3.719 | `5.95 / 1.60 = 3.719` |
| `idf_strength` | 4.017 | `average_idf(question_text) = 4.0170`, then rounded to `4.017` |
| `idf_scaled` | 0.826 | `(4.0170 - 2.7805) / (4.2771 - 2.7805) = 0.826` |
| `construct_bonus` | 13.006 | `12.381 + 0.465 + 0.08 * 2 = 13.006` |
| `construct_scaled` | 0.691 | `(13.0060 - 2.1457) / (17.8633 - 2.1457) = 0.691` |
| `construct_count` | 2 | `len(set(["Financial Coping", "Government Aid"])) = 2` |
| `richness_scaled` | 1.000 | `(2 - 1) / (2 - 1) = 1.000` |
| `portability_bonus` | 0.020 | Toggle item with a source-specific term, so the rule returns `0.02` |
| `redundancy_penalty` | 0.418 | `max cosine similarity to another question = 0.4179`, then rounded to `0.418` |
| `redundancy_scaled` | 0.418 | `(0.4179 - 0.0) / (1.0 - 0.0) = 0.418` |
| `augmented_utility` | 9.343 | `5.95 * (1 + 0.32*0.826 + 0.24*0.691 + 0.12*1.000 + 0.02) = 9.343` |
| `Pi` | 4.592 | `9.343 / [1.60 * (1 + 0.65*0.418)] = 4.592` |

#### Construct bonus breakdown

-   constructs = `Financial Coping`, `Government Aid`
-   rarity component = `12.381`
-   priority component = `0.465`
-   richness count = `2`
-   richness contribution = `0.08 * 2 = 0.16`

So:

``` text
construct_bonus = 12.381 + 0.465 + 0.160 = 13.006
```

#### Pi calculation

``` text
augmented_utility = 5.95 * (1 + 0.32*0.826 + 0.24*0.691 + 0.12*1.000 + 0.02)
                  = 5.95 * 1.5702
                  = 9.343

Pi = 9.343 / [1.6 * (1 + 0.65*0.418)]
   = 9.343 / 2.0349
   = 4.592
```

Why its `Pi` is lower than the pandemic example even though `Ui` is high:

-   it is much longer
-   it carries more burden
-   it also receives a stronger redundancy penalty than the pandemic earnings example

This is a good example of why `Pi` is useful. A question can be substantively rich but still move down if it is too costly or repetitive for a short module.

## 12. How The Final Selection Works

This part is especially important for non-technical readers.

The workflow does not invent the routing categories from scratch. Each question already belongs to a category such as:

-   `Generic Core`
-   `Toggle: Financial Crisis`
-   `Toggle: Pandemic / Disaster`

The model then scores those questions and selects the strongest final mix under the 30-minute cap.

In the current benchmark:

| Toggle category | Selected count | Calculation / rule |
|----------------------|----------------------------:|----------------------|
| `Generic Core` | 7 | `count(selected rows where toggle_category == "Generic Core") = 7` |
| `Toggle: Financial Crisis` | 1 | `count(selected rows where toggle_category == "Toggle: Financial Crisis") = 1` |
| `Toggle: Pandemic / Disaster` | 20 | `count(selected rows where toggle_category == "Toggle: Pandemic / Disaster") = 20` |

The reason the Pandemic / Disaster bank dominates is not arbitrary. It happens because the Katrina and COVID material contributes many strong housing, trauma, displacement, and aid questions with good information value.

## 13. Why The Generic Core Is Small

The Generic Core is intentionally short.

Why?

-   It must remain useful across many crisis types.
-   It should not consume the entire time budget before crisis-specific content is added.
-   It works best when it captures a few stable, reusable ideas such as hardship, employment disruption, income continuity, aid, housing instability, and wellbeing.

This is why the workflow uses portability and construct logic instead of simply keeping the most familiar demographic questions.

## 14. What `build_all()` Produces

The production refresh path does all of the following from one place:

1.  loads the ranked CSV
2.  computes the enhanced scoring fields
3.  writes the refreshed ranked CSV
4.  writes the summary JSON
5.  writes the dashboard JavaScript payload
6.  regenerates the report figures
7.  saves figure aliases used by older artifact names

That is why the notebook, dashboard, report, and demos stay aligned when `build_all()` is used as the only supported regeneration path.

## 15. Final Takeaway

The model architecture can be summarized simply:

-   start with candidate questions
-   translate wording into crisis constructs
-   calculate utility and burden
-   improve the ranking using rarity, priority, richness, portability, and redundancy control
-   select a compact final module under a hard time limit
-   write synchronized artifacts for analysis, review, and presentation

For a non-technical audience, the easiest way to explain it is this:

> The workflow is designed to keep the questions that say the most, in the clearest way, for the least amount of respondent effort.

That is what the formulas, the weights, and the construct bonus are all trying to achieve together.