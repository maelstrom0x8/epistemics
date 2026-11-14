# Certificate Transparency

**Authors:** B. Laurie, A. Langley, E. Kasper (Google)
**Source:** RFC 6962, IETF (2013)
**URL:** https://datatracker.ietf.org/doc/html/rfc6962
**Accessed:** 2026-11-14
**Type:** primary source / technical standard

## Summary

RFC 6962 specifies Certificate Transparency (CT), an experimental IETF protocol (not Standards Track) for maintaining publicly auditable, append-only logs of all issued TLS certificates. The core idea is that a log server accepts submitted certificates (or "precertificates" submitted before issuance), incorporates them into a single Merkle Hash Tree, and issues a Signed Certificate Timestamp (SCT) as a promise to include the entry within a bounded time (the Maximum Merge Delay). The log does not itself prevent certificate misissuance; it makes misissuance detectable by anyone who monitors or audits the log. The protocol was later superseded by RFC 9162 (Certificate Transparency Version 2.0).

## Key Claims / Findings

- **Purpose:** addresses the problem of misissued (fraudulently or mistakenly issued) TLS certificates by creating logs that are "publicly auditable, append-only, untrusted logs of all issued certificates" (abstract).
- **What the log does not do:** "The logs do not themselves prevent misissue" — detection, not prevention, is the mechanism; the burden of acting on detected misissuance falls on domain owners, browsers, or other interested parties.
- **Merkle tree structure:** each log is a single binary Merkle Hash Tree built with SHA-256, with leaf and interior node hashes distinguished by different prefix bytes (domain separation) to prevent certain forgery attacks on the tree structure.
- **Append-only guarantee:** enforced cryptographically via the Merkle tree rather than by institutional trust. The RFC states this property "is technically achieved using Merkle Trees."
- **Signed Certificate Timestamp (SCT):** issued by a log on accepting a submission; defined as "the log's promise to incorporate the certificate in the Merkle Tree within a fixed amount of time" (the Maximum Merge Delay). It contains the log ID, a timestamp, extensions, and a signature.
- **Signed Tree Head (STH):** the log periodically signs its current tree root hash together with the tree size and a timestamp, giving a verifiable, dated snapshot of the whole log state.
- **Delivery mechanisms for SCTs:** an X.509 certificate extension, a TLS extension, or OCSP stapling; compliant TLS clients are expected to support all three delivery paths.
- **Merkle audit proofs:** demonstrate that a specific certificate (leaf) is actually included in the tree corresponding to a given STH — used to check that an SCT's promise was honored.
- **Merkle consistency proofs:** demonstrate that a newer STH is an extension of an older STH without alteration of previously logged entries. The RFC states "Merkle consistency proofs prove the append-only property of the tree" — this is the specific mechanism that detects tampering or rewriting of log history.
- **Monitors vs. auditors (two distinct trust-verification roles):** monitors fetch and verify STHs and new entries over time, watching for certificates of interest (e.g., a domain owner watching for certificates issued for their own domain); auditors check partial information they hold (an SCT, an STH) for consistency against other information, using consistency and audit proofs, without needing to download the whole log.
- **Gossip (noted but not specified in this RFC):** clients are expected to exchange STHs with each other so that a log cannot show different, inconsistent views to different parties undetected; RFC 6962 defers the actual gossip protocol to a separate document.
- **Attack model defended against:** a CA (or a log, or an attacker who compromises either) issuing or presenting a fraudulent certificate without detection. CT does not stop issuance but removes the ability to do so silently, since any split-view or unlogged certificate becomes visible to monitors/auditors or produces a detectable Merkle-proof failure.

## Relevance to the sprint

RFC 6962 is a directly applicable prior-art model for the "Tamper-Evident Action Recorder" project: it is a working, deployed instance of a publicly auditable, append-only log secured by Merkle trees rather than by trusting the log operator. The split between SCT (a promise about a single entry), STH (a signed snapshot of the whole log), audit proofs (single-entry inclusion), and consistency proofs (whole-log non-tampering between snapshots) maps onto the distinct guarantees an AI-agent-action log would need: proof that a specific action was recorded, and proof that the log's history has not been rewritten since. The monitor/auditor role split is also relevant to designing who verifies an agent-action log and how much data they need to download to do it.

## Access notes / limitations

Full text was retrieved via the WebFetch tool, which fetches the page and summarizes/extracts content through an intermediate model rather than returning raw HTML for direct line-by-line reading. The summary above is based on that extraction, including the quoted short phrases, which were reported as drawn directly from the document text. The quoted phrases were not independently re-verified against the raw RFC text by a second, separate fetch. No other access problems occurred (no 404, no paywall); the document is public.
