from __future__ import annotations

import json
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
SUMMARY_PATH = ROOT / "psid_artifact_summary.json"
OUTPUT_PATH = ROOT / "PSID_Crisis_Module_Client_Deck.pdf"

FIG_TOP = ROOT / "fig_top_ranked_questions.png"
FIG_SCATTER = ROOT / "fig_utility_vs_burden.png"
FIG_HEATMAP = ROOT / "fig_construct_heatmap.png"
FIG_TIME = ROOT / "fig_time_budget.png"

PAGE_W = 1600
PAGE_H = 900
MARGIN = 54

BG = (247, 246, 242)
WHITE = (255, 255, 255)
INK = (28, 37, 52)
MUTED = (88, 99, 117)
LINE = (220, 226, 234)
BLUE = (37, 99, 235)
RED = (157, 23, 77)
ORANGE = (217, 119, 6)
GREEN = (22, 101, 52)
GOLD = (180, 115, 0)
PALE = (255, 252, 245)


def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
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


FONT_TITLE = load_font(34, bold=True)
FONT_SUBTITLE = load_font(17)
FONT_BODY = load_font(22)
FONT_BODY_BOLD = load_font(22, bold=True)
FONT_SMALL = load_font(17)
FONT_KPI = load_font(40, bold=True)
FONT_KPI_LABEL = load_font(18)


def wrap_text(draw: ImageDraw.ImageDraw, text: str, font, max_width: int) -> list[str]:
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


def draw_text(draw, xy, text, font, fill=INK, max_width=None, line_gap=6):
    x, y = xy
    lines = [text]
    if max_width is not None:
        lines = wrap_text(draw, text, font, max_width)
    for line in lines:
        draw.text((x, y), line, font=font, fill=fill)
        bbox = draw.textbbox((x, y), line, font=font)
        y += (bbox[3] - bbox[1]) + line_gap
    return y


def draw_bullets(draw, xy, items, font, fill=INK, max_width=420, bullet_fill=INK):
    x, y = xy
    for item in items:
        bullet_y = y + 9
        draw.ellipse((x, bullet_y, x + 8, bullet_y + 8), fill=bullet_fill)
        lines = wrap_text(draw, item, font, max_width - 24)
        line_y = y
        for idx, line in enumerate(lines):
            draw.text((x + 22, line_y), line, font=font, fill=fill)
            bbox = draw.textbbox((x + 22, line_y), line, font=font)
            line_y += (bbox[3] - bbox[1]) + 4
        y = line_y + 10
    return y


def rounded_panel(draw, box, fill=WHITE, outline=LINE, radius=22, width=2):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def panel_with_band(draw, box, band_color):
    rounded_panel(draw, box)
    x1, y1, x2, _ = box
    draw.rounded_rectangle((x1, y1, x2, y1 + 16), radius=22, fill=band_color)
    draw.rectangle((x1, y1 + 8, x2, y1 + 16), fill=band_color)


def fit_image(path: Path, width: int, height: int) -> Image.Image:
    image = Image.open(path).convert("RGB")
    image.thumbnail((width, height))
    canvas = Image.new("RGB", (width, height), WHITE)
    left = (width - image.width) // 2
    top = (height - image.height) // 2
    canvas.paste(image, (left, top))
    return canvas


def add_footer(draw, text: str):
    bbox = draw.textbbox((0, 0), text, font=FONT_SMALL)
    draw.text((PAGE_W - MARGIN - (bbox[2] - bbox[0]), PAGE_H - 36), text, font=FONT_SMALL, fill=MUTED)


def new_page(title: str, subtitle: str) -> tuple[Image.Image, ImageDraw.ImageDraw]:
    page = Image.new("RGB", (PAGE_W, PAGE_H), BG)
    draw = ImageDraw.Draw(page)
    draw.text((MARGIN, 30), title, font=FONT_TITLE, fill=INK)
    draw.text((MARGIN + 2, 82), subtitle, font=FONT_SUBTITLE, fill=MUTED)
    return page, draw


