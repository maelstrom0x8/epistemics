# AI can help humans find common ground in democratic deliberation

**Authors:** Michael Henry Tessler, Michiel A. Bakker, Daniel Jarrett, Hannah Sheahan, Martin Chadwick, Raphael Koster, Georgina Evans, Lucy Campbell-Gillingham, Teddy Collins, David C. Parkes, Matthew Botvinick, Christopher Summerfield (Google DeepMind, with several external co-authors, per the DeepMind publication page)

**Source:** Science, 2024 (vol. 386, issue 6719; published October 18, 2024)

**URL:** https://www.science.org/doi/10.1126/science.adq2852

**Accessed:** 2026-11-14

**Type:** Peer-reviewed (research article)

## Summary

This paper reports on the "Habermas Machine," a large language model trained to mediate group deliberation by generating and iteratively refining statements of "common ground" from participants' individually stated opinions and critiques. In a large-scale study with UK participants discussing divisive political topics (including Brexit, immigration, the minimum wage, climate change, and universal childcare), participants rated the AI-generated group statements as more informative, clear, and unbiased than statements written by human mediators, and many discussants updated their views toward convergence after the process. The authors report that the finding replicated in a virtual citizens' assembly with a demographically representative UK sample. This is independently paraphrased from the abstract and the authors' own publication summary; the full text of the article was not accessible to verify methodology or results beyond what is stated there.

## Key Claims / Findings

- The system (the "Habermas Machine") is an AI mediator that takes individual participants' opinions and critiques of draft group statements and uses them to iteratively generate and refine a statement intended to represent group common ground on a social or political issue.
- Study scale: N = 5,734 participants (per the abstract).
- Headline result: participants preferred AI-generated group statements over those written by human mediators, rating the AI statements as more informative, clearer, and less biased.
- Discussants frequently changed their individual positions after the deliberation process and converged toward a shared view.
- Using text embeddings, the authors report that the most successful group statements incorporated dissenting minority views while still reflecting the majority position.
- The core finding was reported as replicating in a second setting: a virtual citizens' assembly convened with a demographically representative sample of the UK population.
- Topics used in the discussions included Brexit, immigration, the minimum wage, climate change, and universal childcare (per search-result summaries of the paper; not independently verified against the full text).

Short verbatim phrase from the abstract (via the DeepMind publication page): "Participants (N = 5734) preferred AI-generated statements to those written by human mediators."

External commentary (not part of the paper itself): a Communications of the ACM blog post ("Computation and Deliberation: The Ghost in the Habermas Machine") reportedly argued that the study's statistical findings are sound but that optimizing for agreement risks reducing deliberation to a language-optimization problem, and noted that the study does not appear to measure how participants' attitudes toward *each other* (as opposed to toward the issue) changed over the course of deliberation. This characterization comes from a search-result summary of that commentary, not from reading the commentary itself, and should be treated as a secondhand account pending direct verification.

## Relevance to the sprint

The Habermas Machine is a direct precedent for a "Crux Mapper" tool: both target the problem of identifying what a group of disagreeing people actually diverge on, and both use an AI intermediary to synthesize individual positions into a shared artifact (a common-ground statement here, a crux map in the sprint's framing) rather than having one side simply "win" the argument. A Crux Mapper project could borrow the Habermas Machine's iterative critique-and-refine loop, but would need to additionally surface and preserve *where* and *why* disagreement persists, not only converge on a statement that commands shared assent, since collapsing to agreement is also where the external critique above locates the risk.

## Access notes / limitations

Direct fetches of the Science.org article page (both the plain DOI URL and the publisher's own author-token "view publication" link) returned HTTP 403 Forbidden with no body retrieved, on repeated attempts via two different fetch pathways. The full text, and the publisher's own abstract page, could not be accessed.

What was actually obtained: the abstract and author list as reproduced on Google DeepMind's own publication page (https://deepmind.google/research/publications/ai-can-help-humans-find-common-ground-in-democratic-deliberation/), which is the paper's own research group describing their published Science article, fetched successfully (HTTP 200). This is being treated as a reliable restatement of the abstract, but it is not the publisher's primary record, and the full text of the Science article (methods, detailed results, limitations section, supplementary materials) was not read. A third-party PDF mirror of the article was located via search but was not fetched, by policy, so no claims in this file rely on it.

All findings and claims above are therefore sourced to the abstract as reproduced by the authors' own institution and to search-engine summaries, not to a direct reading of the published article. Any detail beyond what is stated above (exact effect sizes, full methodology, statistical tests, limitations as stated by the authors) is unverified and intentionally omitted rather than inferred.
