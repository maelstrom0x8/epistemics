# Community Notes (X/Twitter)

**Org:** X Corp (formerly Twitter; code and documentation published under the `twitter` GitHub organization)
**Source:** GitHub repository (code/documentation), 2022-present
**URL:** https://github.com/twitter/communitynotes
**Accessed:** 2026-11-14
**Type:** open dataset + code (primary source for algorithm; institutional for program description)

## Summary

The `twitter/communitynotes` repository holds the documentation and source code behind X's Community Notes program (formerly Birdwatch), which lets contributors attach notes to posts that may be misleading. The repository's stated purpose is to let the public inspect and contribute to the scoring algorithm that decides which notes are shown. It bundles the scoring code (`scoring/src`), the Markdown source of the public Community Notes Guide, a template for the AI Note Writer API, and the original 2022 research paper (`birdwatch_paper_2022_10_27.pdf`). The underlying notes, ratings, and contributor data are published daily as a separate open dataset, with download instructions linked from the repository rather than hosted in it.

## Key Claims / Findings

- Repository description: "Documentation and source code powering Twitter's Community Notes." Licensed Apache-2.0; roughly 1.9k stars and 363 forks at time of access.
- States the program's aim is to "create a better informed world" by letting people add helpful notes to potentially misleading posts, and says it is being built in the open with the intent to expand the contributor base country by country.
- Repository contents, per the README:
  - `scoring/src` – the open-source implementation of the Community Notes scoring algorithm.
  - `template-api-note-writer` – a template for the Community Notes AI Note Writer API.
  - `documentation` – Markdown source for the public Community Notes Guide site.
  - `birdwatch_paper_2022_10_27.pdf` – the original research paper.
  - Additional top-level folders (`collaborative-note-generator`, `evaluator`, `liked-by-different-perspectives`, `scoring`, `.github/workflows`) appear in the repo listing but are not described in the README itself.
- Setup instructions given: create a virtual environment under `scoring`, `pip install -r requirements.txt`, download the published data files into `scoring/src`, then run `main.py`; the README notes the code has been tested with Python 3.10.
- On the scoring/bridging algorithm itself, the README does **not** explain the mechanism (e.g., how it weights cross-ideological agreement). It only points readers to the `scoring/src` code and to the Guide's "note ranking code" page (`twitter.github.io/communitynotes/note-ranking-code/`) for the explanation. No "bridging-based ranking" description was found in the README text itself, so any claim about *how* the algorithm achieves cross-perspective agreement is not verified from this page and would need to come from the Guide or the paper directly.
- Contribution policy: pull requests are accepted for downstream analyses of scoring output, alternate scoring ideas outside the core algorithm, documentation, and open issues. API-altering changes are not accepted, and the README states that small cleanup PRs to `scoring/src` are unlikely to be merged because that code is deployed from an internal repository (i.e., this GitHub mirror is not the live production branch).
- Data access: "Notes, ratings, and contributor data" are described as publicly available and published daily. Download instructions are linked, not embedded, at `communitynotes.x.com/guide/under-the-hood/download-data/` and `x.com/i/communitynotes/download-data`.
- Further documentation linked from the repo: the public Guide (`communitynotes.x.com/guide`), the project's GitHub Pages mirror (`twitter.github.io/communitynotes`), the Note Writer API guide (`communitynotes.x.com/guide/en/api/note-writer`), and the 2022 research paper included in the repo.

## Relevance to the sprint

This is a rare case of a platform publishing both its trust/reliability scoring code and the raw rating data it runs on, making it a direct reference point for any Track 2 system that scores sources, claims, or raters rather than just aggregating opinions. For a "Track-Record Ledger" or "Provenance Study" project, the daily-published notes/ratings data give a real-world longitudinal record of rater behavior and note outcomes that could be used to validate or benchmark a reputation-scoring approach, while the open scoring code itself is a concrete example of an existing, deployed algorithm to compare against rather than design from scratch.

## Access notes / limitations

The GitHub repository page loaded successfully (no redirect, no 404); the WebFetch agent read the README/landing content and reported it in full, including repo metadata (license, stars, forks), stated contents, setup instructions, and contribution policy. The agent explicitly could not find an explanation of the scoring/bridging algorithm's mechanics within the README itself — that detail is deferred to the linked Guide page and the research paper, neither of which was fetched for this entry. Consequently, this file does not characterize *how* the bridging algorithm works beyond naming where that explanation lives; a follow-up fetch of `twitter.github.io/communitynotes/note-ranking-code/` or the PDF paper would be needed to verify and describe the mechanism itself. No content was fabricated to fill this gap.
