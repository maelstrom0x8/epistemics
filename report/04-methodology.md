# 4. Methodology

## 4.1 Overview

The study models a two-agent handoff. An upstream "researcher" agent produces a fixed proposition and attaches a source. A receiving "analyst" agent evaluates whether the proposition is supported and reports a judgment. Two things vary across the four experimental conditions: whether an upstream conclusion is present at all, and, when it is present, how much claim-specific verification information accompanies it. The underlying claim and source material are held identical across all four conditions for a given case.

The researcher's messages are authored and fixed in advance, not generated dynamically by another model call. This isolates the effect of how evidence is presented from any variability in how an upstream agent might phrase a claim.

## 4.2 Experimental conditions

| Condition | Upstream conclusion present? | Verification information given |
| --- | --- | --- |
| A. Independent baseline | No | None (no upstream message at all) |
| B. Unverified handoff | Yes | None |
| C. Binary verification | Yes | A single verdict field: `supported` or `not_supported` |
| D. Evidence-bound receipt | Yes | A structured receipt: per-component claim assessment, the exact supporting or contradicting passage, and an explicit list of what was not checked |

Four pairwise comparisons do four different jobs:

| Comparison | What it isolates |
| --- | --- |
| A vs. B | The effect of introducing an unverified upstream conclusion at all |
| B vs. C | The effect of adding a bare binary verdict to an existing handoff |
| C vs. D | The additional effect of claim-level evidence detail, beyond a bare verdict |
| B vs. D | The overall effect of the evidence-bound receipt relative to an unverified handoff (the primary comparison) |

A vs. D is not treated as a clean estimate of the receipt's isolated effect, since it differs from A in two ways at once (presence of a conclusion, and the verification detail behind it). It is reported only as a bound on the complete intervention's overall effect relative to no social pressure and no verification at all.

## 4.3 Independently solvable cases and the answer-substitution metric

The research question in Chapter 3 is restricted to cases a receiving agent can get right on its own. Measuring the headline metric without that restriction would conflate two different things: a receiving agent that is simply wrong regardless of what it is told, and a receiving agent that was misled by an upstream message away from an answer it would otherwise have reached. Only the second is answer substitution, following the operational definition in Gong et al. (2026).

**Screening procedure.** For every case and every receiving model, Condition A (source and proposition only, no upstream message) is run three independent times. A case is classified as independently solvable for that model if at least two of the three runs reach the correct classification. Cases that fail this screen are excluded from the primary answer-substitution metric for that model; they still contribute to the baseline-accuracy and calibration statistics in Section 4.9, since those describe the model's underlying competence rather than the substitution effect specifically.

**Primary metric.** For a given condition c, restricted to cases independently solvable for the model under test and cases where the upstream conclusion in that case is deliberately wrong:

ASR_c = (independently solvable cases where the receiving agent's answer switches to match the peer's specific wrong conclusion) / (independently solvable cases with a wrong peer conclusion)

The primary comparison is ASR_B − ASR_D: whether the evidence-bound receipt reduces the rate of switching to the peer's wrong conclusion, relative to an unverified handoff carrying the same wrong conclusion. A case where the receiving agent reaches some other wrong answer, not the specific one the upstream agent supplied, counts as an ordinary error, not as answer substitution, and is tracked separately (Section 4.8).

Partially-supported cases require a decision about what counts as "wrong": the upstream conclusion is treated as wrong, for the purposes of this metric, whenever it asserts full support for a proposition the benchmark labels as only partially supported. This is stated here, before data collection, so it is not adjusted after seeing results.

## 4.4 Benchmark construction

A frozen corpus of claim-and-source cases is constructed and labeled before any receiving-agent trial is run. The corpus has two parts, kept separate because they test different things.

**Semantic cases (used in the receiving-agent experiment).** 24 cases, 6 per category:

| Label | Meaning |
| --- | --- |
| Fully supported | The source establishes the proposition as stated. |
| Partially supported | Some component of the proposition is supported; another component is missing, overstated, or unaddressed. |
| Contradicted | The source provides evidence against the proposition. |
| Unsupported | The source is available and readable but does not establish the proposition, and does not contradict it either; it is insufficient, or relevant but incomplete, or off-topic. |

Each case also records, separately from the support label, whether the source is topically relevant to the proposition at all. An off-topic source and a relevant-but-incomplete source can both receive an "unsupported" verdict, but for different reasons, and the case record preserves which reason applies rather than collapsing the two.

