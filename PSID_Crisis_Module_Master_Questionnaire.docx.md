**PSID Generic Crisis Module**

**Master Survey Questionnaire**

*Optimized via NLP-Driven Utility–Burden Analysis*

April 2026

**Document Summary**

| Field | Value |
| :---- | :---- |
| Architecture | Generic Core \+ Crisis-Specific Toggles |
| Generic Core Questions | 18 |
| Pandemic/Disaster Toggle | 14 (5 pandemic \+ 5 disaster \+ 4 trauma) |
| Financial Crisis Toggle | 3 |
| War/Conflict Template | 4 (placeholder) |
| Total Questions | 39 |
| Estimated Duration (Core) | 12–14 minutes |
| Time Budget (Max) | 30 minutes |
| Data Sources | 5 (PSID COVID-19, Katrina 2007, Govt Shutdown, Understanding Society, PSID Generic) |
| Optimization Method | Ri \= Ui / Bi (NLP pipeline with TF-IDF, cosine similarity, construct mapping) |

# **Table of Contents**

1\. Scripting Notes

2\. Module Architecture Overview

3\. Generic Core Module (18 Questions)

4\. Crisis-Specific Toggle: Pandemic / Disaster

5\. Alternate Toggle: Financial Crisis / Shutdown

6\. Template Toggle: War / Armed Conflict

7\. NLP Optimization Methodology Summary

8\. Appendix – Ranked Question Summary Table

9\. References

# **1\. Scripting Notes**

This document specifies the PSID Generic Crisis Module questionnaire, an NLP-optimized instrument designed for rapid deployment across diverse crisis contexts. The two-tier architecture separates always-applicable items (Generic Core) from crisis-type-specific toggle modules.

**Modules deployed in order:**

Generic Core Module — Always administered (18 questions, approximately 12–14 minutes)

Crisis-Specific Toggle Module — Activated based on crisis type classification. Only one toggle active per administration.

**Toggle activation table:**

| Toggle Module | Activation Condition | Questions |
| :---- | :---- | :---- |
| Pandemic / Disaster | Pandemic, epidemic, natural disaster | 14 items (5 \+ 5 \+ 4\) |
| Financial Crisis / Shutdown | Government shutdown, recession, banking crisis | 3 items |
| War / Armed Conflict | Armed conflict, civil unrest, displacement (template) | 4 items (placeholder) |

**Crisis classification variable:**

**cr\_crisis\_type \[Type of crisis event\]**

1 \= Pandemic / Public health emergency

2 \= Natural disaster (hurricane, flood, earthquake, wildfire)

3 \= Government shutdown / financial crisis

4 \= War / armed conflict

# **2\. Module Architecture Overview**

The questionnaire employs a two-tier architecture:

Tier 1 – Generic Core (Always-On): 18 questions covering demographics, employment, income, financial coping, housing, government aid, and wellbeing. Selected through NLP-driven utility scoring plus expert review.

Tier 2 – Crisis-Specific Toggles: Separate question banks activated by crisis type.

**Optimization Formula:**

*Ri \= Ui / Bi*

*Enhanced Priority Score: Pi \= Augmented\_Utility / (Bi × (1 \+ 0.65 × redundancy\_scaled))*

*Where Augmented\_Utility \= Ui × (1 \+ 0.32×idf\_scaled \+ 0.24×construct\_scaled \+ 0.12×richness\_scaled \+ portability\_bonus)*

Time Budget Constraint: Max 30 minutes (1,800 seconds). Reading rate: 7 seconds per word.

# **3\. Generic Core Module (18 Questions)**

Routing variables: cr\_crisis\_type, cr\_empstat, cr\_findiff

## **3.A Demographics and Household Context (5 questions)**

**\[cr\_age\]**

*Ask all.*

Source: Understanding Society / PSID baseline

NLP metrics: Ri \= 1.67 | Construct: Demographics | Always-on core

What is the respondent's age?

1. \[Numeric textbox: Enter age in years\]

