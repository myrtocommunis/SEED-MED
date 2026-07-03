# Schema Map — Dataset Libia (corpus news 2025-2026)

> Generato da `schema_builder` il 2026-07-02. Fonte: `00_inbox/dataset_libia/` (21 MD leggibili
> + CSV QIC; 177 PDF NON ancora estratti). Nessuna web search (mappatura strutturale).

## Macro-temi rilevati (batch scan: 21 headline + CSV QIC codificato)

| Wisdom-note atomica | Segnale (headline ricorrenti) | Stato |
|---------------------|-------------------------------|-------|
| **`Bilancio libico`** | Cluster dominante: primo bilancio unificato in oltre un decennio (Reuters, US DOS, Boulos) | **draft** ✓ pilota |
| **`Mediazione statunitense`** | Convergenza USA-Italia-Turchia (Istanbul ago 2025), Boulos | **draft** ✓ pilota |
| **`Presenza russa`** | Base Al-Khadim (armi verso Sahel), riapertura ambasciata Tripoli | **draft** ✓ pilota |
| **`Petrolio`** | Asta dopo 18 anni; deal Total/Conoco 25 anni (>20 mld $); ritorno Eni | **draft** ✓ pilota |
| **`Haftar`** | Clan Haftar; deal Pakistan-LNA 16 JF-17 (Cina) | **draft** ✓ pilota |
| **`Cina`** | Penetrazione industrial-militare est via Pakistan-LNA | **draft** ✓ pilota |
| `Migrazione` *(esiste)* | EU return hubs, Return Regulation, Economist | riuso |
| `Turchia` *(esiste)* | Mandato truppe esteso, capo di SM libico morto in Turchia | riuso |
| `Libia` *(esiste)* | Nodo-arena; frammentazione politica | riuso |
| `Eni` *(esiste)* | Petrolio/energia (via PDF da estrarre) | riuso |

## Metodo sorgente (dalla Sezione 1 - QIC)
Il CSV `1.1_...QIC_PESTL_SM_v12.csv` (80 news) è codificato con: Eventi · Tema · **Affidabilità
fonte (A-F)** · **Attendibilità info (1-6)** [scala Admiralty] · Nota QIC · Valutazioni ·
Previsioni · Fattori · **Categoria PESTLE-SM**. Riusabile come ground-truth per l'Admiralty delle note.

## Regole di collocazione / prossimi passi
- Splitting MECE già applicato ai temi ibridi (es. "budget **e** Flintlock" → `Bilancio libico` + `Mediazione statunitense`).
- I 177 PDF restano da estrarre: il `curator` li processerà in un secondo passo (nuovo Pre-Flight Gate).
- Naming atomico minimo; wikilink solo a note esistenti.

## Estensione pilota — Migrazione & stabilizzazione regionale (12 PDF, 2026-07-02)
| Wisdom-note atomica | Segnale | Stato |
|---------------------|---------|-------|
| `Migrazione` | Patto UE (12/6/26), Frontex -40%, svolta policy | **draft** ✓ |
| `Rotta del mediterraneo centrale` | ~1/3 ingressi UE; bengalesi 31% verso Italia; ~1.300 morti | **draft** ✓ |
| `Return hubs` | Return Regulation UE (voto 17/6/26), modello Italia-Albania | **draft** ✓ |
| `Frontex` | -40% attraversamenti; rotte a confronto | **draft** ✓ |
| `Ritorni volontari` | Programmi OIM/UE (somali, sudanesi) | **draft** ✓ |
| `Egitto` | Ritiro forze straniere; meccanismo Algeria-Egitto-Tunisia | **draft** ✓ |
| `Ricostruzione libica` | 200→570 mld $; DRF est (Belkacem Haftar) | **draft** ✓ |

## Estensione pilota — Attori esterni (12 PDF, 2026-07-02)
| Wisdom-note atomica | Segnale | Stato |
|---------------------|---------|-------|
| `Pakistan` | Deal armi >4 mld $ a LNA (16 JF-17), viola embargo | **draft** ✓ |
| `Cina` (arricchita) | Ritorno FOCAC 2024; diversificazione energetica; via Pakistan | **draft** ✓ |
| `Francia` | Inviato Soler; MoU Business France; concorrente dell'Italia | **draft** ✓ |
| `Ucraina` | Guerra coperta vs Russia; attacco tanker Arctic Metagaz; forze a Misurata | **draft** ✓ |
| `Presenza russa` (arricchita) | Africa Corps; ritiro da Sirte→Fezzan; consolato Bengasi | **draft** ✓ |
| `Embargo armi` | UNSC Ris. 2819 (14/4/26); road map Tetteh; 5+5 | **draft** ✓ |

