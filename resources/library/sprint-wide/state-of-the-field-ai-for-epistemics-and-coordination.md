# State of the Field: AI for Epistemics and Coordination
**Authors:** Ben_N and AlexCsaky (LessWrong usernames)
**Source:** LessWrong (Frontpage post, ~46-minute read), 2026
**URL:** https://www.lesswrong.com/posts/uw8RQ8yjKexnhTw6E/state-of-the-field-ai-for-epistemics-and-coordination
**Accessed:** 2026-11-14
**Type:** Expert analysis / field survey, grounded in original primary research (roughly 65 in-depth interviews conducted May-July 2026, plus 90+ broader conversations). Published on a community forum without peer review; not a journalistic piece.

## Summary
The post surveys an emerging, self-described "AI for Epistemics and Coordination" field: projects using AI to help people form beliefs, make decisions, and coordinate with one another. Its central argument is that deployment, not the ability to build prototypes, is the main bottleneck constraining the field's impact, and that this bottleneck is compounded by a lack of shared priorities among funders and builders and by the absence of any clearly agreed "winning" precedent. The authors map the field into nine overlapping niches with examples for each, report themes from their interviews, and close with four unranked recommendations for funders and field-builders.

## Key Claims / Findings

**Framing and stakes**
- The field is underdeveloped relative to its importance; left to market incentives alone, these tools will likely be built unevenly, since markets serve paying customers rather than public-interest needs.
- Early products and standards in this space may set lasting norms, which is one reason the authors argue against leaving development purely to existing incentives.
- Central claim, stated directly: "building a prototype is often far easier than getting it used."
- The field faces a chicken-and-egg problem: few projects reach deployment, so few clear wins emerge, so funders remain uncertain about where to invest.

**Nine field niches identified (Section 2), with cited examples**
1. Forecasting and strategic awareness (Metaculus, FutureSearch, Mantic, Sentinel, FRI, RAND Forecasting Initiative) — the authors judge the bottleneck here is deployment and workflow fit rather than forecast accuracy.
2. GovTech and institutional decision support (Singapore's Pair, USAi, UK i.AI) — constraints are mostly institutional (procurement, trust, data access, workflow integration); existing evidence covers adoption and time saved, not decision quality.
3. CivicTech and collective deliberation (Pol.is, CIP, Talk to the City, Remesh, Natter) — adoption is largely ad hoc and evaluation methods remain underdeveloped.
4. Epistemic and decision-support tools (Elicit, Alma, Society Library) — users may need epistemic features bundled into products they already want, rather than standalone tools.
5. Evaluations for model epistemics (FACTS, SimpleQA Verified, MASK, DarkBench, Petri, Bloom) — benchmark work is uneven and often one-off; Goodharting is flagged as a risk, and the authors see "misleadingness" as an underexplored evaluation target.
6. Verification, provenance, and reliability (Community Notes, SynthID, C2PA, Pangram, FullFact) — provenance mechanisms do not establish truth, and adoption at the point of consumption remains weak.
7. Multi-agent work (Cooperative AI Foundation, DeepMind multi-agent research, FOCAL, A2A) — safety-oriented deployment lags well behind the underlying research.
8. Human coordination and negotiation tools (Pactum, Luminance, Chord, Harmonica, BRKT) — described as among the least mature niches, though older tools like Spliddit and Panelot have real users.
9. AI manipulation and persuasion (UK AISI, CAIS, DebunkBot) — measurement of manipulation risk is currently ahead of defensive countermeasures.
- Adjacent but distinct areas noted: AI for science, AI for philosophy, misinformation/platform safety, and hardware-backed verification (FlexHEG).
- Encouraging examples cited: Mantic's $25M seed round following strong Metaculus Cup results; Pol.is's role in Taiwan's deliberation processes (explicitly caveated as one component of a broader process, not the dominant mechanism); the Habermas Machine; Community Notes and Pangram operating at platform scale.

**Interview themes (Section 3)**
- Deployment is the most consistently cited bottleneck across interviewees, though a minority view holds that few tools yet deliver enough value to justify changing an existing workflow.
- No shared view of priorities exists among funders and builders.
- Funders report they lack good projects to fund; builders report they lack funding, especially for the 6-18 month "refinement" stage between initial build and deployment-ready product.
- No clear "winning" precedent exists in the field, and practitioners disagree about what would even count as a win.
- The label "AI for Epistemics" itself is criticized as poor and overly broad; practitioners more often use terms like "decision intelligence."
- The authors describe a staged bottleneck model: entry and first-money stages are partly/fully working, but refinement, deployment, and proof stages are not working well. Case studies include a policy wargaming team that folded during a funding gap, and a collective intelligence startup unable to find design partners.
- Limitations the authors disclose about their own interview sample: all funders interviewed are EA/AI-safety-adjacent; no journalists were interviewed; coverage of niches 2.6 (verification/provenance) and 2.9 (manipulation/persuasion) relies more on desk research than interviews; the sample skews toward supply-side (builder/funder) voices rather than users or deployers.

**Recommendations (Section 4, presented as unranked)**
1. Test AI deployment in specific institutional workflows, via institution-first or tool-first approaches, framed around concepts like state capacity and "assurance cases"; forecasting is offered as a clear tool-first example.
2. Build decision-making evaluations and benchmarks — specifically a maintained, multi-turn benchmark for honesty, calibration, and non-sycophancy, while cautioning against using such evals to judge contested moral or political conclusions.
3. Run longer-runway field-building programs: 6-18 month residencies or fellowships with continuation decisions made before funding runs out, tied to specific users or deployment partners.
4. Develop pieces of an "Epistack" — shared infrastructure such as reliability tracking usable by both humans and AI agents — while flagging dual-use risks such as collusion, and suggesting adoption routes via API integration, incumbent acquisition, or bundling into products such as "guardian angel" agents.

**Disclosures**
- The authors state they used AI tools (identified in the piece as GPT-5.6 and Claude Fable 5) for desk research, improving writing clarity, and synthesizing interview themes, while stating the overall writing and judgment are their own except that AI assisted in drafting and compressing parts of Section 2.
- The post is not labeled by its authors as an output of any specific hackathon or sprint; it reads as independent field research. (Note: one comment on the post, by AlexCsaky, mentions a separate BlueDot-supported hackathon connected to the field-building recommendation, with a linked retrospective — this is a comment, not part of the main post's claimed provenance.)

## Relevance to the sprint
This piece is directly relevant to the "AI x Epistemics" theme because it is the most comprehensive available map of existing projects, organizations, and open problems across model epistemic evaluation, verification/provenance infrastructure, deliberation tools, and coordination/negotiation technology — precisely the landscape a hackathon team would need to orient within before choosing a project angle. Its core finding, that deployment and institutional adoption (not technical buildability) is the binding constraint, is a direct and actionable warning for any sprint team tempted to optimize only for a working prototype rather than a path to real use.

## Access notes / limitations
Full text of the main post was read via automated fetch and is reflected above in reasonable detail, though the fetch tool processed and summarized the page rather than returning raw HTML, so exact wording beyond the one quoted phrase should not be treated as verbatim. The comments section was retrieved only partially: two comments (AlexCsaky and Simon DeDeo) were captured, but a third comment, from a user named Maryam Hampaei, was cut off in the fetched content and is not described here beyond that it exists and is incomplete in the source retrieved. No claims about that third comment's content are made. The sprint reading list's attribution ("Ben N & Alex Csaky," LessWrong, 2026) matches what was found: the post is credited to LessWrong users Ben_N and AlexCsaky, posted 2 October 2026. No corrections to the sprint's citation were needed.
