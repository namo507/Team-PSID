window.PSID_DASHBOARD = {
  "summary": {
    "rows": 52,
    "selected_rows": 28,
    "selected_minutes": 29.98,
    "all_minutes": 68.6,
    "toggle_counts": {
      "Specific": 49,
      "Generic": 3
    },
    "selected_toggle_counts": {
      "Specific": 25,
      "Generic": 3
    },
    "source_counts": {
      "Hurricane Katrina 2007": 37,
      "COVID-19": 8,
      "Govt Shutdown Income": 3,
      "Understanding Society": 3,
      "Govt Shutdown Crisis": 1
    },
    "selected_source_counts": {
      "Hurricane Katrina 2007": 14,
      "COVID-19": 8,
      "Govt Shutdown Income": 3,
      "Understanding Society": 2,
      "Govt Shutdown Crisis": 1
    },
    "construct_counts": {
      "Trauma / Health": 15,
      "Employment": 7,
      "Housing / Shelter": 6,
      "Government Aid": 5,
      "Economic / Income": 4,
      "Financial Coping": 2,
      "Demographics": 2
    },
    "avg_ri": 2.201,
    "max_ri": 5.667,
    "avg_pi": 2.561,
    "max_pi": 7.86,
    "recommended_generic_count": 6,
    "recommended_specific_count": 8
  },
  "rows": [
    {
      "question_text": "Was your home damaged or destroyed by Katrina or Rita?",
      "source": "Hurricane Katrina 2007",
      "toggle_category": "Specific",
      "Ui": 2.65,
      "Bi": 1.0,
      "Ri": 2.65,
      "Pi": 2.266,
      "augmented_utility": 3.276,
      "idf_strength": 3.013,
      "redundancy_penalty": 0.686,
      "construct_bonus": 5.182,
      "word_count": 10,
      "selected": true,
      "constructs": [
        "Housing / Shelter",
        "Trauma / Health"
      ],
      "recommended_wording": "Was your home damaged or destroyed by the disaster?"
    },
    {
      "question_text": "Was your business damaged or destroyed by Katrina or Rita?",
      "source": "Hurricane Katrina 2007",
      "toggle_category": "Specific",
      "Ui": 3.3,
      "Bi": 1.0,
      "Ri": 3.3,
      "Pi": 2.962,
      "augmented_utility": 4.282,
      "idf_strength": 3.107,
      "redundancy_penalty": 0.686,
      "construct_bonus": 7.893,
      "word_count": 10,
      "selected": true,
      "constructs": [
        "Economic / Income",
        "Trauma / Health"
      ],
      "recommended_wording": "Was your business damaged or destroyed by the disaster?"
    },
    {
      "question_text": "Any financial difficulties",
      "source": "COVID-19",
      "toggle_category": "Generic",
      "Ui": 1.7,
      "Bi": 0.3,
      "Ri": 5.667,
      "Pi": 7.187,
      "augmented_utility": 2.742,
      "idf_strength": 3.776,
      "redundancy_penalty": 0.418,
      "construct_bonus": 17.863,
      "word_count": 3,
      "selected": true,
      "constructs": [
        "Financial Coping"
      ],
      "recommended_wording": "Have you experienced any financial difficulties because of the crisis?"
    },
    {
      "question_text": "Lost earnings because of the pandemic",
      "source": "COVID-19",
      "toggle_category": "Generic",
      "Ui": 3.4,
      "Bi": 0.6,
      "Ri": 5.667,
      "Pi": 7.86,
      "augmented_utility": 5.237,
      "idf_strength": 4.196,
      "redundancy_penalty": 0.17,
      "construct_bonus": 7.893,
      "word_count": 6,
      "selected": true,
      "constructs": [
        "Economic / Income",
        "Trauma / Health"
      ],
      "recommended_wording": "Did you lose earnings because of the pandemic?"
    },
    {
      "question_text": "Only work from home",
      "source": "COVID-19",
      "toggle_category": "Specific",
      "Ui": 1.4,
      "Bi": 0.4,
      "Ri": 3.5,
      "Pi": 3.957,
      "augmented_utility": 1.889,
      "idf_strength": 3.629,
      "redundancy_penalty": 0.298,
      "construct_bonus": 7.929,
      "word_count": 4,
      "selected": true,
      "constructs": [
        "Employment"
      ],
      "recommended_wording": "Did you work entirely from home during the crisis?"
    },
    {
      "question_text": "stopped this work?",
      "source": "Govt Shutdown Income",
      "toggle_category": "Specific",
      "Ui": 1.4,
      "Bi": 0.4,
      "Ri": 3.5,
      "Pi": 4.134,
      "augmented_utility": 1.974,
      "idf_strength": 3.911,
      "redundancy_penalty": 0.298,
      "construct_bonus": 7.929,
      "word_count": 4,
      "selected": true,
      "constructs": [
        "Employment"
      ],
      "recommended_wording": "Have you stopped this work because of the crisis?"
    },
    {
      "question_text": "Were/Was there any wages or salarys from this job/these jobs?",
      "source": "Govt Shutdown Income",
      "toggle_category": "Specific",
      "Ui": 3.0,
      "Bi": 1.1,
      "Ri": 2.727,
      "Pi": 4.134,
      "augmented_utility": 4.892,
      "idf_strength": 4.178,
      "redundancy_penalty": 0.117,
      "construct_bonus": 10.784,
      "word_count": 10,
      "selected": true,
      "constructs": [
        "Economic / Income",
        "Employment"
      ],
      "recommended_wording": "Were there any wages or salary payments from this job during the crisis period?"
    },
    {
      "question_text": "Was anyone in your immediate family killed as a result of Katrina or Rita?",
      "source": "Hurricane Katrina 2007",
      "toggle_category": "Specific",
      "Ui": 2.75,
      "Bi": 1.3,
      "Ri": 2.115,
      "Pi": 2.06,
      "augmented_utility": 3.129,
      "idf_strength": 3.331,
      "redundancy_penalty": 0.259,
      "construct_bonus": 2.146,
      "word_count": 13,
      "selected": true,
      "constructs": [
        "Trauma / Health"
      ],
      "recommended_wording": "Was anyone in your immediate family killed as a result of the disaster?"
    },
    {
      "question_text": "Did you experience hurricane force winds at your location during Katrina or Rita?",
      "source": "Hurricane Katrina 2007",
      "toggle_category": "Specific",
      "Ui": 2.7,
      "Bi": 1.3,
      "Ri": 2.077,
      "Pi": 2.106,
      "augmented_utility": 3.167,
      "idf_strength": 3.497,
      "redundancy_penalty": 0.241,
      "construct_bonus": 2.146,
      "word_count": 13,
      "selected": true,
      "constructs": [
        "Trauma / Health"
      ],
      "recommended_wording": "Did you experience hurricane force winds at your location during the disaster?"
    },
    {
      "question_text": "Did you experience major flooding in your home from Katrina or Rita?",
      "source": "Hurricane Katrina 2007",
      "toggle_category": "Specific",
      "Ui": 4.55,
      "Bi": 1.2,
      "Ri": 3.792,
      "Pi": 4.222,
      "augmented_utility": 5.884,
      "idf_strength": 3.28,
      "redundancy_penalty": 0.248,
      "construct_bonus": 5.182,
      "word_count": 12,
      "selected": true,
      "constructs": [
        "Housing / Shelter",
        "Trauma / Health"
      ],
      "recommended_wording": "Did you experience major flooding in your home during the disaster?"
    },
    {
      "question_text": "Received stimulus payment",
      "source": "COVID-19",
      "toggle_category": "Generic",
      "Ui": 1.4,
      "Bi": 0.3,
      "Ri": 4.667,
      "Pi": 6.328,
      "augmented_utility": 2.173,
      "idf_strength": 4.196,
      "redundancy_penalty": 0.222,
      "construct_bonus": 7.989,
      "word_count": 3,
      "selected": true,
      "constructs": [
        "Government Aid"
      ],
      "recommended_wording": "Did you receive a stimulus payment or other emergency government support?"
    },
    {
      "question_text": "Were you physically injured in any way as a result of Katrina or Rita?",
      "source": "Hurricane Katrina 2007",
      "toggle_category": "Specific",
      "Ui": 3.7,
      "Bi": 1.3,
      "Ri": 2.846,
      "Pi": 2.804,
      "augmented_utility": 4.259,
      "idf_strength": 3.394,
      "redundancy_penalty": 0.259,
      "construct_bonus": 2.146,
      "word_count": 13,
      "selected": true,
      "constructs": [
        "Trauma / Health"
      ],
      "recommended_wording": "Were you physically injured in any way as a result of the disaster?"
    },
    {
      "question_text": "How severe was the property damage to your home from Katrina or Rita?",
      "source": "Hurricane Katrina 2007",
      "toggle_category": "Specific",
      "Ui": 3.6,
      "Bi": 1.3,
      "Ri": 2.769,
      "Pi": 3.169,
      "augmented_utility": 4.692,
      "idf_strength": 3.328,
      "redundancy_penalty": 0.214,
      "construct_bonus": 5.182,
      "word_count": 13,
      "selected": true,
      "constructs": [
        "Housing / Shelter",
        "Trauma / Health"
      ],
      "recommended_wording": "How severe was the damage to your home during the disaster?"
    },
    {
      "question_text": "Since Katrina and Rita, how often have you been bothered by feeling down depressed or hopeless?",
      "source": "Hurricane Katrina 2007",
      "toggle_category": "Specific",
      "Ui": 1.8,
      "Bi": 1.8,
      "Ri": 1.0,
      "Pi": 0.832,
      "augmented_utility": 1.941,
      "idf_strength": 3.053,
      "redundancy_penalty": 0.454,
      "construct_bonus": 2.146,
      "word_count": 16,
      "selected": false,
      "constructs": [
        "Trauma / Health"
      ],
      "recommended_wording": "Since the disaster, how often have you been bothered by feeling down depressed or hopeless?"
    },
    {
      "question_text": "How afraid were you during Katrina or Rita that you might be killed or seriously injured?",
      "source": "Hurricane Katrina 2007",
      "toggle_category": "Specific",
      "Ui": 4.65,
      "Bi": 1.9,
      "Ri": 2.447,
      "Pi": 2.584,
      "augmented_utility": 5.389,
      "idf_strength": 3.431,
      "redundancy_penalty": 0.15,
      "construct_bonus": 2.146,
      "word_count": 16,
      "selected": true,
      "constructs": [
        "Trauma / Health"
      ],
      "recommended_wording": "How afraid were you during the disaster that you might be seriously injured or killed?"
    },
    {
      "question_text": "Working in a job that was considered essential work?",
      "source": "COVID-19",
      "toggle_category": "Specific",
      "Ui": 3.6,
      "Bi": 0.9,
      "Ri": 4.0,
      "Pi": 5.223,
      "augmented_utility": 5.205,
      "idf_strength": 4.078,
      "redundancy_penalty": 0.165,
      "construct_bonus": 7.929,
      "word_count": 9,
      "selected": true,
      "constructs": [
        "Employment"
      ],
      "recommended_wording": "Were you working in a job that was considered essential during the crisis?"
    },
    {
      "question_text": "Since Katrina and Rita, have you been bothered by repeated disturbing memories thoughts or images of the hurricane?",
      "source": "Hurricane Katrina 2007",
      "toggle_category": "Specific",
      "Ui": 3.65,
      "Bi": 2.0,
      "Ri": 1.825,
      "Pi": 1.588,
      "augmented_utility": 4.23,
      "idf_strength": 3.43,
      "redundancy_penalty": 0.51,
      "construct_bonus": 2.146,
      "word_count": 18,
      "selected": true,
      "constructs": [
        "Trauma / Health"
      ],
      "recommended_wording": "Since the disaster, how often have you had disturbing memories or images about what happened?"
    },
    {
      "question_text": "How did you/your family manage any financial difficulties due to the shutdown - sell your belongings?",
      "source": "Govt Shutdown Crisis",
      "toggle_category": "Specific",
      "Ui": 5.95,
      "Bi": 1.6,
      "Ri": 3.719,
      "Pi": 4.592,
      "augmented_utility": 9.343,
      "idf_strength": 4.017,
      "redundancy_penalty": 0.418,
      "construct_bonus": 13.006,
      "word_count": 16,
      "selected": true,
      "constructs": [
        "Financial Coping",
        "Government Aid"
      ],
      "recommended_wording": "How did your household manage financial difficulties caused by the shutdown or crisis?"
    },
    {
      "question_text": "stopped working at this business?",
      "source": "Govt Shutdown Income",
      "toggle_category": "Specific",
      "Ui": 2.25,
      "Bi": 0.6,
      "Ri": 3.75,
      "Pi": 5.177,
      "augmented_utility": 3.6,
      "idf_strength": 4.034,
      "redundancy_penalty": 0.244,
      "construct_bonus": 10.784,
      "word_count": 6,
      "selected": true,
      "constructs": [
        "Economic / Income",
        "Employment"
      ],
      "recommended_wording": "Have you stopped working at this business because of the crisis?"
    },
    {
      "question_text": "Paycheck protection",
      "source": "COVID-19",
      "toggle_category": "Specific",
      "Ui": 0.7,
      "Bi": 0.2,
      "Ri": 3.5,
      "Pi": 5.212,
      "augmented_utility": 1.042,
      "idf_strength": 4.277,
      "redundancy_penalty": 0.0,
      "construct_bonus": 7.989,
      "word_count": 2,
      "selected": true,
      "constructs": [
        "Government Aid"
      ],
      "recommended_wording": "Did you receive paycheck protection or other emergency business support?"
    },
    {
      "question_text": "Stimulus payments",
      "source": "COVID-19",
      "toggle_category": "Specific",
      "Ui": 0.7,
      "Bi": 0.2,
      "Ri": 3.5,
      "Pi": 4.466,
      "augmented_utility": 1.022,
      "idf_strength": 4.142,
      "redundancy_penalty": 0.222,
      "construct_bonus": 7.989,
      "word_count": 2,
      "selected": true,
      "constructs": [
        "Government Aid"
      ],
      "recommended_wording": "Did you receive a stimulus payment or other emergency government support?"
    },
    {
      "question_text": "Since Katrina and Rita, have you felt nervous anxious or on edge?",
      "source": "Hurricane Katrina 2007",
      "toggle_category": "Specific",
      "Ui": 1.8,
      "Bi": 1.4,
      "Ri": 1.286,
      "Pi": 1.287,
      "augmented_utility": 2.066,
      "idf_strength": 3.378,
      "redundancy_penalty": 0.225,
      "construct_bonus": 2.146,
      "word_count": 12,
      "selected": false,
      "constructs": [
        "Trauma / Health"
      ],
      "recommended_wording": "Since the disaster, have you felt nervous anxious or on edge?"
    },
    {
      "question_text": "Since Katrina and Rita, have you been bothered by repeated disturbing dreams about the hurricane?",
      "source": "Hurricane Katrina 2007",
      "toggle_category": "Specific",
      "Ui": 2.7,
      "Bi": 1.7,
      "Ri": 1.588,
      "Pi": 1.316,
      "augmented_utility": 2.979,
      "idf_strength": 3.17,
      "redundancy_penalty": 0.51,
      "construct_bonus": 2.146,
      "word_count": 15,
      "selected": false,
      "constructs": [
        "Trauma / Health"
      ],
      "recommended_wording": "Since the disaster, how often have you had disturbing dreams about what happened?"
    },
    {
      "question_text": "How long did you stay in temporary housing after Katrina or Rita?",
      "source": "Hurricane Katrina 2007",
      "toggle_category": "Specific",
      "Ui": 2.7,
      "Bi": 1.1,
      "Ri": 2.455,
      "Pi": 3.09,
      "augmented_utility": 3.614,
      "idf_strength": 3.492,
      "redundancy_penalty": 0.097,
      "construct_bonus": 5.182,
      "word_count": 11,
      "selected": true,
      "constructs": [
        "Housing / Shelter",
        "Trauma / Health"
      ],
      "recommended_wording": "How long did you stay in temporary housing after the disaster?"
    },
    {
      "question_text": "Can I just check, are you normally resident at this address?",
      "source": "Understanding Society",
      "toggle_category": "Specific",
      "Ui": 1.4,
      "Bi": 1.2,
      "Ri": 1.167,
      "Pi": 1.908,
      "augmented_utility": 2.289,
      "idf_strength": 4.277,
      "redundancy_penalty": 0.0,
      "construct_bonus": 17.553,
      "word_count": 11,
      "selected": false,
      "constructs": [
        "Demographics"
      ],
      "recommended_wording": "Are you currently living at this address?"
    },
    {
      "question_text": "Since Katrina and Rita, have you had trouble relaxing?",
      "source": "Hurricane Katrina 2007",
      "toggle_category": "Specific",
      "Ui": 1.8,
      "Bi": 1.2,
      "Ri": 1.5,
      "Pi": 1.4,
      "augmented_utility": 1.907,
      "idf_strength": 2.964,
      "redundancy_penalty": 0.208,
      "construct_bonus": 2.146,
      "word_count": 10,
      "selected": false,
      "constructs": [
        "Trauma / Health"
      ],
      "recommended_wording": "Since the disaster, have you had trouble relaxing?"
    },
    {
      "question_text": "Since Katrina and Rita, have you felt your heart pounding or racing?",
      "source": "Hurricane Katrina 2007",
      "toggle_category": "Specific",
      "Ui": 1.8,
      "Bi": 1.5,
      "Ri": 1.2,
      "Pi": 1.201,
      "augmented_utility": 2.066,
      "idf_strength": 3.378,
      "redundancy_penalty": 0.225,
      "construct_bonus": 2.146,
      "word_count": 13,
      "selected": false,
      "constructs": [
        "Trauma / Health"
      ],
      "recommended_wording": "Since the disaster, have you felt your heart pounding or racing?"
    },
    {
      "question_text": "Since Katrina and Rita, have you been unable to stop or control worrying?",
      "source": "Hurricane Katrina 2007",
      "toggle_category": "Specific",
      "Ui": 1.8,
      "Bi": 1.5,
      "Ri": 1.2,
      "Pi": 1.261,
      "augmented_utility": 2.1,
      "idf_strength": 3.468,
      "redundancy_penalty": 0.171,
      "construct_bonus": 2.146,
      "word_count": 13,
      "selected": false,
      "constructs": [
        "Trauma / Health"
      ],
      "recommended_wording": "Since the disaster, have you been unable to stop or control worrying?"
    },
    {
      "question_text": "Did you evacuate from your home before Katrina or Rita hit?",
      "source": "Hurricane Katrina 2007",
      "toggle_category": "Specific",
      "Ui": 3.55,
      "Bi": 1.1,
      "Ri": 3.227,
      "Pi": 3.53,
      "augmented_utility": 4.509,
      "idf_strength": 3.173,
      "redundancy_penalty": 0.248,
      "construct_bonus": 5.182,
      "word_count": 11,
      "selected": true,
      "constructs": [
        "Housing / Shelter",
        "Trauma / Health"
      ],
      "recommended_wording": "Did you evacuate from your home before the disaster hit?"
    },
    {
      "question_text": "Did you lose your job because of Katrina or Rita?",
      "source": "Hurricane Katrina 2007",
      "toggle_category": "Specific",
      "Ui": 3.2,
      "Bi": 1.0,
      "Ri": 3.2,
      "Pi": 3.708,
      "augmented_utility": 3.989,
      "idf_strength": 3.066,
      "redundancy_penalty": 0.117,
      "construct_bonus": 5.117,
      "word_count": 10,
      "selected": true,
      "constructs": [
        "Employment",
        "Trauma / Health"
      ],
      "recommended_wording": "Did the disaster cause you to lose your job?"
    },
    {
      "question_text": "Laid off or furloughed because of the pandemic",
      "source": "COVID-19",
      "toggle_category": "Specific",
      "Ui": 2.55,
      "Bi": 1.1,
      "Ri": 2.318,
      "Pi": 3.106,
      "augmented_utility": 3.794,
      "idf_strength": 4.196,
      "redundancy_penalty": 0.17,
      "construct_bonus": 5.117,
      "word_count": 8,
      "selected": true,
      "constructs": [
        "Employment",
        "Trauma / Health"
      ],
      "recommended_wording": "Were you laid off or furloughed because of the pandemic?"
    },
    {
      "question_text": "Were you displaced from the place you were living because of Katrina or Rita?",
      "source": "Hurricane Katrina 2007",
      "toggle_category": "Specific",
      "Ui": 2.75,
      "Bi": 1.3,
      "Ri": 2.115,
      "Pi": 2.643,
      "augmented_utility": 3.587,
      "idf_strength": 3.333,
      "redundancy_penalty": 0.068,
      "construct_bonus": 5.182,
      "word_count": 13,
      "selected": true,
      "constructs": [
        "Housing / Shelter",
        "Trauma / Health"
      ],
      "recommended_wording": "Were you displaced from the place you were living because of the disaster?"
    },
    {
      "question_text": "Since Katrina and Rita, how often have you been bothered by little interest or pleasure in doing things?",
      "source": "Hurricane Katrina 2007",
      "toggle_category": "Specific",
      "Ui": 1.8,
      "Bi": 2.0,
      "Ri": 0.9,
      "Pi": 0.877,
      "augmented_utility": 2.022,
      "idf_strength": 3.263,
      "redundancy_penalty": 0.236,
      "construct_bonus": 2.146,
      "word_count": 18,
      "selected": false,
      "constructs": [
        "Trauma / Health"
      ],
      "recommended_wording": "Since the disaster, how often have you been bothered by little interest or pleasure in doing things?"
    },
    {
      "question_text": "How much financial help did you receive from FEMA?",
      "source": "Hurricane Katrina 2007",
      "toggle_category": "Specific",
      "Ui": 1.5,
      "Bi": 0.9,
      "Ri": 1.667,
      "Pi": 2.057,
      "augmented_utility": 2.265,
      "idf_strength": 3.735,
      "redundancy_penalty": 0.343,
      "construct_bonus": 13.006,
      "word_count": 9,
      "selected": false,
      "constructs": [
        "Financial Coping",
        "Government Aid"
      ],
      "recommended_wording": "Did you receive emergency financial assistance because of the disaster?"
    },
    {
      "question_text": "Since Katrina and Rita, how often have you been bothered by poor appetite or overeating?",
      "source": "Hurricane Katrina 2007",
      "toggle_category": "Specific",
      "Ui": 1.8,
      "Bi": 1.7,
      "Ri": 1.059,
      "Pi": 0.679,
      "augmented_utility": 1.904,
      "idf_strength": 2.958,
      "redundancy_penalty": 1.0,
      "construct_bonus": 2.146,
      "word_count": 15,
      "selected": false,
      "constructs": [
        "Trauma / Health"
      ],
      "recommended_wording": "Since the disaster, how often have you been bothered by poor appetite or overeating?"
    },
    {
      "question_text": "Since Katrina and Rita, have you felt emotionally distant or cut off from other people?",
      "source": "Hurricane Katrina 2007",
      "toggle_category": "Specific",
      "Ui": 1.8,
      "Bi": 1.7,
      "Ri": 1.059,
      "Pi": 1.103,
      "augmented_utility": 2.119,
      "idf_strength": 3.517,
      "redundancy_penalty": 0.201,
      "construct_bonus": 2.146,
      "word_count": 15,
      "selected": false,
      "constructs": [
        "Trauma / Health"
      ],
      "recommended_wording": "Since the disaster, have you felt emotionally distant or cut off from other people?"
    },
    {
      "question_text": "Since Katrina and Rita, how often have you been bothered by poor appetite or overeating?",
      "source": "Hurricane Katrina 2007",
      "toggle_category": "Specific",
      "Ui": 1.8,
      "Bi": 1.7,
      "Ri": 1.059,
      "Pi": 0.679,
      "augmented_utility": 1.904,
      "idf_strength": 2.958,
      "redundancy_penalty": 1.0,
      "construct_bonus": 2.146,
      "word_count": 15,
      "selected": false,
      "constructs": [
        "Trauma / Health"
      ],
      "recommended_wording": "Since the disaster, how often have you been bothered by poor appetite or overeating?"
    },
    {
      "question_text": "Since Katrina and Rita, how often have you been bothered by feeling bad about yourself?",
      "source": "Hurricane Katrina 2007",
      "toggle_category": "Specific",
      "Ui": 1.8,
      "Bi": 1.7,
      "Ri": 1.059,
      "Pi": 0.834,
      "augmented_utility": 1.836,
      "idf_strength": 2.781,
      "redundancy_penalty": 0.454,
      "construct_bonus": 2.146,
      "word_count": 15,
      "selected": false,
      "constructs": [
        "Trauma / Health"
      ],
      "recommended_wording": "Since the disaster, how often have you been bothered by feeling bad about yourself?"
    },
    {
      "question_text": "Since Katrina and Rita, how often have you been bothered by trouble concentrating on things?",
      "source": "Hurricane Katrina 2007",
      "toggle_category": "Specific",
      "Ui": 1.8,
      "Bi": 1.7,
      "Ri": 1.059,
      "Pi": 0.942,
      "augmented_utility": 1.927,
      "idf_strength": 3.016,
      "redundancy_penalty": 0.313,
      "construct_bonus": 2.146,
      "word_count": 15,
      "selected": false,
      "constructs": [
        "Trauma / Health"
      ],
      "recommended_wording": "Since the disaster, how often have you been bothered by trouble concentrating on things?"
    },
    {
      "question_text": "Overall how would you rate the impact of Katrina or Rita on your family?",
      "source": "Hurricane Katrina 2007",
      "toggle_category": "Specific",
      "Ui": 1.8,
      "Bi": 1.4,
      "Ri": 1.286,
      "Pi": 1.373,
      "augmented_utility": 2.09,
      "idf_strength": 3.441,
      "redundancy_penalty": 0.134,
      "construct_bonus": 2.146,
      "word_count": 14,
      "selected": false,
      "constructs": [
        "Trauma / Health"
      ],
      "recommended_wording": "Overall how would you rate the impact of the disaster on your family?"
    },
    {
      "question_text": "Have you been able to return to your original home?",
      "source": "Hurricane Katrina 2007",
      "toggle_category": "Specific",
      "Ui": 0.85,
      "Bi": 1.0,
      "Ri": 0.85,
      "Pi": 1.137,
      "augmented_utility": 1.234,
      "idf_strength": 4.098,
      "redundancy_penalty": 0.132,
      "construct_bonus": 8.059,
      "word_count": 10,
      "selected": false,
      "constructs": [
        "Housing / Shelter"
      ],
      "recommended_wording": "Have you been able to return to your original home?"
    },
    {
      "question_text": "Calculate respondents age",
      "source": "Understanding Society",
      "toggle_category": "Specific",
      "Ui": 0.5,
      "Bi": 0.3,
      "Ri": 1.667,
      "Pi": 2.725,
      "augmented_utility": 0.818,
      "idf_strength": 4.277,
      "redundancy_penalty": 0.0,
      "construct_bonus": 17.553,
      "word_count": 3,
      "selected": true,
      "constructs": [
        "Demographics"
      ],
      "recommended_wording": "What is your age in years?"
    },
    {
      "question_text": "Since Katrina and Rita, how often have you been bothered by trouble falling or staying asleep or sleeping too much?",
      "source": "Hurricane Katrina 2007",
      "toggle_category": "Specific",
      "Ui": 1.8,
      "Bi": 2.2,
      "Ri": 0.818,
      "Pi": 0.783,
      "augmented_utility": 2.074,
      "idf_strength": 3.398,
      "redundancy_penalty": 0.313,
      "construct_bonus": 2.146,
      "word_count": 20,
      "selected": false,
      "constructs": [
        "Trauma / Health"
      ],
      "recommended_wording": "Since the disaster, how often have you been bothered by trouble falling or staying asleep or sleeping too much?"
    },
    {
      "question_text": "How many days were you without electricity after Katrina or Rita?",
      "source": "Hurricane Katrina 2007",
      "toggle_category": "Specific",
      "Ui": 1.8,
      "Bi": 1.1,
      "Ri": 1.636,
      "Pi": 1.521,
      "augmented_utility": 1.922,
      "idf_strength": 3.005,
      "redundancy_penalty": 0.229,
      "construct_bonus": 2.146,
      "word_count": 11,
      "selected": false,
      "constructs": [
        "Trauma / Health"
      ],
      "recommended_wording": "How many days were you without electricity after the disaster?"
    },
    {
      "question_text": "How many days were you without running water after Katrina or Rita?",
      "source": "Hurricane Katrina 2007",
      "toggle_category": "Specific",
      "Ui": 1.8,
      "Bi": 1.1,
      "Ri": 1.636,
      "Pi": 1.607,
      "augmented_utility": 2.031,
      "idf_strength": 3.288,
      "redundancy_penalty": 0.229,
      "construct_bonus": 2.146,
      "word_count": 11,
      "selected": false,
      "constructs": [
        "Trauma / Health"
      ],
      "recommended_wording": "How many days were you without running water after the disaster?"
    },
    {
      "question_text": "Did you receive any help from FEMA Federal Emergency Management Agency?",
      "source": "Hurricane Katrina 2007",
      "toggle_category": "Specific",
      "Ui": 2.0,
      "Bi": 1.1,
      "Ri": 1.818,
      "Pi": 2.027,
      "augmented_utility": 2.727,
      "idf_strength": 3.971,
      "redundancy_penalty": 0.343,
      "construct_bonus": 7.989,
      "word_count": 11,
      "selected": true,
      "constructs": [
        "Government Aid"
      ],
      "recommended_wording": "Did you receive any help from FEMA Federal Emergency Management Agency?"
    },
    {
      "question_text": "Since Katrina and Rita, have you been worrying too much about different things?",
      "source": "Hurricane Katrina 2007",
      "toggle_category": "Specific",
      "Ui": 1.8,
      "Bi": 1.5,
      "Ri": 1.2,
      "Pi": 1.186,
      "augmented_utility": 1.984,
      "idf_strength": 3.166,
      "redundancy_penalty": 0.178,
      "construct_bonus": 2.146,
      "word_count": 13,
      "selected": false,
      "constructs": [
        "Trauma / Health"
      ],
      "recommended_wording": "Since the disaster, have you been worrying too much about different things?"
    },
    {
      "question_text": "Did you have to move to a different city or state because of Katrina or Rita?",
      "source": "Hurricane Katrina 2007",
      "toggle_category": "Specific",
      "Ui": 1.8,
      "Bi": 1.5,
      "Ri": 1.2,
      "Pi": 1.22,
      "augmented_utility": 2.041,
      "idf_strength": 3.313,
      "redundancy_penalty": 0.178,
      "construct_bonus": 2.146,
      "word_count": 15,
      "selected": false,
      "constructs": [
        "Trauma / Health"
      ],
      "recommended_wording": "Did you have to move to a different city or state because of the disaster?"
    },
    {
      "question_text": "Since Katrina and Rita, how often have you been bothered by feeling tired or having little energy?",
      "source": "Hurricane Katrina 2007",
      "toggle_category": "Specific",
      "Ui": 1.8,
      "Bi": 1.9,
      "Ri": 0.947,
      "Pi": 0.877,
      "augmented_utility": 2.056,
      "idf_strength": 3.352,
      "redundancy_penalty": 0.36,
      "construct_bonus": 2.146,
      "word_count": 17,
      "selected": false,
      "constructs": [
        "Trauma / Health"
      ],
      "recommended_wording": "Since the disaster, how often have you been bothered by feeling tired or having little energy?"
    },
    {
      "question_text": "Since Katrina and Rita, how often have you been bothered by moving or speaking slowly or being restless?",
      "source": "Hurricane Katrina 2007",
      "toggle_category": "Specific",
      "Ui": 1.8,
      "Bi": 1.9,
      "Ri": 0.947,
      "Pi": 0.979,
      "augmented_utility": 2.054,
      "idf_strength": 3.348,
      "redundancy_penalty": 0.161,
      "construct_bonus": 2.146,
      "word_count": 17,
      "selected": false,
      "constructs": [
        "Trauma / Health"
      ],
      "recommended_wording": "Since the disaster, how often have you been bothered by moving or speaking slowly or being restless?"
    },
    {
      "question_text": "Did you receive help from other government agencies or nonprofit organizations?",
      "source": "Hurricane Katrina 2007",
      "toggle_category": "Specific",
      "Ui": 1.2,
      "Bi": 1.1,
      "Ri": 1.091,
      "Pi": 1.312,
      "augmented_utility": 1.704,
      "idf_strength": 3.955,
      "redundancy_penalty": 0.278,
      "construct_bonus": 7.989,
      "word_count": 11,
      "selected": false,
      "constructs": [
        "Government Aid"
      ],
      "recommended_wording": "Did you receive help from other government agencies or nonprofit organizations?"
    },
    {
      "question_text": "And are you... 1. Male 2. Female",
      "source": "Understanding Society",
      "toggle_category": "Specific",
      "Ui": 1.35,
      "Bi": 1.1,
      "Ri": 1.227,
      "Pi": 1.933,
      "augmented_utility": 2.127,
      "idf_strength": 4.277,
      "redundancy_penalty": 0.0,
      "construct_bonus": 17.553,
      "word_count": 7,
      "selected": true,
      "constructs": [
        "Demographics"
      ],
      "recommended_wording": "How do you describe your sex or gender?"
    }
  ],
  "recommendations": {
    "generic": [
      {
        "module": "Generic",
        "title": "Financial strain flag",
        "question": "Have you experienced any financial difficulties because of the crisis?",
        "constructs": [
          "Financial Coping"
        ],
        "why_it_matters": "A compact cross-crisis screener that activates downstream coping and aid questions without wasting time on respondents unaffected financially.",
        "support_score": 5.889,
        "supporting_sources": [
          "COVID-19",
          "Govt Shutdown Crisis"
        ],
        "supporting_examples": [
          "Have you experienced any financial difficulties because of the crisis?",
          "How did your household manage financial difficulties caused by the shutdown or crisis?"
        ]
      },
      {
        "module": "Generic",
        "title": "Income continuity",
        "question": "Were there any wages or salary payments from this job during the crisis period?",
        "constructs": [
          "Employment",
          "Economic / Income"
        ],
        "why_it_matters": "Links employment status to realized income loss, which is more informative than demographics alone for a generic always-on core.",
        "support_score": 5.736,
        "supporting_sources": [
          "COVID-19",
          "Govt Shutdown Income"
        ],
        "supporting_examples": [
          "Did you lose earnings because of the pandemic?",
          "Did you receive paycheck protection or other emergency business support?"
        ]
      },
      {
        "module": "Generic",
        "title": "Government assistance",
        "question": "Did you receive any government financial assistance because of the crisis?",
        "constructs": [
          "Government Aid"
        ],
        "why_it_matters": "Captures public support exposure in a reusable way without tying the wording to one historical event or program.",
        "support_score": 5.335,
        "supporting_sources": [
          "COVID-19"
        ],
        "supporting_examples": [
          "Did you receive a stimulus payment or other emergency government support?",
          "Did you receive paycheck protection or other emergency business support?"
        ]
      },
      {
        "module": "Generic",
        "title": "Work interruption",
        "question": "Have you stopped this work because of the crisis?",
        "constructs": [
          "Employment"
        ],
        "why_it_matters": "Preserves one of the strongest employment disruption signals while remaining portable across shutdowns, disasters, and public-health emergencies.",
        "support_score": 4.139,
        "supporting_sources": [
          "COVID-19",
          "Govt Shutdown Income"
        ],
        "supporting_examples": [
          "Have you stopped working at this business because of the crisis?",
          "Have you stopped this work because of the crisis?"
        ]
      },
      {
        "module": "Generic",
        "title": "Housing instability",
        "question": "Did your household fall behind on rent, mortgage, utilities, or other major bills because of the crisis?",
        "constructs": [
          "Housing / Shelter",
          "Economic / Income"
        ],
        "why_it_matters": "Adds meaningful household vulnerability context that is much more actionable than a pure demographic check.",
        "support_score": 1.557,
        "supporting_sources": [
          "Hurricane Katrina 2007"
        ],
        "supporting_examples": [
          "Was your home damaged or destroyed by the disaster?",
          "Did you have to move to a different city or state because of the disaster?"
        ]
      },
      {
        "module": "Generic",
        "title": "Wellbeing check",
        "question": "Since the crisis, how often have you felt worried, unable to relax, or unable to sleep well?",
        "constructs": [
          "Trauma / Health"
        ],
        "why_it_matters": "A condensed wellbeing item keeps the generic core from being reduced to only demographics and labor-market questions.",
        "support_score": 1.416,
        "supporting_sources": [
          "Hurricane Katrina 2007"
        ],
        "supporting_examples": [
          "Since the disaster, how often have you had disturbing memories or images about what happened?",
          "Since the disaster, have you had trouble relaxing?"
        ]
      }
    ],
    "specific": [
      {
        "module": "Specific",
        "title": "Pandemic earnings loss",
        "question": "Did you lose earnings because of the pandemic?",
        "constructs": [
          "Economic / Income"
        ],
        "why_it_matters": "High-yield pandemic item that directly captures the core economic shock from public-health restrictions.",
        "support_score": 5.483,
        "supporting_sources": [
          "COVID-19"
        ],
        "supporting_examples": [
          "Did you lose earnings because of the pandemic?",
          "Were you laid off or furloughed because of the pandemic?"
        ]
      },
      {
        "module": "Specific",
        "title": "Emergency payment receipt",
        "question": "Did you receive a stimulus payment or other emergency government support?",
        "constructs": [
          "Government Aid"
        ],
        "why_it_matters": "Keeps the assistance signal but generalizes it beyond one named program, making the item reusable.",
        "support_score": 5.335,
        "supporting_sources": [
          "COVID-19"
        ],
        "supporting_examples": [
          "Did you receive a stimulus payment or other emergency government support?",
          "Did you receive paycheck protection or other emergency business support?"
        ]
      },
      {
        "module": "Specific",
        "title": "Financial coping strategy",
        "question": "How did your household manage financial difficulties caused by the shutdown or crisis?",
        "constructs": [
          "Financial Coping"
        ],
        "why_it_matters": "Maintains the strongest scored shutdown item while making the wording cleaner and easier to field.",
        "support_score": 4.592,
        "supporting_sources": [
          "Govt Shutdown Crisis"
        ],
        "supporting_examples": [
          "How did your household manage financial difficulties caused by the shutdown or crisis?"
        ]
      },
      {
        "module": "Specific",
        "title": "Essential work exposure",
        "question": "Were you working in a job that was considered essential during the crisis?",
        "constructs": [
          "Employment"
        ],
        "why_it_matters": "Distinguishes frontline disruption from remote-capable employment and strengthens interpretation of labor-market exposure.",
        "support_score": 4.59,
        "supporting_sources": [
          "COVID-19"
        ],
        "supporting_examples": [
          "Were you working in a job that was considered essential during the crisis?",
          "Did you work entirely from home during the crisis?"
        ]
      },
      {
        "module": "Specific",
        "title": "Evacuation",
        "question": "Did you evacuate from your home before the disaster hit?",
        "constructs": [
          "Housing / Shelter"
        ],
        "why_it_matters": "One of the cleanest disaster-routing questions and a strong marker of direct exposure.",
        "support_score": 3.53,
        "supporting_sources": [
          "Hurricane Katrina 2007"
        ],
        "supporting_examples": [
          "Did you evacuate from your home before the disaster hit?"
        ]
      },
      {
        "module": "Specific",
        "title": "Home damage severity",
        "question": "How severe was the damage to your home during the disaster?",
        "constructs": [
          "Housing / Shelter"
        ],
        "why_it_matters": "Converts detailed Katrina evidence into a portable housing-impact severity item.",
        "support_score": 3.219,
        "supporting_sources": [
          "Hurricane Katrina 2007"
        ],
        "supporting_examples": [
          "Did you experience major flooding in your home during the disaster?",
          "How severe was the damage to your home during the disaster?"
        ]
      },
      {
        "module": "Specific",
        "title": "Temporary housing",
        "question": "How long did you stay in temporary housing after the disaster?",
        "constructs": [
          "Housing / Shelter"
        ],
        "why_it_matters": "Captures longer-run displacement burden that simple yes/no housing items can miss.",
        "support_score": 2.318,
        "supporting_sources": [
          "Hurricane Katrina 2007"
        ],
        "supporting_examples": [
          "How long did you stay in temporary housing after the disaster?",
          "Were you displaced from the place you were living because of the disaster?"
        ]
      },
      {
        "module": "Specific",
        "title": "Disaster distress",
        "question": "Since the disaster, how often have you had disturbing memories or dreams about what happened?",
        "constructs": [
          "Trauma / Health"
        ],
        "why_it_matters": "Condenses multiple trauma items into one deployable distress signal while preserving the strongest construct evidence.",
        "support_score": 1.452,
        "supporting_sources": [
          "Hurricane Katrina 2007"
        ],
        "supporting_examples": [
          "Since the disaster, how often have you had disturbing memories or images about what happened?",
          "Since the disaster, how often have you had disturbing dreams about what happened?"
        ]
      }
    ]
  }
};
