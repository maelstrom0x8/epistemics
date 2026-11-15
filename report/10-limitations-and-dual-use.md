# 10. Limitations and Dual-Use / Ethical Considerations

This chapter is required by the sprint's submission guidelines and is written to the same standard as the rest of this report: specific, falsifiable where possible, and not used as a place to bury caveats that belong earlier in the document. Several of these limitations are discussed in more depth in the chapters cited.

## 10.1 Scope limitations

**Single-provider pilot.** Both receiving models are Claude-family models (`sonnet` and `haiku` aliases), accessed through this session's own agent-spawning interface. No external model-provider API access was available in this environment (checked directly before the study began). This is a within-provider, two-tier comparison, not a cross-provider one, and nothing in this report should be read as a claim about model families this study did not test (Section 4.7).

**No fixed model snapshot or sampling control.** The `sonnet` and `haiku` aliases resolve to whichever specific model version was current when each trial ran, on 2026-11-15. No pinned version identifier, and no control over temperature or sampling, was available through this interface (Section 4.7). A reader attempting to reproduce this experiment at a later date may be running a different underlying model version under the same alias.

**Single-annotator benchmark.** All 24 semantic cases and 6 retrieval-failure cases were authored and labeled by one person, checked in two passes against a written rubric rather than cross-validated by an independent second annotator (Section 4.4, Section 5.3). One labeling defect was found and corrected during this project (Section 5.5); the two-pass procedure did not catch it, an external check (the Citation Binder's independently applied rollup logic) did. This is disclosed as evidence that a single-annotator benchmark of this kind is not fully self-correcting, not as evidence that the correction process failed.

**Small scale.** 24 semantic cases, 16-17 of them eligible for the primary comparison after independently-solvable screening (Section 8.1), is a pilot sample, not one sized to detect a plausible effect with adequate power. A null result at this scale is reported as inconclusive, not as evidence of absence (Section 8.1, Section 9.1).

**Reused source material.** Every semantic case pairs a proposition with a source this study had already independently verified elsewhere in its own research process (Section 5.2), which carries a disclosed risk of receiving-model familiarity with the underlying papers from pretraining, partially but not fully mitigated by the passage-level nature of the task.

**Shared context across cases within a single trial run, and an experimental instruction that may have suppressed the effect under study.** Both are discussed in full in Section 7.3 and Section 9.2 and are not repeated here beyond naming them: this study's own experimental design may be partly or wholly responsible for the null result in Chapter 8, and that possibility is treated as a limitation of this pilot's execution, not resolved.

**Citation Binder architecture.** All three of its steps (decomposition, matching, classification) are performed by a single prompted model call rather than a dedicated retrieval index or natural-language-inference model (Section 6.1), and its rollup logic has a specific, documented blind spot around cherry-picked or scope-conflated figures (Section 6.3, Section 9.3).

**Frozen corpus, not live retrieval.** This study's findings describe behavior against a fixed, pre-verified corpus of source excerpts. They do not describe behavior under live web retrieval, where link rot, paywalls, and retrieval variance introduce failure modes this study's retrieval-failure cases only partially approximate (Section 5.4).

## 10.2 Dual use

A claim-specific evidence receipt is only informative if it is itself accurate. If a verification component (automated or otherwise) produces a confidently formatted but wrong receipt, a receiving agent or a downstream human reader could place more trust in a false receipt than in an unverified claim, laundering false confidence rather than reducing it. This is precisely why this study evaluates the Citation Binder's own accuracy separately from the behavioral effect of a correct receipt (Section 4.6): a hypothetical positive behavioral result would not, by itself, certify that any particular automated verifier is safe to deploy. This pilot's own Citation Binder scored 92% overall but had a specific, repeatable blind spot (Section 6.3, Section 9.3); a system built on it without awareness of that blind spot would systematically mislabel one category of citation misuse with high confidence.

More broadly, any infrastructure that marks claims as "verified" or "unverified" creates a point of control. If adopted by a platform or institution with unaccountable authority over what counts as verified, the same mechanism intended to reduce unsupported-claim propagation could instead be used to selectively suppress or privilege claims for reasons unrelated to evidential support. This is a structural risk of trust infrastructure as a category, not unique to the specific design proposed here, and nothing in this study's current scope mitigates it; a deployment-stage version of this idea would need governance safeguards this research-stage pilot does not address.

## 10.3 Human subjects and data

This study involves no human subjects and no personal data. All receiving-agent trials are model API/tool calls over fixed, already-public source text (academic abstracts, technical specifications, and similar material already cited throughout this report). No findings here are claimed to generalize to human reviewers or human trust calibration; extending this design to a human-facing verification tool would raise separate questions this study does not address.

## 10.4 Disclosure on AI tool use

This entire research project, including the benchmark construction, the Citation Binder implementation, the receiving-agent trials, the discovery and correction of two distinct defects (a benchmark labeling error in Section 5.5 and a scoring script bug in Section 8.6), and the writing of this report, was conducted using Claude Code (Claude-family models) as the primary research and drafting tool, under the direction and review of the named author. Every external factual claim in this report was independently checked against a primary source before being relied upon (documented per-source in `references.md`), consistent with this project's own stated research protocol (`CLAUDE.md`) and with the sprint's own prohibition on made-up results or references.