**\[cr\_sex\]**

*Ask all.*

Source: Understanding Society covid-19 survey

NLP metrics: Ri \= 1.23 | Construct: Demographics | Always-on core

And are you...

2. Male

3. Female

4. Another identity or prefer not to say

**\[cr\_addrchk\]**

*Ask all.*

Source: Understanding Society covid-19 survey

NLP metrics: Ri \= 1.17 | Construct: Demographics | Always-on core

Can I just check, are you normally resident at this address?

5. Yes

6. No

**\[cr\_hhsize\]**

*Ask all.*

Source: PSID Generic Crisis Module (expanded)

NLP metrics: Expanded generic item | Construct: Demographics

How many people currently live in your household, including yourself?

7. \[Numeric textbox\]

**\[cr\_depend\]**

*Ask all.*

Source: PSID Generic Crisis Module (expanded)

NLP metrics: Expanded generic item | Household vulnerability context

Do you have any children or dependents currently living with you?

8. Yes

9. No

## **3.B Employment and Income Disruption (5 questions)**

**\[cr\_empstat\]**

*Ask all.*

Source: PSID Generic Crisis Module (expanded)

NLP metrics: Expanded generic item | Construct: Employment

What is your current employment status?

10. Employed full-time

11. Employed part-time

12. Self-employed

13. Temporarily laid off

14. Unemployed, looking for work

15. Unemployed, not looking for work

16. Retired

17. Unable to work (disability)

18. Student

19. Other (please specify)

**\[cr\_stopwork\]**

*IF cr\_empstat \= employed or self-employed in previous wave.*

Source: PSID Government Shutdown Income module

NLP metrics: Ri \= 4.67 | Construct: Employment | Always-on core

Have you stopped this work because of the crisis?

20. Yes

21. No

22. Not applicable

**\[cr\_stopbus\]**

*IF self-employed or business owner in previous wave.*

Source: PSID Government Shutdown Income module

NLP metrics: Ri \= 4.50 | Construct: Economic / Income | Always-on core

Have you stopped working at this business because of the crisis?

23. Yes

24. No

25. Not applicable

**\[cr\_wages\]**

*IF cr\_empstat \= employed.*

Source: PSID Government Shutdown Income module

NLP metrics: Ri \= 2.73 | Construct: Economic / Income | Always-on core

Were there any wages or salary payments from this job during the crisis period?

26. Yes

27. No

28. Don't know

**\[cr\_hourschange\]**

*IF cr\_empstat \= employed or self-employed.*

Source: PSID Generic Crisis Module (expanded)

NLP metrics: Expanded generic item | Construct: Employment

Did your working hours change as a result of the crisis?

29. Increased significantly

30. Increased somewhat

31. Stayed about the same

32. Decreased somewhat

33. Decreased significantly

## **3.C Financial Coping and Public Support (5 questions)**

**\[cr\_findiff\]**

*Ask all.*

Source: PSID COVID-19 module

NLP metrics: Ri \= 5.67 | Construct: Financial Coping | Always-on core (highest ranked)

Have you experienced any financial difficulties because of the crisis?

34. Yes

35. No

**\[cr\_govtaid\]**

*Ask all.*

Source: PSID Generic Crisis Module (expanded, documentation-backed)

NLP metrics: Documentation-backed generic item | Construct: Government Aid

Did you receive any government financial assistance because of the crisis?

36. Yes

37. No

38. Don't know

**\[cr\_copestrategy\]**

*IF cr\_findiff \= Yes.*

Source: PSID Generic Crisis Module (expanded)

NLP metrics: Expanded generic item | Construct: Financial Coping

How did your household manage these financial difficulties? (Select all that apply)

39. Used savings

40. Borrowed from family or friends

41. Sold belongings or assets

42. Took on additional debt (credit card, loan)

43. Reduced spending on food or essentials

44. Took on a second job or extra work

45. Used a food bank or community support

46. Delayed paying bills (rent, mortgage, utilities)

