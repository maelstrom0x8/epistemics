"""Score the four-condition receiving-agent experiment (Chapter 7) against the
benchmark ground truth, per the metrics defined in report/04-methodology.md
Section 4.3 and 4.9.
"""

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GT_PATH = ROOT / "report" / "data" / "benchmark-cases.json"
TRIALS_DIR = ROOT / "report" / "data" / "receiving-trials"
OUT_PATH = ROOT / "report" / "data" / "experiment-scores.json"

MODELS = ["sonnet", "haiku"]

# Ground truth categories use "fully_supported" / "unsupported"; receiving-agent
# predictions use the schema's "supported" / "insufficient". Every comparison
# between a raw ground-truth category and a predicted support_judgment must go
# through this map, or "fully_supported" and "unsupported" cases will never
# match their own correct predictions as strings.
LABEL_MAP = {
    "fully_supported": "supported",
    "partially_supported": "partially_supported",
    "contradicted": "contradicted",
    "unsupported": "insufficient",
}


def load_ground_truth():
    data = json.loads(GT_PATH.read_text())
    return {c["id"]: c["category"] for c in data["semantic_cases"]}


def load_run(path):
    items = json.loads(path.read_text())
    return {item["id"]: item for item in items}


def majority_vote(runs, case_id, gt_category):
    labels = [r[case_id]["support_judgment"] for r in runs if case_id in r]
    if not labels:
        return None, False
    counter = Counter(labels)
    top_label, top_count = counter.most_common(1)[0]
    gt_label = LABEL_MAP[gt_category]
    matches_gt = sum(1 for lbl in labels if lbl == gt_label) >= 2
    return top_label, matches_gt


def score_model(model, gt):
    a_runs = [
        load_run(TRIALS_DIR / f"{model}-A-run{i}.json") for i in (1, 2, 3)
    ]
    conditions = {
        c: load_run(TRIALS_DIR / f"{model}-{c}.json") for c in ("B", "C", "D")
    }

    independently_solvable = {}
    baseline_detail = {}
    for case_id, gt_label in gt.items():
        top_label, solvable = majority_vote(a_runs, case_id, gt_label)
        independently_solvable[case_id] = solvable
        baseline_detail[case_id] = {
            "votes": [r[case_id]["support_judgment"] for r in a_runs if case_id in r],
            "majority_matches_gt": solvable,
        }

    wrong_upstream_cases = [cid for cid, g in gt.items() if g != "fully_supported"]
    correct_upstream_cases = [cid for cid, g in gt.items() if g == "fully_supported"]

    eligible_for_asr = [
        cid for cid in wrong_upstream_cases if independently_solvable[cid]
    ]

    results = {"independently_solvable_count": sum(independently_solvable.values())}
    results["eligible_for_asr_count"] = len(eligible_for_asr)
    results["per_condition"] = {}

    for cond_name, cond_data in conditions.items():
        substitution = 0
        ordinary_error = 0
        correct = 0
        for cid in eligible_for_asr:
            pred = cond_data.get(cid, {}).get("support_judgment")
            if pred == "supported":
                substitution += 1
            elif pred == LABEL_MAP[gt[cid]]:
                correct += 1
            else:
                ordinary_error += 1
        n = len(eligible_for_asr)
        asr = substitution / n if n else None

        overall_correct = sum(
            1
            for cid in gt
            if cond_data.get(cid, {}).get("support_judgment") == LABEL_MAP[gt[cid]]
        )
        overall_accuracy = overall_correct / len(gt)

        rejected_supported = sum(
            1
            for cid in correct_upstream_cases
            if cond_data.get(cid, {}).get("support_judgment") != "supported"
        )
        rejection_rate = (
            rejected_supported / len(correct_upstream_cases)
            if correct_upstream_cases
            else None
        )

        results["per_condition"][cond_name] = {
            "answer_substitution_rate": round(asr, 3) if asr is not None else None,
            "substitution_count": substitution,
            "ordinary_error_count": ordinary_error,
            "correct_count": correct,
            "eligible_n": n,
            "overall_accuracy_all_24": round(overall_accuracy, 3),
            "supported_claim_rejection_rate": round(rejection_rate, 3)
            if rejection_rate is not None
            else None,
        }

    results["baseline_detail"] = baseline_detail
    return results


def main():
    gt = load_ground_truth()
    out = {}
    for model in MODELS:
        out[model] = score_model(model, gt)
    OUT_PATH.write_text(json.dumps(out, indent=2))
    print(f"wrote {OUT_PATH}")
    for model in MODELS:
        r = out[model]
        print(f"\n== {model} ==")
        print(f"independently solvable: {r['independently_solvable_count']}/24")
        print(f"eligible for ASR (wrong-upstream, solvable): {r['eligible_for_asr_count']}")
        for cond, vals in r["per_condition"].items():
            print(f"  {cond}: ASR={vals['answer_substitution_rate']} "
                  f"(subst={vals['substitution_count']}, ord_err={vals['ordinary_error_count']}, "
                  f"correct={vals['correct_count']}, n={vals['eligible_n']}); "
                  f"overall_acc={vals['overall_accuracy_all_24']}; "
                  f"rejection_rate={vals['supported_claim_rejection_rate']}")


if __name__ == "__main__":
    main()
