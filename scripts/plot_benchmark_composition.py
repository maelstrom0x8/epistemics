"""Render the benchmark corpus composition described in report/04-methodology.md
Section 4.4, from the case data in report/data/benchmark-cases.json, as a figure
for report/05-benchmark-construction.md.
"""

import json
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "report" / "data" / "benchmark-cases.json"
OUT_PATH = ROOT / "report" / "figures" / "benchmark-composition.png"

LABELS = {
    "fully_supported": "Fully\nsupported",
    "partially_supported": "Partially\nsupported",
    "contradicted": "Contradicted",
    "unsupported": "Unsupported",
}

COLOR_SEMANTIC = "#3b6fa0"
COLOR_RETRIEVAL = "#a0523b"


def main() -> None:
    data = json.loads(DATA_PATH.read_text())
    semantic = data["semantic_cases"]
    retrieval = data["retrieval_failure_cases"]

    counts = {key: 0 for key in LABELS}
    for case in semantic:
        counts[case["category"]] += 1

    retrieval_modes = {}
    for case in retrieval:
        retrieval_modes[case["failure_mode"]] = retrieval_modes.get(case["failure_mode"], 0) + 1

    fig, (ax_left, ax_right) = plt.subplots(
        1, 2, figsize=(9, 4), gridspec_kw={"width_ratios": [4, 3]}
    )

    cats = list(LABELS.keys())
    values = [counts[c] for c in cats]
    bars = ax_left.bar([LABELS[c] for c in cats], values, color=COLOR_SEMANTIC)
    ax_left.set_title("Semantic cases by category (n=%d)" % sum(values))
    ax_left.set_ylabel("Number of cases")
    ax_left.set_ylim(0, max(values) + 2)
    for bar, value in zip(bars, values):
        ax_left.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.1,
            str(value),
            ha="center",
            va="bottom",
            fontsize=10,
        )
    ax_left.spines["top"].set_visible(False)
    ax_left.spines["right"].set_visible(False)

    modes = list(retrieval_modes.keys())
    mode_labels = [m.replace("_", "\n") for m in modes]
    mode_values = [retrieval_modes[m] for m in modes]
    provenance_by_mode = {
        c["failure_mode"]: c["provenance"] for c in retrieval
    }
    colors = [
        "#6d8fb0" if provenance_by_mode[m] == "real" else COLOR_RETRIEVAL for m in modes
    ]
    bars2 = ax_right.bar(mode_labels, mode_values, color=colors)
    ax_right.set_title("Retrieval-failure cases by mode (n=%d)" % sum(mode_values))
    ax_right.set_ylim(0, max(mode_values) + 1)
    for bar, value in zip(bars2, mode_values):
        ax_right.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.05,
            str(value),
            ha="center",
            va="bottom",
            fontsize=10,
        )
    ax_right.spines["top"].set_visible(False)
    ax_right.spines["right"].set_visible(False)

    handles = [
        plt.Rectangle((0, 0), 1, 1, color="#6d8fb0"),
        plt.Rectangle((0, 0), 1, 1, color=COLOR_RETRIEVAL),
    ]
    ax_right.legend(
        handles,
        ["Logged from this study's own fetch attempts", "Engineered fixture"],
        fontsize=7,
        loc="upper right",
        frameon=False,
    )

    fig.suptitle("Benchmark corpus composition (30 cases total)", fontsize=12)
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT_PATH, dpi=200)
    print(f"wrote {OUT_PATH}")


if __name__ == "__main__":
    main()
