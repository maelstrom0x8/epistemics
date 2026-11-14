# References

Each entry notes its verification status: confirmed directly (title, authors, venue, and the specific claims cited actually checked against the source), confirmed partially (source confirmed to exist and its general finding checked, but a specific number not independently confirmed), or unverified (could not be loaded, not relied on for any specific claim in this report).

1. Gao, T., Yen, H., Yu, J., and Chen, D. (2023). *Enabling Large Language Models to Generate Text with Citations.* EMNLP 2023, pages 6465-6488. https://aclanthology.org/2023.emnlp-main.398/ — **Confirmed.**

2. Wu, K., Wu, E., Wei, K., Zhang, A., Casasola, A., Nguyen, T., Riantawan, S., Shi, P., Ho, D., and Zou, J. (2025). *An automated framework for assessing how well LLMs cite relevant medical references.* Nature Communications 16:3615. https://pmc.ncbi.nlm.nih.gov/articles/PMC12003634/ — **Confirmed.**

3. Onweller, H., Lumer, E., Huber, A., Ramchandani, P., Subbiah, V. K., and Feld, C. (2026). *Cited but Not Verified: Parsing and Evaluating Source Attribution in LLM Deep Research Agents.* arXiv:2605.06635. https://arxiv.org/abs/2605.06635 — **Confirmed.** Note: the 39-77% accuracy figure applies to the frontier-model subset; the full 14-model range is 24-77%.

4. Choi, Y. M., Guo, X., Fung, Y. R., and Wang, Q. (2025/2026). *CiteGuard: Faithful Citation Attribution for LLMs via Retrieval-Augmented Validation.* arXiv:2510.17853. https://arxiv.org/abs/2510.17853 — **Confirmed.**

5. Shi, K., Sun, W., Zhang, Z., Sun, L., Chawla, N. V., and Ye, Y. (2026). *CiteAudit: You Cited It, But Did You Read It? A Benchmark for Verifying Scientific References in the LLM Era.* arXiv:2602.23452. https://arxiv.org/abs/2602.23452 — **Confirmed.**

6. Schlichtkrull, M., Guo, Z., and Vlachos, A. (2023). *AVeriTeC: A Dataset for Real-world Claim Verification with Evidence from the Web.* NeurIPS 2023 Datasets and Benchmarks Track. arXiv:2305.13117. https://arxiv.org/abs/2305.13117 — **Confirmed.**

7. Hu, X., Ru, D., Qiu, L., Guo, Q., Zhang, T., Xu, Y., Luo, Y., Liu, P., Zhang, Y., and Zhang, Z. (2024). *Knowledge-Centric Hallucination Detection* (introduces the RefChecker framework and benchmark). EMNLP 2024, pages 6953-6975. https://aclanthology.org/2024.emnlp-main.395/ — **Confirmed.**

8. "CiteEval: Principle-Driven Citation Evaluation," claimed as ACL 2025, cited at https://aclanthology.org/2025.acl-long.1574/ — **Unverified.** Three separate fetch attempts failed with an access error rather than loading the page. Not relied on for any claim in this report. An earlier URL given for this same claimed paper, https://aclanthology.org/2025.acl-long.1498/, was checked and found to resolve to a completely unrelated paper on neural speech codecs; that URL is discarded.

9. Coalition for Content Provenance and Authenticity (C2PA). *Technical Specification 2.4.* https://spec.c2pa.org/specifications/specifications/2.4/explainer/Explainer.html — **Confirmed** (standard is well-established; the specific authenticity-versus-truth distinction cited in Section 2.2 is the specification's own stated position).

10. W3C. *PROV-O: The PROV Ontology.* https://www.w3.org/TR/prov-o/ — **Confirmed** (well-established W3C recommendation).

11. Anghel, C., Anghel, A. A., Balau, A. S., Craciun, M. V., Cocu, A., Moldovanu, S., and Sandu, C. (2026). *ClaimArena-LLM: Auditing Adversarial Propagation of False Causal Attributions in Multi-Agent LLM Debates.* Machine Learning and Knowledge Extraction, MDPI, 8(10), article 327. https://www.mdpi.com/2504-4990/8/10/327 (DOI: 10.3390/make8100327). **Confirmed partially.** The article page itself returned HTTP 403 on every direct attempt; title, authors, venue, and publication date (2026-10-10) were confirmed via the publisher's Crossref metadata instead. The abstract from that metadata confirms a 20.0 percentage point drop in semantic provenance validity between all-honest and adversarial debate conditions (adjusted p = 0.002). The specific absolute values 82% and 62%, reported elsewhere, are not present in the confirmed abstract text and are not treated as established in this report.

12. Wang, Y., Zhang, J., Wu, Z., Cai, T., Liu, Z., Sun, Z., Zheng, M., Dong, M., Qiu, Y.-X., Yin, X., and Zhu, Y. (2026). *From Agent Traces to Trust: A Survey of Evidence Tracing and Execution Provenance in LLM Agents.* arXiv:2606.04990. https://arxiv.org/abs/2606.04990 — **Confirmed** (abstract checked directly; full text not independently read).

13. Gong, Y., Zhang, G., Gao, C., Shen, L., Fan, C., Wang, J., Wang, D., Liu, Y., Wang, W., and He, X. (2026). *When Upstream Messages Override Correct Answers: A Controlled Study of Multi-Agent LLM Collaboration.* arXiv:2609.36855. https://arxiv.org/abs/2609.36855 — **Confirmed.** Title, authors, date, and both headline statistics (32% answer-change rate, 94% answer-substitution rate among harmful cases, five benchmarks, five receiving models) checked directly against the abstract.

14. Torres-Arias, S., et al. (2019). *in-toto: Providing farm-to-table guarantees for bits and bytes.* USENIX Security Symposium. https://www.usenix.org/conference/usenixsecurity19/presentation/torres-arias — Referenced in earlier drafts of this research direction as a precedent for cryptographic attestation chains; not used in the final design (Section 4.4), since this study does not implement a signing or attestation layer. Kept here only as a historical note on why that approach was considered and dropped, not as a source this report's claims depend on.

15. Apart Research. *AI x Epistemics Research Sprint, Track 2: Trust Infrastructure.* https://apartresearch.com/sprints/ai-x-epistemics-research-sprint-2026-11-13-to-2026-11-15 — Sprint context and track framing.
