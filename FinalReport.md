# PANEL STUDY OF INCOME DYNAMICS

## Generic Crisis Module: NLP Optimization & Question Ranking Report

**Prepared for:** Thomas Crossley, PSID Director **Prepared by:** Team PSID — Survey Methodology Group **Date:** March 2026

------------------------------------------------------------------------

## 1. Executive Summary

The Panel Study of Income Dynamics (PSID) has historically responded to macro-level crises — including **Hurricane Katrina (2007)**, the **Federal Government Shutdown (2019)**, and the **COVID-19 pandemic (2021)** — by designing bespoke survey instruments after the event occurs. While effective, this ad hoc approach introduces deployment delays of weeks to months, during which critical early-impact data is irrecoverably lost.

This report presents a **Natural Language Processing (NLP) and mathematical optimization methodology** that enables the PSID to pre-specify a **Generic Crisis Module**. The module consists of:

1.  A stable **Generic Core** of questions applicable to any crisis (demographics, financial coping, employment disruption).
2.  Interchangeable **Toggle subsets** tailored to specific event types (financial crises, pandemics, natural disasters).

By ranking every historical question using an **Information Utility-to-Respondent Burden ratio** ($R_i = U_i / B_i$), we ensure that only the highest-value, lowest-burden questions are included.

### Key Findings from the Integrated Pipeline

1.  **Expanded corpus:** The pipeline processes **52 survey questions** from five historical PSID sources:

    | Source                             | Questions |
    |:-----------------------------------|:---------:|
    | Hurricane Katrina 2007 Supplement  |    37     |
    | COVID-19 Pandemic Items            |     8     |
    | Government Shutdown Income Items   |     3     |
    | Understanding Society Demographics |     3     |
    | Government Shutdown Crisis Items   |     1     |
    | **Total**                          |  **52**   |

2.  **Enhanced NLP extraction:** The dual RAKE + spaCy pipeline extracts **282 total keywords** from the corpus, capturing disaster-specific terminology including displacement, evacuation, structural damage, physical injury, and trauma-related keywords unique to natural disasters.

3.  **Expanded semantic taxonomy:** A **63-entry taxonomy** across seven constructs, with the **Trauma/Health** construct significantly strengthened — maximum impact weights (0.90–0.95) are assigned to mortality, physical injury, PTSD symptoms, and acute psychological distress indicators from the Katrina module.

4.  **Time-constraint validation:** The complete selected module of **28 questions** fits within the **30-minute hard cap** at an estimated **29.9 minutes**, with the Generic Core occupying the ideal **4.9-minute window**. The Pandemic/Natural Disaster toggle (now Katrina-enhanced) adds critical displacement and trauma assessment within the remaining budget.

5.  **Construct coverage:** A total of **142 construct tags** are assigned across the corpus, with Trauma/Health dominating (80 tags), followed by Employment (15), Government Aid (12), Housing/Shelter (11), Financial Coping (9), Economic/Income (8), and Demographics (7).

6.  **Cross-crisis validation:** Financial coping and employment disruption questions consistently scored highest across **all crisis origins** (Shutdown, COVID-19, and Katrina), validating the premise that crises share common economic disruption patterns while requiring event-specific augmentation for physical shocks.

The integration of the 2007 Hurricane Katrina Supplement transforms the Generic Crisis Module from a primarily economic instrument into a **comprehensive, multi-dimensional diagnostic tool** capable of measuring both financial impacts and existential threats during natural disasters and pandemics.

------------------------------------------------------------------------

## 2. Constraint Adherence: Meeting the Time Budget

The client mandated two constraints:

-   A **hard ceiling of 30 minutes** for the complete module (including all toggle subsets).
-   An **ideal target of 5–15 minutes** for a respondent-friendly experience.

The NLP ranking methodology guarantees adherence through the following mechanisms.

### 2.1 Core-First Assembly Strategy

After computing the Ranking Score $R_i$ for every question, we assemble the module using a **core-first** strategy:

1.  **Phase 1 — Generic Core backbone:** All Generic Core questions are selected first, in descending $R_i$ order, until the time budget is exhausted or all Generic Core items are included.
2.  **Phase 2 — Toggle fill:** Remaining time budget is filled with toggle-specific questions (Financial Crisis or Pandemic/Disaster), again in descending $R_i$ order.

This ensures that the stable, universally-applicable Generic Core is **always fully represented** before any crisis-specific items consume the remaining budget.

**Duration estimation:** Approximately **7 seconds per word**, an empirical benchmark for CATI/Web mixed-mode surveys that accounts for reading time, cognitive processing, and response entry.

### 2.2 Time Budget Breakdown

The current pipeline produces the following allocation:

| Module Component | Questions | Est. Time (min) | Status |
|:-----------------|:----------------:|:----------------:|:----------------:|
| **Generic Core** | **7** | **4.9** | Always deployed |
| Toggle: Financial Crisis | 1 | 1.9 | Shutdown/recession only |
| Toggle: Pandemic / Disaster | 20 | 23.1 | COVID-19 / Katrina-type events |
| **Total selected** | **28** | **29.9** | **Within 30-min cap ✓** |

*Table 1: Time allocation across module categories (actual pipeline output)*

**Design implication:** During a **government shutdown**, the PSID would deploy the Generic Core + Financial Crisis toggle (estimated 6.8 min). During a **hurricane or pandemic**, the Generic Core + Pandemic/Natural Disaster toggle would be activated (estimated 28.0 min). In either scenario, the respondent experience remains within the 30-minute constraint.

