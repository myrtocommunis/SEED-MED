# Health Check — SEED-MED Vault

**Data:** 2026-09-08 (post-backfill Admiralty) · **Esito:** ✅ VERDE (12/12 check superati)

## Corpus
- **55 note** (29 validated + 26 draft), 22 deep
- **6 report** · **19 critiche**
- Sync GitHub: 117/117 · tree pulito

## Check (12)
| # | Check | Esito |
|---|-------|-------|
| 1 | Wikilink fantasma | ✅ 0 |
| 2 | Wikilink spezzati da newline | ✅ 0 |
| 3 | Note validate orfane | ✅ 0 |
| 4 | Campi frontmatter (8 obbligatori) | ✅ completi |
| 5 | Deep con <5 fonti | ✅ 0 |
| 6 | Fonti Wikipedia | ✅ 0 |
| 7 | Status (draft 26 / validated 29) | ✅ coerente |
| 8 | Provenance morta a demo | ✅ 0 |
| 9 | Anglicismo "carve-up" (corpus attivo) | ✅ 0 |
| 10 | Codici Admiralty per report | ✅ tutti e 6 codificati |
| 11 | A1 usato come rating (vietato) | ✅ 0 (solo la frase "mai A1") |
| 12 | Dataset grezzi gitignorati + non tracciati | ✅ |

## Backfill Admiralty (completato 2026-09-08)
Tutti e 6 i report hanno ora codici Admiralty inline per fonte, secondo la rubrica estesa
(A2 primarie IGO/gov neutre · B2 analisi/think-tank · B3 flagship press/wire/organi statali interessati/stampa
regionale · C3 outlet locale · **mai A1**). Copertura: Convergenza mediatori (A2/B2/B3/C3), Presenza cinese
(A2/B2/B3/C3), Tregua (A2/B2/B3), Italia asseconda (A2/B3), Hub gas (B2), Est-Med (B2). Hub gas ed Est-Med
espongono meno codici perché citano prevalentemente note, non fonti dirette (copertura onesta massima).

## Convenzione codici (aggiornata)
- **gov.cn → B3** (organo statale interessato); primarie IGO neutre (UNSC, UNSMIL) → A2.
- **Mai A1**: anche i documenti primari ONU si fermano ad A2.
- Rubrica completa in memoria: `admiralty-rating-rubric`.
