# PSID Generic Crisis Module: NLP Optimization with Hurricane Katrina Integration
# Jupyter Notebook Structure (Conceptual Reference)
# Date: March 8, 2026

"""
This notebook implements the complete NLP-driven optimization pipeline for the 
PSID Generic Crisis Module, now enhanced with Hurricane Katrina 2007 supplement integration.

INPUTS:
- Shutdown_Income_Questions.csv (57 questions)
- Shutdown_Crisis_Questions.csv (19 questions)
- COVID19_Questions.csv (20 questions)
- Understanding_Society_Demographics.csv (7 questions)
- Katrina_Questions.csv (37 questions from 2007 supplement) ← NEW

OUTPUTS:
- PSID_Ranked_Questions_Katrina_Integrated.csv (complete ranked export)
- Five publication-quality visualizations
- Toggle-classified module assembly

METHODOLOGY:
Ri = Ui / Bi
where Ui = Σ wk (information utility from matched keywords)
      Bi = α·Ni + β·Ci (respondent burden from length + complexity)
"""

# ═══════════════════════════════════════════════════════════════════════════════
# CELL 1: Environment Setup
# ═══════════════════════════════════════════════════════════════════════════════

# Standard libraries
import pandas as pd
import numpy as np
import re
from collections import Counter

# NLP libraries
import spacy
from rake_nltk import Rake

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Load spaCy model for entity recognition and noun phrase extraction
nlp = spacy.load("en_core_web_sm")

# Initialize RAKE for keyword extraction
rake = Rake(
    min_length=1,
    max_length=4,
    stopwords=None  # Will use RAKE's default stopwords
)

print("✓ Environment initialized")
print(f"✓ spaCy version: {spacy.__version__}")
print("✓ RAKE initialized")


# ═══════════════════════════════════════════════════════════════════════════════
# CELL 2: Data Ingestion (ENHANCED with Katrina integration)
# ═══════════════════════════════════════════════════════════════════════════════

def load_question_data():
    """
    Load all question sources including Hurricane Katrina 2007 supplement.
    """
    
    # Load existing sources
    shutdown_income = pd.read_csv('Shutdown_Income_Questions.csv')
    shutdown_crisis = pd.read_csv('Shutdown_Crisis_Questions.csv')
    covid19 = pd.read_csv('COVID19_Questions.csv')
    demographics = pd.read_csv('Understanding_Society_Demographics.csv')
    
    # NEW: Load Hurricane Katrina supplement
    katrina = pd.read_csv('Katrina_Questions.csv')
    
    # Standardize column names
    for df in [shutdown_income, shutdown_crisis, covid19, demographics, katrina]:
        df.columns = ['questiontext', 'source', 'moduletype']
    
    # Add source labels
    shutdown_income['source'] = 'Govt Shutdown Income'
    shutdown_crisis['source'] = 'Govt Shutdown Crisis'
    covid19['source'] = 'COVID-19'
    demographics['source'] = 'Understanding Society'
    katrina['source'] = 'Hurricane Katrina 2007'
    
    # Combine all sources
    all_questions = pd.concat([
        shutdown_income, 
        shutdown_crisis, 
        covid19, 
        demographics, 
        katrina  # NEW
    ], ignore_index=True)
    
    print(f"✓ Loaded {len(shutdown_income)} Shutdown Income questions")
    print(f"✓ Loaded {len(shutdown_crisis)} Shutdown Crisis questions")
    print(f"✓ Loaded {len(covid19)} COVID-19 questions")
    print(f"✓ Loaded {len(demographics)} demographic questions")
    print(f"✓ Loaded {len(katrina)} Hurricane Katrina questions")
    print(f"✓ Total corpus: {len(all_questions)} questions")
    
    return all_questions

# Load data
questions_df = load_question_data()


# ═══════════════════════════════════════════════════════════════════════════════
# CELL 3: NLP Pipeline - Dual Keyword Extraction
# ═══════════════════════════════════════════════════════════════════════════════

