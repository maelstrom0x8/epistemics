# 3. Research Question and Hypotheses

This chapter is frozen as of the date below. The benchmark (Chapter 5) and the experiment (Chapter 7) are built to test what is written here, not the other way around. If anything written here turns out to need revision once work is underway, that revision will be recorded explicitly in this chapter, dated, with the original left visible, rather than edited away silently.

**Frozen:** 2026-11-14. **Revised:** 2026-11-14 (same day, before any benchmark case or experimental trial existed; see the revision note at the end of this section).

## 3.1 Primary research question

Among cases a receiving AI agent can answer correctly on its own, without any upstream message, does providing it with a claim-specific, evidence-bound verification receipt reduce how often it instead adopts an upstream agent's specific unsupported conclusion, compared with an unverified handoff or a bare binary verdict?

**Revision note.** The question as originally written ("Does providing a receiving AI agent with a claim-specific, evidence-bound verification receipt reduce its adoption of an upstream agent's unsupported conclusions...") did not restrict to cases the receiving agent could independently get right. Gong et al. (2026), the paper this study's phenomenon is named after, define answer substitution specifically as a transition away from an independently correct answer toward the upstream agent's specific wrong answer, and screen for "independently solvable" cases using repeated baseline runs before measuring it. Without that restriction, a receiving agent that is simply wrong on its own, in every condition, for reasons unrelated to the upstream message, would be indistinguishable from one that was misled by the message. The revised wording and the methodology in Chapter 4 adopt Gong et al.'s restriction so the primary metric actually measures the phenomenon the title names, not ordinary model error.

## 3.2 Secondary questions

1. Does a receiving agent, given no upstream conclusion at all, correctly judge whether a source supports a given claim, on its own? (This establishes a baseline rate of competence, independent of any social influence from another agent.)
2. Does an unverified upstream conclusion, attached to the same source material, change the receiving agent's judgment relative to that baseline, and in which direction?
3. Does a bare binary verdict ("supported" or "not supported") attached to the handoff change the receiving agent's judgment, relative to the unverified handoff?
4. Does a structured, claim-level evidence receipt (naming the specific supporting or contradicting passage) change the receiving agent's judgment more than a bare binary verdict does?
5. Does any observed benefit come at a cost: does the receiving agent start rejecting genuinely supported conclusions more often, or take measurably longer or more tokens to respond, as verification information is added?

## 3.3 Hypotheses

**H1. Baseline susceptibility (manipulation check).** Among cases a receiving agent answers correctly when given only the source material and no upstream message, replacing that silence with an unverified upstream conclusion that is wrong increases the rate at which the receiving agent's answer changes to match it. This restates, as something this study's own data must reproduce rather than merely cite, the finding already established by Gong et al. (2026). If this check fails, that is evidence the experimental setup is not eliciting the phenomenon under study, and the remaining hypotheses should be read with that in mind.

**H2. A binary verdict helps.** Among the same independently-solvable, wrong-upstream-conclusion cases, providing a binary support verdict (Condition C) reduces the rate of adoption relative to the unverified handoff (Condition B).

**H3. An evidence-bound receipt helps more than a binary verdict.** The proposed mechanism: a binary verdict gives the receiving agent another conclusion to weigh against the upstream one, but nothing to check it against. A receipt that names the specific supporting or contradicting passage (Condition D) gives the receiving agent something it can inspect directly, independent of whether it trusts the verdict itself. If that mechanism holds, Condition D should show a lower adoption rate than Condition C on the same case set.

**Verification costs and trade-offs.** This is tracked as a measurement, not stated as a hypothesis to confirm or deny. Any reduction in adoption achieved under H2 or H3 may come with a cost: more frequent wrongful rejection of a conclusion that actually is supported, or increased response length, latency, or token use. These are measured for every condition and reported regardless of whether H2 or H3 holds, so a result where Condition D reduces adoption but also increases wrongful rejection is reported as a trade-off, not presented as an unqualified improvement.

**Null and inconclusive results.** It is possible that none of the four conditions produce a measurable difference in this pilot, for the Claude-family models actually tested, at this sample size. Such a result is reported as inconclusive at this scale, not interpreted as proof that evidence receipts have no effect, and not suppressed or reframed to look more decisive than the data support.

## 3.4 Scope boundaries

**In scope:**

- A frozen, manually constructed and annotated benchmark of claim-and-source cases (not live web retrieval), so every experimental condition sees identical underlying material.
- A minimal citation-verification component limited to atomic claim decomposition and evidence-passage matching against the frozen corpus.
- A controlled, four-condition comparison (defined in Chapter 4) using Claude-family models as the receiving agent, at different capability tiers.
- Descriptive and exploratory statistics appropriate to a small pilot: raw counts, proportions, paired per-case comparisons, and confidence intervals. This study does not claim to be adequately powered to establish a universal effect.

**Out of scope, and why:**

- Cross-provider model comparison. No external model API credentials are available in this environment. This is disclosed as a limitation, not minimized.
- Live web retrieval. A frozen corpus is used instead, to keep what each condition sees identical and to avoid link rot or retrieval variance confounding the comparison.
- Cryptographic signing, trust registries, or any provenance-authentication layer. These establish origin and integrity, not evidential support, which is the actual object of study (Section 2.2). Building them would add engineering effort without answering the research question.
- Real user studies or live deployment. The receiving agent in this study is an LLM, not a human reviewer; this study does not claim its findings generalize to human decision-makers.
- Establishing whether a claim is actually, factually true. The study evaluates whether a cited source supports a proposition, which is a narrower and more tractable question than establishing ground truth about the world.
- Cherry-picking detection that requires synthesizing multiple independent sources. The benchmark (Chapter 5) will note where a case could raise this concern, but will not attempt to adjudicate it unless sufficient corroborating material is available for that specific case.

## 3.5 What would count as sufficient evidence

All of the following are restricted to cases classified as independently solvable for the model and condition in question, as defined in Chapter 4.

For H1 to be considered supported in this study's own data (as opposed to simply cited from prior work): the unverified-handoff condition must show a measurable adoption rate above the no-message baseline's error rate on the same cases, for at least one tested model.

For H2: the binary-verdict condition must show a lower adoption rate than the unverified-handoff condition, with the comparison reported alongside its confidence interval rather than as a bare point estimate.

For H3: the evidence-receipt condition must show a lower adoption rate than the binary-verdict condition, under the same reporting standard.

For the cost side: the study reports supported-claim rejection rates and response-cost metrics for every condition regardless of whether H2 or H3 is supported, so that any trade-off is visible even if the headline hypotheses succeed.

Given the sample size planned in Chapter 4, any of these comparisons may show a wide confidence interval or fail to reach significance. That outcome is reported honestly as inconclusive, not rounded up to a positive or negative finding it does not actually support.
