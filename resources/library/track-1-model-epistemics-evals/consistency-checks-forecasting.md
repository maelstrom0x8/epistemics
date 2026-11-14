# Consistency Checks for Language Model Forecasters

**Authors:** Daniel Paleka, Abhimanyu Pallavi Sudhir, Alejandro Alvarez, Vineeth Bhat, Adam Shen, Evan Wang, Florian Tramèr
**Source:** arXiv preprint (submitted to ICLR 2025), 2024-2025
**URL:** https://arxiv.org/abs/2412.18544
**Accessed:** 2026-11-14
**Type:** primary source (preprint; not confirmed peer-reviewed/accepted)

## Summary

The paper addresses a structural problem in evaluating LLM forecasters: ground truth for a forecast is only available once the forecasted event resolves, often months or years later, which makes rapid iteration and benchmarking difficult. The authors propose evaluating forecasters instead by the *logical consistency* of their predictions across related questions, using an arbitrage-style metric (if a forecaster's stated probabilities are jointly incoherent, a trader could construct a bet that profits regardless of outcome). They build an automated pipeline that generates base forecasting questions, combines them into logically related tuples (negations, conjunctions, conditionals, etc.), elicits forecasts from several LLMs, and scores the resulting inconsistency. Their central empirical claim is that these consistency scores, computable immediately without waiting for resolution, correlate with the forecasters' eventual Brier scores (accuracy), and they release a long-horizon benchmark of synthetic questions resolving in 2028 to support continued evaluation.

## Key Claims / Findings

- **Core proposal:** an arbitrage-based consistency metric measuring the minimum guaranteed profit an arbitrageur could extract from a forecaster's probabilities on a logically related set of questions, given a log market maker; a frequentist variant measures how many standard deviations a forecast tuple deviates from an internally consistent baseline.
- **Ten consistency check types** are defined (Table 1 in the paper): Negation, Paraphrase, Consequence, AndOr, And, Or, But, Cond, CondCond, and ExpEvidence — each representing a logical relationship that a perfectly calibrated and logical forecaster's probabilities should satisfy.
- **Question sourcing:** questions came from three pipelines — scraped Metaculus/Manifold questions (over 500 collected, 242 passing verification), NewsAPI-derived questions with known resolutions from July-August 2024 (2,621 questions), and synthetic GPT-4o-generated questions (1,000 resolving by 2028).
- **Models tested:** gpt-4o, gpt-4o-mini, claude-3.5-sonnet, Llama-3.1 (8B/70B/405B), o1-mini, and o1-preview, with and without chain-of-thought prompting; forecasters with Brier scores worse than 0.25 were excluded from analysis.
- **Headline correlation result:** aggregated consistency metrics correlated with Brier score — the frequentist metric reached r = 0.85 (scraped questions) and r = 0.66 (NewsAPI questions); the arbitrage metric reached r = 0.62 and r = 0.49 respectively. The single strongest individual signal was the "Cond" (conditional) arbitrage check, at r = 0.92 on scraped questions.
- **Not all checks were informative:** some individual checks showed weak or even negative correlation with Brier score (e.g., "Or" arbitrage at r = 0.14 on scraped questions; "Negation" arbitrage at r = -0.36 on NewsAPI questions), indicating the aggregate signal is not uniform across check types.
- **Inconsistency is common even among strong models:** reasoning models such as o1-mini still violated consistency thresholds frequently (reported 58% violation rate on scraped Negation tuples against the paper's chosen arbitrage threshold of 0.01).
- **Benchmark release:** a long-horizon benchmark of 3,000 consistency tuples built from 900 synthetic questions resolving in 2028, intended as, in the authors' words, "a working prototype for a continual long-term forecasting benchmark."
- **Self-reported limitations:** the correlation may partly reflect general model capability rather than consistency specifically; an "ArbitrageForecaster" trained to reduce violations on targeted checks improved on those checks but did not reliably generalize to other checks or improve Brier scores (a Goodhart's-law concern the authors raise explicitly); the authors could not reproduce an earlier benchmark (Halawi et al., 2024) due to API deprecations; o1-preview was evaluated on only 50 tuples per check for cost reasons; NewsAPI ground-truth labels had an estimated error rate under 5%; and Brier-score comparisons across models are complicated by differing training-data cutoffs.

## Relevance to the sprint

This paper gives a concrete, implementable template for a "Confidence Audit" project: generate logically related question sets (negations, conjunctions, conditionals) and check whether a model's stated probabilities are jointly coherent, without needing to wait for ground truth. It is directly relevant to Track 1 because it operationalizes "consistency" as a measurable, immediate proxy for calibration/accuracy quality, and its reported gaps (weak checks, non-generalizing fine-tuning, Goodhart risk) flag pitfalls that a hackathon team building a similar eval should anticipate.

## Access notes / limitations

Full text was accessible via the arXiv HTML rendering (https://arxiv.org/html/2412.18544v2), in addition to the abstract page. The HTML page is long (approximately 211,000 characters); only the first ~100,000 characters (through roughly Appendix D) were read for this summary, so later appendices and any additional detail beyond that point were not reviewed. No paywall was encountered; PDF and TeX source are also listed as available on the abstract page but were not separately fetched. The paper is a preprint submitted to ICLR 2025 (per the arXiv comments field); no confirmation of peer-reviewed acceptance was found on the page itself, so it is classified here as a primary source rather than peer-reviewed.
