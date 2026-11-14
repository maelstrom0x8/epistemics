# Community Notes Public Dataset (Downloading Data)

**Org:** X (Community Notes)
**Source:** Community Notes Guide, communitynotes.x.com (institutional documentation page; content last updated 2026)
**URL:** https://communitynotes.x.com/guide/en/under-the-hood/download-data
**Accessed:** 2026-11-14
**Type:** institutional (official documentation of a primary-source, open dataset)

## Summary

The page documents X's public Community Notes dataset, downloadable at a separate page (x.com/i/communitynotes/download-data) linked from this guide. The dataset is released as five tab-separated-value (TSV) files: Notes, Ratings, Note Status History, User Enrollment, and Note Requests. These are normalized tables joinable on `noteId` (or `participantId`/`tweetId` for some tables), and a new cumulative snapshot is published daily on a best-effort basis, containing notes and ratings as of 48 hours before release. The guide page itself documents the schema (field name, type, description, and allowed response values) for each table and keeps a changelog of schema changes.

## Key Claims / Findings

- Five files released: **Notes** (all notes), **Ratings** (all ratings), **Note Status History** (status/timing metadata per note, including scoring-algorithm outputs), **User Enrollment** (per-user enrollment state), and **Note Requests** (requests for a note on a post, submittable by any X account).
- Quote: "The Community Notes data is released as five separate files."
- Tables form a **normalized data model**: note-related tables join on `noteId`; this is explicitly stated to reduce duplication.
- **Update frequency:** "A new snapshot of the Community Notes public data is released daily, on a best-effort basis," with no delivery-time guarantee; snapshots are cumulative but "only contain notes and ratings that were created as of 48 hours before the dataset release time."
- **Deletion handling:** once a note/rating is deleted, it is dropped from all future downloads, but Note Status History keeps retaining metadata (noteId, creation time, hashed author participant ID, status history) for already-scored notes even after deletion — the note's actual text is not retained.
- **File format:** each table is a TSV file with a header row (newline-separated rows, tab-separated columns, first row = column names). Note and rating data come directly from user-submitted forms "with minimal added metadata (like ids and timestamp)"; Note Status History is derived metadata including outputs of the note-scoring algorithm.
- **Access/download method:** files are obtained from the separate "Download Data" page on the Community Notes product (x.com/i/communitynotes/download-data), which the guide links to and which shows a date stamp for the most recent included data. The guide page itself does not host the files, only the schema documentation.
- **Schema detail examples:** Notes table includes `noteId`, `participantId` (permanent, handle-independent user identifier), `createdAtMillis`, `tweetId`, `classification`, multiple misleading-reason checkboxes, free-text `summary`, `isMediaNote`, and (new as of 2026-02-04) `isCollaborativeNote`. Ratings table includes helpfulness fields (`helpfulnessLevel`, various `helpful*`/`notHelpful*` checkboxes), `ratedOnTweetId`, `ratingSourceBucketed` (new 2025-09-30), and collaborative-note fields `suggestion`/`suggestionId` (new 2026, used for "collaborative notes"). Note Status History includes per-model current-status fields (core/expansion/group/multi-group submodels) and a `timestampMillisAbovePcrhThreshold` field (new as of 2026-09-18). User Enrollment documents enrollment states (`newUser`, `earnedIn`, `atRisk`, `earnedOutNoAcknowledge`, `earnedOutAcknowledge`, `apiEarnedIn`) and `modelingGroup`/`modelingPopulation`. Note Requests includes `tweetId`, `sourceLinks`, `suggestions`, and per-API-feed-size eligibility timestamps.
- **Changelog on page:** documents deprecated columns (e.g., `believable`, `harmful`, `validationDifficulty` deprecated 2022-10-27; `helpful`/`notHelpful` replaced by `helpfulnessLevel` in 2021-06-30) and added columns over time, up through 2026 additions (e.g., `suggestionId`, `timestampMillisAbovePcrhThreshold`).
- **Usage note:** the page invites feedback — "If you have questions or feedback about the Community Notes public data or would like to share your analyses of this data with us, please DM us at @CommunityNotes" — but states no explicit license terms, access restrictions, rate limits, or authentication requirements on this particular page.
- No statement on this page specifies a data license (e.g., CC BY) or any usage/redistribution restrictions; none should be assumed from what was read.

## Relevance to the sprint

This is a genuine, actively maintained, field-level-documented real-world dataset of crowdsourced fact-checking annotations (notes, helpfulness ratings, status outcomes, and the algorithmic scoring states that determine note visibility) joined to enrollment/trust states of raters. For Track 4 (Open Track) projects on trust infrastructure, it offers a directly usable ground truth for modeling how community-based fact-checking systems score, surface, or suppress claims, and for evaluating whether an AI system's judgments of note quality or helpfulness align with the existing crowd/algorithmic pipeline. The daily cumulative snapshots and documented schema changes also make it suitable for impact-over-time analyses (e.g., tracking adoption of "collaborative notes" or AI Note Writer API-sourced notes since their 2025-2026 rollout).

## Access notes / limitations

- A direct WebFetch request to the URL returned HTTP 402 Payment Required from the fetch tool.
- A `curl` request to the same URL returned HTTP 200, but the page is a client-rendered single-page app; the raw HTML body contained no article text, only a script that loads the actual content from a JSON "content model" endpoint (`/guide/en/under-the-hood/download-data.model.json`, part of the same site's rendering pipeline).
- That JSON model was fetched directly (HTTP 200) and contains the full rendered text of the guide page — section text, schema tables, and changelog — which is what this file's claims are drawn from. This is the site's own underlying content for this exact URL, not a different or cached page.
- This file does not reflect the separate product page (x.com/i/communitynotes/download-data) where the actual TSV downloads are served; that page was not fetched, so file sizes, exact current download links, and the precise current date stamp were not verified.
- No explicit license or terms-of-use text for the dataset was found on this page; its absence here should not be read as confirmation that no such terms exist elsewhere on the site.
