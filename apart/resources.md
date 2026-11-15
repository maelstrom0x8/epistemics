# Suggested reading material
> Most relevant items in bold.

## Sprint-wide
- ["State of the Field: AI for Epistemics and Coordination"](https://www.lesswrong.com/posts/uw8RQ8yjKexnhTw6E/state-of-the-field-ai-for-epistemics-and-coordination) (Ben N & Alex Csaky, LessWrong, 2026): a survey of the field that finds getting tools adopted, not building them, is the main bottleneck, and lays out priority directions.
- ["What's Important in 'AI for Epistemics'?"](https://www.forethought.org/research/whats-important-in-ai-for-epistemics) (Lukas Finnveden, 2024): Why early epistemic tools have outsized, path-dependent effects.
- ["AI Impacts on Epistemics: the Good, the Bad and the Ugly"](https://www.forethought.org/research/ai-impacts-on-epistemics-the-good-the-bad-and-the-ugly) (Cotton-Barratt & Hadshar, Forethought, 2026): a taxonomy of how AI could push collective knowledge either way.
- "Design Sketches for a More Sensible World" (Cotton-Barratt, Vaintrob, Sourbut & Hadshar, Forethought, 2026): 19 buildable tool sketches with feasibility notes, spanning all four tracks.
- "Project Ideas: Epistemics" (Finnveden, 2024, updated 2025): a concrete list of neglected projects, many needing no ML skills.
- "The most interesting startup idea I've seen recently: AI for epistemics" (Benjamin Todd, 80,000 Hours, 2024): an accessible introduction.
- "A Full Epistemic Stack" (Sourbut & Goldhaber, LessWrong, 2025): an integrated infrastructure sketch that individual Sprint tools could slot into.
- "Multi-Agent Risks from Advanced AI" (Hammond et al., Cooperative AI Foundation, 2025): the threat-model taxonomy for interacting AI systems.

## Track 1: Model Epistemics & Decision-Making Evals
- "Design Sketches: Collective Epistemics" (Cotton-Barratt, Vaintrob & Sourbut, Forethought, 2025): includes the epistemic virtue evals sketch several projects build on directly.
- "The MASK Benchmark" (Ren et al., CAIS, 2025): 1,000+ scenarios showing models knowingly contradict their own beliefs under pressure.
- "DarkBench" (Kran et al., ICLR 2025 oral): 660 prompts measuring six manipulative patterns.
- "SycEval" (Fanous et al., AIES 2025) and "ELEPHANT" (Cheng et al., 2025): answer-flipping under rebuttal pressure and social sycophancy respectively.
- "Why Language Models Hallucinate" (Kalai et al., OpenAI, 2025): binary-graded benchmarks reward confident guessing over honest abstention.
- "ForecastBench" (Karger et al., ICLR 2025): a contamination-free benchmark of nightly-refreshed questions.
Petri and Bloom (Anthropic, 2025): open-source agentic tools for behavioural auditing and targeted eval generation.
EU AI Act, Article 5 (applicable since Feb 2025): a manipulation ban with few measurement standards behind it.

## Track 2: Trust Infrastructure
C2PA Technical Specification v2.4 (2025) and c2patool: the provenance standard.
Community Notes open dataset
- "From Birdwatch to Community Notes" (Mohammadi et al., 2025): four years of longitudinal analysis of the system under real incentives.
- "AI for AI for Epistemics" (Cotton-Barratt & Finnveden, Forethought, 2026): early epistemic tools accumulate trust whether or not they deserve it, so auditability is a design requirement.

## Track 3: Epistemic Products
"Design Sketches: Angels-on-the-Shoulder" (Cotton-Barratt, Vaintrob, Sourbut & Hadshar, Forethought, 2026): the track's core menu, from aligned recommenders and deep briefings to guardian angels.
"Guardian Angels: LLM Personalization for Productivity and Security" (Gwern, 2026): the original always-on personal agent essay.
"Sycophancy in GPT-4o" (OpenAI, 2025): the first-party postmortem of how thumbs-up signals produced a rolled-back, escalation-prone model.
"Sycophantic AI Decreases Prosocial Intentions and Promotes Dependence" (Cheng et al., Science, 2025): agreeable chatbots make users more convinced they are right and less willing to repair disputes.
"AI Can Help Humans Find Common Ground" (Tessler et al., Science, 2024): the Habermas Machine study, a working template for machine-mediated crux finding.
Track 4: Open Track (deployment, adoption and impact)
"The AI Adoption Gap" (Vaintrob, Forethought, 2025): why government lags private AI adoption and which procurement fixes close the gap; the track's framing document.
"AI Tools for Existential Security" (Vaintrob & Cotton-Barratt, Forethought, 2025): names "why superior epistemic tools fail to get adopted" as an open problem.
"Did the Roll-Out of Community Notes Reduce Engagement With Misinformation?" (Chuai et al., CSCW 2024): causal evidence that notes cut reposts but arrive too late to dent total views.
Community Notes public dataset: every note, rating and status history, downloadable without an account.
"Accuracy of Forecasts in Strategic Intelligence" (Mandel & Barnes, PNAS, 2014): six years of intelligence forecasts scored for calibration (pre-AI).
FutureSearch, Swift Centre and Sentinel writeups: three live forecasting organisations publishing methods and client-facing outputs.

# Example projects per track
## Track 1: Model Epistemics & Decision-Making Evals
MisleadBench. Models can be technically accurate while leaving a false impression, and existing honesty benchmarks (MASK, DarkBench) mostly test single-turn lies. Build a multi-turn benchmark that first elicits what a model implies, then challenges it to defend the claim, scoring the gap between implied and defended positions, with a question-rotation protocol so scores stay meaningful.
Confidence Audit. Does the model know how solid its claims are? Calibration is already measured on cleanly resolvable questions (ForecastBench, consistency checks). Design a protocol that elicits a model's confidence in its own recommendations across domains where ground truth arrives later, then verify elicited confidence against outcomes.
FlipRate. A model that agrees with whoever pushed back last is useless for decisions. Single-turn agreement is already measured (SycEval, ELEPHANT). Measure flip curves: how a model's answer and stated confidence change across one, two and three escalating rebuttals, separating warranted updating from capitulation.
Epistemic virtue eval suite. Forethought's collective-epistemics sketches propose evaluating calibration, honest uncertainty, manipulation resistance and claim-level scoring, but no maintained suite exists. Build them as Inspect tasks with transparent rubrics, run them across frontier models, and publish grader disagreements as part of the result.
Article 5 measurement protocol. The EU AI Act bans manipulative and deceptive AI techniques, yet regulators have no agreed test procedure. Draft a protocol mapping DarkBench and MASK-style measurements onto Article 5(1)(a) legal language, with worked examples and thresholds.
Track 2: Trust Infrastructure
Track-Record Ledger. Pundits, forecasters and outlets make checkable public claims, but nobody keeps score in a form software can consume (Community Notes is the closest thing). Build a public API that records dated claims, resolves them against primary sources, and serves reliability summaries per source, plus a first consumer: a browser extension or feed-reader plugin showing a source's track record beside their latest claim.
Tamper-Evident Action Recorder. When an AI agent takes a consequential action, the operator's own logs are the only record, and they can be edited. An example project here could be to build a signed, secure logging layer on the OpenTelemetry GenAI conventions so instrumented agent frameworks emit append-only, verifiable traces (Certificate Transparency is the precedent), plus a viewer for auditors.
Citation Binder. A large share of citations in papers, briefs and Wikipedia articles do not support the sentence they are attached to. Build a tool that locates each cited source and verifies whether it genuinely supports the specific claim, with per-citation verdicts and quoted passages (evaluation data exists: AVeriTeC).
Provenance Study. Everyone assumes provenance and reliability metadata will help AI systems behave better; nobody has measured it. Run a controlled experiment: the same research tasks with and without machine-readable signals (C2PA manifests, track records, Community Notes context), measuring accuracy, citation quality and susceptibility to planted false sources. Users: agent-framework developers deciding whether consuming signals is worth the cost.
Track 3: Epistemic Products
Dispute Escalation Benchmark. When someone describes a conflict with their landlord, employer or ex-partner, does the chatbot steer them towards repair or escalation (evidence this is a live harm)? Build realistic dispute scenarios, ask practising mediators to define graded good advice, and score frontier models after every release.
Decision-Brief Rubric. Use expertise in, for example, financial-guidance, careers or health charities to define a rubric, then build a grading harness scoring chatbot briefings against it.
Crux Mapper. Groups argue past each other because nobody knows which factual questions actually divide them. Run short asynchronous AI interviews with each member, extract claims and probabilities, and render a disagreement map showing shared ground, genuine cruxes and internal inconsistencies (cf. the Habermas Machine, which drafts agreement; this maps disagreement).
Track 4: Open Track
Scenario planning on tap for resilience teams. Run hundreds of LLM narrative simulations & forecasts from a plain-language situation brief and report recurring failure points in the two-page format emergency planners already use.
Fast facilitation for communities that cannot afford a mediator. An assistant that interviews each participant asynchronously, maps where people actually agree and disagree, and drafts candidate consensus statements for human sign-off.
QALY for epistemics. Health economics got serious when the QALY gave decision-makers one comparable unit; epistemic interventions have nothing similar, so budgets go to whatever demos well. Design a candidate decision-quality metric and measurement kit, then stress-test it retroactively on documented decisions.
Procurement Gap Report. Legislative staff use personal AI accounts because official procurement cannot keep up. Trace, at the document level, exactly which rules block a legislature from getting access to the best AI and decision-making tools.
Do their numbers match? Pair quantitative claims from parliamentary transcripts and press releases with the statistical releases they cite, flag mismatches with links to primary sources, and publish as an auditable open dataset.
A wish registry for privacy-preserving matchmaking. Participants privately register offers and needs; an AI matcher reveals a connection only when both sides' criteria are met, with logs auditable by a neutral steward.
Next: Guidelines