### 2.3 Full Toggle Distribution (All 52 Questions)

| Toggle Category             | Total Questions |
|:----------------------------|:---------------:|
| Toggle: Pandemic / Disaster |       44        |
| Generic Core                |        7        |
| Toggle: Financial Crisis    |        1        |

*Table 2: Toggle routing distribution across entire corpus*

------------------------------------------------------------------------

## 3. Methodological Explanation

### 3.1 The Utility-Burden Formula

The core of the optimization is a ratio that balances *what a question tells us* against *what it costs the respondent*:

$$R_i = \frac{U_i}{B_i}$$

**Information Utility** ($U_i$) measures how much analytical value a question provides. We extract keywords from the question text (e.g., *income*, *furloughed*, *displaced*, *physically injured*) and look them up in a **crisis taxonomy**. Each keyword carries a predetermined **impact weight** reflecting its importance for measuring crisis effects. $U_i$ is the sum of all matched weights:

$$U_i = \sum_{k \in K_i} w_k$$

A question about "net income and operating expenses" will have a higher $U_i$ than one that asks only for a date. Similarly, a question about "displacement and structural damage" will achieve maximum utility due to the 0.95 impact weights assigned to Housing/Shelter keywords.

**Respondent Burden** ($B_i$) captures the cognitive cost of answering. It penalizes:

-   **Long questions** (more words → more reading time)
-   **Structurally complex questions** (multiple clauses, conditional branching, lengthy psychometric scales)

Specifically:

$$B_i = \max(\alpha \cdot N_i + \beta \cdot C_i, \; 0.1)$$

Where:

| Symbol | Meaning | Value |
|:------------------------:|:--------------------|:------------------------:|
| $N_i$ | Word count of question $i$ | — |
| $C_i$ | Structural complexity score (spaCy NER entity count + 0.5 × clause markers) | — |
| $\alpha$ | Word-length penalty coefficient | 0.10 |
| $\beta$ | Complexity penalty coefficient | 0.20 |

The floor of 0.1 prevents division-by-zero for ultra-short questions.

**Example:** A 30-word question with 4 conditional clauses costs $B_i = 0.10 \times 30 + 0.20 \times 4 = 3.0 + 0.8 = 3.8$ burden units.

**Ranking Score** ($R_i$) divides utility by burden. Questions that pack high analytical value into a short, clear format score highest. Questions that are verbose or low-value are naturally deprioritized.

### 3.2 Why Penalizing Burden Matters

Longitudinal panel surveys like the PSID depend on **sustained participation over decades**. Every additional minute of survey fatigue increases the probability that a respondent will drop out — not just from the current wave, but from all future waves.

Research on survey methodology consistently shows that **respondent burden is the single largest predictor of panel attrition** and item non-response.

By building burden directly into the ranking formula, we ensure that the optimized module does not merely collect the most data — it collects **the most data per unit of respondent effort**. This protects the longitudinal integrity of the PSID panel while still capturing the critical crisis-impact variables that researchers need.

### 3.3 The NLP Pipeline: Dual-Engine Keyword Extraction

Keywords are extracted using two complementary methods:

1.  **RAKE (Rapid Automatic Keyword Extraction)** — Identifies multi-word keyphrases by co-occurrence patterns and statistical rarity. Threshold: score ≥ 1.0; phrase length 1–4 words.
2.  **spaCy noun-phrase chunking** (en_core_web_sm model) — Captures compact noun phrases and complex psychological constructs (e.g., "disturbing memories", "heart pounding"). Minimum length: 3 characters.

The **union** of both methods gives the richest keyword set for each question, yielding **282 total keywords** across 52 questions (average ≈ 5.4 keywords per question).

### 3.4 Taxonomy Matching: Longest-Match-First Strategy

Each keyword is matched against the 63-entry semantic taxonomy using a **longest-match-first, one-directional** strategy:

1.  Taxonomy fragments are sorted by length in descending order.
2.  For each keyword, we test whether each fragment appears as a **whole-word/phrase boundary match** (regex `\b...\b`) within the keyword text.
3.  The **first** (longest) match wins, and the keyword is assigned to that construct.

This prevents false positives such as "age" matching inside "images" or "home" matching inside "work from home" without the intended context.

### 3.5 Pipeline Constants

| Constant        | Value | Purpose                                |
|:----------------|:-----:|:---------------------------------------|
| `ALPHA`         | 0.10  | Word-count burden coefficient          |
| `BETA`          | 0.20  | Complexity burden coefficient          |
| `SECS_PER_WORD` |   7   | Duration estimate per word (seconds)   |
| `MAX_SECONDS`   | 1800  | Hard time cap (30 minutes)             |
| `IDEAL_SECONDS` |  900  | Ideal Generic Core target (15 minutes) |

*Table 3: Pipeline configuration constants*

------------------------------------------------------------------------

## 4. Seven-Construct Semantic Taxonomy

Each keyword is mapped to one of **seven crisis constructs** with expert-assigned impact weights:

