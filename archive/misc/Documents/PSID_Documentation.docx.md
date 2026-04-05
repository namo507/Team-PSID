

**PSID Generic Crisis Module**  
Questionnaire Specification Document  
Team PSID

*Optimized via NLP-Driven Utility–Burden Analysis*

\[22/03/2026\]

| Architecture | Generic Core \+ Crisis-Specific Toggles |
| :---- | :---- |
| **Generic Core Questions** | 18 |
| **Pandemic/Disaster Toggle** | 14 (5 pandemic \+ 5 disaster \+ 4 trauma) |
| **Financial Crisis Toggle** | 3 |
| **War/Conflict Template** | 4 (placeholder) |
| **Total Questions** | 39 |
| **Estimated Duration (Core)** | 12–14 minutes |
| **Time Budget (Max)** | 30 minutes |
| **Data Sources** | 4 (PSID COVID-19, Katrina 2007, Govt Shutdown, Understanding Society) |
| **Optimization Method** | Ri \= Ui / Bi (RAKE \+ spaCy NLP pipeline) |

**Table of Contents**

**1\. Scripting Notes**

**2\. Module Architecture Overview**

**3\. Generic Core Module (18 questions)**

   **3.A  Demographics and Household Context**

   **3.B  Employment and Income Disruption**

   **3.C  Financial Coping and Public Support**

   **3.D  Housing Stability and Wellbeing**

**4\. Crisis-Specific Toggle: Pandemic / Disaster**

   **4.A  Pandemic Economic Impact**

   **4.B  Disaster Housing and Displacement**

   **4.C  Trauma, Injury, and Exposure**

**5\. Alternate Toggle: Financial Crisis / Shutdown**

**6\. Template Toggle: War / Armed Conflict**

**7\. NLP Optimization Methodology**

**8\. Appendix – Ranked Question Summary Table**

**1\. Scripting Notes**

This document specifies the PSID Generic Crisis Module questionnaire, an NLP-optimized instrument designed for rapid deployment across diverse crisis contexts. The two-tier architecture separates always-applicable items (Generic Core) from crisis-type-specific toggle modules.

The following modules are deployed in this order within the questionnaire:

**Generic Core Module – Always administered (18 questions, approximately 12–14 minutes).**

**Crisis-Specific Toggle Module – Activated based on crisis type classification. Only one toggle is active per administration:**

| Toggle Module | Activation Condition | Questions |
| :---- | :---- | :---- |
| Pandemic / Disaster | Pandemic, epidemic, natural disaster | 14 items (5 \+ 5 \+ 4\) |
| Financial Crisis / Shutdown | Government shutdown, recession, banking crisis | 3 items |
| War / Armed Conflict | Armed conflict, civil unrest, displacement (template) | 4 items (placeholder) |

Toggle selection is driven by the crisis classification variable:

**cr\_crisis\_type \[Type of crisis event\]**

1 \= Pandemic / Public health emergency

2 \= Natural disaster (hurricane, flood, earthquake, wildfire)

3 \= Government shutdown / financial crisis

4 \= War / armed conflict

**2\. Module Architecture Overview**

The PSID Generic Crisis Module uses a two-tier architecture to balance measurement comprehensiveness with respondent burden:

**Tier 1 – Generic Core (Always-On)**

18 questions covering demographics, employment disruption, income loss, financial coping, housing stability, government aid, and psychological wellbeing. These items were selected through a combination of NLP-driven utility scoring (using RAKE keyphrase extraction and spaCy noun-phrase chunking) and expert review. Seven items are “always-on core” with the highest Utility–Burden ratios (Ri), and eleven are expanded generic items that ensure construct coverage regardless of crisis type.

**Tier 2 – Crisis-Specific Toggles**

Separate question banks activated depending on the type of crisis. The Pandemic/Disaster toggle draws from PSID COVID-19 and Hurricane Katrina 2007 source instruments. The Financial Crisis toggle draws from the PSID Government Shutdown module. The War/Conflict toggle is a template for future development. Only one toggle is administered per session.

**Optimization Formula**

Each candidate question was scored using: Ri \= Ui / Bi

