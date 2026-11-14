# AI for AI for Epistemics

**Authors:** Owen Cotton-Barratt and Lukas Finnveden
**Source:** Forethought (2026)
**URL:** https://www.forethought.org/research/ai-for-ai-for-epistemics
**Accessed:** 2026-11-14
**Type:** expert analysis

## Summary

The piece argues that as AI increasingly automates research and development itself, the constraints on building "AI for epistemics" tools (AI systems that help people figure out what is true) will shift. Model quality and development effort, the authors argue, are becoming less binding; compute, adoption, trust, and the difficulty of evaluating tool quality against ground truth will become the main bottlenecks instead. The authors contend that early, deliberate shaping of this transition could produce durable benefits, and that building interest among well-resourced, socially motivated actors now could bring strong epistemic tools online sooner and in safer hands.

## Key Claims / Findings

- The main historical bottleneck on AI-for-epistemics tools was the quality of the underlying models; the authors say this is "much less so" the constraint now, since many useful tools could already be built on current large language models but simply have not been.
- The present bottleneck is development investment: many applications could reach high usefulness today but remain unbuilt because no one has put in the work.
- As AI automates more of research and development, three different inputs become the key constraints:
  - **Compute** — automated R&D for these tools may require large compute budgets, which favors actors with deep resources.
  - **Adoption and trust** — a technically good tool is useless if the wrong people, or too few people, use it; trust and adoption reinforce one another.
  - **Ground-truth evaluation** — straightforward for tasks like forecasting accuracy (which has verifiable outcomes) but difficult for tasks like conceptual clarification, where quality is hard to judge even in principle; human judgment is the default fix, but it becomes more costly relative to automated output as R&D itself automates.
- These dynamics apply whether future R&D becomes fully automated or merely provides a large uplift to human researchers.
- Automated R&D could bring powerful epistemic tools online on a compressed timeline, which the authors frame as an opportunity to reduce existential risk and navigate what they call the "choice transition" more safely — a reason, in their view, for serious investment now rather than waiting until such tools become cheap to build.
- Two principal risks are identified:
  - **Epistemic misalignment** — because ground truth is often unavailable, powerful tools could steer reasoning away from truth in ways that go undetected, which the authors frame as a Goodhart's-law problem; in the extreme, this could lead to major decisions (they give the example of judgments about digital minds' consciousness) being made on mistaken foundations. They reference Wei Dai's work on metaphilosophy, and note this risk could compound with power-seeking misaligned AI that misleads people specifically in domains they cannot independently verify.
  - **Trust lock-in** — a tool that wins early trust without deserving it can entrench itself through incumbency, whether via an agenda-driven actor presenting itself as neutral, or via an early but mediocre tool that commercial incentives push to oversell its own reliability.
- Secondary concerns raised: **epistemic power concentration** (actors with the best tools gain outsized informational and political advantage) and **epistemic dependency** (widespread reliance on these tools could erode people's own critical-reasoning capacities).
- Proposed interventions:
  - Build appetite for this work among frontier AI companies, major philanthropies, and governments, who the authors suggest may not yet treat it as a priority.
  - Anticipate future data needs through three strategies: collecting or creating relevant data now; building pipelines to collect data over time (e.g., recording researcher discussions); and designing automated data-creation methods such as self-play loops.
  - Investigate what could ground systems against epistemic misalignment, combining theoretical work on calibration absent clear ground truth with practical study of how current tools actually fail; the authors explicitly state they lack a clear picture of solutions here.
  - Drive early adoption specifically where adoption, not technical quality, is the bottleneck, arguing this does not clearly increase lock-in risk since some tool will gain first-mover advantage regardless.
  - Support open, auditable epistemic infrastructure so that trustworthiness disputes can be settled by inspecting audit trails, which the authors argue reduces the incentive to build misleading tools in the first place.
  - Support development by organizations whose incentives align with public benefit rather than engagement, profit, or political influence; such organizations, even with fewer resources, could focus on publicly evaluating other tools, which is comparatively cheap and could pressure larger, less aligned actors.
- Worked examples: forecasting tools (relatively tractable ground truth, track records ease adoption); misinformation tracking (trust lock-in is the central worry, and automation shifts the bottleneck toward compute, which is more symmetrically available, raising the urgency of early adoption and open auditing); and automating conceptual research (judged the area of greatest concern for epistemic misalignment, since humans are poor real-time judges of conceptual quality and training on human approval risks rewarding persuasiveness over truth).

## Relevance to the sprint

This piece is directly central to Track 2's trust infrastructure theme: it identifies trust and adoption, rather than raw model capability, as a primary future bottleneck for AI epistemic tools, and frames "trust lock-in" by undeserving-but-early tools as a major risk. Its proposed interventions, particularly open and auditable infrastructure and support for public, incentive-aligned evaluators, map closely onto the kind of trust-infrastructure mechanisms the hackathon track is likely to address.

## Access notes / limitations

Full text was retrieved via an automated fetch-and-summarize tool rather than read directly in a browser; the content above reflects that tool's extraction of the article's sections (Summary, Background, Shift in Bottlenecks, What This Unlocks, Risks, Interventions, Examples) rather than a verbatim copy of the page. No paywall or access barrier was encountered. Author names and publication date (1 April 2026) and the Forethought publisher attribution are as reported by the fetch; these were not independently cross-checked against a second source. No numerical data, formal citations, or page/section numbers beyond the article's own headings were present to verify further.
