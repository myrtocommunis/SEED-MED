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

## [2026-07-08] v1.3.0 — maintainer added
- New agent: maintainer (quality-gate, model sonnet). Trigger: "health check", "audit", "status", "maintainer"
- Ruolo: QA non distruttiva del vault — LEGGE tutto, NON modifica note, NON promuove/demota
- Controlli: backlink rotti (pipe-aware), orfani, duplicati draft↔knowledge, igiene frontmatter
  (sources 0 / admiralty vuoto / tags vuoto), violazioni regole (Admiralty A1 automatico, titoli
  composti, residui Wikipedia), rischio-hallucination ([UNVERIFIED] pendenti, note C3), candidati
  alla promozione (draft deep ≥4 fonti)
- Output: sovrascrive SEMPRE system/60_ops/health_check.md (mai copie datate)
- Protocolli iniettati (Sez. 6): Anti-Hallucination, Source Obligation, Chain-of-Verification, N1 Astensione Calibrata
- Deploy: .claude/agents/maintainer.md + mirror system/40_agents/ e system/30_prompts/compiled/ + spec in system/20_specs/agents/
- Formalizza l'health-check inline eseguito manualmente il 2026-07-08
