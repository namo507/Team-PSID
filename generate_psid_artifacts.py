from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from PSID_NLP_Crisis_Module_Structure import (
    SECS_PER_WORD,
    extract_constructs,
    parse_keywords,
    tag_keywords,
)


ROOT = Path(__file__).resolve().parent
CSV_PATH = ROOT / "PSID_Ranked_Questions_Final.csv"
SUMMARY_PATH = ROOT / "psid_artifact_summary.json"
DASHBOARD_DATA_PATH = ROOT / "psid_dashboard_data.js"

FIG_TOP = ROOT / "fig_top_ranked_questions.png"
FIG_TOGGLE = ROOT / "fig_toggle_comparison.png"
FIG_UTILITY = ROOT / "fig_utility_vs_burden.png"
FIG_HEATMAP = ROOT / "fig_construct_heatmap.png"
FIG_TIME = ROOT / "fig_time_budget.png"

LEGACY_ALIASES = {
    FIG_TOP: ROOT / "fig_top_ranked.png",
    FIG_TOGGLE: ROOT / "fig_toggle_dist.png",
    FIG_UTILITY: ROOT / "fig_utility_burden.png",
    FIG_HEATMAP: ROOT / "fig_heatmap.png",
}

CONSTRUCT_PRIORITY = {
    "Economic / Income": 0.40,
    "Employment": 0.42,
    "Financial Coping": 0.45,
    "Housing / Shelter": 0.55,
    "Government Aid": 0.48,
    "Trauma / Health": 0.58,
    "Demographics": 0.14,
}

SOURCE_SPECIFIC_TERMS = {
    "katrina",
    "rita",
    "fema",
    "covid",
    "pandemic",
    "shutdown",
    "government shutdown",
}