Where Ui \= sum of expert-assigned keyword weights (from a 63-entry crisis taxonomy across 7 constructs), and Bi \= 0.10 × word\_count \+ 0.20 × complexity\_score (minimum floor of 0.1). Questions with the highest Ri were selected first for the Generic Core, then remaining time budget was allocated to toggle items.

**Time Budget Constraint**

Total maximum: 30 minutes (1,800 seconds). Ideal target for Generic Core: 5–15 minutes. Reading rate assumption: 7 seconds per word. The selected 28-question scored set totals approximately 29.2 minutes.

**3\. Generic Core Module**

### **Variables used for routing – from sample file**

### 

### **cr\_crisis\_type \[Type of crisis event\]**

### 1 \= Pandemic / Public health emergency

### 2 \= Natural disaster

### 3 \= Government shutdown / financial crisis

### 4 \= War / armed conflict

### 

### **Variables used for routing – from other modules**

### cr\_empstat \[Employment status from this module\]

### cr\_findiff \[Financial difficulties flag from this module\]

### 

## **3.A  Section A – Demographics and Household Context**

## These items preserve minimal respondent identity and household structure, while adding enough context to support routing and downstream interpretation across any crisis scenario.

## 

## **cr\_age \[Respondent age\]**

## **Universe: Ask all.**

## **Source: Understanding Society / PSID baseline**

## **Scripting notes: Do not display DK and REF answer options, answer required. Range \[16-110\].**

## **NLP metrics: *Ri \= 1.67 | Construct: Demographics | Always-on core***

## **Text: What is the respondent’s age?**

## **\[Numeric textbox: Enter age in years\]**

## 

## **cr\_sex \[Respondent sex\]**

## **Universe: Ask all.**

## **Source: Understanding Society covid-19 survey**

## **Scripting notes: Do not display DK and REF answer options, answer required.**

## **NLP metrics: *Ri \= 1.23 | Construct: Demographics | Always-on core***

## **Text: And are you…**

## **Male**

## **Female**

## **Another identity or prefer not to say**

## 

## **cr\_addrchk \[Address check\]**

## **Universe: Ask all.**

## **Source: Understanding Society covid-19 survey**

## **Scripting notes: Do not display DK and REF answer options, answer required.**

## **NLP metrics: *Ri \= 1.17 | Construct: Demographics | Always-on core***

## **Text: Can I just check, are you normally resident at this address?**

## **Yes**

## **No**

## 

## **cr\_hhsize \[Household size\]**

## **Universe: Ask all.**

## **Source: PSID Generic Crisis Module (expanded)**

## **Scripting notes: Range \[1-20\]. Answer required.**

## **NLP metrics: *Expanded generic item | Construct: Demographics***

## **Text: How many people currently live in your household, including yourself?**

## **\[Numeric textbox\]**

## 

## **cr\_depend \[Dependents\]**

## **Universe: Ask all.**

## **Source: PSID Generic Crisis Module (expanded)**

## **NLP metrics: *Expanded generic item | Household vulnerability context***

## **Text: Do you have any children or dependents currently living with you?**

## **Yes**

## **No**

## 

## **3.B  Section B – Employment and Income Disruption**

## This block retains the highest-ranked work disruption questions and fills in generic labour-force context that applies across shutdowns, disasters, conflicts, and health emergencies.

## 

## **cr\_empstat \[Employment status\]**

## **Universe: Ask all.**

## **Source: PSID Generic Crisis Module (expanded)**

## **Scripting notes: Single-code. Answer required.**

## **NLP metrics: *Expanded generic item | Construct: Employment***

## **Text: What is your current employment status?**

## **Employed full-time**

## **Employed part-time**

## **Self-employed**

## **Temporarily laid off**

## **Unemployed, looking for work**

## **Unemployed, not looking for work**

## **Retired**

## **Unable to work (disability)**

## **Student**

## **Other (please specify)**

## 

## **cr\_stopwork \[Stopped work\]**

## **Universe: IF cr\_empstat \= employed or self-employed in previous wave.**

## **Source: PSID Government Shutdown Income module**

## **Scripting notes: Answer required.**

## **NLP metrics: *Ri \= 4.67 | Construct: Employment | Always-on core***

## **Text: Have you stopped this work?**

## **Yes**

## **No**

## **Not applicable**

## 

