"""Utility helpers for the PSID crisis-module notebook.

This module exposes reusable keyword extraction, tagging, scoring, and
classification helpers for the Katrina-integrated ranked-question dataset.
It is designed to be safe to import from a notebook without triggering any
file I/O or long-running pipeline execution at import time.
"""

from __future__ import annotations

import ast
import re
from functools import lru_cache
from typing import Any

import pandas as pd

try:
    import nltk
except ModuleNotFoundError:  # pragma: no cover - handled at runtime
    nltk = None

try:
    import spacy
except ModuleNotFoundError:  # pragma: no cover - handled at runtime
    spacy = None

try:
    from rake_nltk import Rake
except ModuleNotFoundError:  # pragma: no cover - handled at runtime
    Rake = None


ALPHA = 0.10
BETA = 0.20
SECS_PER_WORD = 7
MAX_SECONDS = 30 * 60
IDEAL_SECONDS = 15 * 60

CSV_PATH = "/Users/namomac/Team-PSID/PSID_Ranked_Questions_Katrina_Integrated.csv"

COLUMN_RENAME_MAP = {
    "questiontext": "question_text",
    "moduletype": "module_type",
    "togglecategory": "toggle_category",
    "nkeywords": "n_keywords",
    "ntagged": "n_tagged",
    "wordcount": "word_count",
    "selectedformodule": "selected_for_module",
}

SOURCE_TO_CRISIS_ORIGIN = {
    "Govt Shutdown Income": "Shutdown 2019",
    "Govt Shutdown Crisis": "Shutdown 2019",
    "Govt Shutdown (Income)": "Shutdown 2019",
    "Govt Shutdown (Crisis)": "Shutdown 2019",
    "COVID-19": "COVID-19 2021",
    "Understanding Society": "Understanding Society",
    "Hurricane Katrina 2007": "Hurricane Katrina 2005",
}

TOGGLE_LABEL_MAP = {
    "Toggle Financial Crisis": "Toggle: Financial Crisis",
    "Toggle Pandemic Disaster": "Toggle: Pandemic / Disaster",
}

