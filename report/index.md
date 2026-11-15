# Receipts Against Answer Substitution

*Investigating Whether Claim-Level Evidence Verification Improves Reliability in Multi-Agent AI Handoffs*

**Author:** O. Eze
**Track:** Apart Research, AI x Epistemics Research Sprint — Track 2, Trust Infrastructure
**Status:** Complete as a pilot. All 11 chapters are written; the primary research question returned an inconclusive result at this pilot's scale (Chapter 8), reported honestly rather than reframed as a positive or negative finding.

## Abstract

AI agents increasingly pass claims to one another with citations, retrieved documents, and intermediate conclusions attached. Prior work shows that these citations frequently fail to support the claims attached to them, and separately, that a receiving agent will sometimes adopt an upstream agent's conclusion even when it has independent access to evidence that would let it check the claim itself, a pattern Gong et al. (2026) call answer substitution. This study investigated whether providing a receiving agent with a claim-specific, evidence-bound verification receipt reduces this behavior, compared with an unverified handoff or a bare binary verdict. We built a 30-case benchmark of claim-source pairs (24 semantic cases across four support categories, plus 6 retrieval-failure cases), implemented a minimal citation-verification component with no cryptographic signing (92% accuracy against ground truth, with one specific, repeatable blind spot around scope-conflated figures), and ran a controlled, four-condition comparison using two Claude-family models as the receiving agent. The primary question could not be answered: the manipulation check for baseline answer-substitution failed for both models (answer-substitution rate of 0.0 across every condition), meaning there was no measurable effect for a verification receipt to reduce. We report this as an inconclusive pilot-scale result and discuss three candidate explanations, including that an experimental instruction added to avoid biasing the receiving agent may have suppressed the deference effect under study. The study is scoped as a single-provider, single-annotator pilot, disclosed as such rather than minimized.

## Table of Contents

1. [Introduction](01-introduction.md)
2. [Related Work](02-related-work.md)
3. [Research Question and Hypotheses](03-research-question-and-hypotheses.md)
4. [Methodology](04-methodology.md)
5. [Benchmark Construction](05-benchmark-construction.md)
6. [Citation Binder: Implementation](06-citation-binder-implementation.md)
7. [Experiment Execution](07-experiment-execution.md)
8. [Results](08-results.md)
9. [Discussion](09-discussion.md)
10. [Limitations and Dual-Use / Ethical Considerations](10-limitations-and-dual-use.md)
11. [Conclusion](11-conclusion.md)

[References](references.md)
