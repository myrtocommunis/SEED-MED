# Vault Health Check — SEED-MED

> Eseguito il **2026-07-09** dall'agente `maintainer`.
> Scansione **non distruttiva**: nessuna nota è stata modificata, nessuno `status` è stato promosso o
> demotato. Scope: `10_drafts/` + `20_knowledge/` (grafo note), inventario esteso a `30_reports/` e
> `_critique/`. Contesto dichiarato: churn recente da linter/sync Obsidian (frammenti orfani tipo
> "Emirati 1.md", wikilink corrotti `[[Emirati 1]]") — verificato puntualmente (vedi sotto).

## Inventario
| Area | Conteggio | Note |
|---|---|---|
| `20_knowledge/` validated | 22 | tutte con `status: "validated"` (verificato nota per nota) |
| `20_knowledge/` non-nota | 4 | `index.md`, `log.md`, `_schema_map.md`, `_schema_map_libia.md` (esclusi dal conteggio note) |
| `10_drafts/` | 27 | 26 con `status: "draft"`, 1 con `status: "schema"` (`Gasdotti`) |
| `30_reports/` | 3 | report formali del Reporter |
| `_critique/` | 9 | 3 note × 3 revisioni (v1/v2/v3) |
| Wikilink interni totali (draft+knowledge) | 261 | 118 in `10_drafts/`, 143 in `20_knowledge/` |
| Densità backlink | **≈5,3**/nota (261 / 49 note) | ≥5 → grafo denso (ok) |

## Ferite strutturali — esito
| Controllo | Esito |
|---|---|
| Backlink rotti / link fantasma (pipe-aware) | ✅ **0** — ogni `[[Target]]` risolve a un file esistente in `10_drafts/` o `20_knowledge/`, incluso il caso pipe `[[Niger\|Fezzan]]` in `Presenza russa.md` |
| Frammento "Emirati 1.md" / wikilink corrotti `[[Emirati 1]]` | ✅ **0** — nessun file `Emirati 1.md` presente (`glob **/*Emirati*` → solo `20_knowledge/Emirati.md`); nessuna occorrenza testuale di "Emirati 1" in tutto il vault. Il danno segnalato risulta già sanato (coerente col commit `d8a42fd fix: restore [[Emirati]] links corrupted...`) |
| Duplicati draft↔knowledge (stessa nota in entrambe le aree) | ✅ **0** — confrontati tutti i 27 titoli di `10_drafts/` contro i 22 di `20_knowledge/`: nessuna sovrapposizione di Nome Atomico |
| File anomali tipo "X 1.md" / "X (1).md" | ✅ **0** — nessun match per `** *1.md` dentro `10_drafts/` o `20_knowledge/` (match trovati solo in `wiki/`, area non gestita dagli agenti, fuori scope) |
| Note draft in `20_knowledge/` (violazione lifecycle) | ✅ **0** — tutte le 22 note in `20_knowledge/` hanno `status: "validated"` |
| Note validated in `10_drafts/` (violazione lifecycle) | ✅ **0** — tutte le 26 note-draft hanno `status: "draft"`; `Gasdotti` ha `status: "schema"` (coerente, mai stato promosso) |
| Admiralty A/1 automatico (vietato) | ✅ **0** — nessuna nota con `admiralty: "A1"` |
| Titoli composti (violazione atomicità, connettori `,`/`e`/`ed`/`+`/`—`) | ✅ **0** — tutti i 49 titoli sono Nomi Atomici Minimi (entità singole o nomi propri composti tipo "Banca centrale libica", non liste) |
| Residui "wikipedia" (case-insensitive) | ✅ **0** — le uniche occorrenze in `_critique/*v3.md` sono citazioni legittime ("no Wikipedia", a conferma dell'assenza della fonte); nessun residuo in `10_drafts/`/`20_knowledge/`. `20_knowledge/log.md` escluso per policy, comunque irrilevante (0 match) |
| Marcatori `[UNVERIFIED]` pendenti | ✅ **0** — nessuna occorrenza in `10_drafts/` o `20_knowledge/` |

## Ferite minori — da valutare (non bloccanti)
| # | Finding | Nota/e coinvolta/e |
|---|---|---|
| 1 | `sources: "0"`, `admiralty: ""` (frontmatter vuoto) | `10_drafts/Gasdotti.md` — nota-schema non ancora compilata dal curator (`status: "schema"`), pur essendo molto citata (linkata da `Diversificazione energetica`, `Algeria`, `Eni`, `Italia` in 20_knowledge). Da riempire web-first. |
| 2 | Note orfane (0 backlink in entrata, pur avendo outbound link corretti) | `10_drafts/Regno unito.md`, `10_drafts/Saif al-islam.md` — nessun'altra nota del vault le cita. Cosmetico: valutare se collegarle (es. da `Ricostruzione libica`/`Milizie`/`Elezioni`) o accettarle come note-foglia. |
| 3 | Note a fonte debole **C3** | `10_drafts/Sudan.md`, `10_drafts/Sahel.md`, `10_drafts/Niger.md`, `10_drafts/Arabia saudita.md`, `10_drafts/Ricostruzione libica.md`, `10_drafts/Ritorni volontari.md`, `10_drafts/Tunisia.md` — 7 note, correttamente **escluse** da `20_knowledge/` e dai report formali. Nessuna di queste risulta promossa (verificato). |

## Candidati alla prossima promozione (draft `deep` con ≥4 fonti)
| Nota | Depth | Fonti | Admiralty | Priorità |
|---|---|---|---|---|
| `Milizie` | deep | **5** | B2 | 1 — il più pronto (soglia deep-dive ≥5 fonti già raggiunta) |
| `Ucraina` | deep | 4 | B2 | 2 |
| `Saif al-islam` | deep | 4 | B2 | 3 (nota: orfana, vedi ferita minore #2 — collegarla prima della promozione migliorerebbe il grafo) |
| `Sudan` | deep | 4 | C3 | non raccomandato — fonte debole (C3), da rafforzare prima di considerare la promozione |

Nessun altro draft `deep` raggiunge la soglia ≥4 fonti (`Frammentazione interna`: 3, `Banca centrale libica`: 3, `Blue homeland`: 3, `Egeo`: 3, `Opec`: 3, `Sahel`: 3 — tutti sotto soglia).

## Verdetto di salute
**Vault in salute (buono).** Zero findings 🔴 Critici e zero findings 🟠 Seri: nessun backlink rotto,
nessun duplicato draft↔knowledge, nessun Admiralty A1, nessun residuo Wikipedia, nessun `[UNVERIFIED]`
pendente, lifecycle rispettato ovunque (status draft/validated coerenti con l'area). In particolare,
l'artefatto di churn segnalato dall'utente — il frammento "Emirati 1.md" e i wikilink corrotti
`[[Emirati 1]]` — **non è più presente**: la scansione odierna non trova alcuna traccia residua, in
linea con il commit di fix già applicato manualmente. Il grafo è denso (≈5,3 backlink/nota, sopra
soglia 5). Le uniche ferite residue sono 🟡 minori e non bloccanti: uno stub non compilato (`Gasdotti`),
due note orfane cosmetiche (`Regno unito`, `Saif al-islam`) e 7 note C3 correttamente tenute fuori dal
knowledge validato. Nessuna azione correttiva automatica è stata applicata, come da mandato: la
promozione di `Milizie` (candidato più maturo) e l'eventuale bonifica delle note orfane restano
decisioni umane.