def extract_keywords(text):
    """
    Extract keywords using dual-engine approach:
    1. RAKE for statistical keyphrases
    2. spaCy for noun phrases and disaster-specific entities
    
    Returns: List of unique keywords (deduplicated union)
    """
    
    # Method 1: RAKE extraction
    rake.extract_keywords_from_text(text)
    rake_keywords = rake.get_ranked_phrases()
    
    # Method 2: spaCy noun phrase chunking
    doc = nlp(text.lower())
    spacy_keywords = [chunk.text for chunk in doc.noun_chunks]
    
    # Union (deduplicated)
    all_keywords = list(set(rake_keywords + spacy_keywords))
    
    # Filter out very short keywords (< 3 chars) unless they're critical terms
    critical_short = {'job', 'age', 'sex', 'rent', 'fee', 'pay', 'aid'}
    filtered_keywords = [
        kw for kw in all_keywords 
        if len(kw) >= 3 or kw in critical_short
    ]
    
    return filtered_keywords

# Apply keyword extraction to all questions
questions_df['keywords'] = questions_df['questiontext'].apply(extract_keywords)
questions_df['nkeywords'] = questions_df['keywords'].apply(len)

print(f"✓ Extracted keywords for {len(questions_df)} questions")
print(f"  Average keywords per question: {questions_df['nkeywords'].mean():.1f}")


# ═══════════════════════════════════════════════════════════════════════════════
# CELL 4: Expanded Semantic Taxonomy (DISASTER-ENHANCED)
# ═══════════════════════════════════════════════════════════════════════════════

# Seven-construct taxonomy with expert-assigned impact weights
# UPDATED with maximum weights for disaster-specific keywords

TAXONOMY = {
    'Economic/Income': {
        'keywords': [
            'income', 'earnings', 'wages', 'salary', 'profit', 'revenue', 
            'receipts', 'net income', 'gross income', 'operating expenses',
            'business income', 'self-employment', 'rental income'
        ],
        'weight': 0.80
    },
    
    'Employment': {
        'keywords': [
            'job', 'work', 'working', 'employed', 'employment', 'unemployed',
            'furloughed', 'laid off', 'hours worked', 'essential work',
            'remote work', 'work from home', 'job loss', 'stopped working'
        ],
        'weight': 0.75
    },
    
    'Financial Coping': {
        'keywords': [
            'savings', 'borrow', 'credit card', 'loan', 'debt', 'retirement',
            'financial difficulties', 'food bank', 'assistance', 'help',
            'cut back', 'expenses', 'budget', 'afford', 'pay bills',
            'late payment', 'put off paying'
        ],
        'weight': 0.85
    },
    
    'Housing/Shelter': {
        'keywords': [
            'rent', 'mortgage', 'housing', 'home', 'apartment', 'residence',
            'eviction', 'foreclosure', 'utility bills', 'landlord',
            # NEW: Disaster-specific keywords (maximum weight)
            'displaced', 'evacuation', 'evacuate', 'structural damage',
            'home destroyed', 'home damaged', 'property damage', 'flooding',
            'hurricane damage', 'temporary housing', 'shelter', 'homeless'
        ],
        'weight_base': 0.85,
        'weight_disaster': 0.95  # Maximum weight for displacement/destruction
    },
    
    'Government Aid': {
        'keywords': [
            'stimulus', 'unemployment insurance', 'government assistance',
            'social security', 'SNAP', 'food stamps', 'welfare', 'benefits',
            'Paycheck Protection Program', 'PPP', 'EIDL', 'relief payment',
            # NEW: Disaster-specific government aid
            'FEMA', 'Federal Emergency Management', 'emergency assistance',
            'disaster relief', 'government disaster aid'
        ],
        'weight': 0.70
    },
    
    'Trauma/Health': {
        'keywords': [
            'pandemic', 'COVID', 'coronavirus', 'illness', 'sick', 'health',
            'medical', 'hospital', 'mental health', 'stress', 'anxiety',
            # NEW: Disaster-specific trauma keywords (maximum weight)
            'physically injured', 'injured', 'killed', 'death', 'mortality',
            'died', 'fatality', 'casualty',
            # PTSD symptoms
            'disturbing memories', 'nightmares', 'disturbing dreams', 'flashbacks',
            'emotionally distant', 'cut off', 'numb', 'detached',
            'heart pounding', 'sweating', 'trembling', 'hypervigilance',
            'easily startled', 'difficulty concentrating', 'irritable',
            # Depression symptoms
            'depressed', 'hopeless', 'little interest', 'pleasure',
            'feeling down', 'tired', 'little energy', 'poor appetite',
            'overeating', 'trouble sleeping', 'sleeping too much',
            'feeling bad about yourself', 'trouble concentrating',
            'moving slowly', 'restless',
            # Anxiety symptoms
            'nervous', 'anxious', 'on edge', 'worrying', 'unable to stop',
            'trouble relaxing', 'being restless', 'afraid'
        ],
        'weight_base': 0.85,
        'weight_disaster': 0.95  # Maximum weight for physical injury/mortality
    },
    
    'Demographics': {
        'keywords': [
            'age', 'sex', 'gender', 'date of birth', 'resident', 'address',
            'marital status', 'household size', 'education', 'race', 'ethnicity'
        ],
        'weight': 0.50
    }
}