## **cr\_stopbus \[Stopped business\]**

## **Universe: IF self-employed or business owner in previous wave.**

## **Source: PSID Government Shutdown Income module**

## **Scripting notes: Answer required.**

## **NLP metrics: *Ri \= 4.50 | Construct: Employment / Economic-Income | Always-on core***

## **Text: Have you stopped working at this business?**

## **Yes**

## **No**

## **Not applicable**

## 

## **cr\_wages \[Wages or salaries\]**

## **Universe: IF cr\_empstat \= employed.**

## **Source: PSID Government Shutdown Income module**

## **Scripting notes: Answer required.**

## **NLP metrics: *Ri \= 2.73 | Construct: Employment / Economic-Income | Always-on core***

## **Text: Were there any wages or salaries from this job?**

## **Yes**

## **No**

## 

## **cr\_hourfall \[Hours reduction\]**

## **Universe: IF cr\_empstat \= employed or self-employed.**

## **Source: PSID Generic Crisis Module (expanded)**

## **NLP metrics: *Expanded generic item | Construct: Employment***

## **Text: Did your hours of work fall because of the crisis?**

## **Yes, significantly (more than half)**

## **Yes, somewhat**

## **No**

## **Not applicable**

## 

## **cr\_incloss \[Income loss\]**

## **Universe: Ask all.**

## **Source: PSID Generic Crisis Module (expanded)**

## **NLP metrics: *Expanded generic item | Construct: Economic / Income***

## **Text: Did you lose earnings or income because of the crisis?**

## **Yes, all earnings**

## **Yes, some earnings**

## **No**

## 

## 

## **3.C  Section C – Financial Coping and Public Support**

## These questions capture high-value financial strain signals that repeatedly rank well regardless of the original source module.

## 

## **cr\_findiff \[Financial difficulties\]**

## **Universe: Ask all.**

## **Source: PSID COVID-19 survey**

## **Scripting notes: Answer required.**

## **NLP metrics: *Ri \= 5.67 | Construct: Financial coping | Always-on core***

## **Text: Have you experienced any financial difficulties?**

## **Yes**

## **No**

## 

## **cr\_fincope \[Financial coping strategies\]**

## **Universe: IF cr\_findiff \= Yes.**

## **Source: PSID Generic Crisis Module (expanded)**

## **Scripting notes: Multi-code. Select all that apply.**

## **NLP metrics: *Expanded generic item | Construct: Financial coping***

## **Text: How did your household cope with financial strain caused by the crisis?**

## **Used savings**

## **Borrowed from family or friends**

## **Took on additional debt (credit cards, loans)**

## **Sold belongings or assets**

## **Reduced spending on essentials**

## **Accessed community or charity support**

## **Other (please specify)**

## 

## **cr\_govaid \[Government assistance\]**

## **Universe: Ask all.**

## **Source: PSID Generic Crisis Module (expanded)**

## **NLP metrics: *Expanded generic item | Construct: Government aid***

## **Text: Did you receive any government financial assistance because of the crisis?**

## **Yes**

## **No**

## **Do not know**

## 

## 

## **3.D  Section D – Housing Stability and Wellbeing**

## The generic module should still acknowledge housing disruption and psychological strain even when the crisis type is not yet known.

## 

## **cr\_billbehind \[Behind on bills\]**

## **Universe: Ask all.**

## **Source: PSID Generic Crisis Module (expanded)**

## **NLP metrics: *Expanded generic item | Construct: Housing / Shelter / Economic-Income***

## **Text: Did your household fall behind on rent, mortgage, utilities, or other major bills?**

## **Yes**

## **No**

## 

## **cr\_leavehome \[Left home temporarily\]**

## **Universe: Ask all.**

## **Source: PSID Generic Crisis Module (expanded)**

## **NLP metrics: *Expanded generic item | Construct: Housing / Shelter***

## **Text: Did you have to leave your home temporarily because of the crisis?**

## **Yes**

## **No**

## 

## **cr\_homedmg \[Home damage\]**

## **Universe: Ask all.**

## **Source: PSID Generic Crisis Module (expanded)**

## **NLP metrics: *Expanded generic item | Construct: Housing / Shelter***

## **Text: Was your home damaged, unsafe, or otherwise difficult to live in because of the crisis?**

