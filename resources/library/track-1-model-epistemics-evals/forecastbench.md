# ForecastBench: A Dynamic Benchmark of AI Forecasting Capabilities

**Authors:** Ezra Karger, Houtan Bastani, Chen Yueh-Han, Zachary Jacobs, Danny Halawi, Fred Zhang, Philip E. Tetlock
**Source:** arXiv preprint (arXiv:2409.19839 [cs.LG]), 2024-2025. Sprint page attributes it to "ICLR 2025," but the arXiv abstract page itself carries no Comments or Journal-reference field confirming a conference venue; this was not independently verified against a second source.
**URL:** https://arxiv.org/abs/2409.19839
**Accessed:** 2026-11-14
**Type:** primary source (preprint; peer-review status at a venue not confirmed from this page)

## Summary

ForecastBench is a dynamic, continuously refreshed benchmark for evaluating forecasting ability, built to avoid the data-leakage problem that affects static benchmarks (questions are drawn only from events whose outcomes are unknown at the time of question creation). The authors assembled roughly 1,000 automatically generated and regularly updated questions and, on a random subset of 200, compared forecasts from expert human forecasters, members of the general public, and large language models. Their headline finding is that LLMs forecast worse than they perform on many other reasoning benchmarks relative to humans: expert forecasters outperformed the best-performing LLM in the comparison, a difference reported as statistically significant (p < 0.001).

## Key Claims / Findings

- **Problem motivation:** No standardized framework existed for evaluating the forecasting accuracy of ML/LLM systems on a fixed, comparable question set; static benchmarks risk data leakage because future events eventually resolve and become known.
- **Benchmark design:** ForecastBench consists of about 1,000 questions that are automatically generated and regularly updated, each concerning a future event with no known answer at the time of submission, intended to keep the benchmark leakage-free on an ongoing basis.
- **Forecaster comparison:** On a random sample of 200 questions, the authors collected forecasts from three groups: expert human forecasters, the general public, and LLMs.
- **Headline result:** Expert forecasters outperformed the top-performing LLM in the comparison (p < 0.001), despite LLMs often matching or exceeding human performance on other types of benchmarks.
- **Public leaderboard:** The authors report system and human forecasting scores on a public leaderboard hosted at forecastbench.org, implying the benchmark is intended for ongoing, repeated evaluation rather than a one-off test.
- **Scope note:** The abstract page fetched gives the overview and headline comparison; it does not itself provide the full scoring methodology (e.g., exact scoring rule, calibration metrics, question sourcing pipeline, or per-model breakdowns), which would require the full paper text.

## Relevance to the sprint

ForecastBench is directly on-topic for Track 1: it is a purpose-built, leakage-resistant evaluation of model forecasting accuracy against calibrated human benchmarks (expert superforecasters and the public), which is exactly the kind of calibration/accuracy comparison a "Confidence Audit" style project would want as a reference design or dataset. Its dynamic-question methodology is also a relevant pattern for any sprint project worried about benchmark contamination in epistemics evals.

## Access notes / limitations

Only the arXiv abstract page (https://arxiv.org/abs/2409.19839) was fetched and read, via WebFetch, which returned the title, author list, abstract content, subject categories, and submission history (v1 30 Sep 2024 through v5 28 Feb 2025). A PDF link, an experimental HTML full-text version, and TeX source are listed as available from that page, but the full text itself was not fetched or read in this session, so claims beyond the abstract (detailed methodology, specific numerical results beyond what the abstract states, limitations discussed in the body) are not verified here. The abstract page shows no "Comments" or "Journal reference" field, so the ICLR 2025 attribution from the sprint page could not be confirmed from this source alone.
