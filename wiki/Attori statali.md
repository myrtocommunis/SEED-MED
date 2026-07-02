---
title: Attori statali
tags:
- OSINT
- processed
- attori-statali
date: '2026-05-15'
status: draft
depth: standard
sources: '1'
tipo: concetto
---

# Attori statali

## 🎯 Sintesi Strategica

Gli [[Attori statali]] rappresentano una categoria fondamentale nella valutazione della minaccia informativa, caratterizzati da capacità, intenti e opportunità variabili. La minaccia complessiva può essere quantificata dalla formula: **Threat = Capacità × Intent × Opportunità**. In contesti come quello italiano, si osserva una diversificazione delle strategie: la Russia, pur avendo subito un declino del 70% nel *reach* diretto post-2022, continua a operare tramite [[Proxy]] con circa il 30% dei livelli pre-ban. La Cina, invece, adotta un profilo meno aggressivo, focalizzato sulla difesa e sul *targeting* delle élite, piuttosto che sulla destabilizzazione di massa.

## 📚 Contesto e Definizioni

Gli [[Attori statali]] sono entità governative o a esse direttamente riconducibili che operano nello spazio informativo per perseguire obiettivi geopolitici, economici o di [[Sicurezza nazionale]]. La loro azione può manifestarsi attraverso campagne di [[Disinformazione]], influenza, spionaggio o destabilizzazione. Un'analisi approfondita rivela che non tutti gli attori statali impiegano tattiche identiche; ad esempio, la differenza tra le strategie di Russia e Cina è emblematica. I dati per la valutazione di tali attori provengono da relazioni pubbliche di enti di intelligence (es. Copasir/DIS), stime di *reach* e valutazioni comparative.

## 📊 Dati, Tecnologie e Metriche

La valutazione degli [[Attori statali]] si basa su metriche quantitative che ne delineano capacità e impatto.

### Russia (Contesto Italia)

| Indicatore | Pre-2022 | Post-2022 |
|---|---|---|
| Budget operativo | 5-10M EUR/anno | N/D |
| Staff Italia | ~50 persone | N/D |
| Reach diretto (Sputnik/RT) | 100-300k unique/mese (Sputnik) / 50-150k unique/mese (RT) | -70% |
| Reach proxy | N/D | ~30% pre-ban |
| Bot network | N/D | 100-500 stimati |
| Social impressions | 500k-1M/mese combiNATO | N/D |
| Tattiche | Destabilizzazione aperta, bot massivi, narrazioni offensive | Siti terzi non affiliati, canali Telegram non dichiarati |

### Minaccia Comparata (Attori Statali)

| Attore | Capacità | Intent | Opportunità | Threat |
|---|---|---|---|---|
| Russia | Alta→Media | Alto | Media | MEDIO |
| Cina | Media | Basso | Bassa | BASSO |

*Nota: La tabella include anche attori non-statali per un confronto contestuale, ma il focus è sugli attori statali.*

## 🔍 Analisi Operativa ed Applicazioni OSINT

L'analisi delle operazioni degli [[Attori statali]] rivela strategie distinte e offre spunti cruciali per l'[[Osint]].

### 1. La Differenza Russia/Cina

La Russia predilige la destabilizzazione aperta, utilizzando [[Proxy]], *bot* massivi e narrazioni offensive per influenzare le masse. La Cina, al contrario, adotta una strategia di "nigonzation" difensiva, focalizzandosi su contro-narrative, diplomazia legata alla Belt and Road Initiative (BRI) e tattiche "wolf warrior" per influenzare le élite. Le minacce cinesi in Italia si manifestano prevalentemente attraverso canali economici e diplomatici, piuttosto che tramite *troll factories*.

### 2. Il Caso Bucha come Test di Resilienza

L'operazione di disinformazione russa su Bucha ha dimostrato la vulnerabilità delle narrazioni false di fronte a prove fisiche inconfutabili. La geolocalizzazione SATellitare (es. Maxar) ha reso i fatti irrefutabili in 72 ore. Questa situazione evidenzia un'implicazione chiave per l'[[Osint]]: la [[Disinformazione]] tende a crollare quando le prove fisiche sono schiaccianti, mentre persiste in contesti di ambiguità probatoria.

### 3. Rilevamento del Coordinated Inauthentic Behavior (CIB)

Il rilevamento del [[Coordinated sharing behavior]] (CIB), spesso impiegato dagli attori statali, è diventato sempre più complesso. Le restrizioni all'accesso alle API di piattaforme come Twitter/X e la deprecazione di strumenti come Crowdtangle (Facebook) limitano la capacità di analisi. L'analisi di Telegram rimane possibile ma richiede un approccio manuale, mentre Tiktok offre API solo a partner selezionati. Strumenti [[Osint]] per il CIB (es. Botometer, Hoaxy, Gephi) offrono una copertura ridotta rispetto al 2020. I *pattern* di CIB includono *temporal clustering*, *linguistic similarity* e *network interconnection*.

## 🔮 Lacune Informative e Prossimi Passi

Permangono diverse lacune informative che ostacolano una comprensione completa delle operazioni degli [[Attori statali]]:
*   **Dati non pubblici:** La verifica indipendente delle stime su finanziamenti e capacità, in particolare per attori meno trasparenti, è difficile a causa della natura classificata di molti dati di intelligence (es. DIS/Copasir).
*   **Metriche aggiornate:** È necessario un aggiornamento continuo delle metriche relative a nuovi *trigger* o movimenti emergenti che potrebbero essere strumentalizzati da attori statali (es. movimenti anti-*15-minute cities*, anti-CBDC).
*   **Strumenti di *bot detection*:** La mancanza di *tool* completamente affidabili per la rilevazione di *bot* nell'era post-API rappresenta una sfida significativa per l'[[Osint]].

## 🔗 Connessioni e Pattern

- [[Applicazioni osint]]
- [[Disinformazione]]
- [[Osint]]
- [[Piattaforme]]
- [[Sicurezza nazionale]]


- [[--]]
F/I/H
- [[--]]