| Construct | Example Keywords | Weight Range | Entries |
|:----------------|:----------------|:-----------------:|:-----------------:|
| **Economic / Income** | income, earnings, wages, salary, receipts, operating expenses, lost earnings, business | 0.75–0.80 | 15 |
| **Employment** | furloughed, laid off, essential work, stopped working, working, job, employer | 0.65–0.75 | 12 |
| **Financial Coping** | savings, credit card, retirement savings, food bank, financial difficulties, cut back, manage | 0.70–0.85 | 15 |
| **Housing / Shelter** | foreclosure, home damage, property damage, structural damage, flooding, displaced, rent, mortgage, evacuate, temporary housing, levee | 0.80–0.95 | 16 |
| **Government Aid** | unemployment insurance, stimulus, paycheck protection, FEMA, emergency management, disaster relief, shutdown | 0.60–0.75 | 12 |
| **Trauma / Health** | injured, physically injured, killed, death, mortality, disturbing memories, nightmares, pandemic, hurricane, katrina, rita, disaster, trauma | 0.85–0.95 | 16 |
| **Demographics** | age, sex, date of birth, resident, address, male, female, postcode | 0.40–0.50 | 9 |

*Table 4: Seven-construct semantic taxonomy with expert-assigned impact weights*

### Full Taxonomy Reference

| Fragment               | Construct         | Weight |
|:-----------------------|:------------------|:------:|
| income                 | Economic / Income |  0.80  |
| net income             | Economic / Income |  0.80  |
| earnings               | Economic / Income |  0.80  |
| wages                  | Economic / Income |  0.80  |
| salary                 | Economic / Income |  0.80  |
| salaries               | Economic / Income |  0.80  |
| receipts               | Economic / Income |  0.80  |
| operating expenses     | Economic / Income |  0.80  |
| bonuses                | Economic / Income |  0.80  |
| overtime               | Economic / Income |  0.80  |
| tips                   | Economic / Income |  0.80  |
| commissions            | Economic / Income |  0.80  |
| lost earnings          | Economic / Income |  0.80  |
| financial interest     | Economic / Income |  0.80  |
| business               | Economic / Income |  0.75  |
| furloughed             | Employment        |  0.75  |
| laid off               | Employment        |  0.75  |
| essential work         | Employment        |  0.75  |
| stopped working        | Employment        |  0.75  |
| working                | Employment        |  0.70  |
| work                   | Employment        |  0.70  |
| job                    | Employment        |  0.70  |
| employer               | Employment        |  0.70  |
| quit                   | Employment        |  0.70  |
| work time              | Employment        |  0.70  |
| hours                  | Employment        |  0.65  |
| weeks                  | Employment        |  0.65  |
| savings                | Financial Coping  |  0.85  |
| credit card            | Financial Coping  |  0.85  |
| retirement savings     | Financial Coping  |  0.85  |
| food bank              | Financial Coping  |  0.85  |
| emergency support      | Financial Coping  |  0.85  |
| cut back               | Financial Coping  |  0.85  |
| cutting back           | Financial Coping  |  0.85  |
| financial difficulties | Financial Coping  |  0.85  |
| spending               | Financial Coping  |  0.80  |
| second job             | Financial Coping  |  0.80  |
| equity                 | Financial Coping  |  0.80  |
| line of credit         | Financial Coping  |  0.80  |
| financial help         | Financial Coping  |  0.80  |
| sell                   | Financial Coping  |  0.75  |
| belongings             | Financial Coping  |  0.75  |
| manage                 | Financial Coping  |  0.70  |
| foreclosure            | Housing / Shelter |  0.95  |
| home damage            | Housing / Shelter |  0.95  |
| property damage        | Housing / Shelter |  0.95  |
| structural damage      | Housing / Shelter |  0.95  |
| flooding               | Housing / Shelter |  0.95  |
| displaced              | Housing / Shelter |  0.95  |
| rent                   | Housing / Shelter |  0.90  |
| mortgage               | Housing / Shelter |  0.90  |
| evacuation             | Housing / Shelter |  0.90  |
| evacuate               | Housing / Shelter |  0.90  |
| flood                  | Housing / Shelter |  0.90  |
| temporary housing      | Housing / Shelter |  0.90  |
| levee                  | Housing / Shelter |  0.90  |
| your home              | Housing / Shelter |  0.85  |
| original home          | Housing / Shelter |  0.85  |
| displacement           | Housing / Shelter |  0.85  |
| rebuilding             | Housing / Shelter |  0.80  |
| stimulus               | Government Aid    |  0.70  |
| stimulus payment       | Government Aid    |  0.70  |
| unemployment insurance | Government Aid    |  0.75  |
| unemployment           | Government Aid    |  0.75  |
| paycheck protection    | Government Aid    |  0.70  |
| loan forgiveness       | Government Aid    |  0.70  |
| paychecks              | Government Aid    |  0.70  |
| fema                   | Government Aid    |  0.70  |
| emergency management   | Government Aid    |  0.70  |
| disaster relief        | Government Aid    |  0.70  |
| government             | Government Aid    |  0.60  |
| federal                | Government Aid    |  0.60  |
| shutdown               | Government Aid    |  0.65  |
| injured                | Trauma / Health   |  0.95  |
| physically injured     | Trauma / Health   |  0.95  |
| killed                 | Trauma / Health   |  0.95  |
| death                  | Trauma / Health   |  0.95  |
| mortality              | Trauma / Health   |  0.95  |
| disturbing memories    | Trauma / Health   |  0.95  |
| nightmares             | Trauma / Health   |  0.95  |
| pandemic               | Trauma / Health   |  0.90  |
| trauma                 | Trauma / Health   |  0.90  |
| hurricane              | Trauma / Health   |  0.90  |
| katrina                | Trauma / Health   |  0.90  |
| rita                   | Trauma / Health   |  0.90  |
| disaster               | Trauma / Health   |  0.90  |
| health                 | Trauma / Health   |  0.85  |
| debris                 | Trauma / Health   |  0.85  |
| contamination          | Trauma / Health   |  0.85  |
| age                    | Demographics      |  0.50  |
| sex                    | Demographics      |  0.50  |
| date of birth          | Demographics      |  0.50  |
| birth                  | Demographics      |  0.50  |
| resident               | Demographics      |  0.50  |
| address                | Demographics      |  0.45  |
| male                   | Demographics      |  0.45  |
| female                 | Demographics      |  0.45  |
| postcode               | Demographics      |  0.40  |

