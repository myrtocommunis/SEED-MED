# Health Check — SEED-MED Vault

> Esecuzione: **2026-07-10 (re-check)** · maintainer (inline) · audit read-only, non distruttivo.

## 🟢 Stato generale: SANO

| Check | Esito |
|-------|-------|
| Note totali | 26 validated + 27 draft = 53 |
| Wikilink 1:1 (link fantasma) | ✅ **zero** |
| Note orfane | ✅ **zero** |
| Schema frontmatter (8 campi) | ✅ **completo** |
| No-Wikipedia | ✅ **zero** |
| Draft marcati `validated` (viol. §3) | ✅ **nessuno** |
| Regressioni dai 9 commit recenti | ✅ **nessuna** (5 note aggiornate + Pakistan rev.2 integri) |

## 🟡 Finding persistente: 20 note `deep` sotto le 5 fonti
Invariato dall'ultimo giro. Quality gate §5 = ≥5 fonti per `deep`.
- **Validate:** Egitto(4) · Haftar(3) · Libia(3) · Eni(3) · Algeria(4) · Cipro(4) · Dispute zee(3) · Bilancio libico(3) · Migrazione(3) · Rotta del mediterraneo centrale(4)
- **Draft:** Egeo(3) · Gasdotti(4) · Blue homeland(3) · Ucraina(4) · Saif al-islam(4) · Sahel(3) · Libyan investment authority(2) · Opec(3) · Banca centrale libica(3) · Frammentazione interna(3)

→ Raccomandazione invariata: irrobustire i 4 pilastri (`Libia`, `Eni`, `Migrazione`, `Haftar`) o declassare i nodi di supporto a `standard`.

## 🔵 Nuovo finding (basso): scarto `sources` dichiarate vs voci Fonti
12 note dichiarano più fonti di quante ne elenchino come link in `## Fonti` (es. Turchia 6 vs 3, Mediazione statunitense 6 vs 2). **Nella maggior parte è convenzione, non difetto**: il conteggio `sources` include le fonti-dataset di `provenance` (non ripubblicate come weblink). Eccezione già sanata: `Pakistan` (Nikkei citata ma fuori Fonti → corretta in rev.2).
→ Azione suggerita (facoltativa, cosmetica): quando si promuove/rafforza una nota, allineare `## Fonti` all'elenco completo, o annotare che i weblink sono un sottoinsieme del `provenance`.

## Delta dall'ultimo run (2026-07-09/10)
- +4 note migrazione (Patto/Regolamento/Decreto flussi/TUI), +2 promozioni (Return hubs, Regolamento rimpatri).
- +5 note aggiornate (Elezioni, Mediazione statunitense, Italia, Pakistan, Milizie) via ingest 7-12 lug.
- 3 stress-test avversariali + correzioni (Return hubs, Regolamento rimpatri, Pakistan).
- 3 file demo eliminati da 00_inbox.
- Nessun intervento urgente.
