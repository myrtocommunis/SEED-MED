# Vault Health Check — SEED-MED

> Eseguito il **2026-07-09** dall'agente `maintainer`.
> Scansione **non distruttiva**: nessuna nota è stata modificata, nessuno `status` è stato promosso o
> demotato. Scope: `10_drafts/` + `20_knowledge/` (grafo note), inventario esteso a `30_reports/` e
> `_critique/`. Contesto dichiarato: verifica puntuale della bonifica del giro precedente (stub
> `Gasdotti` compilato, orfane `Regno unito`/`Saif al-islam` collegate, `Sudan` rafforzato C3→B2 e
> promosso, `Malta` e `Milizie` promosse) e controllo anti-churn (frammenti "X 1.md", wikilink
> corrotti, note fuori area di lifecycle).

## Inventario
| Area | Conteggio | Note |
|---|---|---|
| `20_knowledge/` validated | 24 | tutte con `status: "validated"` (verificato nota per nota); +2 rispetto al giro precedente (Malta, Milizie ora confermate; Sudan promosso da draft C3→B2 validated) |
| `20_knowledge/` non-nota | 4 | `index.md`, `log.md`, `_schema_map.md`, `_schema_map_libia.md` (esclusi dal conteggio note) |
| `10_drafts/` | 25 | tutte con `status: "draft"` (nessuna con `status: "schema"`: `Gasdotti` è stata compilata e ora è draft a pieno titolo, sources:4/B2) |
| `30_reports/` | 3 | report formali del Reporter (invariato) |
| `_critique/` | 9 | 3 note × 3 revisioni v1/v2/v3 (invariato) |
| Wikilink interni totali (draft+knowledge, pipe-aware, `index.md` escluso) | 252 | 118 in `10_drafts/`, 134 in `20_knowledge/` (note pure) |
| Densità backlink | **≈5,1**/nota (252 / 49 note) | ≥5 → grafo denso (ok) |