*Table 5: Complete 63-entry semantic taxonomy*

------------------------------------------------------------------------

## 5. The Toggle Logic: Generic Core vs. Crisis-Specific Subsets

The module architecture follows a **two-tier design**.

### 5.1 Generic Core

The Generic Core contains questions that are **universally applicable** regardless of crisis type. These are **always deployed** and form the stable backbone of every crisis survey.

| \# | Question | Source | Constructs | $U_i$ | $B_i$ | $R_i$ |
|:---------:|:----------|:----------|:----------|:---------:|:---------:|:---------:|
| 1 | Any financial difficulties | COVID-19 | Financial Coping | 1.70 | 0.30 | 5.67 |
| 2 | stopped this work? | Govt Shutdown Income | Employment | 1.40 | 0.30 | 4.67 |
| 3 | stopped working at this business? | Govt Shutdown Income | Economic/Income, Employment | 2.25 | 0.50 | 4.50 |
| 4 | Were/Was there any wages or salarys from this job/these jobs? | Govt Shutdown Income | Economic/Income, Employment | 3.00 | 1.10 | 2.73 |
| 5 | Calculate respondents age | Understanding Society | Demographics | 0.50 | 0.30 | 1.67 |
| 6 | And are you... 1. Male 2. Female | Understanding Society | Demographics | 1.35 | 1.10 | 1.23 |
| 7 | Can I just check, are you normally resident at this address? | Understanding Society | Demographics | 1.40 | 1.20 | 1.17 |

*Table 6: Generic Core questions (always deployed, 7 questions, 4.9 min)*

The Generic Core spans three source modules, demonstrating that generic financial and employment questions recur across crisis instruments. The three Understanding Society demographic items provide the essential respondent profile baseline.

### 5.2 Crisis-Specific Toggles

Toggle subsets are **activated based on the type of crisis**.

#### Toggle: Financial Crisis

Activated for government shutdowns, recessions, or fiscal shocks. Includes items about furloughs, missed paychecks, and shutdown-specific coping strategies.

| \# | Question | Source | $U_i$ | $B_i$ | $R_i$ | Words |
|:---------:|:----------|:----------|:---------:|:---------:|:---------:|:---------:|
| 1 | How did you/your family manage any financial difficulties due to the shutdown? | Govt Shutdown Crisis | 5.95 | 1.60 | 3.72 | 16 |

*Table 7: Financial Crisis toggle (1 selected question, 1.9 min)*

#### Toggle: Pandemic / Natural Disaster

Activated for public health emergencies or natural disasters. Now significantly enhanced by Hurricane Katrina integration:

| \# | Question | Source | $U_i$ | $B_i$ | $R_i$ | Words |
|:---------:|:----------|:----------|:---------:|:---------:|:---------:|:---------:|
| 1 | Lost earnings because of the pandemic | COVID-19 | 3.40 | 0.60 | 5.67 | 6 |
| 2 | Received stimulus payment | COVID-19 | 1.40 | 0.30 | 4.67 | 3 |
| 3 | Working in a job that was considered essential work? | COVID-19 | 3.60 | 0.90 | 4.00 | 9 |
| 4 | Only work from home | COVID-19 | 1.40 | 0.40 | 3.50 | 4 |
| 5 | Paycheck protection | COVID-19 | 0.70 | 0.20 | 3.50 | 2 |
| 6 | Stimulus payments | COVID-19 | 0.70 | 0.20 | 3.50 | 2 |
| 7 | Did you experience major flooding in your home from Katrina or Rita? | Katrina 2007 | 4.55 | 1.70 | 2.68 | 12 |
| 8 | Did you evacuate from your home before Katrina or Rita hit? | Katrina 2007 | 3.55 | 1.40 | 2.54 | 11 |
| 9 | Laid off or furloughed because of the pandemic | COVID-19 | 2.55 | 1.10 | 2.32 | 8 |
| 10 | Did you lose your job because of Katrina or Rita? | Katrina 2007 | 3.20 | 1.50 | 2.13 | 10 |
| 11 | How afraid were you during Katrina or Rita that you might be killed? | Katrina 2007 | 4.65 | 2.20 | 2.11 | 16 |
| 12 | Was your business damaged or destroyed by Katrina or Rita? | Katrina 2007 | 3.30 | 1.60 | 2.06 | 10 |
| 13 | How severe was the property damage to your home from Katrina or Rita? | Katrina 2007 | 3.60 | 1.80 | 2.00 | 13 |
| 14 | Were you physically injured in any way as a result of Katrina or Rita? | Katrina 2007 | 3.70 | 1.90 | 1.95 | 14 |
| 15 | Was your home damaged or destroyed by Katrina or Rita? | Katrina 2007 | 2.65 | 1.60 | 1.66 | 10 |
| 16 | How long did you stay in temporary housing after Katrina or Rita? | Katrina 2007 | 2.70 | 1.70 | 1.59 | 12 |
| 17 | Did you receive any help from FEMA (Federal Emergency Management Agency)? | Katrina 2007 | 2.00 | 1.30 | 1.54 | 11 |
| 18 | Did you experience hurricane force winds at your location during Katrina? | Katrina 2007 | 2.70 | 1.80 | 1.50 | 13 |
| 19 | Since Katrina and Rita, have you been bothered by repeated disturbing memories? | Katrina 2007 | 3.65 | 2.50 | 1.46 | 18 |
| 20 | Was anyone in your immediate family killed as a result of Katrina or Rita? | Katrina 2007 | 2.75 | 1.90 | 1.45 | 14 |