## **Yes**

## **No**

## **Not applicable**

## 

## **cr\_wellbeing \[Psychological wellbeing\]**

## **Universe: Ask all.**

## **Source: PSID Generic Crisis Module (expanded)**

## **Scripting notes: Single-code frequency scale.**

## **NLP metrics: *Expanded generic item | Construct: Trauma / Health***

## **Text: Since the crisis, how often have you felt worried, unable to relax, or unable to sleep well?**

## **Not at all**

## **Several days**

## **More than half the days**

## **Nearly every day**

## 

## 

**4\. Crisis-Specific Toggle: Pandemic / Disaster**

This toggle is activated when cr\_crisis\_type \= 1 (pandemic) or cr\_crisis\_type \= 2 (natural disaster). It combines pandemic economic impact items, disaster housing/displacement items, and trauma exposure items into a single crisis-specific supplement.

## **4.A  Pandemic Economic Impact**

## High-value COVID-era items that remain useful whenever a public-health emergency or wide-scale shutdown affects work and income.

## 

## **pd\_earnloss \[Pandemic earnings loss\]**

## **Universe: Ask if crisis type \= pandemic.**

## **Source: PSID COVID-19 survey**

## **Scripting notes: Answer required.**

## **NLP metrics: *Ri \= 5.67 | Construct: Economic / Income***

## **Text: Did you lose earnings because of the pandemic?**

## **Yes, all of my earnings**

## **Yes, some of my earnings**

## **No**

## 

## **pd\_stimulus \[Stimulus payment\]**

## **Universe: Ask if crisis type \= pandemic.**

## **Source: PSID COVID-19 survey**

## **NLP metrics: *Ri \= 4.67 | Construct: Government aid***

## **Text: Did you receive a stimulus payment?**

## **Yes**

## **No**

## **Do not know**

## 

## **pd\_essential \[Essential worker status\]**

## **Universe: IF cr\_empstat \= employed.**

## **Source: PSID COVID-19 survey**

## **NLP metrics: *Ri \= 4.00 | Construct: Employment***

## **Text: Were you working in a job that was considered essential work?**

## **Yes**

## **No**

## 

## **pd\_remote \[Remote work\]**

## **Universe: IF cr\_empstat \= employed.**

## **Source: PSID COVID-19 survey**

## **NLP metrics: *Ri \= 3.50 | Construct: Employment***

## **Text: Did you only work from home?**

## **Yes, fully remote**

## **No**

## **Not applicable**

## 

## **pd\_layoff \[Layoff or furlough\]**

## **Universe: IF cr\_empstat \= employed in previous wave.**

## **Source: PSID COVID-19 survey**

## **NLP metrics: *Ri \= 2.32 | Construct: Employment***

## **Text: Were you laid off or furloughed because of the pandemic?**

## **Yes, permanently laid off**

## **Yes, temporarily furloughed**

## **No**

## 

## 

## **4.B  Disaster Housing and Displacement**

## Reframed Katrina items that preserve the housing, evacuation, and infrastructure-disruption concepts in a cleaner, crisis-agnostic format.

## 

## **ds\_flooding \[Major flooding\]**

## **Universe: Ask if crisis type \= natural disaster.**

## **Source: PSID Hurricane Katrina 2007 module**

## **NLP metrics: *Ri \= 2.68 | Construct: Housing / Shelter***

## **Text: Did you experience major flooding in your home from the disaster?**

## **Yes**

## **No**

## 

## **ds\_evacuate \[Evacuation\]**

## **Universe: Ask if crisis type \= natural disaster.**

## **Source: PSID Hurricane Katrina 2007 module**

## **NLP metrics: *Ri \= 2.54 | Construct: Housing / Shelter***

## **Text: Did you evacuate from your home before the disaster hit?**

## **Yes**

## **No**

## 

## **ds\_dmgseverity \[Damage severity\]**

## **Universe: Ask if crisis type \= natural disaster.**

## **Source: PSID Hurricane Katrina 2007 module**

## **Scripting notes: Single-code scale.**

## **NLP metrics: *Ri \= 2.53 | Construct: Housing / Shelter***

## **Text: How severe was the property damage to your home?**

## **Total destruction**