**Retrieval-failure cases (evaluated against the Citation Binder only).** A separate set of 6 cases where the cited material cannot be reliably retrieved or read. These are excluded from the receiving-agent experiment: Conditions A and B both require giving the receiving agent the source material, and there is no comparable material to give when retrieval has failed. Retrieval failure is a property of the citation-verification pipeline, evaluated in Section 4.5, not a semantic-support category a receiving agent is asked to judge.

This brings the total corpus to 30 cases, the same overall scale as originally planned, correctly partitioned so the behavioral experiment only ever sees cases where source material actually exists to compare conditions against.

**Annotation.** Cases are authored and labeled by one person (the author of this study), which is a single-annotator benchmark, not an independently cross-validated one. Two independent annotators and an inter-annotator agreement statistic such as Cohen's kappa would be preferable and are not used here, because no second annotator is available within this project's scope. As a partial mitigation, each case is labeled twice by the same annotator, in two separate sessions against the same written rubric, and a case is only finalized when both passes agree; a disagreement is resolved by rewriting the case until it is unambiguous under the rubric rather than by picking one label and discarding the mismatch. This catches careless labeling errors; it does not catch a rubric interpretation the sole annotator applies consistently but wrongly. That remains a disclosed limitation of this benchmark, not something the two-pass procedure is claimed to fully resolve.

AVeriTeC's annotation care (Section 2.1) is used as a reference for how to write a defensible rubric. Its verdicts are not imported directly as ground truth, because AVeriTeC labels a whole claim against multi-source web evidence, while this benchmark labels a single source against a single proposition.

Cherry-picking (a real finding, true in a subgroup, cited to support a claim about everyone) is treated as a sub-case of "partially supported" or "unsupported" where it arises naturally in a case, not pursued as its own category requiring multi-source synthesis, which Chapter 3 places out of scope.

## 4.5 Citation Binder: deliberately limited scope

The study's own citation-verification component, used to produce the automated version of the Condition D receipt (and evaluated separately from the oracle-labeled receipts used in the main behavioral experiment; see Section 4.6), is restricted to three operations, each performed by a separately prompted model call rather than a dedicated retrieval or natural-language-inference model:

1. Decomposing a compound proposition into its atomic components.
2. Matching each component against the frozen source text for that case and retrieving the relevant passage.
3. Reporting, per component, a status (supported, contradicted, or insufficient) and the exact passage used to justify it.

Using a prompted model for all three steps, rather than a purpose-built NLI model or a separate retrieval index, is a scope decision disclosed here rather than a hidden implementation detail. It means a failure in decomposition (splitting a compound proposition incorrectly) can propagate into the matching and support-judgment steps; Section 4.6 evaluates decomposition quality separately for this reason, not only the end-to-end support judgment.

The Citation Binder does not sign anything, hash anything for authentication purposes, or query a trust registry. A content hash of the frozen source snapshot may be recorded for reproducibility, so a reader can confirm which exact version of a source text was used, but this is a record-keeping detail, not a claim about the source's authenticity, and is never presented to the receiving agent as a judgment about trustworthiness.

## 4.6 Separating the verifier from the behavioral question

Two different questions are easy to accidentally collapse into one experiment, and this design keeps them apart deliberately:

1. **Is the Citation Binder itself accurate?** Evaluated by comparing its automated output against the hand-authored ground-truth labels from Section 4.4, reported as precision, recall, and macro-F1 per semantic category, plus separately as decomposition accuracy (did it split the proposition into the intended components) and retrieval-failure detection rate on the held-out retrieval-failure set.
2. **Does a reliable verification result change receiving-agent behavior?** Evaluated using hand-authored, oracle-labeled receipts in Conditions C and D, not the automated Citation Binder's own output. If the automated verifier turns out to be unreliable, that is a limitation of the Citation Binder, reported in Chapter 6, and does not contaminate the answer to the behavioral question, which is tested against ground truth either way.

A result from this study can therefore say "a correct, claim-level evidence receipt changes receiving-agent behavior in such-and-such way" without that claim depending on whether this study's own automated Citation Binder is good enough to produce such receipts reliably in practice. Whether it is good enough is a separate, secondary finding.

## 4.7 Receiving-agent model selection and reproducibility

No external model-provider API credentials are available in this environment; this was checked directly before planning this study; and the receiving-agent role is filled using two Claude-family models accessed through this session's own agent-spawning capability, selected via that capability's `sonnet` and `haiku` model aliases. These aliases resolve to whichever specific Claude Sonnet and Claude Haiku models and versions are current at the time each trial actually runs; neither a fixed, versioned model snapshot identifier nor direct control over temperature, sampling, or maximum output tokens is exposed through this interface. Chapter 7 records, for the actual experiment run, the exact date and session in which each trial was executed, as the best available substitute for a pinned snapshot identifier, and discloses the absence of sampling-parameter control as a reproducibility limitation rather than presenting an assumed determinism that cannot actually be configured here.

