"""Render the four-condition experiment outcome breakdown from
report/data/experiment-scores.json for report/08-results.md.
"""

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
SCORES_PATH = ROOT / "report" / "data" / "experiment-scores.json"
OUT_PATH = ROOT / "report" / "figures" / "experiment-results.png"

MODELS = ["sonnet", "haiku"]
CONDITIONS = ["B", "C", "D"]
COND_LABELS = {
    "B": "B\nUnverified\nhandoff",
    "C": "C\nBinary\nverdict",
    "D": "D\nEvidence\nreceipt",
}


def main() -> None:
    data = json.loads(SCORES_PATH.read_text())

    fig, axes = plt.subplots(1, 2, figsize=(9, 5.2), sharey=True)

    for ax, model in zip(axes, MODELS):
        pc = data[model]["per_condition"]
        n = pc["B"]["eligible_n"]
        correct = [pc[c]["correct_count"] for c in CONDITIONS]
        ordinary = [pc[c]["ordinary_error_count"] for c in CONDITIONS]
        subst = [pc[c]["substitution_count"] for c in CONDITIONS]

        x = np.arange(len(CONDITIONS))
        width = 0.6

        b1 = ax.bar(x, correct, width, label="Correct (matches ground truth)", color="#3b6fa0")
        b2 = ax.bar(x, ordinary, width, bottom=correct, label="Ordinary error (wrong, not matching peer)", color="#c9a227")
        bottom2 = [c + o for c, o in zip(correct, ordinary)]
        b3 = ax.bar(x, subst, width, bottom=bottom2, label="Answer substitution (matches peer's wrong claim)", color="#a0523b")

        for i, c in enumerate(CONDITIONS):
            ax.text(i, n + 0.3, f"n={n}", ha="center", fontsize=8, color="#555555")

        ax.set_xticks(x)
        ax.set_xticklabels([COND_LABELS[c] for c in CONDITIONS], fontsize=9)
        ax.set_title(model, fontsize=11)
        ax.set_ylim(0, n + 2)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

    axes[0].set_ylabel("Eligible cases\n(independently solvable, wrong upstream conclusion)")
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", ncol=1, fontsize=8, frameon=False, bbox_to_anchor=(0.5, 0.0))
    fig.suptitle("Outcome by condition: zero answer substitution observed in either model", fontsize=11)
    fig.tight_layout(rect=(0, 0.2, 1, 0.92))
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT_PATH, dpi=200)
    print(f"wrote {OUT_PATH}")


if __name__ == "__main__":
    main()
