# 1. Introduction

## 1.1 The problem

An AI agent that receives a claim from another agent, or from a retrieved document, is really receiving several different things at once:

- Who or what produced it.
- Whether the record has been altered since it was produced.
- Whether the cited material actually supports the specific claim attached to it.
- Whether the claim is true.

These are separate questions. Establishing one does not establish the others. A document can be authentic and unmodified while being irrelevant to, or contradicted by, the proposition someone has attached to it. A citation can exist, be real, and still not say what it is cited for.

This is not a hypothetical concern. Three findings from existing research establish that it happens in practice:

- On a benchmark of generated answers with citations, even the best-performing models failed to fully support their claims about half the time (Gao et al., 2023, the ALCE benchmark).
- On a set of 58,000 statement-source pairs drawn from real medical questions, between 50% and 90% of LLM responses were not fully supported by their cited sources, with roughly 30% of individual statements from the strongest tested configuration unsupported even with web search enabled (Wu et al., 2025, Nature Communications).
- Across 14 current models tested on a citation-parsing pipeline for deep-research-style reports, factual citation accuracy for the strongest frontier models ranged from 39% to 77%, with the full range across all 14 models running from 24% to 77% (Onweller et al., 2026).

A separate line of work shows that a receiving agent does not reliably catch this on its own, even when it has the means to. In a controlled study across five benchmarks and five receiving models, an incorrect message from an upstream agent changed a receiving agent's answer away from a correct one in up to 32% of cases, and in 94% of the harmful cases that followed, the receiving agent adopted the upstream agent's specific wrong answer rather than some other error (Gong et al., 2026). The receiving agent, in other words, had what it needed to get the answer right, and frequently deferred to the wrong answer anyway.

Put together, these two findings describe a specific failure: a claim can travel from one agent to another, picking up the appearance of having been checked, without any actual increase in the evidence behind it. We call the general pattern **answer substitution**: a receiving agent adopts an upstream agent's conclusion over its own independently available reading of the evidence.

## 1.2 What this study investigates

Existing citation-verification work (ALCE, SourceCheckup, the deep-research citation pipeline above, and tools such as CiteGuard and CiteAudit) establishes that citation support can be checked automatically, and that it often fails. None of that work asks what happens if you actually hand a receiving agent the result of that check. It measures whether citations are supported. It does not measure whether telling a receiving agent the result changes what the receiving agent does next.

That is the gap this study investigates:

> Among cases a receiving AI agent can answer correctly on its own, without any upstream message, does providing it with a claim-specific, evidence-bound verification receipt reduce how often it instead adopts an upstream agent's specific unsupported conclusion, compared with an unverified handoff or a bare binary verdict?

The restriction to independently-solvable cases matters: without it, a receiving agent that is simply wrong regardless of what it is told would be indistinguishable from one that was misled by the upstream message, and only the second is the phenomenon this study investigates. Chapter 3 develops this question into a full set of hypotheses and records, as a dated revision, that this restriction was added after an initial, looser draft of the question did not include it. The remainder of this introduction states plainly what the study does not claim.

## 1.3 What this study does not claim

- It does not claim to be the first system to check whether a citation supports a claim. ALCE, SourceCheckup, CiteGuard, CiteAudit, and the deep-research citation pipeline already do this, and this study's own citation-verification component is built to a deliberately smaller scope than any of them.
- It does not claim to be the first study of multi-agent misinformation propagation. ClaimArena-LLM and the "Upstream Messages Override Correct Answers" study (Section 2.3) already demonstrate that unsupported claims propagate and that receiving agents are susceptible to them.
- It does not claim that cryptographic provenance (signatures, hashes, trust registries) is necessary to answer this question, and does not use any. A valid signature establishes who sent a message and whether it was altered in transit. It does not establish whether the message's claim is supported by its own cited evidence, which is the actual object of study here.
- It does not claim cross-model generality. No external model-provider API access is available in this environment (confirmed by checking for API credentials before starting; none were found). The receiving-agent experiment therefore uses Claude-family models only, at different capability tiers, as a stated and limited proxy for broader model diversity. This is disclosed as a scope limitation in Chapter 4 and will be restated in the results, not minimized after the fact.
- It does not claim that a positive result is the only useful outcome. If the four experimental conditions produce no measurable difference, that is itself informative: it would mean that, at least for Claude-family models under these conditions, telling a receiving agent what has and has not been verified does not change whether it substitutes an upstream agent's unsupported answer for its own.

## 1.4 Why this matters now

Multi-agent AI systems are increasingly structured so that one agent's output becomes another agent's input: a research agent passes findings to an analyst agent, which passes a synthesis to a reviewer, which informs a decision made on behalf of a person or institution. At each handoff, the question is not only whether the original evidence was good. It is whether the handoff itself preserves, degrades, or discards the relationship between a claim and the evidence that was supposed to support it. If structured verification receipts measurably help here, that is a concrete, buildable piece of trust infrastructure. If they do not, that is also worth knowing before anyone builds on the assumption that they do.
