"""Score the Citation Binder's predictions (report/data/citation-binder-predictions.json)
against the hand-authored ground truth (report/data/benchmark-cases.json), per the
evaluation design in report/04-methodology.md Section 4.6.
"""

import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GROUND_TRUTH_PATH = ROOT / "report" / "data" / "benchmark-cases.json"
PREDICTIONS_PATH = ROOT / "report" / "data" / "citation-binder-predictions.json"
OUT_PATH = ROOT / "report" / "data" / "citation-binder-scores.json"

CATEGORIES = ["fully_supported", "partially_supported", "contradicted", "unsupported"]
# Ground truth uses "fully_supported" / "unsupported"; predictions use "supported" / "insufficient".
LABEL_MAP = {
    "fully_supported": "supported",
    "partially_supported": "partially_supported",
    "contradicted": "contradicted",
    "unsupported": "insufficient",
}
REVERSE_LABEL_MAP = {v: k for k, v in LABEL_MAP.items()}


def load():
    gt = json.loads(GROUND_TRUTH_PATH.read_text())
    pred = json.loads(PREDICTIONS_PATH.read_text())
    return gt, pred


def score_semantic(gt, pred):
    gt_by_id = {c["id"]: c for c in gt["semantic_cases"]}
    pred_by_id = {c["id"]: c for c in pred["semantic_predictions"]}

    missing = set(gt_by_id) - set(pred_by_id)
    extra = set(pred_by_id) - set(gt_by_id)

    rows = []
    confusion = defaultdict(lambda: defaultdict(int))
    relevance_correct = 0
    relevance_total = 0

    for case_id, gt_case in gt_by_id.items():
        if case_id not in pred_by_id:
            continue
        p = pred_by_id[case_id]
        gt_label_normalized = LABEL_MAP[gt_case["category"]]
        pred_label_raw = p.get("support_judgment", "")
        correct = pred_label_raw == gt_label_normalized
        confusion[gt_case["category"]][pred_label_raw] += 1
        rows.append(
            {
                "id": case_id,
                "gt_category": gt_case["category"],
                "predicted": pred_label_raw,
                "correct": correct,
            }
        )
        gt_relevant = gt_case["relevant"]
        pred_relevant = p.get("relevant")
        if pred_relevant is not None:
            relevance_total += 1
            if pred_relevant == gt_relevant:
                relevance_correct += 1

    n = len(rows)
    n_correct = sum(r["correct"] for r in rows)
    accuracy = n_correct / n if n else 0.0

    per_category = {}
    for cat in CATEGORIES:
        gt_label_normalized = LABEL_MAP[cat]
        tp = sum(
            1
            for r in rows
            if r["gt_category"] == cat and r["predicted"] == gt_label_normalized
        )
        fn = sum(
            1
            for r in rows
            if r["gt_category"] == cat and r["predicted"] != gt_label_normalized
        )
        fp = sum(
            1
            for r in rows
            if r["gt_category"] != cat and r["predicted"] == gt_label_normalized
        )
        precision = tp / (tp + fp) if (tp + fp) else 0.0
        recall = tp / (tp + fn) if (tp + fn) else 0.0
        f1 = (
            2 * precision * recall / (precision + recall)
            if (precision + recall)
            else 0.0
        )
        per_category[cat] = {
            "precision": round(precision, 3),
            "recall": round(recall, 3),
            "f1": round(f1, 3),
            "support": tp + fn,
        }

    macro_f1 = sum(v["f1"] for v in per_category.values()) / len(per_category)

    return {
        "n_cases_scored": n,
        "missing_from_predictions": sorted(missing),
        "unexpected_extra_ids": sorted(extra),
        "overall_accuracy": round(accuracy, 3),
        "per_category": per_category,
        "macro_f1": round(macro_f1, 3),
        "relevance_accuracy": round(relevance_correct / relevance_total, 3)
        if relevance_total
        else None,
        "confusion_matrix": {k: dict(v) for k, v in confusion.items()},
        "rows": rows,
    }


def score_retrieval(gt, pred):
    gt_by_id = {c["id"]: c for c in gt["retrieval_failure_cases"]}
    pred_by_id = {c["id"]: c for c in pred["retrieval_predictions"]}

    rows = []
    for case_id, gt_case in gt_by_id.items():
        if case_id not in pred_by_id:
            continue
        p = pred_by_id[case_id]
        predicted_status = p.get("retrieval_status")
        # Expected status is not fixed for R1/R2 (real, live, time-varying);
        # record what was observed, and whether the prediction correctly
        # distinguishes success from failure, which is the behavior that matters.
        expected_class = (
            "failure" if gt_case["failure_mode"] != "success" else "success"
        )
        predicted_class = "success" if predicted_status == "success" else "failure"
        rows.append(
            {
                "id": case_id,
                "provenance": gt_case["provenance"],
                "failure_mode_at_authoring_time": gt_case["failure_mode"],
                "predicted_status": predicted_status,
                "predicted_class": predicted_class,
                "evidence": p.get("evidence", ""),
                "matches_failure_vs_success_expectation": (
                    predicted_class == "failure"
                    if gt_case["provenance"] != "real"
                    or gt_case["failure_mode"] != "transient_block"
                    else None  # R2's status may have changed since authoring; not scored as pass/fail
                ),
            }
        )
    return {"rows": rows}


def main():
    gt, pred = load()
    semantic_scores = score_semantic(gt, pred)
    retrieval_scores = score_retrieval(gt, pred)
    out = {"semantic": semantic_scores, "retrieval": retrieval_scores}
    OUT_PATH.write_text(json.dumps(out, indent=2))
    print(f"wrote {OUT_PATH}")
    print(f"overall accuracy: {semantic_scores['overall_accuracy']}")
    print(f"macro F1: {semantic_scores['macro_f1']}")
    print(f"per-category: {json.dumps(semantic_scores['per_category'], indent=2)}")


if __name__ == "__main__":
    main()