## **Major damage (roof, walls, or structural)**

## **Minor damage (cosmetic, windows, landscaping)**

## **No damage**

## 

## **ds\_homedestroy \[Home damaged or destroyed\]**

## **Universe: Ask if crisis type \= natural disaster.**

## **Source: PSID Hurricane Katrina 2007 module**

## **NLP metrics: *Ri \= 1.13 | Construct: Housing / Shelter***

## **Text: Was your home damaged or destroyed by the disaster?**

## **Damaged**

## **Destroyed**

## **Neither**

## 

## **ds\_temphousing \[Temporary housing duration\]**

## **Universe: IF ds\_evacuate \= Yes OR ds\_homedestroy \= Damaged/Destroyed.**

## **Source: PSID Hurricane Katrina 2007 module**

## **Scripting notes: Open numeric or banded.**

## **NLP metrics: *Ri \= 1.59 | Construct: Housing / Shelter***

## **Text: How long did you stay in temporary housing after the disaster?**

## **Less than 1 week**

## **1–4 weeks**

## **1–3 months**

## **3–6 months**

## **6–12 months**

## **More than 12 months**

## **Did not need temporary housing**

## 

## 

## **4.C  Trauma, Injury, and Exposure**

## These questions keep the high-value trauma, fear, injury, and emergency-assistance content visible without forcing the entire Katrina battery.

## 

## **tr\_afraid \[Fear of death or injury\]**

## **Universe: Ask if crisis type \= natural disaster.**

## **Source: PSID Hurricane Katrina 2007 module**

## **Scripting notes: Single-code.**

## **NLP metrics: *Ri \= 1.68 | Construct: Trauma / Health***

## **Text: How afraid were you during the disaster that you might be killed or seriously injured?**

## **Not at all**

## **Somewhat afraid**

## **Very afraid**

## **Extremely afraid**

## 

## **tr\_injured \[Physical injury\]**

## **Universe: Ask if crisis type \= natural disaster.**

## **Source: PSID Hurricane Katrina 2007 module**

## **NLP metrics: *Ri \= 1.45 | Construct: Trauma / Health***

## **Text: Were you physically injured in any way as a result of the disaster?**

## **Yes**

## **No**

## 

## **tr\_fema \[FEMA assistance\]**

## **Universe: Ask if crisis type \= natural disaster AND country \= US.**

## **Source: PSID Hurricane Katrina 2007 module**

## **NLP metrics: *Ri \= 2.09 | Construct: Government aid***

## **Text: Did you receive any help from FEMA?**

## **Yes**

## **No**

## **Did not apply**

## 

## **tr\_distress \[Post-disaster distress\]**

## **Universe: Ask if crisis type \= natural disaster.**

## **Source: PSID Hurricane Katrina 2007 module (condensed)**

## **Scripting notes: Grid format with frequency scale.**

## **NLP metrics: *Condensed from multiple Katrina distress items | Construct: Trauma / Health***

## **Text: Since the disaster, how often have you experienced the following?**

## **Repeated disturbing memories or images – Not at all / Several days / More than half the days / Nearly every day**

## **Disturbing dreams about the event – Not at all / Several days / More than half the days / Nearly every day**

## **Feeling nervous, anxious, or on edge – Not at all / Several days / More than half the days / Nearly every day**

## **Trouble relaxing – Not at all / Several days / More than half the days / Nearly every day**

## 

## 

**5\. Alternate Toggle: Financial Crisis / Shutdown**

Activated when cr\_crisis\_type \= 3\. The scored model selects one shutdown coping item (Ri \= 3.72). Two companion questions are added so the financial toggle reads like a usable mini-module.

**fc\_manage \[Financial difficulty management\]**

**Universe: Ask if crisis type \= financial crisis / government shutdown.**

**Source: PSID Government Shutdown Crisis module**

**Scripting notes: Multi-code. Select all that apply.**

**NLP metrics: *Ri \= 3.72 | Construct: Financial coping***

**Text: How did your household manage financial difficulties caused by the shutdown?**

**Used savings**

**Borrowed from family or friends**

**Sold belongings**

**Took on debt**

**Reduced spending**

**Other**

**fc\_paycheck \[Missed paycheck\]**