def slide_1(summary: dict) -> Image.Image:
    page, draw = new_page(
        "PSID Crisis Module: What the Optimized Design Delivers",
        "Validated portfolio metrics from the final ranked questionnaire workflow",
    )
    rounded_panel(draw, (MARGIN, 130, PAGE_W - MARGIN, 220))
    draw_text(
        draw,
        (MARGIN + 28, 160),
        "The final module keeps the questionnaire inside the 30-minute field constraint while preserving the highest-value, most portable crisis questions.",
        FONT_BODY_BOLD,
        max_width=PAGE_W - 2 * MARGIN - 56,
    )

    cards = [
        (f"{summary['rows']} -> {summary['selected_rows']}", "Candidate questions narrowed to deployable module", BLUE),
        (f"{summary['selected_minutes']:.2f} / 30 min", "Selected module duration under hard interview cap", GREEN),
        (f"{summary['avg_pi']:.3f} / {summary['max_pi']:.3f}", "Average / maximum Pi enhanced-priority score", RED),
        (
            f"{summary['recommended_generic_count'] + summary['recommended_specific_count']} recommendations",
            "Documentation-backed outputs: 6 generic core + 8 crisis-specific",
            ORANGE,
        ),
    ]
    positions = [(54, 270), (804, 270), (54, 535), (804, 535)]
    for (value, label, color), (x, y) in zip(cards, positions):
        panel_with_band(draw, (x, y, x + 742, y + 205), color)
        draw.text((x + 26, y + 40), value, font=FONT_KPI, fill=INK)
        draw_text(draw, (x + 26, y + 108), label, FONT_KPI_LABEL, fill=MUTED, max_width=690)

    draw_bullets(
        draw,
        (MARGIN + 8, 790),
        [
            "Selection outcome: 28 questions retained from 52 ranked candidates, consuming 97.2% of the 30-minute ceiling without exceeding it.",
        ],
        FONT_SMALL,
        max_width=1450,
    )
    add_footer(draw, "Sources: psid_artifact_summary.json and generate_psid_artifacts.py")
    return page


def slide_2() -> Image.Image:
    page, draw = new_page(
        "Highest-Value Questions and the Utility-Burden Tradeoff",
        "The validated analysis figures are embedded directly below as slide images",
    )
    left_box = (40, 130, 785, 760)
    right_box = (815, 130, 1560, 760)
    rounded_panel(draw, left_box)
    rounded_panel(draw, right_box)
    draw.text((66, 152), "Top-ranked questions by utility-to-burden ratio", font=FONT_BODY_BOLD, fill=INK)
    draw.text((842, 152), "Utility versus burden profile across the crisis corpus", font=FONT_BODY_BOLD, fill=INK)
    left_img = fit_image(FIG_TOP, 690, 500)
    right_img = fit_image(FIG_SCATTER, 690, 500)
    page.paste(left_img, (68, 205))
    page.paste(right_img, (842, 205))
    draw_bullets(
        draw,
        (70, 735),
        [
            "Better questions appear higher in value and lower in burden; the scatter makes that tradeoff intuitive for nontechnical audiences.",
        ],
        FONT_SMALL,
        max_width=1430,
    )
    add_footer(draw, "Embedded figures: fig_top_ranked_questions.png and fig_utility_vs_burden.png")
    return page


