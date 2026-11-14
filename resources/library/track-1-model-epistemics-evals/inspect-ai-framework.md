# Inspect

**Maintainer/Org:** UK AI Security Institute (UK AISI; formerly part of UK Government BEIS / UK AI Safety Institute), GitHub organization `UKGovernmentBEIS`
**Source:** GitHub repository (code hosting platform, ongoing project; repository created and actively maintained as of access date)
**URL:** https://github.com/UKGovernmentBEIS/inspect_ai
**Accessed:** 2026-11-14
**Type:** primary source / open-source tool

## Summary

Inspect is an open-source Python framework for building and running large language model evaluations, maintained by the UK AI Security Institute. The GitHub repository describes it as providing "many built-in components, including facilities for prompt engineering, tool usage, multi-turn dialog, and model graded evaluations," with support for third-party Python packages that extend it with new elicitation and scoring techniques. The project ships with a catalog of more than 200 pre-built evaluations and maintains separate documentation at inspect.aisi.org.uk. The repository is substantial and active: at the time of access it showed 3.2k stars, 931 forks, 382 open issues, and 8,381 commits on the `main` branch.

## Key Claims / Findings

- Self-description from the repo: "Inspect: A framework for large language model evaluations."
- Core built-in facilities named in the README: prompt engineering, tool usage, multi-turn dialog, and model-graded evaluations. The README does not spell out further mechanics (e.g., specific model providers, sandboxing, or scorer types) on the GitHub page itself; those live in the separate documentation site.
- The framework is extensible: other Python packages can add "new elicitation and scoring techniques," indicating a plugin-style architecture rather than a closed system.
- It bundles "a collection of over 200 pre-built evaluations ready to run on any model," cataloged at inspect.aisi.org.uk/evals/. The README does not name specific example evals by title; it only points to this external catalog page, which was not fetched for this entry.
- The repository includes a TypeScript/React web UI (`src/inspect_ai/_view/ts-mono/`), maintained as a git submodule, suggesting Inspect has a results-viewing interface in addition to the Python evaluation runner.
- Development setup (for contributors) uses `uv` (version 0.13.4+) and `uv sync --locked` to install the project in editable mode; standard contributor tooling includes `make check` (lint/format/type-check) and `make test`.
- The repository explicitly targets AI coding agents as a documentation audience: it exposes machine-readable docs indexes (`llms.txt`, `llms-guide.txt`, `llms-full.txt`) and lets any docs page be fetched as Markdown by appending `.md` to its URL.
- Licensed under the MIT license (per the repository's LICENSE file).
- No task/eval code sample (e.g., a `@task` definition, solver, or scorer) appears on the GitHub repository page or in the README itself; the README is oriented toward contributor/development setup rather than a usage quickstart. The structural details of "how a task/eval is defined in Inspect" were not found in this source and would need to be confirmed from the documentation site (inspect.aisi.org.uk) rather than assumed here.

## Relevance to the sprint

Inspect is a maintained, actively developed evaluation framework built specifically for the kind of structured LLM evals the "epistemic virtue eval suite" project describes, built by an institutional AI safety body (UK AISI) rather than a hobby project, which matters for credibility and longevity. Its stated support for multi-turn dialog, tool usage, and model-graded evaluation, plus an extensible scoring mechanism, maps onto the practical needs of a suite testing things like calibration, honesty under pressure, or reasoning transparency across conversational turns. Because this entry is based only on the GitHub landing page, a team building the actual eval suite will still need to consult inspect.aisi.org.uk directly for the task/solver/scorer API and a working code example before implementation.

## Access notes / limitations

Fetched two things directly: (1) the rendered GitHub repository page at https://github.com/UKGovernmentBEIS/inspect_ai via WebFetch, which returned repo metadata, the rendered README content, file listing, and stats; (2) the raw README source at https://raw.githubusercontent.com/UKGovernmentBEIS/inspect_ai/main/README.md via WebFetch, which returned a summarized (not verbatim) version of the same file due to tool-side quoting limits, but corroborated the rendered page's content and confirmed no code example is present in the README.

Both fetches succeeded (no 404 or access failure). Neither fetch retrieved the external documentation site (inspect.aisi.org.uk) or the evals catalog page, so claims about the detailed task/solver/scorer structure, specific example eval names, and supported model providers are not covered by this entry and are marked above as not found rather than inferred. All content in this file is drawn only from the GitHub repository page and README; nothing has been fabricated or filled in from general knowledge of the tool.
