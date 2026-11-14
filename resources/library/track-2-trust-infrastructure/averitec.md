# AVeriTeC: A Dataset for Real-world Claim Verification with Evidence from the Web

**Authors:** Michael Schlichtkrull, Zhijiang Guo, Andreas Vlachos (Department of Computer Science and Technology, University of Cambridge)
**Source:** arXiv preprint 2305.13117; accepted to the 37th Conference on Neural Information Processing Systems (NeurIPS 2023), Datasets and Benchmarks Track
**URL:** https://arxiv.org/abs/2305.13117 (PDF: https://arxiv.org/pdf/2305.13117, v3, 8 Nov 2023)
**Accessed:** 2026-11-14
**Type:** Primary source (dataset/benchmark release) and peer-reviewed (NeurIPS Datasets and Benchmarks Track)

## Summary

The paper introduces AVeriTeC, a dataset of 4,568 real-world claims drawn from fact-checks published by 50 different fact-checking organizations, collected via Google's FactCheck Claim Search API (itself built on the ClaimReview schema). Each claim is annotated with question-answer pairs grounded in evidence documents found on the open web, a four-way veracity label (supported, refuted, not enough evidence, or a newly introduced "conflicting evidence/cherrypicking" class), and a free-text justification explaining how the evidence supports the verdict. The authors designed a multi-round annotation pipeline specifically to avoid three failure modes they identify in prior fact-checking datasets: claims that cannot be verified without added context ("context dependence"), annotated evidence that does not actually establish the claimed label ("evidence insufficiency"), and evidence published after the claim date ("temporal leakage"). They also propose an approximate-matching evaluation metric (the "AVeriTeC score") and a runnable baseline pipeline for retrieving evidence and predicting verdicts.

## Key Claims / Findings

**Dataset construction**
- 4,568 claims from fact-checking articles by 50 organizations, sourced through the Google FactCheck Claim Search API (CC-BY-4.0, built on the ClaimReview project).
- Annotation pipeline (Figure 1): claim normalization → question-answer generation round 1 → evidence sufficiency check → question-answer generation round 2 (if needed) → second sufficiency check → final label. Claims that are non-text/non-factual or where the fact-checker's label is mismatched are discarded.
- Annotators were restricted to evidence documents published before the claim date, and splits (train/dev/test) are ordered temporally, specifically to prevent temporal leakage, including leakage from pretrained language models used downstream.
- Inter-annotator agreement: free-marginal κ = 0.619 (described as "substantial") on verdicts, based on double-annotation of 100 claims; Fleiss' κ on the same subsample was 0.503. The authors compare favorably to a cited prior "hard" fact-checking annotation task with κ between 0.30 and 0.63.
- All evidence pages are archived via the Internet Archive to guard against link rot.
- Dataset and baseline code released under CC-BY-NC-4.0 at https://github.com/MichSchli/AVeriTeC.

**Evaluation metric**
- Because AVeriTeC evidence is retrieved from the open web rather than a fixed corpus like Wikipedia (as in FEVER), exact-match evidence scoring is not possible. The authors instead score question-answer pairs via approximate matching: a pairwise scoring function (Hungarian METEOR, using the Hungarian algorithm for optimal assignment between generated and reference QA sequences, with METEOR as the underlying similarity function).
- Veracity and justification scores are credited only when the evidence match score exceeds a cutoff λ; the authors recommend λ = 0.25 and call veracity accuracy at this threshold the "AVeriTeC score."
- Measuring their own two annotation rounds against each other with this metric gave low agreement (0.28 for questions, 0.22 for questions+answers), which the authors flag as evidence that automatic scoring of "equivalent but differently phrased" evidence is intrinsically difficult.

**Baseline pipeline and headline results**
- Baseline stages: query generation from the claim (reduced to verbs/nouns/adjectives) → Google Search retrieval of documents published before the claim date → question generation (best model: BLOOM-7b, few-shot) → BM25 coarse filtering plus BERT-large reranking of evidence sentences → BERT-large stance detection for veracity → BART-large for justification generation.
- Table 4 (macro-F1 across the four veracity labels): no-evidence baseline 0.17; full AVeriTeC pipeline 0.23; gold-evidence upper bound 0.49; gpt-3.5-turbo (prompted, no retrieval) 0.39.
- gpt-3.5-turbo scored higher on raw veracity macro-F1 than the retrieval-based baseline but is explicitly flagged as not directly comparable, since it cannot produce real, checkable evidence sources; many of its generated "evidence" answers are either alternative correct answers or outright hallucinations.
- Concrete documented failure: for the claim "1 cup of dandelion greens = 535% of your daily recommended vitamin K and 112% of your daily recommended vitamin A," gpt-3.5-turbo labeled it "supported" and generated a fabricated evidence string attributed to the USDA; the authors state directly that "there is no such statement from the USDA," and the correct verdict actually requires a multi-step calculation across several question-answer pairs, not a single citation.
- The veracity model performs particularly poorly on the new "conflicting evidence/cherrypicking" class, with precision around 10% even using gold evidence, often because any question that merely adds context gets misclassified as refuting evidence.
- Manual analysis of 20 development examples found that Google Search plus generated questions returned useful evidence for only 9/20 claims; using the gold (human-written) questions as search queries instead found correct evidence for 16/20, underscoring that retrieval/query generation, not downstream reasoning, is the main bottleneck in the baseline.

## Relevance to the sprint

AVeriTeC is directly on point for a "Citation Binder" that checks whether cited sources actually support the claims attached to them: its core annotation structure (claim → evidence-grounded question-answer pairs → justification linking evidence to verdict) is essentially a formal schema for "does this evidence support this claim," and its evaluation metric is built around scoring whether retrieved evidence is adequate rather than merely topically related. The paper's own case study of gpt-3.5-turbo fabricating a plausible-sounding USDA citation that does not exist, while still landing on the correct verdict, is a concrete, documented example of exactly the failure mode (confident claims with non-existent or non-supporting sources) that a citation-verification tool is meant to catch.

## Access notes / limitations

Full text was retrieved and read directly (not just the abstract): the arXiv HTML abstract page was fetched for title, author, date, and category metadata, and the PDF (arxiv.org/pdf/2305.13117, v3) was downloaded and read in full for pages 1-3 and 6-9, covering the abstract, introduction, related work, annotation structure, evaluation methodology, baseline design, and results tables. Remaining sections of the paper (e.g., full annotation guideline appendices, complete related-work comparison details beyond Table 1) were not read and are not characterized here. No content in this file was taken from memory or invented; all figures (κ = 0.619, macro-F1 values, the dandelion-greens example) are transcribed from the tables and text as rendered in the PDF.
