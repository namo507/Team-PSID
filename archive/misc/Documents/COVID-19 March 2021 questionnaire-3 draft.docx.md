***Understanding Society*** **Coronavirus Study: March 2021 questionnaire** 

\[26/02/2021\]

**Table of contents**

[Scripting notes	2](#scripting-notes)

[ID check and household composition module	3](#id-check-and-household-composition-module)

[Household relationships module	8](#household-relationships-module)

[Self-assessed health module	18](#self-assessed-health-module)

[Coronavirus illness module	19](#coronavirus-illness-module)

[Coronavirus vaccine module	29](#coronavirus-vaccine-module)

[Long term health condition management module	33](#long-term-health-condition-management-module)

[Caring within household module	45](#caring-within-household-module)

[Caring outside the household module	49](#caring-outside-the-household-module)

[Loneliness module	53](#loneliness-module)

[Housing module	54](#housing-module)

[Employment module	59](#employment-module)

[Travel to work module	85](#travel-to-work-module)

[Transport module	88](#transport-module)

[Finance module	91](#finance-module)

[Financial security module	104](#financial-security-module)

[5-11 year-olds: strengths and difficulties questionnaire module	109](#5-11-year-olds:-strengths-and-difficulties-questionnaire-module)

[Neighbourhood cohesion module	118](#neighbourhood-cohesion-module)

[Volunteering module	121](#volunteering-module)

[Life satisfaction module	123](#life-satisfaction-module)

[GHQ module	125](#ghq-module)

[Health linkage consent module	129](#health-linkage-consent-module)

[Serology consent module	132](#serology-consent-module)

[Consent follow-up questions module	135](#heading=h.hqzd24vooqxk)

[Survey device and incentives module	141](#survey-device-and-incentives-module)

[Closing module	143](#closing-module)

# **Scripting notes** {#scripting-notes}

The following modules are to be asked in varying positions and order within the questionnaire: 

* Health linkage consent module  
* Serology consent module  
* Consent follow-up questions module (this module is always the last of the three)

The position of these modules is driven by the randomised allocation variable: 

**ff\_consentpos \[Position and order of consent questions\]**

1. Early – health then serology  
2. Early – serology then health  
3. Early in context – health then serology  
4. Early in context – serology then health  
5. Late – health then serology  
6. Late – serology then health  
7. Early in context – serology, later in context – health 

The consent follow-up questions module is always asked after health linkage consent and serology consent, i.e. in third place.

**Positions in the questionnaire:**

| Treatment group | Label | Position in the questionnaire |
| :---- | :---- | :---- |
| 1, 2 | Early | After the household relationships module |
| 3, 4 | Early in context | After the coronavirus vaccination module |
| 5, 6 | Late | After the GHQ module |
| 7 | Early in context | After the coronavirus vaccination module |
|  | Later in context | After the long-term health condition management module |

# **ID check and household composition module** {#id-check-and-household-composition-module}

### **Variables used for routing – from sample file**

**ff\_country** \[country of residence\] 

1. England  
2. Wales  
3. Scotland  
4. N Ireland  
   

**forename** \[forename\]  
**ff\_dobd** \[date of birth\]  
**ff\_dobm** \[month of birth\]  
**ff\_doby** \[year of birth\]

### **Variables used for routing – from other modules**

n/a

**tsidcheckst \[Time stamp: id check module start\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time arrived at first question in this module

**welsh \[Welsh language\]**    
**Universe:**  IF ff\_country \= 2 // Ask if respondent lives in Wales.  
**Source:** UKHLS covid-19 survey  
**Scripting notes:** Do not display DK and REF answer options, answer required.  
**Text:** Would you like to complete this survey in Welsh or English?  
Hoffech chi gwblhau'r arolwg hwn yn Gymraeg neu yn Saesneg?

1. Welsh/Cymraeg  
2. English/Saesneg

**dob \[Respondent date of birth\]**    
**Universe:**  Ask all.  
**Source:** UKHLS covid-19 survey  
**Scripting notes:** Do not display DK and REF answer options, answer required. Calendar to default to month/year of birth of expected sample member. First name {forename} to appear on screen.   
**Hard check:** If date of birth does not match ff\_dobd/ff\_dobm/ff\_doby  
**Hard check text:** That date of birth does not match the one we hold in our records. Please make sure you have followed your own unique link to this survey and re-select your date of birth.   
**Hard check text 2:** \[Second time hard check failed\] Sorry, that date of birth does not match the one we hold in our records. You will not be able to complete the survey online this month. Please contact contact@understandingsociety.ac.uk with information about this error, and quote your PID: {ff\_pid}  
**Text:** We need to make sure we are surveying the correct person. {Forename}, what is your date of birth?  
*Please click on the red calendar in order to select your date of birth.*  
\[dd/mm/yyyy – calendar function\]

**dobchk \[Check respondent date of birth\]**    
**Universe:**  Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Flag of 1 if the dob matches ff\_dobd/ff\_dobm/ff\_doby, and 0 if these do not match. 

0. No match  
1. Match

**age \[Age \- derived\]**    
**Universe:**  Ask all.  
**Source:** UKHLS covid-19 survey  
**Scripting notes:** Do not display DK and REF answer options, answer required. Range \[16 – 110\].  
**DERIVED**: Calculate respondent’s age.  
\[Numeric textbox\]

**sex\_cv \[Respondent sex\]**    
**Universe.** Ask all.  
**Source:** UKHLS covid-19 survey  
**Scripting notes:** Do not display DK and REF answer options, answer required.  
**Text:** And are you…

1. Male  
2. Female  
3. Prefer not to say  
   

**addrchk \[Address check\]**    
**Universe:**  Ask all.  
**Source:** UKHLS covid-19 survey  
**Scripting notes:** Do not display DK and REF answer options, answer required.  
**Text:** Can I just check, are you normally resident at this address?  
{ff\_address1}  
{ff\_address2}  
{ff\_address3}  
{ff\_address4}  
{ff\_postcode}

1. Yes  
2. No 

**addrnew \[New postcode\]**    
**Universe:**  IF addrchk \= 2 // Ask if changed address.  
**Source:** UKHLS covid-19 survey  
**Scripting notes:** Do not display DK and REF answer options, answer required.  
**Text:** Please can you tell us your new postcode?  
\[Textbox\]

1. I live outside the UK  
   

**addressuk \[New address, UK\]**    
**Universe:** if addrchk \= 2 AND addrnew \= valid postcode // Ask if changed address and valid UK postcode entered.  
**Source:** UKHLS covid-19 survey  
**Scripting notes:** Do not display DK and REF answer options, answer required.  
**Text:** Please can you tell us your new address?  
If you need to leave any of the boxes blank, please click ‘Next’ twice

| House/Building number  | ![][image1] |
| :---- | :---: |
| Street  | ![][image2] |
|  | ![][image3] |
| Town or city  | ![][image4] |
| County  | ![][image5] |
| Postcode  | ![][image6] |
|  |  |

**addressnonuk \[New address, outside UK\]**    
**Universe:** if addrchk \= 2 AND addrnew \= 1 // Ask if changed address and new address is outside the UK.  
**Source:** UKHLS covid-19 survey  
**Scripting notes:** Do not display DK and REF answer options, answer required.  
**Text:** Please enter your address.  
\[Textbox\]

**couplewsh \[Living with a partner\]**    
**Universe:**  IF welsh \= 1 // Ask if survey completed in Welsh.  
**Source:** UKHLS covid-19 survey  
**Scripting notes:** Do not display DK and REF answer options, answer required.  
**Text:** Are you currently living with a partner?

1. Yes  
2. No  
   

**hhcompwsh \[Household composition, excluding respondent\]**    
**Universe:** IF welsh \= 1 // Ask if survey completed in Welsh.  
**Source:** UKHLS covid-19 survey  
**Scripting notes:** Present as a grid. Do not display DK and REF answer options, answer required. Range \[0 – 10\].  
**Text:** Thinking about the people who live in your household. Without counting yourself, how many are…?  
*Please enter your answers in the boxes below. Enter “0” if no-one is in that age group.*  
**hhcompwsha**. Aged 0-4 \[Numeric textbox\]  
**hhcompwshb**. Aged 5-15 \[Numeric textbox\]  
**hhcompwshc**. Aged 16-18 \[Numeric textbox\]  
**hhcompwshd**. Aged 19-69 \[Numeric textbox\]  
**hhcompwshe.** Aged 70 or older \[Numeric textbox\]

**tsidcheckend \[Time stamp: id check module end\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time completed last question in this module

# **Household relationships module** {#household-relationships-module}

**Note:** the questions in this module were not translated into Welsh.   
**Universe for module:** IF ff\_country is not 2 OR (ff\_country \= 2 AND welsh \= 2\) // Ask if respondent is not living in Wales or living in Wales and completed the survey in English. 

### **Variables used for routing – from sample file**

**surveymonth –** calendar month and year of current survey  
January 2021

**ff\_country** \[country of residence\] 

1. England  
2. Wales  
3. Scotland  
4. N Ireland

### **Variables used for routing – from other modules**

**welsh \[Welsh language\]** – ID check and household composition module

1. Welsh   
2. English 

**couplewsh \[Living with a partner\]** – ID check and household composition module

1. Yes  
2. No

**Number of other household members** – ID check and household composition module  
**hhcompwsha – aged 0-4**  
**hhcompwshb – aged 5-15**  
**hhcompwshc – aged 16-18**  
**hhcompwshd – aged 19-69**  
**hhcompwshe – aged 70+**

**tshhrelst \[Time stamp: household relationships module start\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time arrived at first question in this module

**hhnum \[Household size\]**    
**Universe**: Ask all.  
**Source:** UKHLS covid-19 survey  
**Scripting notes:** Do not display DK and REF answer options, answer required. Range \[1 \- 26\].   
**Text:** Including yourself, how many people are currently living in your household? Please include everyone, even if it is only a temporary arrangement.  
\[Numeric text box\] 

**person \[Household members\]**    
**Universe**: IF hhnum \> 1 // Ask if more than one person in household.   
**Source:** UKHLS covid-19 survey  
**Scripting notes** IF hhnum \> 1 display a grid of hhnum-1 rows. Headings for “sex”, “age” and “relationship”. Within each row a drop-down menu for sex \[1 Male/2 Female\], age \[numeric text box, range 0-120\], and drop down box for relationship should appear for every person in the household (excluding the respondent). Do not display DK and REF answer options, answer required.    
**Text:** Thinking about the people other than yourself who currently live in your household, please tell us each person’s sex, age and relationship to you. It may help you to start with the oldest person.

**personsexa** \[sex – drop-down\] **personagea** \[age – numeric text box\] **relationa** \[drop-down\]  
**personsexb** \[sex – drop-down\] **personageb** \[age – numeric text box\] **relationb** \[drop-down\]  
**personsexc** \[sex – drop-down\] **personagec** \[age – numeric text box\] **relationc** \[drop-down\]  
**personsexd** \[sex – drop-down\] **personaged** \[age – numeric text box\] **relationd** \[drop-down\]   
Etc.

**Relation drop down options**

| 1 | Husband/wife/civil partner |
| :---- | :---- |
| 2 | Partner/cohabitee |
| 3 | Son/daughter (incl. adopted, step, foster) |
| 4 | Parent |
| 5 | Brother/sister |
| 6 | Grand-child |
| 7 | Grand-parent |
| 8 | Other relative |
| 9 | Other non-relative |

**couple \[Living with a partner\]**    
**Universe** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED:**   
1\. Yes: IF (welsh \= 1 AND couplewsh \= 1\) OR (welsh is not 1 AND (relationa \= 1, 2 OR relationb \=    
1, 2 OR relationc \= 1, 2 OR relationd \= 1, 2 OR relatione \= 1, 2 OR relationf \= 1, 2 OR relationg \= 1, 2 OR relationh \= 1, 2 OR relationi \= 1, 2 OR relationj \= 1, 2 OR relationk \= 1, 2 OR relationl \= 1, 2 OR relationm \= 1, 2 OR relationn \= 1, 2 OR relationo \= 1, 2 OR relationp \= 1, 2 OR relationq \= 1, 2 OR relationr \= 1, 2 OR relations \= 1, 2 OR relationt \= 1, 2 OR relationu \= 1, 2 OR relationv \= 1, 2 OR relationw \= 1, 2 OR relationx \= 1, 2 OR relationy \= 1, 2))  
2\. No: otherwise

**hhcompa \[Number of household members aged 0-4, excluding respondent\]**    
**Universe**: Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**:   
IF welsh \= 1: hhcompwsha  
IF welsh \= is not 1: Number of household members aged 0-4 based on variables personagea to personagey  
\[Numeric\]

**hhcompb \[Number of household members aged 5-15, excluding respondent\]**    
**Universe**: Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**:   
IF welsh \= 1: hhcompwshb  
IF welsh \= is not 1: Number of household members aged 5-15 based on variables personagea to personagey  
\[Numeric\]

**hhcompc \[Number of household members aged 16-18, excluding respondent\]**    
**Universe**: Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**:   
IF welsh \= 1: hhcompwshc  
IF welsh \= is not 1: Number of household members aged 16-18 based on variables personagea to personagey  
\[Numeric\]

**hhcompd \[Number of household members aged 19-69, excluding respondent\]**    
**Universe**: Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**:   
IF welsh \= 1: hhcompwshd  
IF welsh \= is not 1: Number of household members aged 19-69 based on variables personagea to personagey   
\[Numeric\]

**hhcompe \[Number of household members aged 70 plus, excluding respondent\]**    
**Universe**: Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**:   
IF welsh \= 1: hhcompwshe  
IF welsh \= is not 1: Number of household members aged 70+ based on variables personagea to personagey  
\[Numeric\]

**parent0plus \[Parent of children aged 0-4 in household\]**    
**Universe**: Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: 

1. Yes: IF (relationa \= 3 AND personagea \< 5\) OR (relationb \= 3 AND personageb \< 5\) OR  (relationc \= 3 AND personagec \< 5\) OR  (relationd \= 3 AND personaged \< 5\) OR  (relatione \= 3 AND personagee \< 5\) OR  (relationf \= 3 AND personagef \< 5\) OR  (relationg \= 3 AND personageg \< 5\) OR  (relationh \= 3 AND personageh \< 5\) OR  (relationi \= 3 AND personagei \< 5\) OR  (relationj \= 3 AND personagej \< 5\) OR  (relationk \= 3 AND personagek \< 5\) OR  (relationl \= 3 AND personagel \< 5\) OR  (relationm \= 3 AND personagem \< 5\) OR  (relationn \= 3 AND personagen \< 5\) OR  (relationo \= 3 AND personageo \< 5\) OR  (relationp \= 3 AND personagep \< 5\) OR  (relationq \= 3 AND personageq \< 5\) OR  (relationr \= 3 AND personager \< 5\) OR  (relations \= 3 AND personages \< 5\) OR  (relationt \= 3 AND personaget \< 5\) OR  (relationu \= 3 AND personageu \< 5\) OR  (relationv \= 3 AND personagev \< 5\) OR  (relationw \= 3 AND personagew \< 5\) OR  (relationx \= 3 AND personagex \< 5\) OR  (relationy \= 3 AND personagey \< 5\)  
2. No: otherwise

**parent5plus \[Parent of children aged 5+ in household\]**    
**Universe**: Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: 

1. Yes: IF (relationa \= 3 AND personagea \>= 5\) OR (relationb \= 3 AND personageb \=\> 5\) OR  (relationc \= 3 AND personagec \=\> 5\) OR  (relationd \= 3 AND personaged \=\> 5\) OR  (relatione \= 3 AND personagee \=\> 5\) OR  (relationf \= 3 AND personagef \=\> 5\) OR  (relationg \= 3 AND personageg \=\> 5\) OR  (relationh \= 3 AND personageh \=\> 5\) OR  (relationi \= 3 AND personagei \=\> 5\) OR  (relationj \= 3 AND personagej \=\> 5\) OR  (relationk \= 3 AND personagek \=\> 5\) OR  (relationl \= 3 AND personagel \=\> 5\) OR  (relationm \= 3 AND personagem \=\> 5\) OR  (relationn \= 3 AND personagen \=\> 5\) OR  (relationo \= 3 AND personageo \=\> 5\) OR  (relationp \= 3 AND personagep \=\> 5\) OR  (relationq \= 3 AND personageq \=\> 5\) OR  (relationr \= 3 AND personager \=\> 5\) OR  (relations \= 3 AND personages \=\> 5\) OR  (relationt \= 3 AND personaget \=\> 5\) OR  (relationu \= 3 AND personageu \=\> 5\) OR  (relationv \= 3 AND personagev \=\> 5\) OR  (relationw \= 3 AND personagew \=\> 5\) OR  (relationx \= 3 AND personagex \=\> 5\) OR  (relationy \= 3 AND personagey \=\> 5\)   
2. No: otherwise

**parent015 \[Parent of children aged 0-15 in household\]**    
**Universe**: Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: 

1. Yes: IF (relationa \= 3 AND personagea \< 16\) OR (relationb \= 3 AND personageb \< 16\) OR  (relationc \= 3 AND personagec \< 16\) OR  (relationd \= 3 AND personaged \< 16\) OR  (relatione \= 3 AND personagee \< 16\) OR  (relationf \= 3 AND personagef \< 16\) OR  (relationg \= 3 AND personageg \< 16\) OR  (relationh \= 3 AND personageh \< 16\) OR  (relationi \= 3 AND personagei \< 16\) OR  (relationj \= 3 AND personagej \< 16\) OR  (relationk \= 3 AND personagek \< 16\) OR  (relationl \= 3 AND personagel \< 16\) OR  (relationm \= 3 AND personagem \< 16\) OR  (relationn \= 3 AND personagen \< 16\) OR  (relationo \= 3 AND personageo \< 16\) OR  (relationp \= 3 AND personagep \< 16\) OR  (relationq \= 3 AND personageq \< 16\) OR  (relationr \= 3 AND personager \< 16\) OR  (relations \= 3 AND personages \< 16\) OR  (relationt \= 3 AND personaget \< 16\) OR  (relationu \= 3 AND personageu \< 16\) OR  (relationv \= 3 AND personagev \< 16\) OR  (relationw \= 3 AND personagew \< 16\) OR  (relationx \= 3 AND personagex \< 16\) OR  (relationy \= 3 AND personagey \< 16\)  
2. No: otherwise  
   

**parent1619 \[Parent of children aged 16-19 in household\]**    
**Universe**: Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: 

1. Yes: IF (relationa \= 3 AND personagea \> 15 AND personagea \< 20\) OR (relationb \= 3 AND personageb \> 15 AND personageb \< 20\) OR  (relationc \= 3 AND personagec \> 15 AND personagec \< 20\) OR  (relationd \= 3 AND personaged \> 15 AND personaged \< 20\) OR  (relatione \= 3 AND personagee \> 15 AND personagee \< 20\) OR  (relationf \= 3 AND personagef \> 15 AND personagef \< 20\) OR  (relationg \= 3 AND personageg \> 15 AND personageg \< 20\) OR  (relationh \= 3 AND personageh \> 15 AND personageh \< 20\) OR  (relationi \= 3 AND personagei \> 15 AND personagei \< 20\) OR  (relationj \= 3 AND personagej \> 15 AND personagej \< 20\) OR  (relationk \= 3 AND personagek \> 15 AND personagek \< 20\) OR  (relationl \= 3 AND personagel \> 15 AND personagel \< 20\) OR  (relationm \= 3 AND personagem \> 15 AND personagem \< 20\) OR  (relationn \= 3 AND personagen \> 15 AND personagen \< 20\) OR  (relationo \= 3 AND personageo \> 15 AND personageo \< 20\) OR  (relationp \= 3 AND personagep \> 15 AND personagep \< 20\) OR  (relationq \= 3 AND personageq \> 15 AND personageq \< 20\) OR  (relationr \= 3 AND personager \> 15 AND personager \< 20\) OR  (relations \= 3 AND personages \> 15 AND personages \< 20\) OR  (relationt \= 3 AND personaget \> 15 AND personaget \< 20\) OR  (relationu \= 3 AND personageu \> 15 AND personageu \< 20\) OR  (relationv \= 3 AND personagev \> 15 AND personagev \< 20\) OR  (relationw \= 3 AND personagew \> 15 AND personagew \< 20\) OR  (relationx \= 3 AND personagex \> 15 AND personagex \< 20\) OR  (relationy \= 3 AND personagey \> 15 AND personagey \< 20\)  
2. No: otherwise

**parent511 \[Parent of children aged 5-11 in household\]**    
**Universe**: Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: 

1. Yes: IF (relationa \= 3 AND personagea \> 4 AND personagea \< 12\) OR (relationb \= 3 AND personageb \> 4 AND personageb \< 12\) OR  (relationc \= 3 AND personagec \> 4 AND personagec \< 12\) OR  (relationd \= 3 AND personaged \> 4 AND personaged \< 12\) OR  (relatione \= 3 AND personagee \> 4 AND personagee \< 12\) OR  (relationf \= 3 AND personagef \> 4 AND personagef \< 12\) OR  (relationg \= 3 AND personageg \> 4 AND personageg \< 12\) OR  (relationh \= 3 AND personageh \> 4 AND personageh \< 12\) OR  (relationi \= 3 AND personagei \> 4 AND personagei \< 12\) OR  (relationj \= 3 AND personagej \> 4 AND personagej \< 12\) OR  (relationk \= 3 AND personagek \> 4 AND personagek \< 12\) OR  (relationl \= 3 AND personagel \> 4 AND personagel \< 12\) OR  (relationm \= 3 AND personagem \> 4 AND personagem \< 12\) OR  (relationn \= 3 AND personagen \> 4 AND personagen \< 12\) OR  (relationo \= 3 AND personageo \> 4 AND personageo \< 12\) OR  (relationp \= 3 AND personagep \> 4 AND personagep \< 12\) OR  (relationq \= 3 AND personageq \> 4 AND personageq \< 12\) OR  (relationr \= 3 AND personager \> 4 AND personager \< 12\) OR  (relations \= 3 AND personages \> 4 AND personages \< 12\) OR  (relationt \= 3 AND personaget \> 4 AND personaget \< 12\) OR  (relationu \= 3 AND personageu \> 4 AND personageu \< 12\) OR  (relationv \= 3 AND personagev \> 4 AND personagev \< 12\) OR  (relationw \= 3 AND personagew \> 4 AND personagew \< 12\) OR  (relationx \= 3 AND personagex \> 4 AND personagex \< 12\) OR  (relationy \= 3 AND personagey \> 4 AND personagey \< 12\)  
2. No: otherwise

**parent1217 \[Parent of children aged 12-17 in household\]**    
**Universe**: Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: 

1. Yes: IF (relationa \= 3 AND personagea \> 11 AND personagea \< 18\) OR (relationb \= 3 AND personageb \> 11 AND personageb \< 18\) OR  (relationc \= 3 AND personagec \> 11 AND personagec \< 18\) OR  (relationd \= 3 AND personaged \> 11 AND personaged \< 18\) OR  (relatione \= 3 AND personagee \> 11 AND personagee \< 18\) OR  (relationf \= 3 AND personagef \> 11 AND personagef \< 18\) OR  (relationg \= 3 AND personageg \> 11 AND personageg \< 18\) OR  (relationh \= 3 AND personageh \> 11 AND personageh \< 18\) OR  (relationi \= 3 AND personagei \> 11 AND personagei \< 18\) OR  (relationj \= 3 AND personagej \> 11 AND personagej \< 18\) OR  (relationk \= 3 AND personagek \> 11 AND personagek \< 18\) OR  (relationl \= 3 AND personagel \> 11 AND personagel \< 18\) OR  (relationm \= 3 AND personagem \> 11 AND personagem \< 18\) OR  (relationn \= 3 AND personagen \> 11 AND personagen \< 18\) OR  (relationo \= 3 AND personageo \> 11 AND personageo \< 18\) OR  (relationp \= 3 AND personagep \> 11 AND personagep \< 18\) OR  (relationq \= 3 AND personageq \> 11 AND personageq \< 18\) OR  (relationr \= 3 AND personager \> 11 AND personager \< 18\) OR  (relations \= 3 AND personages \> 11 AND personages \< 18\) OR  (relationt \= 3 AND personaget \> 11 AND personaget \< 18\) OR  (relationu \= 3 AND personageu \> 11 AND personageu \< 18\) OR  (relationv \= 3 AND personagev \> 11 AND personagev \< 18\) OR  (relationw \= 3 AND personagew \> 11 AND personagew \< 18\) OR  (relationx \= 3 AND personagex \> 11 AND personagex \< 18\) OR  (relationy \= 3 AND personagey \> 11 AND personagey \< 18\)  
2. No: otherwise

**parent418 \[Parent of children aged 4-18 in household\]**    
**Universe**: Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: 

1. Yes: IF (relationa \= 3 AND personagea \> 3 AND personagea \< 19\) OR (relationb \= 3 AND personageb \> 3 AND personageb \< 19\) OR  (relationc \= 3 AND personagec \> 3 AND personagec \< 19\) OR  (relationd \= 3 AND personaged \> 3 AND personaged \< 19\) OR  (relatione \= 3 AND personagee \> 3 AND personagee \< 19\) OR  (relationf \= 3 AND personagef \> 3 AND personagef \< 19\) OR  (relationg \= 3 AND personageg \> 3 AND personageg \< 19\) OR  (relationh \= 3 AND personageh \> 3 AND personageh \< 19\) OR  (relationi \= 3 AND personagei \> 3 AND personagei \< 19\) OR  (relationj \= 3 AND personagej \> 3 AND personagej \< 19\) OR  (relationk \= 3 AND personagek \> 3 AND personagek \< 19\) OR  (relationl \= 3 AND personagel \> 3 AND personagel \< 19\) OR  (relationm \= 3 AND personagem \> 3 AND personagem \< 19\) OR  (relationn \= 3 AND personagen \> 3 AND personagen \< 19\) OR  (relationo \= 3 AND personageo \> 3 AND personageo \< 19\) OR  (relationp \= 3 AND personagep \> 3 AND personagep \< 19\) OR  (relationq \= 3 AND personageq \> 3 AND personageq \< 19\) OR  (relationr \= 3 AND personager \> 3 AND personager \< 19\) OR  (relations \= 3 AND personages \> 3 AND personages \< 19\) OR  (relationt \= 3 AND personaget \> 3 AND personaget \< 19\) OR  (relationu \= 3 AND personageu \> 3 AND personageu \< 19\) OR  (relationv \= 3 AND personagev \> 3 AND personagev \< 19\) OR  (relationw \= 3 AND personagew \> 3 AND personagew \< 19\) OR  (relationx \= 3 AND personagex \> 3 AND personagex \< 19\) OR  (relationy \= 3 AND personagey \> 3 AND personagey \< 19\)  
2. No: otherwise

**tshhrelend \[Time stamp: household relationships module end\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time completed last question in this module

# **Self-assessed health module** {#self-assessed-health-module}

### **Variables used for routing – from sample file**

n/a

### **Variables used for routing – from other modules**

n/a 

**tssahst \[Time stamp: sah module start\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time arrived at first question in this module

**scsf1 \[General health\]**  
**Universe**: Ask all.  
**Source:** UKHLS, Quality Metric Inc., 2007   
**Text:** In general, would you say your health is...

1. Excellent   
2. Very good   
3. Good   
4. Fair   
5. Poor 

**tssahend \[Time stamp: sah module end\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time completed last question in this module

# **Coronavirus illness module**   {#coronavirus-illness-module}

### **Variables used for routing – from sample file**

**ff\_prevsurv** \[Whether full respondent in a previous monthly survey\] 

0. No   
1. Yes

**Date of the last monthly interview the respondent completed:**  
**ff\_intd \[dd\]**   
**ff\_intm \[January…\]**   
**ff\_inty \[yyyy\]**

**ff\_country** \[country of residence\] 

1. England  
2. Wales  
3. Scotland  
4. N Ireland

**surveymonth –** calendar month and year of current survey  
January 2021

**ff\_hadsymp \[Previously reported COVID symptoms\]**  
**Notes:** cumulative variable that takes on value “1” if respondent has previously reported 1 to hadsymp  in any previous monthly survey. 

0. Not mentioned  
1. Mentioned

### **Variables used for routing – from other modules**

**welsh \[Welsh language\]** – ID check and household composition module

1. Welsh   
2. English 

**tscovidst \[Time stamp: coronavirus illness module start\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time arrived at first question in this module

**hadsymp \[Has had symptoms that could be coronavirus\]**  
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**Text:** Have you experienced symptoms that could be caused by coronavirus (COVID-19) {IF ff\_prevsurv=0: ? / IF ff\_prevsurv=1: , since the last time you completed this survey on {ff\_intd} {ff\_intm} {ff\_inty}?}

1. Yes  
2. No

**hassymp \[Has symptoms that could be coronavirus\]**  
**Universe:**  IF hadsymp \= 1 // Ask if has had symptoms that could be coronavirus.  
**Source:** UKHLS covid-19 survey  
**Text:** Are you **currently** experiencing symptoms that could be caused by coronavirus?

1. Yes  
2. No

**symptoms \[Symptoms\]**  
**Universe:**  IF hadsymp \= 1 // Ask if has had symptoms that could be coronavirus.  
**Source:** Adapted Wellcome Common Questionnaire 23rd April 2020   
**Scripting notes:** For compatibility with the April 2020 version, use code 11 for ‘None of these’, add new categories as codes 12+**.** Code 11 is exclusive.  
**Text:** Which of the following symptoms have you had?  
*Please select all that apply.*

1. High temperature  
2. A new continuous cough {IF ff\_hadsymp \= 0 // not reported symptoms in earlier surveys}

23\. Persistent coughing {IF ff\_hadsymp \= 1 // has reported symptoms in earlier surveys}  
24\. Loss of concentration {IF ff\_hadsymp \= 1 // has reported symptoms in earlier surveys}  
25\. Difficulty remembering things {IF ff\_hadsymp \= 1 // has reported symptoms in earlier surveys}

3. Shortness of breath or trouble breathing  
4. Runny or stuffy nose   
5. Muscle or body aches  
6. Headaches  
7. Sore throat  
8. Fatigue   
9. Diarrhoea/Digestive issues/Upset stomach   
10. Loss of sense of smell or taste   
12. Decrease in appetite  
13. Sneezing  
14. Sore eyes  
15. Hoarse voice  
16. Dizziness  
17. Tightness in the chest  
18. Chest pain  
19. Chills (feeling too cold)  
20. Difficulty sleeping  
21. Numbness or tingling somewhere in the body  
22. Feeling of heaviness in arms or legs  
11. None of these  
  


**cv19treat \[Medical help for covid19 symptoms\]**  
**Universe:** IF hadsymp \= 1 // Ask if has had symptoms that could be coronavirus.  
**Source:** Adapted Wellcome Common Questionnaire 23rd April 2020   
**Text:** Did you seek medical attention for the symptoms you experienced? 

1. Yes  
2. No  
   

**cv19trwhat \[What medical help for covid19 symptoms\]**  
**Universe:** IF hadsymp \= 1 AND cv19treat \= 1 // Ask if has had symptoms that could be coronavirus and sought medical help.  
**Source:** Adapted Wellcome Common Questionnaire 23rd April 2020   
**Text:** What kind of medical attention did you access?     
*Please select all that apply.*

1. Contacted NHS 111 in England, Wales and Northern Ireland or NHS 24 in Scotland by phone or online   
2. Received an NHS 111 isolation note  
3. Visited pharmacist   
4. Consulted GP/practice nurse over the phone or online  
5. Consulted GP/practice nurse face to face  
6. Received a ‘fit note’ from GP  
7. Walk-in centre   
8. Accident and Emergency  
9. Inpatient hospital stay  
10. Employer’s occupational health service  
11. Other

   
**longcovid \[Has long covid\]**  
**Universe**: IF ff\_hadsymp \= 1 AND hadsymp is not 1 AND (ff\_country is not 2 OR (ff\_country \= 2 AND welsh is not 1)) // Ask if previously reported having covid symptoms, and not reported having symptoms in current survey, and respondent not living in Wales, or living in Wales and did not complete survey in Welsh.  
**Source:** UKHLS covid-19 survey   
**Text:** You previously reported having coronavirus symptoms. Have you recovered from these and returned to your previous level of health?  
1\. Yes  
2\. No

**lgcvsymp \[Long covid symptoms\]**  
**Universe**: IF ff\_hadsymp \= 1 AND hadsymp is not 1 AND longcovid \= 2 AND (ff\_country is not 2 OR (ff\_country \= 2 AND welsh is not 1)) // Ask if previously reported having covid symptoms, and not reported having symptoms in current survey, and has not returned to previous health, and respondent not living in Wales, or living in Wales and did not complete survey in Welsh.  
**Source:** UKHLS covid-19 survey   
**Scripting notes:** For compatibility with ‘symptoms’ for current covid, category numbering is not in order – please follow order below.  
**Text:** Which of the following symptoms do you have?  
*Please select all that apply.*

1. High temperature

23\. Persistent coughing   
24\. Loss of concentration   
25\. Difficulty remembering things 

3. Shortness of breath or trouble breathing  
4. Runny or stuffy nose   
5. Muscle or body aches  
6. Headaches  
7. Sore throat  
8. Fatigue   
9. Diarrhoea/Digestive issues/Upset stomach   
10. Loss of sense of smell or taste   
12. Decrease in appetite  
13. Sneezing  
14. Sore eyes  
15. Hoarse voice  
16. Dizziness  
17. Tightness in the chest  
18. Chest pain  
19. Chills (feeling too cold)  
20. Difficulty sleeping  
21. Numbness or tingling somewhere in the body  
22. Feeling of heaviness in arms or legs  
26. Other

 **lgcvsympoth \[Other symptoms of long covid\]**    
**Universe:** IF ff\_hadsymp \= 1 AND hadsymp is not 1 AND longcovid \= 2 AND lgcvsymp \= 26 AND (ff\_country is not 2 OR (ff\_country \= 2 AND welsh is not 1)) // Ask if previously reported having covid symptoms, and not reported having symptoms in current survey, and has not returned to previous health, and other long covid symptoms, and respondent not living in Wales, or living in Wales and did not complete survey in Welsh.  
**Source:** UKHLS covid-19 survey  
**Text:** What other symptoms do you have?  
\[Textbox\]

**cvtime \[How long had covid\]**    
**Universe**: IF ((ff\_hadsymp \= 1 AND longcovid \= 2\) OR hadsymp \= 1\) AND (ff\_country is not 2 OR (ff\_country \= 2 AND welsh is not 1)) // Ask if previously reported having covid symptoms and has not returned to previous health or reported having symptoms in current survey, and respondent not living in Wales, or living in Wales and did not complete survey in Welsh.  
**Source:** UKHLS covid-19 survey   
**Scripting notes:** Range \[1 \- 60\].  
**Text:** For how many weeks have you experienced coronavirus symptoms?  
\[Numeric textbox\] Weeks

**tested \[Tested for coronavirus\]**  
**Universe:**  Ask all.  
**Source:** UKHLS covid-19 survey  
**Text:** Have you been tested for coronavirus {IF ff\_prevsurv=0: ? / IF ff\_prevsurv=1: since the last time you completed this survey on {ff\_intd} {ff\_intm} {ff\_inty}?}

1. Yes  
2. No

**ntests \[Number of coronavirus tests\]**  
**Universe:**  IF tested \= 1 // Ask if tested for coronavirus.  
**Source:** UKHLS covid-19 survey  
**Scripting notes**: Range \[1 \- 100\].  
**Text:** How many times have you been tested {IF ff\_prevsurv=0: ? / IF ff\_prevsurv=1: since the last time you completed this survey on {ff\_intd} {ff\_intm} {ff\_inty}?}  
\[Numeric textbox\] Times

**testpos \[Whether tested positive for coronavirus\]**  
**Universe:**  IF tested \= 1 // Ask if tested for coronavirus.  
**Source:** UKHLS covid-19 survey  
**Text:** {IF ntests \= 1, MIS, DK, REF: Was this test result / IF ntests \> 1: Were any of these test results} positive, showing that you had coronavirus?

1. Yes  
2. No

**ntestpos \[Number of positive coronavirus tests\]**  
**Universe:**  IF tested \= 1 AND ntests \> 1 AND testpos \= 1 // Ask if tested for coronavirus, and had more than one test, and tested positive.  
**Source:** UKHLS covid-19 survey  
**Scripting notes**: Range \[1 \- 100\].  
**Text:** How many times have you tested positive {IF ff\_prevsurv=0: ? / IF ff\_prevsurv=1: since the last time you completed this survey on {ff\_intd} {ff\_intm} {ff\_inty}?}  
\[Numeric textbox\] Times

**ntestpos\_dv \[Number of positive coronavirus tests, derived\]**  
**Universe:**  IF tested \= 1 AND testpos \= 1 // Ask if tested for coronavirus and tested positive.  
**Source:** UKHLS covid-19 survey  
**DERIVED:** takes value

* 1: IF (tested \= 1 AND ntests \= 1 AND testpos \= 1\) // tested for coronavirus, tested once, and test result was positive  
* ntestpos: IF (tested \= 1 AND ntests \> 1 AND testpos \= 1\) // tested for coronavirus, had more than one test, and tested positive  
* \-9: otherwise // missing

**testdateintro \[Intro to coronavirus test date loop\]**  
**Universe:**  IF tested \= 1 AND ntests \> 1 AND testpos \= 1 AND ntestpos \> 1 // Ask if tested for coronavirus, and had more than one test, and tested positive, and had more than one positive result.   
**Source:** UKHLS covid-19 survey  
**Text:** We would like to ask you about the dates of each of your positive coronavirus tests, starting with the most recent. 

START LOOP.  
LOOP OVER NUMBER OF NTESTPOS\_DV.  

**testwhen3 \[When had coronavirus test\]**  
**Universe:**  IF tested \= 1 AND testpos \= 1 // Ask if tested for coronavirus and tested positive.  
**Source:** UKHLS covid-19 survey   
**Text:** When did you receive the result of your {IF loop \= 1 AND ntestpos\_dv \> 1: **most recent**} positive coronavirus test result {IF loop \> 1: before that}?    
\[dd/mm/yyyy – calendar function\]

END LOOP.

**hadcovid \[Likelihood of having had coronavirus\]**  
**Universe:**  IF hadsymp \= 1 AND (tested \= 2 OR (tested \= 1 AND testpos is not 1)) // Ask if has had symptoms that could be coronavirus, and has not been tested, or tested and result is not positive.  
**Source:** UKHLS covid-19 survey  
**Text:** In your view, how likely is it that you have had COVID-19?

1. Definitely had it  
2. Very likely  
3. Likely  
4. Unlikely  
5. Very unlikely   
6. Don’t know/can’t tell

**testtrace \[Contacted by test\&trace\]**  
**Universe:**  IF tested \= 1 AND testpos \= 1 // Ask if tested for coronavirus and had positive test result.  
**Source:** UKHLS covid-19 survey   
**Text:** Were you contacted by the coronavirus NHS test and trace service after {IF ntestpos\_dv \= 1: your test result? / IF ntestpos\_dv \= 2, …, 100: any of your test results?}

1. Yes  
2. No  
   

**traceinfo2 \[Information provided to test\&trace\]**  
**Universe:**  IF tested \= 1 AND testresult \= 1 AND testtrace \= 1 // Ask if tested for coronavirus, and test result is positive, and contacted by test & trace service.  
**Source:** UKHLS covid-19 survey   
**Text:** Were you able to provide information on places you had been and people you had been in contact with?

1. Yes, all of them   
2. Some of them  
3. No

**traced \[Traced by test\&trace\]**  
**Universe:**  Ask all.  
**Source:** UKHLS covid-19 survey  
**Text:** Have you been contacted by the NHS test and trace service to say you have been in contact with someone who has COVID-19 and should self-isolate {IF surveymonth \= July 2020: ? / IF surveymonth is not July 2020: since the last time you completed this survey on {ff\_intd} {ff\_intm} {ff\_inty}?}

1. Yes  
2. No, but someone in my household has  
3. No

**contactcv19t \[Contact with covid19 case including tracing\]**  
**Universe:**  Ask all.  
**Source:** Adapted from Wellcome Common Questionnaire 23rd April 2020 , extra categories  
**Scripting notes:** Codes 4 and 6 are exclusive. Numbering is deliberately not sequential (to match previous version). Present response options in the order listed below, not in the order of the numbering.  
**Text:** Have you been in close contact with anyone with COVID-19 in the last **two weeks**?  
*Please select all that apply.*

1. Yes, and I was contacted by the NHS test and trace service 

5\.    Yes, and I was notified by the {IF ff\_country \= 1, 2: “NHS COVID-19” app / IF ff\_country \= 3: NHS Scotland “Protect Scotland” app / IF ff\_country \= 4: HSC “StopCOVID NI” app}

2. Yes, but I was **not** notified by the NHS test and trace Service or the app  
3. Yes, I was in contact with a **suspected** COVID-19 case

6\.   No, but someone in my household has

4. No, not to my knowledge

**riskcv19 \[Risk of getting covid19\]**  
**Universe:**  Ask all.  
**Source:** UKHLS covid-19 survey  
**Text:** In your view, how likely is it that you will contract COVID-19 in the **next month**?

1. Very likely   
2. Likely  
3. Unlikely  
4. Very unlikely

**nhsshield3 \[New NHS shielded patient\]**  
**Universe:**  Ask all.   
**Source:** UKHLS covid-19 survey  
**Text:** Since February 2021, have you received a letter, text or email from the NHS or Chief Medical Officer saying that you have been newly added to the shielding list as someone at risk of severe illness if you catch coronavirus? 

1. Yes  
2. No

**tscovidend \[Time stamp: coronavirus illness module end\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time completed last question in this module

# **Coronavirus vaccine module** {#coronavirus-vaccine-module}

**Note:** the questions in this module were not translated into Welsh.   
**Universe for module:** IF ff\_country is not 2 OR (ff\_country \= 2 AND welsh \= 2\) // Ask if respondent is not living in Wales or living in Wales and completed the survey in English. 

### **Variables used for routing – from sample file**

**ff\_country** \[country of residence\] 

1. England  
2. Wales  
3. Scotland  
4. N Ireland

**ff\_hadcvvac \[Had covid-19 vaccine\]**

1. Yes, first vaccination only: IF (hadcvvac \= 1 in at least one previous month AND hadcvvac is not 2 in any previous month) // respondent has reported receiving one covid vaccine jab.  
2. Yes, both vaccinations: IF hadcvvac \= 2 in at least one previous month // respondent has reported receiving two covid vaccine jabs.  
3. No: IF neither code 1 nor code 2 apply // respondent has not reported receiving a covid jab, including if hadcvvac is MIS/DK/REF/NA in previous months. 

### **Variables used for routing – from other modules**

**welsh \[Welsh language\]** – ID check and household composition module

1. Welsh   
2. English 

**tscvvacst \[Time stamp: Coronavirus vaccine module start\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time arrived at first question in this module

**cv2dose \[Had second dose of coronavirus vaccine\]**  
**Universe**: IF ff\_hadcvvac \= 1 // Ask if respondent reported in a previous month that they had a single dose of coronavirus vaccine.  
**Source:** UKHLS covid-19 survey  
**Text:** Have you had the second dose of the coronavirus vaccination? 

1. Yes  
2. No

**cvinvite \[Invited for covid-19 vaccine\]**  
**Universe**: IF ff\_hadcvvac \= 3 // Ask if respondent has not reported in a previous month that they had a coronavirus vaccine.  
**Source:** UKHLS covid-19 survey  
**Text:** Have you been **invited** to have the coronavirus vaccination by the NHS (even if you have not had the vaccination yet)? 

1. Yes  
2. No

**hadcvvac \[Had covid-19 vaccine\]**  
**Universe**: IF ff\_hadcvvac \= 3 // Ask if respondent has not reported in a previous month that they had a coronavirus vaccine.  
**Source:** UKHLS covid-19 survey  
**Text:**  {IF cvinvite \= 2: Even if you have not been invited, have / IF cvinvite \= 1, MIS, DK,REF, NA: Have} you had a coronavirus vaccination? 

1. Yes, first vaccination only  
2. Yes, both vaccinations  
3. No, but I have an appointment  
4. No 

**vaxxer2 \[Likelihood of taking up a coronavirus vaccination\]**  
**Universe**: IF ff\_hadcvvac \= 3 AND hadcvvac \= 4 // Ask if has not reported in a previous month that they had a coronavirus vaccine, and has not reported having a vaccine or an appointment in this survey.    
**Source:** UKHLS covid-19 survey  
**Text:**  When you are offered the coronavirus vaccination, how likely or unlikely would you be to take it?

1. Very likely  
2. Likely  
3. Unlikely  
4. Very unlikely  
   

**vaxno \[Why not take vaccine\]**  
**Universe**: IF ff\_hadcvvac \= 3 AND hadcvvac \= 4 AND vaxxer2 \= 3, 4 // Ask if respondent has not reported in a previous month that they had a coronavirus vaccine, and has not reported having a vaccine or an appointment in this survey, and is unlikely to take the vaccine when invited.  
**Source:** UKHLS covid-19 survey  
**Scripting notes:** Numbering is deliberately not sequential (to match previous version).  
**Text:**  What is the main reason you would not take the vaccine? 

1. The chances of me catching the coronavirus are low   
2. The chances of me becoming seriously unwell from the coronavirus are low  
3. The impact of the coronavirus is being greatly exaggerated  
4. Vaccines are limited and other people need it more than me  
5. Herd immunity will protect me even if I don’t have the vaccine  
6. I don’t think I would be offered the vaccine for free and I wouldn’t pay for it  
7. I don’t think it would be effective at stopping me catching the coronavirus  
8. I am worried about side effects  
9. I am worried about unknown future effects of the vaccine

15\. I am pregnant

10. I don’t trust vaccines  
11. I have a condition which would make it unsafe for me

13\. I cannot get to the vaccination centre (safely)  
14\. Because of my religion

12. Other

**vaxwhy \[Why would take vaccine\]**  
**Universe**: IF ff\_hadcvvac \= 3 AND (hadcvvac \= 1, 2, 3 OR (hadcvvac \= 4 AND vaxxer2 \= 1, 2)) // Ask if respondent has not reported in a previous month that they had a coronavirus vaccine, and in this survey has reported having the vaccine or has an appointment to receive the vaccine, or the respondent has not had the vaccine but is likely to take it when invited.  
**Source:** UKHLS covid-19 survey  
**Scripting notes:** Numbering is deliberately not sequential (to match previous version).  
**Text:**  {IF hadcvvac \= 1, 2: What was your main reason for taking the vaccine? / If hadcvvav \= 3 OR (hadcvvac \= 4 AND vaxxer2 \= 1, 2): What would be your main reason for taking the vaccine?} 

1. To stop me catching the coronavirus or getting very ill from it  
2. To allow me to go out of my home safely again  
3. To allow me to get the help or care I need at home  
4. Because I am a key worker working with high risk groups  
5. To allow me to return to my workplace  
6. To allow my social and family life to get back to normal  
7. To reduce the disruption to my children’s education   
8. Because the vaccine won’t work unless most people in the UK take it  
9. To protect other people from catching the coronavirus  
10. Because I take the vaccines offered or recommended to me

12\. To allow me to travel

11. Other

**tscvvacend \[Time stamp Coronavirus vaccine module end\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time completed last question in this module

# **Long term health condition management module** {#long-term-health-condition-management-module}

### **Variables used for routing – from sample file**

**ff\_prevsurv** \[Whether full respondent in a previous monthly survey\] 

0. No   
1. Yes

**ff\_hcond1 \[Long term health condition: Asthma\]**  
**Notes:** cumulative variable that takes on value “1” if respondent has selected response option 1 (Asthma) in responses to hcond\_cv or hcondnew\_cv in any previous monthly survey. 

0. Not mentioned  
1. Mentioned

**ff\_hcond2 \[Long term health condition: Arthritis\]**  
**Notes:** cumulative variable that takes on value “1” if respondent has selected response option 2 (Arthritis) in responses to hcond\_cv or hcondnew\_cv in any previous monthly survey. 

0. Not mentioned  
1. Mentioned

…. Etc to …

**ff\_hcond28 \[Long term health condition: Cystic fibrosis\]  **  
**Notes:** cumulative variable that takes on value “1” if respondent has selected response option 28 (Cystic fibrosis) in responses to hcond\_cv or hcondnew\_cv in any previous monthly survey. 

0. Not mentioned  
1. Mentioned

**ff\_hcondhas \[Has long term health condition\]**  
**Notes:** cumulative variable that takes on value “1” if any of the variables ff\_hcond1 – ff\_hcond28 have value “1”.

0. Does not have a heath condition  
1. Has a health condition

**ff\_pregnow \[Whether pregnant\]**  
**Notes:** values of pregnow from the last monthly survey completed.  
\-9. Missing  
\-8. Inapplicable  
\-2. Refusal  
\-1. Don’t know

1. Yes  
2. No  
3. Don’t know

**ff\_stillpreg \[Whether still pregnant\]**  
**Notes:** values of stillpreg from the last monthly survey completed.  
\-9. Missing  
\-8. Inapplicable  
\-2. Refusal  
\-1. Don’t know

1. Yes  
2. No  
3. Don’t know

### **Variables used for routing – from other modules**

**sex\_cv \[Respondent sex\] \-** ID and household composition module

1. Male  
2. Female  
3. Prefer not to say

**age \[Age – derived\] \-** ID and household composition module

**tslthealthst \[Time stamp: long term health module start\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time arrived at first question in this module

**hcondimpactintro \[Intro to long term health condition management module\]**  
**Universe**: Ask all.  
**Source:** UKHLS covid-19 survey  
**Text:** The health and social care of many people with long term health conditions has been affected by the coronavirus pandemic. If you have health conditions, we’d like to know the sorts of treatment and support you usually receive and how these have been affected. To start with we would like to ask about long term health conditions you may have.

**hcondnew\_cv** **\[New health conditions diagnosed\]**  
**Universe**: IF ff\_prevsurv \= 1 // Ask if completed at least one previous monthly covid-19 survey.   
**Source:** UKHLS, question HCONDNEW adapted with additional response options  
**Scripting notes:** How to specify comma separation within the list of conditions previously reported? Code 96 is exclusive.  
**Text:** Since you last completed this survey on {ff\_intd} {ff\_intm} {ff\_inty}, has a doctor or other health professional told you that you have any of these conditions? {IF ff\_hcondhas \= 1: You have previously already told us that you have been diagnosed with the following health conditions: {IF ff\_hcond1 \= 1: asthma / IF ff\_hcond2 \= 1: arthritis / ... / IF ff\_hcond28: cystic fibrosis}.}  
*Please select all that apply.*  
1\. Asthma   
2\. Arthritis   
3\. Congestive heart failure    
4\. Coronary heart disease    
5\. Angina    
6\. Heart attack or myocardial infarction    
7\. Stroke    
8\. Emphysema    
11\. Chronic bronchitis   
21\. COPD (Chronic Obstructive Pulmonary Disease)  
28\. Cystic fibrosis    
10\. Hypothyroidism or an under-active thyroid   
12\. Any kind of liver condition   
13\. Cancer or malignancy    
14\. Diabetes    
15\. Epilepsy    
16\. High blood pressure/hypertension  
22\. An emotional, nervous or psychiatric problem    
19\. Multiple Sclerosis   
20\. H.I.V.   
23\. Chronic kidney disease  
24\. Conditions affecting the brain and nerves, such as Parkinson's disease, motor neurone disease, a learning disability or cerebral palsy   
25\. Problems with your spleen or you've had your spleen removed  
26\. Sickle cell disease  
27\. Are very overweight (having a BMI of 40 or above)  
18\. Other long standing/chronic condition   
96\. None of these** **

**arthtypn \[New: if has arthritis\]**  
**Universe**: IF ff\_prevsurv \= 1 AND hcondnew\_cv \= 2 // Ask if completed at least one previous monthly covid-19 survey and reports arthritis as new condition.  
**Source:** UKHLS 

**Text:** What type of arthritis was that?

1. Osteoarthritis  
2. Rheumatoid arthritis  
3. Other type of arthritis  
4. More than one of the above  
5. Don't know  
   

**cancertypn\_cv \[New: if has cancer\]**  
**Universe**: IF ff\_prevsurv \= 1 AND hcondnew\_cv \= 13 // Ask if completed at least one previous monthly covid-19 survey and reports cancer as new condition.  
**Source:** UKHLS, question CANCERTYPN with additional response options  
**Scripting notes:** The numbering is deliberately not sequential for categories 7 and 8\. 

**Text:** What type of cancer or malignancy was that?  
*Please select all that apply.*  
1\. Bowel/colorectal  
2\. Lung  
3\. Breast  
4\. Prostate {IF sex\_cv \= 1 // Male)  
5\. Liver  
6\. Skin cancer or melanoma  
8\. Blood or bone marrow cancer, such as leukaemia  
7\. Other

**mhealthtypn \_cv \[New: mental health\]**  
**Universe**: IF ff\_prevsurv \= 1 AND hcondnew\_cv \= 22 // Ask if completed at least one previous monthly covid-19 survey and reports emotional, nervous or psychiatric problem as new condition.  
**Source:** UKHLS, question MHEALTHTYPN with additional response options  
**Scripting notes:** The numbering is deliberate, codes 1 and 7 are deliberately missing for compatibility with the UKHLS question. Code 20 is exclusive.  
**Text:** What type of emotional, nervous or psychiatric problem was that?   
*Please select all that apply.*

2. Depression  
3. Psychosis or schizophrenia   
4. Bipolar disorder (or 'manic depression')   
5. An eating disorder   
6. Post-traumatic stress disorder   
8. A phobia   
9. Panic attacks   
10. Attention deficit hyperactivity disorder (ADHD) or Attention deficit disorder (ADD)   
11. Post-natal depression   
12. Dementia (including Alzheimers)   
13. Nervous breakdown   
14. A personality disorder   
15. Obsessive compulsive disorder (OCD)   
16. Seasonal affective disorder   
17. Alcohol or drug dependence   
18. Any other anxiety disorder   
19. Any other mental, emotional or neurological problem or condition  
20. Don’t know

**hcond\_treat \[Existing treatments\]**  
**Universe**: Ask All.  
**Source:** UKHLS covid-19 survey

**Scripting notes:** Code 6 is exclusive.   
**Text:** Are you currently receiving treatment or taking medications that may affect your immune system?   
*Please select all that apply.*

1. Medication following an organ transplant   
2. Medicines such as steroid tablets that weaken the immune system   
3. Targeted therapy or chemotherapy for cancer treatment   
4. Radiotherapy for cancer treatment  
5. Other treatment or medication that may affect immune system  
6. None of these

**hcondtreat \[Intro to Long Term Health Condition treatment cancelled module\]**  
**Universe**: Ask all.  
**Source:** UKHLS covid-19 survey  
**Text:** Now we would like to ask whether you had any health care treatment planned and if these plans have been affected by the current coronavirus pandemic.

**treatment \[Treatment planned\]**  
**Universe**: Ask all.  
**Source:** UKHLS covid-19 survey  
**Scripting notes:** Code 5 is exclusive.  
**Text:** {IF ff\_prevsurv \= 0: Since 1st January 2020, have you had or been waiting for NHS treatment? / IF ff\_prevsurv \= 1: Since the last time you completed this survey on {ff\_intd} {ff\_intm} {ff\_inty}, have you had or been waiting for NHS treatment?}  
*Please select all that apply.*

1. Yes, tests/consultations planned or in progress  
2. Yes, operation or procedure planned  
3. Yes, targeted therapy, chemotherapy or radiotherapy planned or in progress  
4. Yes, other treatment planned  
5. No  
   

**canceltreat \[Health condition treatment cancelled\]**  
**Universe**: IF treatment \= 1, 2, 3, 4 // Ask if health condition treatment planned.  
**Source:** UKHLS covid-19 survey  
**Text:** Has your treatment plan(s) been changed in any way?

1. Yes, consultations/treatments cancelled or postponed by NHS  
2. Yes, alternative treatment provided   
3. Yes, I cancelled or postponed treatment  
4. No, treatment continuing as planned  
   

**hcondnowintro2 \[Intro to health & social care current use module\]**  
**Universe**: ASK ALL.  
**Source:** UKHLS covid-19 survey  
**Text:** Thinking about your situation now, we would like to ask you some questions about your current access to NHS and social care services.

**nhsnowgp2 \[Use of NHS now for condition – GP\]**  
**Universe**: ASK ALL.  
**Source:** UKHLS covid-19 survey  
**Text:** Thinking about your situation now, have you been able to access the NHS services you need over the last 4 weeks?  
GP or primary care practice staff?

1. Yes, in person  
2. Yes, online or by phone only  
3. No, not able to access  
4. No, decided not to seek help at this time  
5. Not required  
   

**nhsnowpm2  \[Use of NHS for condition – prescription meds\]**  
**Universe**: ASK ALL.  
**Source:** UKHLS covid-19 survey  
**Text:** Still thinking about your situation now, have you been able to access the NHS services you need…   
Prescription medicine?

1. Yes   
2. No  
3. Not required

**nhsnowop2  \[Use of NHS for condition – outpatients\]**  
**Universe:** ASK ALL.  
**Source:** UKHLS covid-19 survey  
**Text:** Have you been able to access the NHS services you need…   
Hospital or clinic **outpatient**?

1. Yes, in person  
2. Yes, online or by phone only  
3. No, postponed or cancelled by NHS  
4. No, I postponed or cancelled   
5. No, different treatment provided  
6. Not required

**nhsnowip2  \[Use of NHS for condition – inpatients\]**  
**Universe**: ASK ALL.  
**Source:** UKHLS covid-19 survey  
**Text:** Still thinking about your situation now, have you been able to access the NHS services you need…   
Hospital or clinic **inpatient**?

1. Yes   
2. No, postponed or cancelled by NHS  
3. No, I postponed or cancelled   
4. No, different treatment provided  
5. Not required

**nhsnow1112** **\[Use of NHS now for condition – NHS111\]**  
**Universe**: ASK ALL.  
**Source:** UKHLS covid-19 survey  
**Text:** Have you been able to access the NHS services you need…   
NHS 111 in England, Wales and Northern Ireland or NHS 24 in Scotland?

1. Yes   
2. No, not able to access  
3. No, I decided not to seek help at this time  
4. Not required  
   

**chscnowpharm2** **\[Use of CH\&SC now for condition – pharmacists\]**  
**Universe**: ASK ALL.  
**Source:** UKHLS covid-19 survey  
**Text:** Thinking about your situation now, have you been able to access the community health and social care services and support you need to help manage your condition(s) over the last 4 weeks?  
Local pharmacists for advice?

1. Yes, in person  
2. Yes, online or by phone only  
3. No, not able to access  
4. No, decided not to seek help at this time  
5. Not required

**chscnowotcm2** **\[Use of CH\&SC now for condition – otc meds\]**  
**Universe**: ASK ALL.  
**Source:** UKHLS covid-19 survey  
**Text:** Still thinking about your situation now, have you been able to access the community health and social care services and support you need…  
Over the counter medications?

1. Yes   
2. No  
3. Not required  
   

**chscnowcarer2** **\[Use of CH\&SC now for condition – formal carer\]**  
**Universe**: ASK ALL.  
**Source:** UKHLS covid-19 survey  
**Text:** Have you been able to access the community health and social care services and support you need…  
Someone visiting you at home regularly to help with personal care/ medications/ shopping/ cooking/ cleaning/ wound dressing/ injections?

1. Yes, as before  
2. Yes, but reduced support  
3. Yes, with increased support  
4. No  
5. Not required

**chscnowpsy2** **\[Use of CH\&SC now for condition – Psychotherapist**  
**Universe** ASK ALL.  
**Source:** UKHLS covid-19 survey  
**Text:** Still thinking about your situation now, have you been able to access the community health and social care services and support you need…  
Counselling or talking therapy?

1. Yes, in person  
2. Yes, by telephone or online  
3. Yes, group sessions   
4. No  
5. Not required

**pregnow \[Whether pregnant\]**  
**Universe**: IF sex\_cv \= 2 AND age \> 15 AND age \< 50 AND (ff\_prevsurv \= 0 OR (ff\_prevsurv \= 1 AND ff\_pregnow is not 1 AND ff\_stillpreg is not 1)) // Ask if female respondent aged between 16 and 49 and not completed previous survey,  or completed a previous survey and did not report pregnancy or that still pregnant.  
**Source:** UKHLS covid-19 survey  
**Text:** Are you currently pregnant?

1. Yes  
2. No  
3. Don’t know

**stillpreg \[Whether still pregnant\]**  
**Universe**: IF sex\_cv \= 2 AND age \> 15 AND age \< 50 AND ff\_prevsurv \= 1 AND (ff\_pregnow \= 1 OR ff\_stillpreg \= 1\) // Ask if female respondent aged between 16 and 49, and completed a previous survey, and reported pregnancy or still being pregnant.  
**Source:** UKHLS covid-19 survey  
**Text:** Are you still pregnant?

1. Yes  
2. No  
3. Don’t know

**pregscan \[Ongoing care of pregnant women, scans\]**  
**Universe**: IF sex\_cv \= 2 AND age \> 15 AND age \< 50 AND (pregnow \= 1 OR stillpreg \= 1\) // Ask if female respondent aged between 16 and 49, and pregnant.  
**Source:** UKHLS covid-19 survey  
**Text:** Are you still able to attend support services and appointments as planned?  
Blood tests and scans?

1. Yes  
2. No

**pregmidwife \[Ongoing care of pregnant women, midwife\]**  
**Universe**: IF sex\_cv \= 2 AND age \> 15 AND age \< 50 AND (pregnow \= 1 OR stillpreg \= 1\) // Ask if female respondent aged between 16 and 49, and pregnant.  
**Source:** UKHLS covid-19 survey  
**Text:** Are you still able to attend…  
Midwife appointments?

1. Yes, in person  
2. Yes, online or by phone only  
3. No, not able to access  
4. Not required  
   

**pregantenatal \[Ongoing care of pregnant women, antenatal\]**  
**Universe**: IF sex\_cv \= 2 AND age \> 15 AND age \< 50 AND (pregnow \= 1 OR stillpreg \= 1\) // Ask if female respondent aged between 16 and 49, and pregnant.  
**Source:** UKHLS covid-19 survey  
**Text:** Are you still able to attend…  
NHS antenatal classes?

1. Yes, in person  
2. Yes, online or by phone only  
3. No, not able to access  
4. Not required

**tslthealthend \[Time stamp: long term health module end\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time completed last question in this module

# **Caring within household module** {#caring-within-household-module}

**Note:** the questions in this module were not translated into Welsh.   
**Universe for module:** IF ff\_country is not 2 OR (ff\_country \= 2 AND welsh \= 2\) // Ask if respondent is not living in Wales or living in Wales and completed the survey in English. 

## **Variables used for routing – from sample file**

**ff\_country** \[country of residence\] 

1. England  
2. Wales  
3. Scotland  
4. N Ireland

## **Variables used for routing – from other modules**

**welsh \[Welsh language\]** – ID check and household composition module

1. Welsh   
2. English 

**Number of other household members – Household relationship module**   
**hhcompa – aged 0-4**  
**hhcompb – aged 5-15**  
**hhcompc – aged 16-18**  
**hhcompd – aged 19-69**  
**hhcompe – aged 70+**

**tscaringhhst \[Time stamp: caring within household module start\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time arrived at first question in this module

**aidhh \[Cares for handicapped/other in household\]**  
**Universe**: IF hhcompa \> 0 OR hhcompb \> 0 OR hhcompc \> 0 OR hhcompd \> 0  OR hhcompe \> 0 // Ask if not living alone.  
**Source:** UKHLS  
**Text:** Is there anyone living with you who is sick, disabled or elderly whom you look after or give special help to (for example, a sick, disabled or elderly relative, husband, wife or friend etc)?

1. Yes  
2. No 

**aidnum \[Number cared for in household\]**  
**Universe**: IF (hhcompa \> 0 OR hhcompb \> 0 OR hhcompc \> 0 OR hhcompd \> 0  OR hhcompe \> 0\) AND aidhh \= 1 // Ask if not living alone and cares for someone in household.  
**Source:** UKHLS covid-19 survey  
**Scripting notes:** Range \[1 \- 25\].  
**Text:** How many people living with you do you look after or give special help to?  
\[Numeric textbox\] People

**carehhc \[Cares for sick/disabled/elderly in household\]**  
**Universe**: IF (hhcompa \> 0 OR hhcompb \> 0 OR hhcompc \> 0 OR hhcompd \> 0  OR hhcompe \> 0\) AND aidhh \= 1 AND aidnum \>= 1 // Ask if not living alone and cares for 1 or more people in household.  
**Source:** UKHLS covid-19 survey  
**Text:** {IF aidnum \> 1: Thinking of the main person you care for in the household.} Please can you tell us the nature of their condition, disability or illness?  
*Please select all that apply.*

1. A long-term health condition (excluding mental health)  
2. A long-term mental health condition  
3. A learning disability or developmental disorder such as autism  
4. A physical disability  
5. Other problems related to old age    
6. Other

**carehhwho \[Who caring for inside the household\]**  
**Universe**: IF (hhcompa \> 0 OR hhcompb \> 0 OR hhcompc \> 0 OR hhcompd \> 0  OR hhcompe \> 0\) AND aidhh \= 1 // Ask if not living alone and cares for someone in household.  
**Source:** UKHLS covid-19 survey  
**Text:** Who do you give special help to in your household?  
*Please select all that apply.*

1. Children (under 18\)  
2. Adult children   
3. Parents or Grandparents, including in-laws  
4. Siblings  
5. Spouse or partner  
6. Friends  
7. Other relatives  
8. Someone else

**carehhsh \[Share caring responsibilities inside the household\]**  
**Universe**: IF (hhcompa \> 0 OR hhcompb \> 0 OR hhcompc \> 0 OR hhcompd \> 0  OR hhcompe \> 0\) AND aidhh \= 1 // Ask if not living alone and cares for someone in household.  
**Source:** UKHLS covid-19 survey  
**Text:** Do you share these caring responsibilities with another member of the household? 

1. Yes   
2. No  
   

**aidhrs\_cv \[Hours per week spent caring\]**  
**Universe**: IF (hhcompa \> 0 OR hhcompb \> 0 OR hhcompc \> 0 OR hhcompd \> 0  OR hhcompe \> 0\) AND aidhh \= 1 // Ask if not living alone and cares for someone in household.  
**Source:** UKHLS**,** question AIDHRS adapted wording  
**Text:** Now thinking about {IF aidnum \= 1: the person /IF aidnum \> 1: the people} you said you care for in the household, how many hours do you spend each week looking after or helping them?

1. 0 \- 4 hours per week  
2. 5 \- 9 hours per week  
3. 10 \- 19 hours per week  
4. 20 \- 34 hours per week  
5. 35 \- 49 hours per week  
6. 50 \- 99 hours per week  
7. 100 or more hours per week/continuous care  
8. Varies under 20 hours  
9. Varies 20 hours or more  
97. Other

**respitenow \[Hours per week of respite care now\]**  
**Universe**: IF (hhcompa \> 0 OR hhcompb \> 0 OR hhcompc \> 0 OR hhcompd \> 0  OR hhcompe \> 0\) AND aidhh \= 1 // Ask if not living alone and gives care to someone in household  
**Source:** UKHLS covid-19 survey  
**Scripting notes**: Range \[0 – 168\]. Allow one decimal.   
**Text:** Thinking about the last 4 weeks, how many hours per week – if any – of respite or support did you have with caring for {IF aidnum \= 1: the person /IF aidnum \> 1: the people} you have just mentioned, such as at day-care centres, school, college or carers supporting them in the home?   
\[Numeric textbox\] Hours per week

**tscaringhhend \[Time stamp: caring within household module end\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time completed last question in this module

**Caring outside the household module**

**Note:** the questions in this module were not translated into Welsh.   
**Universe for module:** IF ff\_country is not 2 OR (ff\_country \= 2 AND welsh \= 2\) // Ask if respondent is not living in Wales or living in Wales and completed the survey in English. 

## **Variables used for routing – from sample file**

**ff\_country** \[country of residence\] 

1. England  
2. Wales  
3. Scotland  
4. N Ireland

## **Variables used for routing – from other modules**

**welsh \[Welsh language\]** – ID check and household composition module

1. Welsh   
2. English 

**tscareexhhst \[Time stamp: caring outside household module start\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time arrived at first question in this module

**caringintro \[Intro to caring module\]**

**Universe**: Ask all.

**Source:** UKHLS covid-19 survey

**Text:** We would now like to ask you some questions about the help you give to and receive from family and friends living outside of your household

**caring \[Caring for others outside the household\]**  
**Universe**: Ask all.  
**Source:** UKHLS covid-19 survey  
**Text:** Thinking about the last 4 weeks, did you **provide** help or support to family, friends or neighbours who do not live in the same house/flat as you?

1. Yes  
2. No

**carehow \[Caring for others\]**  
**Universe**: IF caring \= 1 // Ask if gives care to someone outside household.  
**Source:** UKHLS covid-19 survey, response options adapted from family network questions in UKHLS  
**Text:** How did you help?  
*Please select all that apply.*

1. Giving them lifts in your car (if you have one)   
2. Shopping for them (including going to the shop or ordering an online delivery)  
3. Providing or cooking meals   
4. Helping with basic personal needs like dressing, eating or bathing   
5. Washing, ironing or cleaning   
6. Dealing with personal affairs e.g. paying bills, writing letters   
7. Assisting with online or internet access  
8. Decorating, gardening or house repairs   
9. Looking after children   
10. Something else  
    

**carewho \[Who caring for outside household\]**  
**Universe**: IF caring \= 1 // Ask if gives care to someone outside household.  
**Source:** UKHLS covid-19 survey  
**Text:** Who did you help?  
*Please select all that apply.*

1. Adult children, including in-laws  
2. Parents or grandparents, including in-laws  
3. Siblings  
4. Spouse or partner  
5. Former spouse or partner  
6. Friends  
7. Neighbours  
8. Someone else

**help \[Receiving care from outside the household\]**  
**Universe**: Ask all.  
**Source:** UKHLS covid-19 survey  
**Text:** Thinking about the last 4 weeks, did you **receive** support from family, neighbours or friends who do not currently live in the same house/flat as you?

1. Yes  
2. No

**helpwhat \[Help receiving\]**  
**Universe**: IF help \= 1 // Ask if receives help from outside household.  
**Source:** UKHLS covid-19 survey, response options adapted from family network questions in UKHLS  
**Text:** What kind of help did you receive?  
*Please select all that apply.*

1. Giving you lifts in their car   
2. Shopping for you (including going to the shop or ordering an online delivery)  
3. Providing or cooking meals   
4. Helping with basic personal needs like dressing, eating or bathing   
5. Washing, ironing or cleaning   
6. Dealing with personal affairs e.g. paying bills, writing letters   
7. Assisting with online or internet access   
8. Decorating, gardening or house repairs   
9. Looking after children   
10. Something else

**helpwho \[Who helping from outside household\]**  
**Universe**: IF help \= 1 // Ask if receives help from outside household.  
**Source:** UKHLS covid-19 survey  
**Text:** Who helped you?  
*Please select all that apply.*

1. Adult children, including in-laws  
2. Parents or grandparents, including in-laws  
3. Siblings  
4. Spouse or partner  
5. Former spouse or partner  
6. Friends  
7. Neighbours  
8. Someone else

**tscareexhhend \[Time stamp: caring outside household module end\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time completed last question in this module

# **Loneliness module**    {#loneliness-module}

### **Variables used for routing – from sample file**

n/a

### **Variables used for routing – from other modules**

n/a

**tslonelyst \[Time stamp: loneliness module start\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time arrived at first question in this module

**sclonely\_cv \[How often feels lonely\]**  
**Universe**: Ask all.  
**Source:** ELSA, in UKHLS, adapted to ask about last 4 weeks.  
**Text:** In the last 4 weeks, how often did you feel lonely?

1. Hardly ever or never  
2. Some of the time  
3. Often

**tslonelyend \[Time stamp: loneliness module end\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time completed last question in this module

**Housing module** 

**Note:** the questions in this module were not translated into Welsh.   
**Universe for module:** IF ff\_country is not 2 OR (ff\_country \= 2 AND welsh \= 2\) // Ask if respondent is not living in Wales or living in Wales and completed the survey in English. 

## **Variables used for routing – from sample file**

**surveymonth – calendar month and year of current survey**  
**January 2021**

**ff\_country** \[country of residence\] 

1. England  
2. Wales  
3. Scotland  
4. N Ireland

## **Variables used for routing – from other modules**

**addrchk \[Address check\]** – ID check module

1. Yes \[still resident at same address\]  
2. No \[address changed\]

**Number of other household members – household relationship module**   
**hhcompb – aged 5-15**  
**hhcompc – aged 16-18**  
**hhcompd – aged 19-69**  
**hhcompe – aged 70+**

**welsh \[Welsh language\]** – ID check and household composition module

1. Welsh   
2. English 

**tshsingst \[Time stamp: housing module start\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time arrived at first question in this module

**whymove \[Why moved\]**  
**Universe**: IF addrchk \= 2 // Ask if respondent has moved.   
**Source:** UKHLS covid-19 survey  
**Scripting notes:** Codes 1 and 4 are mutually exclusive.  
**Text:** The next questions are about your current housing situation.   
Why have you moved home?   
*Please select all that apply.*

1. For a larger home  
2. For more garden or outdoor space  
3. For a nicer area  
4. For a smaller home  
5. To reduce housing costs  
6. To live with another person or household  
7. End of tenancy  
8. Eviction  
9. To take advantage of the stamp duty holiday  
10. For work, or the work of another member of your household  
11. To reduce commuting  
12. For better schools  
13. Other reason

**hsownd\_cv \[House owned or rented\]**  
**Universe**: IF surveymonth \= July 2020 OR (ff\_prevsurv \= 1 AND addrchk \= 2\) // Ask if survey month is July 2020 or respondent has moved.   
**Source:** BHPS, UKHLS, question HSOWND with added response categories  
**Scripting notes:** Numbering is deliberately not sequential. Present response options in the order listed below, not in the order of the numbering. Help text: Shared ownership includes co-ownership and equity sharing schemes: a share in the property is being bought. The occupier may never become the sole owner of the property but will receive a cash sum on leaving the scheme. Where accommodation is owned or part-owned by ex-spouse or separated spouse answer 'owned'. Do not count as rent-free cases where a rent would normally be paid but the whole amount is rebated (or paid direct to the landlord by the DWP through benefit payments). If you live in rent free accommodation owned by relatives answer 'rent free'.  
**Text:** Does your household own this accommodation outright, is it being bought with a mortgage, is it rented or does it come rent-free?

1. Owned outright    
2. Owned/being bought on mortgage    
3. Shared ownership (part-owned part-rented)    
4. Rented (social housing or from council)  

6\. 	Rented (privately)  
5\. 	Rent free    
97\. Other 

**garden \[House outdoor space\]**  
**Universe**: IF ff\_prevsurv \= 0 OR (ff\_prevsurv \= 1 AND addrchk \= 2\) // Ask if not completed previous monthly interview, or completed previous interview and respondent has moved.   
**Source:** UKHLS covid-19 survey  
**Scripting notes:** Code 6 is exclusive.  
**Text:** Does your current accommodation have outdoor space that you can use?   
*Please select all that apply.*

1. Private garden    
2. Shared garden  
3. Balcony  
4. Rooftop garden or terrace  
5. Other outdoor space  
6. No

**deskspace \[Desk space for all\]**  
**Universe**: IF (ff\_prevsurv \= 0 OR (ff\_prevsurv \= 1 AND addrchk \= 2)) AND (hhcompb \> 0 OR hhcompc \> 0 OR hhcompd \> 0 OR hhcompe \> 0\) // Ask if not completed previous monthly interview or completed previous interview and respondent has moved, and at least one other person aged 5+ in the household.  
**Source:** UKHLS covid-19 survey  
**Text:** Thinking about everyone in your household who is currently working from home or home schooling. Does everyone have their own quiet space at a desk or table to work at?

1. Yes   
2. No

**pcnet \[Has access to the internet from home\]**  
**Universe**: IF ff\_prevsurv \= 0 OR (ff\_prevsurv \= 1 AND addrchk \= 2\) // Ask if not completed previous monthly interview, or completed previous interview and respondent has moved.   
**Source:** BHPS, UKHLS   
**Text:** Does your household have access to the internet from home?

1. Yes  
2. No

**expmove \[Expected Move\]**     
**Universe**: Ask all.  
**Source:** UKHLS covid-19 survey  
**Scripting notes:** Range \[0 – 100\].  
**Text:** On a scale of 0-100% how likely do you think it is that you will move home in the next 12 months?   
\[Numeric textbox\] %

**whyexpmove \[Why expect moved\]**  
**Universe:** IF expmove \= 1 to 100 // Ask if positive probability of moving.   
**Source:** UKHLS covid-19 survey  
**Scripting notes:** Codes 1 and 4 are mutually exclusive.  
**Text:** If you did move home, what would be the reason?   
*Please select all that apply.*

1. For a larger home  
2. For more garden or outdoor space  
3. For a nicer area  
4. For a smaller home  
5. To reduce housing costs  
6. To live with another person or household  
7. End of tenancy  
8. Eviction  
9. To take advantage of the stamp duty holiday  
10. For work, or the work of another member of your household  
11. To reduce commuting  
12. For better schools  
13. Other reason

**tshsingend \[Time stamp: housing module end\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time completed last question in this module

# **Employment module**  {#employment-module}

### **Variables used for routing – from sample file**

**ff\_prevsurv** \[Whether full respondent in a previous monthly survey\] 

0. No   
1. Yes  
   

**ff\_intwave7 \[Completed full survey at Wave 7, January 2021\]**

0. Partial or non-respondent at Wave 7 survey  
1. Completed full Wave 7 survey

**surveymonth –** calendar month and year of current survey  
March 2021

**Date of the last monthly interview the respondent completed:**  
**ff\_intd \[dd\] – day**   
**ff\_intm \[January…\] – month**   
**ff\_inty \[yyyy\] – year** 

**ff\_country** \[country of residence\] 

1. England  
2. Wales  
3. Scotland  
4. N Ireland

**ff\_sempderived** \[Employee or self-employed\]   
**Notes:** values of sempderived from the last monthly survey completed.   
\-9. Missing  
\-8. Inapplicable  
\-2. Refusal  
\-1. Don’t know

1. Employed   
2. Self-employed   
3. Both employed and self-employed   
4. Neither

**ff\_hours** \[Hours worked\]  
**Notes**: values of hours from the last monthly survey completed. Range \[0 – 168\]. Allow one decimal.  
Numeric, include 0  
\-9. Missing  
\-8. Inapplicable  
\-2. Refusal  
\-1. Don’t know

**ff\_blwork \[Baseline: worked in Jan Feb 2020\]**  
**Notes:** values of blwork from the first monthly survey the respondent completed. Don’t over-write.   
\-9. Missing  
\-8. Inapplicable   
\-2. Refusal  
\-1. Don’t know

1. Yes, employed  
2. Yes, self-employed  
3. Yes, both employed and self-employed  
4. No

**ff\_sempgovt3b \[Government support for self-employed, round 3\]**

0. Has not received government support for the self-employed in round 3: IF sempgovt3b is not 1 in any of the previous survey months  
1. Has received government support for the self-employed in round 3: IF sempgovt3b \= 1 in any of the previous survey months  
   

### **Variables used for routing – from other modules**

**Number of other household members –** household relationships module  
**hhcompc – aged 16-18**  
**hhcompd – aged 19-69**  
**hhcompe – aged 70+**

**welsh \[Welsh language\]** – ID check module

1. Welsh   
2. English 

**tsempst \[Time stamp: employment module start\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time arrived at first question in this module

**econintro \[Intro to economics module\]**  
**Universe**: Ask all.  
**Source:** UKHLS covid-19 survey  
**Text:** Many people have been affected financially by the coronavirus. We’d like to know how you have been affected, and how you and your household are coping.

**sempchk \[Still employee or self-employed\]**  
**Universe:** IF ff\_prevsurv \= 1 AND ff\_sempderived= 1, 2, 3, 4 // Ask if completed at least one previous monthly survey and ff\_sempderived is not missing.  
**Source:** UKHLS covid-19 survey  
**Text:** Last time you completed this survey on {ff\_intd} {ff\_intm} {ff\_inty} you said you were {IF ff\_sempderived=1: employed / IF ff\_sempderived=2: self-employed / IF ff\_sempderived=3: both employed and self-employed / IF ff\_sempderived=4: neither employed nor self-employed}. Is that still the case? Note that if you have been furloughed you are still employed.

1. Yes  
2. No

**semp \[Employee or self-employed\]**  
**Universe**: IF ff\_prevsurv \= 0 OR (ff\_prevsurv \= 1 AND sempchk is not 1\) // Ask if has not completed any previous monthly surveys, or has completed previous surveys and has not confirmed previous employment status as still applying.  
**Source:** UKHLS covid-19 survey  
**Text:** Thinking about your situation now. Even if you did not do any paid work last week, are you currently employed or self-employed?

1. Yes, employed only  
2. Yes, self-employed only  
3. Both employed and self-employed  
4. No

**sempderived \[Employee or self-employed, derived\]**  
**Universe**: Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED:** 

1. Employed: IF semp=1 OR (sempchk=1 AND ff\_sempderived=1)   
2. Self-employed: IF semp=2 OR (sempchk=1 AND ff\_sempderived=2)  
3. Both employed and self-employed: IF semp=3 OR (sempchk=1 AND ff\_sempderived=3)  
4. No: IF semp=4 OR (sempchk=1 AND ff\_sempderived=4)

**empchk \[Still working for same employer\]**  
**Universe:** IF (ff\_country is not 2 OR (ff\_country \= 2 AND welsh is not 1)) AND (sempderived \= 1, 3\) AND (ff\_intwave7 \= 1\) // Ask if respondent not living in Wales or living in Wales and did not complete survey in Welsh, and employed now and full respondent in January 2021 survey.  
**Source:** UKHLS covid-19 survey  
**Text:** Do you have the same main employer as the last time you completed this survey on {ff\_intd} {ff\_intm} {ff\_inty}?

1. Yes  
2. No

**jobtenyr \[Job tenure year\]**  
**Universe**: IF (ff\_country is not 2 OR (ff\_country \= 2 AND welsh is not 1)) AND (sempderived \= 1, 3\) AND (ff\_intwave7 \= 0 OR empchk \= 2\) // Ask if respondent not living in Wales or living in Wales and did not complete survey in Welsh, and employed now, and either not full respondent in January 2021 survey or changed main employer.  
**Source:** UKHLS covid-19 survey  
**Scripting note:** Dropdown list of years from 2021 to 1950 (most recent at the top of the list).  
**Text:** In what **year** did you first start working for your current employer?  
If you currently have more than one employer, please tell us about the employer at your main job.   
\[Dropdown\] Year  

**jobtenmnth \[Job tenure month\]**  
**Universe**: IF (ff\_country is not 2 OR (ff\_country \= 2 AND welsh is not 1)) AND (sempderived \= 1, 3\) AND (ff\_intwave7 \= 0 OR empchk \= 2\) AND jobtenyr \> 2016 // Ask if respondent not living in Wales or living in Wales and did not complete survey in Welsh, and employed now, and either not full respondent in January 2021 survey or changed main employer, and started working with current employer since the start of 2017\.  
**Source:** UKHLS covid-19 survey  
**Scripting note:** Dropdown list of months.  
**Text:** In what **month** in {jobtenyr} did you first start working for your current employer?  
If you currently have more than one employer, please tell us about the employer at your main job.   
\[Dropdown\] Month  

**jobtenyrdk \[Job tenure year not known\]**  
**Universe**: IF (ff\_country is not 2 OR (ff\_country \= 2 AND welsh is not 1)) AND (sempderived \= 1, 3\) AND (ff\_intwave7 \= 0 OR empchk \= 2\) AND jobtenyr \= DK // Ask if respondent not living in Wales or living in Wales and did not complete survey in Welsh, and employed now and either not full respondent in January 2021 survey or changed main employer**,** and the respondent did not know the year they started working for this employer.  
**Source:** UKHLS covid-19 survey  
**Text:** Did you first start working for your current employer…

1. Within the last year (since 1 February 2020\)  
2. More than a year, but less than 3 years ago (1 February 2017 to 31 January 2020\)  
3. More than 3 years ago (before 1 February 2017\)

**indchk \[Still working in same industry\]**  
**Universe:** IF (ff\_country is not 2 OR (ff\_country \= 2 AND welsh is not 1)) AND (sempderived \= 1, 2, 3\) AND (ff\_intwave7 \= 1\) // Ask if respondent not living in Wales or living in Wales and did not complete survey in Welsh, and employed or self-employed now and full respondent in January 2021 survey.  
**Source:** UKHLS covid-19 survey  
**Text:** Do you work in the same industry as the last time you completed this survey on {ff\_intd} {ff\_intm} {ff\_inty}?

1. Yes  
2. No

**jbindustry \[Industry main activity\]**  
**Universe:**  IF (ff\_country is not 2 OR (ff\_country \= 2 AND welsh is not 1)) AND   
 (sempderived \= 1, 2, 3\) AND (ff\_intwave7 \= 0 OR indchk \= 2\) // Ask if respondent not living in Wales or living in Wales and did not complete survey in Welsh and respondent is employed, self-employed, or both, and either not full respondent in January 2021 survey or changed industry.    
**Source:**  UKHLS covid-19 survey  
**Scripting note:** Add info buttons with explanation for each category.  
Agriculture, Forestry and Fishing info button to show: This includes crop and animal production, hunting and related service activities, forestry and logging, and fishing and aquaculture.  
Mining and Quarrying info button to show: This includes mining of coal, lignite, or metal ores, extraction of crude petroleum and natural gas and mining support service activities.   
Manufacturing info button to show: This includes, but is not limited to, the manufacture of furniture, machinery, electronics, metals, mineral products, paper, wood, textiles, clothing, food and drink, tobacco and the reproduction of media.   
Electricity, Gas, Steam and Air Conditioning Supply info button to show: This group includes the generation and distribution of bulk electric power, the manufacture and distribution of natural or synthetic gas through a system of mains, and the production, collection and distribution of steam, hot water and cooled air. This also covers gas marketers and brokers.  
Water Supply; Sewerage, Waste Management and Remediation Activities info button to show: This includes water collection, water treatment and water supply, waste collection, waste treatment and waste disposal activities, remediation activities and other waste management services.  
Construction info button to show: This includes the construction of buildings, civil engineering works and specialised construction activities such as electrical installation and plumbing.   
Wholesale and Retail Trade info button to show: This includes, but is not limited to, the wholesale and retail sale of products such as motor vehicles and motorcycles, clothing, textiles, food and drink, homewares, pet products.   
Repair of Motor Vehicles and Motorcycles info button to show: This includes the maintenance and repair of motor vehicles and motorcycles and the sale of motor parts and accessories.   
Transportation and Storage info button to show: This includes land transport and transport via pipelines, e.g. passenger rail and freight rail services, water transport, air transport, postal and courier activities, and warehousing and storage facilities.  
Accommodation and Food Service Activities info button to show: This includes hotels and short-stay accommodation, camping sites, restaurants and take-away food outlets, licensed clubs, public houses and bars.   
Information and Communication info button to show: This includes publishing activities, the production of motion pictures, video and television programmes, sound recording and music publishing, radio and television broadcasting, computer programming and consultancy and data processing and hosting.   
Financial and Insurance Activities info button to show: This includes the activities of obtaining and redistributing funds other than for the purpose of insurance or pension funding or compulsory social security through banks and building societies, financial leasing, asset management and credit granting   
Real Estate Activities info button to show: This includes the buying and selling of real estate, renting and operating of owned or leased real estate, and real estate activities on a fee or contract basis.   
Professional, Scientific and Technical Activities info button to show: This includes, but is not limited, to legal activities, accounting, auditing and tax consultancy, architectural and engineering activities, scientific research and development, advertising and market research and veterinary services.     
Administrative and Support Service Activities info button to show: This includes office administrative work, employment services (e.g. recruitment, casting), cleaning services, landscaping services, security and investigation activities, travel agency and tour operator services and rental and leasing activities.   
Public Administration and Defence; Compulsory Social Security info button to show: This includes general public administration activities, regulation of health care, education, cultural services and other social services, and the provision of services to the community relating to foreign affairs, defence activities, justice and judicial activities, public order and safety, fire services and social security services.   
Education info button to show: This includes pre-primary education, primary education, secondary education, higher education, and other education such as sports and recreation and driving school activities. This also covers educational support activities.   
Human Health and Social Work Activities info button to show: This includes hospital services, medical and dental practice services, all forms of residential care services, child day-care services and social work with the elderly and disabled.   
Arts, Entertainment and Recreation info button to show: This includes creative, arts and entertainment activities, libraries, archives, museums and cultural activities (e.g. botanical gardens), gambling and betting services, sports facilities and activities and amusement parks.   
Other Service Activities info button to show: This includes trade unions, religious organisations and political organisations, the repair of computers and personal and household goods, and other personal services such as hairdressing and beauty, physical well-being and funeral services.   
Activities of Households as Employers info button to show: This includes the activities of households as employers of domestic personnel such as live-in staff, cooks, hospitality staff, valets, butlers, gardeners, gatekeepers, caretakers, babysitters, tutors, secretaries etc.

**Text:** In which industry do you currently work? If you work in more than one industry, please tell us about the **main industry**, that normally provided the largest share of your earnings.  

1. Agriculture, Forestry and Fishing  
2. Mining and Quarrying  
3. Manufacturing  
4. Electricity, Gas, Steam and Air Conditioning Supply  
5. Water Supply; Sewerage, Waste Management and Remediation Activities  
6. Construction  
7. Wholesale and Retail Trade   
8. Repair of Motor Vehicles and Motorcycles  
9. Transportation and Storage  
10. Accommodation and Food Service Activities  
11. Information and Communication  
12. Financial and Insurance Activities  
13. Real Estate Activities  
14. Professional, Scientific and Technical Activities  
15. Administrative and Support Service Activities  
16. Public Administration and Defence; Compulsory Social Security  
17. Education  
18. Human Health and Social Work Activities  
19. Arts, Entertainment and Recreation  
20. Other Service Activities  
21. Activities of Households as Employers

**indtenyr \[Industry tenure year\]**  
**Universe:**  IF (ff\_country is not 2 OR (ff\_country \= 2 AND welsh is not 1)) AND  (sempderived \= 1, 2, 3\) AND (ff\_intwave7 \= 0 OR indchk \= 2\) // Ask if respondent not living in Wales or living in Wales and did not complete survey in Welsh and respondent is employed, self-employed, or both, and either not full respondent in January 2021 survey or changed industry.    
**Source:**  UKHLS covid-19 survey  
**Scripting note:** Dropdown list of years from 2021 to 1950 (most recent at the top of the list).  
**Text:** In what **year** did you first start working in this industry?   
\[Dropdown\] Year  

**indtenmnth \[Industry tenure month\]**  
**Universe**: IF (ff\_country is not 2 OR (ff\_country \= 2 AND welsh is not 1)) AND (sempderived \= 1, 2, 3\) AND (ff\_intwave7 \= 0 OR indchk \= 2\) AND indtenyr \> 2016 // Ask if respondent not living in Wales or living in Wales and did not complete survey in Welsh, and employed or self-employed now, and either not full respondent in January 2021 survey or changed industry, and started working in the current industry since the start of 2017\.  
**Source:** UKHLS covid-19 survey  
**Scripting note:** Dropdown list of months.  
**Text:** In what **month** in {indtenyr} did you first start working in your current industry?  
\[Dropdown\] Month  

**indtenyrdk \[Industry tenure year not known\]**  
**Universe**: IF (ff\_country is not 2 OR (ff\_country \= 2 AND welsh is not 1)) AND (sempderived \= 1, 2, 3\) AND (ff\_intwave \= 0 OR indchk \= 2\) AND indtenyr \= DK // Ask if respondent not living in Wales or living in Wales and did not complete survey in Welsh, and employed or self-employed now and either not full respondent in January 2021 survey or changed industry, and the respondent did not know the year they started working in their current industry.  
**Source:** UKHLS covid-19 survey  
**Text:** Did you first start working in your current industry…

1. Within the last year (since 1 February 2020\)  
2. More than a year, but less than 3 years ago (1 February 2017 to 31 January 2020\)  
3. More than 3 years ago (before 1 February 2017\)  
   

**occhk \[Still same occupation\]**  
**Universe:** IF (ff\_country is not 2 OR (ff\_country \= 2 AND welsh is not 1)) AND (sempderived \= 1, 2, 3\) AND (ff\_intwave7 \= 1\) // Ask if respondent not living in Wales or living in Wales and did not complete survey in Welsh, and employed or self-employed now and full respondent in January 2021 survey.  
**Source:** UKHLS covid-19 survey  
**Text:** Whether or not you are with the same employer, do you have the same job title as when you completed this survey on {ff\_intd} {ff\_intm} {ff\_inty}?

1. Yes  
2. No

**jbsoc \[Job title and description\]**  
**Universe:**  IF (ff\_country is not 2 OR (ff\_country \= 2 AND welsh is not 1)) AND sempderived \= 1, 2, 3 AND (ff\_intwave7 \= 0 OR occhk \= 2\) // Ask if respondent not living in Wales or living in Wales and did not complete survey in Welsh and respondent is employed, self-employed, or both and not full respondent in January 2021 survey or changed job title.    
**Source:**  UKHLS  
**Soft check:** If less than 40 characters entered.  
**Soft check text: “**That is a short answer. Please record as much detail as possible.”  
**Text:** What was your main job last week? Please provide the exact job title and describe fully the sort of work you do. If you have more than one job, please describe the job that is the highest paid. If equal earnings then describe the job that is the most hours.  
\[Textbox\]

**occtenyr \[Occupation tenure year\]**  
**Universe:**  IF (ff\_country is not 2 OR (ff\_country \= 2 AND welsh is not 1)) AND   
(sempderived \= 1, 2, 3\) AND (ff\_intwave7 \= 0 OR occhk \= 2\) // Ask if respondent not living in Wales or living in Wales and did not complete survey in Welsh and respondent is employed, self-employed, or both and either not full respondent in January 2021 survey or changed job title.    
**Source:**  UKHLS covid-19 survey  
**Scripting note:** Dropdown list of years from 2021 to 1950 (most recent at the top of the list).  
**Text:** In what **year** did you start working in this role (including with previous employers)? If you have been promoted or changed grades, please give the date of that change.   
\[Dropdown\] Year  

**occtenmnth \[Occupation tenure month\]**  
**Universe**: IF (ff\_country is not 2 OR (ff\_country \= 2 AND welsh is not 1)) AND (sempderived \= 1, 2, 3\) AND (ff\_intwave7 \= 0 OR occhk \= 2\) AND occtenyr \> 2016 // Ask if respondent not living in Wales or living in Wales and did not complete survey in Welsh, and employed or self-employed now, and either not full respondent in January 2021 survey or changed job title, and started working in the current role since the start of 2017\.   
**Source:** UKHLS covid-19 survey  
**Scripting note:** Dropdown list of months.  
**Text:** In what **month** in {occtenyr} did you first start working in your role?  
\[Dropdown\] Month  

**occtenyrdk \[Occupation tenure year not known\]**  
**Universe**: IF (ff\_country is not 2 OR (ff\_country \= 2 AND welsh is not 1)) AND (sempderived \= 1, 2, 3\) AND (ff\_intwave7 \= 0 OR occhk \= 2\) AND occtenyr \= DK // Ask if respondent not living in Wales or living in Wales and did not complete survey in Welsh, and employed or self-employed now, and either not full respondent in January 2021 survey or changed job title, and the respondent did not know the year they started their current role.  
**Source:** UKHLS covid-19 survey  
**Text:** Did you first start working in your current role?

1. Within the last year (since 1 February 2020\)  
2. More than a year, but less than 3 years ago (1 February 2017 to 31 January 2020\)  
3. More than 3 years ago (before 1 February 2017\)  
   

**jbmngr \[Managerial duties: current job\]**  
**Universe:**  IF (ff\_country is not 2 OR (ff\_country \= 2 AND welsh is not 1)) AND   
 (sempderived \= 1, 2, 3\) AND (ff\_intwave7 \= 0 OR occhk \= 2\) // Ask if respondent not living in Wales or living in Wales and did not complete survey in Welsh and respondent is employed, self-employed, or both, and either not full respondent in January 2021 survey or changed job title.    
**Source:**  UKHLS  
**Scripting note:** Help text: This question is asking about management responsibilities over other people (i.e. work colleagues) either directly, or through supervisors.  
**Text:** Do you have any managerial duties or do you supervise any other employees?

1. Manager   
2. Foreman/supervisor  
3. NOT manager or supervisor

**jbsize \[No employed at current workplace\]**  
**Universe:**  IF (ff\_country is not 2 OR (ff\_country \= 2 AND welsh is not 1)) AND (sempderived \= 1, 2, 3\) AND (ff\_intwave7 \= 0 OR occhk \= 2\) // Ask if respondent not living in Wales or living in Wales and did not complete survey in Welsh and respondent is employed, self-employed, or both, and either not full respondent in January 2021 survey or changed job title.    
**Source:**  UKHLS  
**Scripting note:** Help text: This is the total number of employees at the workplace, not just the number employed within the particular section or department in which you work.  
\*If you work from a depot or office (e.g. a service engineer), base the answer on the number of people who work from that depot.  
\*If you are employed by an employment agency, please answer these questions with reference to the place at which you are currently working (or last worked) rather than the agency.  
\*If you have worked in more than one workplace in the course of a week, please refer to the place where you worked the most hours.  
\*People working for sub-contractors or merchandisers within a larger workplace should answer with reference to the larger workplace (for example, school meals staff should answer with respect to the school rather than the kitchens, and people working on a fish stall franchise within a supermarket should answer with respect to the supermarket).  
**Text:** How many people are employed at the place where you work?

1. 1-2  
2. 3-9  
3. 10-24  
4. 25-49  
5. 50-99  
6. 100-199  
7. 200-499  
8. 500-999  
9. 1000 or more  
10. Don’t know but fewer than 25  
11. Don’t know but 25 or more  

**hours \[Hours worked\]**  
**Universe**: IF sempderived= 1, 2, 3 // Ask if currently in paid work or self-employed.  
**Source:** UKHLS covid-19 survey  
**Scripting notes:** Range \[0 – 168\]. Allow one decimal.  
**Text:** How many hours did you work, as an employee or self-employed, last week? Please include all jobs and self-employment activities. If you didn’t work any hours in your job(s), please enter zero.  
\[Numeric textbox\] Hours  
**hrschange1 \[Hours, employees\]**  
**Universe**: IF (ff\_prevsurv \= 1 AND sempderived \= 1  AND (hours+1) \< ff\_hours AND hours is not DK/REF/MIS AND ff\_hours is not \-9, \-2, \-1) OR (ff\_prevsurv \= 1 AND ff\_sempderived \= 1 AND sempderived \= 4)) // Ask if completed a previous monthly survey, and is currently in paid work, and hours reported now plus one are less than hours in previous survey, and hours are not missing, and previous hours are not missing. Or if completed a previous monthly survey and was previously in work and is now neither in work nor self-employed.    
**Source:** UKHLS covid-19 survey  
**Scripting notes**: Numbering is deliberately not sequential (to match April 2020 version). Present response options in the order listed below, not in the order of the numbering.   
**Text:** Your answers suggest that you are working fewer hours than when you last completed this survey on {ff\_intd} {ff\_intm} {ff\_inty}. Can you tell us why?  
*Please select all that apply.*

12. Normal or expected variation  
1. Laid off by employer with certain recall date  
2. Laid off or made redundant by employer with some prospect of recall  
3. Permanently laid off or made redundant by employer/employer ceased trading/contract ended  
4. Employer cut hours/reduced tasks  
5. Have been put on furlough or paid leave 

16\. On Job Support Scheme 

6. Using annual leave

13\. Quit job/changed employer or job  
7\.  Self-isolating or sick leave with company sick pay  
8\. Self-isolating or sick leave with statutory sick pay  
9\. Self-isolating or sick leave without sick pay  
14\. Avoiding risk of becoming sick

10. Caring for children or others/Parental Leave

15\. Bereavement  
11\. Other reasons

**hrschange2 \[Hours, self-employed\]**  
**Universe**: IF (ff\_prevsurv \= 1 AND sempderived \= 2  AND (hours+1) \< ff\_hours AND hours is not DK/REF/MIS AND ff\_hours is not \-9, \-2, \-1) OR (ff\_prevsurv \= 1 AND ff\_sempderived \= 2 AND sempderived \= 4)) // Ask if completed a previous monthly survey, and is currently self-employed, and hours reported now plus one are less than hours in previous survey, and hours are not missing, and previous hours are not missing. Or if completed a previous monthly survey and was previously self-employed and is now neither in work nor self-employed.    
**Source:** UKHLS covid-19 survey  
**Scripting notes**: Numbering is deliberately not sequential (to match April 2020 version). Present response options in the order listed below, not in the order of the numbering.   
**Text:** Your answers suggest that you are working fewer hours than when you last completed this survey on {ff\_intd} {ff\_intm} {ff\_inty}. Can you tell us why?  
*Please select all that apply.*  
8\. Normal or expected variation

1. My business is directly affected by regulations on opening or travelling or other new regulations related to Coronavirus  
2. My business is directly affected by a shortage of supplies that I need for my business  
3. My business is directly affected by reduced demand for my services or products  
4. Illness  
5. Self-isolating 

9\. Avoiding risk of becoming sick

6. Caring for children or others

10\. Bereavement  
7\. Other reasons

**hrschange3 \[Hours, employed & self-employed\]**  
**Universe**: IF (ff\_prevsurv \= 1 AND (sempderived \= 3  AND (hours+1) \< ff\_hours AND hours is not DK/REF/MIS AND ff\_hours is not \-9, \-2, \-1) OR (ff\_sempderived \= 3 AND sempderived \= 4)) // Ask if completed a previous monthly survey, and is currently in work and self-employed, and hours reported now plus one are less than hours in previous survey, and hours are not missing, and previous hours are not missing. Or if completed a previous monthly survey and was previously in work and self-employed and is now neither in work nor self-employed.    
**Source:** UKHLS covid-19 survey  
**Scripting notes**: Numbering is deliberately not sequential (to match April 2020 version). Present response options in the order listed below, not in the order of the numbering.   
**Text:** Your answers suggest that you are working fewer hours than when you last completed this survey on {ff\_intd} {ff\_intm} {ff\_inty}. Can you tell us why?  
*Please select all that apply.*  
15\. Normal or expected variation

1. Laid off by employer with certain recall date  
2. Laid off or made redundant by employer with some prospect of recall  
3. Permanently laid off or made redundant by employer/employer ceased trading/contract ended  
4. Employer cut hours/reduced tasks  
5. Have been put on furlough or paid leave 

19\. On Job Support Scheme

6. Using annual leave

16\. Quit job/changed employer or job  
7\. My business is directly affected by regulations on opening or travelling or other new regulations related to Coronavirus  
8\. My business is directly affected by a shortage of supplies that I need for my business  
9\. My business is directly affected by reduced demand for my services or products

10. Self-isolating or sick leave with company sick pay  
11. Self-isolating or sick leave with statutory sick pay  
12. Self-isolating or sick leave without sick pay

17\. Avoiding risk of becoming sick

13. Caring for children or others/parental Leave

18\. Bereavement  
14\. Other reasons

**hrschangeup1 \[Increased hours\]**  
**Universe**: IF (ff\_country is not 2 OR (ff\_country \= 2 AND welsh is not 1)) AND    
((ff\_prevsurv \= 0 AND blwork \= 1, 2, 3 AND (hours \- 1\) \> blhours AND hours is not DK/REF AND blhours is not DK/REF)   
OR (ff\_prevsurv \= 0 AND blwork \= 4 AND sempderived \= 1, 2, 3\)     
OR (ff\_prevsurv \= 1 AND sempderived \= 1, 2, 3 AND (hours \- 1\) \> ff\_hours AND hours is not DK/REF/MIS AND ff\_hours is not \-9, \-2, \-1)   
OR (ff\_prevsurv \= 1 AND ff\_sempderived \= 4 AND sempderived \= 1, 2, 3))) // Ask if respondent not living in Wales or living in Wales and did not complete survey in Welsh and   
not completed any previous monthly covid-19 survey, and in paid work or self-employed in Jan/Feb 2020, and hours worked last week minus one are more than hours worked in Jan/Feb, and hours and blhours are not missing due to refusal or don’t know answers. Or if not completed any previous survey, and in not in paid work or self-employed in Jan/Feb 2020 and currently in work or self-employed. Or if completed a previous monthly survey, and is currently in paid work or self-employed, and hours reported now minus one are more than hours in previous survey, and hours are not missing, and previous hours are not missing. Or if completed a previous monthly survey and was previously not in work or self-employed and is now either in work or self-employed.    
**Source:** UKHLS covid-19 survey  
**Text:** Your answers suggest that you are working more hours than {IF ff\_prevsurv \= 0: earlier in the year. / IF ff\_prevsurv \= 1: when you last completed this survey on {ff\_intd} {ff\_intm} {ff\_inty}.} Can you tell us why?  
*Please select all that apply.*

1. Normal or expected variation  
2. Returned to the same employer from furlough   
3. Returned to the same employer from self-isolation or sick leave  
4. Returned to the same employer from leave (other than furlough, self-isolation or sick leave)  
5. Reduction in caring duties for children or others  
6. Employer increased hours/tasks or changed role with same employer  
7. Changed employer or started new job  
8. Started self-employment business  
9. I am self-employed and government restrictions related to coronavirus have been relaxed  
10. I am self-employed and demand for my business has increased   
11. I am self-employed and the availability of supplies has increased  
12. I am self-employed and I am returning from self-isolation or illness  
13. Other reasons

**newfurlough \[**Currently Furloughed under the Coronavirus Job Retention Scheme**\]**  
**Universe**: IF sempderived \= 1, 3 AND (ff\_country is not 2 OR (ff\_country \= 2 AND welsh is not 1)) // Ask if respondent is currently in paid work, and not living in Wales or living in Wales and did not complete survey in Welsh.   
**Source:** UKHLS covid-19 survey   
**Text**: Are you currently furloughed under the Coronavirus Job Retention Scheme? 

1. Yes   
2. No 

**supprob6 \[Probability of wage support, 6 months\]**   
**Universe**: IF (ff\_country is not 2 OR (ff\_country \= 2 AND welsh is not 1)) AND (surveymonth \= March 2021\) // Ask if respondent not living in Wales or living in Wales and did not complete survey in Welsh, and survey month is March 2021\.  
**Source:** UKHLS covid-19 survey  
**Scripting notes**: Range \[0 \- 100\].  
**Text:** On a scale of 0-100%, what is the chance that the government will be supporting wages of private sector workers, either directly or through payments to employers, in 6 months' time **(i.e. at the end of September 2021\)**?* *We would like to know what you think, even if you have not been receiving government support through a program like the Job Retention (“Furlough”) Scheme or the Job Support Scheme.   
\[Numeric textbox\] %

**sempgovt3a \[Government support for self-employed, round 2\]**  
**Universe**: IF (ff\_prevsurv \= 0 AND blwork \= 2, 3\) OR (ff\_prevsurv \= 1 AND ff\_blwork \= 2, 3\) AND (ff\_intwave7 \= 0\) // Ask if was self-employed in Jan/Feb 2020 and not full respondent in January 2021 survey.  
**Source:** UKHLS covid-19 survey  
**Text:** Did you receive government support for the self-employed in the 2nd round (available from 14 July to the end of October 2020)?

1. Yes  
2. No

**sempgovt3b \[Government support for self-employed, round 3\]**  
**Universe**: IF (ff\_prevsurv \= 0 AND blwork \= 2, 3\) OR (ff\_prevsurv \= 1 AND ff\_blwork \= 2, 3\) AND ff\_sempgovt3b is not 1 // Ask if was self-employed in Jan/Feb 2020, and has not previously reported receiving support for the self-employed in the third round.  
**Source:** UKHLS covid-19 survey  
**Text:** Have you received government support for the self-employed in the third round (from 1 November 2020)?

1. Yes  
2. No  
   

**netpay\_amount \[Current earnings amount\]**  
**Universe**: IF sempderived \= 1, 2, 3 // Ask if currently in paid work or self-employment.     
**Source:** UKHLS covid-19 survey  
**Scripting notes:** Range \[0 – 1,000,000\].  
**Text:** What is your usual **take-home** **pay/earnings** now? Take-home pay is after tax, National Insurance and pension contributions have been deducted. Please include all jobs and self-employment activities.    
\[Numeric textbox\] Pounds

**netpay\_period \[Current earnings period\]**  
**Universe**: IF sempderived \= 1, 2, 3 // Ask if currently in paid work or self-employment.     
**Source:** UKHLS covid-19 survey  
**Scripting notes:** Display on same page as netpay\_amount.  
**Text:** Per 

1. Week  
2. Two weeks  
3. Month  
4. Year

**netpayweek \[Current earnings, derived weekly\]**  
**Note:** variable not released.   
**Universe**: IF sempderived \= 1, 2, 3 AND netpay\_amount is not DK, REF, MIS AND netpay\_period is not DK, REF, MIS // Ask if currently in paid work or self-employment, and reported net pay and pay period.     
**Source:** UKHLS covid-19 survey  
**DERIVED:**    
\= netpay\_amount: IF netpay\_period \= 1  
\= netpay\_amount/2: IF netpay\_period \= 2  
\= netpay\_amount/4.33: IF netpay\_period \= 3  
\= netpay\_amount/52.14: IF netpay\_period \= 4  
**grosspay\_amount \[Current gross earnings amount\]**  
**Universe**: IF sempderived \= 1, 2, 3 // Ask if currently in paid work or self-employment.     
**Source:** UKHLS covid-19 survey  
**Scripting notes:** Range \[0 – 1,000,000\].  
**Text:** Would you also be able to tell us your **gross** pay/earnings now? Gross pay is **before** tax, National Insurance and pension contributions have been deducted. Again, please include all jobs and self-employment activities.    
\[Numeric textbox\] Pounds

**grosspay\_period \[Current gross earnings period\]**  
**Universe**: IF sempderived \= 1, 2, 3 // Ask if currently in paid work or self-employment.     
**Source:** UKHLS covid-19 survey  
**Scripting notes:** Display on same page as grosspay\_amount.  
**Text:** Per 

1. Week  
2. Two weeks  
3. Month  
4. Year

**grosspayweek \[Current gross earnings, derived weekly\]**  
**Note:** variable not released.   
**Universe**: IF sempderived \= 1, 2, 3 AND grosspay\_amount is not DK, REF, MIS AND grosspay\_period is not DK, REF, MIS // Ask if currently in paid work or self-employment, and reported gross pay and pay period.     
**Source:** UKHLS covid-19 survey  
**DERIVED:**    
\= grosspay\_amount: IF grosspay\_period \= 1  
\= grosspay\_amount/2: IF grosspay\_period \= 2  
\= grosspay\_amount/4.33: IF grosspay\_period \= 3  
\= grosspay\_amount/52.14: IF grosspay\_period \= 4

**hhearners \[Current household earners\]**  
**Universe**: IF hhcompc \> 0 OR hhcompd \> 0 OR hhcompe \> 0 // Ask if living with others aged 16-18, 19-69, or 70+.      
**Source:** UKHLS covid-19 survey  
**Text:** Thinking about the other people living with you at the moment, are any of them employed or self-employed (even if they did not do any paid work last week)? 

1. Yes  
2. No

**hhearn\_amount \[Current household earnings amount\]**  
**Universe**: IF (hhcompc \> 0 OR hhcompd \> 0 OR hhcompe \> 0\) AND hhearners \= 1 // Ask if living with others aged 16-18, 19-69, or 70+, and at least one other earner in household.  
**Source:** UKHLS covid-19 survey  
**Scripting notes:** Range \[0 – 2,500,000\].   
**Soft check:** IF (hhearn\_period \= 1 AND hhearn\_amount \< netpayweek) OR (hhearn\_period \= 2 AND hhearn\_amount/2 \< netpayweek) OR (hhearn\_period \= 3 AND hhearn\_amount/4.33 \< netpayweek) OR (hhearn\_period \= 4 AND hhearn\_amount/52.14 \< netpayweek) // Household earnings converted to weekly amount are less than weekly net pay.   
**Soft check text:** “Your household earnings are lower than your net pay.”  
**Text:** Thinking about everyone living with you at the moment, what is the **total take-home** **pay/earnings** of your household now? Please only include earnings from paid work or self-employment. If you are not sure, please tell us an approximate amount.   
\[Numeric textbox\] Pounds

**hhearn\_period \[Current household earnings period\]**  
**Universe**: IF (hhcompc \> 0 OR hhcompd \> 0 OR hhcompe \> 0\) AND hhearners \= 1 // Ask if living with others aged 16-18, 19-69, or 70+, and at least one other earner in household.  
**Source:** UKHLS covid-19 survey  
**Scripting notes:** Display on same page as hhearn\_amount.   
**Text:** Per 

1. Week  
2. Two weeks  
3. Month  
4. Year

**hhearnweek \[Household earnings, derived weekly\]**  
**Note:** variable not released.   
**Universe**: IF (hhcompc \> 0 OR hhcompd \> 0 OR hhcompe \> 0\) AND hhearners \= 1 AND hhearn\_amount is not DK, REF, MIS AND hhearn\_period is not DK, REF, MIS // Ask if living with others aged 16-18, 19-69, or 70+, and at least one other earner in household, and reported household earnings and earnings period.  
**Source:** UKHLS covid-19 survey  
**DERIVED:**    
\= hhearn\_amount: IF hhearn\_period \= 1  
\= hhearn\_amount/2: IF hhearn\_period \= 2  
\= hhearn\_amount/4.33: IF hhearn\_period \= 3  
\= hhearn\_amount/52.14: IF hhearn\_period \= 4

**hhincome\_amount \[Current household income amount\]**  
**Universe**: Ask all.   
**Source:** UKHLS covid-19 survey  
**Scripting notes:** Range \[0 – 2,500,000\].   
**Soft check:** IF (hhincome\_period \= 1 AND hhincome\_amount \< hhearnweek) OR (hhincome\_period \= 2 AND hhincome\_amount/2 \< hhearnweek) OR (hhincome\_period \= 3 AND hhincome\_amount/4.33 \< hhearnweek) OR (hhincome\_period \= 4 AND hhincome\_amount/52.14 \< hhearnweek) // Household income converted to weekly amount is less than weekly household earnings.   
**Soft check text:** “Your household income should include earnings for all household members (after tax) added with other sources of income like benefits, pensions and earnings from investments on top. Normally it would be more than household earnings.”  
**Text:** Many people have additional sources of income beyond earnings from paid work and self-employment. Thinking about everyone living with you at the moment, what is the **total take-home/after tax** **income** of your household now? Please include **all** sources of income, such as benefits, pensions and earnings from investments, as well as earnings from paid work or self-employment. If you are not sure, please tell us an approximate amount.   
\[Numeric textbox\] Pounds

**hhincome\_period \[Current household income period\]**  
**Universe**: Ask all.   
**Source:** UKHLS covid-19 survey  
**Scripting notes:** Display on same page as hhincome\_amount.   
**Text:** Per 

1. Week  
2. Two weeks  
3. Month  
4. Year

**hhincome\_bracket \[Current household income brackets\]**  
**Universe**: IF (ff\_country is not 2 OR (ff\_country \= 2 AND welsh is not 1)) AND hhincome\_amount \= 0, MIS, DK, REF OR hhincome\_period \= MIS, DK, REF // Ask if respondent not living in Wales or living in Wales and did not complete survey in Welsh, and hhincome\_amount is 0, missing, don’t know or prefer not to say, or hhincome\_period is missing, don’t know or prefer not to say.   
**Source:** UKHLS covid-19 survey  
**Text:** Would you say the **total take-home/after tax** **income** of your household is… 

1. Up to £1300 per month  
2. £1301 to £2200 per month  
3. £2201 to £3500 per month  
4. £3501 to £4800 per month  
5. £4801 or more per month

**hhincomeweek \[Household income, derived weekly\]**  
**Note:** variable not released.   
**Universe**: Ask All.  
**Source:** UKHLS covid-19 survey  
**DERIVED:**    
\= hhincome\_amount: IF hhincome\_period \= 1  
\= hhincome\_amount/2: IF hhincome\_period \= 2  
\= hhincome\_amount/4.33: IF hhincome\_period \= 3  
\= hhincome\_amount/52.14: IF hhincome\_period \= 4

**ghhincome\_amount \[Gross current household income amount\]**  
**Universe**: IF (ff\_country is not 2 OR (ff\_country \= 2 AND welsh is not 1)) // Ask if respondent not living in Wales or living in Wales and did not complete survey in Welsh.  
**Source:** UKHLS covid-19 survey  
**Scripting notes:** Range \[0 – 2,500,000\].   
**Soft check:** IF (ghhincome\_period \= 1 AND ghhincome\_amount \< hhincomeweek) OR (ghhincome\_period \= 2 AND ghhincome\_amount/2 \< hhincomeweek) OR (ghhincome\_period \= 3 AND ghhincome\_amount/4.33 \< hhincomeweek) OR (ghhincome\_period \= 4 AND ghhincome\_amount/52.14 \< hhincomeweek) // GROSS Household income converted to weekly amount is less than weekly NET household income.   
**Soft check text:** “Your gross household income is before tax and other deductions, and so is normally greater than your take-home/after tax household income.”  
**Text:** Still thinking about everyone living with you at the moment, what is the **total** gross income of your household, that is, the total income of your household **before taxes and other deductions**? Again please include **all** sources of income, such as benefits, pensions and earnings from investments, as well as earnings from paid work or self-employment. If you are not sure, please tell us an approximate amount.   
\[Numeric textbox\] Pounds

**ghhincome\_period \[Gross current household income period\]**  
**Universe**: IF (ff\_country is not 2 OR (ff\_country \= 2 AND welsh is not 1)) // Ask if respondent not living in Wales or living in Wales and did not complete survey in Welsh.  
**Source:** UKHLS covid-19 survey  
**Scripting notes:** Display on same page as ghhincome\_amount.   
**Text:** Per 

1. Week  
2. Two weeks  
3. Month  
4. Year  
   

**ghhincome\_bracket \[Gross current household income brackets\]**  
**Universe**: IF (ff\_country is not 2 OR (ff\_country \= 2 AND welsh is not 1)) AND ghhincome\_amount \= 0, MIS, DK, REF OR ghhincome\_period \= MIS, DK, REF // Ask if respondent not living in Wales or living in Wales and did not complete survey in Welsh, and ghhincome\_amount is 0, missing, don’t know or prefer not to say, or ghhincome\_period is missing, don’t know or prefer not to say.  
**Source:** UKHLS covid-19 survey  
**Text:** Would you say the total income of your household **before taxes and other deductions** is… 

1. Up to £1700 per month  
2. £1701 to £2800 per month  
3. £2801 to £4100 per month  
4. £4101 to £6000 per month  
5. £6001 or more per month

**keyworksector \[Key work sector\]**  
**Universe**: IF sempderived \= 1, 2, 3 // Ask if currently in paid work or self-employment.  
**Source:** DfE COVID-19 Parents Childcare Survey  
**Scripting notes:** Include info buttons with government definitions of key worker roles per sector.  
Health and social care info button to show: This includes but is not limited to doctors, nurses, midwives, paramedics, social workers, care workers, and other frontline health and social care staff including volunteers; the support and specialist staff required to maintain the UK’s health and social care sector; those working as part of the health and social care supply chain, including producers and distributors of medicines and medical and personal protective equipment.   
Education and childcare info button to show: This includes childcare, support and teaching staff, social workers and those specialist education professionals who must remain active during the coronavirus response.  
Key Public Services info button to show: This includes those essential to the running of the justice system, religious staff, charities and workers delivering key frontline services, those responsible for the management of the deceased, and journalists and broadcasters who are providing public service broadcasting.  
Local and national government info button to show: This only includes those administrative occupations essential to the effective delivery of the coronavirus response, or delivering essential public services, such as the payment of benefits, including in government agencies and arms length bodies.  
Food and other necessary goods info button to show: This includes those involved in food production, processing, distribution, sale and delivery, as well as those essential to the provision of other key goods (for example hygienic and veterinary medicines).  
Public safety and national security info button to show: This includes police and support staff, Ministry of Defence civilians, contractor and armed forces personnel (those critical to the delivery of key defence and national security outputs and essential to the response to the coronavirus pandemic), fire and rescue service employees (including support staff), National Crime Agency staff, those maintaining border security, prison and probation staff and other national security roles, including those overseas.  
Transport info button to show: This includes those who will keep the air, water, road and rail passenger and freight transport modes operating during the coronavirus response, including those working on transport systems through which supply chains pass.  
Utilities, communications and financial services info button to show: This includes staff needed for essential financial services provision (including but not limited to workers in banks, building societies and financial market infrastructure), the oil, gas, electricity and water sectors (including sewerage), information technology and data infrastructure sector and primary industry supplies to continue during the coronavirus response, as well as key staff working in the civil nuclear, chemicals, telecommunications (including but not limited to network operations, field engineering, call centre staff, IT and data infrastructure, 999 and 111 critical services), postal services and delivery, payments providers and waste disposal sectors.

**Text:** Are you working as a key worker in any of the key sectors below during the current coronavirus situation?

1. Health and social care  
2. Education and childcare  
3. Key public services  
4. Local and national government   
5. Food and other necessary goods  
6. Public safety and national security  
7. Transport  
8. Utilities, communications and financial services  
9. No, I am not working as a key worker

**wah \[Working at home\]**  
**Universe**: IF sempderived \= 1, 2, 3 // Ask if currently in paid work or self-employment.  
**Source:** UKHLS covid-19 survey  
**Text:** During the last four weeks how often did you work at home? 

1. Always  
2. Often  
3. Sometimes  
4. Never

**tsempend \[Time stamp: employment module end\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time completed last question in this module

# **Travel to work module**   {#travel-to-work-module}

**Note:** the questions in this module were not translated into Welsh.   
**Universe for module:** IF ff\_country is not 2 OR (ff\_country \= 2 AND welsh \= 2\) // Ask if respondent is not living in Wales or living in Wales and completed the survey in English. 

### **Variables used for routing – from sample file**

**ff\_country** \[country of residence\] 

1. England  
2. Wales  
3. Scotland  
4. N Ireland

### **Variables used for routing – from other modules**

**welsh \[Welsh language\]** – ID check and household composition module

1. Welsh   
2. English 

**sempderived \[Employee or self-employed, derived\]** – Employment module

1. Employed  
2. Self-employed  
3. Both employed and self-employed  
4. No    
   

**hours \[Hours worked\]** – Employment module

**wah \[Working at home\]** – Employment module

1. Always  
2. Often  
3. Sometimes  
4. Never

**tsttwst \[Time stamp: travel to work module start\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time arrived at first question in this module

**wktrv\_cv \[Mode(s) of transport for journey to work\]**  
**Universe:**  IF sempderived \= 1, 2, 3 AND hours \> 0 AND wah \= 2, 3, 4 // Ask if employed or self-employed, worked last week, and did not always work from home.   
**Source**: UKHLS, question WKTRV adapted  
**Scripting notes:** Code 12 is exclusive.  
**Text:** How did you get to your place(s) of work last week {IF wah \= 4:? / IF wah \= 2, 3:, on days when you were not working from home?}  
*Please select all that apply.*

1. Drove myself by car or van   
2. Got a lift with someone from household   
3. Got a lift with someone outside the household   
4. Motorcycle/moped/scooter   
5. Taxi/minicab   
6. Bus/coach   
7. Train   
8. Underground/Metro/Tram/Light railway   
9. Cycle   
10. Walk   
11. Other  
12. I did not travel to my place of work last week  
    

**wktrvfar\_cv \[Main mode of transport to work\]**  
**Universe:**  IF sempderived \= 1, 2, 3 AND hours \> 0 AND  wah \= 2, 3, 4 AND more than one response at wktrv\_cv // Ask if employed or self-employed, worked last week, and did not always work from home, and more than one mode of transport to work.   
**Source**: UKHLS, question WKTRVFAR question wording adapted  
**Scripting notes:** List only the response options selected at wktrv\_cv.  
**Text:** Which did you use for the furthest part of your journey to work? 

1. Drove myself by car or van   
2. Got a lift with someone from household   
3. Got a lift with someone outside the household   
4. Motorcycle/moped/scooter   
5. Taxi/minicab   
6. Bus/coach   
7. Train   
8. Underground/Metro/Tram/Light railway   
9. Cycle   
10. Walk   
11. Other  
    

**tsttwend \[Time stamp: travel to work module end\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time completed last question in this module

# **Transport module**   {#transport-module}

**Note:** the questions in this module were not translated into Welsh.   
**Universe for module:** IF ff\_country is not 2 OR (ff\_country \= 2 AND welsh \= 2\) // Ask if respondent is not living in Wales or living in Wales and completed the survey in English. 

### **Variables used for routing – from sample file**

**ff\_country** \[country of residence\] 

1. England  
2. Wales  
3. Scotland  
4. N Ireland

### **Variables used for routing – from other modules**

**welsh \[Welsh language\]** – ID check and household composition module

1. Welsh   
2. English 

**tstranspst \[Time stamp: transport module start\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time arrived at first question in this module

**trcarfq\_cv \[Frequency travel by car\]**  
**Universe:**  Ask all.  
**Source:**  UKHLS, question TRCARFQ time frame and response options adapted  
**Text:** The next questions are about how you get around these days. How frequently do you travel by private car or van \- whether as a driver or passenger these days? Please count a single trip as one journey and each return trip as two. 

1. At least once a day  
2. Less than once a day but at least 3 times a week  
3. Once or twice a week  
4. Less than that or never 

**trbikefq\_cv \[Frequency using a bicycle\]**  
**Universe:**  Ask all.  
**Source:**  UKHLS, question TRBIKEFQ time frame and response options adapted  
**Text:** How frequently do you travel by bike these days? This excludes times when you may have ‘gone for a bike ride’. Please count a single trip as one journey and each return trip as two.

1. At least once a day  
2. Less than once a day but at least 3 times a week  
3. Once or twice a week  
4. Less than that or never 

**trwalkfq \[Frequency walking\]**  
**Universe:**  Ask all.  
**Source:**  UKHLS covid-19 survey   
**Text:** How frequently do you travel on foot these days? This excludes times when you may have ‘gone for a walk’. Please count a single trip as one journey and each return trip as two.

1. At least once a day  
2. Less than once a day but at least 3 times a week  
3. Once or twice a week  
4. Less than that or never 

**trbusfq\_cv \[Frequency travel by bus\]**  
**Universe:**  Ask all.  
**Source:**  UKHLS, question TRBUSFQ time frame and response options adapted  
**Text:** How frequently do you use an ordinary bus these days? Please count a single trip as one journey and each return trip as two.

1. At least once a day  
2. Less than once a day but at least 3 times a week  
3. Once or twice a week  
4. Less than that or never 

**trtrnfq\_cv \[Frequency of travel by train\]**  
**Universe:**  Ask all.  
**Source:**  UKHLS, question TRTRNFQ time frame and response options adapted  
**Text:** How frequently do you use a train, **not** including underground, tram or light rail these days? Please count a single trip as one journey and each return trip as two.

1. At least once a day  
2. Less than once a day but at least 3 times a week  
3. Once or twice a week  
4. Less than that or never 

**trtubefq \[Frequency tube\]**  
**Universe:**  Ask all.  
**Source:**  UKHLS covid-19 survey  
**Text:** How frequently do you use the underground, tram or light rail these days? This excludes other train journeys. Please count a single trip as one journey and each return trip as two. 

1. At least once a day  
2. Less than once a day but at least 3 times a week  
3. Once or twice a week  
4. Less than that or never   
   

**tstranspend \[Time stamp: transport module end\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time completed last question in this module

**Finance module**  

## **Variables used for routing – from sample file**

**ff\_country** \[country of residence\] 

1. England  
2. Wales  
3. Scotland  
4. N Ireland

**ff\_prevsurv \[Whether full respondent in a previous monthly survey\]** 

0. No   
1. Yes  
   

**ff\_ucredit** \[Receives Universal Credit\]

1. Award approved or receiving Universal Credit: IF (blbenefitsb65 \= 1 OR ucredit \= 5, 6 in any previous month OR ucredit2 \= 1, 2 in any previous month) // respondent has reported award approved or receiving Universal Credit  
2. Application in process: IF (blbenefitsb65 is not 1 AND ucredit is not 5, 6 in any previous month AND ucredit2 is not 1, 2 in any previous month AND (ucredit \= 4 in any previous month OR ucredit2 \= 3 in any previous month)) // respondent has not reported receiving Universal Credit, but has reported an application in process  

\-8. Inapplicable: IF neither code 1 nor code 2 apply

**ff\_morhol** \[Mortgage holiday\]

1. Mortgage holiday was granted: IF (morhol \= 1 in any previous month OR morhol2 \= 1 in any previous month) // mortgage holiday has been granted.  
2. Application in process: IF (morhol is not 1 in any previous month AND morhol2 is not 1 in any previous month AND (morhol \= 2 in any previous month OR morhol2 \= 3 in any previous month)) // respondent has not reported a granted mortgage holiday, but has reported an application in process

\-8. Inapplicable: IF neither code 1 nor code 2 apply

**ff\_hsownd\_cv \[House owned or rented\]**  
**Notes:** values of hsownd\_cv from the last monthly survey in which the respondent was asked this question**. That is, only over-write ff\_hsownd\_cv if the value of hsownd\_cv from the last survey completed is not \-8 “Inapplicable”.**  
\-9. Missing  
\-8. Inapplicable  
\-2. Refusal  
\-1. Don’t know

1. Owned outright    
2. Owned/being bought on mortgage    
3. Shared ownership (part-owned part-rented)    
4. Rented (social housing or from council)      
5. Rent free  
6. Rented (privately)   

97\. Other 

**ff\_credithol \[Credit holiday\]**

1. Payment holiday(s) granted: IF (credithol \= 1, 2 in any previous month) // payment holiday has been granted 

\-8. Inapplicable: IF code 1 does not apply

## **Variables used for routing – from other modules**

**hsownd\_cv \[House owned or rented\] – housing module**

1. Owned outright    
2. Owned/being bought on mortgage    
3. Shared ownership (part-owned part-rented)    
4. Rented (social housing or from council)   
5. Rent free    
6. Rented (privately) 

97\. Other 

**age \[Age – derived\]** \- ID check and household composition module

**welsh \[Welsh language\]** – ID check and household composition module

1. Welsh   
2. English 

**tsfinst \[Time stamp: finance module start\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time arrived at first question in this module

**ucreditb65 \[Universal Credit\]**  
**Universe**: IF ((ff\_prevsurv \= 0 AND blbenefitsb65 is not 1\) OR (ff\_prevsurv \= 1 AND ff\_ucredit is not 1, 2)) AND age \< 66 // Ask if not completed any previous monthly covid-19 surveys and not already receiving Universal Credit in Jan/Feb 2020, or completed previous surveys but not previously reported receiving Universal Credit and not previously reported application in process and less than state pension age.  
**Source:** UKHLS covid-19 survey, question UCREDIT adapted to ask those younger than state pension age.  
**Text:** Have you applied for Universal Credit since {IF ff\_prevsurv=0: March 1st 2020? / IF ff\_prevsurv=1: the last time you completed this survey on {ff\_intd} {ff\_intm} {ff\_inty}?}

1. No   
2. I tried, but was unable to complete the application  
3. Yes, but I am not eligible  
4. Yes, and my claim is being processed  
5. Yes, my claim has been approved and I am waiting for the first payment  
6. Yes, and I am now receiving Universal Credit

**ucredit2b65 \[Universal Credit, previous applicants\]**   
**Universe**: IF ff\_prevsurv \= 1 AND ff\_ucredit \= 2 AND age \< 66 // If completed previous monthly covid-19 surveys and reported claim being processed at previous interview and less than state pension age.   
**Source:** UKHLS covid-19 survey, question UCREDIT2 adapted to ask those younger than state pension age.  
**Text:** The last time you completed this survey on {ff\_intd} {ff\_intm} {ff\_inty}, you said you had applied for Universal Credit and that your claim was being processed. What was the outcome of your application?

1. My claim has been approved and I am waiting for the first payment  
2. I am now receiving Universal Credit  
3. My application is still being processed  
4. I was not eligible

**ucreditadvance65 \[Universal Credit Advance\]**   
**Universe**: IF ff\_prevsurv \= 1 AND age \< 66 AND ((ff\_ucredit is not 1, 2 AND ucreditb65 \= 4, 5, 6\) OR (ff\_ucredit \= 1\) OR (ff\_ucredit \= 2 AND ucredit2b65 \= 1, 2, 3)) // Ask if completed previous monthly covid-19 surveys, and less than state pension age, and has not previously reported receipt or application and reported receipt or application in current survey, or previously reported receipt, or previously reported application in process and it has been approved or is still in process.   
**Source:** UKHLS covid-19 survey.  
**Text:** Have you received an advance on Universal Credit this year?

1. Yes  
2. No.

**benefitsamt65 \[Benefits amount\]**   
**Universe**: IF age \< 66 // Ask if less than state pension age.   
**Source:** UKHLS covid-19 survey,   
**Scripting notes**: Range \[0 \- 20,000\].  
**Text:** How much in **total** are you currently receiving per month for the following benefits?   
If you are not receiving any of these, please enter “0”.   
If you are not sure of the exact amount, please enter an approximate total. 

* Universal Credit  
* Working Tax Credit  
* Child Tax Credit  
* Jobseeker’s Allowance  
* Employment and Support Allowance  
* Housing benefit

\[Numeric textbox\] Pounds per month

**transfers \[Transfers\]**  
**Universe**: Ask all.  
**Source:** UKHLS covid-19 survey  
**Text:** Have you given financial help to, or received financial help from, family or friends who do not currently live in the same house as you since {IF ff\_prevsurv \= 0: March 1st 2020? / IF ff\_prevsurv \= 1: the last time you completed this survey on {ff\_intd} {ff\_intm} {ff\_inty}?} Financial help could be in the form of money or paying for goods (for example groceries, medicines).

1. Gave financial help (money or goods you paid for)  
2. Received financial help (money or goods someone else paid for)  
3. Gave **and** received financial help (money or goods)  
4. Neither

**transfmade \[Transfers made\]**  
**Universe**: IF transfers \= 1, 3 // Ask if made financial transfers.  
**Source:** UKHLS covid-19 survey  
**Text:** Who did you **give** financial help to?  
*Please select all that apply.*

1. Adult children, including in-laws  
2. Parents or grandparents, including in-laws  
3. Siblings  
4. Former spouse or partner  
5. Friends  
6. Neighbours  
7. Someone else  
   

**transfrec \[Financial transfers received\]**  
**Universe**: IF transfers \= 2, 3 // Ask if financial transfers received.  
**Source:** UKHLS covid-19 survey  
**Text:** Who have you **received** financial help from?  
*Please select all that apply.*

1. Adult children, including in-laws  
2. Parents or grandparents, including in-laws  
3. Siblings  
4. Former spouse or partner  
5. Friends  
6. Neighbours  
7. Someone else

**transfout2 \[Amount Transfers made\]**  
**Universe**: IF transfers \= 1, 3 // Ask if made financial transfers.  
**Source:** UKHLS covid-19 survey  
**Scripting notes**: Range \[0 \- 50,000\].  
**Text:** How much in **total** have you **given** in financial help to family or friends who were not living in the same house as you since {IF ff\_prevsurv \= 0: March 1st 2020? / IF ff\_prevsurv \= 1: the last time you completed this survey on {ff\_intd} {ff\_intm} {ff\_inty}?}   
Remember that financial help could be in the form of money or paying for goods (for example groceries, medicines).   
\[Numeric textbox\] Pounds 

**transfin2 \[Amount Transfers received\]**  
**Universe**: IF transfers \= 2, 3 // Ask if financial transfers received.**Source:** UKHLS covid-19 survey  
**Scripting notes**: Range \[0 \- 50,000\].  
**Text:** How much in **total** have you **received** in financial help from family or friends who were not living in the same house as you since {IF ff\_prevsurv \= 0: March 1st 2020? / IF ff\_prevsurv \= 1: the last time you completed this survey on {ff\_intd} {ff\_intm} {ff\_inty}?}   
Remember that financial help could be in the form of money or paying for goods (for example groceries, medicines).  
\[Numeric textbox\] Pounds

**xphs\_cv \[Up to date with housing payments\]**  
**Universe**: IF ff\_hsownd\_cv is not 1 AND hsownd\_cv is not 1 // Ask if home is not owned outright.  
**Source:** UKHLS, altered version of question XPHSDB   
**Text:** Many people find it hard to keep up with their housing payments. May we ask, are you up to date with your rent/mortgage?

1. Yes  
2. No

**morhol \[Mortgage holiday\]**  
**Universe**: IF (ff\_prevsurv \= 1 AND (hsownd\_cv \= 2 OR ff\_hsownd\_cv \= 2\) AND ff\_morhol is not 1, 2\) // Ask if completed previous surveys and home owned with a mortgage and not reported that bank has granted a mortgage holiday, or that their application was under review.   
**Source:** UKHLS covid-19 survey  
**Text:** Have you asked your bank for a mortgage holiday?

1. Yes, it was granted  
2. Yes, my application is under review  
3. Yes, but it was declined  
4. No

**morhol2 \[Mortgage holiday – outcome of previous application\]**  
**Universe**: IF (ff\_prevsurv \= 1 AND ff\_morhol \= 2 ) // Ask if respondent reported in a previous monthly survey that they had applied for a mortgage holiday and it was still under review.   
**Source:** UKHLS covid-19 survey  
**Text:** You have previously told us that you applied for a mortgage holiday and that your application was under review. What is the current status of your application? 

1. It was granted  
2. It was declined  
3. My application is still under review

**morhol3 \[Mortgage holiday ended\]**  
**Universe**: IF ff\_morhol \= 1 // Ask if respondent reported in a previous monthly survey that they had received a mortgage holiday.   
**Source:** UKHLS covid-19 survey  
**Text:** You have previously told us that you applied for and received a mortgage holiday. What is the current status of your mortgage holiday? 

1. It is continuing  
2. It has ended

**mortover1 \[Mortgage overpayment\]**  
**Universe**: IF hsownd\_cv \= 2 OR ff\_hsownd\_cv \= 2 // Ask if reported in current or previous interview that owns home with a mortgage.   
**Source:** UKHLS covid-19 survey  
**Text:** Thinking back to the start of the pandemic in March 2020, have you made any overpayments on your mortgage **over the last year**? This would be amounts in addition to or in excess of your regular monthly payments.  

1. Yes  
2. No

**mortover3 \[Mortgage overpayments prior to pandemic\]**  
**Universe:** IF hsownd\_cv \= 2 OR ff\_hsownd\_cv \= 2  // Ask if reported in current or previous interview that owns home with a mortgage.  
**Text:** Did you make any overpayments on your mortgage in the year **prior** to the start of the pandemic, that is, from **March 2019 to February 2020**?

1. Yes  
2. No

**renthol \[Rent holiday or reduction\]**  
**Universe**: IF hsownd\_cv \= 4 OR hsownd\_cv \= 6 OR ff\_hsownd\_cv \= 4 OR ff\_hsownd\_cv \= 6 // Ask if home is rented.  
**Source:** UKHLS covid-19 survey  
**Text:** Do you currently have a rent holiday or reduction?

1. Yes  
2. No

**xpbills\_cv \[Up to date with bill payments\]**  
**Universe**: Ask all.  
**Source:** UKHLS, altered version of question XPHSDBA    
**Text:** Sometimes people are not able to pay every household bill when it falls due. May we ask, are you up to date with all your household bills such as electricity, gas, water rates, telephone, council tax, credit cards and other bills or are you behind with any of them?

1. Up to date with all bills  
2. Behind with some bills  
3. Behind with all bills  
   

**credithol \[Credit holiday\]**  
**Universe**: Ask all.  
**Source:** UKHLS covid-19 survey  
**Text:** Have you applied for/received a payment holiday on any credit product other than a mortgage {IF ff\_prevsurv \= 0: since March 1st 2020? / ff\_prevsurv \= 1: since the last time you completed this survey on {ff\_intd} {ff\_intm} {ff\_inty}? For example, a credit card, personal loan, car loan or payday loan.

1. Yes, payment holiday(s) granted  
2. Yes, some applications successful, others declined  
3. Yes, but application(s) declined  
4. No  
   

**creditholend \[Credit holiday ended\]**  
**Universe**: IF ff\_credithol \= 1 OR credithol \= 1, 2 // Ask if respondent has reported a credit holiday in a previous or the current survey.  
**Source:** UKHLS covid-19 survey  
**Text:** You have told us {IF ff\_credithol \= 1 AND credithol is not 1, 2: previously} that you have been granted payment holiday(s) on credit products other than mortgages. Have any of these payment holidays ended?

1. Yes  
2. No  
   

**creditholwhich \[Which credit holiday ended\]**  
**Universe**: IF (ff\_credithol \= 1 OR credithol \= 1, 2\) AND creditholend \= 1 // Ask if respondent has reported a credit holiday in a previous or the current survey, and credit holiday has ended.  
**Source:** UKHLS covid-19 survey  
**Text:** For which types of credits have your payment holiday(s) ended?  
*Please select all that apply.*

1. Credit card  
2. Personal loan  
3. Car loan  
4. Payday loan  
5. Other loans/credits  
   

**inoutflows \[Earnings loss\]**  
**Universe**: Ask all.  
**Source:** UKHLS covid-19 survey  
**Scripting notes**: Numbering is deliberately not sequential (to match April 2020 version). Present response options in the order listed below, not in the order of the numbering. Code 8 is exclusive.  
**Text:** If your household is now earning less than in January/February 2020, have you done any of the following to deal with this?    
*Please select all that apply.*

1. Reduced spending   
2. Used savings

9\. 	Accessed pension or reduced pension contribution  
3\. 	New borrowing from bank (including personal loan) or credit card  
4\. 	New borrowing from family and friends  
5\. 	Found new work/increased hours   
6\. 	Another member of my household found new work or increased hours  
10\. New or increased welfare benefits  
7\. 	Dealt with earnings loss in another way  
8\. None of these/does not apply

**save\_cv \[Any savings\]**  
**Universe**: IF ff\_country is not 2 OR (ff\_country \= 2 AND welsh is not 1\) // Ask if respondent not living in Wales, or living in Wales and did not complete survey in Welsh.  
**Source:** UKHLS, question SAVE amended time frame  
**Text:** In the last 4 weeks, have you saved any amount of your income, for example by putting some away in a bank, building society, or Post Office account, other than to meet regular bills? Please include share purchase schemes and ISAs.

1. Yes  
2. No  
   

**saved\_cv \[Savings amount\]**  
**Universe**: IF ff\_country is not 2 OR (ff\_country \= 2 AND welsh is not 1\) AND save\_cv \= 1 // Ask if respondent not living in Wales or living in Wales and did not complete survey in Welsh, and saves.  
**Source:** UKHLS, altered version of question SAVED  
**Scripting notes**: Range \[0 \- 20,000\].  
**Text:** About how much have you personally managed to save in the last 4 weeks?   
\[Numeric textbox\] Pounds

**debtnonmort \[Any non-mortgage debt\]**  
**Universe**: IF ff\_country is not 2 OR (ff\_country \= 2 AND welsh is not 1\) // Ask if respondent not living in Wales, or living in Wales and did not complete survey in Welsh.  
**Source:** UKHLS covid-19 survey 

**Text:** We would now like to ask you about any other money you may owe, **apart from mortgages**. Please include personal loans, overdrafts, credit card balances that are rolled over month-to-month, loans from a private individual or any other unsecured borrowing. Please do not include credit card and other bills being fully paid off in the current month.   
Do you currently owe any money, other than for a mortgage? 

1. Yes  
2. No

**debtamt \[Debt amount\]**  
**Universe**: IF (ff\_country is not 2 OR (ff\_country \= 2 AND welsh is not 1)) AND debtnonmort \= 1 // Ask if respondent not living in Wales, or living in Wales and did not complete survey in Welsh and has non-mortgage debt.  
**Source:** UKHLS covid-19 survey   
**Scripting notes**: Range \[0 \- 1,000,000\].   
**Text:** About how much do you currently owe in total?   
\[Numeric textbox\] Pounds

**debt2 \[Debt change\]**  
**Universe**: IF ff\_country is not 2 OR (ff\_country \= 2 AND welsh is not 1\) // Ask if respondent not living in Wales, or living in Wales and did not complete survey in Welsh.  
**Source:** UKHLS covid-19 survey  
**Scripting notes:** Help text: “If you had debt that you have paid off entirely in the last 4 weeks, please select ‘Decreased’. If you had no debt but have borrowed in the last 4 weeks, please select ‘Gone up’.”  
**Text:** In the last 4 weeks, has the amount of money you owe, if any…

1. Gone up   
2. Stayed the same  
3. Decreased   
   

**debt3 \[Amount of debt change\]**  
**Universe**: IF ff\_country is not 2 OR (ff\_country \= 2 AND welsh is not 1\) AND debt2 \= 1, 3 // Ask if respondent not living in Wales or living in Wales and did not complete survey in Welsh, and debt has gone up or decreased.  
**Source:** UKHLS covid-19 survey  
**Scripting notes**: Range\[0 \- 1,000,000\].  
**Text:** By about how much has your debt changed in the last 4 weeks?   
\[Numeric textbox\] Pounds

**spend \[Spending change\]**  
**Universe**: IF ff\_country is not 2 OR (ff\_country \= 2 AND welsh is not 1\) // Ask if respondent not living in Wales, or living in Wales and did not complete survey in Welsh.  
**Source:** UKHLS covid-19 survey  
**Text:** Thinking about your household spending (e.g. on food and household goods, products and services, on commuting, bills, etc.) but excluding housing costs (e.g. mortgage payments, rent). Over the last 4 weeks, has your household spending increased, decreased, or stayed the same relative to the same four week period last year?

1. Increased by more than a quarter (i.e. over 25%)  
2. Increased by up to a quarter (i.e. up to 25%)  
3. Stayed the same  
4. Decreased by up to a quarter (i.e. up to 25%)  
5. Decreased by more than a quarter (i.e. over 25%)  
6. Don’t know  
7. Prefer not to answer

**wchange \[Net wealth change\]**  
**Universe**: IF ff\_country is not 2 OR (ff\_country \= 2 AND welsh is not 1\) // Ask if respondent not living in Wales, or living in Wales and did not complete survey in Welsh.  
**Source:** UKHLS covid-19 survey  
**Text:** During the pandemic, some people have had to borrow or use their savings to make ends meet. Others have saved more than usual because lockdowns restricted how they could spend. We are interested in what has happened to your household’s **total net wealth**. That is, thinking about the value of any assets you may have (property including home, investments, deposit or current accounts, and other) minus any debts (mortgage, personal or car loans, credit cards and other), would you say that relative to just before the pandemic began (**January/February 2020**) the net amount has: 

1. Gone up by 10% or more  
2. Stayed about the same  
3. Gone down by 10% or more

**wchange2 \[Effect of pandemic on net wealth\]**  
**Universe**: IF ff\_country is not 2 OR (ff\_country \= 2 AND welsh is not 1\) // Ask if respondent not living in Wales, or living in Wales and did not complete survey in Welsh.  
**Source: **UKHLS** **covid-19 survey  
**Text:** Do you think your household's total net wealth is higher, lower, or about the same as it would have been today if the pandemic had not occurred?  
1.     Higher  
2.     About the same  
3.     Lower  
   
**tsfinend \[Time stamp: finance module end\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time completed last question in this module

**Financial security module**  

## **Variables used for routing – from sample file**

**ff\_country** \[country of residence\] 

1. England  
2. Wales  
3. Scotland  
4. N Ireland

**ff\_mpcalloc** \[Allocation to marginal propensity to consume questions\]

1. Personal windfall  
2. Public windfall

## **Variables used for routing – from other modules**

**welsh \[Welsh language\]** – ID check and household composition module

1. Welsh   
2. English 

**sempderived** \[Employee or self-employed, derived\] – employment module

1. Employed   
2. Self-employed  
3. Both employed and self-employed

**tsfinsecst \[Time stamp: financial security module start\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time arrived at first question in this module

**finnow \[Subjective financial situation \- current\]**     
**Universe**: Ask all.  
**Source:** BHPS, UKHLS  
**Text:** How well would you say you yourself are managing financially these days? Would you say you are...

1. Living comfortably    
2. Doing alright    
3. Just about getting by  
4. Finding it quite difficult    
5. Finding it very difficult

**finfut\_cv3 \[Subjective financial situation – 3 months future\]**     
**Universe**: Ask if surveymonth \>= November 2020 // Ask if survey month is November 2020 onwards.  
**Source:** UKHLS, question FINFUT altered from yearly to 3-monthly  
**Text:** Looking ahead, how do you think you will be financially **3 months** from now, will you be... 

1. Better off  
2. Worse off than you are now  
3. Or about the same?

**jobsec \[Job security\]**     
**Universe**: IF sempderived \= 1, 2, 3 // Ask if currently in paid work or self-employed.  
**Source:** Adapted from survey by Adams-Prassl, Boneva, Golin, and Rauh (2020)  
**Scripting notes:** Range \[0 – 100\].  
**Text:** On a scale of 0-100% how likely do you think it is that you will {IF sempderived \= 1: lose your job / IF sempderived \= 2: shut your business / IF sempderived \= 3: lose your job or shut your business} in the next three months?   
\[Numeric textbox\] %

**finsec \[Financial security\]**     
**Universe**: All // Ask all.  
**Source:** Adapted from survey by Adams-Prassl, Boneva, Golin, and Rauh (2020)  
**Scripting notes:** Range \[0 – 100\].  
**Text:** On a scale of 0-100% how likely do you think it is that you will have difficulty paying your usual bills and expenses in the next three months?   
\[Numeric textbox\] %

**mpc1 \[Marginal propensity to consume\]**     
**Universe**: IF ff\_mpcalloc \= 1 AND (ff\_country is not 2 OR (ff\_country \= 2 AND welsh is not 1)) // Ask if allocated to group 1 and respondent not living in Wales, or living in Wales and did not complete survey in Welsh.  
**Source:** Adapted from survey by Federal Reserve Bank of New York \[[https://www.minneapolisfed.org/institute/working-papers/wp18-15.pdf](https://www.minneapolisfed.org/institute/working-papers/wp18-15.pdf)\]  
**Text:** Now consider a hypothetical situation where you unexpectedly receive a one-time payment of £500 today. We would like to know whether this extra income would cause you to change your spending, borrowing and saving behaviour in any way over the next 3 months.  
If you received the one-time £500 payment: 

1. Over the next 3 months, I would spend **more** than if I hadn’t received the £500   
2. Over the next 3 months, I would spend the **same** as if I hadn’t received the £500   
3. Over the next 3 months, I would spend **less** than if I hadn’t received the £500   
   

**mpc2 \[Marginal propensity to consume amount\]**     
**Universe**: IF ff\_mpcalloc \= 1 AND (ff\_country is not 2 OR (ff\_country \= 2 AND welsh is not 1)) AND mpc1 \= 1, 3 // Ask if allocated to group 1 and respondent not living in Wales or living in Wales and did not complete survey in Welsh, and would spend more or less than before.   
**Source:** Adapted from survey by Federal Reserve Bank of New York \[[https://www.minneapolisfed.org/institute/working-papers/wp18-15.pdf](https://www.minneapolisfed.org/institute/working-papers/wp18-15.pdf)\]  
**Scripting notes:** Range \[0 \- 10000\].  
**Text:** You indicated that you would {IF mpc1 \= 1: increase / IF mpc1 \= 3: reduce} your spending/donations over the next 3 months following the receipt of the £500 payment. How much {IF mpc1 \= 1: more / IF mpc1 \= 3: less} would you spend than if you hadn’t received the £500?   
\[Numeric textbox\] Pounds

**mpc3 \[Marginal propensity to borrow and save\]**     
**Universe**: IF ff\_mpcalloc \= 1 AND (ff\_country is not 2 OR (ff\_country \= 2 AND welsh is not 1)) AND (mpc1 \= 2, 3 OR (mpc1 \= 1 AND mpc2 \< 500)) // Ask if allocated to group 1 and respondent not living in Wales or living in Wales and did not complete survey in Welsh, and would spend the same or less, or would spend more but less than £500.  
**Source:** Adapted from survey by Federal Reserve Bank of New York \[[https://www.minneapolisfed.org/institute/working-papers/wp18-15.pdf](https://www.minneapolisfed.org/institute/working-papers/wp18-15.pdf)\]  
**Text:** You have indicated that you would not spend all of the £500 payment. What would you do with the amount that you do not spend:   
*Please select all that apply.*

1. Over the next 3 months, I would **pay off more debt** (or borrow less) than if I hadn’t received the £500   
2. Over the next 3 months, I would **save more** than if I hadn’t received the £500   
3. Over the next 3 months, I would **receive less financial help** from friends or family than if I hadn’t received the £500.  
4. Over the next 3 months, I would **give more financial help** to friends or family than if I hadn’t received the £500.

**mpc1b \[Marginal propensity to consume, public windfall\]**     
**Universe**: IF ff\_mpcalloc \= 2 AND (ff\_country is not 2 OR (ff\_country \= 2 AND welsh is not 1)) // Ask if allocated to group 2 and respondent not living in Wales, or living in Wales and did not complete survey in Welsh.  
**Source:** Adapted from survey by Federal Reserve Bank of New York \[[https://www.minneapolisfed.org/institute/working-papers/wp18-15.pdf](https://www.minneapolisfed.org/institute/working-papers/wp18-15.pdf)\]  
**Text:** Now consider a hypothetical situation where the government unexpectedly gives everyone a one-time payment of £500 today. We would like to know whether this extra income would cause you to change your spending, borrowing and saving behaviour in any way over the next 3 months.

If the government gave all adults a one-time £500 payment today: 

1. Over the next 3 months, I would spend **more** than I would have without that payment.   
2. Over the next 3 months, I would spend the **same** as I would have without that payment.   
3. Over the next 3 months, I would spend **less** than if I would have without that payment.    
   

**mpc2b \[Marginal propensity to consume amount, public windfall\]**     
**Universe**: IF ff\_mpcalloc \= 2 AND (ff\_country is not 2 OR (ff\_country \= 2 AND welsh is not 1)) AND mpc1b \= 1, 3 // Ask if allocated to group 2 and respondent not living in Wales or living in Wales and did not complete survey in Welsh, and would spend more or less than before.   
**Source:** Adapted from survey by Federal Reserve Bank of New York \[[https://www.minneapolisfed.org/institute/working-papers/wp18-15.pdf](https://www.minneapolisfed.org/institute/working-papers/wp18-15.pdf)\]  
**Scripting notes:** Range \[0 \- 10000\].  
**Text:** You indicated that you would {IF mpc1b \= 1: increase / IF mpc1b \= 3: reduce} your spending/donations over the next 3 months following the receipt of the £500 payment. How much {IF mpc1b \= 1: more / IF mpc1b \= 3: less} would you spend than if the Government hadn’t issued the £500 payments?   
\[Numeric textbox\] Pounds

**mpc3b \[Marginal propensity to borrow and save, public windfall\]**     
**Universe**: IF ff\_mpcalloc \= 2 AND (ff\_country is not 2 OR (ff\_country \= 2 AND welsh is not 1)) AND (mpc1b \= 2, 3 OR (mpc1b \= 1 AND mpc2b \< 500)) // Ask if allocated to group 2 and respondent not living in Wales or living in Wales and did not complete survey in Welsh, and would spend the same or less, or would spend more but less than £500.  
**Source:** Adapted from survey by Federal Reserve Bank of New York \[[https://www.minneapolisfed.org/institute/working-papers/wp18-15.pdf](https://www.minneapolisfed.org/institute/working-papers/wp18-15.pdf)\]  
**Text:** You have indicated that you would not spend all of the £500 payment. What would you do with the amount that you do not spend:   
*Please select all that apply.*

1. Over the next 3 months, I would **pay off more debt** (or borrow less) than I would have without that payment.   
2. Over the next 3 months, I would **save more** than if I would have without that payment.   
3. Over the next 3 months, I would **receive less financial help** from friends or family than I would have without that payment.   
4. Over the next 3 months, I would **give more financial help** to friends or family than I would have without that payment. 

**tsfinsecend \[Time stamp: financial security module end\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time completed last question in this module

# **5-11 year-olds: strengths and difficulties questionnaire module** {#5-11-year-olds:-strengths-and-difficulties-questionnaire-module}

**Note:** the questions in this module were not translated into Welsh.   
**Universe for module:** IF ff\_country is not 2 OR (ff\_country \= 2 AND welsh \= 2\) // Ask if respondent is not living in Wales or living in Wales and completed the survey in English. 

## **Variables used for routing – from sample file**

**ff\_country** \[country of residence\] 

1. England  
2. Wales  
3. Scotland  
4. N Ireland

## **Variables used for routing – from other modules**

**welsh \[Welsh language\]** – ID check and household composition module

1. Welsh   
2. English 

**parent511 \[Parent of child aged 5 to 11 in household\]** – Household relationships module

**tssdqst \[Time stamp: SDQ module start\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time arrived at first question in this module

**num511 \[Number of children aged 5-11\]**    
**Universe:** If parent511 \= 1 // Ask if respondent is parent of 5-11 year old living in the household.  
**Source:** UKHLS covid-19 survey  
**Text:** How many children of your own aged between 5 and 11 are currently living with you? 

1. 1 child  
2. 2 children  
3. 3 children  
4. 4 children	  
5. 5 or more children  
6. I don’t have any children aged 5-11 currently living with me

**ch511 \[Details of 5-11 year olds\]**    
**Universe**: IF parent511 \= 1 AND num511 \= 1, 2, 3, 4, 5 // Ask if respondent is parent of 5-11 year old living in the household and number of children in that age group is reported.   
**Source:** UKHLS covid-19 survey  
**Scripting notes:** Display a grid of rows \= num511. Column headings for “First name” and “Date of birth”. Within each row a text box for name and numeric text box for date of birth. Respondents to enter date of birth with format dd/mm/yyyy rather than a date selector. Do not display DK and REF answer options, answer required. Range for ch511dob \[24/07/2008 \- 30/07/2015\].  
**Text:** {IF num511 \= 1: We would like to ask you about your child aged 5-11 who is living with you./ IF num511 \= 2, 3, 4, 5: We would like to ask you about your children aged 5-11 who are living with you.} So it’s easier to know who you are answering about, please give us the child’s first name and date of birth. {IF num511 \= 5: If you have 5 or more children, please give us the names of the eldest 5.}  
   
**ch511namea.** \[Textbox\] Name   **ch511doba.** \[Numeric textbox\] Date of birth (dd/mm/yyyy)  
**ch511nameb.** \[Textbox\] Name   **ch511dobb.** \[Numeric textbox\] Date of birth (dd/mm/yyyy)  
**ch511namec.** \[Textbox\] Name   **ch511dobc.** \[Numeric textbox\] Date of birth (dd/mm/yyyy)  
**ch511named.** \[Textbox\] Name  **ch511dobd.** \[Numeric textbox\] Date of birth (dd/mm/yyyy)  
**ch511namee.** \[Textbox\] Name   **ch511dobe.** \[Numeric textbox\] Date of birth (dd/mm/yyyy)

START LOOP.  
LOOP OVER EACH CHILD REPORTED AT CH511. 

**chsdpf\_cv \[Behaviour: considerate\]**  
**Universe**: IF parent511 \= 1 AND num511 \= 1, 2, 3, 4, 5 AND ch511namea is not missing // Ask if respondent is parent of 5-11 year old living in the household, and number of children in that age group is reported, and at least one child name is reported.   
**Source:** SDQ, Robert Goodman (2005), UKHLS, question CHSDPF with a different time frame  
**Text:** Strengths and Difficulties Questionnaire.  
We next have some questions about what {ch511name} is like. For each item, please mark the box for Not True, Somewhat True or Certainly True. It would help us if you answered all items as best you can even if you are not absolutely certain or the item seems daft\! Please give your answers on the basis of the child's behaviour over the last six months.   
{ch511name} is considerate of other people’s feelings.  

1. Not true  
2. Somewhat true  
3. Certainly true  
   

**chsdro\_cv \[Behaviour: restless\]**  
**Universe**: IF parent511 \= 1 AND num511 \= 1, 2, 3, 4, 5 AND ch511namea is not missing // Ask if respondent is parent of 5-11 year old living in the household, and number of children in that age group is reported, and at least one child name is reported.   
**Source:** SDQ, Robert Goodman (2005), UKHLS, question CHSDRO with a different time frame  
**Text:** {ch511name} is restless, overactive, cannot stay still for long.  

1. Not true  
2. Somewhat true  
3. Certainly true

**chsdhs\_cv \[Behaviour: headaches\]**  
**Universe**: IF parent511 \= 1 AND num511 \= 1, 2, 3, 4, 5 AND ch511namea is not missing // Ask if respondent is parent of 5-11 year old living in the household, and number of children in that age group is reported, and at least one child name is reported.   
**Source:** SDQ, Robert Goodman (2005), UKHLS, question CHSDHS with a different time frame  
**Text:** {ch511name} often complains of headaches, stomach-aches or sickness.  

1. Not true  
2. Somewhat true  
3. Certainly true

**chsdsr\_cv \[Behaviour: shares readily\]**  
**Universe**: IF parent511 \= 1 AND num511 \= 1, 2, 3, 4, 5 AND ch511namea is not missing // Ask if respondent is parent of 5-11 year old living in the household, and number of children in that age group is reported, and at least one child name is reported.   
**Source:** SDQ, Robert Goodman (2005), UKHLS, question CHSDSR with a different time frame  
**Text:** {ch511name} shares readily with other children (treats, toys, pencils etc.).  

1. Not true  
2. Somewhat true  
3. Certainly true

**chsdtt\_cv \[Behaviour: temper tantrums\]**  
**Universe**: IF parent511 \= 1 AND num511 \= 1, 2, 3, 4, 5 AND ch511namea is not missing // Ask if respondent is parent of 5-11 year old living in the household, and number of children in that age group is reported, and at least one child name is reported.   
**Source:** SDQ, Robert Goodman (2005), UKHLS, question CHSDTT with a different time frame  
**Text:** {ch511name} often has temper tantrums or hot tempers.  

1. Not true  
2. Somewhat true  
3. Certainly true

**chsdsp\_cv \[Behaviour: solitary\]**  
**Universe**: IF parent511 \= 1 AND num511 \= 1, 2, 3, 4, 5 AND ch511namea is not missing // Ask if respondent is parent of 5-11 year old living in the household, and number of children in that age group is reported, and at least one child name is reported.   
**Source:** SDQ, Robert Goodman (2005), UKHLS, question CHSDSP with a different time frame  
**Text:** {ch511name} is rather solitary, tends to play alone.  

1. Not true  
2. Somewhat true  
3. Certainly true

**chsdor\_cv \[Behaviour: obedient\]**  
**Universe**: IF parent511 \= 1 AND num511 \= 1, 2, 3, 4, 5 AND ch511namea is not missing // Ask if respondent is parent of 5-11 year old living in the household, and number of children in that age group is reported, and at least one child name is reported.   
**Source:** SDQ, Robert Goodman (2005), UKHLS, question CHSDOR with a different time frame  
**Text:** {ch511name} is generally obedient, usually does what adults request.  

1. Not true  
2. Somewhat true  
3. Certainly true

**chsdmw\_cv \[Behaviour: many worries\]**  
**Universe**: IF parent511 \= 1 AND num511 \= 1, 2, 3, 4, 5 AND ch511namea is not missing // Ask if respondent is parent of 5-11 year old living in the household, and number of children in that age group is reported, and at least one child name is reported.   
**Source:** SDQ, Robert Goodman (2005), UKHLS, question CHSDMW with a different time frame  
**Text:** {ch511name} has many worries, often seems worried.  

1. Not true  
2. Somewhat true  
3. Certainly true

**chsdhu\_cv \[Behaviour: helpful\]**  
**Universe**: IF parent511 \= 1 AND num511 \= 1, 2, 3, 4, 5 AND ch511namea is not missing // Ask if respondent is parent of 5-11 year old living in the household, and number of children in that age group is reported, and at least one child name is reported.   
**Source:** SDQ, Robert Goodman (2005), UKHLS, question CHSDHU with a different time frame  
**Text:** {ch511name} is helpful if someone is hurt, upset or feeling ill.  

1. Not true  
2. Somewhat true  
3. Certainly true

**chsdfs\_cv \[Behaviour: fidgeting\]**  
**Universe**: IF parent511 \= 1 AND num511 \= 1, 2, 3, 4, 5 AND ch511namea is not missing // Ask if respondent is parent of 5-11 year old living in the household, and number of children in that age group is reported, and at least one child name is reported.   
**Source:** SDQ, Robert Goodman (2005), UKHLS, question CHSDFS with a different time frame  
**Text:** {ch511name} is constantly fidgeting or squirming.  

1. Not true  
2. Somewhat true  
3. Certainly true

**chsdgf\_cv \[Behaviour: good friend\]**  
**Universe**: IF parent511 \= 1 AND num511 \= 1, 2, 3, 4, 5 AND ch511namea is not missing // Ask if respondent is parent of 5-11 year old living in the household, and number of children in that age group is reported, and at least one child name is reported.   
**Source:** SDQ, Robert Goodman (2005), UKHLS, question CHSDGF with a different time frame  
**Text:** {ch511name} has at least one good friend.  

1. Not true  
2. Somewhat true  
3. Certainly true

**chsdfb\_cv \[Behaviour: fights\]**  
**Universe**: IF parent511 \= 1 AND num511 \= 1, 2, 3, 4, 5 AND ch511namea is not missing // Ask if respondent is parent of 5-11 year old living in the household, and number of children in that age group is reported, and at least one child name is reported.   
**Source:** SDQ, Robert Goodman (2005), UKHLS, question CHSDFB with a different time frame  
**Text:** {ch511name} often fights with other children or bullies them.  

1. Not true  
2. Somewhat true  
3. Certainly true

**chsdud\_cv \[Behaviour: unhappy\]**  
**Universe**: IF parent511 \= 1 AND num511 \= 1, 2, 3, 4, 5 AND ch511namea is not missing // Ask if respondent is parent of 5-11 year old living in the household, and number of children in that age group is reported, and at least one child name is reported.   
**Source:** SDQ, Robert Goodman (2005), UKHLS, question CHSDUD with a different time frame  
**Text:** {ch511name} is often unhappy, down-hearted or tearful.  

1. Not true  
2. Somewhat true  
3. Certainly true

**chsdlc\_cv \[Behaviour: liked\]**  
**Universe**: IF parent511 \= 1 AND num511 \= 1, 2, 3, 4, 5 AND ch511namea is not missing // Ask if respondent is parent of 5-11 year old living in the household, and number of children in that age group is reported, and at least one child name is reported.   
**Source:** SDQ, Robert Goodman (2005), UKHLS, question CHSDLC with a different time frame  
**Text:** {ch511name} is generally liked by other children.  

1. Not true  
2. Somewhat true  
3. Certainly true

**chsddc\_cv \[Behaviour: distracted\]**  
**Universe**: IF parent511 \= 1 AND num511 \= 1, 2, 3, 4, 5 AND ch511namea is not missing // Ask if respondent is parent of 5-11 year old living in the household, and number of children in that age group is reported, and at least one child name is reported.   
**Source:** SDQ, Robert Goodman (2005), UKHLS, question CHSDDC with a different time frame  
**Text:** {ch511name} is easily distracted, concentration wanders.  

1. Not true  
2. Somewhat true  
3. Certainly true

**chsdnc\_cv \[Behaviour: nervous\]**  
**Universe**: IF parent511 \= 1 AND num511 \= 1, 2, 3, 4, 5 AND ch511namea is not missing // Ask if respondent is parent of 5-11 year old living in the household, and number of children in that age group is reported, and at least one child name is reported.   
**Source:** SDQ, Robert Goodman (2005), UKHLS, question CHSDNC with a different time frame  
**Text:** {ch511name} is nervous or clingy in new situations, easily loses confidence.  

1. Not true  
2. Somewhat true  
3. Certainly true

**chsdky\_cv \[Behaviour: kind\]**  
**Universe**: IF parent511 \= 1 AND num511 \= 1, 2, 3, 4, 5 AND ch511namea is not missing // Ask if respondent is parent of 5-11 year old living in the household, and number of children in that age group is reported, and at least one child name is reported.   
**Source:** SDQ, Robert Goodman (2005), UKHLS, question CHSDKY with a different time frame  
**Text:** {ch511name} is kind to younger children.  

1. Not true  
2. Somewhat true  
3. Certainly true

**chsdoa\_cv \[Behaviour: often lies\]**  
**Universe**: IF parent511 \= 1 AND num511 \= 1, 2, 3, 4, 5 AND ch511namea is not missing // Ask if respondent is parent of 5-11 year old living in the household, and number of children in that age group is reported, and at least one child name is reported.   
**Source:** SDQ, Robert Goodman (2005), UKHLS, question CHSDOA with a different time frame  
**Text:** {ch511name} often lies or cheats.  

1. Not true  
2. Somewhat true  
3. Certainly true

**chsdpb\_cv \[Behaviour: bullied\]**  
**Universe**: IF parent511 \= 1 AND num511 \= 1, 2, 3, 4, 5 AND ch511namea is not missing // Ask if respondent is parent of 5-11 year old living in the household, and number of children in that age group is reported, and at least one child name is reported.   
**Source:** SDQ, Robert Goodman (2005), UKHLS, question CHSDPB with a different time frame  
**Text:** {ch511name} is picked on or bullied by other children.  

1. Not true  
2. Somewhat true  
3. Certainly true

**chsdvh\_cv \[Behaviour: volunteers\]**  
**Universe**: IF parent511 \= 1 AND num511 \= 1, 2, 3, 4, 5 AND ch511namea is not missing // Ask if respondent is parent of 5-11 year old living in the household, and number of children in that age group is reported, and at least one child name is reported.   
**Source:** SDQ, Robert Goodman (2005), UKHLS, question CHSDVH with a different time frame  
**Text:** {ch511name} often volunteers to help others (parents, teachers, other children).  

1. Not true  
2. Somewhat true  
3. Certainly true

**chsdst\_cv \[Behaviour: thinks\]**  
**Universe**: IF parent511 \= 1 AND num511 \= 1, 2, 3, 4, 5 AND ch511namea is not missing // Ask if respondent is parent of 5-11 year old living in the household, and number of children in that age group is reported, and at least one child name is reported.   
**Source:** SDQ, Robert Goodman (2005), UKHLS, question CHSDST with a different time frame  
**Text:** {ch511name} thinks things out before acting.  

1. Not true  
2. Somewhat true  
3. Certainly true

**chsdcs\_cv \[Behaviour: steals\]**  
**Universe**: IF parent511 \= 1 AND num511 \= 1, 2, 3, 4, 5 AND ch511namea is not missing // Ask if respondent is parent of 5-11 year old living in the household, and number of children in that age group is reported, and at least one child name is reported.   
**Source:** SDQ, Robert Goodman (2005), UKHLS, question CHSDCS with a different time frame  
**Text:** {ch511name} steals from home, school or elsewhere.  

1. Not true  
2. Somewhat true  
3. Certainly true

**chsdgb\_cv \[Behaviour: gets on better\]**  
**Universe**: IF parent511 \= 1 AND num511 \= 1, 2, 3, 4, 5 AND ch511namea is not missing // Ask if respondent is parent of 5-11 year old living in the household, and number of children in that age group is reported, and at least one child name is reported.   
**Source:** SDQ, Robert Goodman (2005), UKHLS, question CHSDGB with a different time frame  
**Text:** {ch511name} gets on better with adults than with other children.  

1. Not true  
2. Somewhat true  
3. Certainly true

**chsdfe\_cv \[Behaviour: fears\]**  
**Universe**: IF parent511 \= 1 AND num511 \= 1, 2, 3, 4, 5 AND ch511namea is not missing // Ask if respondent is parent of 5-11 year old living in the household, and number of children in that age group is reported, and at least one child name is reported.   
**Source:** SDQ, Robert Goodman (2005), UKHLS, question CHSDFE with a different time frame  
**Text:** {ch511name} has many fears, easily scared.  

1. Not true  
2. Somewhat true  
3. Certainly true

**chsdte\_cv \[Behaviour: completes tasks\]**  
**Universe**: IF parent511 \= 1 AND num511 \= 1, 2, 3, 4, 5 AND ch511namea is not missing // Ask if respondent is parent of 5-11 year old living in the household, and number of children in that age group is reported, and at least one child name is reported.   
**Source:** SDQ, Robert Goodman (2005), UKHLS, question CHSDTE with a different time frame  
**Text:** {ch511name} sees tasks through to the end, good attention span.  

1. Not true  
2. Somewhat true  
3. Certainly true

END LOOP.

**tssdqend \[Time stamp: SDQ module end\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time completed last question in this module

# **Neighbourhood cohesion module** {#neighbourhood-cohesion-module}

**Note:** the questions in this module were not translated into Welsh.   
**Universe for module:** IF ff\_country is not 2 OR (ff\_country \= 2 AND welsh \= 2\) // Ask if respondent is not living in Wales or living in Wales and completed the survey in English. 

### **Variables used for routing – from sample file**

**ff\_country** \[country of residence\] 

1. England  
2. Wales  
3. Scotland  
4. N Ireland

### **Variables used for routing – from other modules**

**welsh \[Welsh language\]** – ID check and household composition module

1. Welsh   
2. English 

**tsnbhdst \[Time stamp: neighbourhood module start\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time arrived at first question in this module

**scopngbhh\_cv \[Talk regularly to neighbours\]**    
**Universe:** Ask all.  
**Source:** UKHLS, question SCOPNGBHH wording adapted   
**Text:** Here are some statements about neighbourhoods. Please answer how strongly you agree or disagree with each statement.   
I regularly stop and talk with people in my neighbourhood.

1. Strongly agree  
2. Agree  
3. Neither agree nor disagree  
4. Disagree  
5. Strongly disagree

**nbrcoh3 \[People in this neighbourhood can be trusted\]**    
**Universe:** Ask all.  
**Source:** PHDCN, UKHLS   
**Text:** People in this neighbourhood can be trusted.

1. Strongly agree  
2. Agree  
3. Neither agree nor disagree  
4. Disagree  
5. Strongly disagree

**nbrcoh2 \[People willing to help their neighbours\]**    
**Universe:** Ask all.  
**Source:** PHDCN, UKHLS   
**Text:** People around here are willing to help their neighbours.

1. Strongly agree  
2. Agree  
3. Neither agree nor disagree  
4. Disagree  
5. Strongly disagree  
   

**nbrcoh4 \[People don’t get along with each other\]**    
**Universe:** Ask all.  
**Source:** PHDCN, UKHLS   
**Text:** People in this neighbourhood generally don't get along with each other.

1. Strongly agree  
2. Agree  
3. Neither agree nor disagree  
4. Disagree  
5. Strongly disagree  
   

**scopngbhg \[Am similar to others in neighbourhood\]**    
**Universe:** Ask all.  
**Source:** UKHLS   
**Text:** I think of myself as similar to the people that live in this neighbourhood.

1. Strongly agree  
2. Agree  
3. Neither agree nor disagree  
4. Disagree  
5. Strongly disagree  
   

**crrace\_cv \[Extent of: Racial insults/attacks\]**    
**Universe:** Ask all.  
**Source:** UKHLS, question CRRACE question wording adapted to ask as stand-alone question  
**Text:** How common in your area are insults or attacks to do with someone's race or colour?

1. Very common  
2. Fairly common  
3. Not very common  
4. Not at all common

**tsnbhdend \[Time stamp: neighbourhood module end\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time completed last question in this module

**Volunteering module**

**Note:** the questions in this module were not translated into Welsh.   
**Universe for module:** IF ff\_country is not 2 OR (ff\_country \= 2 AND welsh \= 2\) // Ask if respondent is not living in Wales or living in Wales and completed the survey in English. 

## **Variables used for routing – from sample file**

**ff\_country** \[country of residence\] 

1. England  
2. Wales  
3. Scotland  
4. N Ireland

## **Variables used for routing – from other modules**

**welsh \[Welsh language\]** – ID check and household composition module

1. Welsh   
2. English 

**tsvolst \[Time stamp: volunteering module start\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time arrived at first question in this module

**volun\_cv \[Volunteer in last 4 months\]**    
**Universe:** Ask all.  
**Source:** UKHLS, question VOLUN adapted to ask about last 4 months  
**Text:** Since **March 2020**, have you given any unpaid help or worked as a volunteer for any type of local, national or international organisation or charity? 

1. Yes   
2. No

**volcause \[Reason for volunteering\]**    
**Universe:** IF volun\_cv \= 1 // Ask if volunteered in the last 4 months.  
**Source:** UKHLS covid-19 survey  
**Text:** Why have you been doing unpaid or voluntary work since March 2020?  
*Please select all that apply.*

1. My main motivation was to support the response to the coronavirus pandemic  
2. Other reasons

**volhow \[How volunteering\]**    
**Universe:** IF volun\_cv \= 1 // Ask if volunteered in the last 4 months.  
**Source:** UKHLS covid-19 survey  
**Text:** And since March 2020, how have you been doing unpaid or voluntary work?   
*Please select all that apply.* 

1. In person, together with other volunteers **from outside of my household**   
2. In person, together with other members **of my household**   
3. In person, on my own  
4. Remotely from my home, by making phone calls  
5. Remotely from my home, by using the internet  
6. Other

**volhrs \[Hours spent volunteering in last 4 weeks\]**    
**Universe:** IF volun\_cv \= 1 // Ask if volunteered in the last 4 months.  
**Source:** UKHLS  
**Soft check:** If volhrs \> 50   
**Soft check text:** “You have just entered that you spent {volhrs} volunteering in the last 4 weeks.” Range \[0 \- 200\].  
**Text:** And in the **last 4 weeks** approximately how many hours have you spent doing unpaid or voluntary work for any organisation? If you volunteer for more than one group or agency, please total the time spent in all groups together.  
\[Numeric textbox\] Hours

**tsvolend \[Time stamp: volunteering module end\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time arrived at last question in this module

# **Life satisfaction module** {#life-satisfaction-module}

**Note:** the questions in this module were not translated into Welsh.   
**Universe for module:** IF ff\_country is not 2 OR (ff\_country \= 2 AND welsh \= 2\) // Ask if respondent is not living in Wales or living in Wales and completed the survey in English. 

## **Variables used for routing – from sample file**

**ff\_country** \[country of residence\] 

1. England  
2. Wales  
3. Scotland  
4. N Ireland

## **Variables used for routing – from other modules**

**welsh \[Welsh language\]** – ID check and household composition module

1. Welsh   
2. English 

**tslfsatst \[Time stamp: life satisfaction module start\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time arrived at first question in this module

**sclfsato\_cv \[Satisfaction with life overall\]**  
**Universe**: Ask all.  
**Source:** UKHLS, question SCLFSATO, question wording adapted  
**Text:** How satisfied are you currently with your life overall?

1. Completely dissatisfied  
2. Mostly dissatisfied  
3. Somewhat dissatisfied  
4. Neither satisfied nor dissatisfied  
5. Somewhat satisfied  
6. Mostly satisfied  
7. Completely satisfied

**tslfsatend \[Time stamp: life satisfaction module end\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time completed last question in this module

# **GHQ module**   {#ghq-module}

### **Variables used for routing – from sample file**

n/a

### **Variables used for routing – from other modules**

n/a

**tsghqst \[Time stamp: GHQ module start\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time arrived at first question in this module

**scghqa \[GHQ: concentration\]**  
**Universe:**  Ask all.  
**Source:**  UKHLS   
**Text:** The next questions are about how you have been feeling over the last few weeks.   
Have you recently been able to concentrate on whatever you're doing?

1. Better than usual  
2. Same as usual  
3. Less than usual  
4. Much less than usual  
   

**scghqb \[GHQ: loss of sleep\]**  
**Universe:**  Ask all.  
**Source:**  UKHLS   
**Text:** Have you recently lost much sleep over worry?

1. Not at all  
2. No more than usual  
3. Rather more than usual  
4. Much more than usual

**scghqc \[GHQ: playing a useful role\]**  
**Universe:**  Ask all.  
**Source:**  UKHLS   
**Text:** Have you recently felt that you were playing a useful part in things?

1. More so than usual  
2. Same as usual  
3. Less so than usual  
4. Much less than usual

**scghqd \[GHQ: capable of making decisions\]**  
**Universe:**  Ask all.  
**Source:**  UKHLS   
**Text:** Have you recently felt capable of making decisions about things?

1. More so than usual  
2. Same as usual  
3. Less so than usual  
4. Much less capable

**scghqe \[GHQ: constantly under strain\]**  
**Universe:**  Ask all.  
**Source:**  UKHLS   
**Text:** Have you recently felt constantly under strain?

1. Not at all  
2. No more than usual  
3. Rather more than usual  
4. Much more than usual

**scghqf \[GHQ: problem overcoming difficulties\]**  
**Universe:**  Ask all.  
**Source:**  UKHLS   
**Text:** Have you recently felt you couldn't overcome your difficulties?

1. Not at all  
2. No more than usual  
3. Rather more than usual  
4. Much more than usual

**scghqg \[GHQ: enjoy day-to-day activities\]**  
**Universe:**  Ask all.  
**Source:**  UKHLS   
**Text:** Have you recently been able to enjoy your normal day-to-day activities?

1. More so than usual  
2. Same as usual  
3. Less so than usual  
4. Much less than usual

**scghqh \[GHQ: ability to face problems\]**  
**Universe:**  Ask all.  
**Source:**  UKHLS   
**Text:** Have you recently been able to face up to problems?

1. More so than usual  
2. Same as usual  
3. Less able than usual  
4. Much less able  
   

**scghqi \[GHQ: unhappy or depressed\]**  
**Universe:**  Ask all.  
**Source:**  UKHLS   
**Text:** Have you recently been feeling unhappy or depressed?

1. Not at all  
2. No more than usual  
3. Rather more than usual  
4. Much more than usual

**scghqj \[GHQ: losing confidence\]**  
**Universe:**  Ask all.  
**Source:**  UKHLS   
**Text:** Have you recently been losing confidence in yourself?

1. Not at all  
2. No more than usual  
3. Rather more than usual  
4. Much more than usual

**scghqk \[GHQ: believe worthless\]**  
**Universe:**  Ask all.  
**Source:**  UKHLS   
**Text:** Have you recently been thinking of yourself as a worthless person?

1. Not at all  
2. No more than usual  
3. Rather more than usual  
4. Much more than usual

**scghql \[GHQ: general happiness\]**  
**Universe:**  Ask all.  
**Source:**  UKHLS   
**Text:** Have you recently been feeling reasonably happy, all things considered?

1. More so than usual  
2. About the same as usual  
3. Less so than usual  
4. Much less than usual

**tsghqend \[Time stamp: GHQ module end\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time completed last question in this module

# **Health linkage consent module** {#health-linkage-consent-module}

### **Variables used for routing – from sample file**

n/a

### **Variables used for routing – from other modules**

n/a

**tshlthdatast \[Time stamp: health linkage module start\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time arrived at first question in this module

**cvhlthlink \[Health data linkage consent\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**Scripting notes:** Link to leaflet: [https://www.understandingsociety.ac.uk/participants/health-records](https://www.understandingsociety.ac.uk/participants/health-records) and link to diagram: [https://www.understandingsociety.ac.uk/participants/data-linkage](https://www.understandingsociety.ac.uk/participants/data-linkage)   
Display information icon after “….about your health including”: “The data only contains information that has been coded, for example, categories of treatments. It does not include any free text, such as notes written by consultants.”  
**Text:** To complement the information Understanding Society collects, we would like to find out more about your health and treatment from data held by the NHS (in the four countries of the UK). This would allow researchers to investigate how your health and wider circumstances interact. If you agree: 

* We would like to link to information the NHS has about your health including:  
  * data from hospital care records (including dates of admission and consultations, treatments received, and referrals made)   
  * primary care records (including doctor and nurse consultations, diagnoses received, treatments given, and referrals made)   
  * data on prescriptions  
  * information on COVID-19 infection notification and test results

* We will send NHS data holders your personal identifiers (including name, address, sex and date of birth) so that they can identify the records they have about you.   
* The NHS data holders will anonymise your records: they will contain an anonymous identification number but not your personal identifiers (name, address, sex, date of birth or NHS number).   
* The anonymised NHS records will be added to the answers you have given in this study.   
* We will make the combined anonymous data available for academic and policy research purposes only.   
* Access to the data will be restricted and controlled, to make sure that researchers use the information responsibly and safely.   
* This will not affect the way that you deal with the NHS in any way. 

   
Please read this leaflet and look at this diagram for further information.

Do you give permission for us to pass your personal identifiers (including name, address, postcode, sex and date of birth) to NHS data holders for this purpose?

1. Yes  
2. No

**cvreglink \[Registry data linkage consent\]**   
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**Text:** We would also like to link to information about cancer registrations and the death registration records held by the General Registrars and Public Health bodies in each of the four countries of the UK. 

Do you give permission for us to pass your personal identifiers (including name, address, postcode, sex and date of birth) to the NHS data holders for this purpose?

1. Yes  
2. No

**tshlthdataend \[Time stamp: health data module end\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time completed last question in this module

# **Serology consent module** {#serology-consent-module}

### **Variables used for routing – from sample file**

**ff\_incentw8** **\[Treatment allocation for incentive experiment, wave 8\]**  
\-8.  Inapplicable (£2 for survey)  
1\. £2 for survey \+ £5 for blood sample  
2\. £7 for survey \+ £5 for blood sample  
3\. £12 for survey \+ £5 for blood sample  
4\. £7 for survey   
5\. £12 for survey   
6\. £17 for survey 

### **Variables used for routing – from other modules**

**Age \[Age – derived\]** – ID check and household composition module

**tsserolst \[Time stamp: serology module start\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time arrived at first question in this module

**serolconsent \[Serology consent\]**    
**Universe:** IF age \=\> 18 // Ask if respondent is aged 18 or older.   
**Source:** UKHLS covid-19 survey  
**Scripting notes:** Link for additional information: [www.understandingsociety.ac.uk/participants/serology](http://www.understandingsociety.ac.uk/participants/serology)   
Link to video: [https://www.youtube.com/watch?v=okTozcGMDlU](https://www.youtube.com/watch?v=okTozcGMDlU)   
Add info button after the first sentence: “Antibodies are made by our immune system to fight infection.” Add info button after the final bullet and after the 3rd response option: “You will not be able to take part if you are pregnant; have clotting or bleeding disorders; are currently on anti-coagulant medication (e.g. Warfarin therapy); have had a recent mastectomy and there is swelling of the arm; on renal dialysis; or are HIV, Hepatitis B or Hepatitis C positive.”  
**Text:** We would like to understand how many of our participants across the country have developed antibodies against the virus that causes COVID-19. 

This is part of a national initiative where other research studies in the UK are also asking their participants to complete the same antibody test. Analysing the information from Understanding Society alongside these other studies will allow a greater understanding of the impact of COVID-19 on people’s health and other aspects of life. You can take part even if you have recently been vaccinated.

{IF ff\_incentw8 \= 1, 2, 3: If you return your completed blood sample to us, we will give you a £5 reward to thank you for your extra help.}

* If you agree, we would like to send you a small kit which will allow you to 	take an antibody test.   
* The test will involve pricking your finger with a small needle and collecting the blood in a small tube.   
* You will then need to send the blood sample back in the pre-paid return envelope that will be included in the pack.   
* The laboratory will test your blood for COVID-19 antibodies and, if you want it, you will receive a letter with your result within two weeks of posting your sample back to us.   
* If you change your mind after you receive the kit, that is fine – you don’t need to do anything.   
* All the materials and full instructions will be included in the package.   
* Your name and address will be used by Ipsos MORI to send you the kit, but no identifiable information will be sent to the laboratory.  
* The results of your test will be added to your survey responses, and the data from the project will be available in **anonymised** format to other researchers, through the UK Data Service or other data repositories. **Anonymised** data and sample results may be shared with other bona fide scientists, including those from the Department of Health and Social Care (DHSC) and Public Health England (PHE).  
* If you have certain health or medical conditions you will not be able to take part. 

For more information, please click \<here\>.   
To see a video of what is in the kit and what is involved, please click \<here\>. 

May we send you the antibody testing kit through the post?

1. Yes  
2. No  
3. I have one of the health or medical conditions that means I cannot take part

**serolfeed \[Serology feedback\]**    
**Universe:**  IF serolconsent \= 1 // Ask if participant consents to having the serology kit sent.   
**Source:** UKHLS covid-19 survey  
**Text:** Would you like to receive your results from the antibody test? 

1. Yes  
2. No

**tsserolend \[Time stamp: serology module end\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time completed last question in this module

# **Consent follow-up questions module**

### **Variables used for routing – from sample file**

n/a

### **Variables used for routing – from other modules**

**serolconsent \[Serology consent\]** – Serology consent module

4. Yes  
5. No

**cvhlthlink \[Health data linkage consent\] –** Health linkage consent module

3. Yes  
4. No

**cvreglink \[Registry data linkage consent\] –** Health linkage consent module

1. Yes  
2. No

**tsconsfust \[Time stamp: consent follow-up module start\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time arrived at first question in this module

**consentintro \[Consent follow-up questions, intro\]**  
**Universe**: Ask all.  
**Source:** UKHLS covid-19 survey  
**Text:** To help us understand how we might improve questions about linking health data and antibody tests in future, we would like to ask you a couple of questions.

**whynotorder1 \[Why not consented to data linkage, response order 1\]**  
**Universe**: Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED:** Randomised order of numbers 1 – 6, to determine order in which the response options for healthwhynot, regwhynot, serolwhynot are displayed. 

**whynotorder2 \[Why not consented to data linkage, response order 2\]**  
**Universe**: Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED:** Randomised order of numbers 7 – 9, to determine order in which the response options for serolwhynot are displayed. 

**healthwhynot \[Why not consented to health data linkage\]**  
**Universe**: IF cvhlthlink is not 1 // Ask if did not consent to health data linkage.  
**Source:** UKHLS covid-19 survey  
**Scripting notes:** Display response options 1 – 6 in the order determined by whynotorder1. Display options 7, 8 last.  
**Text:** Can you tell us why you did **not** give us permission to add records collected by the National Health Service, or NHS, to the answers you have given in this study?  
*Please select all that apply.*

1. Too personal, I’ve shared enough information with this survey   
2. I am unclear about the risks involved / don’t understand what would be done  
3. I’m worried that my health records might be used against me  
4. I’m worried that my health records might be lost / hacked / stolen  
5. I was too tired / didn’t want to make a decision  
6. Unclear why I am being asked for this / what the data would be used for  
7. The NHS doesn’t have any data about me  
8. Other reason

**regwhynot \[Why not consented to Registry data linkage\]**  
**Universe**: IF cvreglink is not 1 // Ask if did not consent to Registry data linkage.  
**Source:** UKHLS covid-19 survey  
**Scripting notes:** Display response options 1 – 6 in the order determined by whynotorder1. Display options 7, 8 last.  
**Text:** Can you tell us why you did **not** give us permission to add records held by the General Registrars and Public Health bodies to the answers you have given in this study?  
*Please select all that apply.*

1. Too personal, I’ve shared enough information with this survey   
2. I am unclear about the risks involved  / don’t understand what would be done  
3. I’m worried that my records might be used against me  
4. I’m worried that my records might be lost / hacked / stolen  
5. I was too tired / didn’t want to make a decision  
6. Unclear why I am being asked for this / what the data would be used for  
7. The General Registrars and Public Health bodies don’t have any data about me  
8. Other reason

**serolwhynot \[Why not consented to serology\]**  
**Universe**: IF age \>= 18 AND serolconsent is not 1, 3 // Ask if respondent is aged 18 or older, and did not consent to being sent blood kit for antibody test and does not have a health condition that means they cannot do the test.  
**Source:** UKHLS covid-19 survey  
**Scripting notes:** Display response options 1 – 6 in the order determined by whynotorder1. Display response options 7 – 9 in the order determined by whynotorder2, after response options 1 – 6\. Display option 10 last.   
**Text:** Can you tell us why you did **not** give permission for us to send you the COVID-19 antibody testing kit through the post?  
*Please select all that apply.*

1. Too personal, I’ve shared enough information with this survey   
2. I am unclear about the risks involved  / don’t understand what would be done  
3. I’m worried that my COVID-19 test result might be used against me  
4. I’m worried that my COVID-19 test result might be lost / hacked / stolen  
5. I was too tired / didn’t want to make a decision  
6. Unclear why I am being asked for this / what the data would be used for  
7. I don’t want to know whether I have had COVID-19   
8. I don’t want to prick my finger   
9. Takes too much time  
10. Other reason

**whyorder \[Why consented to data linkage, response order\]**  
**Universe**: Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED:** Randomised order of numbers 1 – 5, to determine order in which the response options for healthwhy, regwhy, serolwhy are displayed. 

**healthwhy \[Why consented to health data linkage\]**  
**Universe**: IF cvhlthlink \= 1 // Ask if consented to health data linkage.  
**Source:** UKHLS covid-19 survey  
**Scripting notes:** Display response options 1 – 5 in the order determined by whyorder. Display option 6 last.  
**Text:** Can you tell us why you gave us permission to add records collected by the National Health Service, or NHS, to the answers you have given in this study?  
*Please select all that apply.*

1. I trust the study not to mishandle information  
2. I trust the NHS  
3. To support the NHS  
4. To support research for the greater good of society  
5. I didn’t see any reason not to / I have nothing to hide  
6. Other reason  
   

**regwhy \[Why consented to Registry data linkage\]**  
**Universe**: IF cvreglink \= 1 // Ask if consented to Registry data linkage.  
**Source:** UKHLS covid-19 survey  
**Scripting notes:** Display response options 1 – 5 in the order determined by whyorder. Display option 6 last.  
**Text:** Can you tell us why you gave us permission to add records held by the General Registrars and Public Health bodies to the answers you have given in this study?  
*Please select all that apply.*

1. I trust the study not to mishandle information  
2. I trust the General Registrars and Public Health bodies  
3. To support the General Registrars and Public Health bodies  
4. To support research for the greater good of society  
5. I didn’t see any reason not to / I have nothing to hide  
6. Other reason

**serolwhy \[Why consented to serology\]**  
**Universe**: IF serolconsent \= 1 // Ask if consented to being sent blood kit for antibody test.  
**Source:** UKHLS covid-19 survey  
**Scripting notes:** Display response options 1 – 5 in the order determined by whyorder. Display options 6 and 7 last.  
**Text:** Can you tell us why you gave permission for us to send you the COVID-19 antibody testing kit through the post?  
*Please select all that apply.*

1. I trust the study not to mishandle information  
2. I trust the NHS  
3. To support the NHS  
4. To support research for the greater good of society  
5. I didn’t see any reason not to / I have nothing to hide  
6. I wanted to know if I have had COVID-19  
7. Other reason

**objunda \[Objective understanding of health data linkage A\]**  
**Universe:** Ask all.   
**Source:** Das and Couper 2014  
**Scripting notes:** Display objunda, objundb, objundc, objundd on the same screen.   
**Text:** To help us understand whether the explanation we gave you about linking NHS data and your answers to this study was clear or unclear, here are a few statements about how the linkage is done. Please specify whether you think each of the statements is true or false.   
*Please select one answer per row.*

The NHS will be able to see the answers you have given in this study.

1. True  
2. False   
   

**objundb \[Objective understanding of health data linkage B\]**  
**Universe:** Ask all.   
**Source:** Das and Couper 2014  
**Scripting notes:** Display objunda, objundb, objundc, objundd on the same screen.  
**Text:** The NHS data holder will send us the information they have about you.

1. True  
2. False 

	  
**objundc \[Objective understanding of health data linkage C\]**  
**Universe:** Ask all.   
**Source:** Das and Couper 2014  
**Scripting notes:** Display objunda, objundb, objundc, objundd on the same screen.  
**Text:** Your name, address, sex, and date of birth will be saved with the linked data.

1. True  
2. False 

**objundd \[Objective understanding of health data linkage D\]**  
**Universe:** Ask all.   
**Source:** Das and Couper 2014  
**Scripting notes:** Display objunda, objundb, objundc, objundd on the same screen.  
**Text:** We will send your name, address, sex, and date of birth to the NHS data holder.

1. True  
2. False 

**linkrsrc \[Data linkage reassurance screen\]**  
**Universe**: Ask all.   
**Source:** UKHLS   
**Text:** Thank you for answering the True/False questions about the process of adding NHS data. Just to reassure you, the information you give us is always treated confidentially. Names, addresses and dates of birth are never included with the data. The NHS does not get access to the answers you have given in this study.

**tsconsfuend \[Time stamp: consent follow-up module end\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time completed last question in this module

# **Survey device and incentives module** {#survey-device-and-incentives-module}

**Note:** the questions in this module were not translated into Welsh.   
**Universe for module:** IF ff\_country is not 2 OR (ff\_country \= 2 AND welsh \= 2\) // Ask if respondent is not living in Wales or living in Wales and completed the survey in English. 

### **Variables used for routing – from sample file**

**ff\_country** \[country of residence\] 

5. England  
6. Wales  
7. Scotland  
8. N Ireland

### **Variables used for routing – from other modules**

**welsh \[Welsh language\]** – ID check and household composition module

3. Welsh   
4. English 

**tsdevicest \[Time stamp: survey device module start\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time arrived at first question in this module

**device \[Device used for survey\]**  
**Universe**: Ask all.  
**Source:** UKHLS covid-19 survey  
**Text:** What device are you using to complete this survey? 

4. My own smartphone  
5. My work smartphone   
6. A smartphone that I own / share with someone else  
7. Someone else’s smartphone  
8. A tablet  
9. A laptop or notebook  
10. A PC/desktop computer  
11. Something else

**incentval \[Incentive value\]**  
**Universe**: Ask all.  
**Source:** UKHLS covid-19 survey  
**Scripting notes:** Range \[0 – 99\].   
**Text:** As far as you remember, what is the reward amount that you will receive for completing this month’s COVID-19 survey?   
\[Numeric textbox\] Pounds

1. Don’t know

**incentvalhow \[How reported incentive value\]**  
**Universe**: IF incentval is not missing // Ask if incentive value reported.   
**Source:** UKHLS covid-19 survey  
**Scripting notes:** Range \[0 – 99\].   
**Text:** Did you remember the reward amount for this month’s COVID-19 survey or did you look it up?

1. I remembered  
2. I looked it up 

**tsdeviceend \[Time stamp: survey device module end\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time completed last question in this module

# **Closing module** {#closing-module}

### **Variables used for routing – from sample file**

**surveymonth –** calendar month and year of current survey  
March 2021

**mobnoflag \[Mobile number known\]**  
Notes: Set to 1 if a number is known – either from the initial sample file or has been updated since the start of fieldwork.

0. No  
1. Yes

**smsoptout \[Opted out of receiving invitations by SMS\]**  
Notes: Set to 1 if respondent has opted out of receiving invitations by SMS.

1. Yes

Missing or 0 for everyone else?

 **emailflag \[Valid email address known\]**

0. No  
1. Yes

**emailoptout \[Opted out of receiving invitations by email\]**

1. Yes

Missing or 0 for everyone else?

**ff\_incentw8** **\[Treatment allocation for incentive experiment, wave 8\]**  
\-8.  Inapplicable (£2 for survey)

1. £2 for survey \+ £5 for blood sample  
2. £7 for survey \+ £5 for blood sample  
3. £12 for survey \+ £5 for blood sample  
4. £7 for survey   
5. £12 for survey   
6. £17 for survey 

### **Variables used for routing – from other modules**

**serolconsent \[Serology consent\]** – Serology consent module

1. Yes  
2. No   
   

**tsclosest \[Time stamp: closing module start\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time arrived at first question in this module

**openend \[Other experiences with coronavirus\]**  
**Universe**: Ask all.  
**Source:** UKHLS covid-19 survey  
**Scripting notes:** Display character limit (4,000).  
**Text:** Is there anything else you would like to tell us about how the coronavirus is affecting your life, that you have not previously told us about?  
\[Textbox\]

**mobno \[Mobile number\]**  
**Universe**: IF monobflag \= 0 AND smsoptout is not 1 // Ask if mobile number not known and has not opted out of receiving invitations by SMS.  
**Source:** UKHLS covid-19 survey  
**Scripting notes:** Range \[tbc\]. Allow respondent to leave this blank. The script checks the mobile number and this message will appear if incorrect: “Please ensure you enter your mobile number correctly. Your number should start with 07 and be a total of 11 digits, entered with no spaces”.  
**Text:** We do not have a mobile number for you. If you would like to receive an invitation for the next monthly survey by SMS, please enter your mobile number.   
\[Numeric textbox\]

1. I do not wish to receive an invitation by SMS  
2. I do not have a mobile phone

**email1 \[Email address\]**  
**Universe**: IF emailflag \= 0 AND emailoptout is not 1 // Ask if no valid email address known and has not opted out of receiving invitations by email.  
**Source:** UKHLS covid-19 survey  
**Scripting notes:** Soft check “This is not a valid email address, please enter a valid address (e.g. [undcorona@ipsos.com)](mailto:undcorona@ipsos.com\)).” Allow respondent to leave this blank. The script checks the email address and this message will appear if incorrect: “This is not a valid email address, please enter a valid address (e.g. undcorona@ipsos.com)”.  
**Text:** We do not have an email address for you. If you would like to receive an invitation for the next monthly survey by email, please enter your email.  
\[Alphanumeric textbox\]

1. I do not wish to receive an invitation by email  
2. I do not have an email address

**incentives \[Incentives earned\]**  
**Universe**: Ask all.  
**Source:** UKHLS covid-19 survey  
**Text:** Thank you for telling us about how the coronavirus is affecting your life.   
Your ‘reward account’ has been credited with {IF ff\_incentw8 \= 1: £2 / IF ff\_incentw8 \= 2, 4: £7 / IF ff\_incentw8 \= 3, 5: £12 / IF ff\_incentw8 \= 6: £17}. {IF ff\_incentw8 \= 1, 2, 3 AND serolconsent \= 1: Plus, if you return your completed blood sample to us, we will give you a £5 reward to thank you for your extra help.}  
You can exchange the reward amount for a range of gift-cards and electronic vouchers at any point.   
{IF surveymonth is not July 2021: You currently have vouchers worth £\<VALUE\>. Would you like to claim this now, or wait until you have completed the final COVID-19 survey in July?}  
{IF surveymonth \= July 2021: You currently have vouchers worth £\<VALUE\>. Please click to claim your voucher.}

1. Claim now – You will need to get to the end of the survey in order to claim your incentive  
2. {IF surveymonth is not July 2021} Wait until I’ve completed the final COVID-19 survey in July  
3. Donate everything in my reward account to NHS Charities Together  
   

**email2 \[Email address\]**  
**Universe**: IF incentives \= 1 AND emailflag \= 0 AND email1 is not valid address // Ask if wants to claim incentive and no valid email address known and has not provided a valid address at email1.  
**Source:** UKHLS covid-19 survey  
**Scripting notes:** Soft check “This is not a valid email address, please enter a valid address (e.g. undcorona@ipsos.com).”  
**Text:** We currently do not hold an email address for you, please provide one.   
\[Alphanumeric textbox\]

1. I do not have an email address

**noemailvoucher \[Voucher without email\]**  
**Universe**: IF incentives \= 1 AND emailflag \= 0 AND email1 is not valid address AND email2 \= 1 // Ask if wants to claim incentive and no valid email address known and has not provided a valid address at email1 and selects not having an email address at email2.  
**Source:** UKHLS covid-19 survey  
**Scripting notes:** Do not display DK and REF answer options, answer required.  
**Text:** As we do not hold a valid email address for you, our incentive provider SVM Global will send you a letter with a hardcopy voucher to thank you for participating in our study. Please allow up to three weeks for this letter to arrive.

Please select which voucher you would like.

1. Asda  
2. John Lewis  
3. M\&S  
4. Next  
5. Tesco

**incentclaim \[Claiming incentives\]**  
**Universe**: IF incentives \= 1 AND (emailflag \= 1 OR email1 is valid address OR email 2 is valid address) // Ask if respondent wants to claim incentives and we have a valid email address, or they provided a valid address at email1 or email2.  
**Source:** UKHLS covid-19 survey  
**Text:** You will receive an email from our incentive provider SVM Global explaining exactly how to claim your voucher. Please allow up to ten days for this email to arrive and check your junk mailbox.

**charclaim \[Charity donation\]**  
**Universe:** IF incentives \= 3 // Ask if respondent wants to donate incentive value to charity.   
**Source:** UKHLS covid-19 survey  
**Text:** Thank you for deciding to charitably donate everything in your reward account to **NHS Charities Together**. The donation will be made automatically, and you do not need to do anything. For more information on this charity, please go to: [www.nhscharitiestogether.co.uk](http://www.nhscharitiestogether.co.uk) 

**end \[Closing statement\]**  
**Universe**: Ask all.  
**Source:** UKHLS covid-19 survey  
**Text:** Many thanks for taking the time to answer these questions and for your contributions to the *Understanding Society* study.   
	  
If you have any concerns about coronavirus or your mental health or would like further support, please visit [http://www.nhs.uk/coronavirus](http://www.nhs.uk/coronavirus) or call the Samaritans on 116 123\.

**tscloseend \[Time stamp: closing module end\]**    
**Universe:** Ask all.  
**Source:** UKHLS covid-19 survey  
**DERIVED**: Date and time completed last question in this module

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEIAAAAYCAYAAABOQSt5AAAAWElEQVR4Xu3QwQ0AIAjFUNZlK3ZjEA2mF2egTb7B64uqOts3xRyZuXbd/UPE0oQgIUgIEoKEICFICBKChCAhSAgSgoQgIUgIEoKEICFICPog5rN5D+K9di7jPEw4b7RRHQAAAABJRU5ErkJggg==>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEIAAAAYCAYAAABOQSt5AAAA5UlEQVR4Xu2WAQrDIAxFva636t08SEe6BNLfRO3ElWIeuMafYLtHB0vbtu2rLyJRkXNedpVSziLSooQIJkQwIYIJEcyoCGveyjSt/ig/nf+EiH9x6zlmiqCrXgLuJcO9l1nna/C+Vv8CiUjUmyQCM11bWW+NWHNWhrVm6huBma5bmeD1aI8ZYc17tTD8z9Ka730QvGKNeD0UUjvXPeNJEVLjGV4fc43Vs2Yw0wyJIOQGeKO7tdBznuxrc17u8Z0fEPEWqt9t9KfxFvDtuLCKiCYhggkRTIhgQgRzEkGbldch4vgM9g9b17TM6nMiXQAAAABJRU5ErkJggg==>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEIAAAAYCAYAAABOQSt5AAAA2UlEQVR4Xu2WawrEIAyEva638m4epEtqhHRItPiApeYDu8kkxHTojw0ppev0QwQKYozHnpzz04hwKG4E40YwbgTjRjAzRmAv5Zomf1exeh5R9h80QvZjXrUd7Jg7/EUQaERLw9labmlYs3RZQyy9ss2IVu1fYskSI7SLRrSKVuvF1hxLR0rvoBGV3mKoaTUNq0+LtTnl5d4x9UUQ2mWtvNcv66ivivF+YokRCGq4CFKXwyVHYmuOpkumjfgEM3+oPoUbwbgRjBvBuBGMG8E8jKDk5HMbcT+d6wc5Vqd/hxg4AwAAAABJRU5ErkJggg==>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEIAAAAYCAYAAABOQSt5AAAA0UlEQVR4Xu2VUQqEMAxEe93eqnfrQVyiKcQhidWq4DYP4urMpsj7MZVSltmHSHSTc552aq17EWlSQgQTIpgQwYQI5g4RtCPnTGdh7Wk7LcMduduTbXNRhDxYZu3X6vBe4u1hTngdgTk+E8OfT+//Vnf2xSVaN3Je45MitLE6zC0+KQI5Ok9iCXlExNGL9fYSb6enQzB/XYTMtJ7Q8p4ztY7QcsyGRRC0I+dqJ3svR1qGO94gt4j4C0IEEyKYEMGECCZEMCGC2Ymgh5lnFbFeg+UH0aLVA7U3NnQAAAAASUVORK5CYII=>

[image5]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEIAAAAYCAYAAABOQSt5AAAAr0lEQVR4Xu2SUQrFIAwEva638m4epCVlC3ZJyns0frTuQIrZRsHB0lrbVi+j2KLWumz13q8iyqJIBJAIIBFAIsBTETbv1evIEPEJZomIXkeUG5x7/TQyRHAxXmZEl/TW0RlpZIjwuJPCOfcGy/BmUpkl4iS6xJh7/0eiM1KZIYKz6MJjz2vew3vTyRDxS538k3sz03gq4jNIBJAIIBFAIoBEAIkAFxHWrFyHiOMrth3mP5nqT6kySgAAAABJRU5ErkJggg==>

[image6]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEIAAAAYCAYAAABOQSt5AAAA20lEQVR4Xu2QAQ7DIAhFva636t08SBcMJEg/tE3dlk1eYqN8sO0r27btqy+i0KbWuuxqrY0iyqKkCCZFMCmCSRHMDBE0o9fVTIgywsuju6MM8lQEepGco0yD+gRd9/b2jO6z5wMzRHh4mf1oW/NAcwgv8+qdb4q482M2l5qtE6hGePXOL4gQvB4rJOpzeYcI9KMa+XC0zojujjLCq3c+LQLViCt1LQv1o0xmUP/AUxGEfpmdjzKNl0XzdzKbH5gh4i9IEUyKYFIEkyKYFMGkCGYQQYeVVxfRn8n+ArCWwMMyCWDzAAAAAElFTkSuQmCC>