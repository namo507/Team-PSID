from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
from PIL import Image, ImageDraw, ImageFont

import generate_psid_artifacts as artifacts


ROOT = Path(__file__).resolve().parent
NOTEBOOK_PATH = ROOT / "PSID_NLP_Crisis_Module_Final.ipynb"
SUMMARY_PATH = ROOT / "psid_artifact_summary.json"
OUTPUT_PATH = ROOT / "PSID_Model_Architecture_Documentation.pdf"

PAGE_W = 1654
PAGE_H = 2339
MARGIN = 90

BG = (248, 249, 251)
WHITE = (255, 255, 255)
INK = (31, 41, 55)
MUTED = (107, 114, 128)
NAVY = (30, 58, 95)
BLUE = (37, 99, 235)
GREEN = (5, 150, 105)
AMBER = (217, 119, 6)
RED = (220, 38, 38)
LINE = (229, 231, 235)
SOFT_BLUE = (248, 251, 255)
SOFT_AMBER = (255, 249, 241)
SOFT_GREEN = (244, 251, 247)


def load_font(size: int, bold: bool = False):
    candidates = []
    if bold:
        candidates.extend(
            [
                "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
                "/Library/Fonts/Arial Bold.ttf",
                "/System/Library/Fonts/Supplemental/Helvetica.ttc",
            ]
        )
    else:
        candidates.extend(
            [
                "/System/Library/Fonts/Supplemental/Arial.ttf",
                "/Library/Fonts/Arial.ttf",
                "/System/Library/Fonts/Supplemental/Helvetica.ttc",
            ]
        )
    for candidate in candidates:
        if Path(candidate).exists():
            try:
                return ImageFont.truetype(candidate, size=size)
            except OSError:
                continue
    return ImageFont.load_default()


FONT_TITLE = load_font(54, bold=True)
FONT_SUBTITLE = load_font(24)
FONT_H1 = load_font(36, bold=True)
FONT_H2 = load_font(28, bold=True)
FONT_BODY = load_font(22)
FONT_BODY_BOLD = load_font(22, bold=True)
FONT_SMALL = load_font(18)
FONT_MONO = load_font(22)
FONT_KPI = load_font(42, bold=True)


def new_page(title: str, subtitle: str | None = None):
    page = Image.new("RGB", (PAGE_W, PAGE_H), BG)
    draw = ImageDraw.Draw(page)
    draw.text((MARGIN, 54), title, font=FONT_TITLE, fill=NAVY)
    if subtitle:
        draw.text((MARGIN + 2, 124), subtitle, font=FONT_SUBTITLE, fill=MUTED)
    return page, draw


def rounded(draw, box, *, fill=WHITE, outline=LINE, radius=28, width=2):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def text_height(draw, text, font):
    bbox = draw.textbbox((0, 0), text, font=font)
    return bbox[3] - bbox[1]


def wrap_lines(draw, text: str, font, max_width: int):
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        trial = word if not current else f"{current} {word}"
        if draw.textbbox((0, 0), trial, font=font)[2] <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines or [""]


def draw_wrapped(draw, x: int, y: int, width: int, text: str, font, fill=INK, gap: int = 8):
    for line in wrap_lines(draw, text, font, width):
        draw.text((x, y), line, font=font, fill=fill)
        y += text_height(draw, line, font) + gap
    return y


def draw_bullets(draw, x: int, y: int, width: int, items: list[str], font, fill=INK, bullet_fill=INK, gap: int = 12):
    for item in items:
        lines = wrap_lines(draw, item, font, width - 28)
        draw.ellipse((x, y + 9, x + 8, y + 17), fill=bullet_fill)
        line_y = y
        for idx, line in enumerate(lines):
            draw.text((x + 20, line_y), line, font=font, fill=fill)
            line_y += text_height(draw, line, font) + 6
        y = line_y + gap
    return y


def draw_footer(draw, text: str):
    bbox = draw.textbbox((0, 0), text, font=FONT_SMALL)
    draw.text((PAGE_W - MARGIN - (bbox[2] - bbox[0]), PAGE_H - 48), text, font=FONT_SMALL, fill=MUTED)


def draw_kpi(draw, x: int, y: int, w: int, h: int, value: str, label: str, accent):
    rounded(draw, (x, y, x + w, y + h))
    draw.rectangle((x, y, x + w, y + 14), fill=accent)
    draw.text((x + 24, y + 28), value, font=FONT_KPI, fill=INK)
    draw_wrapped(draw, x + 24, y + 90, w - 48, label, FONT_SMALL, fill=MUTED, gap=4)