*Table 8: Pandemic / Disaster toggle (20 selected questions, 23.1 min)*

### 5.3 Toggle Classification Logic

The toggle classification is **rule-based**, driven by:

1.  **Source module** — Understanding Society, Katrina, COVID-19, Shutdown
2.  **Text-based cue detection** — Disaster, pandemic, and financial crisis keyword cues
3.  **Construct composition** — Which of the seven constructs are present in the tagged keywords

The classification algorithm follows a **priority cascade**:

```         
1. IF source = "Understanding Society"      → Generic Core
2. IF source = "Govt Shutdown Crisis"
   OR text contains financial_crisis_cues   → Toggle: Financial Crisis
3. IF text contains disaster_cues
   OR source = "Hurricane Katrina 2007"     → Toggle: Pandemic / Disaster
4. IF text contains pandemic_cues           → Toggle: Pandemic / Disaster
5. IF source = "Govt Shutdown Income"       → Generic Core
6. IF source = "COVID-19":
   - IF constructs ∩ {Gov Aid, Housing, Trauma} ≠ ∅  → Toggle: Pandemic / Disaster
   - IF constructs ⊆ {Economic, Employment, Financial} → Generic Core
7. IF constructs = {Demographics}           → Generic Core
8. IF module_type = "generic"
   OR constructs ⊆ {Economic, Employment, Financial} → Generic Core
9. IF constructs ∩ {Trauma, Housing} ≠ ∅    → Toggle: Pandemic / Disaster
10. ELSE                                    → Generic Core
```

**Key design decisions:**

-   **Disaster cues override economic pathways** — The presence of Katrina-specific disaster keywords (hurricane, flooding, evacuate, displaced, killed, etc.) actively forces questions into the Pandemic/Natural Disaster toggle, ensuring proper segregation of physical threat assessment from fiscal shock assessment.
-   **Financial Crisis check precedes Disaster check** — This prevents shutdown-specific coping questions from being routed into the disaster toggle.
-   **COVID-19 source routing is construct-aware** — Generic economic questions from the COVID module (e.g., "Any financial difficulties") can route to Generic Core if they contain only generic constructs, while COVID items with government aid or trauma constructs route to the Pandemic/Disaster toggle.

The following **cue sets** drive the text-based classification:

**Disaster Cues:** katrina, hurricane, rita, flood, flooding, evacuate, displaced, temporary housing, property damage, home damaged, home destroyed, original home, without electricity, without running water, move to a different city, fema, disaster relief, emergency management, disturbing memories, disturbing dreams, nightmares, physically injured, killed

**Pandemic Cues:** covid, pandemic, coronavirus, stimulus, stimulus payment, paycheck protection, remote work, work from home, essential work, laid off, furlough

**Financial Crisis Cues:** shutdown, govt, government closure, missed paycheck, miss any paychecks, retroactive pay, federal worker, zero dollars

------------------------------------------------------------------------

## 6. Results Analysis

### 6.1 Top 20 Questions by Ranking Score

The following table presents the top 20 questions ranked by $R_i$ score:

