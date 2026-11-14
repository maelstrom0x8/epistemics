# Receipts Against Answer Substitution

*Investigating Whether Claim-Level Evidence Verification Improves Reliability in Multi-Agent AI Handoffs*

**Author:** O. Eze
**Track:** Apart Research, AI x Epistemics Research Sprint — Track 2, Trust Infrastructure
**Status:** In progress. Chapters 1 through 4 define the frozen research question and protocol. Later chapters are written only after the steps they depend on are actually completed.

## Abstract (draft, to be finalized after results)

AI agents increasingly pass claims to one another with citations, retrieved documents, and intermediate conclusions attached. A growing body of work shows that these citations frequently fail to support the claims they are attached to, and that a receiving agent will sometimes adopt an upstream agent's conclusion even when it has independent access to evidence that contradicts it. This study investigates whether providing a receiving agent with a claim-specific, evidence-bound verification receipt reduces its adoption of an upstream agent's unsupported conclusions, compared with an unverified handoff or a bare binary verdict. We construct a small, manually annotated benchmark of claim-evidence cases, build a minimal citation-verification component (no cryptographic signing), and run a controlled, four-condition comparison using Claude-family models as the receiving agent. The study is explicitly scoped as a single-model-family pilot: we do not have access to other model providers in this environment, and treat that as a stated limitation rather than a gap to paper over.

## Table of Contents

1. [Introduction](01-introduction.md)
2. [Related Work](02-related-work.md)
3. [Research Question and Hypotheses](03-research-question-and-hypotheses.md)
4. [Methodology](04-methodology.md)
5. Benchmark Construction — *pending: written after the annotated case set exists*
6. Citation Binder: Implementation — *pending*
7. Experiment Execution — *pending*
8. Results — *pending*
9. Discussion — *pending*
10. Limitations and Dual-Use Considerations — *pending*
11. Conclusion — *pending*

[References](references.md)