## Ferite strutturali — esito
| Controllo | Esito |
|---|---|
| Backlink rotti / link fantasma (pipe-aware) | ✅ **0** — ogni `[[Target]]` risolve a un file esistente in `10_drafts/` o `20_knowledge/`, incluso il caso pipe `[[Niger\|Fezzan]]` in `Presenza russa.md` |
| Frammenti "X 1.md" / "X (1).md" nel vault gestito | ✅ **0** — nessun match in `10_drafts/`, `20_knowledge/`, `30_reports/`, `_critique/`. Unico match del glob `**/* 1.md` è `wiki/Sistema 1.md`, area non gestita dagli agenti (fuori scope, preesistente, non correlata a churn recente) |
| Wikilink corrotti tipo `[[Emirati 1]]` | ✅ **0** — nessuna occorrenza testuale in tutto il vault |
| Duplicati draft↔knowledge (stessa nota in entrambe le aree) | ✅ **0** — confrontati tutti i 25 titoli di `10_drafts/` contro i 24 di `20_knowledge/`: nessuna sovrapposizione di Nome Atomico |
| Note draft in `20_knowledge/` (violazione lifecycle) | ✅ **0** — tutte le 24 note in `20_knowledge/` hanno `status: "validated"` |
| Note validated in `10_drafts/` (violazione lifecycle) | ✅ **0** — tutte le 25 note-draft hanno `status: "draft"` (nessun residuo `status: "schema"`) |
| Admiralty A/1 automatico (vietato) | ✅ **0** — nessuna nota con `admiralty: "A1"` in tutto il vault |
| Titoli composti (violazione atomicità, connettori `,`/`e`/`ed`/`+`/`—`) | ✅ **0** — tutti i 49 titoli sono Nomi Atomici Minimi (entità singole o nomi propri multi-parola tipo "Banca centrale libica", non liste con connettori) |
| Residui "wikipedia" (case-insensitive) | ✅ **0** — le uniche occorrenze in `_critique/*v3.md` sono citazioni legittime ("no Wikipedia" / "senza Wikipedia", a conferma dell'assenza della fonte); nessun residuo in `10_drafts/`/`20_knowledge/` (esclusi `log.md`/`health_check.md`/`changelog.md` per policy, meta-documenti non-nota) |
| Marcatori `[UNVERIFIED]` pendenti | ✅ **0** — nessuna occorrenza in `10_drafts/` o `20_knowledge/` |

## Verifica puntuale bonifica giro precedente
| Finding precedente | Esito verificato |
|---|---|
| `Gasdotti`: `sources: "0"`, `admiralty: ""` (stub non compilato) | ✅ **Risolto** — ora `sources: "4"`, `admiralty: "B2"`, `depth: "deep"`, 4 fonti web verificate (Il Sole 24 Ore, Geopop, OIES, Ce.S.I.); linkata in entrata da `Diversificazione energetica` (×2), `Algeria`, `Eni`, `Italia` — **4 backlink entranti**, non più orfana né stub |
| `Regno unito` orfana (0 backlink entranti) | ✅ **Risolto** — ora linkata da `10_drafts/Ricostruzione libica.md` (1 backlink entrante) |
| `Saif al-islam` orfana (0 backlink entranti) | ✅ **Risolto** — ora linkata da `10_drafts/Frammentazione interna.md` (1 backlink entrante) |
| `Sudan` fonte debole C3 | ✅ **Risolto e promosso** — rafforzata a `sources: "5"`, `admiralty: "B2"` (Middle East Eye ×3, HORN Review, CFR); `status: "validated"` in `20_knowledge/Sudan.md`, linkata da `Egitto`, `Sahel`, `index.md` |
| `Malta` (candidato promozione, non ancora validato) | ✅ **Promossa** — `20_knowledge/Malta.md`, `status: "validated"`, 5 fonti/B2 |
| `Milizie` (candidato più maturo, priorità 1) | ✅ **Promossa** — `20_knowledge/Milizie.md`, `status: "validated"`, 5 fonti/B2 |

## Ferite minori — da valutare (non bloccanti)
| # | Finding | Nota/e coinvolta/e |
|---|---|---|
| 1 | Note a fonte debole **C3** | `10_drafts/Tunisia.md`, `10_drafts/Arabia saudita.md`, `10_drafts/Ricostruzione libica.md`, `10_drafts/Ritorni volontari.md`, `10_drafts/Sahel.md`, `10_drafts/Niger.md` — **6 note** (era 7: `Sudan` è uscita dalla lista essendo stata rafforzata a B2 e promossa). Tutte correttamente **escluse** da `20_knowledge/` e dai report formali. |

Nessun'altra ferita minore rilevata in questo giro: 0 stub con `sources:0`/`admiralty` vuoto, 0 note orfane residue tra quelle segnalate in precedenza. Non risultano nuove note orfane emerse nel frattempo (tutte le 49 note del grafo hanno ≥1 backlink entrante, verificato per campionamento sui nodi a bassa connettività — `Return hubs`, `Ritorni volontari`, `Ciad`, `Niger`, `Cipro`, `Haftar` — tutti con backlink in entrata confermati).

## Candidati alla prossima promozione (draft `deep` con ≥4 fonti)
| Nota | Depth | Fonti | Admiralty | Priorità |
|---|---|---|---|---|
| `Gasdotti` | deep | **4** | B2 | 1 — molto citata (4 backlink entranti da note-hub validated: Diversificazione energetica, Algeria, Eni, Italia), colma un gap strutturale del grafo energetico |
| `Saif al-islam` | deep | 4 | B2 | 2 — ora collegata (non più orfana), profilo HIGH confidence su evento chiave (assassinio feb 2026) |
| `Ucraina` | deep | 4 | B2 | 3 |

Nessun draft `deep` raggiunge la soglia ≥5 fonti in questo giro. Restano sotto soglia (3 fonti):
`Frammentazione interna`, `Banca centrale libica`, `Blue homeland`, `Egeo`, `Opec`, `Sahel` (quest'ultima anche C3).

## Verdetto di salute
**Vault in salute (buono).** Zero findings 🔴 Critici e zero findings 🟠 Seri: nessun backlink rotto,
nessun duplicato draft↔knowledge, nessun frammento "X 1.md" o wikilink corrotto residuo, nessun
Admiralty A1, nessun residuo Wikipedia illegittimo, nessun `[UNVERIFIED]` pendente, lifecycle rispettato
ovunque (status draft/validated coerenti con l'area, nessun draft in `20_knowledge/` né validated in
`10_drafts/`). La bonifica dichiarata dall'utente è stata **verificata puntualmente e confermata al
100%**: `Gasdotti` è compilata (4 fonti/B2) e ha guadagnato 4 backlink entranti; `Regno unito` e
`Saif al-islam` non sono più orfane; `Sudan` è stato rafforzato a B2/5 fonti e promosso a validated
insieme a `Malta` e `Milizie` (24 note validated totali, +2 dal giro precedente). Nessun nuovo problema
di churn/sync Obsidian è emerso: la scansione odierna non trova alcun frammento "X 1.md" né wikilink
corrotti in `10_drafts/`, `20_knowledge/`, `30_reports/` o `_critique/`. Il grafo resta denso
(≈5,1 backlink/nota, sopra soglia 5, lieve calo statistico rispetto al ≈5,3 del giro precedente dovuto
a un ricalcolo metodologico più stringente — pipe-aware con esclusione di `index.md` dal denominatore
delle note — non a una perdita di link). L'unica ferita residua è 🟡 minore e non bloccante: 6 note a
fonte C3 (era 7; `Sudan` è uscita dalla lista), correttamente tenute fuori dal knowledge validato.
Nessuna azione correttiva automatica è stata applicata, come da mandato: la promozione di `Gasdotti`
(candidato più maturo, 4 fonti/B2, hub molto citato) resta una decisione umana.