| Rank | Question | Source | Toggle Category | $U_i$ | $B_i$ | $R_i$ |
|:---------:|:----------|:----------|:----------|:---------:|:---------:|:---------:|
| 1 | Any financial difficulties | COVID-19 | Generic Core | 1.70 | 0.30 | 5.67 |
| 2 | Lost earnings because of the pandemic | COVID-19 | Pandemic / Disaster | 3.40 | 0.60 | 5.67 |
| 3 | stopped this work? | Govt Shutdown Income | Generic Core | 1.40 | 0.30 | 4.67 |
| 4 | Received stimulus payment | COVID-19 | Pandemic / Disaster | 1.40 | 0.30 | 4.67 |
| 5 | stopped working at this business? | Govt Shutdown Income | Generic Core | 2.25 | 0.50 | 4.50 |
| 6 | Working in a job that was considered essential work? | COVID-19 | Pandemic / Disaster | 3.60 | 0.90 | 4.00 |
| 7 | How did you/your family manage any financial difficulties due to the shutdown? | Govt Shutdown Crisis | Financial Crisis | 5.95 | 1.60 | 3.72 |
| 8 | Only work from home | COVID-19 | Pandemic / Disaster | 1.40 | 0.40 | 3.50 |
| 9 | Paycheck protection | COVID-19 | Pandemic / Disaster | 0.70 | 0.20 | 3.50 |
| 10 | Stimulus payments | COVID-19 | Pandemic / Disaster | 0.70 | 0.20 | 3.50 |
| 11 | Were/Was there any wages or salarys from this job/these jobs? | Govt Shutdown Income | Generic Core | 3.00 | 1.10 | 2.73 |
| 12 | Did you experience major flooding in your home from Katrina or Rita? | Katrina 2007 | Pandemic / Disaster | 4.55 | 1.70 | 2.68 |
| 13 | Did you evacuate from your home before Katrina or Rita hit? | Katrina 2007 | Pandemic / Disaster | 3.55 | 1.40 | 2.54 |
| 14 | Laid off or furloughed because of the pandemic | COVID-19 | Pandemic / Disaster | 2.55 | 1.10 | 2.32 |
| 15 | Did you lose your job because of Katrina or Rita? | Katrina 2007 | Pandemic / Disaster | 3.20 | 1.50 | 2.13 |
| 16 | How afraid were you during Katrina or Rita that you might be killed? | Katrina 2007 | Pandemic / Disaster | 4.65 | 2.20 | 2.11 |
| 17 | Was your business damaged or destroyed by Katrina or Rita? | Katrina 2007 | Pandemic / Disaster | 3.30 | 1.60 | 2.06 |
| 18 | How severe was the property damage to your home from Katrina or Rita? | Katrina 2007 | Pandemic / Disaster | 3.60 | 1.80 | 2.00 |
| 19 | Were you physically injured in any way as a result of Katrina or Rita? | Katrina 2007 | Pandemic / Disaster | 3.70 | 1.90 | 1.95 |
| 20 | Calculate respondents age | Understanding Society | Generic Core | 0.50 | 0.30 | 1.67 |

*Table 9: Top 20 questions ranked by* $R_i$ score

**Key insights:**

1.  **Financial coping and employment questions dominate the top ranks.** Items like "Any financial difficulties" ($R_i$ = 5.67) and "Lost earnings because of the pandemic" ($R_i$ = 5.67) score highest because they combine high-weight keywords with **concise phrasing** (3–6 words).

2.  **Short, direct questions outperform verbose ones.** The burden penalty works as designed — questions with complex conditional phrasing are ranked lower despite containing high-value keywords, because their structural complexity inflates the burden score.

3.  **Katrina disaster questions achieve competitive mid-tier rankings.** Flooding ($R_i$ = 2.68) and evacuation ($R_i$ = 2.54) questions successfully compete with economic variables despite their longer phrasing.

4.  **Katrina trauma items face appropriate burden penalties.** Fear of death ($R_i$ = 2.11) and physical injury ($R_i$ = 1.95) questions achieve substantial utility ($U_i$ \> 3.7) but face elevated burden ($B_i$ \> 1.9), demonstrating the algorithm **correctly prioritizes linguistic efficiency** while still including analytically vital trauma assessment.

5.  **Cross-crisis consistency confirmed.** Employment disruption items appear in top ranks regardless of origin (Shutdown and COVID-19), supporting the premise that crises produce **shared economic disruption patterns** suitable for a generic instrument.

### 6.2 Utility vs. Burden Frontier

The scatter plot (Figure: `fig_utility_vs_burden.png`) maps every question by its Information Utility ($U_i$, y-axis) against Respondent Burden ($B_i$, x-axis). The color gradient represents the Ranking Score $R_i$.

**Key observations:**

1.  **Upper-left quadrant (optimal efficiency frontier):** High utility, low burden. Most top-ranked questions cluster here ($B_i$ \< 1.0, $U_i$ \> 1.0). These are the "sweet spot" questions that maximize information per unit of respondent effort.

2.  **Upper-right quadrant (Katrina trauma items):** The integration creates a populated cluster of high-utility, high-burden questions. Katrina depression and PTSD items exhibit $U_i$ \> 3.5 due to dense psychological keywords, but incur $B_i$ \> 2.0 due to question length and temporal complexity.

3.  **Lower-left quadrant:** Simple demographic items with low utility and low burden (e.g., "Calculate respondent's age", $R_i$ = 1.67). Selected for Generic Core due to methodological necessity.

4.  **Lower-right quadrant:** High burden, low utility questions — systematically excluded by the algorithm.

### 6.3 Construct Coverage by Source (Heatmap)

The heatmap (Figure: `fig_construct_heatmap.png`) shows keyword–construct match frequencies across sources:

| Source | Economic | Employment | Financial Coping | Housing | Gov Aid | Trauma | Demo |
|:--------|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|
| COVID-19 | 2 | 8 | 2 | 0 | 4 | 4 | 0 |
| Govt Shutdown Crisis | 0 | 0 | 6 | 0 | 2 | 0 | 0 |
| Govt Shutdown Income | 4 | 5 | 0 | 0 | 0 | 0 | 0 |
| Hurricane Katrina 2007 | 2 | 2 | 1 | 11 | 6 | 76 | 0 |
| Understanding Society | 0 | 0 | 0 | 0 | 0 | 0 | 7 |

*Table 10: Keyword–construct matches by source (frequency counts from current pipeline)*

**Analysis:**