47. Other (please specify)

**\[cr\_incomeloss\]**

*IF cr\_findiff \= Yes.*

Source: PSID Generic Crisis Module (expanded)

NLP metrics: Expanded generic item | Construct: Economic / Income

Approximately how much did your household's total income decrease as a result of the crisis?

48. Less than 10%

49. 10–25%

50. 26–50%

51. More than 50%

52. Don't know

**\[cr\_recovery\]**

*IF cr\_findiff \= Yes.*

Source: PSID Generic Crisis Module (expanded)

NLP metrics: Expanded generic item | Construct: Financial Coping

How long do you expect it will take for your household's finances to return to pre-crisis levels?

53. Already recovered

54. Less than 6 months

55. 6 months to 1 year

56. 1–2 years

57. More than 2 years

58. Don't expect to recover

## **3.D Housing Stability and Wellbeing (3 questions)**

**\[cr\_housing\]**

*Ask all.*

Source: PSID Generic Crisis Module (documentation-backed)

NLP metrics: Documentation-backed generic item | Construct: Housing / Shelter, Economic / Income

Did your household fall behind on rent, mortgage, utilities, or other major bills because of the crisis?

59. Yes

60. No

61. Not applicable (no such obligations)

**\[cr\_wellbeing\]**

*Ask all.*

Source: PSID Generic Crisis Module (documentation-backed)

NLP metrics: Documentation-backed generic item | Construct: Trauma / Health

Since the crisis, how often have you felt worried, unable to relax, or unable to sleep well?

62. Not at all

63. Several days

64. More than half the days

65. Nearly every day

**\[cr\_childimpact\]**

*IF cr\_depend \= Yes.*

Source: PSID Generic Crisis Module (expanded, based on CDS/SDQ items)

NLP metrics: Expanded generic item | Construct: Trauma / Health

Has the crisis noticeably affected the emotional wellbeing or behaviour of any children in your household?

66. Yes, significantly

67. Yes, somewhat

68. No

69. Don't know

# **4\. Crisis-Specific Toggle: Pandemic / Disaster**

Activated when cr\_crisis\_type \= 1 or 2\.

## **4.A Pandemic Economic Impact (5 questions)**

**\[pd\_earningloss\]**

*Ask if crisis type \= pandemic.*

Source: PSID COVID-19 module

NLP metrics: Ri \= 5.67 | Construct: Economic / Income | Documentation-backed

Did you lose earnings because of the pandemic?

70. Yes

71. No

**\[pd\_stimulus\]**

*Ask if crisis type \= pandemic.*

Source: PSID COVID-19 module

NLP metrics: Ri \= 4.67 | Construct: Government Aid | Documentation-backed

Did you receive a stimulus payment or other emergency government support?

72. Yes

73. No

**\[pd\_essential\]**

*Ask if crisis type \= pandemic AND cr\_empstat \= employed.*

Source: PSID COVID-19 module

NLP metrics: Ri \= 4.00 | Construct: Employment | Documentation-backed

Were you working in a job that was considered essential during the crisis?

74. Yes

75. No

**\[pd\_wfh\]**

*Ask if crisis type \= pandemic AND cr\_empstat \= employed.*

Source: PSID COVID-19 module

NLP metrics: Ri \= 3.50 | Construct: Employment

Did you work entirely from home during the crisis?

76. Yes

77. No

78. Partially (mix of home and on-site)

**\[pd\_layoff\]**

*Ask if crisis type \= pandemic.*

Source: PSID COVID-19 module

NLP metrics: Ri \= 2.32 | Construct: Employment

Were you laid off or furloughed because of the pandemic?

79. Yes

80. No

## **4.B Disaster Housing and Displacement (5 questions)**

**\[tr\_evacuate\]**

*Ask if crisis type \= natural disaster.*

Source: PSID Hurricane Katrina 2007 module

NLP metrics: Ri \= 3.18 | Construct: Housing / Shelter | Documentation-backed

