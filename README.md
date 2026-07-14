# SEED-MED Vault 🌍

> Second Brain agentico su **Geopolitica del Mediterraneo — prospettiva italiana** (Mediterraneo Allargato).
> Vault Obsidian generato e mantenuto con il framework spec-driven **SEED_V7** e una squadra di agenti Claude.

## Dominio e fuoco
Interesse nazionale italiano nel Mediterraneo allargato, su quattro assi:
**energia** (ENI, hub del gas), **migrazione** (rotta del Mediterraneo centrale), **sicurezza/difesa**
(Libia, fianco sud NATO, dispute ZEE) e **proiezione in Africa** (Piano Mattei).

Deep-dive prioritari:
1. Sicurezza energetica italiana e hub del gas (Algeria, Libia, EastMed)
2. Rotta migratoria del Mediterraneo centrale e politica italiana
3. Piano Mattei e proiezione italiana in Africa mediterranea

## Come aprirlo in Obsidian
1. Clona o scarica il repo.
2. Obsidian → **"Apri cartella come vault"** → seleziona la cartella del repo.
3. Wikilink `[[...]]`, "Menzioni collegate" e grafo funzionano nativamente (integrità link 1:1 verificata).

## Struttura
```
20_knowledge/   → note validate (promozione solo umana) + index.md + log.md
10_drafts/      → note in lavorazione (Curator)
30_reports/     → analisi formali "prose-as-title" (Reporter)
_critique/      → stress-test avversariali (Adversary)
00_inbox/       → area di ingestione sorgenti  [dataset grezzo NON versionato]
system/         → kernel, ops, health_check, changelog
.claude/agents/ → definizioni dei 6 agenti
wiki/ bozze/    → contenuto pre-esistente (non gestito dagli agenti)
CLAUDE.md       → kernel operativo del vault (regole, tassonomia, soglie)
```

## Ciclo di vita delle note
`draft → review → validated`. **La promozione a `validated` è sempre e solo umana** — nessun agente la imposta.

## Convenzioni di qualità
- **Soglie:** `standard` = ≥1 fonte web verificata; `deep` = ≥5 fonti + matrice gap + analisi avversariale.
- **Affidabilità:** codici Admiralty (`A1`–`F6`); mai `A1` automatico.
- **Confidenza:** etichette `[HIGH / MEDIUM / LOW confidence]` sui claim.
- **Atomicità:** nomi-nota minimi e universali; una fonte multi-tema si scinde in più note (MECE).
- **Verifica:** web-first, niente Wikipedia; claim numerici riconciliati su ≥2 percorsi (self-consistency).

## I 6 agenti
| Agente | Ruolo |
|--------|-------|
| **architect** | compila/aggiorna gli agenti dal manuale SEED_V7 |
| **curator** | distilla le sorgenti di `00_inbox/` in note atomiche |
| **adversary** | stress-test avversariale delle note (critical reading, steel-man, gap matrix) |
| **reporter** | sintetizza le note validate in analisi formali |
| **schema_builder** | mappa i macro-temi di un corpus |
| **maintainer** | health-check read-only del grafo (link, schema, coerenza) |

## Cosa NON è nel repo
- `00_inbox/dataset_libia/` — il corpus grezzo di fonti (~256 file) resta solo in locale (`.gitignore`).
- Settings locali (`.claude/settings.local.json`, `CLAUDE.local.md`) e stato UI di Obsidian.

## Stato attuale
26 note validate · 27 draft · 13 critiche · 3 report · integrità del grafo verificata (0 link fantasma/orfani, 0 Wikipedia).
Log operativo completo in [`20_knowledge/log.md`](20_knowledge/log.md); ultimo health-check in [`system/60_ops/health_check.md`](system/60_ops/health_check.md).

---
*Vault personale di ricerca. Le note riflettono fonti aperte alla data di accesso indicata; verificare sempre prima dell'uso.*