This is a within-provider, two-tier comparison, not a cross-provider one, and results in Chapter 8 are reported as applying to these two specific models, not generalized to "LLMs" as a class.

Each trial, across all conditions and all repeated baseline runs, is a fresh, independent evaluation with no shared conversation state between cases, conditions, or repeats, and case presentation order is randomized per model to reduce ordering effects.

## 4.8 Receiving-agent output format

Each trial requires a structured response:

```
{
  "support_judgment": "supported | partially_supported | contradicted | insufficient",
  "support_confidence": 0.0,
  "component_assessments": [
    {"proposition": "...", "status": "supported | contradicted | insufficient"}
  ],
  "evidence_quote": "...",
  "receipt_interpretation": ""
}
```

`support_judgment` uses the same four semantic labels as the benchmark in Section 4.4 (collapsing "fully supported" to "supported" for this field), so ground truth, automated-verifier output, and receiving-agent output all share one category scheme; nothing here introduces a fourth, unaligned classification. `component_assessments` is populated whenever the proposition has more than one checkable part, which is how "partially supported" judgments are distinguished from "supported" or "insufficient" ones rather than collapsed into a single binary field. `receipt_interpretation` is required only in Conditions C and D, and records what the receiving agent understood the verification information to establish, which is compared against what the receipt actually says (Section 4.9) to check whether the receiving agent is reading it rather than ignoring it.

**Rollup rule, stated explicitly.** A case-level `support_judgment` is derived from its component-level classifications as follows: `supported` if every component is supported; `contradicted` if any component is contradicted; `partially_supported` if the components are a mix of supported and insufficient with no contradicted component; `insufficient` if every component is insufficient. One exception is carved out deliberately: a proposition that correctly states a figure drawn from a narrower subset of a source's data, but presents it as if it described the source's full dataset (for example, citing a frontier-model subset's accuracy range as if it were the full study population's range), is classified as `partially_supported`, not `contradicted`, even though the specific number technically conflicts with the full-population figure. This is the cherry-picking sub-case already described in Section 4.4; without this carve-out, a generic rollup rule would fold every scope-conflation case into "contradicted," which would make it indistinguishable from a case where the source flatly states the opposite of the proposition. This exception must be applied by whoever or whatever assigns the label; the automated Citation Binder (Chapter 6) was not given this exception explicitly, and Chapter 6 reports what happens when it is not.

## 4.9 Evaluation metrics

**Primary metric:** the answer-substitution rate defined in Section 4.3, computed per condition and per model, restricted to independently solvable cases with a wrong upstream conclusion.

**Secondary metrics:**

- Ordinary error rate on the same case set: wrong answers that do not match the specific upstream conclusion, tracked separately from substitution so the two are never summed into one undifferentiated "wrong" count.
- Supported-claim rejection rate: how often a genuinely supported conclusion is wrongly rejected, the cost side tracked in Chapter 3.
- Baseline accuracy and balanced accuracy across the four semantic categories, computed on all cases (not restricted to the independently-solvable subset), to describe underlying task competence.
- Calibration: elicited confidence compared against actual correctness, reported as a multiclass calibration measure rather than assumed to be meaningful without checking.
- Receipt comprehension: agreement between the receiving agent's stated interpretation of the verification information and what the receipt actually says.
- Response cost: token usage and latency per trial.

## 4.10 Statistical approach

Comparisons are paired at the case level, since the same case appears under multiple conditions, with repeated baseline runs (Section 4.3) accounted for as clustered observations within a case rather than treated as independent data points. Results are reported as raw counts, proportions, and the actual eligible denominator for every comparison (which will typically be smaller than the full 24-case semantic set once the independently-solvable restriction is applied), with confidence intervals from case-level bootstrap resampling.

The primary comparison, ASR_B against ASR_D, is the one this pilot is designed to speak to; the other three pairwise comparisons in Section 4.2 are secondary and exploratory. At this scale, roughly two dozen semantic cases before any independently-solvable screening narrows the eligible set further, this is a pilot, not an adequately powered study, and a null or wide-interval result is reported as such rather than interpreted as evidence that evidence receipts have no effect.

If the full benchmark described in Section 4.4 cannot be completed in the time available, a smaller set built to the same per-category balance and the same two-pass annotation standard is preferred over a larger set built to a lower standard, a preference stated here rather than invoked after the fact as an excuse.
