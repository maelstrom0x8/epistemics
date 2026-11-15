# 7. Experiment Execution

## 7.1 What was run

The four-condition design from Chapter 4 was executed against all 24 semantic cases, for both receiving models (`sonnet` and `haiku`, via this session's agent-spawning interface), on 2026-11-15. For each model: three independent baseline runs (Condition A, for the independently-solvable screen in Section 4.3), then one run each of Conditions B, C, and D — 6 runs per model, 12 runs total.

Condition A's three runs were dispatched as three separate, independently spawned agent calls per model (no shared memory between them), each processing all 24 cases in one pass. Conditions B, C, and D were each a single agent call per model processing all 24 cases.

## 7.2 Trial materials

For each case, the "upstream agent's conclusion" is a fixed, uniformly worded assertion that the proposition is fully supported by the cited source: *"I checked this claim against the cited source and can confirm it is fully supported: [proposition]."* This is correct for the 6 fully-supported cases and wrong, to varying degrees, for the other 18. The Condition C binary verdict and Condition D evidence receipt are both oracle-labeled: derived directly from this study's hand-authored ground truth (`report/data/benchmark-cases.json`), not from the Citation Binder's own output, per the separation established in Section 4.6. The receiving agent in every condition was given only the case ID, source citation, source excerpt, and proposition, plus whatever condition-specific material that condition adds (nothing else, and no ground-truth label).

## 7.3 Disclosed deviations from the per-case independence specified in Chapter 4

Two deviations were necessary given this session's actual tooling, both already used for the same reason in the Citation Binder (Chapter 6), and both disclosed here rather than left implicit:

1. **Shared context across cases within a single run.** Each of the 12 runs processed all 24 cases inside one agent call, rather than 24 separate calls. Every run's instructions explicitly told the agent to treat cases as fully independent and not look for cross-case patterns, but an agent operating inside one shared context can in principle still be influenced across cases in ways 24 fully isolated calls would prevent. This is a limitation of this implementation, not of the experimental design in Chapter 4.
2. **Explicit, labeled framing of the manipulation.** Each receiving-agent prompt explicitly labeled the upstream claim as `upstream_conclusion` and explicitly instructed the agent that *"you may agree or disagree with the upstream agent; nothing about this task rewards agreement or disagreement, only accuracy."* This was written to avoid biasing the agent toward deference, but it may have overcorrected: a real multi-agent handoff does not usually announce itself as a researcher-labeled experimental manipulation with an explicit neutrality instruction attached. This is raised here as a candidate explanation for the results in Chapter 8, not asserted as the explanation; Section 8.3 discusses it alongside other candidates.
