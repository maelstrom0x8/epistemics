# A Full Epistemic Stack: Knowledge Commons for the 21st Century

**Authors:** Oliver Sourbut and Ben Goldhaber (the post states it is written in a personal capacity, though informed by the authors' work at the Future of Life Foundation)
**Source:** LessWrong (first published 19 December 2025; the post also links to a version hosted on oliversourbut.net)
**URL:** https://www.lesswrong.com/posts/DMswzhPQqkqx2XAma/a-full-epistemic-stack-knowledge-commons-for-the-21st-1
**Accessed:** 2026-11-14
**Type:** Commentary (a LessWrong forum essay combining argument and proposal; not peer-reviewed or institutional, though informed by the authors' institutional work)

## Summary

The post argues that reliable shared knowledge depends on a set of missing technical and social infrastructure, which the authors call a "full epistemic stack," running from raw observations and data up through verifiable inference, discourse mapping, and trust assessment. The authors contend that information overload, weak institutions, and platform incentives have made collective sense-making fragile, and that AI, automation, and biotechnology raise the stakes while large language models simultaneously make the needed tooling newly practical. The piece sketches the stack's layers and several downstream applications (such as Community-Notes-style annotation, "aligned" recommenders, and dynamic encyclopedias) but is explicitly framed as the first in a planned series, with implementation detail and distribution strategy deferred to later posts.

## Key Claims / Findings

- The stack has roughly three layers: **ingestion** (observations, data, and identity, with provenance metadata and stronger guarantees such as reputation or cryptographic proof where stakes are high); **structure**, split into "inference structure" (the genealogy of claims and evidence, so conclusions can be checked or repeated — the authors cite Nanopublications as an existing example) and "discourse structure" (how claims, counterarguments, and alternative positions relate over time); and **assessment** (credence, endorsement, and trust).
- Trust is argued to be a "late-binding" property that should be set at the application layer rather than built into the shared infrastructure itself.
- The authors state: "The epistemic power is in the process, not in the AI."
- They argue agreement on conclusions is less achievable, and less necessary, than agreement on the status of a debate: "We don't need to agree on all conclusions — but we can much more easily agree on the status of discourse."
- Cheap LLM labor is framed as the enabling condition: models can now handle the clerical work of tracing sources and mapping discourse structure that was previously too costly to do at scale.
- Once this metadata exists, it is argued to generate "positive epistemic spillover" — work done by one power user or agent becomes reusable by other applications.
- A proposed design for handling open contribution is "public library"-style authorities that maintain curated, well-connected views over a corpus while exposing public APIs for others to endorse or critique that view, rather than gatekeeping contribution outright.
- "Append-only" discourse records are described as more adversarially robust than centrally edited, opinionated summaries.
- The authors attribute the phrase "machines are in the human loop" to Audrey Tang, using it to frame AI's role as embedded within human sense-making rather than the reverse.
- The authors identify distribution and uptake, not technical feasibility, as the central risk, citing past failures of similar epistemic-infrastructure projects on exactly this point, and caution that "trying to be too preachy and prescriptive is presumably doomed to fail."
- The post is explicitly the first of a series; later posts are said to cover existing related efforts, interoperability, and distribution strategy — meaning this piece is a framing document, not a finished technical proposal.
- Comments on the post (not verified further here) raise concerns about bias in source-reliability judgments (citing Wikipedia as a comparison) and the risk of political capture of "epistemic" infrastructure projects; the authors reportedly responded that identifying verified authentic content via reputation or cryptographic provenance may matter more than detecting fakes directly.

## Relevance to the sprint

This post is a direct, programmatic match for the "AI x Epistemics" theme: it proposes a layered model of epistemic infrastructure (provenance, inference structure, discourse structure, trust/assessment) that maps closely onto the sprint's interest in trust infrastructure and epistemic products, and it explicitly argues that LLMs are the enabling technology that makes such infrastructure newly feasible. Its emphasis on distribution and uptake as the binding constraint, rather than technical design, is also directly relevant to any sprint project assessing adoption and real-world impact rather than only technical feasibility.

## Access notes / limitations

Full text was read (via a fetch of the live LessWrong page, including the post body and a brief look at the comment section). The bibliographic details given by the sprint reading list were checked against the piece itself: the authors (Sourbut and Goldhaber), venue (LessWrong), and year (2025) are correct, but the reading list's short title "A Full Epistemic Stack" omits the post's subtitle, "Knowledge Commons for the 21st Century," and the exact publication date (19 December 2025) was not stated in the reading list and is reported here for completeness. No independent verification was performed of secondary claims within the post itself (e.g., the characterization of Nanopublications, or the comment-thread exchange about deepfake detection) beyond what the fetched page presented; these are reported as the post's own claims, not independently confirmed facts.
