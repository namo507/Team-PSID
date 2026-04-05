

**PSID Crisis Module**

**NLP Data Modeling Codebook**

*Model Architecture, Scoring Logic, and Pipeline Documentation*

April 2026

# **Table of Contents**

# **1\. Introduction and Purpose**

This codebook documents the NLP-augmented data modeling pipeline used to evaluate, rank, and select survey questions for the PSID Crisis Module. The pipeline replaces subjective committee review with a deterministic, mathematically optimized process. 

**Key Output:** a 28-question module requiring 29.17 minutes, optimized within a 30-minute cap.

**Data Sources (52 historical crisis questions):**

* PSID Hurricane Katrina 2007 follow-up — 32 items  
* PSID COVID-19 pandemic module — 9 items  
* PSID Government Shutdown Income module — 4 items  
* PSID Government Shutdown Crisis module — 3 items  
* Understanding Society Coronavirus Study — 4 items

# **2\. Pipeline Architecture Overview**

The pipeline consists of seven sequential phases, each transforming the data toward a final optimized module.

┌─────────────────────────────────┐  
│  1\. DATA INGESTION              │  
│  load\_dataset() → CSV (52 rows) │  
└───────────────┬─────────────────┘  
                │  
                ▼  
┌─────────────────────────────────┐  
│  2\. KEYWORD PARSING & TAGGING  │  
│  parse\_keywords() → tokens     │  
│  tag\_keywords() → taxonomy     │  
└───────────────┬─────────────────┘  
                │  
                ▼  
┌─────────────────────────────────┐  
│  3\. CONSTRUCT EXTRACTION       │  
│  extract\_constructs() → domain │  
│  labels (63-entry taxonomy)    │  
└───────────────┬─────────────────┘  
                │  
                ▼  
┌─────────────────────────────────┐  
│  4\. PORTABILITY TRANSFORMATION │  
│  suggest\_deployable\_wording()  │  
│  Neutralize event-specific     │  
└───────────────┬─────────────────┘  
                │  
                ▼  
┌─────────────────────────────────┐  
│  5\. MATHEMATICAL SCORING      │  
│  compute\_augmented\_scores()    │  
│  Ri, Pi, IDF, Redundancy      │  
└───────────────┬─────────────────┘  
                │  
                ▼  
┌─────────────────────────────────┐  
│  6\. MODULE SELECTION           │  
│  select\_for\_time\_budget()      │  
│  28 questions ≤ 30 min         │  
└───────────────┬─────────────────┘  
                │  
                ▼  
┌─────────────────────────────────┐  
│  7\. ARTIFACT GENERATION        │  
│  build\_all() → CSV, JSON, JS, │  
│  PNG figures                   │  
└─────────────────────────────────┘

Pipeline Phase Summary Table:

| Phase | Function | Input | Output | Key Metric |
| ----- | ----- | ----- | ----- | ----- |
| 1 | load\_dataset() | CSV with 52 questions | pandas DataFrame | 52 rows |
| 2 | parse\_keywords() | Raw text | Token lists | 63-entry taxonomy |
| 3 | extract\_constructs() | Tagged keywords | Construct labels | 7 domains |
| 4 | suggest\_deployable\_wording() | Event-specific text | Generic wording | portability\_bonus |
| 5 | compute\_augmented\_scores() | Constructs & text | Ri, Pi, IDF scores | Ranking metrics |
| 6 | select\_for\_time\_budget() | Scored DataFrame | 28 selected Q's | 29.17 minutes |
| 7 | build\_all() | Selected module | CSV, JSON, JS, PNG | 5 figures |

# **3\. Scoring Formulas and Calculation Logic**

## **3.1 Min-Max Scaling**

**Formula:** x\_scaled \= (x − x\_min) / (x\_max − x\_min)

When x\_max \= x\_min, output defaults to 0.0 to prevent division by zero.

**Example:** If raw IDF values \= \[2.1, 3.5, 4.8, 1.9\], then min=1.9, max=4.8, range=2.9

* 2.1 → (2.1−1.9)/2.9 \= 0.069  
* 3.5 → (3.5−1.9)/2.9 \= 0.552  
* 4.8 → (4.8−1.9)/2.9 \= 1.000

## **3.2 Burden Calculation (B\_i)**

