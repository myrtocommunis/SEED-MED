---
title: Community detection
tags:
- OSINT
- processed
- community-detection
date: '2026-05-15'
status: draft
depth: standard
sources: '3'
tipo: concetto
---

# Community detection

## 🎯 Sintesi Strategica

La [[Community detection]] è un processo fondamentale nell'[[Social network analysis]] (SNA) che mira a identificare gruppi di nodi (individui, account, entità) all'interno di una rete che sono più densamente connessi tra loro rispetto al resto della rete. Questo approccio è cruciale nell'[[Osint]] per svelare strutture latenti, come fazioni politiche, [[Echo chamber]], reti di influenza o comportamenti coordinati, fornendo una comprensione approfondita delle dinamiche relazionali e informative.

## 📚 Contesto e Definizioni

La community detection si basa sul principio di partizionare una rete in sottoinsiemi di nodi, detti comunità o cluster, dove le connessioni interne a ciascun sottoinsieme sono significativamente più numerose o intense rispetto a quelle che collegano nodi di sottoinsiemi diversi. Questo fenomeno è spesso guidato da meccanismi come l'Omophilia (la tendenza dei nodi simili a connettersi) e le dinamiche di Polarizzazione.

Per valutare la qualità di una partizione in comunità, si utilizza la Modularity (Q), una metrica che quantifica la forza della divisione in comunità. Un valore di Q superiore a 0.3 è generalmente considerato indicativo di una struttura comunitaria significativa.

Tra gli algoritmi più diffusi per la community detection, spiccano:
*   **Louvain algorithm**: Altamente raccomandato per applicazioni OSINT grazie alla sua scalabilità (complessità O(n log n)) ed efficienza su reti di grandi dimensioni. Ottimizza la [[Modularità]] in modo euristico, gerarchico e greedy, producendo una gerarchia di comunità. È un algoritmo randomizzato, quindi i risultati possono variare leggermente ad ogni esecuzione.
*   **Edge Betweenness**: Un metodo che rimuove iterativamente gli archi con la più alta Betweenness centrality. È computazionalmente più oneroso (O(m²n)) e quindi più adatto a reti di dimensioni ridotte.

La scelta dell'algoritmo e dei parametri è cruciale e dipende dalla natura della rete e dagli obiettivi analitici.

## 📊 Dati, Tecnologie e Metriche

La community detection si applica a diverse tipologie di reti derivate da dati di piattaforma, in particolare dai social media:
*   **Reti di Retweet**: Nodi = utenti, Archi = chi retweeta chi. Rivelano flussi di informazione e fonti primarie.
*   **Reti di Menzioni**: Nodi = utenti, Archi = chi menziona chi. Indicano interazioni dirette e attenzione.
*   **Reti di Reply**: Nodi = utenti, Archi = chi risponde a chi. Evidenziano dibattiti e conflitti.
*   **Reti Utente-Hashtag**: [[Reti bipartite]] con nodi di due tipi (utenti e hashtag), archi solo tra tipi diversi. Rivelano narrative e temi condivisi.
*   **Reti Account-Contenuto**: [[Reti bipartite]] con account e contenuti, archi che indicano chi condivide cosa. Fondamentali per la Coordinated Sharing Detection.

Le Proiezione di rete trasformano le reti bipartite in reti monopartite, ad esempio, proiettando una rete Utente-Hashtag in una rete Utente-Utente, dove due utenti sono collegati se condividono gli stessi hashtag. Il peso degli archi può indicare il numero di elementi condivisi.

**Metriche chiave:**
*   **Modularity (Q)**: Come descritto, misura la qualità della partizione.
*   **NMI (Normalized Mutual Information)**: Utilizzato per confrontare diverse partizioni di comunità, con valori da 0 (indipendenti) a 1 (identiche). Altre metriche includono Variation of Information (VI) e Adjusted Rand Index (ARI).

**Tecnologie e Strumenti:**
*   Librerie di analisi di rete come `igraph` (R) o `NetworkX` (Python) implementano gli algoritmi di community detection.
*   Il pacchetto [[Coortweet]] (sviluppato da Nicola Righetti) è specifico per l'identificazione di comportamenti coordinati su piattaforme social, spesso come fase preliminare alla community detection.
*   Strumenti di visualizzazione come `ggraph` (R) o Gephi sono essenziali per l'interpretazione visiva delle comunità.

