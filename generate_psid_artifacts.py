from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

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


def load_dataset() -> pd.DataFrame:
    df = pd.read_csv(CSV_PATH)
    df["keyword_list"] = df["keywords"].apply(parse_keywords)
    df["tagged_keywords"] = df["keyword_list"].apply(tag_keywords)
    df["constructs"] = df["tagged_keywords"].apply(extract_constructs)
    df["selected"] = df["selected_for_module"].fillna(False).astype(bool)
    df["minutes"] = df["word_count"] * SECS_PER_WORD / 60
    df["selected_label"] = df["selected"].map({True: "Selected", False: "Not selected"})
    return df


def build_summary(df: pd.DataFrame) -> dict:
    selected = df[df["selected"]].copy()
    construct_counts = (
        selected["constructs"].explode().dropna().value_counts().to_dict()
    )

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
    }
    SUMMARY_PATH.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    return summary


def write_dashboard_data(df: pd.DataFrame, summary: dict) -> None:
    dashboard_df = df[
        [
            "question_text",
            "source",
            "toggle_category",
            "Ui",
            "Bi",
            "Ri",
            "word_count",
            "selected",
            "constructs",
        ]
    ].copy()
    dashboard_df["Ui"] = dashboard_df["Ui"].round(3)
    dashboard_df["Bi"] = dashboard_df["Bi"].round(3)
    dashboard_df["Ri"] = dashboard_df["Ri"].round(3)
    payload = {
        "summary": summary,
        "rows": dashboard_df.to_dict(orient="records"),
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