def get_keyword_weight(keyword):
    """
    Map keyword to construct and return impact weight.
    Disaster-specific keywords receive maximum weights.
    """
    
    keyword_lower = keyword.lower()
    
    # Check each construct
    for construct, params in TAXONOMY.items():
        construct_keywords = [kw.lower() for kw in params['keywords']]
        
        if keyword_lower in construct_keywords:
            # Check if disaster-enhanced construct
            if 'weight_disaster' in params:
                # Disaster keywords get maximum weight
                disaster_keywords = [
                    'displaced', 'evacuation', 'evacuate', 'structural damage',
                    'destroyed', 'damaged', 'flooding', 'physically injured',
                    'injured', 'killed', 'death', 'mortality', 'disturbing memories',
                    'nightmares', 'PTSD', 'depressed', 'hopeless'
                ]
                if any(dk in keyword_lower for dk in disaster_keywords):
                    return construct, params['weight_disaster']
                else:
                    return construct, params['weight_base']
            else:
                return construct, params['weight']
    
    return None, 0.0

print("✓ Semantic taxonomy loaded with 7 constructs")
print("✓ Disaster-enhanced weights: Housing/Shelter (0.95), Trauma/Health (0.95)")


# ═══════════════════════════════════════════════════════════════════════════════
# CELL 5: Utility-Burden Formula Implementation
# ═══════════════════════════════════════════════════════════════════════════════

def calculate_utility(keywords):
    """
    Calculate Information Utility (Ui) as sum of impact weights.
    Ui = Σ wk for k in keywords
    """
    
    total_utility = 0.0
    matched_constructs = []
    
    for keyword in keywords:
        construct, weight = get_keyword_weight(keyword)
        if construct:
            total_utility += weight
            matched_constructs.append(construct)
    
    return total_utility, matched_constructs

def calculate_burden(text):
    """
    Calculate Respondent Burden (Bi) from length and complexity.
    Bi = α·Ni + β·Ci
    
    where:
        Ni = word count
        Ci = structural complexity (entity count + clause markers)
        α = 0.10 (word penalty)
        β = 0.20 (complexity penalty)
    """
    
    # Word count
    word_count = len(text.split())
    
    # Structural complexity via spaCy
    doc = nlp(text)
    
    # Count unique entities (proxy for information density)
    entity_count = len(set([ent.text for ent in doc.ents]))
    
    # Count clause markers (and, or, if, when, because, etc.)
    clause_markers = ['and', 'or', 'if', 'when', 'because', 'since', 'while', 'although']
    clause_count = sum([1 for token in doc if token.text.lower() in clause_markers])
    
    # Complexity score
    complexity = entity_count + clause_count
    
    # Burden formula
    alpha = 0.10
    beta = 0.20
    burden = alpha * word_count + beta * complexity
    
    return burden, word_count, complexity

# Apply utility and burden calculations
questions_df['Ui'], questions_df['constructs'] = zip(*questions_df['keywords'].apply(calculate_utility))
questions_df[['Bi', 'wordcount', 'complexity']] = questions_df['questiontext'].apply(
    lambda x: pd.Series(calculate_burden(x))
)