TAXONOMY: dict[str, tuple[str, float]] = {
    "income": ("Economic / Income", 0.80),
    "net income": ("Economic / Income", 0.80),
    "earnings": ("Economic / Income", 0.80),
    "wages": ("Economic / Income", 0.80),
    "salary": ("Economic / Income", 0.80),
    "salaries": ("Economic / Income", 0.80),
    "receipts": ("Economic / Income", 0.80),
    "operating expenses": ("Economic / Income", 0.80),
    "bonuses": ("Economic / Income", 0.80),
    "overtime": ("Economic / Income", 0.80),
    "tips": ("Economic / Income", 0.80),
    "commissions": ("Economic / Income", 0.80),
    "lost earnings": ("Economic / Income", 0.80),
    "financial interest": ("Economic / Income", 0.80),
    "business": ("Economic / Income", 0.75),
    "furloughed": ("Employment", 0.75),
    "laid off": ("Employment", 0.75),
    "working": ("Employment", 0.70),
    "work": ("Employment", 0.70),
    "job": ("Employment", 0.70),
    "essential work": ("Employment", 0.75),
    "stopped working": ("Employment", 0.75),
    "employer": ("Employment", 0.70),
    "quit": ("Employment", 0.70),
    "work time": ("Employment", 0.70),
    "hours": ("Employment", 0.65),
    "weeks": ("Employment", 0.65),
    "savings": ("Financial Coping", 0.85),
    "credit card": ("Financial Coping", 0.85),
    "retirement savings": ("Financial Coping", 0.85),
    "food bank": ("Financial Coping", 0.85),
    "emergency support": ("Financial Coping", 0.85),
    "cut back": ("Financial Coping", 0.85),
    "cutting back": ("Financial Coping", 0.85),
    "spending": ("Financial Coping", 0.80),
    "second job": ("Financial Coping", 0.80),
    "sell": ("Financial Coping", 0.75),
    "belongings": ("Financial Coping", 0.75),
    "equity": ("Financial Coping", 0.80),
    "line of credit": ("Financial Coping", 0.80),
    "financial help": ("Financial Coping", 0.80),
    "financial difficulties": ("Financial Coping", 0.85),
    "manage": ("Financial Coping", 0.70),
    "rent": ("Housing / Shelter", 0.90),
    "mortgage": ("Housing / Shelter", 0.90),
    "your home": ("Housing / Shelter", 0.85),
    "original home": ("Housing / Shelter", 0.85),
    "foreclosure": ("Housing / Shelter", 0.95),
    "home damage": ("Housing / Shelter", 0.95),
    "property damage": ("Housing / Shelter", 0.95),
    "structural damage": ("Housing / Shelter", 0.95),
    "evacuation": ("Housing / Shelter", 0.90),
    "evacuate": ("Housing / Shelter", 0.90),
    "flood": ("Housing / Shelter", 0.90),
    "flooding": ("Housing / Shelter", 0.95),
    "displaced": ("Housing / Shelter", 0.95),
    "displacement": ("Housing / Shelter", 0.85),
    "temporary housing": ("Housing / Shelter", 0.90),
    "rebuilding": ("Housing / Shelter", 0.80),
    "levee": ("Housing / Shelter", 0.90),
    "stimulus": ("Government Aid", 0.70),
    "stimulus payment": ("Government Aid", 0.70),
    "unemployment insurance": ("Government Aid", 0.75),
    "unemployment": ("Government Aid", 0.75),
    "paycheck protection": ("Government Aid", 0.70),
    "loan forgiveness": ("Government Aid", 0.70),
    "government": ("Government Aid", 0.60),
    "federal": ("Government Aid", 0.60),
    "shutdown": ("Government Aid", 0.65),
    "paychecks": ("Government Aid", 0.70),
    "fema": ("Government Aid", 0.70),
    "emergency management": ("Government Aid", 0.70),
    "disaster relief": ("Government Aid", 0.70),
    "pandemic": ("Trauma / Health", 0.90),
    "health": ("Trauma / Health", 0.85),
    "trauma": ("Trauma / Health", 0.90),
    "hurricane": ("Trauma / Health", 0.90),
    "katrina": ("Trauma / Health", 0.90),
    "rita": ("Trauma / Health", 0.90),
    "disaster": ("Trauma / Health", 0.90),
    "injured": ("Trauma / Health", 0.95),
    "physically injured": ("Trauma / Health", 0.95),
    "killed": ("Trauma / Health", 0.95),
    "death": ("Trauma / Health", 0.95),
    "mortality": ("Trauma / Health", 0.95),
    "disturbing memories": ("Trauma / Health", 0.95),
    "nightmares": ("Trauma / Health", 0.95),
    "debris": ("Trauma / Health", 0.85),
    "contamination": ("Trauma / Health", 0.85),
    "age": ("Demographics", 0.50),
    "sex": ("Demographics", 0.50),
    "date of birth": ("Demographics", 0.50),
    "birth": ("Demographics", 0.50),
    "resident": ("Demographics", 0.50),
    "address": ("Demographics", 0.45),
    "male": ("Demographics", 0.45),
    "female": ("Demographics", 0.45),
    "postcode": ("Demographics", 0.40),
}


def _require_dependency(name: str, module: Any) -> Any:
    if module is None:
        raise ModuleNotFoundError(
            f"{name} is required by PSID_NLP_Crisis_Module_Structure.py"
        )
    return module


def _download_nltk_resource(resource: str, path: str) -> None:
    nltk_module = _require_dependency("nltk", nltk)
    try:
        nltk_module.data.find(path)
    except LookupError:
        nltk_module.download(resource, quiet=True)


@lru_cache(maxsize=1)
def get_rake() -> Any:
    _require_dependency("nltk", nltk)
    rake_cls = _require_dependency("rake_nltk", Rake)
    _download_nltk_resource("stopwords", "corpora/stopwords")
    _download_nltk_resource("punkt", "tokenizers/punkt")
    try:
        _download_nltk_resource("punkt_tab", "tokenizers/punkt_tab")
    except Exception:
        pass
    return rake_cls(min_length=1, max_length=4, include_repeated_phrases=False)


@lru_cache(maxsize=1)
def get_nlp() -> Any:
    spacy_module = _require_dependency("spacy", spacy)
    return spacy_module.load("en_core_web_sm")