**Formula:** B\_i \= max(α × word\_count \+ β × complexity, 0.1)

Where: α \= 0.10, β \= 0.20

The floor of 0.1 prevents asymptotic inflation of R\_i for very short questions.

**Examples:**

* "Any financial difficulties" → 3 words, complexity=0.0 → B\_i \= max(0.30, 0.1) \= 0.30  
* "Working in a job that was considered essential work?" → 9 words → B\_i \= max(0.90, 0.1) \= 0.90

## **3.3 Utility Calculation (U\_i)**

**Formula:** U\_i \= Σ(weight\_k) for all matched keywords k

The utility is the sum of all keyword weights from the 63-entry taxonomy that match within the question text.

**Example:** "Lost earnings because of the pandemic"

* "earnings" → Economic/Income, weight=0.80  
* "lost earnings" → Economic/Income, weight=0.80  
* "pandemic" → Trauma/Health, weight=0.90  
* U\_i \= 0.80 \+ 0.80 \+ 0.90 \= 3.40

## **3.4 Rank Index (R\_i)**

**Formula:** R\_i \= U\_i / B\_i

This is the baseline efficiency metric: analytical yield per unit of respondent burden. Higher R\_i indicates better utility-to-burden ratio.

**Example:** "Any financial difficulties" → R\_i \= 1.70 / 0.30 \= 5.667

## **3.5 Temporal Burden Estimation**

**Formula:** minutes \= (word\_count × SECS\_PER\_WORD) / 60

Where SECS\_PER\_WORD \= 7 (conservative estimate for telephone/web administration)

**Example:** "Any financial difficulties" (3 words) → (3 × 7\) / 60 \= 0.35 minutes

Total for 28 selected questions: 29.17 minutes (within 30-min cap)

## **3.6 Enhanced Priority Score (P\_i)**

**Formula:** P\_i \= Augmented\_Utility / (B\_i × (1 \+ 0.65 × redundancy\_scaled))

Where:

