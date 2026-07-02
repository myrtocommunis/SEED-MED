---
title: Coortweet
tags:
- OSINT
- processed
- coortweet
date: '2026-05-15'
status: draft
depth: standard
sources: '2'
tipo: concetto
---

# Coortweet

## 🎯 Sintesi Strategica

Coortweet è un framework analitico e un pacchetto software (implementato in R) progettato per la detection di coordinated sharing sui social media. Il suo obiettivo primario è identificare gruppi di account che condividono gli stessi contenuti in modo sincronizzato e con una frequenza statisticamente anomala. Questo strumento è fondamentale per le operazioni di [[Osint]] (Open Source Intelligence), consentendo di smascherare campagne di [[Disinformazione]], astroturfing e l'attività di reti di bot o account inautentici.

## 📚 Contesto e Definizioni

Il **Coordinated Sharing** si riferisce al fenomeno in cui più account sui social media condividono gli stessi contenuti entro finestre temporali ristrette, suggerendo un'azione coordinata piuttosto che organica. Questa pratica è spesso associata a tentativi di manipolazione dell'opinione pubblica o diffusione di narrazioni specifiche.

**Coortweet** è il nome del pacchetto R che implementa una metodologia robusta per rilevare tale coordinamento. La sua importanza per l'[[Osint]] risiede nella capacità di:
*   Rilevare e analizzare campagne di [[Disinformazione]] e influenza.
*   Identificare fenomeni di astroturfing e manipolazione orchestrata.
*   Scoprire reti di bot o account inautentici che operano in modo coordiNATO.

È cruciale notare che la rilevazione di un comportamento coordiNATO non implica automaticamente una manipolazione malevola; eventi di cronaca simultanei, la condivisione di fonti comuni o l'attività di comunità organiche possono generare pattern simili. L'analisi richiede quindi un'interpretazione contestuale.

## 📊 Dati, Tecnologie e Metriche

Il principio di funzionamento di Coortweet si basa sull'analisi delle relazioni tra account e contenuti attraverso la [[Social network analysis]] (SNA), con un focus sulle [[Reti bipartite]]. La pipeline analitica si articola in diverse fasi:

1.  **Identificazione dei Contenuti Condivisi**: Il sistema identifica i contenuti (es. URL, testi) che sono stati condivisi da più account.
2.  **Calcolo delle Finestre Temporali**: Viene definita una finestra temporale (es. 60 minuti) entro la quale le condivisioni multiple dello stesso contenuto sono considerate "sincronizzate".
3.  **Creazione di una Rete Bipartita**: Si costruisce una rete dove i nodi sono di due tipi: account (chi condivide) e contenuti (cosa viene condiviso). Un arco collega un account a un contenuto se quest'ultimo è stato condiviso entro la finestra temporale specificata.
4.  **Proiezione su Rete di Co-sharing**: Dalla rete bipartita Account-Contenuto, si genera una proiezione su una rete unipartita di soli account. In questa rete, due utenti sono connessi se hanno condiviso lo stesso contenuto. Il peso dell'arco tra due account indica il numero di contenuti condivisi in comune.
5.  **Filtraggio Statistico**: Viene applicato un filtro per identificare le co-condivisioni anomale. Parametri chiave includono:
    *   `time_window`: la finestra temporale in minuti (es. 60 minuti).
    *   `min_repetition`: il numero minimo di condivisioni per considerare un contenuto rilevante (es. 2).
    *   `percentile_edge`: una soglia statistica (es. 0.95) oltre la quale la frequenza di co-condivisione è considerata anomala rispetto alla distribuzione generale.
6.  **[[Community detection]]**: Sulla rete di co-sharing filtrata, viene applicato un algoritmo di [[Community detection]], come l'Algoritmo Louvain, per RAGgruppare gli account in cluster. Ogni cluster rappresenta un gruppo di account che condividono gli stessi contenuti, nella stessa finestra temporale, con una frequenza anomala. La modularity è una metrica utilizzata per valutare la qualità di questi RAGgruppamenti.

Il pacchetto complementare **Coortweetpost** estende le funzionalità di Coortweet, offrendo analisi temporali dei cluster, estrazione dettagliata dei contenuti, metriche avanzate e la generazione automatica di report.

## 🔍 Analisi Operativa ed Applicazioni OSINT

Nell'ambito dell'[[Osint]], Coortweet fornisce un approccio strutturato per l'identificazione di comportamenti sospetti sui social media. Le sue applicazioni includono:
*   **Identificazione di Campagne di Influenza**: Rilevare gruppi di account che spingono una narrazione specifica, potenzialmente indicando una campagna coordinata.
*   **Analisi di Reti Inautentiche**: Scoprire cluster di account che mostrano pattern di condivisione tipici di bot o account falsi, spesso utilizzati per amplificare messaggi.
*   **Monitoraggio di Eventi e Crisi**: Analizzare la diffusione di informazioni durante eventi critici per distinguere la condivisione organica da quella coordinata, prevenendo la diffusione di [[Disinformazione]].

Una checklist analitica per l'operatore [[Osint]] include:
*   Chi sono gli account all'interno di un cluster coordiNATO?
*   Quali contenuti specifici condividono e con quale frequenza?
*   Esiste un pattern temporale sospetto nelle loro attività di condivisione?

## 🔮 Lacune Informative e Prossimi Passi

Nonostante la sua robustezza metodologica, Coortweet presenta alcune aree di miglioramento e lacune analitiche:
*   **Finestra Temporale Fissa**: L'uso di una `time_window` fissa (es. 60 minuti) potrebbe non essere ottimale per tutte le campagne, alcune delle quali operano su scale temporali più ampie (ore o giorni).
*   **Soglia `min_repetition` Bassa**: Un valore di `min_repetition` pari a 2 può generare molti falsi positivi, poiché la condivisione organica di contenuti virali o di notizie può facilmente superare questa soglia.
*   **Bias dell'Algoritmo Louvain**: L'algoritmo tende a favorire la rilevazione di comunità più piccole, il che potrebbe frammentare cluster di coordinamento più ampi.
*   **Mancanza di Normalizzazione per la Dimensione degli Account**: La proiezione non normalizza per il numero di follower o l'influenza degli account, trattando allo stesso modo un account con milioni di follower e uno con pochi, il che può distorcere l'analisi.
*   **Limiti API**: La raccolta dati da piattaforme come X/Twitter è soggetta a limiti API, che possono influenzare la completezza e la rappresentatività del dataset.
*   **Metriche di Validazione**: Mancano metriche di qualità oltre la modularity (es. precisione, recall) per validare l'accuratezza dei cluster in assenza di un ground truth.
*   **Distinzione Bot vs. Umani**: Lo strumento rileva il coordinamento ma non distingue intrinsecamente tra bot coordinati e umani che agiscono in modo coordiNATO.
*   **Autocorrelazione Temporale**: Non viene esplicitamente considerata l'autocorrelazione temporale, dove tweet in finestre adiacenti non sono indipendenti.

I prossimi passi per l'evoluzione di Coortweet e metodologie simili dovrebbero includere l'integrazione di soglie dinamiche per la finestra temporale e la ripetizione minima, la normalizzazione per la dimensione degli account, l'implementazione di metriche di validazione più sofisticate e l'esplorazione di tecniche complementari come Coovoter per una validazione incrociata del coordinamento.

## 🔗 Connessioni e Pattern

- [[Community detection]]
- [[Disinformazione]]
- [[Osint]]
- [[Reti bipartite]]
- [[Social network analysis]]


- [[--]]
F/I/H
- [[--]]
