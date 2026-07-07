# Vault Health Check — SEED-MED

> Eseguito il 2026-07-08 (funzione `maintainer` inline; agente non installato).
> Non distruttivo salvo la consolidazione del duplicato `Elezioni` (autorizzata come fix della promozione).

## Inventario
| Area | Conteggio |
|---|---|
| `20_knowledge/` validated | 18 |
| `10_drafts/` | 29 |
| `30_reports/` | 3 |
| `_critique/` | 9 |
| Backlink interni totali | ~291 (media **5,9**/nota) |

## ✅ Ferite strutturali — esito
| Controllo | Esito |
|---|---|
| Backlink rotti (link fantasma) | ✅ **0** |
| Titoli composti (violazione atomicità) | ✅ **0** |
| Admiralty A/1 automatico (vietato) | ✅ **0** |
| Residui Wikipedia | ✅ **0** |
| Marcatori `[UNVERIFIED]` pendenti | ✅ **0** |
| Duplicati draft↔knowledge | ⚠️→✅ **1 trovato e risolto** (`Elezioni`) |

### 🔧 Fix applicato
- **`Elezioni` era duplicata**: `draft` a 5 fonti (rafforzata) + `validated` a 3 fonti (stale). La promozione
  aveva validato la copia vecchia. **Consolidata** sulla versione a 5 fonti (canonica, su cui poggiano i report);
  rimosso il draft stale.

## ⚠️ Ferite minori — da valutare (non bloccanti)
| # | Finding | Nota |
|---|---|---|
| 1 | **`Gasdotti`** ha `sources: 0` | Stub-schema strutturato ma non compilato, benché molto linkato (TransMed/Greenstream/TAP). Da riempire web-first. |
| 2 | Note orfane: **`Regno unito`**, **`Saif al-islam`** | Nessun backlink in entrata; valutare se collegarle (es. da `Ricostruzione libica`/`Milizie`) o accettarle come foglie. |
| 3 | 7 note a fonte debole **C3** (`Sudan`, `Sahel`, `Niger`, `Arabia saudita`, `Ricostruzione libica`, `Ritorni volontari`, `Tunisia`) | Correttamente **escluse** da validated/report. Rafforzabili con fonti indipendenti se servono in futuro. |

## 💡 Candidati alla prossima promozione (draft maturi)
- `Milizie` (deep, 5 fonti, B2) — il più pronto
- `Ucraina` (deep, 4 fonti, B2)

## Verdetto di salute
**Vault in salute (buono).** Grafo denso e coerente (0 link rotti, densità 5,9), fonti pulite (0 Wikipedia,
0 A1), lifecycle rispettato (promozione umana). L'unico difetto reale — il duplicato `Elezioni` — è stato
sanato. Le ferite residue sono cosmetiche/di completezza, non di integrità.
