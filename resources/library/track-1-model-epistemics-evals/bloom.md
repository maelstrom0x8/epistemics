# Introducing Bloom: Automated Behavioral Evals

**Authors:** Isha Gupta, Kai Fronsdal, Abhay Sheshadri, Jonathan Michala, Jacqueline Tay, Rowan Wang, Samuel R. Bowman, Sara Price (Anthropic, Alignment team)
**Source:** Anthropic (anthropic.com/research), 2025
**URL:** https://www.anthropic.com/research/bloom
**Accessed:** 2026-11-14
**Type:** institutional

## Summary

Bloom is an open-source agentic framework from Anthropic's Alignment team for generating behavioral evaluations of frontier AI models. Given a description of a target behavior and example transcripts, it automatically generates many scenarios designed to elicit that behavior, runs those scenarios as simulated interactions, and uses a judge model to score how often and how severely the behavior occurs. The stated motivation is that hand-written evals go stale and can leak into training data, so Anthropic built a pipeline to generate and score them automatically at scale.

## Key Claims / Findings

- Anthropic describes Bloom as "an open source agentic framework for generating behavioral evaluations of frontier AI models" that, given a behavior, "quantifies its frequency and severity across automatically generated scenarios."
- Bloom is positioned relative to Petri, another Anthropic auditing tool: Petri explores a model across many diverse, user-specified scenarios and scores it on many dimensions; Bloom instead fixes a single target behavior and generates many scenarios to measure that behavior's rate and severity.
- The pipeline runs four automated stages:
  - **Understanding** – analyzes the behavior description and any example transcripts provided.
  - **Ideation** – generates scenarios, each specifying a situation, a simulated user, a system prompt, and an environment.
  - **Rollout** – runs the generated scenarios in parallel, simulating both the user and tool responses.
  - **Judgment** – a judge model scores each resulting transcript, and a separate meta-judge produces a suite-level analysis across all transcripts.
- Each run generates a different set of scenarios, but a seed configuration file allows a run to be reproduced. Researchers can configure which model is used at each stage, interaction length and modality, scenario diversity, and secondary scoring criteria such as realism.
- Bloom integrates with Weights & Biases for logging and exports transcripts in a format compatible with Inspect (UK AISI's evaluation framework).
- Validation reported on the page:
  - Across ten behavioral "quirks," Bloom's suites distinguished system-prompted model organisms from baseline Claude models in nine of ten cases; the tenth, a self-promotion quirk, showed baseline rates similar to the prompted organism on manual review.
  - On a set of 40 hand-labeled transcripts scored by 11 different judge models, Claude Opus 4.1 had the highest Spearman correlation with human judgments (0.86), followed by Claude Sonnet 4.5 (0.75).
- A case study on self-preferential bias reported that Bloom reproduced the model ranking published in the Claude Sonnet 4.5 system card, and additionally found that increasing reasoning effort reduced self-preferential bias in Claude Sonnet 4, largely because the model increasingly declined to judge its own output at higher effort levels. Filtering out unrealistic or evaluation-aware rollouts improved elicitation quality, and model rankings remained stable across different configurations tested.
- Benchmark results on the page cover four behaviors (delusional sycophancy, instructed long-horizon sabotage, self-preservation, and self-preferential bias) evaluated across what the text describes as 16 frontier models, with 100 rollouts per suite. Note: the accompanying chart on the page appears to label 17 models, a discrepancy between the chart and the body text that this summary flags rather than resolves.
- Linked resources: code at github.com/safety-research/bloom, a technical report at alignment.anthropic.com/2025/bloom-auto-evals/, and example pipeline outputs via a linked Claude.ai public artifact. The page does not itself enumerate limitations in detail and instead points readers to the technical report for those and for additional configuration options.

## Relevance to the sprint

Bloom is directly relevant to Track 1 (Model Epistemics & Decision-Making Evals): it is a concrete, operational framework for automatically generating and scoring behavioral evaluations of models, including judge-model calibration against human ratings and discrimination testing against known model organisms. It is a useful reference both as a method (automated scenario generation plus LLM-judge scoring) and as a cautionary example of the judge-calibration and scenario-realism problems that any model-epistemics eval built on LLM judges will need to address.

## Access notes / limitations

Full page text was retrieved via a web-fetch tool (HTML converted to text/markdown by an intermediate model), not read directly from raw HTML by this agent. The fetched content included the page's title, byline, body text, and descriptions of linked resources, but did not include the full content of the linked technical report (alignment.anthropic.com/2025/bloom-auto-evals/) or the GitHub repository; those were not separately opened or verified. The fetch tool flagged an apparent inconsistency between the body text ("16 frontier models") and a chart on the page (which it read as labeling 17 models) — this is reported as-is and not independently resolved. No paywall or access failure occurred; the page loaded successfully.