DOCUMENTATION_BACKED_QUESTIONS = [
    {
        "kind": "generic",
        "module": "Generic Core",
        "title": "Financial strain flag",
        "question": "Have you experienced any financial difficulties because of the crisis?",
        "constructs": ["Financial Coping"],
        "evidence_terms": ["financial difficulties", "financial strain"],
        "why_it_matters": "A compact cross-crisis screener that activates downstream coping and aid questions without wasting time on respondents unaffected financially.",
    },
    {
        "kind": "generic",
        "module": "Generic Core",
        "title": "Work interruption",
        "question": "Have you stopped this work because of the crisis?",
        "constructs": ["Employment"],
        "evidence_terms": ["stopped this work", "stopped working", "laid off", "furloughed"],
        "why_it_matters": "Preserves one of the strongest employment disruption signals while remaining portable across shutdowns, disasters, and public-health emergencies.",
    },
    {
        "kind": "generic",
        "module": "Generic Core",
        "title": "Income continuity",
        "question": "Were there any wages or salary payments from this job during the crisis period?",
        "constructs": ["Employment", "Economic / Income"],
        "evidence_terms": ["wages", "salary", "earnings", "paycheck"],
        "why_it_matters": "Links employment status to realized income loss, which is more informative than demographics alone for a generic always-on core.",
    },
    {
        "kind": "generic",
        "module": "Generic Core",
        "title": "Government assistance",
        "question": "Did you receive any government financial assistance because of the crisis?",
        "constructs": ["Government Aid"],
        "evidence_terms": ["stimulus", "paycheck protection", "government financial assistance", "fema"],
        "why_it_matters": "Captures public support exposure in a reusable way without tying the wording to one historical event or program.",
    },
    {
        "kind": "generic",
        "module": "Generic Core",
        "title": "Housing instability",
        "question": "Did your household fall behind on rent, mortgage, utilities, or other major bills because of the crisis?",
        "constructs": ["Housing / Shelter", "Economic / Income"],
        "evidence_terms": ["rent", "mortgage", "bills", "utilities", "home damage"],
        "why_it_matters": "Adds meaningful household vulnerability context that is much more actionable than a pure demographic check.",
    },
    {
        "kind": "generic",
        "module": "Generic Core",
        "title": "Wellbeing check",
        "question": "Since the crisis, how often have you felt worried, unable to relax, or unable to sleep well?",
        "constructs": ["Trauma / Health"],
        "evidence_terms": ["trouble relaxing", "sleep", "worrying", "disturbing memories"],
        "why_it_matters": "A condensed wellbeing item keeps the generic core from being reduced to only demographics and labor-market questions.",
    },
    {
        "kind": "specific",
        "module": "Pandemic / Disaster",
        "title": "Pandemic earnings loss",
        "question": "Did you lose earnings because of the pandemic?",
        "constructs": ["Economic / Income"],
        "evidence_terms": ["lost earnings", "pandemic"],
        "why_it_matters": "High-yield pandemic item that directly captures the core economic shock from public-health restrictions.",
    },
    {
        "kind": "specific",
        "module": "Pandemic / Disaster",
        "title": "Emergency payment receipt",
        "question": "Did you receive a stimulus payment or other emergency government support?",
        "constructs": ["Government Aid"],
        "evidence_terms": ["stimulus payment", "stimulus payments", "paycheck protection", "government assistance"],
        "why_it_matters": "Keeps the assistance signal but generalizes it beyond one named program, making the item reusable.",
    },
    {
        "kind": "specific",
        "module": "Pandemic / Disaster",
        "title": "Essential work exposure",
        "question": "Were you working in a job that was considered essential during the crisis?",
        "constructs": ["Employment"],
        "evidence_terms": ["essential work", "work from home", "remote work"],
        "why_it_matters": "Distinguishes frontline disruption from remote-capable employment and strengthens interpretation of labor-market exposure.",
    },
    {
        "kind": "specific",
        "module": "Pandemic / Disaster",
        "title": "Evacuation",
        "question": "Did you evacuate from your home before the disaster hit?",
        "constructs": ["Housing / Shelter"],
        "evidence_terms": ["evacuate", "evacuation"],
        "why_it_matters": "One of the cleanest disaster-routing questions and a strong marker of direct exposure.",
    },
    {
        "kind": "specific",
        "module": "Pandemic / Disaster",
        "title": "Home damage severity",
        "question": "How severe was the damage to your home during the disaster?",
        "constructs": ["Housing / Shelter"],
        "evidence_terms": ["property damage", "home damaged", "flooding"],
        "why_it_matters": "Converts detailed Katrina evidence into a portable housing-impact severity item.",
    },
    {
        "kind": "specific",
        "module": "Pandemic / Disaster",
        "title": "Temporary housing",
        "question": "How long did you stay in temporary housing after the disaster?",
        "constructs": ["Housing / Shelter"],
        "evidence_terms": ["temporary housing", "displaced", "move to a different city"],
        "why_it_matters": "Captures longer-run displacement burden that simple yes/no housing items can miss.",
    },
    {
        "kind": "specific",
        "module": "Pandemic / Disaster",
        "title": "Disaster distress",
        "question": "Since the disaster, how often have you had disturbing memories or dreams about what happened?",
        "constructs": ["Trauma / Health"],
        "evidence_terms": ["disturbing memories", "disturbing dreams", "nightmares"],
        "why_it_matters": "Condenses multiple trauma items into one deployable distress signal while preserving the strongest construct evidence.",
    },
    {
        "kind": "specific",
        "module": "Financial Crisis",
        "title": "Financial coping strategy",
        "question": "How did your household manage financial difficulties caused by the shutdown or crisis?",
        "constructs": ["Financial Coping"],
        "evidence_terms": ["manage financial difficulties", "sell your belongings", "shutdown"],
        "why_it_matters": "Maintains the strongest scored shutdown item while making the wording cleaner and easier to field.",
    },
]


def _min_max_scale(values: pd.Series) -> pd.Series:
    minimum = float(values.min())
    maximum = float(values.max())
    if maximum - minimum == 0:
        return pd.Series([0.0] * len(values), index=values.index)
    return (values - minimum) / (maximum - minimum)


def _contains_source_specific_term(text: str) -> bool:
    lowered = str(text).lower()
    return any(term in lowered for term in SOURCE_SPECIFIC_TERMS)