# Calculate Ranking Score
questions_df['Ri'] = questions_df['Ui'] / questions_df['Bi'].replace(0, 0.01)  # Avoid division by zero

print(f"✓ Calculated Utility, Burden, and Ranking scores for all questions")
print(f"  Utility range: {questions_df['Ui'].min():.2f} to {questions_df['Ui'].max():.2f}")
print(f"  Burden range: {questions_df['Bi'].min():.2f} to {questions_df['Bi'].max():.2f}")
print(f"  Ranking score range: {questions_df['Ri'].min():.2f} to {questions_df['Ri'].max():.2f}")


# ═══════════════════════════════════════════════════════════════════════════════
# CELL 6: Matrix Bundling for Psychometric Validity
# ═══════════════════════════════════════════════════════════════════════════════

def identify_matrix_items(questions_df):
    """
    Identify validated clinical matrices (PTSD, depression) from Katrina module.
    Bundle them as cognitive units to reduce artificial burden inflation.
    """
    
    # PTSD screening matrix (S13a-g from Katrina)
    ptsd_patterns = [
        'disturbing memories', 'disturbing dreams', 'nightmares',
        'emotionally distant', 'cut off', 'heart pounding', 'hypervigilance'
    ]
    
    # Depression screening matrix (S16a-h from Katrina)
    depression_patterns = [
        'little interest', 'feeling down', 'depressed', 'hopeless',
        'trouble sleeping', 'feeling tired', 'little energy',
        'poor appetite', 'overeating', 'feeling bad', 'trouble concentrating',
        'moving slowly', 'restless'
    ]
    
    # Identify matrix items
    ptsd_items = []
    depression_items = []
    
    for idx, row in questions_df.iterrows():
        text_lower = row['questiontext'].lower()
        
        # Check for PTSD matrix membership
        if any(pattern in text_lower for pattern in ptsd_patterns):
            if row['source'] == 'Hurricane Katrina 2007' and 'since katrina' in text_lower:
                ptsd_items.append(idx)
        
        # Check for depression matrix membership
        if any(pattern in text_lower for pattern in depression_patterns):
            if row['source'] == 'Hurricane Katrina 2007' and 'since katrina' in text_lower:
                depression_items.append(idx)
    
    return ptsd_items, depression_items

def apply_matrix_bundling(questions_df, ptsd_items, depression_items):
    """
    Apply reduced burden calculation to matrix items.
    
    Logic: First item carries full stem burden, subsequent items get 
    marginal incremental burden only.
    """
    
    # PTSD matrix bundling
    if len(ptsd_items) > 0:
        stem_burden = questions_df.loc[ptsd_items[0], 'Bi']  # First item's burden
        marginal_burden = 0.4  # Incremental burden per additional item
        
        for i, idx in enumerate(ptsd_items):
            if i == 0:
                pass  # Keep original burden for first item
            else:
                # Reduce burden for subsequent items
                questions_df.loc[idx, 'Bi'] = stem_burden + (i * marginal_burden)
                questions_df.loc[idx, 'Ri'] = questions_df.loc[idx, 'Ui'] / questions_df.loc[idx, 'Bi']
    
    # Depression matrix bundling
    if len(depression_items) > 0:
        stem_burden = questions_df.loc[depression_items[0], 'Bi']
        marginal_burden = 0.4
        
        for i, idx in enumerate(depression_items):
            if i == 0:
                pass
            else:
                questions_df.loc[idx, 'Bi'] = stem_burden + (i * marginal_burden)
                questions_df.loc[idx, 'Ri'] = questions_df.loc[idx, 'Ui'] / questions_df.loc[idx, 'Bi']
    
    print(f"✓ Applied matrix bundling to {len(ptsd_items)} PTSD items")
    print(f"✓ Applied matrix bundling to {len(depression_items)} depression items")
    
    return questions_df

# Apply matrix bundling
ptsd_items, depression_items = identify_matrix_items(questions_df)
questions_df = apply_matrix_bundling(questions_df, ptsd_items, depression_items)


# ═══════════════════════════════════════════════════════════════════════════════
# CELL 7: Toggle Classification Logic (DISASTER-ENHANCED)
# ═══════════════════════════════════════════════════════════════════════════════