def parse_keywords(value: Any) -> list[str]:
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    if pd.isna(value):
        return []

    text = str(value).strip()
    if not text:
        return []

    if text.startswith("[") and text.endswith("]"):
        parsed = ast.literal_eval(text)
        if isinstance(parsed, list):
            return [str(item).strip() for item in parsed if str(item).strip()]

    return [item.strip() for item in text.split(",") if item.strip()]


def normalize_ranked_questions(df: pd.DataFrame) -> pd.DataFrame:
    normalized = df.rename(columns=COLUMN_RENAME_MAP).copy()
    if "keywords" in normalized.columns:
        normalized["keywords"] = normalized["keywords"].apply(parse_keywords)
    if "crisis_origin" not in normalized.columns:
        normalized["crisis_origin"] = normalized["source"].map(SOURCE_TO_CRISIS_ORIGIN)
    if "toggle_category" in normalized.columns:
        normalized["toggle_category"] = normalized["toggle_category"].replace(TOGGLE_LABEL_MAP)
    return normalized


def extract_keywords(text: str) -> list[str]:
    rake = get_rake()
    nlp = get_nlp()
    keywords: set[str] = set()

    rake.extract_keywords_from_text(text)
    for score, phrase in rake.get_ranked_phrases_with_scores():
        if score >= 1.0:
            keywords.add(phrase.lower().strip())

    doc = nlp(text)
    for chunk in doc.noun_chunks:
        clean = chunk.text.lower().strip()
        if len(clean) > 2:
            keywords.add(clean)

    return sorted(keywords)


def _phrase_in_text(phrase: str, text: str) -> bool:
    pattern = r"\b" + re.escape(phrase) + r"\b"
    return re.search(pattern, text) is not None


def _has_any_cue(text: str, cues: set[str]) -> bool:
    return any(cue in text for cue in cues)


def tag_keywords(keywords: list[str]) -> list[dict[str, Any]]:
    matches: list[dict[str, Any]] = []
    sorted_fragments = sorted(TAXONOMY.items(), key=lambda item: len(item[0]), reverse=True)
    for keyword in keywords:
        keyword_lower = keyword.lower().strip()
        for fragment, (construct, weight) in sorted_fragments:
            if _phrase_in_text(fragment, keyword_lower):
                matches.append(
                    {
                        "keyword": keyword_lower,
                        "construct": construct,
                        "weight": weight,
                    }
                )
                break
    return matches


def compute_word_count(text: str) -> int:
    return len(str(text).split())


def compute_complexity(text: str) -> float:
    doc = get_nlp()(text)
    clause_markers = text.count(",") + text.count(";") + text.count(" or ") + text.count(" and ")
    return len(doc.ents) + 0.5 * clause_markers


def compute_utility(tagged: list[dict[str, Any]]) -> float:
    return sum(match["weight"] for match in tagged)


def compute_burden(word_count: int, complexity: float) -> float:
    return max(ALPHA * word_count + BETA * complexity, 0.1)


def extract_constructs(tagged: list[dict[str, Any]]) -> list[str]:
    return sorted({match["construct"] for match in tagged})