def suggest_deployable_wording(question_text: str, toggle_category: str) -> str:
    lowered = question_text.lower()
    replacements = [
        (
            "how did you/your family manage any financial difficulties due to the shutdown - sell your belongings",
            "How did your household manage financial difficulties caused by the shutdown or crisis?",
        ),
        ("calculate respondents age", "What is your age in years?"),
        ("and are you... 1. male 2. female", "How do you describe your sex or gender?"),
        ("normally resident at this address", "Are you currently living at this address?"),
        ("stopped this work", "Have you stopped this work because of the crisis?"),
        ("stopped working at this business", "Have you stopped working at this business because of the crisis?"),
        ("any wages or salarys", "Were there any wages or salary payments from this job during the crisis period?"),
        ("lost earnings because of the pandemic", "Did you lose earnings because of the pandemic?"),
        ("received stimulus payment", "Did you receive a stimulus payment or other emergency government support?"),
        ("stimulus payments", "Did you receive a stimulus payment or other emergency government support?"),
        ("paycheck protection", "Did you receive paycheck protection or other emergency business support?"),
        ("only work from home", "Did you work entirely from home during the crisis?"),
        ("considered essential work", "Were you working in a job that was considered essential during the crisis?"),
        ("laid off or furloughed because of the pandemic", "Were you laid off or furloughed because of the pandemic?"),
        ("evacuate from your home before katrina or rita hit", "Did you evacuate from your home before the disaster hit?"),
        ("major flooding in your home", "Did you experience major flooding in your home during the disaster?"),
        ("property damage to your home", "How severe was the damage to your home during the disaster?"),
        ("financial help did you receive from fema", "Did you receive emergency financial assistance because of the disaster?"),
        ("temporary housing after katrina or rita", "How long did you stay in temporary housing after the disaster?"),
        ("disturbing memories thoughts or images", "Since the disaster, how often have you had disturbing memories or images about what happened?"),
        ("disturbing dreams about the hurricane", "Since the disaster, how often have you had disturbing dreams about what happened?"),
        ("did you lose your job because of katrina or rita", "Did the disaster cause you to lose your job?"),
        ("how afraid were you during katrina or rita", "How afraid were you during the disaster that you might be seriously injured or killed?"),
        ("any financial difficulties", "Have you experienced any financial difficulties because of the crisis?"),
    ]

    for needle, replacement in replacements:
        if needle in lowered:
            return replacement

    cleaned = (
        str(question_text)
        .strip()
        .replace("Katrina and Rita", "the disaster")
        .replace("katrina and rita", "the disaster")
        .replace("Katrina or Rita", "the disaster")
        .replace("katrina or rita", "the disaster")
    )
    cleaned = cleaned.replace("Katrina", "the disaster").replace("Rita", "the disaster")
    cleaned = cleaned.replace("salarys", "salary payments")
    cleaned = cleaned.replace("the disaster and the disaster", "the disaster")
    cleaned = cleaned.replace("the disaster or the disaster", "the disaster")
    cleaned = " ".join(cleaned.split())
    if toggle_category == "Generic Core" and not cleaned.endswith("?"):
        cleaned = cleaned.rstrip(". ") + "?"
    return cleaned


def write_ranked_csv(df: pd.DataFrame) -> None:
    output = df.copy()
    output["keyword_list"] = output["keyword_list"].apply(repr)
    output["tagged_keywords"] = output["tagged_keywords"].apply(repr)
    output["constructs"] = output["constructs"].apply(repr)

    ordered_columns = [
        "question_text",
        "source",
        "module_type",
        "toggle_category",
        "keywords",
        "n_keywords",
        "word_count",
        "complexity",
        "Ui",
        "Bi",
        "Ri",
        "selected_for_module",
        "selected",
        "minutes",
        "Pi",
        "augmented_utility",
        "idf_strength",
        "redundancy_penalty",
        "construct_bonus",
        "portability_bonus",
        "construct_count",
        "recommended_wording",
        "keyword_list",
        "tagged_keywords",
        "constructs",
    ]

    rounded_columns = [
        "Ui",
        "Bi",
        "Ri",
        "minutes",
        "Pi",
        "augmented_utility",
        "idf_strength",
        "redundancy_penalty",
        "construct_bonus",
        "portability_bonus",
    ]
    for column in rounded_columns:
        output[column] = output[column].round(3)

    output = output[ordered_columns]
    output.to_csv(CSV_PATH, index=False)


