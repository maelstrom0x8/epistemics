# 3. Research Question and Hypotheses

This chapter is frozen as of the date below. The benchmark (Chapter 5) and the experiment (Chapter 7) are built to test what is written here, not the other way around. If anything written here turns out to need revision once work is underway, that revision will be recorded explicitly in this chapter, dated, with the original left visible, rather than edited away silently.

**Frozen:** 2026-11-14.

## 3.1 Primary research question

Does providing a receiving AI agent with a claim-specific, evidence-bound verification receipt reduce its adoption of an upstream agent's unsupported conclusions, compared with an unverified handoff or a bare binary verdict?

## 3.2 Secondary questions

1. Does a receiving agent, given no upstream conclusion at all, correctly judge whether a source supports a given claim, on its own? (This establishes a baseline rate of competence, independent of any social influence from another agent.)
2. Does an unverified upstream conclusion, attached to the same source material, change the receiving agent's judgment relative to that baseline, and in which direction?
3. Does a bare binary verdict ("supported" or "not supported") attached to the handoff change the receiving agent's judgment, relative to the unverified handoff?
4. Does a structured, claim-level evidence receipt (naming the specific supporting or contradicting passage) change the receiving agent's judgment more than a bare binary verdict does?
5. Does any observed benefit come at a cost: does the receiving agent start rejecting genuinely supported conclusions more often, or take measurably longer or more tokens to respond, as verification information is added?

## 3.3 Hypotheses

**H1. Baseline susceptibility.** Even with full access to the same source material the upstream agent had, a receiving agent will sometimes adopt an upstream agent's unsupported conclusion rather than independently verifying it against the source. This is not a novel prediction; it restates the finding already established by Gong et al. (2026) and is included here as something this study's own baseline condition should reproduce, not as a claim of discovery.

**H2. Bare verification is insufficient on its own.** A binary support verdict reduces, but does not eliminate, unsupported-conclusion adoption relative to an unverified handoff.

**H3. Evidence-bound receipts outperform bare verdicts.** A structured receipt that names the specific supporting or contradicting passage reduces unsupported-conclusion adoption more than a bare binary verdict does.

**H4. No improvement is free.** Any reduction in unsupported-conclusion adoption achieved under H2 or H3 may be accompanied by costs: increased rejection of conclusions that are actually supported, or increased response length, latency, or token use. These trade-offs are measured, not assumed away, and a result showing H3 holds but at a real cost to accuracy on supported claims is reported as such, not treated as a clean win.

**H0, the null, stays live throughout.** It is entirely possible that none of the four conditions produce a measurable difference in this pilot, for Claude-family models, at this sample size. That outcome is treated as a legitimate and useful result, not as a failed experiment, provided the experimental controls held.

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

For H1 to be considered supported in this study's own data (as opposed to simply cited from prior work): the baseline-handoff condition must show a measurable rate of unsupported-conclusion adoption above what the no-handoff baseline condition shows, for at least one tested model.

For H2: the binary-verdict condition must show a lower rate of unsupported-conclusion adoption than the unverified-handoff condition, with the comparison reported alongside its confidence interval rather than as a bare point estimate.

For H3: the evidence-receipt condition must show a lower rate of unsupported-conclusion adoption than the binary-verdict condition, under the same reporting standard.

For H4: the study reports supported-claim rejection rates and response-cost metrics for every condition regardless of whether H2 or H3 is supported, so that any trade-off is visible even if the headline hypotheses succeed.

Given the sample size planned in Chapter 4, any of these comparisons may show a wide confidence interval or fail to reach significance. That outcome is reported honestly as inconclusive, not rounded up to a positive or negative finding it does not actually support.