**Universe: IF cr\_empstat \= employed.**

**Source: PSID Government Shutdown prototype extension**

**NLP metrics: *Construct: Economic / Income***

**Text: Did your household miss a paycheck or salary payment because of the shutdown?**

**Yes**

**No**

**Not applicable**

**fc\_backpay \[Back pay expectation\]**

**Universe: IF fc\_paycheck \= Yes.**

**Source: PSID Government Shutdown prototype extension**

**NLP metrics: *Construct: Government aid***

**Text: Did you expect to receive back pay or repayment later?**

**Yes**

**No**

**Unsure**

**6\. Template Toggle: War / Armed Conflict**

Activated when cr\_crisis\_type \= 4\. These questions are placeholders for a future scored bank if PSID wants to extend the taxonomy beyond shutdown, pandemic, and disaster coverage. They are not yet NLP-scored and should be treated as prompts for expert review.

**wc\_displace \[Conflict displacement\]**

**Universe: Ask if crisis type \= armed conflict.**

**Source: PSID War/Conflict template (placeholder)**

**Scripting notes: Template – not scored; for future bank.**

**NLP metrics: *Template | Construct: Housing / Shelter / Trauma***

**Text: Were you forced to leave your home because of armed conflict or security concerns?**

**Yes**

**No**

**wc\_workint \[Conflict work interruption\]**

**Universe: Ask if crisis type \= armed conflict.**

**Source: PSID War/Conflict template (placeholder)**

**Scripting notes: Template.**

**NLP metrics: *Template | Construct: Employment / Economic-Income***

**Text: Did conflict interrupt your work, business activity, or income source?**

**Yes**

**No**

**Not applicable**

**wc\_violence \[Violence exposure\]**

**Universe: Ask if crisis type \= armed conflict.**

**Source: PSID War/Conflict template (placeholder)**

**Scripting notes: Template.**

**NLP metrics: *Template | Construct: Trauma / Health***

**Text: Did you or anyone in your immediate family experience injury, detention, or threats of violence?**

**Yes**

**No**

**Prefer not to say**

**wc\_agency \[Agency assistance\]**

**Universe: Ask if crisis type \= armed conflict.**

**Source: PSID War/Conflict template (placeholder)**

**Scripting notes: Template.**

**NLP metrics: *Template | Construct: Government Aid***

**Text: Did you receive assistance from government, humanitarian, or refugee-support agencies?**

**Yes**

**No**

**Not applicable**

**7\. NLP Optimization Methodology**

**7.1  Data Integration**

52 candidate questions were sourced from four historical PSID and longitudinal survey instruments: Hurricane Katrina 2007 follow-up (32 items), COVID-19 pandemic module (9 items), 2019 Federal Government Shutdown Income and Crisis modules (7 items), and Understanding Society Coronavirus Study (4 items).

**7.2  Dual NLP Pipeline**

Each question was processed through two complementary NLP extractors:

RAKE (Rapid Automatic Keyword Extraction): Multi-word keyphrase extraction with a minimum score threshold of 1.0 to filter noise.

spaCy noun-phrase chunking: Using the en\_core\_web\_sm model to capture domain-specific noun phrases not flagged by RAKE.

The union of both extractions forms the keyword set for each question.

**7.3  Crisis Taxonomy Matching**

A 63-entry crisis taxonomy maps keywords to seven constructs with expert-assigned weights:

| Construct | Weight Range | Example Keywords |
| :---- | :---- | :---- |
| Economic / Income | 0.75–0.80 | earnings, income, wages |
| Employment | 0.65–0.75 | job, furloughed, essential work |
| Financial Coping | 0.70–0.85 | savings, debt, financial difficulties |
| Housing / Shelter | 0.80–0.95 | evacuate, flooding, damaged |
| Government Aid | 0.60–0.75 | FEMA, stimulus, government assistance |
| Trauma / Health | 0.85–0.95 | injured, afraid, disturbing memories |
| Demographics | 0.40–0.50 | age, sex, household |

**7.4  Scoring Formula**

Utility (Ui) \= Sum of matched keyword weights from the taxonomy.

Burden (Bi) \= 0.10 × word\_count \+ 0.20 × complexity\_score (minimum floor: 0.1).

