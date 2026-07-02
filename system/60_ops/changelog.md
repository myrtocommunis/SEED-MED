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

## [2026-07-02] v1.2.0 — Domain specialization: Mediterranean geopolitics (Italy-centric)
- Domain: "OSINT & Geopolitics" → "Geopolitica del Mediterraneo — prospettiva italiana"
- Vault renamed: SEED-OSINT → SEED-MED
- Tag taxonomy specialized (domain/region/actor), Italy-centric key_terms + 3 deep-dive topics
- Recalibrated identity + examples of curator/adversary/reporter/schema_builder
- architect.md unchanged (domain-agnostic)
