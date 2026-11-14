# Did the Roll-Out of Community Notes Reduce Engagement With Misinformation on X/Twitter?

**Authors:** Yuwei Chuai (University of Luxembourg), Haoye Tian (University of Melbourne), Nicolas Pröllochs (JLU Giessen), Gabriele Lenzini (University of Luxembourg)
**Source:** Proceedings of the ACM on Human-Computer Interaction, Vol. 8, No. CSCW2, Article 428 (CSCW 2024), published November 2024; also available as arXiv preprint 2307.07960 (v1: 16 July 2023, v2: 23 August 2024)
**URL:** https://arxiv.org/abs/2307.07960 (PDF: https://arxiv.org/pdf/2307.07960)
**Accessed:** 2026-11-14
**Type:** Peer-reviewed (CSCW 2024, published via ACM; preprint also on arXiv)

## Summary

The paper is a large-scale empirical study of whether X/Twitter's Community Notes feature (formerly "Birdwatch") reduced engagement — measured as retweet and like counts — with misinformation after its roll-out to all U.S. users on October 6, 2022, and worldwide on December 11, 2022. Using Difference-in-Differences models at the feature-roll-out level and Regression Discontinuity Design at the note-display level, the authors analyze a dataset of all Community Notes and their source tweets from July 2021 through April 2023. They find a significant increase in the volume and speed of fact-checking after roll-out, concentrated on tweets from verified, high-follower accounts, but no significant reduction in engagement with misleading tweets attributable to the feature itself.

## Key Claims / Findings

- **Research question:** whether the roll-out of Community Notes to the U.S. (October 6, 2022) and globally (December 11, 2022) reduced retweet volume and like counts on misinformation, compared to the pre-roll-out period and to tweets without displayed notes.
- **Data:** all Community Notes contributions downloaded April 8, 2023 (68,235 notes, 75,508 note status histories, 2,293,934 ratings, 64,359 enrolled users), plus source tweets collected via X/Twitter's Academic Research API. Of 45,664 unique referenced tweet IDs, 39,268 (86%) were retrievable. After filtering to English-language tweets and restricting to the period from July 1, 2021 (six months after Community Notes launched, to allow the program to mature) to April 6, 2023, the analysis dataset comprises 30,267 unique tweets by 15,345 authors (83.9% of the English-language subset).
- **Methodology:** (1) Difference-in-Differences (DiD) comparing engagement with fact-checked tweets before versus after each of the two roll-out dates, including a placebo test to validate the design; (2) Regression Discontinuity Design (RDD) exploiting the threshold at which a note becomes "Currently Rated Helpful" and is displayed on a tweet, to estimate the discontinuity in engagement at note display; (3) robustness checks addressing confounds at multiple levels (e.g., account verification status, follower count, emotion and topic controls).
- **Headline result 1:** a significant increase in the volume and speed of fact-checking after roll-out, particularly for tweets from verified users with large followings.
- **Headline result 2:** no significant evidence, under either DiD or RDD, that the roll-out of Community Notes reduced retweet or like counts on misinformation.
- **Headline result 3:** engagement with community-fact-checked tweets did decline after the global expansion when veracity was not distinguished, but this decline disappeared when the analysis was restricted to the same set of authors fact-checked both before and after expansion — indicating the apparent drop was driven by a change in which accounts got fact-checked (composition effect), not by the notes reducing engagement on a given account's posts.
- **Authors' interpretation:** Community Notes may be too slow, relative to the short half-life of viral content, to curb engagement during the early and most viral stage of a tweet's diffusion. The paper cites background virality statistics (tweets lose about half their impressions within roughly 79.5 minutes, and about 95% have no meaningful impressions after two days) to support this timing argument — note this specific statistic is attributed by the authors to a separate cited source, not derived from their own dataset.
- Direct framing from the abstract: "we find no evidence that the introduction of Community Notes significantly reduced engagement with misleading tweets on X/Twitter."

## Relevance to the sprint

This is a directly on-point, peer-reviewed causal study of whether a deployed, platform-scale crowd-sourced fact-checking system actually changed real-world engagement with misinformation, rather than merely producing accurate notes. It is a strong counterpoint to any assumption that Community Notes "works" by default, and its composition-effect finding (section on authors fact-checked before/after expansion) is a useful methodological caution for Track 4 work on measuring real-world impact of crowd fact-checking interventions.

## Access notes / limitations

Full text was obtained directly: the arXiv abstract page (HTML) was fetched for title, authors, dates, and categories, and the PDF (https://arxiv.org/pdf/2307.07960) was downloaded and read in full-page-image form for the abstract, introduction, background (Section 2), and methods/data sections (Section 3, through variable extraction). The results and discussion sections beyond Section 3.2 were not individually re-verified page-by-page in this pass; the headline findings above are drawn from the paper's own abstract and introduction, which explicitly state the DiD/RDD results. No paywall was encountered; the paper is open access on arXiv and published via ACM under CSCW2024 (DOI 10.1145/3686967). No fabricated figures are included; all numbers above are quoted from the text as read.