* Augmented\_Utility \= U\_i × (1 \+ 0.32×idf\_scaled \+ 0.24×construct\_scaled \+ 0.12×richness\_scaled \+ portability\_bonus  
* 0.32 \= weight for IDF (information density / term rarity)  
* 0.24 \= weight for construct alignment (thematic priority)  
* 0.12 \= weight for richness (multi-construct coverage)  
* 0.65 \= redundancy penalty weight

These scalar weights are calibrated to balance information density against thematic alignment, ensuring no single feature overwhelms the utility score.

# **4\. NLP Feature Extraction**

## **4.1 TF-IDF Vectorization**

The pipeline uses sklearn's TfidfVectorizer with:

* ngram\_range \= (1, 2\) — unigrams and bigrams  
* stop\_words \= "english"  
* min\_df \= 1

IDF Strength \= mean IDF of all tokens in a question. Higher values indicate rarer, more diagnostic vocabulary.

## **4.2 Cosine Similarity and Redundancy**

A cosine similarity matrix is computed across all 52 vectorized questions.

* Diagonal set to 0.0 (exclude self-similarity)  
* Redundancy penalty \= max cosine similarity between target question and any other question

This penalizes questions that overlap heavily with others already in the pool, promoting diversity.

# **5\. Construct Priority Weights and Justification**

| Construct | Weight | Justification |
| ----- | ----- | ----- |
| Trauma / Health | 0.58 | Highest priority — severe compounding effects on human capital and mortality, critical during COVID-19 and natural disasters |
| Housing / Shelter | 0.55 | Captures dislocation, eviction, structural instability — primary vectors of wealth destruction |
| Government Aid | 0.48 | Essential for tracking efficacy of stimulus payments, PPP, SNAP in stabilizing household finances |
| Financial Coping | 0.45 | Monitors endogenous behavioral adaptations: food banks, liquidating retirement, accumulating debt |
| Employment | 0.42 | Assesses acute labor disruptions: furloughs, remote work transitions, hours reductions |
| Economic / Income | 0.40 | Quantifies absolute monetary losses for poverty dynamics modeling |
| Demographics | 0.14 | Lowest priority — static variables already tracked in core PSID modules |

## **5.1 Construct Bonus Calculation**

When a question maps to multiple constructs (e.g., Employment and Trauma/Health):

* Priority \= mean of mapped construct weights  
* Rarity \= weighted frequency inverse  
* Richness \= number of constructs spanned

construct\_bonus \= rarity \+ priority \+ 0.08 × richness

# **6\. Portability Logic**

Portability ensures questions are event-agnostic and can be deployed across different crisis types ("always-on").

The function \_contains\_source\_specific\_term() scans for restricted keywords: "katrina", "rita", "fema", "covid", "pandemic", "shutdown", "government shutdown"

## **6.1 Portability Bonus Structure**

| Classification | Source-Specific Terms | Bonus Type | Value |
| ----- | ----- | ----- | ----- |
| Generic Core | None (portable) | Portable Core | \+0.16 |
| Generic Core | Present (needs cleaning) | Needs Cleanup | \+0.03 |
| Toggle Item | None (portable) | Portable Toggle | \+0.08 |
| Toggle Item | Present (needs cleaning) | Needs Cleanup | \+0.02 |

## **6.2 String Substitution Examples**

* "evacuate from your home before katrina or rita hit" → "Did you evacuate from your home before the disaster hit?"  
* "salarys" → "salary payments"  
* "received stimulus payment" → "Did you receive a stimulus payment or other emergency government support?"

# **7\. Module Selection Algorithm**

The select\_for\_time\_budget() function implements a greedy selection strategy to maximize utility within a fixed time constraint.

**Process:**

1. Select Generic Core items first (sorted by R\_i descending)  
2. Fill remaining time budget with highest-R\_i toggle items

Constraint: Total ≤ MAX\_SECONDS \= 1800 seconds (30 minutes)

Module Selection Flow Diagram:

    Scored DataFrame (52 questions)  
              │  
              ▼  
    ┌─────────────────────────┐  
    │  STEP 1: Generic Core   │  
    │  Sort by Ri (desc)      │  
    │  Greedily add items     │  
    └───────────┬─────────────┘  
                │  
    Running total: \~XX seconds  
                │  
                ▼  
    ┌─────────────────────────┐  
    │  STEP 2: Toggle Items   │  
    │  Sort remaining by Ri   │  
    │  Greedily add items     │  
    └───────────┬─────────────┘  
                │  
                ▼  
    ┌─────────────────────────┐  
    │  OUTPUT                 │  
    │  28 selected questions  │  
    │  Total: 29.17 minutes   │  
    │  (1750.2 seconds)       │  
    └─────────────────────────┘

# **8\. Integration of Respondent Data**

This section explains how empirical respondent data distributions from actual crises validated and refined the model.

## **8.1 Federal Government Shutdown (2018-2019)**

* Variable ER34810: individual-level shutdown impact flag  
* Variables ER72973–ER72991: family-level economic disruptions  
* Key finding: 2.5% of families reported acute financial difficulties  
* Behavioral responses: 70.6% decreased spending, 28.3% visited food banks  
* Impact on model: Validates heavy weighting of "Financial Coping" construct (0.45)

## **8.2 COVID-19 Pandemic (2020-2021)**

* Variable ER34999: COVID-19 infection tracking  
* Variable ER35000: vaccination tracking  
* Variables ER81347–ER81397: charitable donations during pandemic  
* Mortality spike: 339 known deaths between 2019-2021  
* Vaccination gradient: 63.1% vaccinated by June 2021  
* Impact on model: Confirms importance of "Trauma/Health" (0.58) and "Government Aid" (0.48)

## **8.3 Stimulus Payment Response Heterogeneity**

* April 2020 stimulus: uniform consumption increase across all income quartiles  
* January 2021 stimulus: highly heterogeneous — low-income spent out of necessity, high-income saved  
* Low-wage workers in high-rent areas: employment plummeted 40%  
* Impact on model: Validates Government Aid construct weight (0.48) as essential for macro-fiscal policy

# **9\. Artifact Output Schema**

## **9.1 Master CSV: PSID\_Ranked\_Questions\_Final.csv**

25-column schema containing:

* question\_text, source, module\_type, toggle\_category  
* keywords, n\_keywords, word\_count, complexity  
* Ui, Bi, Ri (base scores)  
* selected\_for\_module, selected, minutes  
* Pi, augmented\_utility, idf\_strength, redundancy\_penalty  
* construct\_bonus, portability\_bonus, construct\_count  
* recommended\_wording, keyword\_list, tagged\_keywords, constructs

Quantitative columns rounded to 3 decimal places. List columns serialized with repr().

## **9.2 Summary JSON: psid\_artifact\_summary.json**

Contains:

* rows, selected\_rows, selected\_minutes (29.17), all\_minutes (68.95)  
* avg\_ri (2.079), max\_ri (5.667)  
* toggle\_counts, source\_counts, construct\_counts

## **9.3 Dashboard Payload: psid\_dashboard\_data.js**

JavaScript object for HTML/React dashboards. Contains summary, rows array, and recommendations for visualization and interactivity.

## **9.4 Five PNG Figures**

* fig\_top\_ranked\_questions.png — highest Pi and Ri scores  
* fig\_toggle\_comparison.png — Generic Core vs Toggle distributions  
* fig\_utility\_vs\_burden.png — scatter plot (optimal \= upper-left quadrant)  
* fig\_construct\_heatmap.png — questions × constructs matrix  
* fig\_time\_budget.png — cumulative time vs 30-min cap

# **10\. Complete Worked Example**

Walk through one question end-to-end:

**Question:** "Any financial difficulties"  
**Source:** COVID-19 module

3. **Keyword Parsing:** parse\_keywords() extracts: \["any financial difficulties", "financial difficulties"\]  
4. **Taxonomy Matching:** tag\_keywords() matches Financial Coping, weight=0.85  
5. **Construct Extraction:** extract\_constructs() → \["Financial Coping"\]  
6. **Utility:** U\_i \= 0.85 \+ 0.85 \= 1.70  
7. **Burden:** word\_count \= 3, complexity \= 0.0 → B\_i \= max(0.30, 0.1) \= 0.30  
8. **Rank Index:** R\_i \= 1.70 / 0.30 \= 5.667  
9. **Time Estimate:** minutes \= (3 × 7\) / 60 \= 0.35 minutes  
10. **Toggle Classification:** "Generic Core"  
11. **Portability:** No source-specific terms → portability\_bonus \= \+0.16  
12. **Deployable Wording:** "Have you experienced any financial difficulties because of the crisis?"  
13. **Augmented Scoring:** Pi \= 7.187 (highest in corpus)  
14. **Selection:** Selected \= True (Generic Core, within time budget)

# **11\. Assumptions and Limitations**

15. Reading rate assumption: 7 seconds per word is a conservative estimate for telephone/web administration  
16. Complexity scoring uses entity count \+ clause markers — does not capture all cognitive difficulty  
17. Taxonomy is manually curated (63 entries) — may miss emerging crisis-specific vocabulary  
18. TF-IDF computed over 52-item corpus — small corpus may reduce IDF discrimination  
19. Greedy selection algorithm — not guaranteed globally optimal, but computationally efficient  
20. Construct priority weights are expert-derived, informed by but not statistically fitted to respondent data  
21. Portability bonus values (0.02–0.16) are heuristic, not estimated from response-rate data

# **12\. References**

22. Panel Study of Income Dynamics (PSID): Main Interview, 2021 (ICPSR 39190\) — https://www.icpsr.umich.edu/web/sbeccc/studies/39190  
23. Fifty Years of the Panel Study of Income Dynamics — https://pmc.ncbi.nlm.nih.gov/articles/PMC6820672/  
24. PSID 2021 Longitudinal Weights — https://psidonline.isr.umich.edu/data/weights/long\_weight\_21.pdf  
25. User Guide 2019 — https://psidonline.isr.umich.edu/data/Documentation/UserGuide2019.pdf  
26. User Guide 2023 — https://psidonline.isr.umich.edu/data/Documentation/UserGuide2023.pdf  
27. TAS 2021 User Guide — https://psidonline.isr.umich.edu/cds/TAS21\_UserGuide.pdf  
28. User Guide 2021 — https://psidonline.isr.umich.edu/data/documentation/userguide2021.pdf  
29. generate\_psid\_artifacts.py (internal pipeline script)  
30. PSID Online Data Center — https://psidonline.isr.umich.edu/  
31. 2021 Family File Codebook — https://psidonline.isr.umich.edu/documents/psid/codebook/FAM2021ER\_codebook.pdf