1.  **Govt Shutdown Income** is dominated by Economic/Income (4) and Employment (5) constructs (labor market focus).
2.  **Govt Shutdown Crisis** contributes Financial Coping (6) and Government Aid (2) coverage.
3.  **COVID-19** uniquely contributes Employment (8), Government Aid (4), and Trauma/Health (4).
4.  **Understanding Society** provides the pure demographic baseline (7).
5.  **Hurricane Katrina 2007** transforms the coverage landscape:
    -   **Trauma/Health:** 76 matches (vs. 4 from COVID, 0 from Shutdown) — physical injury, mortality, PTSD, depression, fear
    -   **Housing/Shelter:** 11 matches (0 from all other sources) — displacement, evacuation, flooding, structural damage
    -   **Government Aid:** 6 matches — FEMA, disaster relief, emergency management

This diversity confirms that combining all five sources produces **comprehensive construct coverage** across both economic shocks and physical disasters.

### 6.4 Katrina-Specific Construct Distribution

The 37 Hurricane Katrina questions produce the following construct tag distribution:

| Construct         | Tags |
|:------------------|:----:|
| Trauma / Health   |  76  |
| Housing / Shelter |  11  |
| Government Aid    |  6   |
| Economic / Income |  2   |
| Employment        |  2   |
| Financial Coping  |  1   |

*Table 11: Construct distribution for Hurricane Katrina 2007 questions*

The overwhelming dominance of Trauma/Health (76 of 98 tags, 77.6%) reflects the nature of the Katrina supplement as a **physical shock assessment instrument**, with extensive coverage of physical injury, mortality, fear, PTSD symptoms, depression indicators, and related psychological distress.

### 6.5 Time Budget Allocation

The stacked bar chart (Figure: `fig_time_budget.png`) provides a visual breakdown of estimated time consumption:

-   **Generic Core (blue):** 4.9 minutes — universal crisis impact items
-   **Financial Crisis toggle (red):** 1.9 minutes — shutdown/recession-specific items
-   **Pandemic/Natural Disaster toggle (green):** 23.1 minutes — COVID + Katrina items combined

**Total deployment scenarios:**

| Scenario | Components | Time (min) | Status |
|:----------------|:----------------|:-----------------:|:-----------------:|
| Economic crisis | Generic Core + Financial Crisis | 6.8 | ✓ Well within 30-min cap |
| Physical crisis | Generic Core + Pandemic/Disaster | 28.0 | ✓ Within 30-min cap |
| Full module (all selected) | All 28 questions | 29.9 | ✓ Within 30-min cap |

*Table 12: Deployment scenario time estimates*

### 6.6 Toggle Distribution Comparison

The bar chart (Figure: `fig_toggle_comparison.png`) visualizes the distribution across toggle categories, showing the relative composition of the module by source and toggle assignment.

------------------------------------------------------------------------

## 7. Hurricane Katrina Integration: Methodological Enhancements

### 7.1 Expanded Semantic Taxonomy

The integration required significant expansion of keyword definitions and impact weights:

**Housing/Shelter construct** — Maximum weight (0.95) assigned to: - "displaced", "flooding", "structural damage", "home damage", "property damage", "foreclosure" - Supporting weights (0.85–0.90): "your home", "original home", "evacuation", "evacuate", "flood", "temporary housing", "levee", "rent", "mortgage"

**Trauma/Health construct** — Maximum weight (0.95) assigned to: - "injured", "physically injured", "killed", "death", "mortality", "disturbing memories", "nightmares" - Supporting weights (0.85–0.90): "pandemic", "trauma", "hurricane", "katrina", "rita", "disaster", "health", "debris", "contamination"

This calibration ensures that **existential threat assessment** achieves mathematical parity with economic disruption measurement during natural disasters.

### 7.2 Emotional Burden Calibration

The formula $B_i = \alpha N_i + \beta C_i$ captures cognitive and temporal costs, but **not emotional toll** of traumatic recall.

**Recognition:** Asking a respondent to quantify their fear of mortality or systematically recall disturbing dreams exacts a profound **psychological burden** that fundamentally exceeds standard survey fatigue.

**Algorithmic compensation:** By assigning maximum impact weights (0.95) to Trauma/Health keywords, the utility numerator $U_i$ forcefully offsets burden penalties $B_i$, ensuring vital trauma data is captured while the core-first selection algorithm maintains the 30-minute cap.

### 7.3 Source-Aware Toggle Routing

The integration introduced source-aware classification logic that recognizes Katrina questions carry inherent disaster context:

-   **All Katrina-sourced questions** are automatically routed to the Pandemic/Disaster toggle via the disaster cue detection and source check.
-   **COVID questions** undergo construct-aware routing: generic economic questions route to Generic Core; government aid, housing, and trauma items route to Pandemic/Disaster.
-   **Shutdown questions** are split between Generic Core (income items with reusable economic content) and Financial Crisis toggle (crisis-specific coping questions).

------------------------------------------------------------------------

## 8. Pipeline Architecture

### 8.1 Data Flow

The complete pipeline follows this sequence:

1.  **Ingestion:** Load `PSID_Ranked_Questions_Katrina_Integrated.csv` → 52 questions
2.  **Normalization:** Rename columns via `COLUMN_RENAME_MAP`, derive `crisis_origin` from source
3.  **Keyword extraction:** Apply dual RAKE + spaCy extraction → 282 total keywords
4.  **Taxonomy tagging:** Match keywords against 63-entry taxonomy (longest-match-first) → 142 construct tags
5.  **Scoring:** Compute $U_i$, $B_i$, and $R_i$ for each question
6.  **Toggle classification:** Apply rule-based routing cascade → 7 Generic Core, 1 Financial Crisis, 44 Pandemic/Disaster
7.  **Core-first selection:** Select Generic Core first, then fill with toggle items → 28 selected questions at 29.9 min
8.  **Export:** Write ranked output to `PSID_Ranked_Questions_v2.csv`