def draw_code_box(draw, x: int, y: int, w: int, h: int, text: str, *, fill=SOFT_BLUE):
    rounded(draw, (x, y, x + w, y + h), fill=fill)
    draw_wrapped(draw, x + 22, y + 20, w - 44, text, FONT_MONO, fill=NAVY, gap=6)


def draw_arrow(draw, x1: int, y1: int, x2: int, y2: int, color=BLUE):
    draw.line((x1, y1, x2, y2), fill=color, width=5)
    draw.polygon([(x2, y2), (x2 - 18, y2 - 12), (x2 - 18, y2 + 12)], fill=color)


def load_notebook_sections():
    notebook = json.loads(NOTEBOOK_PATH.read_text())
    headings = []
    for cell in notebook.get("cells", []):
        if cell.get("cell_type") != "markdown":
            continue
        for line in cell.get("source", []):
            if line.startswith("## "):
                headings.append(line.replace("## ", "").strip())
                break
    return headings


def get_examples(df: pd.DataFrame):
    generic = df[df["toggle_category"] == "Generic Core"].sort_values("Pi", ascending=False).iloc[0]
    financial = df[df["toggle_category"] == "Toggle: Financial Crisis"].sort_values("Pi", ascending=False).iloc[0]
    specific = df[df["toggle_category"] == "Toggle: Pandemic / Disaster"].sort_values("Pi", ascending=False).iloc[0]
    return generic, financial, specific


def page_cover(summary: dict):
    page, draw = new_page(
        "PSID Crisis Module Documentation",
        "A non-technical guide to the notebook, code architecture, formulas, weights, and final selection logic",
    )
    rounded(draw, (MARGIN, 190, PAGE_W - MARGIN, 400), fill=SOFT_BLUE)
    draw_wrapped(
        draw,
        MARGIN + 30,
        230,
        PAGE_W - 2 * MARGIN - 60,
        "This report explains how the PSID crisis-module workflow turns a large bank of candidate questions into a short, deployable module. It walks through the notebook structure, the main code functions, the Ri and Pi formulas, the construct-priority weights, and the logic used to decide which questions stay in the Generic Core and which remain crisis-specific toggles.",
        FONT_BODY,
        fill=INK,
    )

    cards = [
        (str(summary["rows"]), "total ranked questions", BLUE),
        (str(summary["selected_rows"]), "selected questions", GREEN),
        (f"{summary['selected_minutes']:.2f}", "selected minutes", AMBER),
        (f"{summary['avg_pi']:.3f}", "average Pi", RED),
    ]
    x_positions = [MARGIN, MARGIN + 370, MARGIN + 740, MARGIN + 1110]
    for (value, label, accent), x in zip(cards, x_positions):
        draw_kpi(draw, x, 470, 300, 180, value, label, accent)

    rounded(draw, (MARGIN, 720, PAGE_W - MARGIN, 1320), fill=WHITE)
    draw.text((MARGIN + 30, 760), "What the project does", font=FONT_H1, fill=NAVY)
    draw_bullets(
        draw,
        MARGIN + 36,
        840,
        PAGE_W - 2 * MARGIN - 72,
        [
            "Loads the final ranked CSV and reuses it as the single source of truth for the notebook, dashboard, report, and questionnaire demos.",
            "Scores each question using a baseline utility-to-burden ratio, then improves that ranking with an enhanced priority score called Pi.",
            "Writes synchronized outputs: ranked CSV, summary JSON, dashboard payload, recommendation bundle, and figure files.",
            "Keeps the final selected module below the 30-minute ceiling while preserving high-value crisis content.",
        ],
        FONT_BODY,
        fill=INK,
        bullet_fill=BLUE,
    )

    rounded(draw, (MARGIN, 1380, PAGE_W - MARGIN, 1930), fill=SOFT_AMBER)
    draw.text((MARGIN + 30, 1420), "Validated headline results", font=FONT_H1, fill=NAVY)
    draw_bullets(
        draw,
        MARGIN + 36,
        1500,
        PAGE_W - 2 * MARGIN - 72,
        [
            f"The final benchmark selects {summary['selected_rows']} questions out of {summary['rows']} ranked candidates.",
            f"The selected module takes {summary['selected_minutes']:.2f} minutes, compared with {summary['all_minutes']:.2f} minutes for the full corpus.",
            f"Average Ri is {summary['avg_ri']:.3f} and average Pi is {summary['avg_pi']:.3f}.",
            f"The pipeline currently produces {summary['recommended_generic_count']} generic-core recommendations and {summary['recommended_specific_count']} crisis-specific recommendations.",
        ],
        FONT_BODY,
        fill=INK,
        bullet_fill=AMBER,
    )
    draw_footer(draw, "Sources: PSID_NLP_Crisis_Module_Final.ipynb, generate_psid_artifacts.py, psid_artifact_summary.json")
    return page