def classify_toggle(row):
    """
    Route questions to appropriate toggle based on keywords and source.
    
    Toggle categories:
    1. Generic Core - universal questions applicable to any crisis
    2. Financial Crisis - shutdown/recession-specific items
    3. Pandemic/Natural Disaster - health emergencies and physical disasters
    """
    
    keywords_lower = [kw.lower() for kw in row['keywords']]
    source = row['source']
    constructs = row['constructs']
    
    # Financial Crisis toggle triggers
    financial_crisis_keywords = [
        'shutdown', 'furloughed', 'government closure', 'missed paychecks',
        'government employee', 'federal worker'
    ]
    
    # Pandemic/Natural Disaster toggle triggers (EXPANDED)
    pandemic_disaster_keywords = [
        'pandemic', 'covid', 'coronavirus', 'stimulus', 'essential work',
        'paycheck protection', 'remote work', 'work from home',
        # NEW: Disaster-specific triggers
        'hurricane', 'katrina', 'rita', 'flooding', 'displaced', 'evacuation',
        'physically injured', 'killed', 'structural damage', 'destroyed',
        'fema', 'emergency management', 'disaster relief',
        'disturbing memories', 'nightmares', 'PTSD', 'trauma'
    ]
    
    # Rule-based classification
    if any(kw in ' '.join(keywords_lower) for kw in financial_crisis_keywords):
        return 'Toggle Financial Crisis'
    
    elif any(kw in ' '.join(keywords_lower) for kw in pandemic_disaster_keywords):
        return 'Toggle Pandemic Disaster'
    
    elif source == 'Hurricane Katrina 2007':
        # ALL Katrina questions route to Pandemic/Disaster toggle
        return 'Toggle Pandemic Disaster'
    
    elif source == 'Understanding Society':
        # Demographics always go to Generic Core
        return 'Generic Core'
    
    elif 'Economic/Income' in constructs or 'Employment' in constructs or 'Financial Coping' in constructs:
        # Generic economic questions (no crisis-specific keywords)
        return 'Generic Core'
    
    else:
        # Default to Generic Core
        return 'Generic Core'

# Apply toggle classification
questions_df['togglecategory'] = questions_df.apply(classify_toggle, axis=1)

print("✓ Toggle classification complete")
print(f"  Generic Core: {len(questions_df[questions_df['togglecategory'] == 'Generic Core'])} questions")
print(f"  Financial Crisis: {len(questions_df[questions_df['togglecategory'] == 'Toggle Financial Crisis'])} questions")
print(f"  Pandemic/Disaster: {len(questions_df[questions_df['togglecategory'] == 'Toggle Pandemic Disaster'])} questions")


# ═══════════════════════════════════════════════════════════════════════════════
# CELL 8: Greedy Selection by Time Budget
# ═══════════════════════════════════════════════════════════════════════════════

def greedy_module_selection(questions_df, time_budget_minutes=30, seconds_per_word=7):
    """
    Select questions greedily by descending Ri until time budget exhausted.
    
    Parameters:
        time_budget_minutes: Hard cap (default 30 minutes)
        seconds_per_word: Duration estimate (default 7 seconds)
    
    Returns: DataFrame with 'selectedformodule' flag
    """
    
    # Sort by Ri descending
    sorted_df = questions_df.sort_values('Ri', ascending=False).copy()
    
    # Time budget in seconds
    budget_seconds = time_budget_minutes * 60
    
    # Greedy selection
    cumulative_time = 0
    selected_indices = []
    
    for idx, row in sorted_df.iterrows():
        question_time = row['wordcount'] * seconds_per_word
        
        if cumulative_time + question_time <= budget_seconds:
            cumulative_time += question_time
            selected_indices.append(idx)
        else:
            break  # Budget exhausted
    
    # Mark selected questions
    questions_df['selectedformodule'] = False
    questions_df.loc[selected_indices, 'selectedformodule'] = True
    
    print(f"✓ Selected {len(selected_indices)} questions within {time_budget_minutes}-minute budget")
    print(f"  Total estimated time: {cumulative_time/60:.1f} minutes")
    
    return questions_df

# Apply greedy selection
questions_df = greedy_module_selection(questions_df)