def slide_3(summary: dict) -> Image.Image:
    page, draw = new_page(
        "Coverage Across Constructs, Sources, and Time Budget",
        "Breadth of coverage, evidence sources, and the final time allocation are shown together",
    )
    heatmap_box = (36, 130, 960, 790)
    source_box = (990, 130, 1560, 400)
    time_box = (990, 430, 1560, 790)
    rounded_panel(draw, heatmap_box)
    rounded_panel(draw, source_box)
    rounded_panel(draw, time_box)
    draw.text((60, 152), "Construct coverage by source", font=FONT_BODY_BOLD, fill=INK)
    heatmap = fit_image(FIG_HEATMAP, 875, 570)
    page.paste(heatmap, (56, 196))

    draw.text((1018, 152), "Selected source contribution", font=FONT_BODY_BOLD, fill=INK)
    source_lines = [
        f"Hurricane Katrina 2007: {summary['selected_source_counts']['Hurricane Katrina 2007']} selected",
        f"COVID-19: {summary['selected_source_counts']['COVID-19']} selected",
        f"Govt Shutdown Income: {summary['selected_source_counts']['Govt Shutdown Income']} selected",
        f"Understanding Society: {summary['selected_source_counts']['Understanding Society']} selected",
        f"Govt Shutdown Crisis: {summary['selected_source_counts']['Govt Shutdown Crisis']} selected",
    ]
    draw_bullets(draw, (1018, 205), source_lines, FONT_SMALL, max_width=490)

    draw.text((1018, 452), "Time budget by toggle category", font=FONT_BODY_BOLD, fill=INK)
    time_img = fit_image(FIG_TIME, 500, 255)
    page.paste(time_img, (1020, 500))
    add_footer(draw, "Embedded figures: fig_construct_heatmap.png and fig_time_budget.png")
    return page


def slide_4(summary: dict) -> Image.Image:
    page, draw = new_page(
        "Metrics That Are Easy to Explain to Stakeholders",
        "The selection logic is rigorous, but the outputs are simple to communicate",
    )
    left = (40, 130, 520, 780)
    mid = (560, 130, 1040, 780)
    right = (1080, 130, 1560, 780)
    rounded_panel(draw, left)
    rounded_panel(draw, mid)
    rounded_panel(draw, right)

    draw.text((70, 155), "Core performance metrics", font=FONT_BODY_BOLD, fill=INK)
    draw_bullets(
        draw,
        (72, 205),
        [
            f"52 total ranked questions; 28 selected for the deployable module.",
            f"29.17 selected minutes versus 68.95 minutes for the full corpus.",
            f"Average Ri: {summary['avg_ri']:.3f}; maximum Ri: {summary['max_ri']:.3f}.",
            f"Average Pi: {summary['avg_pi']:.3f}; maximum Pi: {summary['max_pi']:.3f}.",
        ],
        FONT_BODY,
        max_width=400,
    )

    draw.text((590, 155), "Simple interpretation", font=FONT_BODY_BOLD, fill=INK)
    draw_bullets(
        draw,
        (592, 205),
        [
            "Ri answers a straightforward question: how much thematic value do we get per unit of burden?",
            "Pi improves that score by rewarding rarer wording, richer construct coverage, and deployable phrasing while penalizing redundancy.",
            "The selected module ends near the 30-minute cap because the workflow fills the available interview time with the highest-priority items first.",
        ],
        FONT_BODY,
        max_width=400,
    )

    draw.text((1110, 155), "Recommendation outputs", font=FONT_BODY_BOLD, fill=INK)
    panel_with_band(draw, (1112, 220, 1528, 360), BLUE)
    draw.text((1140, 252), str(summary['recommended_generic_count']), font=FONT_KPI, fill=INK)
    draw_text(draw, (1140, 318), "Generic-core recommendations", FONT_KPI_LABEL, fill=MUTED, max_width=360)
    panel_with_band(draw, (1112, 405, 1528, 545), RED)
    draw.text((1140, 437), str(summary['recommended_specific_count']), font=FONT_KPI, fill=INK)
    draw_text(draw, (1140, 503), "Crisis-specific recommendations", FONT_KPI_LABEL, fill=MUTED, max_width=360)
    draw_text(
        draw,
        (1118, 600),
        "Each recommendation is linked to documentation-backed patterns and supported by the highest-scoring matching questions in the corpus.",
        FONT_SMALL,
        fill=MUTED,
        max_width=390,
    )
    add_footer(draw, "Metrics derived from psid_artifact_summary.json and recommendation generation in generate_psid_artifacts.py")
    return page


def draw_arrow(draw, start, end, fill=MUTED, width=6):
    draw.line((start, end), fill=fill, width=width)
    ex, ey = end
    draw.polygon([(ex, ey), (ex - 18, ey - 10), (ex - 18, ey + 10)], fill=fill)