Did you evacuate from your home before the disaster hit?

81. Yes

82. No

**\[tr\_flooding\]**

*Ask if crisis type \= natural disaster.*

Source: PSID Hurricane Katrina 2007 module

NLP metrics: Ri \= 2.68 | Construct: Housing / Shelter

Did you experience major flooding in your home during the disaster?

83. Yes

84. No

**\[tr\_damage\]**

*Ask if crisis type \= natural disaster.*

Source: PSID Hurricane Katrina 2007 module

NLP metrics: Ri \= 2.53 | Construct: Housing / Shelter | Documentation-backed

How severe was the damage to your home during the disaster?

85. None / minimal

86. Minor (cosmetic or easily repaired)

87. Moderate (structural repair needed)

88. Severe (uninhabitable)

89. Destroyed

**\[tr\_temphousing\]**

*Ask if tr\_evacuate \= Yes OR tr\_damage \>= Moderate.*

Source: PSID Hurricane Katrina 2007 module

NLP metrics: Ri \= 1.59 | Construct: Housing / Shelter | Documentation-backed

How long did you stay in temporary housing after the disaster?

90. Did not need temporary housing

91. Less than 1 week

92. 1–4 weeks

93. 1–6 months

94. More than 6 months

**\[tr\_returnhome\]**

*Ask if tr\_evacuate \= Yes OR tr\_damage \>= Moderate.*

Source: PSID Hurricane Katrina 2007 module

NLP metrics: Ri \= 1.70 | Construct: Housing / Shelter

Have you been able to return to your original home?

95. Yes, fully returned

96. Yes, but home still under repair

97. No, living elsewhere permanently

98. No, still in temporary housing

## **4.C Trauma, Injury, and Exposure (4 questions)**

**\[tr\_afraid\]**

*Ask if crisis type \= natural disaster.*

Source: PSID Hurricane Katrina 2007 module

NLP metrics: Ri \= 1.68 | Construct: Trauma / Health

How afraid were you during the disaster that you might be seriously injured or killed?

99. Not at all afraid

100. Slightly afraid

101. Moderately afraid

102. Very afraid

103. Extremely afraid

**\[tr\_injured\]**

*Ask if crisis type \= natural disaster.*

Source: PSID Hurricane Katrina 2007 module

NLP metrics: Ri \= 1.45 | Construct: Trauma / Health

Were you physically injured in any way as a result of the disaster?

104. Yes

105. No

**\[tr\_fema\]**

*Ask if crisis type \= natural disaster AND country \= US.*

Source: PSID Hurricane Katrina 2007 module

NLP metrics: Ri \= 2.09 | Construct: Government Aid

Did you receive any help from FEMA?

106. Yes

107. No

108. Did not apply

**\[tr\_distress\]**

*Ask if crisis type \= natural disaster.*

Source: PSID Hurricane Katrina 2007 module (condensed)

NLP metrics: Condensed from multiple Katrina distress items | Construct: Trauma / Health

Since the disaster, how often have you experienced the following?

Repeated disturbing memories or images

109. Not at all

110. Several days

111. More than half the days

112. Nearly every day

Disturbing dreams about the event

113. Not at all

114. Several days

115. More than half the days

116. Nearly every day

Feeling nervous, anxious, or on edge

117. Not at all

118. Several days

119. More than half the days

120. Nearly every day

Trouble relaxing

121. Not at all

122. Several days

123. More than half the days

124. Nearly every day

# **5\. Alternate Toggle: Financial Crisis / Shutdown**

Activated when cr\_crisis\_type \= 3\.

**\[fc\_manage\]**

*Ask if crisis type \= financial crisis / government shutdown.*

Source: PSID Government Shutdown Crisis module

NLP metrics: Ri \= 3.72 | Construct: Financial Coping | Documentation-backed

How did your household manage financial difficulties caused by the shutdown? (Select all that apply)

125. Used savings

126. Borrowed from family or friends

127. Sold belongings

