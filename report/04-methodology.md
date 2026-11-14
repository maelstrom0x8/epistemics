# 4. Methodology

## 4.1 Overview

The study models a two-agent handoff. An upstream "researcher" agent produces a fixed proposition and attaches a source. A receiving "analyst" agent evaluates whether the proposition is supported and reports a judgment. What varies across the four experimental conditions is only what the receiving agent is told about the source's verification status. The underlying claim and source material are held identical across all four conditions for a given case.

The researcher's messages are authored and fixed in advance, not generated dynamically by another model call. This isolates the effect of how evidence is presented from any variability in how an upstream agent might phrase a claim.

## 4.2 Experimental conditions

| Condition | What the receiving agent is given |
| --- | --- |
| A. Independent baseline | The source material and the proposition to evaluate. No upstream conclusion is attached. |
| B. Unverified handoff | The same proposition, presented as an upstream agent's conclusion, plus the same source material. No verification information. |
| C. Binary verification | Everything in B, plus a single verdict field: `supported` or `not_supported`. |
| D. Evidence-bound receipt | Everything in B, plus a structured receipt: per-component claim assessment, the exact supporting or contradicting passage, and an explicit list of what was not checked. |

Condition A exists to measure the receiving agent's own baseline competence at the underlying task, independent of any social influence from an upstream agent. Without it, a difference between B and D could be read as "verification helps" when it might really be "the receiving agent is bad at this regardless of what it's told," and the two are not the same finding.

The primary comparison is B against D: does an evidence-bound receipt reduce unsupported-conclusion adoption relative to a bare handoff with no verification information at all. B against C tests whether a verdict alone, with no supporting detail, is enough. A against D gives the overall value of the full intervention relative to no social pressure and no verification at all.

## 4.3 Benchmark construction

A frozen corpus of claim-and-source cases is constructed and labeled before any receiving-agent trial is run. Each case is independently labeled along one dimension, the relationship between the source and the proposition attached to it:

| Label | Meaning |
| --- | --- |
| Fully supported | The source establishes the proposition as stated. |
| Partially supported | Some component of the proposition is supported; another component is missing, overstated, or unaddressed. |
| Contradicted | The source provides evidence against the proposition. |
| Unsupported | The source does not establish the proposition, and does not contradict it either; it is simply insufficient or off-topic. |
| Retrieval failure | The cited material cannot be reliably retrieved or read at all. This is a technical status, not a semantic judgment, and is tracked separately from the other four. |

The initial target is 30 cases, 6 per category, authored and labeled by hand rather than generated and self-labeled by a model. This count is a deliberate scope decision given a single-session, single-researcher pilot, not a claim that 30 cases is enough to generalize from; Chapter 3 already states that this study is not claiming to be adequately powered. AVeriTeC's annotation approach (Section 2.1) is used as a reference for how to write a defensible rubric, but its verdicts are not imported directly, because its labels apply to a whole claim checked against multi-source web evidence, not to a single source-claim pair.

Cherry-picking (a real study showing an effect in a subgroup, cited to support a claim about everyone) is treated as a sub-case of "partially supported" or "unsupported" where it naturally arises, not pursued as its own category requiring multi-source synthesis, which Chapter 3 places out of scope.

## 4.4 Citation Binder: deliberately limited scope

The study's own citation-verification component, used to produce the automated version of the Condition D receipt, is restricted to:

- Decomposing a compound proposition into its atomic components.
- Matching each component against the frozen source text for that case.
- Reporting, per component, a status (supported, contradicted, or insufficient) and the exact passage used to justify it.

It does not sign anything, hash anything for authentication purposes, or query a trust registry. A content hash of the frozen source snapshot may be recorded for reproducibility (so a reader can confirm which exact version of a source text was used), but this is a record-keeping detail, not a claim about the source's authenticity, and is never presented to the receiving agent as a judgment about whether the content is trustworthy.

## 4.5 Separating the verifier from the behavioral question

Two different questions are easy to accidentally collapse into one experiment, and this design keeps them apart deliberately:

1. Is the Citation Binder itself accurate? This is evaluated by comparing its automated output against the hand-authored ground-truth labels from Section 4.3, reported as precision, recall, and macro-F1 per category, plus retrieval-failure rate, independent of any receiving-agent trial.
2. Does a reliable verification result change receiving-agent behavior? This is evaluated using the hand-authored, oracle-labeled receipts in Conditions C and D, not the automated Citation Binder's own output. If the automated verifier turns out to be unreliable, that is a limitation of the Citation Binder, reported in Chapter 6, and it does not contaminate the answer to the behavioral question, which is tested against ground truth either way.

## 4.6 Receiving-agent model selection

No external model-provider API credentials are available in this environment; this was checked directly before planning this study, not assumed. The receiving-agent role is filled using Claude-family models accessed through this session's own agent-spawning capability, at two different capability tiers, as a stated and limited proxy for broader model diversity. This is not equivalent to a genuine cross-provider comparison, and the results in Chapter 8 will be reported as applying to the specific Claude-family models actually used, identified by name, not generalized to "LLMs" as a class.

Each trial is run as a fresh, independent evaluation with no shared conversation state between cases or conditions, and presentation order is randomized to reduce ordering effects.

## 4.7 Receiving-agent output format

Each trial requires a structured response containing:

1. `support_judgment`: supported, contradicted, or insufficient.
2. `support_confidence`: a number from 0 to 1.
3. `evidence_quote`: the exact passage the receiving agent used to justify its judgment.
4. `receipt_interpretation` (Conditions C and D only): what the receiving agent understood the verification information to establish, used to check whether it is actually reading the receipt correctly rather than ignoring it.

## 4.8 Evaluation metrics

**Primary metric:** unsupported-conclusion adoption rate, the proportion of contradicted or unsupported cases in which the receiving agent's judgment matches the upstream agent's (unsupported) conclusion rather than the ground-truth label.

**Secondary metrics:**

- Supported-claim rejection rate: how often a genuinely supported conclusion is wrongly rejected, the cost side of H4.
- Balanced accuracy across the four semantic categories.
- Calibration: reported confidence compared against actual correctness.
- Receipt comprehension: whether the receiving agent's stated interpretation of the verification information matches what it actually says.
- Response cost: token usage.

## 4.9 Statistical approach

Comparisons are paired at the case level, since the same case appears under multiple conditions. Results are reported as raw counts and proportions, with confidence intervals from case-level bootstrap resampling, and the primary comparison (B against D) is treated as the one comparison this pilot is actually designed to speak to; other comparisons are reported as secondary and exploratory. With roughly 30 cases per condition, this is explicitly a pilot scale: a null or wide-interval result is reported as such, not treated as evidence of absence.

## 4.10 What happens if time runs out

If the full 30-case benchmark cannot be completed, a smaller set with the same per-category balance and the same annotation standard is preferred over a larger set built to a lower standard. This preference is stated here, before any time pressure exists, so it does not look like a post-hoc excuse if invoked later.
