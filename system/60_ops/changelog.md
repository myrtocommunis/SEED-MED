# Changelog — System Operations

## [2026-07-02] v1.0.0 — Initial Seed
- Seed version: 7.0 (Spec-Driven, Compute-Adaptive, Atomic Backlinks)
- Tier: 1 (Preset OSINT) · Platform: Claude Code · LLM: Claude (Opus/Sonnet)
- Agents deployed: architect, curator, adversary, reporter
- Phase 0 SOTA discovery: added N1 (Calibrated Abstention), N2 (Self-Consistency), N3 (CO-STAR)

## [2026-07-02] v1.1.0 — schema_builder added
- New agent: schema_builder (corpus-preprocessor, model sonnet)
- Enables `fai ingest` step 2 (macro-theme mapping for large corpora)
- Reads 00_inbox/ (optionally wiki/) → empty wisdom-notes in 10_drafts/ + 20_knowledge/_schema_map.md
