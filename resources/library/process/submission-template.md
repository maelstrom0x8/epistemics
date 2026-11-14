# Official Submission Template
**Source:** Apart Research, AI x Epistemics Research Sprint
**URL:** https://docs.google.com/document/d/17b3JWki-ZkaqdmqGI5d0gof-HwlGuWU9Mc1_klNZXKs/copy?usp=sharing
**Accessed:** 2026-11-14
**Type:** primary source (template)

## Summary
The fetch attempt did not reach the template content. The URL is a Google Docs "copy" link, and requesting it returned an HTTP 302 redirect to a Google account sign-in page (`accounts.google.com/ServiceLogin`) rather than the document itself. The fetch was not continued past that redirect, since doing so would mean attempting to authenticate with a Google account, which is outside what this tool can or should do. No part of the actual template document was retrieved or viewed.

## Content (if accessible)
Not accessible. No section headings, instructional text, or body content from the template could be read, because the request never reached the document and was stopped at the Google sign-in redirect. Nothing below should be read as a description of the template's actual contents.

## Relevance to the sprint
Per the Guidelines tab (extracted separately), this document is described as the mandatory report format for every submission to the sprint, expected to cover project title, abstract, author information, standard sections (Introduction, Related Work, Methodology, Results, Discussion), a required Limitations and Dual-Use / Ethical Considerations appendix, and References, within an 8-page limit excluding references and appendices. That description comes from the Guidelines tab, not from this document, and has not been cross-checked against the template itself.

## Access notes / limitations
The fetch failed at a login wall. Specifically:

- The initial request to the `/copy?usp=sharing` URL returned a 302 redirect.
- The redirect target was `https://accounts.google.com/ServiceLogin?...&continue=https://docs.google.com/document/d/17b3JWki-ZkaqdmqGI5d0gof-HwlGuWU9Mc1_klNZXKs/copy...`, i.e. a Google sign-in page with a `continue` parameter pointing back to the document.
- This confirms the document (or at least its "copy" action) requires an authenticated Google session to access, which is consistent with how Google Docs "copy" template links typically behave for documents not fully public.
- No credentials were available or used, and no attempt was made to sign in. This is an expected and legitimate outcome for this type of link, not a tool failure to be retried.
- As a result, nothing about the template's actual structure, headings, or instructional text in this file is based on direct observation. All of the "Relevance" section above is attributed explicitly to the separately-extracted Guidelines tab, not to this document, and should not be treated as verified content of the template itself.
- If verified access to the template is needed, it would require either: (a) a logged-in Google account with access attempting the copy manually, or (b) obtaining a publicly viewable (non-copy, non-auth-gated) link to the same document from the sprint organizers.