def page_notebook_walkthrough(sections: list[str]):
    page, draw = new_page(
        "How The Notebook Documents The Workflow",
        "The notebook is not a separate experimental branch. It mirrors the production-ranked workflow and refresh path.",
    )

    rounded(draw, (MARGIN, 190, PAGE_W - MARGIN, 2050), fill=WHITE)
    draw.text((MARGIN + 30, 230), "Notebook sections in plain language", font=FONT_H1, fill=NAVY)

    descriptions = {
        "Final Corpus Snapshot": "Confirms how many questions are in the final ranked pool and how they are distributed by source and toggle.",
        "Top Ranked Question Review": "Shows which questions rise to the top when the model rewards high information value and low burden.",
        "Selected Module Composition": "Explains how the final 28-question module is distributed across Generic Core and crisis-specific content.",
        "Construct Coverage in the Selected Module": "Shows which crisis dimensions dominate the final shortlist, such as trauma, housing, and aid.",
        "Stakeholder Deliverables": "Lists the dashboard, report, demos, and summary files that are regenerated from the same ranked workflow.",
        "Figure Outputs and Supporting Bundles": "Verifies that the PNG figures, JSON summary, and JavaScript dashboard payload are present and synchronized.",
        "Selected Question Inspection": "Lets the user inspect the selected questions directly by source, toggle, timing, and constructs.",
        "Validation Checks": "Pins the final benchmark values so accidental changes can be caught before downstream artifacts are refreshed.",
        "Refresh the Production Artifacts": "Runs build_all() so the notebook refreshes the same outputs used outside Jupyter.",
        "Refresh Checklist": "Reminds the user what to verify after regeneration.",
        "Post-Refresh Verification": "Reloads the written summary JSON to confirm persisted artifact values, not just in-memory values.",
    }

    y = 310
    for index, title in enumerate(sections, start=1):
        box_top = y
        rounded(draw, (MARGIN + 30, box_top, PAGE_W - MARGIN - 30, box_top + 125), fill=SOFT_BLUE if index % 2 else WHITE)
        draw.text((MARGIN + 58, box_top + 20), f"{index}. {title}", font=FONT_H2, fill=NAVY)
        draw_wrapped(draw, MARGIN + 58, box_top + 62, PAGE_W - 2 * MARGIN - 116, descriptions.get(title, "Notebook section used to explain the current production workflow."), FONT_BODY, fill=MUTED, gap=4)
        y += 145

    rounded(draw, (MARGIN, 1935, PAGE_W - MARGIN, 2120), fill=SOFT_GREEN)
    draw_wrapped(
        draw,
        MARGIN + 30,
        1975,
        PAGE_W - 2 * MARGIN - 60,
        "The important point for a non-technical reader is that the notebook is a guided explanation and validation layer. It loads the same final CSV and calls the same generator used to refresh the dashboard, report, figures, and recommendation outputs.",
        FONT_BODY,
        fill=INK,
    )
    draw_footer(draw, "Notebook source: PSID_NLP_Crisis_Module_Final.ipynb")
    return page


