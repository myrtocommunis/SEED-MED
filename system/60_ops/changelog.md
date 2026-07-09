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

## [2026-07-09] maintainer | health check eseguito — 0 findings (0 critici)
- Scope: 10_drafts/ (27) + 20_knowledge/ (22 validated) + 30_reports/ (3) + _critique/ (9)
- 0 backlink rotti, 0 duplicati draft↔knowledge, 0 Admiralty A1, 0 residui Wikipedia, 0 [UNVERIFIED]
- Verificato specificamente l'artefatto di churn segnalato (frammento "Emirati 1.md" / wikilink
  corrotti [[Emirati 1]]): nessuna traccia residua, danno già sanato
- Densità backlink ≈5,3/nota (261 wikilink / 49 note) — grafo denso
- Ferite minori (non bloccanti): Gasdotti (sources:0, stub non compilato), 2 note orfane
  (Regno unito, Saif al-islam), 7 note C3 correttamente escluse da validated
- Candidato più maturo alla promozione: Milizie (deep, 5 fonti, B2)
- Verdetto: Vault in salute (buono). Report in system/60_ops/health_check.md

## [2026-07-09] maintainer | health check eseguito — 0 findings (0 critici)
- Scope: 10_drafts/ (25) + 20_knowledge/ (24 validated) + 30_reports/ (3) + _critique/ (9)
- Verifica puntuale bonifica giro precedente: Gasdotti compilata (4 fonti/B2, ora 4 backlink
  entranti, non più stub né orfana); Regno unito e Saif al-islam collegate (non più orfane);
  Sudan rafforzato a 5 fonti/B2 e promosso; Malta e Milizie promosse — tutto confermato al 100%
- 0 backlink rotti, 0 duplicati draft↔knowledge, 0 frammenti "X 1.md"/wikilink corrotti residui,
  0 Admiralty A1, 0 residui Wikipedia, 0 [UNVERIFIED], 0 violazioni lifecycle
- Densità backlink ≈5,1/nota (252 wikilink pipe-aware / 49 note) — grafo denso
- Ferite minori (non bloccanti): 6 note C3 (era 7, Sudan uscito dalla lista dopo rafforzamento)
- Candidato più maturo alla promozione: Gasdotti (deep, 4 fonti, B2, hub molto citato)
- Verdetto: Vault in salute (buono). Report in system/60_ops/health_check.md