def compute_augmented_scores(df: pd.DataFrame) -> pd.DataFrame:
    enriched = df.copy()
    texts = enriched["question_text"].fillna("").astype(str)

    vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2), min_df=1)
    matrix = vectorizer.fit_transform(texts)
    similarities = cosine_similarity(matrix)
    np.fill_diagonal(similarities, 0.0)

    analyzer = vectorizer.build_analyzer()
    idf_lookup = dict(zip(vectorizer.get_feature_names_out(), vectorizer.idf_))
    mean_idf = float(np.mean(vectorizer.idf_))

    def average_idf(text: str) -> float:
        features = [idf_lookup[token] for token in analyzer(text) if token in idf_lookup]
        return float(np.mean(features)) if features else mean_idf

    construct_frequency = enriched["constructs"].explode().dropna().value_counts()

    def construct_bonus(constructs: list[str]) -> float:
        if not constructs:
            return 0.0
        rarity = np.mean([1.0 / construct_frequency.get(name, 1) for name in constructs]) * len(enriched)
        priority = np.mean([CONSTRUCT_PRIORITY.get(name, 0.25) for name in constructs])
        richness = len(set(constructs))
        return float(rarity + priority + 0.08 * richness)

    def portability_bonus(row: pd.Series) -> float:
        source_specific = _contains_source_specific_term(row["question_text"])
        if row["toggle_category"] == "Generic Core":
            return 0.16 if not source_specific else 0.03
        return 0.08 if not source_specific else 0.02

    enriched["idf_strength"] = texts.apply(average_idf)
    enriched["redundancy_penalty"] = similarities.max(axis=1)
    enriched["construct_bonus"] = enriched["constructs"].apply(construct_bonus)
    enriched["portability_bonus"] = enriched.apply(portability_bonus, axis=1)
    enriched["construct_count"] = enriched["constructs"].apply(lambda values: len(set(values)))

    idf_scaled = _min_max_scale(enriched["idf_strength"])
    redundancy_scaled = _min_max_scale(enriched["redundancy_penalty"])
    construct_scaled = _min_max_scale(enriched["construct_bonus"])
    richness_scaled = _min_max_scale(enriched["construct_count"])

    uplift = (
        1.0
        + 0.32 * idf_scaled
        + 0.24 * construct_scaled
        + 0.12 * richness_scaled
        + enriched["portability_bonus"]
    )
    enriched["augmented_utility"] = enriched["Ui"] * uplift
    enriched["Pi"] = enriched["augmented_utility"] / (
        enriched["Bi"] * (1.0 + 0.65 * redundancy_scaled)
    )
    enriched["recommended_wording"] = enriched.apply(
        lambda row: suggest_deployable_wording(row["question_text"], row["toggle_category"]),
        axis=1,
    )
    return enriched


def build_design_recommendations(df: pd.DataFrame) -> dict:
    recommendations: dict[str, list[dict[str, object]]] = {"generic": [], "specific": []}

    lowered_text = df["question_text"].str.lower()
    for item in DOCUMENTATION_BACKED_QUESTIONS:
        evidence_mask = lowered_text.apply(
            lambda text: any(term in text for term in item["evidence_terms"])
        )
        evidence = df[evidence_mask].copy()

        if evidence.empty:
            evidence = df[
                df["constructs"].apply(
                    lambda values: any(name in values for name in item["constructs"])
                )
            ].copy()

        evidence = evidence.sort_values("Pi", ascending=False).head(3)
        entry = {
            "module": item["module"],
            "title": item["title"],
            "question": item["question"],
            "constructs": item["constructs"],
            "why_it_matters": item["why_it_matters"],
            "support_score": round(float(evidence["Pi"].mean()), 3) if not evidence.empty else None,
            "supporting_sources": sorted(evidence["source"].unique().tolist()) if not evidence.empty else [],
            "supporting_examples": evidence["recommended_wording"].head(2).tolist(),
        }
        bucket = "generic" if item["kind"] == "generic" else "specific"
        recommendations[bucket].append(entry)

    for bucket in recommendations:
        recommendations[bucket] = sorted(
            recommendations[bucket],
            key=lambda item: item["support_score"] if item["support_score"] is not None else -1,
            reverse=True,
        )

    return recommendations


def load_dataset() -> pd.DataFrame:
    df = pd.read_csv(CSV_PATH)
    df["keyword_list"] = df["keywords"].apply(parse_keywords)
    df["tagged_keywords"] = df["keyword_list"].apply(tag_keywords)
    df["constructs"] = df["tagged_keywords"].apply(extract_constructs)
    df["selected"] = df["selected_for_module"].fillna(False).astype(bool)
    df["minutes"] = df["word_count"] * SECS_PER_WORD / 60
    df["selected_label"] = df["selected"].map({True: "Selected", False: "Not selected"})
    return compute_augmented_scores(df)