def classify_toggle(row: Any) -> str:
    if hasattr(row, "get"):
        tagged = row.get("tagged", [])
        constructs_raw = row.get("constructs")
        source = str(row.get("source", "")).lower()
        question_text = str(
            row.get("question_text", row.get("questiontext", ""))
        ).lower()
        module_type = str(row.get("module_type", row.get("moduletype", ""))).lower()
    else:
        tagged = []
        constructs_raw = []
        source = ""
        question_text = ""
        module_type = ""

    if constructs_raw:
        constructs = set(constructs_raw)
    else:
        constructs = {match["construct"] for match in tagged if isinstance(match, dict)}

    combined_text = f"{source} {question_text}"
    source_is_understanding_society = "understanding society" in source
    source_is_katrina = "hurricane katrina 2007" in source
    source_is_covid = source == "covid-19"
    source_is_shutdown_crisis = source == "govt shutdown crisis"
    source_is_shutdown_income = source == "govt shutdown income"

    disaster_cues = {
        "katrina",
        "hurricane",
        "rita",
        "flood",
        "flooding",
        "evacuat",
        "displaced",
        "temporary housing",
        "property damage",
        "home damaged",
        "home destroyed",
        "original home",
        "without electricity",
        "without running water",
        "move to a different city",
        "fema",
        "disaster relief",
        "emergency management",
        "disturbing memories",
        "disturbing dreams",
        "nightmares",
        "physically injured",
        "killed",
    }
    pandemic_cues = {
        "covid",
        "pandemic",
        "coronavirus",
        "stimulus",
        "stimulus payment",
        "paycheck protection",
        "remote work",
        "work from home",
        "essential work",
        "laid off",
        "furlough",
    }
    financial_crisis_cues = {
        "shutdown",
        "govt",
        "government closure",
        "missed paycheck",
        "miss any paychecks",
        "retroactive pay",
        "federal worker",
        "zero dollars",
    }

    has_disaster_cue = _has_any_cue(question_text, disaster_cues)
    has_pandemic_cue = _has_any_cue(question_text, pandemic_cues)
    has_financial_crisis_cue = _has_any_cue(question_text, financial_crisis_cues)
    generic_constructs = {"Economic / Income", "Employment", "Financial Coping"}

    if source_is_understanding_society:
        return "Generic Core"

    if source_is_shutdown_crisis or has_financial_crisis_cue:
        return "Toggle: Financial Crisis"

    if has_disaster_cue or source_is_katrina:
        return "Toggle: Pandemic / Disaster"

    if has_pandemic_cue:
        return "Toggle: Pandemic / Disaster"

    if source_is_shutdown_income:
        return "Generic Core"

    if source_is_covid:
        if constructs & {"Government Aid", "Housing / Shelter", "Trauma / Health"}:
            return "Toggle: Pandemic / Disaster"
        if constructs <= generic_constructs:
            return "Generic Core"

    if "Demographics" in constructs and constructs <= {"Demographics"}:
        return "Generic Core"

    if module_type == "generic" or constructs <= generic_constructs:
        return "Generic Core"

    if constructs & {"Trauma / Health", "Housing / Shelter"}:
        return "Toggle: Pandemic / Disaster"

    if constructs & {"Government Aid"} and source_is_covid:
        return "Toggle: Pandemic / Disaster"

    if constructs & {"Government Aid"} and source_is_shutdown_crisis:
        return "Toggle: Financial Crisis"

    return "Generic Core"


def select_for_time_budget(
    df: pd.DataFrame,
    score_col: str = "Ri",
    word_count_col: str = "word_count",
    selected_col: str = "selected_for_module",
    toggle_col: str = "toggle_category",
) -> pd.DataFrame:
    def add_rows(candidate_df: pd.DataFrame, running_seconds: int) -> int:
        for index, row in candidate_df.sort_values(score_col, ascending=False).iterrows():
            if index in selected_indices:
                continue
            question_seconds = row[word_count_col] * SECS_PER_WORD
            if running_seconds + question_seconds <= MAX_SECONDS:
                selected_indices.append(index)
                running_seconds += question_seconds
        return running_seconds

    cumulative_seconds = 0
    selected_indices: list[int] = []

    if toggle_col in df.columns:
        generic_core_df = df[df[toggle_col] == "Generic Core"]
        cumulative_seconds = add_rows(generic_core_df, cumulative_seconds)

        remaining_df = df.drop(index=selected_indices)
        cumulative_seconds = add_rows(remaining_df, cumulative_seconds)
    else:
        cumulative_seconds = add_rows(df, cumulative_seconds)

    updated = df.copy()
    updated[selected_col] = False
    updated.loc[selected_indices, selected_col] = True
    return updated


__all__ = [
    "ALPHA",
    "BETA",
    "CSV_PATH",
    "COLUMN_RENAME_MAP",
    "IDEAL_SECONDS",
    "MAX_SECONDS",
    "SECS_PER_WORD",
    "SOURCE_TO_CRISIS_ORIGIN",
    "TAXONOMY",
    "TOGGLE_LABEL_MAP",
    "classify_toggle",
    "compute_burden",
    "compute_complexity",
    "compute_utility",
    "compute_word_count",
    "extract_constructs",
    "extract_keywords",
    "normalize_ranked_questions",
    "parse_keywords",
    "select_for_time_budget",
    "tag_keywords",
]


def main() -> None:
    df = normalize_ranked_questions(pd.read_csv(CSV_PATH))
    print(f"Loaded {len(df)} ranked questions from {CSV_PATH}")
    print(df["source"].value_counts().to_string())


if __name__ == "__main__":
    main()