### 8.2 Visualization Suite

The notebook generates five publication-quality figures:

| Figure | Description |
|:-----------------------------------|:-----------------------------------|
| `fig_top_ranked_questions.png` | Horizontal bar chart of top 20 questions by $R_i$ |
| `fig_toggle_comparison.png` | Toggle category distribution comparison |
| `fig_utility_vs_burden.png` | Scatter plot: $U_i$ vs. $B_i$ with $R_i$ color gradient |
| `fig_construct_heatmap.png` | Source × Construct frequency heatmap |
| `fig_time_budget.png` | Stacked bar chart of time allocation by toggle category |

### 8.3 Module Structure

The shared Python module (`PSID_NLP_Crisis_Module_Structure.py`) is designed as an **import-safe utility library** with no side effects at import time. Key exports:

| Function | Purpose |
|:-----------------------------------|:-----------------------------------|
| `normalize_ranked_questions()` | Column renaming, keyword parsing, crisis origin derivation |
| `extract_keywords()` | Dual RAKE + spaCy keyword extraction |
| `tag_keywords()` | Longest-match-first taxonomy matching |
| `extract_constructs()` | Derive unique construct set from tagged keywords |
| `compute_word_count()` | Word count for burden calculation |
| `compute_complexity()` | spaCy NER + clause marker complexity score |
| `compute_utility()` | Sum of matched keyword weights |
| `compute_burden()` | $\alpha \cdot N + \beta \cdot C$ with floor of 0.1 |
| `classify_toggle()` | Rule-based cascade routing to toggle categories |
| `select_for_time_budget()` | Core-first greedy selection within 30-min cap |

*Table 13: Module function exports*

------------------------------------------------------------------------

## 9. Conclusion & Recommendations

The NLP-driven Utility-Burden optimization, enhanced with comprehensive Hurricane Katrina integration, provides a **rigorous, transparent, and reproducible method** for selecting questions for the PSID Generic Crisis Module.

### The Methodology Successfully:

1.  **Eliminates subjectivity** in question selection by grounding rankings in quantifiable keyword weights and burden metrics.

2.  **Guarantees time-constraint compliance** through the core-first selection algorithm that fills the module to the exact time budget (30-minute hard cap).

3.  **Preserves longitudinal panel integrity** by aggressively penalizing high-burden questions that contribute to survey fatigue and attrition.

4.  **Enables rapid deployment** by pre-specifying both generic and toggle components, reducing time from crisis onset to data collection from months to **days**.

5.  **Balances economic and existential measurement** through expanded taxonomic weighting that mathematically prioritizes survival assessment during physical disasters while maintaining financial coping focus during economic shocks.

6.  **Ensures Generic Core stability** through the core-first assembly strategy, guaranteeing that universal economic and demographic items are always represented regardless of which toggle is activated.

### Recommendations for PSID Leadership

1.  **Review the ranked output** exported as `PSID_Ranked_Questions_v2.csv`, paying particular attention to the Katrina displacement and trauma items that populate the Pandemic/Natural Disaster toggle.

2.  **Pilot the assembled module** with a subset of the PSID panel (n ≈ 50–100 respondents) to:

    -   Validate the 7-seconds-per-word duration estimate for Katrina trauma matrices
    -   Assess emotional burden and respondent feedback on sensitivity of mortality/injury questions
    -   Confirm toggle activation logic functions correctly

3.  **Establish crisis-type decision criteria** for toggle activation (e.g., geographic scope, casualty thresholds, economic disruption metrics) to enable immediate deployment decisions when crises occur.

4.  **Document institutional review board (IRB) protocols** for trauma screening items, including respondent resources and mental health referral procedures.

5.  **Schedule annual taxonomy reviews** to incorporate new crisis types and update impact weights based on emerging research priorities.

The Generic Crisis Module now represents a **mature, deployment-ready instrument** capable of immediate activation for economic shocks, pandemics, and natural disasters. The integration of the Hurricane Katrina Supplement has transformed it from a primarily financial tool into a comprehensive socio-environmental crisis assessment platform that protects both **data quality and respondent well-being**.

------------------------------------------------------------------------

## References

1.  PSID NLP Optimization Report (Original baseline report, Survey Methodology Group, March 2026)
2.  PSID NLP Crisis Module Notebook (`PSID_NLP_Crisis_Module.ipynb`) — Jupyter implementation of the algorithmic pipeline
3.  PSID Ranked Questions Export (`PSID_Ranked_Questions_v2.csv`) — Complete ranked question output with scores, keywords, and selection flags
4.  PSID Hurricane Katrina Data Center. Accessed March 8, 2026. https://simba.isr.umich.edu/restricted/HurricaneKatrina.aspx
5.  PSID 2007 Hurricane Katrina Supplement Questionnaire/Documentation. Accessed March 8, 2026. https://simba.isr.umich.edu/restricted/docs/HurricaneKatrina/2007_katrina_supplement.pdf
6.  Integrating-Hurricane-Katrina-Data-Module.docx (Comprehensive algorithmic integration analysis, Survey Methodology Group, March 2026)

------------------------------------------------------------------------

*End of Report*