Ratio (Ri) \= Ui / Bi. Higher Ri indicates better information yield per unit of respondent effort.

**7.5  Selection Algorithm**

Step 1: Generic Core items are selected first (demographics \+ highest-Ri universal items).

Step 2: Remaining time budget is filled with the highest-Ri toggle questions, subject to the 30-minute ceiling.

Step 3: The NLP-scored set of 28 questions achieves a total estimated duration of 29.2 minutes (within the 30-minute constraint).

**8\. Appendix – Ranked Question Summary**

The table below summarizes the top-ranked questions by Utility–Burden ratio (Ri), showing the NLP-selected items that form the optimized module.

| Question | Source | Toggle | Ri | Selected |
| :---- | :---- | :---- | :---- | :---- |
| Any financial difficulties | COVID-19 | Generic Core | 5.67 | ✓ |
| Lost earnings because of the pandemic | COVID-19 | Pandemic / Disaster | 5.67 | ✓ |
| stopped this work? | Govt Shutdown Income | Generic Core | 4.67 | ✓ |
| Received stimulus payment | COVID-19 | Pandemic / Disaster | 4.67 | ✓ |
| stopped working at this business? | Govt Shutdown Income | Generic Core | 4.50 | ✓ |
| Working in a job that was considered essential work? | COVID-19 | Pandemic / Disaster | 4.00 | ✓ |
| How did you/your family manage any financial difficulties du… | Govt Shutdown Crisis | Financial Crisis | 3.72 | ✓ |
| Only work from home | COVID-19 | Pandemic / Disaster | 3.50 | ✓ |
| Stimulus payments | COVID-19 | Pandemic / Disaster | 3.50 | ✓ |
| Paycheck protection | COVID-19 | Pandemic / Disaster | 3.50 | ✓ |
| Did you evacuate from your home before Katrina or Rita hit? | Hurricane Katrina 2007 | Pandemic / Disaster | 3.18 | ✓ |
| Were/Was there any wages or salarys from this job/these jobs… | Govt Shutdown Income | Generic Core | 2.73 | ✓ |
| Did you experience major flooding in your home from Katrina … | Hurricane Katrina 2007 | Pandemic / Disaster | 2.68 | ✓ |
| How severe was the property damage to your home from Katrina… | Hurricane Katrina 2007 | Pandemic / Disaster | 2.53 | ✓ |
| Laid off or furloughed because of the pandemic | COVID-19 | Pandemic / Disaster | 2.32 | ✓ |
| Since Katrina and Rita, have you been bothered by repeated d… | Hurricane Katrina 2007 | Pandemic / Disaster | 2.18 | ✓ |
| Since Katrina and Rita, have you been bothered by repeated d… | Hurricane Katrina 2007 | Pandemic / Disaster | 2.14 | ✓ |
| Did you lose your job because of Katrina or Rita? | Hurricane Katrina 2007 | Pandemic / Disaster | 2.13 | ✓ |
| How much financial help did you receive from FEMA? | Hurricane Katrina 2007 | Pandemic / Disaster | 2.09 | ✓ |
| Did you experience hurricane force winds at your location du… | Hurricane Katrina 2007 | Pandemic / Disaster | 2.00 | ✓ |
| Since Katrina and Rita, have you had trouble relaxing? | Hurricane Katrina 2007 | Pandemic / Disaster | 1.80 | ✓ |
| Have you been able to return to your original home? | Hurricane Katrina 2007 | Pandemic / Disaster | 1.70 | ✓ |
| How afraid were you during Katrina or Rita that you might be… | Hurricane Katrina 2007 | Pandemic / Disaster | 1.68 | ✓ |
| Calculate respondents age | Understanding Society | Generic Core | 1.67 | ✓ |
| Was your business damaged or destroyed by Katrina or Rita? | Hurricane Katrina 2007 | Pandemic / Disaster | 1.59 | ✓ |
| How long did you stay in temporary housing after Katrina or … | Hurricane Katrina 2007 | Pandemic / Disaster | 1.59 | ✓ |
| And are you... 1\. Male 2\. Female | Understanding Society | Generic Core | 1.23 | ✓ |
| Can I just check, are you normally resident at this address? | Understanding Society | Generic Core | 1.17 | ✓ |