128. Took on debt

129. Reduced spending

130. Other

**\[fc\_paycheck\]**

*IF cr\_empstat \= employed.*

Source: PSID Government Shutdown prototype extension

NLP metrics: Construct: Economic / Income

Did your household miss a paycheck or salary payment because of the shutdown?

131. Yes

132. No

133. Not applicable

**\[fc\_backpay\]**

*IF fc\_paycheck \= Yes.*

Source: PSID Government Shutdown prototype extension

NLP metrics: Construct: Government Aid

Did you expect to receive back pay or repayment later?

134. Yes

135. No

136. Unsure

# **6\. Template Toggle: War / Armed Conflict**

Activated when cr\_crisis\_type \= 4\. These are placeholders for future development — not yet NLP-scored.

**\[wc\_displace\]**

*Ask if crisis type \= armed conflict.*

Source: PSID War/Conflict template (placeholder)

NLP metrics: Template | Construct: Housing / Shelter / Trauma

Were you forced to leave your home because of armed conflict or security concerns?

137. Yes

138. No

**\[wc\_workint\]**

*Ask if crisis type \= armed conflict.*

Source: PSID War/Conflict template (placeholder)

NLP metrics: Template | Construct: Employment / Economic-Income

Did conflict interrupt your work, business activity, or income source?

139. Yes

140. No

141. Not applicable

**\[wc\_violence\]**

*Ask if crisis type \= armed conflict.*

Source: PSID War/Conflict template (placeholder)

NLP metrics: Template | Construct: Trauma / Health

Did you or anyone in your immediate family experience injury, detention, or threats of violence?

142. Yes

143. No

144. Prefer not to say

**\[wc\_agency\]**

*Ask if crisis type \= armed conflict.*

Source: PSID War/Conflict template (placeholder)

NLP metrics: Template | Construct: Government Aid

Did you receive assistance from government, humanitarian, or refugee-support agencies?

145. Yes

146. No

147. Not applicable

# **7\. NLP Optimization Methodology Summary**

This questionnaire represents the output of an NLP-driven optimization process that evaluated 52 candidate questions sourced from 5 historical PSID modules and external surveys (PSID COVID-19, Hurricane Katrina 2007, Government Shutdown prototype, Understanding Society, and PSID Generic Crisis baseline).

The NLP pipeline utilized dual-phase analysis: (1) RAKE-based keyword extraction and spaCy-based semantic parsing to identify construct themes across the candidate pool, and (2) TF-IDF and cosine similarity scoring to measure question redundancy and unique informational contribution. A 63-entry crisis taxonomy classified each question's applicability across 4 crisis types.

Selection prioritized the Ri \= Ui / Bi metric (utility divided by respondent burden), enhanced by the formula:

*Pi \= Augmented\_Utility / (Bi × (1 \+ 0.65 × redundancy\_scaled))*

This constraint-optimization approach, combined with expert panel review and time-budget validation (30-minute maximum), resulted in the selection of 18 generic core questions and 21 toggle-specific items (14 pandemic/disaster, 3 financial crisis, 4 war/conflict) totaling 39 questions across all modules.

# **8\. Appendix – Ranked Question Summary Table**

