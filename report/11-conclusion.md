# 11. Conclusion

## 11.1 Answering the research question

The frozen research question (Chapter 3) asked: among cases a receiving AI agent can answer correctly on its own, does providing it with a claim-specific, evidence-bound verification receipt reduce how often it instead adopts an upstream agent's specific unsupported conclusion, compared with an unverified handoff or a bare binary verdict? This pilot cannot answer that question. The precondition for asking it, a measurable rate of answer substitution under an unverified handoff, did not appear for either Claude-family model tested, at this benchmark's scale, under this study's specific operationalization of the handoff (Chapter 8). This is reported as an inconclusive result at this pilot's scale, not as a negative finding about evidence-bound receipts and not as a challenge to the prior work (Gong et al., 2026) this study's premise depends on.

## 11.2 What was actually established

Separate from the primary question, three things were established directly by this project's own work, not merely cited from elsewhere:

1. A 30-case benchmark of claim-source pairs, built to a disclosed single-annotator standard, with one labeling defect found and corrected during construction (Chapter 5).
2. A minimal, disclosed-architecture Citation Binder, scoring 92% overall against that benchmark, with a specific, repeatable blind spot around cherry-picked or scope-conflated figures that generalizes to other component-rollup citation verifiers, not just this one (Chapter 6, Section 9.3).
3. A specific, named candidate explanation for why a controlled, researcher-labeled multi-agent handoff experiment may suppress the very phenomenon it is designed to measure: an explicit neutrality instruction, added to avoid biasing a receiving agent toward deference, may have the side effect of removing the deference pressure a real, unlabeled handoff would carry (Chapter 9).

## 11.3 What would need to change for a future iteration to test the original question

A follow-up study, not attempted here given this pilot's scope, would need to vary the handoff's framing (removing or softening the explicit neutrality instruction, and embedding the upstream claim inside a more naturalistic shared task rather than a labeled experimental field) and separately vary case difficulty (including wrong-upstream cases closer to the threshold of plausibility, not only clear contradictions or off-topic claims), while holding everything else in this study's design fixed, to determine which of the three candidate explanations in Section 9.2 is actually responsible for the null result found here.

## 11.4 Final statement

This report does not claim evidence-bound verification receipts work, and does not claim they don't. It establishes a frozen, disclosed, independently-checked protocol; a benchmark and an automated verifier built to that protocol, with their own limitations stated plainly; and an experiment that, run honestly, produced a result this report's own frozen hypotheses (Chapter 3) anticipated as a live possibility and committed in advance to reporting as such. That commitment is kept here.