def build_summary(df: pd.DataFrame) -> dict:
    selected = df[df["selected"]].copy()
    construct_counts = (
        selected["constructs"].explode().dropna().value_counts().to_dict()
    )
    recommendations = build_design_recommendations(df)

    summary = {
        "rows": int(len(df)),
        "selected_rows": int(len(selected)),
        "selected_minutes": round(float(selected["minutes"].sum()), 2),
        "all_minutes": round(float(df["minutes"].sum()), 2),
        "toggle_counts": {k: int(v) for k, v in df["toggle_category"].value_counts().items()},
        "selected_toggle_counts": {
            k: int(v) for k, v in selected["toggle_category"].value_counts().items()
        },
        "source_counts": {k: int(v) for k, v in df["source"].value_counts().items()},
        "selected_source_counts": {
            k: int(v) for k, v in selected["source"].value_counts().items()
        },
        "construct_counts": {k: int(v) for k, v in construct_counts.items()},
        "avg_ri": round(float(df["Ri"].mean()), 3),
        "max_ri": round(float(df["Ri"].max()), 3),
        "avg_pi": round(float(df["Pi"].mean()), 3),
        "max_pi": round(float(df["Pi"].max()), 3),
        "recommended_generic_count": len(recommendations["generic"]),
        "recommended_specific_count": len(recommendations["specific"]),
    }
    SUMMARY_PATH.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    return summary


def write_dashboard_data(df: pd.DataFrame, summary: dict) -> None:
    recommendations = build_design_recommendations(df)
    dashboard_df = df[
        [
            "question_text",
            "source",
            "toggle_category",
            "Ui",
            "Bi",
            "Ri",
            "Pi",
            "augmented_utility",
            "idf_strength",
            "redundancy_penalty",
            "construct_bonus",
            "word_count",
            "selected",
            "constructs",
            "recommended_wording",
        ]
    ].copy()
    dashboard_df["Ui"] = dashboard_df["Ui"].round(3)
    dashboard_df["Bi"] = dashboard_df["Bi"].round(3)
    dashboard_df["Ri"] = dashboard_df["Ri"].round(3)
    dashboard_df["Pi"] = dashboard_df["Pi"].round(3)
    dashboard_df["augmented_utility"] = dashboard_df["augmented_utility"].round(3)
    dashboard_df["idf_strength"] = dashboard_df["idf_strength"].round(3)
    dashboard_df["redundancy_penalty"] = dashboard_df["redundancy_penalty"].round(3)
    dashboard_df["construct_bonus"] = dashboard_df["construct_bonus"].round(3)
    payload = {
        "summary": summary,
        "rows": dashboard_df.to_dict(orient="records"),
        "recommendations": recommendations,
    }
    DASHBOARD_DATA_PATH.write_text(
        "window.PSID_DASHBOARD = " + json.dumps(payload, indent=2) + ";\n",
        encoding="utf-8",
    )


def _style_matplotlib() -> None:
    sns.set_theme(style="whitegrid")
    plt.rcParams.update(
        {
            "figure.dpi": 140,
            "savefig.dpi": 180,
            "axes.titlesize": 14,
            "axes.titleweight": "bold",
            "axes.labelsize": 11,
            "font.family": "DejaVu Sans",
        }
    )


def save_aliases() -> None:
    for source, alias in LEGACY_ALIASES.items():
        alias.write_bytes(source.read_bytes())


def plot_top_ranked(df: pd.DataFrame) -> None:
    top = df.nlargest(15, "Ri").sort_values("Ri")
    labels = [
        f"{row.question_text[:52]}{'...' if len(row.question_text) > 52 else ''}"
        for row in top.itertuples()
    ]
    colors = sns.color_palette("crest", len(top))

    fig, ax = plt.subplots(figsize=(12, 8))
    ax.barh(labels, top["Ri"], color=colors)
    for index, value in enumerate(top["Ri"]):
        ax.text(value + 0.03, index, f"{value:.2f}", va="center", fontsize=9)
    ax.set_title("Top 15 Questions by Utility-to-Burden Ratio")
    ax.set_xlabel("Ri score")
    ax.set_ylabel("")
    fig.tight_layout()
    fig.savefig(FIG_TOP, bbox_inches="tight")
    plt.close(fig)