| Variable | Question Text (abbreviated) | Toggle Category | Ri Score | Selected |
| :---- | :---- | :---- | :---- | :---- |
| cr\_age | Respondent age | Generic Core | 1.67 | Yes |
| cr\_sex | Respondent sex | Generic Core | 1.23 | Yes |
| cr\_addrchk | Address check | Generic Core | 1.17 | Yes |
| cr\_hhsize | Household size | Generic Core | — | Yes |
| cr\_depend | Dependents | Generic Core | — | Yes |
| cr\_empstat | Employment status | Generic Core | — | Yes |
| cr\_stopwork | Stopped work | Generic Core | 4.67 | Yes |
| cr\_stopbus | Stopped business | Generic Core | 4.50 | Yes |
| cr\_wages | Wages during crisis | Generic Core | 2.73 | Yes |
| cr\_hourschange | Change in work hours | Generic Core | — | Yes |
| cr\_findiff | Financial difficulties | Generic Core | 5.67 | Yes |
| cr\_govtaid | Government assistance | Generic Core | — | Yes |
| cr\_copestrategy | Coping strategy | Generic Core | — | Yes |
| cr\_incomeloss | Income loss estimate | Generic Core | — | Yes |
| cr\_recovery | Financial recovery outlook | Generic Core | — | Yes |
| cr\_housing | Housing instability | Generic Core | — | Yes |
| cr\_wellbeing | Wellbeing check | Generic Core | — | Yes |
| cr\_childimpact | Impact on children | Generic Core | — | Yes |
| pd\_earningloss | Lost earnings (pandemic) | Pandemic/Disaster | 5.67 | Yes |
| pd\_stimulus | Stimulus payment | Pandemic/Disaster | 4.67 | Yes |
| pd\_essential | Essential work | Pandemic/Disaster | 4.00 | Yes |
| pd\_wfh | Work from home | Pandemic/Disaster | 3.50 | Yes |
| pd\_layoff | Layoff/furlough | Pandemic/Disaster | 2.32 | Yes |
| tr\_evacuate | Evacuation (disaster) | Pandemic/Disaster | 3.18 | Yes |
| tr\_flooding | Home flooding | Pandemic/Disaster | 2.68 | Yes |
| tr\_damage | Property damage | Pandemic/Disaster | 2.53 | Yes |
| tr\_temphousing | Temporary housing | Pandemic/Disaster | 1.59 | Yes |
| tr\_returnhome | Return to home | Pandemic/Disaster | 1.70 | Yes |
| tr\_afraid | Fear during disaster | Pandemic/Disaster | 1.68 | Yes |
| tr\_injured | Physical injury | Pandemic/Disaster | 1.45 | Yes |
| tr\_fema | FEMA assistance | Pandemic/Disaster | 2.09 | Yes |
| tr\_distress | Post-disaster distress | Pandemic/Disaster | — | Yes |
| fc\_manage | Financial difficulty management | Financial Crisis | 3.72 | Yes |
| fc\_paycheck | Missed paycheck | Financial Crisis | — | Yes |
| fc\_backpay | Back pay expectation | Financial Crisis | — | Yes |
| wc\_displace | Conflict displacement | War/Conflict | — | Yes |
| wc\_workint | Conflict work interruption | War/Conflict | — | Yes |
| wc\_violence | Violence exposure | War/Conflict | — | Yes |
| wc\_agency | Agency assistance | War/Conflict | — | Yes |

# **9\. References**

148. Panel Study of Income Dynamics (PSID): Main Interview, 2021 (ICPSR 39190). https://www.icpsr.umich.edu/web/sbeccc/studies/39190

149. Fifty Years of the Panel Study of Income Dynamics. https://pmc.ncbi.nlm.nih.gov/articles/PMC6820672/

150. PSID 2021 Longitudinal Weights. https://psidonline.isr.umich.edu/data/weights/long\_weight\_21.pdf

151. User Guide 2019\. https://psidonline.isr.umich.edu/data/Documentation/UserGuide2019.pdf

152. User Guide 2023\. https://psidonline.isr.umich.edu/data/Documentation/UserGuide2023.pdf

153. TAS 2021 User Guide. https://psidonline.isr.umich.edu/cds/TAS21\_UserGuide.pdf

154. User Guide 2021\. https://psidonline.isr.umich.edu/data/documentation/userguide2021.pdf

155. 2021 Family File Codebook. https://psidonline.isr.umich.edu/documents/psid/codebook/FAM2021ER\_codebook.pdf

156. Cross-Sectional Weights 2019\. https://psidonline.isr.umich.edu/data/weights/cross\_sec\_weights\_19.pdf

157. CDS Brochure. https://psidonline.isr.umich.edu/guide/brochures/cds.pdf