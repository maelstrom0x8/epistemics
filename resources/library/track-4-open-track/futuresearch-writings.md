# FutureSearch Writings

**Org:** FutureSearch
**Source:** futuresearch.ai, Research/Writings page (accessed 2026)
**URL:** https://futuresearch.ai/writings/
**Accessed:** 2026-11-14
**Type:** institutional / expert analysis — forecasting organization writeups

## Summary

FutureSearch is an AI research and forecasting company. The site promotes a Python SDK, Claude Code and Cursor integrations, a "Track Record" page with trading results and accuracy evaluations, and a tool to "Forecast a decision of your own." The page itself does not give a further self-description of the company (no mission statement or "about" text was visible in the fetched content).

The `/writings/` page is FutureSearch's research and blog hub. It is organized into three sections: **Papers** (academic-style publications, several tied to conference workshops), **Our current forecasts** (object-level forecasts on AI-industry and other questions, labeled by status: live, graded, or superseded), and **Everything else** (general essays, methodology notes, and case studies, mostly authored by named FutureSearch staff). No topic tags or per-article descriptions were visible beyond titles, authors, and dates.

## Key Claims / Findings

Titles and visible metadata observed on the page, grouped by the site's own section headings:

**Papers** (5, with authors and dates)
- "Evaluating Strategic Reasoning in Forecasting Agents" — Tom Liptay, Dan Schwarz, et al.; Apr 2026
- "Automating Forecasting Question Generation and Resolution for AI Evaluation" (ICLR 2026 Workshop on AI for Mechanism Design) — Nikos I. Bosse, Peter Mühlbacher, et al.; Jan 2026
- "Bench to the Future: A Pastcasting Benchmark for Forecasting Agents" — Jack Wildman, Nikos I. Bosse, et al.; Jun 2025
- "Deep Research Bench: Evaluating AI Web Research Agents" — Nikos I. Bosse, Jon Evans, et al.; May 2025
- "Towards a Realistic Long-Term Benchmark for Open-Web Research Agents" — Peter Mühlbacher, Nikos I. Bosse, et al.; Sep 2024

These five papers are the most directly relevant to forecasting-agent benchmarking and methodology.

**Our current forecasts — Live** (23 items; a sample, full list recorded in research notes): "When Will AI Make a Nobel-Caliber Discovery?", "Anthropic Revenue, ARR and Valuation Forecast, 2026 to 2027", "Anthropic and OpenAI IPO Dates and Valuations: Forecasts and Odds", "How we can prevent rogue agents", "Are the AIs Still Out There?", "Recursive Self-Improvement at Frontier AI Labs", "When Will AI Have Continual Learning?", among others on frontier-lab trajectories, AI company financials, and AI-safety-adjacent questions.

**Our current forecasts — Graded** (5 items): includes "Gemini 3.5 Pro Release Date: Grading a Forecast We Missed," "Is OpenAI Profitable? Our 2024 API Margin Analysis, Graded," and other forecasts the organization revisits against realized outcomes.

**Our current forecasts — Superseded** (4 items): older forecasts explicitly marked as replaced by updated analysis, e.g. "OpenAI Revenue, Losses, and Profitability in 2026: Full Financial Breakdown."

**Everything else** (31 items; essays and methodology posts, mostly by Dan Schwarz, Peter Mühlbacher, and other named staff): topics include forecasting methodology ("Forecasting accuracy scales with research," "The best forecasters agree with themselves," "The shared world model behind every forecast"), evaluation of AI model capabilities relevant to forecasting and research tasks ("Do Frontier AI Models Know What They Don't Know?", "Opus 4.6 does better research, Gemini 3.1 has better judgment," "Reasoning Effort Scaling: Claude 4.6 Gains, GPT-5 and Gemini Don't," "Higher effort settings in LLMs can reduce accuracy"), applied financial-analysis techniques using LLMs ("How to Analyze 10-K Filings With LLMs," "How to Analyze Earnings Calls with LLMs," "Can AI Forecast Stocks Through Fundamental Analysis?"), and critiques of other forecasting claims (two external links: "Contra Papers Claiming Superhuman AI Forecasting" on LessWrong, and "The Rationale-Shaped Hole at the Heart of Forecasting" on the EA Forum).

Section labels on the page itself ("Papers," "Our current forecasts," "live"/"graded"/"superseded," "Everything else") are the only structural/categorization text visible; no other descriptive blurbs accompanied individual entries.

## Relevance to the sprint

FutureSearch's output is directly relevant to Track 4's forecasting theme: several papers and essays concern benchmarking AI forecasting/research agents (Bench to the Future, Deep Research Bench) and methodological questions about forecast reliability (calibration, self-consistency, research-depth scaling). Separately, the organization's recurring posts on whether frontier models "know what they don't know" and how reasoning-effort settings affect accuracy bear on the adoption-impact side of the track, since they document observed gaps between model capability claims and measured forecasting/reasoning performance. The page is best used as a pointer to specific papers and posts rather than cited as a single source, since it aggregates many distinct pieces of varying rigor (peer-reviewed-style papers versus informal blog posts).

## Access notes / limitations

Full text of the `/writings/` index page was retrieved via automated fetch and is reflected above. The fetch returned the page's structure (section headings, article titles, authors, and publication/update dates) but did not include per-article descriptions, abstracts, or body text — those were not part of the index page itself. No "about FutureSearch" boilerplate was visible in the fetched content; the one-line characterization of FutureSearch above ("AI research and forecasting company") is inferred from the surrounding page elements (SDK, Track Record, "Forecast a decision of your own") rather than from an explicit mission statement. Individual linked articles were not opened or verified in this pass; any claims about a specific article's content beyond its title, authorship, and date are not covered by this note and have not been verified.
