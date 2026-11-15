"""Render Citation Binder per-category precision/recall/F1 from
report/data/citation-binder-scores.json for report/06-citation-binder-implementation.md.
"""

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
SCORES_PATH = ROOT / "report" / "data" / "citation-binder-scores.json"
OUT_PATH = ROOT / "report" / "figures" / "citation-binder-scores.png"

LABELS = {
    "fully_supported": "Fully\nsupported",
    "partially_supported": "Partially\nsupported",
    "contradicted": "Contradicted",
    "unsupported": "Unsupported",
}


def main() -> None:
    data = json.loads(SCORES_PATH.read_text())["semantic"]
    cats = list(LABELS.keys())
    per_cat = data["per_category"]

    precision = [per_cat[c]["precision"] for c in cats]
    recall = [per_cat[c]["recall"] for c in cats]
    f1 = [per_cat[c]["f1"] for c in cats]

    x = np.arange(len(cats))
    width = 0.25

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.bar(x - width, precision, width, label="Precision", color="#3b6fa0")
    ax.bar(x, recall, width, label="Recall", color="#6d8fb0")
    ax.bar(x + width, f1, width, label="F1", color="#a0523b")

    ax.set_xticks(x)
    ax.set_xticklabels([LABELS[c] for c in cats])
    ax.set_ylim(0, 1.15)
    ax.set_ylabel("Score")
    ax.set_title(
        "Citation Binder accuracy by category\n"
        f"(overall accuracy {data['overall_accuracy']:.0%}, macro F1 {data['macro_f1']:.2f}, n=24)"
    )
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.18), fontsize=9, ncol=3, frameon=False)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.axhline(1.0, color="#999999", linewidth=0.5, linestyle="--")

    fig.tight_layout(rect=(0, 0.1, 1, 1))
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT_PATH, dpi=200)
    print(f"wrote {OUT_PATH}")


if __name__ == "__main__":
    main()