Una pipeline tipica per la detection di comportamenti coordinati e comunità include: importazione dati, costruzione di reti bipartite, proiezione, filtraggio statistico degli archi (es. `percentile_edge = 0.95` per identificare le connessioni più forti), applicazione di algoritmi di community detection (es. Louvain) e successiva visualizzazione e interpretazione.

## 🔍 Analisi Operativa ed Applicazioni OSINT

Nell'OSINT, la community detection è uno strumento potente per:
*   **Identificare Fazioni e [[Echo chamber]]**: Rileva gruppi con affinità ideologiche, politiche o tematiche, spesso caratterizzati da un'elevata omogeneità interna e scarsa interazione esterna.
*   **Rilevare Campagne di Disinformazione e Astroturfing**: L'identificazione di comunità che mostrano pattern di Coordinated Sharing Detection (condivisione sincronizzata degli stessi contenuti) può indicare l'esistenza di campagne di influenza, reti di bot o account inautentici.
*   **Analisi di Reti di Bot**: Comunità con nodi che presentano alto out-degree (molte condivisioni), basso in-degree (poche ricezioni) e pattern temporali ripetitivi possono essere indicatori di attività automatizzata.
*   **Casi Studio**: L'analisi di reti come quelle di TG24ore e Mag24 su Facebook ha dimostrato come la community detection possa mappare la struttura di network di disinformazione e le loro strategie di diffusione. Il framework MP-MPAS e l'Insularity Score sono stati utilizzati per stimare l'attenzione partigiana verso fonti mediatiche e identificare comunità altamente insulari.

**Considerazioni Interpretative Cruciali:**
*   **Coordinamento ≠ Manipolazione Inautentica (CIB)**: È fondamentale distinguere il comportamento coordiNATO dalla manipolazione inautentica. Il coordinamento può avere spiegazioni legittime (es. utenti che seguono le stesse fonti, reazioni a eventi di cronaca, comunità organiche). La classificazione come "Coordinated Inauthentic Behavior" (CIB) richiede un'investigazione OSINT manuale approfondita per accertare l'intenzione e l'autenticità degli account.
*   **SENSibilità dei Parametri**: Parametri come la `time_window` nella coordinated sharing detection influenzano significativamente i risultati. Una finestra temporale più stretta (es. 60 secondi) tende a intercettare sincronizzazioni più strette e ridurre i falsi positivi.

L'etichettatura qualitativa delle comunità, attraverso l'ispezione delle biografie degli utenti, dei contenuti condivisi e degli hashtag principali, è un passo indispensabile per dare significato ai cluster rilevati.

## 🔮 Lacune Informative e Prossimi Passi

Nonostante la robustezza metodologica, permangono alcune lacune e aree di sviluppo:
*   **Dataset Reali OSINT**: La disponibilità di dataset pubblici e verificati di campagne di disinformazione o reti di bot è limitata, rendendo difficile la pratica e la validazione delle competenze analitiche.
*   **Analisi di Rete Temporale**: Molti approcci trattano le reti come statiche. L'integrazione di tecniche di analisi di reti dinamiche, serie temporali, finestre mobili e rilevamento di "burst" è essenziale per monitorare l'evoluzione delle campagne.
*   **Metriche Avanzate**: L'esplorazione di metriche di centralità più avanzate (es. [[PageRank]], Katz centrality, K-core decomposition) e la gestione delle loro problematiche (es. problemi di convergenza per Eigenvector centrality) possono arricchire l'analisi.
*   **SNA Avversariale**: La ricerca su come attori ostili manipolano le reti sociali (es. reti di sock puppet, farm di amplificazione) e lo sviluppo di contromisure è un campo in evoluzione.
*   **Integrazione con Strumenti OSINT**: Una maggiore integrazione tra le librerie di SNA e strumenti OSINT come [[Maltego]] o [[Spiderfoot]] potrebbe ottimizzare i flussi di lavoro.
*   **Formule Dettagliate**: Le formule complete per metriche specifiche come MP-MPAS e l'Insularity Score, così come le tecniche precise per la rilevazione di similarità semantica (NLP, embedding, hashing), non sono sempre pubblicamente disponibili o dettagliate nelle fonti.

## 🔗 Connessioni e Pattern

- [[Coortweet]]
- [[Osint]]
- [[Reti bipartite]]
- [[Social network analysis]]


- [[--]]
F/I/H
- [[--]]
