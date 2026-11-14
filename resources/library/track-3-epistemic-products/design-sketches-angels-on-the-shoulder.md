# Design Sketches: Angels-on-the-Shoulder

**Authors:** Owen Cotton-Barratt, Lizka Vaintrob, Oly Sourbut, Rose Hadshar
**Source:** Forethought ("Design sketches for a more sensible world" series, Part 2 of 4), 2026
**URL:** https://www.forethought.org/research/design-sketches-angels-on-the-shoulder
**Accessed:** 2026-11-14
**Type:** Commentary (speculative/conceptual essay by an AI-focused research organization; not peer-reviewed or empirical)

## Summary

The piece argues that near-term AI systems could narrow the gap between the decisions people make and the decisions they would endorse on reflection. The authors sketch five conceptual technologies they group under the label "angels-on-the-shoulder" (some variants described as "angels-in-the-pocket," acting only when invoked), covering recommender systems, personalized learning, decision briefing, reflection coaching, and ambient risk-detection. They explicitly do not commit to building any of these, and flag a "fallen angel" failure mode in which the same tools constrain or manipulate choices rather than support them. The essay is openly speculative: it is a set of design sketches, not a report of built or tested systems.

## Key Claims / Findings

- The authors claim a persistent gap between how well people *could* decide and how well they actually do, attributed to limited information, poor situational awareness, and decisions made under time pressure or emotional load.
- Five sketched technologies:
  - **Aligned recommender systems**: feeds optimized for long-term, after-the-fact user endorsement rather than engagement, using delayed ratings and occasional "deep-dive" interviews to model preferences.
  - **Personalised learning systems**: an AI tutor that maps a field to a user's goals, designs assessments, and builds a parallel curriculum.
  - **Deep briefing**: an AI "chief of staff" that produces tailored decision briefs including stakeholder maps, precedent mining, outcome analysis, and stress-tested options, with sections a user can expand or rerun under changed assumptions. The authors state the hardest parts are context ingestion (information people struggle to articulate) and reliable analysis in nuanced, non-standard situations, and that humans should stay in the loop initially.
  - **Reflection scaffolding**: a Socratic-style AI coach, mostly listening and asking probing questions, intended to help users separate what they want from what they think they should want, with a separate crisis-detection module that refers users to human experts rather than handling crises itself.
  - **Guardian angels**: an always-on, privacy-first layer that detects risky, unkind, or value-misaligned actions in daily tools and issues graded nudges, up to alerting a trusted third party.
- On adoption, the authors suggest starting in high-demand niches (e.g., people dissatisfied with social media, or high-stakes professional sectors such as finance, law, and healthcare) and integrating into existing workflows (Slack, Docs, email, existing chatbots) rather than building standalone tools.
- They note a framing concern: guardian-angel-type tools should be presented as "catching silly mistakes" rather than as paternalistic "enhancing human judgement," to avoid user resistance.
- They acknowledge candidly that dedicated tools "may not beat chatbots at all" as general-purpose assistants improve, and that the hardest technical obstacle across several sketches is context ingestion plus reliability, not raw model capability.
- The essay states no empirical study was conducted; it is explicitly "design sketches," and the authors disclose they used AI assistance while drafting it.

## Relevance to the sprint

This is a direct conceptual precursor to the "decision brief" style epistemic product targeted by this sprint: the "Deep briefing" sketch describes almost exactly a decision-briefing AI assistant (stakeholder maps, precedent mining, stress-tested options, re-runnable under changed assumptions) and names the open problems — context ingestion and reliable analysis in non-standard situations — that a rubric for evaluating such briefs would need to test for. Because the source is itself speculative and non-empirical, it should be used for framing the design space and failure modes (including the "fallen angel" manipulation risk) rather than as evidence that any such tool works.

## Access notes / limitations

Full text was retrieved via WebFetch (HTML converted to text/markdown by the fetch tool) and read in full; no paywall or access restriction was encountered. The summary above reflects the fetch tool's extraction of the page content, not a direct render of the original HTML by this agent, so formatting details (e.g., exact figure captions, hand-drawn illustration descriptions) were not independently verified against the live page. No other sources were consulted to corroborate claims in this piece; it is presented here as a single primary source for an essay written by its listed authors.