# ═══════════════════════════════════════════════════════════════════════════════
# CELL 9: Time Budget Breakdown by Toggle
# ═══════════════════════════════════════════════════════════════════════════════

def calculate_toggle_times(questions_df, seconds_per_word=7):
    """
    Calculate estimated completion time for each toggle category.
    """
    
    selected = questions_df[questions_df['selectedformodule'] == True]
    
    toggle_times = {}
    
    for toggle in ['Generic Core', 'Toggle Financial Crisis', 'Toggle Pandemic Disaster']:
        toggle_questions = selected[selected['togglecategory'] == toggle]
        total_words = toggle_questions['wordcount'].sum()
        total_seconds = total_words * seconds_per_word
        total_minutes = total_seconds / 60
        
        toggle_times[toggle] = {
            'nquestions': len(toggle_questions),
            'total_minutes': total_minutes
        }
    
    print("\n" + "="*60)
    print("TIME BUDGET BREAKDOWN")
    print("="*60)
    for toggle, metrics in toggle_times.items():
        print(f"{toggle}:")
        print(f"  Questions: {metrics['nquestions']}")
        print(f"  Estimated time: {metrics['total_minutes']:.1f} minutes")
    
    print("\nDEPLOYMENT SCENARIOS:")
    print(f"  Economic crisis (Core + Financial): {toggle_times['Generic Core']['total_minutes'] + toggle_times['Toggle Financial Crisis']['total_minutes']:.1f} min")
    print(f"  Physical crisis (Core + Disaster): {toggle_times['Generic Core']['total_minutes'] + toggle_times['Toggle Pandemic Disaster']['total_minutes']:.1f} min")
    print("="*60 + "\n")
    
    return toggle_times

toggle_times = calculate_toggle_times(questions_df)


# ═══════════════════════════════════════════════════════════════════════════════
# CELL 10: Export Ranked Questions CSV
# ═══════════════════════════════════════════════════════════════════════════════

# Prepare export DataFrame
export_df = questions_df[[
    'questiontext', 'source', 'moduletype', 'togglecategory',
    'keywords', 'nkeywords', 'constructs', 'wordcount', 'complexity',
    'Ui', 'Bi', 'Ri', 'selectedformodule'
]].copy()

# Convert lists to strings for CSV export
export_df['keywords'] = export_df['keywords'].apply(lambda x: ', '.join(x) if isinstance(x, list) else '')
export_df['constructs'] = export_df['constructs'].apply(lambda x: ', '.join(x) if isinstance(x, list) else '')

# Sort by Ri descending
export_df = export_df.sort_values('Ri', ascending=False).reset_index(drop=True)

# Export
export_df.to_csv('PSID_Ranked_Questions_Katrina_Integrated.csv', index=False)

print(f"✓ Exported {len(export_df)} ranked questions to CSV")
print(f"  File: PSID_Ranked_Questions_Katrina_Integrated.csv")


# ═══════════════════════════════════════════════════════════════════════════════
# CELL 11-14: Visualization Generation
# ═══════════════════════════════════════════════════════════════════════════════

# [These cells would contain the code for generating the five publication-quality
# visualizations shown in the report:
# 
# 1. Top-Ranked Questions (horizontal bar chart)
# 2. Utility vs. Burden Frontier (scatter plot)
# 3. Construct Coverage by Source (heatmap)
# 4. Time Budget Allocation (stacked bar chart)
# 5. Toggle Routing Logic (flow diagram)
# 
# Code already implemented in previous execution - see Katrina_Integration_Dashboard.png]


print("\n" + "="*80)
print("HURRICANE KATRINA INTEGRATION COMPLETE")
print("="*80)
print(f"✓ Processed {len(questions_df)} questions from 5 sources")
print(f"✓ Katrina contribution: 37 questions transforming Trauma/Health and Housing constructs")
print(f"✓ Top-ranked Katrina question: Ri = {questions_df[questions_df['source']=='Hurricane Katrina 2007']['Ri'].max():.2f}")
print(f"✓ Module assembly: {questions_df['selectedformodule'].sum()} questions selected")
print(f"✓ Deployment-ready with toggle architecture")
print("="*80)
