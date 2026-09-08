# Health Check — SEED-MED Vault

**Data:** 2026-09-08 · **Esito:** ✅ VERDE (tutti i check strutturali superati)

## Corpus
- **55 note** (29 validated + 26 draft), 22 deep
- **6 report** · **19 critiche**
- Sync GitHub: 115/115 · tree pulito

## Check (11)
| # | Check | Esito |
|---|-------|-------|
| 1 | Wikilink fantasma | ✅ 0 |
| 2 | Wikilink spezzati da newline | ✅ 0 |
| 3 | Note validate orfane | ✅ 0 |
| 4 | Campi frontmatter mancanti (8 obbligatori) | ✅ nessuno |
| 5 | Note deep con <5 fonti | ✅ nessuno |
| 6 | Fonti Wikipedia | ✅ 0 |
| 7 | Status (draft 26 / validated 29) | ✅ coerente |
| 8 | Provenance morta a demo cancellati | ✅ 0 |
| 9 | Anglicismo "carve-up" (corpus attivo) | ✅ 0 (solo log.md, archivio) |
| 10 | Codici Admiralty per report | ⚠️ vedi nota |
| 11 | Dataset grezzi gitignorati e non tracciati | ✅ |

## Nota sul check #10 (non è un difetto)
Solo il report **"Presenza cinese in Libia"** porta codici Admiralty inline per paragrafo (5 codici distinti:
A1/A2/B2/B3/C3): era la richiesta esplicita per quel report. Gli altri 5 report precedono quella convenzione e
usano il sistema `[verificato: <nota>]` / `[confidence]` senza codici inline — **by design**, non un errore.
Backfill dei codici sugli altri 5 disponibile su richiesta.

## Ultime operazioni
- Report "Presenza cinese in Libia" rev.2: adversary 6/10 → corroborazione web (CBL primaria, ChinaMed diretto,
  UNSC 2819/2026) → difetti alti risolti nella sostanza, voto stimato 8/10.
- Nota `Cina` aggiornata a monte con le stesse fonti primarie (7→12 fonti); codici ricalibrati (gov.cn A2→B3,
  Decode39 A2→B2); JF-17 marcato inferenza; `status: validated` invariato.