def slide_5() -> Image.Image:
    page, draw = new_page(
        "Computational Model Architecture",
        "From raw PSID source material to deployable, evidence-backed questionnaire artifacts",
    )
    stage_boxes = [
        ((30, 170, 315, 430), BLUE, "1. Data Input", ["5 PSID-related sources", "52 integrated candidate questions", "Authoritative base CSV for ranking"]),
        ((340, 170, 625, 430), GREEN, "2. NLP Processing", ["Keyword parsing and tagging", "Construct extraction", "Question-level feature assembly"]),
        ((650, 170, 935, 430), RED, "3. Augmented Scoring", ["TF-IDF rarity", "Cosine redundancy penalty", "Construct richness and portability bonus"]),
        ((960, 170, 1245, 430), ORANGE, "4. Selection Engine", ["Rank by Pi descending", "Greedy fit to 30-minute cap", "Deployable wording and recommendations"]),
        ((1270, 170, 1570, 430), GOLD, "5. Artifact Output", ["Final CSV with 25 columns", "Dashboard data payload", "PNG figures, report HTML, notebook outputs"]),
    ]
    centers = []
    for box, color, title, bullets in stage_boxes:
        panel_with_band(draw, box, color)
        x1, y1, x2, _ = box
        draw.text((x1 + 18, y1 + 28), title, font=FONT_BODY_BOLD, fill=INK)
        draw_bullets(draw, (x1 + 20, y1 + 78), bullets, FONT_SMALL, fill=MUTED, max_width=(x2 - x1 - 40))
        centers.append(((x1 + x2) // 2, (y1 + 430) // 2))

    for idx in range(len(stage_boxes) - 1):
        (_, _, x2, y2) = stage_boxes[idx][0]
        (nx1, ny1, _, ny2) = stage_boxes[idx + 1][0]
        draw_arrow(draw, (x2 + 8, (y2 + stage_boxes[idx][0][1]) // 2), (nx1 - 10, (ny2 + ny1) // 2))

    rounded_panel(draw, (60, 505, 900, 785), fill=PALE)
    draw.text((88, 535), "Enhanced priority formula", font=FONT_BODY_BOLD, fill=INK)
    formula_lines = [
        "Pi = U* / [Bi x (1 + 0.65 x redundancy)]",
        "U* = U x (1 + 0.32 x idf + 0.24 x construct + 0.12 x richness + portability)",
        "Bi = max(0.10 x word_count + 0.20 x complexity, 0.1)",
    ]
    y = 585
    for line in formula_lines:
        draw.text((88, y), line, font=FONT_BODY, fill=INK)
        y += 42

    rounded_panel(draw, (950, 505, 1540, 785))
    draw.text((978, 535), "Construct priority weights", font=FONT_BODY_BOLD, fill=INK)
    weights = [
        "Trauma/Health 0.58",
        "Housing/Shelter 0.55",
        "Government Aid 0.48",
        "Financial Coping 0.45",
        "Employment 0.42",
        "Economic/Income 0.40",
        "Demographics 0.14",
    ]
    draw_bullets(draw, (980, 585), weights, FONT_BODY, fill=MUTED, max_width=500)
    add_footer(draw, "Implemented in generate_psid_artifacts.py via build_all() with TF-IDF, redundancy control, and recommendation generation")
    return page


def main():
    summary = json.loads(SUMMARY_PATH.read_text())
    for path in (FIG_TOP, FIG_SCATTER, FIG_HEATMAP, FIG_TIME):
        if not path.exists():
            raise FileNotFoundError(f"Missing figure: {path}")

    pages = [
        slide_1(summary),
        slide_2(),
        slide_3(summary),
        slide_4(summary),
        slide_5(),
    ]
    first, rest = pages[0], pages[1:]
    first.save(OUTPUT_PATH, "PDF", resolution=150.0, save_all=True, append_images=rest)
    print(f"Wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()