def page_architecture():
    page, draw = new_page(
        "Workflow Design Architecture",
        "How raw question text becomes ranked outputs, recommendations, and stakeholder-facing artifacts",
    )

    stages = [
        ("Historical question sources", ["Katrina", "COVID-19", "shutdown", "Understanding Society"], SOFT_BLUE),
        ("Final ranked CSV", ["authoritative question bank", "base columns: wording, source, toggle, keywords"], WHITE),
        ("NLP helpers", ["parse keywords", "tag crisis terms", "extract constructs"], SOFT_GREEN),
        ("Scoring layer", ["compute Ri", "compute Pi", "apply weights and bonuses"], SOFT_AMBER),
        ("Selection layer", ["keep Generic Core", "rank toggle questions", "respect 30-minute cap"], SOFT_BLUE),
        ("Output layer", ["dashboard", "report", "questionnaire demos", "figures and JSON"], WHITE),
    ]
    top = 330
    left = MARGIN
    w = 230
    h = 210
    gap = 30
    for idx, (title, bullets, fill) in enumerate(stages):
        x = left + idx * (w + gap)
        rounded(draw, (x, top, x + w, top + h), fill=fill)
        draw.text((x + 18, top + 18), title, font=FONT_H2, fill=NAVY)
        draw_bullets(draw, x + 18, top + 72, w - 36, bullets, FONT_SMALL, fill=INK, bullet_fill=BLUE, gap=8)
        if idx < len(stages) - 1:
            draw_arrow(draw, x + w, top + h // 2, x + w + gap - 6, top + h // 2)

    rounded(draw, (MARGIN, 680, PAGE_W - MARGIN, 1220), fill=WHITE)
    draw.text((MARGIN + 30, 720), "What each major function does", font=FONT_H1, fill=NAVY)
    function_boxes = [
        ("parse_keywords()", "Turns the stored keyword string into a clean list the code can use."),
        ("tag_keywords()", "Matches each keyword to the project taxonomy, such as Employment, Housing / Shelter, or Trauma / Health."),
        ("extract_constructs()", "Collects the construct labels for each question so the model knows which crisis dimensions that question covers."),
        ("load_dataset()", "Loads the CSV, derives selected flags and minutes, and sends the data into the enhanced scoring pipeline."),
        ("compute_augmented_scores()", "Calculates rarity, redundancy, construct bonus, portability, augmented utility, and final Pi."),
        ("build_all()", "Runs the full refresh path and writes the final stakeholder artifacts."),
    ]
    fx_y = 810
    for idx, (name, desc) in enumerate(function_boxes):
        col = idx % 2
        row = idx // 2
        x = MARGIN + 30 + col * 730
        y = fx_y + row * 135
        rounded(draw, (x, y, x + 670, y + 110), fill=SOFT_BLUE if col == 0 else SOFT_AMBER)
        draw.text((x + 18, y + 16), name, font=FONT_H2, fill=NAVY)
        draw_wrapped(draw, x + 18, y + 58, 634, desc, FONT_SMALL, fill=MUTED, gap=4)

    rounded(draw, (MARGIN, 1290, PAGE_W - MARGIN, 1750), fill=SOFT_GREEN)
    draw.text((MARGIN + 30, 1330), "How toggle decisions work", font=FONT_H1, fill=NAVY)
    draw_bullets(
        draw,
        MARGIN + 36,
        1410,
        PAGE_W - 2 * MARGIN - 72,
        [
            "The model does not invent crisis types from scratch. Each row already belongs to a routing group such as Generic Core, Financial Crisis, or Pandemic / Disaster.",
            "The scoring system ranks all rows, then the final selection keeps the small always-on Generic Core and fills the remaining time with the highest-value crisis-specific rows.",
            "In the current final module, the Pandemic / Disaster toggle dominates because Katrina and COVID questions contribute many strong housing, trauma, and aid signals.",
        ],
        FONT_BODY,
        fill=INK,
        bullet_fill=GREEN,
    )
    draw_footer(draw, "Architecture sources: generate_psid_artifacts.py and PSID_NLP_Crisis_Module_Structure.py")
    return page


def page_formulas():
    page, draw = new_page(
        "Formula Calculations In Plain Language",
        "The scoring system first asks which questions are useful for the least burden, then improves that ranking for deployability",
    )

    rounded(draw, (MARGIN, 190, 780, 1120), fill=WHITE)
    rounded(draw, (850, 190, PAGE_W - MARGIN, 1120), fill=WHITE)
    draw.text((MARGIN + 30, 230), "1. Baseline ranking: Ri", font=FONT_H1, fill=NAVY)
    draw_code_box(draw, MARGIN + 30, 310, 620, 120, "Ri = Ui / Bi", fill=SOFT_BLUE)
    draw_code_box(draw, MARGIN + 30, 470, 620, 120, "Bi = max(0.10 * word_count + 0.20 * complexity, 0.1)", fill=SOFT_AMBER)
    draw_bullets(
        draw,
        MARGIN + 36,
        640,
        640,
        [
            "Utility means how much crisis-relevant information a question gives us.",
            "Burden means how much time or effort that question costs a respondent.",
            "A short, high-value question gets a high Ri.",
            "A long or complicated question gets penalized through Bi.",
        ],
        FONT_BODY,
        fill=INK,
        bullet_fill=BLUE,
    )

    draw.text((880, 230), "2. Enhanced priority: Pi", font=FONT_H1, fill=NAVY)
    draw_code_box(draw, 880, 310, 620, 150, "Pi = augmented_utility / [Bi * (1 + 0.65 * redundancy_scaled)]", fill=SOFT_BLUE)
    draw_code_box(draw, 880, 500, 620, 170, "augmented_utility = Ui * (1 + 0.32 * idf_scaled + 0.24 * construct_scaled + 0.12 * richness_scaled + portability_bonus)", fill=SOFT_AMBER)
    draw_bullets(
        draw,
        886,
        720,
        594,
        [
            "0.32 rewards rare wording, because unique language often signals unique information.",
            "0.24 rewards stronger construct bonus, so questions covering more important crisis dimensions rise.",
            "0.12 rewards richness, meaning one question covering several important ideas gets extra credit.",
            "0.65 penalizes redundancy, so near-duplicate questions do not crowd out the shortlist.",
        ],
        FONT_BODY,
        fill=INK,
        bullet_fill=RED,
    )

    rounded(draw, (MARGIN, 1185, PAGE_W - MARGIN, 2000), fill=SOFT_GREEN)
    draw.text((MARGIN + 30, 1225), "A non-technical way to read the formulas", font=FONT_H1, fill=NAVY)
    draw_bullets(
        draw,
        MARGIN + 36,
        1310,
        PAGE_W - 2 * MARGIN - 72,
        [
            "Ri asks: how much useful information do we get per unit of respondent effort?",
            "Pi asks: after we account for rarity, construct strength, portability, and repetition, which questions are the best ones to keep?",
            "This means a question can have a solid Ri but still move down if it is repetitive, too source-specific, or weak on important constructs.",
            "Likewise, a question can move up if it covers a high-priority construct in a clean and portable way.",
        ],
        FONT_BODY,
        fill=INK,
        bullet_fill=GREEN,
    )
    draw_footer(draw, "Formulas from compute_augmented_scores() and constants from PSID_NLP_Crisis_Module_Structure.py")
    return page


def page_construct_bonus():
    page, draw = new_page(
        "Construct Bonus, Weights, And Why They Matter",
        "The construct bonus is where rarity, priority, and richness come together",
    )

    rounded(draw, (MARGIN, 190, 860, 1280), fill=WHITE)
    rounded(draw, (920, 190, PAGE_W - MARGIN, 1280), fill=WHITE)
    rounded(draw, (MARGIN, 1340, PAGE_W - MARGIN, 2050), fill=SOFT_AMBER)

    draw.text((MARGIN + 30, 230), "How construct_bonus() is computed", font=FONT_H1, fill=NAVY)
    draw_bullets(
        draw,
        MARGIN + 36,
        320,
        700,
        [
            "Rarity: the model checks how often each construct appears across all questions. Less common constructs receive more credit.",
            "Priority: the model looks up the construct weights in the CONSTRUCT_PRIORITY dictionary and averages them for the constructs attached to the question.",
            "Richness: the model counts how many unique constructs a question covers and adds a small bonus for broader coverage.",
        ],
        FONT_BODY,
        fill=INK,
        bullet_fill=BLUE,
    )
    draw_code_box(
        draw,
        MARGIN + 30,
        720,
        700,
        220,
        "rarity = mean(1 / construct_frequency) * N\npriority = mean(CONSTRUCT_PRIORITY[name])\nrichness = len(unique constructs)\nconstruct_bonus = rarity + priority + 0.08 * richness",
        fill=SOFT_BLUE,
    )
    draw_wrapped(
        draw,
        MARGIN + 36,
        980,
        700,
        "In plain English: a question gets extra credit if it touches a rare construct, touches a high-priority construct, or covers several important constructs at once.",
        FONT_BODY,
        fill=MUTED,
    )

    draw.text((950, 230), "Construct-priority weights", font=FONT_H1, fill=NAVY)
    weights = [
        ("Trauma / Health", 0.58),
        ("Housing / Shelter", 0.55),
        ("Government Aid", 0.48),
        ("Financial Coping", 0.45),
        ("Employment", 0.42),
        ("Economic / Income", 0.40),
        ("Demographics", 0.14),
    ]
    y = 340
    for name, value in weights:
        draw.text((950, y), name, font=FONT_BODY_BOLD, fill=INK)
        rounded(draw, (1240, y - 8, 1500, y + 42), fill=(242, 246, 252))
        fill_width = int(260 * (value / 0.58))
        rounded(draw, (1240, y - 8, 1240 + fill_width, y + 42), fill=BLUE)
        draw.text((1460, y), f"{value:.2f}", font=FONT_BODY_BOLD, fill=WHITE if fill_width > 120 else NAVY)
        y += 98

    draw.text((MARGIN + 30, 1380), "Portability bonus and redundancy penalty", font=FONT_H1, fill=NAVY)
    draw_bullets(
        draw,
        MARGIN + 36,
        1470,
        PAGE_W - 2 * MARGIN - 72,
        [
            "Portability bonus rewards wording that can be reused across crisis types. Generic-core questions with non-source-specific wording get the biggest bonus.",
            "Redundancy penalty lowers the score of questions that are too similar to other questions, using cosine similarity over TF-IDF vectors.",
            "This matters because the project is not trying to keep every good question. It is trying to keep a compact set of distinct, high-value questions.",
        ],
        FONT_BODY,
        fill=INK,
        bullet_fill=AMBER,
    )
    draw_code_box(
        draw,
        MARGIN + 30,
        1770,
        PAGE_W - 2 * MARGIN - 60,
        170,
        "Generic Core and no source-specific term -> 0.16\nGeneric Core and source-specific term -> 0.03\nToggle item and no source-specific term -> 0.08\nToggle item and source-specific term -> 0.02",
        fill=WHITE,
    )
    draw_footer(draw, "Weights and construct bonus come from CONSTRUCT_PRIORITY and compute_augmented_scores()")
    return page


def page_examples(df: pd.DataFrame):
    page, draw = new_page(
        "Examples A Non-Technical Audience Can Follow",
        "These examples show how the same scoring logic treats a generic-core question, a financial toggle question, and a pandemic/disaster question",
    )

    generic, financial, specific = get_examples(df)
    examples = [
        (
            "Generic Core example",
            generic,
            "This question stays in the always-on core because it is short, easy to ask, and useful across almost any crisis type.",
            BLUE,
        ),
        (
            "Financial Crisis toggle example",
            financial,
            "This question is longer, but it stays valuable because it captures how households actually cope with financial shock, not just whether hardship happened.",
            AMBER,
        ),
        (
            "Pandemic / Disaster example",
            specific,
            "This question scores very highly because it is compact, clear, and covers strong crisis exposure signals without much burden.",
            RED,
        ),
    ]

    top = 240
    for idx, (title, row, explainer, accent) in enumerate(examples):
        x = MARGIN + idx * 500
        rounded(draw, (x, top, x + 460, top + 1220), fill=WHITE)
        draw.rectangle((x, top, x + 460, top + 14), fill=accent)
        draw.text((x + 24, top + 32), title, font=FONT_H1, fill=NAVY)
        draw_wrapped(draw, x + 24, top + 110, 412, str(row["recommended_wording"]), FONT_BODY_BOLD, fill=INK)
        draw_bullets(
            draw,
            x + 24,
            top + 240,
            412,
            [
                f"Source: {row['source']}",
                f"Toggle category: {row['toggle_category']}",
                f"Constructs: {', '.join(row['constructs'])}",
                f"Ri = {row['Ri']:.3f}",
                f"Pi = {row['Pi']:.3f}",
            ],
            FONT_SMALL,
            fill=INK,
            bullet_fill=accent,
            gap=10,
        )
        rounded(draw, (x + 24, top + 560, x + 436, top + 760), fill=SOFT_BLUE)
        draw_wrapped(draw, x + 42, top + 590, 376, explainer, FONT_SMALL, fill=MUTED)
        draw_wrapped(
            draw,
            x + 24,
            top + 810,
            412,
            "Why this is helpful for a non-technical reader:",
            FONT_BODY_BOLD,
            fill=NAVY,
        )
        draw_bullets(
            draw,
            x + 24,
            top + 860,
            412,
            [
                "You can see that high-ranking questions are not always the longest or most detailed ones.",
                "The model prefers questions that say something important clearly and without repeating what other questions already capture.",
            ],
            FONT_SMALL,
            fill=INK,
            bullet_fill=accent,
            gap=8,
        )

    draw_footer(draw, "Examples taken directly from PSID_Ranked_Questions_Final.csv after load_dataset() and compute_augmented_scores()")
    return page


def page_selection_and_outputs(summary: dict):
    page, draw = new_page(
        "How The Final Module Is Selected And Refreshed",
        "The workflow keeps a compact always-on core, then spends the remaining time budget on the strongest crisis-specific questions",
    )

    rounded(draw, (MARGIN, 190, PAGE_W - MARGIN, 930), fill=WHITE)
    draw.text((MARGIN + 30, 230), "Selection logic in plain language", font=FONT_H1, fill=NAVY)
    draw_bullets(
        draw,
        MARGIN + 36,
        315,
        PAGE_W - 2 * MARGIN - 72,
        [
            "The Generic Core is intentionally small because it must work across many crisis types.",
            "The model then fills the remaining time budget with the highest-value crisis-specific questions.",
            "In the current final module, the Pandemic / Disaster bank wins most of that space because Katrina and COVID contribute many strong housing, trauma, and aid items.",
            "The Financial Crisis toggle is represented by the strongest available coping question in the current scored bank.",
        ],
        FONT_BODY,
        fill=INK,
        bullet_fill=BLUE,
    )

    rounded(draw, (MARGIN + 30, 640, PAGE_W - MARGIN - 30, 880), fill=SOFT_GREEN)
    draw_bullets(
        draw,
        MARGIN + 60,
        680,
        PAGE_W - 2 * MARGIN - 120,
        [
            f"Final result: {summary['selected_rows']} selected questions in {summary['selected_minutes']:.2f} minutes.",
            f"Generic Core selected: {summary['selected_toggle_counts']['Generic Core']} questions.",
            f"Financial Crisis selected: {summary['selected_toggle_counts']['Toggle: Financial Crisis']} question.",
            f"Pandemic / Disaster selected: {summary['selected_toggle_counts']['Toggle: Pandemic / Disaster']} questions.",
        ],
        FONT_BODY,
        fill=INK,
        bullet_fill=GREEN,
    )

    rounded(draw, (MARGIN, 1010, PAGE_W - MARGIN, 1960), fill=SOFT_BLUE)
    draw.text((MARGIN + 30, 1050), "What build_all() refreshes", font=FONT_H1, fill=NAVY)
    outputs = [
        "writes the ranked CSV with enhanced scoring fields",
        "writes psid_artifact_summary.json with headline benchmark values",
        "writes psid_dashboard_data.js for the browser dashboard",
        "regenerates the five main figures",
        "keeps the dashboard, report, notebook, and demos aligned to the same ranked-question workflow",
    ]
    draw_bullets(draw, MARGIN + 36, 1130, PAGE_W - 2 * MARGIN - 72, outputs, FONT_BODY, fill=INK, bullet_fill=BLUE)
    draw_code_box(
        draw,
        MARGIN + 30,
        1470,
        PAGE_W - 2 * MARGIN - 60,
        240,
        "build_all()\n  -> _style_matplotlib()\n  -> load_dataset()\n  -> build_summary(df)\n  -> write_ranked_csv(df)\n  -> write_dashboard_data(df, summary)\n  -> plot_* functions\n  -> save_aliases()",
        fill=WHITE,
    )
    draw_wrapped(
        draw,
        MARGIN + 30,
        1760,
        PAGE_W - 2 * MARGIN - 60,
        "This is why the notebook emphasizes build_all() as the only supported refresh path: it reduces drift and ensures that all public-facing artifacts point back to the same final ranked CSV.",
        FONT_BODY,
        fill=MUTED,
    )
    draw_footer(draw, "Refresh path documented in PSID_NLP_Crisis_Module_Final.ipynb and implemented in build_all()")
    return page


def main():
    summary = json.loads(SUMMARY_PATH.read_text())
    sections = load_notebook_sections()
    df = artifacts.load_dataset()

    pages = [
        page_cover(summary),
        page_notebook_walkthrough(sections),
        page_architecture(),
        page_formulas(),
        page_construct_bonus(),
        page_examples(df),
        page_selection_and_outputs(summary),
    ]

    pages[0].save(OUTPUT_PATH, "PDF", resolution=150.0, save_all=True, append_images=pages[1:])
    print(f"Wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()