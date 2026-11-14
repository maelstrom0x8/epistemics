# Why Language Models Hallucinate

**Authors:** Adam Tauman Kalai (OpenAI), Ofir Nachum (OpenAI), Santosh S. Vempala (Georgia Tech), Edwin Zhang (OpenAI)
**Source:** arXiv preprint, 2025
**URL:** https://arxiv.org/abs/2509.04664
**Accessed:** 2026-11-14
**Type:** primary source

## Summary

The paper argues that language model hallucination is not a mysterious emergent failure but an instance of ordinary statistical error. The authors formalize next-token generation of valid versus invalid statements as a binary classification problem ("Is-It-Valid") and show that a model's generative error rate is bounded below by roughly twice its classification error rate on that problem, so anything that causes classification errors (arbitrary unlearnable facts, model-family limitations, computational hardness, distribution shift, noisy training data) also forces hallucinations. They further argue that post-training fails to eliminate hallucinations because most mainstream benchmarks use binary right/wrong grading that gives zero credit for abstaining, which mathematically makes confident guessing the optimal strategy over admitting uncertainty. Their proposed remedy is not a new hallucination-specific test but a change to grading on existing mainstream benchmarks: explicit confidence thresholds with penalties for wrong answers, so that abstention ("I don't know") becomes the rational choice below a stated confidence level.

## Key Claims / Findings

- **Core theoretical argument:** Valid-text generation is at least as hard as the binary classification problem of deciding whether a candidate statement is valid or invalid (termed "Is-It-Valid," IIV). The paper derives that generative error rate ≳ 2 × IIV misclassification rate, linking hallucination directly to known sources of classification error.
- **Sources of hallucination identified:**
  - *Arbitrary/unlearnable facts* — for facts with no learnable pattern (e.g., a specific person's birthday), the model must err on at least the "singleton rate": the fraction of such facts appearing only once in training data. This extends earlier work by Kalai and Vempala.
  - *Model-family limitations* — some architectures or non-reasoning models cannot represent certain concepts (the paper cites letter-counting failures as an example).
  - *Other contributing factors* — computational hardness, distribution shift, and "garbage in, garbage out" from erroneous training data.
- Cross-entropy pretraining tends to produce base models that are roughly calibrated, which the authors treat as part of the explanation for why statistical errors (and hence hallucinations) appear at all.
- Hallucination is not claimed to be inevitable in every case: a model could in principle answer only what it knows and otherwise say "I don't know."
- **Evaluation/incentive argument:** The authors prove that under standard binary (correct/incorrect) grading, abstaining is never the optimal strategy regardless of the model's actual confidence — directly analogous to a student guessing on a multiple-choice exam with no penalty for wrong answers.
- Their review (Table 2 in the paper) found that most major benchmarks they examined — including GPQA, MMLU-Pro, SWE-bench, and HLE — use binary grading with no credit for "I don't know" responses.
- Consequently, they argue that adding more dedicated hallucination-detection benchmarks will not fix the problem; the mainstream leaderboards that drive model development still reward confident bluffing.
- **Proposed fix — explicit confidence targets in grading:** evaluation prompts state a threshold *t*; a wrong answer costs *t*/(1−*t*) points, a correct answer earns 1 point, and "I don't know" earns 0. Answering only becomes rational when the model's confidence exceeds *t* (example thresholds: 0.5, 0.75, 0.9).
- Stating the threshold explicitly keeps grading objective even though the specific threshold chosen is somewhat arbitrary.
- The authors recommend modifying existing mainstream benchmarks (e.g., SWE-bench) to include confidence targets, rather than relying solely on bespoke hallucination-specific tests.
- Behavioral calibration — a model answering only above the stated threshold and abstaining otherwise — can be audited by comparing accuracy and error rates across different thresholds.
- **Definitions used:** a hallucination is characterized as a "plausible yet incorrect statement" produced instead of an admission of uncertainty. The paper distinguishes *intrinsic* hallucinations (contradicting the prompt) from *extrinsic* hallucinations (contradicting training data or external reality), and notes an alternative definition — output not grounded in training data or prompt — to which they say their lower bound also applies.
- **Stated limitations (acknowledged by the authors):** the framework ignores degrees of error and nonsensical outputs, does not account for hidden context, and search/retrieval augmentation does not fully resolve the problem under binary grading. The authors describe their evaluation proposal as requiring "socio-technical" change (i.e., leaderboard and benchmark-maintainer adoption), not just a technical fix.

## Relevance to the sprint

This paper is directly relevant to Track 1 (Model Epistemics & Decision-Making Evals): it provides a formal account of why models express unwarranted confidence rather than calibrated uncertainty, and ties the problem to specific, auditable properties of existing evaluation design (binary grading with no abstention credit) rather than to an inherent model limitation alone. Its proposed confidence-threshold grading scheme is a concrete, testable intervention that sprint participants could adapt or critique when designing calibration-sensitive evals.

## Access notes / limitations

Full text was accessible and read in two forms: the arXiv abstract page (https://arxiv.org/abs/2509.04664) and the experimental HTML full text (https://arxiv.org/html/2509.04664v1), which was fetched up to character offset 100,000 of approximately 145,577 (roughly the first 69% of the HTML document; the remainder, likely containing proofs, additional experiments, and references, was not reviewed). A PDF version was also listed as available but not separately fetched. Only one arXiv version (v1, submitted 4 September 2025) exists as of access date. The sprint page's attribution ("Kalai et al., OpenAI, 2025") is substantially but not entirely accurate: three of the four listed authors (Kalai, Nachum, Zhang) are affiliated with OpenAI per the paper's own text, but the fourth author, Santosh S. Vempala, is affiliated with Georgia Tech, so the paper is not solely an OpenAI-authored work.