## Estensione pilota — Frammentazione interna & elezioni (12 PDF, 2026-07-02)
| Wisdom-note atomica | Segnale | Stato |
|---------------------|---------|-------|
| `Frammentazione interna` | 3 autorità ovest (GNU/PC/HCS); dinaro -14,7%; vuoto di potere | **draft** ✓ |
| `Elezioni` | Road map 18/6 (voto entro 17/2/2027) vs piano Boulos senza voto | **draft** ✓ |
| `Milizie` | Scontri Zawiya; Rada vs Dbeibah; mediazione MIT turca | **draft** ✓ |
| `Dbeibah` | PM GNU conteso; base Misurata; assenza/proteste | **draft** ✓ |

## Estensione pilota — Golfo (9 PDF, 2026-07-03)
> Nota: asse sottorappresentato nei titoli; contenuto recuperato via scan full-corpus dei termini del Golfo.

| Wisdom-note atomica | Segnale | Stato |
|---------------------|---------|-------|
| `Emirati` | Sponsor di Haftar; canale armi UAE→RSF sudanese; rivalità con Riyadh | **draft** ✓ |
| `Qatar` | Allineato al GNU; co-investimento con l'Italia (Misurata FZ 2,7 mld $) | **draft** ✓ |
| `Arabia saudita` | Contende Haftar agli Emirati (via Pakistan); patto difesa con Islamabad | **draft** ✓ |

## Aggiunta — OPEC & dimensione energetica UAE (5 PDF, 2026-07-03)
| Wisdom-note atomica | Segnale | Stato |
|---------------------|---------|-------|
| `Opec` | Uscita UAE dall'OPEC (apr 2026); Libia +1 mln bpd; quote e prezzi | **draft** ✓ |
| `Emirati` (arricchita) | Aggiunta dimensione energetica: exit OPEC, frizioni con Riyadh | **draft** ✓ |

## Estensione — Finanza & istituzioni economiche (6 PDF, 2026-07-03)
| Wisdom-note atomica | Segnale | Stato |
|---------------------|---------|-------|
| `Libyan investment authority` | Fondo sovrano ~68 mld $ congelato; Kirkoswald; causa Al-Kharafi | **draft** ✓ |
| `Banca centrale libica` | Naji Issa; bilancio 190 mld dinari; ispezione K2; banca parallela est | **draft** ✓ |
| `Bilancio libico` (arricchito) | Firma 11/4 (190 mld dinari, ~30 mld $); legittima Haftar | **draft** ✓ |
> Lead (Italia): raffineria Fezzan — impresa italiana Progetti Europa & Global subentra a Petrofac (da estrarre in futuro).

## Estensione — Spillover Sahel/Sudan (11 PDF, 2026-07-03)
| Wisdom-note atomica | Segnale | Stato |
|---------------------|---------|-------|
| `Sudan` | Haftar arma l'RSF (addestrato in Libia); Egitto colpisce convogli; triangolo di confine | **draft** ✓ |
| `Ciad` | CCMSR nel Fezzan poi espulso; forza congiunta di confine; dimensione Toubou | **draft** ✓ |
| `Sahel` | Fezzan crocevia traffici; corridoio Niger-Libia; uranio russo Niamey-Bengasi | **draft** ✓ |

## Aggiunta — Niger-Libia (3 PDF, 2026-07-03)
| Wisdom-note atomica | Segnale | Stato |
|---------------------|---------|-------|
| `Niger` | Porta d'ingresso migratoria; deportazioni da Barak al-Shatt; uranio Orano→Bengasi | **draft** ✓ |

## Riequilibrio corpus — Egeo/EastMed/Turchia (web-first, 2026-07-03)
> Fonte: verifica web del curator (nessun dataset locale su questi temi).
| Wisdom-note atomica | Segnale | Stato |
|---------------------|---------|-------|
| `Egeo` | Dispute isole/ZEE Grecia-Turchia; "metà dell'Egeo"; mappa UNESCO | **draft** ✓ |
| `EastMed` | Gasdotto in stallo; EMGF (Italia dentro, Turchia esclusa) | **draft** ✓ |
| `Cipro` (arricchita) | 13 blocchi; Eni primo operatore; Cronos/Aphrodite; frizione turca | **draft** ✓ |
| `Grecia` (arricchita) | UNCLOS art.121; accordi ZEE con Italia/Egitto | **draft** ✓ |
| `Turchia` (arricchita) | Elevata a scala di bacino: Egeo+Cipro+Libia | **draft** ✓ |
| `Dispute zee` (arricchita) | 3 fronti (Egeo/Cipro/Libia) + blocco EMGF | **draft** ✓ |