def plot_toggle_comparison(df: pd.DataFrame) -> None:
    counts = pd.crosstab(df["source"], df["toggle_category"]).reindex(
        index=df["source"].value_counts().index
    )
    palette = {
        "Generic Core": "#2563eb",
        "Toggle: Financial Crisis": "#d97706",
        "Toggle: Pandemic / Disaster": "#dc2626",
    }

    fig, ax = plt.subplots(figsize=(12, 7))
    counts.plot(
        kind="barh",
        stacked=True,
        color=[palette.get(col, "#64748b") for col in counts.columns],
        ax=ax,
    )
    ax.set_title("Question Distribution by Source and Toggle Category")
    ax.set_xlabel("Questions")
    ax.set_ylabel("")
    ax.legend(title="Toggle category", frameon=False)
    fig.tight_layout()
    fig.savefig(FIG_TOGGLE, bbox_inches="tight")
    plt.close(fig)


def plot_utility_vs_burden(df: pd.DataFrame) -> None:
    palette = {
        "Generic Core": "#2563eb",
        "Toggle: Financial Crisis": "#d97706",
        "Toggle: Pandemic / Disaster": "#dc2626",
    }
    fig, ax = plt.subplots(figsize=(11, 7))
    sns.scatterplot(
        data=df,
        x="Bi",
        y="Ui",
        hue="toggle_category",
        style="selected_label",
        size="Ri",
        sizes=(60, 360),
        palette=palette,
        alpha=0.8,
        ax=ax,
    )
    ax.set_title("Utility vs Burden, Sized by Ri")
    ax.set_xlabel("Burden (Bi)")
    ax.set_ylabel("Utility (Ui)")
    ax.legend(frameon=False, bbox_to_anchor=(1.02, 1), loc="upper left")
    fig.tight_layout()
    fig.savefig(FIG_UTILITY, bbox_inches="tight")
    plt.close(fig)


def plot_construct_heatmap(df: pd.DataFrame) -> None:
    exploded = df[["source", "constructs"]].explode("constructs").dropna()
    heatmap = pd.crosstab(exploded["source"], exploded["constructs"]).reindex(
        index=df["source"].value_counts().index
    )
    ordered_columns = heatmap.sum(axis=0).sort_values(ascending=False).index.tolist()
    heatmap = heatmap[ordered_columns]

    fig, ax = plt.subplots(figsize=(13, 7))
    sns.heatmap(heatmap, annot=True, fmt="d", cmap="YlOrRd", linewidths=0.5, ax=ax)
    ax.set_title("Construct Coverage by Source")
    ax.set_xlabel("Construct")
    ax.set_ylabel("")
    fig.tight_layout()
    fig.savefig(FIG_HEATMAP, bbox_inches="tight")
    plt.close(fig)


def plot_time_budget(df: pd.DataFrame) -> None:
    selected = df[df["selected"]].copy()
    time_by_toggle = (
        selected.groupby("toggle_category", as_index=False)["minutes"].sum().sort_values("minutes")
    )
    count_by_toggle = selected.groupby("toggle_category")["selected"].sum().to_dict()
    palette = {
        "Generic Core": "#2563eb",
        "Toggle: Financial Crisis": "#d97706",
        "Toggle: Pandemic / Disaster": "#dc2626",
    }

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.barh(
        time_by_toggle["toggle_category"],
        time_by_toggle["minutes"],
        color=[palette.get(name, "#64748b") for name in time_by_toggle["toggle_category"]],
    )
    for bar, toggle, minutes in zip(bars, time_by_toggle["toggle_category"], time_by_toggle["minutes"]):
        count = count_by_toggle.get(toggle, 0)
        ax.text(minutes + 0.15, bar.get_y() + bar.get_height() / 2, f"{minutes:.1f} min | {count} q", va="center")
    ax.axvline(30, color="#111827", linestyle="--", linewidth=1.2, label="30-minute cap")
    ax.set_title("Selected Time Budget by Toggle Category")
    ax.set_xlabel("Minutes")
    ax.set_ylabel("")
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(FIG_TIME, bbox_inches="tight")
    plt.close(fig)


def build_all() -> dict:
    _style_matplotlib()
    df = load_dataset()
    summary = build_summary(df)
    write_ranked_csv(df)
    write_dashboard_data(df, summary)
    plot_top_ranked(df)
    plot_toggle_comparison(df)
    plot_utility_vs_burden(df)
    plot_construct_heatmap(df)
    plot_time_budget(df)
    save_aliases()
    return summary


if __name__ == "__main__":
    summary = build_all()
    print(json.dumps(summary, indent=2))