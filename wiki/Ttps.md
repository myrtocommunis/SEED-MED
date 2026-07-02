---
title: Ttps
tags:
- OSINT
- processed
- ttps
date: '2026-05-15'
status: draft
depth: standard
sources: '1'
tipo: concetto
---

# Ttps

## 🎯 Sintesi Strategica

Le **TTPs** (Tactics, Techniques, and Procedures) rappresentano l'insieme strutturato di metodi e azioni impiegati da attori, sia statali che non-statali, per RAGgiungere specifici obiettivi operativi, in particolare nel contesto della [[Disinformazione]] e delle operazioni di influenza. Questa nota mappa la minaccia informativa in Italia attraverso l'analisi delle TTPs di attori statali (come Russia e Cina) e non-statali (quali gruppi di estrema destra e movimenti no-vax), evidenziando come le loro capacità, intenzioni e opportunità si traducano in un livello di minaccia complessivo. La formula fondamentale per la valutazione della minaccia è **Threat = Capacità × Intent × Opportunità**. Si osserva un declino nel *reach* diretto della Russia post-2022, compensato da operazioni tramite *proxy*, mentre la Cina adotta un profilo più difensivo e mirato alle élite.

## 📚 Contesto e Definizioni

Il concetto di TTPs è centrale nell'analisi della sicurezza e dell'intelligence, fornendo un framework per comprendere e prevedere il comportamento degli avversari. Nel contesto dell'[[Osint]] e dell'analisi della minaccia informativa, le TTPs descrivono le modalità operative specifiche:
*   **Tattiche:** Le strategie di alto livello impiegate per RAGgiungere un obiettivo.
*   **Tecniche:** I metodi specifici utilizzati per eseguire una tattica.
*   **Procedure:** I passaggi dettagliati per implementare una tecnica.

L'analisi qui presentata fornisce un *assessment* quantitativo degli [[Attori statali]] e non-statali della disinformazione con un focus sull'Italia. I dati provengono da relazioni pubbliche (es. Copasir/DIS), stime di *reach* e *assessment* comparati. La distinzione nelle TTPs tra attori come Russia e Cina è cruciale, poiché non tutti gli attori statali impiegano tattiche identiche, influenzando profondamente le strategie di rilevamento e mitigazione.

## 📊 Dati, Tecnologie e Metriche

L'analisi delle TTPs si basa su metriche e dati specifici che quantificano l'impatto e le capacità degli attori.

### Russia Pre-2022 (TTPs di destabilizzazione aperta)

| Indicatore | Valore |
|---|---|
| Budget operativo | 5-10M EUR/anno |
| Staff Italia | ~50 persone |
| Sputnik reach | 100-300k unique/mese |
| RT reach | 50-150k unique/mese |
| Social impressions | 500k-1M/mese combiNATO |

### Russia Post-2022 (TTPs evolute tramite proxy)

| Tattica | Dettaglio |
|---|---|
| Reach diretto | -70% |
| Reach proxy | ~30% pre-ban |
| Bot network | 100-500 stimati |
| Proxy websites | Siti terzi non affiliati |
| Telegram | Canali pacifisti/no-vax non dichiarati |

### No-Vax Peak (2021-2022) vs Core (2023-2024) (TTPs di mobilitazione e frammentazione)

| Indicatore | Peak | Core |
|---|---|---|
| Manifestazioni | 10-50k persone | N/D |
| Telegram | ~200k subscribers | ~10 canali attivi |
| Attivisti | 50k+ | 5-10k |
| Event mobilization | 2nd line | 100-500 persone |

### Minaccia Comparata (Valutazione TTPs-based)

| Attore | Capacità | Intent | Opportunity | Threat |
|---|---|---|---|---|
| Russia | Alta→Media | Alto | Media | MEDIO |
| Cina | Media | Basso | Bassa | BASSO |
| Estrema destra | Bassa | Medio | Media | MEDIO-BASSO |
| No-vax | Bassa | Basso | Bassa | BASSO |
| Politici mainstream | Alta | Variabile | Alta | MEDIO |

## 🔍 Analisi Operativa ed Applicazioni OSINT

L'applicazione delle TTPs nell'[[Osint]] permette di discernere le strategie sottostanti alle operazioni di influenza.

### 1. La Differenza Russia/Cina nelle TTPs

La Russia impiega TTPs di destabilizzazione aperta (es. proxy, bot massivi, narrazioni offensive), mirando alle masse. La Cina, al contrario, adotta TTPs di "nigonization" difensiva (es. contro-narrative, diplomazia della BRI, *wolf warrior diplomacy*), focalizzandosi sulle élite. Questa divergenza ha implicazioni significative per l'analisi: le minacce cinesi in Italia si manifestano prevalentemente attraverso canali economici e diplomatici, piuttosto che tramite *troll factories*.

### 2. Il Caso Bucha come Test di Resilienza delle TTPs di Disinformazione

L'operazione di *false flag* russa su Bucha è un raro esempio di disinformazione "collassata in 72 ore". La geolocalizzazione SATellitare (es. Maxar) ha fornito prove fisiche inconfutabili, rendendo le TTPs di negazione inefficaci. Questo caso sottolinea un insegnamento chiave per l'OSINT: la disinformazione crolla quando le prove fisiche sono irrefutabili, mentre persiste in contesti di ambiguità probatoria.

### 3. Il Caso #Ioapro: Distinzione Cruciale tra Grassroots e Astroturfing

Il movimento dei ristoratori #Ioapro è un esempio di iniziativa *grassroots* con amplificazione politica, non un puro *astroturfing*. Solo il 5% dell'*engagement* era attribuibile a bot. Questa distinzione è fondamentale per l'analisi delle TTPs: non tutto ciò che è coordiNATO è illegittimo. La "grievance" economica reale (crisi del settore) è stata opportunamente politicizzata, non costruita da attori esterni.

### 4. CIB Detection: Limiti delle TTPs di Rilevamento 2023+

Gli indicatori di [[Coordinated sharing behavior]] (CIB) sono sempre più difficili da rilevare a causa dell'evoluzione delle piattaforme e delle TTPs degli attori.
*   **API Twitter/X:** Costi elevati ($100-42k/mese) ne limitano l'accessibilità.
*   **Crowdtangle Facebook:** Deprecato ad Agosto 2024.
*   **Telegram:** L'analisi è possibile ma richiede un approccio manuale.
*   **Tiktok:** API disponibili solo per partner.
I tool OSINT per il CIB rimanenti (es. Botometer, Hoaxy, Gephi) offrono una copertura ridotta rispetto al 2020, rendendo più complesse le TTPs di analisi.

## 🔮 Lacune Informative e Prossimi Passi

L'analisi delle TTPs è un campo in continua evoluzione, con diverse lacune informative da colmare:
*   **Dati DIS/Copasir non pubblici:** Difficoltà nel verificare indipendentemente le stime su finanziamenti a gruppi di estrema destra.
*   **Metriche no-vax 2025:** Necessità di aggiornamenti costanti, considerando nuovi *trigger* (es. anti-*15-minute cities*, anti-CBDC).
*   **Bot detection tools:** Mancanza di strumenti completamente affidabili nell'era post-API, che richiede lo sviluppo di nuove TTPs di rilevamento.

## 🔗 Connessioni e Pattern

- [[Applicazioni osint]]
- [[Attori statali]]
- [[Disinformazione]]
- [[Non-statali]]
- [[Osint]]
- [[Piattaforme]]


- [[--]]
F/I/H
- [[--]]
