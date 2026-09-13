# Health Check — SEED-MED Vault

**Data:** 2026-09-14 (post-sostituzione "hedging" + fix concordanze/target) · **Esito:** ✅ VERDE (15/15)

## Corpus
- **55 note** (29 validated + 26 draft), 22 deep
- **7 report** (tutti datati 2026-09-13, 7-7.5/10 post-adversary) · **21 critiche**
- Sync GitHub: **allineato · tree pulito**

## Check (15)
| # | Check | Esito |
|---|-------|-------|
| 1 | Wikilink fantasma | ✅ 0 |
| 2 | Wikilink spezzati da newline | ✅ 0 |
| 3 | Note validate orfane | ✅ 0 |
| 4 | Frontmatter (8 campi) | ✅ completi |
| 5 | Deep con <5 fonti | ✅ 0 |
| 6 | Fonti Wikipedia | ✅ 0 |
| 7 | Status (draft 26 / validated 29) | ✅ coerente |
| 8 | Provenance morta a demo | ✅ 0 |
| 9 | Anglicismo "carve-up" (report/note) | ✅ 0 |
| 10 | Codici Admiralty per report | ✅ tutti e 7 |
| 11 | A1 come rating (report+note) | ✅ 0 (solo la frase "mai A1") |
| 12 | Terminologia ("hedging"→"copertura strategica"; "modale"→"prevalente") | ✅ 0 residui attivi |
| 13 | Concordanza gender "copertura strategica" (articoli/aggettivi) | ✅ 0 errori |
| 14 | Target critiche → 30_reports/ esistenti | ✅ (1 target descrittivo per critica multi-report, non un path) |
| 15 | Dataset gitignorati/non-tracciati + sync origin | ✅ allineato |

## Terminologia (stato)
- **"hedging" → "copertura strategica"** ovunque nel vault attivo (report, critiche, nota Turchia, index);
  gestite concordanze M→F (articoli elisi, aggettivi condizionata/assunta/trattata/italiana/turca) e il verbo
  "hedgia"→"si cautela". `log.md` lasciato come archivio (5 occorrenze storiche).
- **"modale" → "prevalente"**; **"pena della prova"** → "Perché è difficile credere a un esito pieno".
- Convenzione codici: **mai A1**; gov.cn/organi statali interessati → B3; primarie IGO neutre → A2.

## Manutenzione di questo giro
- Fix concordanza nel report Turchia: "L'copertura strategica turco" → "La copertura strategica turca".
- Ripuntati 2 `target:` di critiche a nomi-file aggiornati (pace v1, Cina) dopo rinomine precedenti.
