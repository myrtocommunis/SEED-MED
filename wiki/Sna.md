---
title: Sna
tags:
- OSINT
- processed
- sna
date: '2026-05-15'
status: draft
depth: standard
tipo: concetto
---

title: "Sna"
tags: ["OSINT", "processed", "sna"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Sna

## 🎯 Sintesi Strategica

La Social Network Analysis (SNA) rappresenta un pilastro fondamentale nell'[[Osint]] per la comprensione delle relazioni e delle strutture all'interno di reti complesse. Il suo valore strategico risiede nella capacità di andare oltre l'identificazione dei singoli attori, rivelando chi sono le entità connesse e la natura delle loro interazioni. Questo approccio, basato sulla [[Teoria dei grafi]], permette di identificare attori chiave, scoprire comunità nascoste, prevedere flussi informativi e rilevare vulnerabilità strutturali, risultando cruciale per l'identificazione di coordinamento e manipolazione in contesti di disinformazione, cybercrime e terrorismo.

## 📚 Contesto e Definizioni

La Social Network Analysis (SNA) si fonda sulla [[Teoria dei grafi]], una struttura matematica che rappresenta relazioni tra entità. Un grafo $G$ è definito come una coppia $(V, E)$, dove $V$ è l'insieme dei nodi (o vertici) e $E$ è l'insieme degli archi (o spigoli) che rappresentano le relazioni tra i nodi.

*   **Nodi (V):** Rappresentano le entità all'interno della rete (es. persone, account social, pagine web, URL).
*   **Archi (E):** Rappresentano le relazioni o le interazioni tra i nodi (es. amicizie, retweet, follow, link ipertestuali).

### Tipi di Grafo Rilevanti per OSINT

1.  **Grafo non diretto:** Le relazioni sono simmetriche (se A è connesso a B, B è connesso ad A). Esempio: amicizia su Facebook.
2.  **Grafo diretto (digraph):** Le relazioni sono asimmetriche. Esempio: follow su Twitter/X, retweet, link tra siti web.
3.  **Grafo pesato:** Ogni arco ha un peso ($w$) che quantifica l'intensità o la frequenza della relazione. Il peso può indicare prossimità (peso alto = più vicini) o distanza (peso alto = più lontani). Le reti di correlazione spesso richiedono tecniche di *backboning* per filtrare connessioni non significative.

### Rappresentazione Matrice di Adiacenza

Una rete può essere rappresentata tramite una matrice di adiacenza $A$, dove $A[i,j] = 1$ se esiste un arco tra il nodo $i$ e il nodo $j$, altrimenti 0. Per i grafi non diretti, la matrice $A$ è simmetrica; per i grafi diretti, $A \neq A^T$.

## 📊 Dati, Tecnologie e Metriche

L'analisi delle reti si avvale di diverse metriche e tecniche per estrarre informazioni significative:

### Proprietà di Base dei Grafi

*   **Ordine:** Numero totale di nodi ($|V|$).
*   **Dimensione:** Numero totale di archi ($|E|$).
*   **Degree ($k(v)$):** Numero di archi incidenti a un nodo $v$.
    *   **In-degree:** Numero di archi entranti (es. chi segue un account).
    *   **Out-degree:** Numero di archi uscenti (es. chi un account segue).
    *   *Insight OSINT:* Alto in-degree e basso out-degree possono indicare un **hub di disinformazione** (amplificatore). Alto out-degree e basso in-degree possono suggerire un **bot** (mass follower).
*   **Strength:** Somma dei pesi degli archi incidenti a un nodo, utile per grafi pesati.
*   **DENSità ($\rho$):** Rapporto tra il numero di archi esistenti e il numero massimo possibile di archi. Le reti reali sono spesso *sparse*.
    *   *Insight OSINT:* Sottoreti molto dense possono indicare **coordinamento artificiale** (es. bot farm).
*   **Cammino:** Sequenza di nodi connessi da archi.
*   **Distanza:** Lunghezza del cammino più breve tra due nodi.
*   **Diametro:** Distanza massima tra due nodi nella rete.
*   **Componenti connesse:** Sottografi in cui ogni nodo è RAGgiungibile da ogni altro. Spesso esiste una "componente gigante" centrale.

### Metriche di Centralità

Le [[Metriche]] identificano i nodi più importanti o influenti in una rete:
*   **Degree Centrality:** Misura il numero di connessioni dirette di un nodo.
    *   *Uso OSINT:* Identifica amplificatori o potenziali bot (alto out-degree), e fonti primarie (alto in-degree).
*   **Betweenness Centrality:** Misura quante volte un nodo si trova sul cammino più breve tra altre coppie di nodi.
    *   *Uso OSINT:* Rileva broker strategici o ponti tra comunità, fondamentali per il flusso di informazioni.
*   **Closeness Centrality:** Misura la distanza media di un nodo da tutti gli altri nodi della rete.
    *   *Uso OSINT:* Identifica diffusori rapidi di informazioni.
*   **Eigenvector Centrality:** Assegna punteggi più alti ai nodi connessi a nodi importanti.
    *   *Uso OSINT:* Rileva figure di autorità o prestigio all'interno della rete.
    *   *Nota operativa:* È buona pratica normalizzare tutte le metriche tra 0 e 1 per facilitare il confronto.

### Community Detection

L'obiettivo è identificare gruppi di nodi più connessi internamente che con il resto della rete, rivelando fazioni, [[Echo chamber]] o comportamenti coordinati.
*   **Edge Betweenness:** Rimuove iterativamente gli archi con la betweenness più alta. Adatto per reti di piccole dimensioni.
*   **Louvain (raccomandato per OSINT):** Ottimizza la [[Modularità]] in modo greedy e gerarchico. Scalabile a milioni di nodi e ampiamente utilizzato in OSINT.
*   **[[Modularità]] (Q):** Una metrica che valuta la qualità di una partizione in comunità. Valori Q > 0.3 indicano una struttura comunitaria significativa.
*   **Confronto di partizioni:** Metriche come NMI (Normalized Mutual Information) permettono di confrontare diverse partizioni in comunità.

### Reti Bipartite e Proiezioni

Le [[Reti bipartite]] contengono due tipi distinti di nodi, con archi che esistono solo tra nodi di tipo diverso (es. Utenti ↔ Hashtag, Account ↔ Contenuti).
*   **Proiezioni:** Trasformano una rete bipartita in una rete mono-tipo.
    *   Proiezione su Utenti (da hashtag): Rileva utenti che condividono la stessa narrativa, suggerendo potenziali gruppi coordinati.
    *   Proiezione su Hashtag (da utenti): Rileva co-occorrenze di hashtag, indicando temi correlati.
    *   Il peso degli archi nella proiezione può rappresentare il numero di elementi (es. hashtag) in comune.

### Coordinated Sharing Detection

Identifica comportamenti in cui più account condividono gli stessi contenuti in modo sincronizzato, rivelando campagne di disinformazione, astroturfing o reti di bot.
*   **Principio (Coortweet):** Identifica contenuti condivisi da più account, calcola finestre temporali di condivisione, crea una rete di co-sharing tra account e rileva cluster coordinati.
*   **Pipeline:** Dati grezzi → Rete bipartita (Account ↔ Contenuto) → Proiezione (Account ↔ Account) → Peso archi (numero co-condivisioni) → Filtraggio statistico (es. percentile 95%) → [[Community detection]] (Louvain) → Interpretazione qualitativa.
*   **Filtraggio statistico:** Distingue il co-sharing normale da quello anomalo (es. 50 link in 60 secondi).

## 🔍 Analisi Operativa ed Applicazioni OSINT

La SNA abilita capacità operative cruciali per l'intelligence OSINT:

### Applicazioni Operative

*   **Disinformazione:** Identificare reti di account coordinati che diffondono notizie false.
*   **Cybercrime:** Mappare infrastrutture criminali, forum underground e reti di riciclaggio.
*   **Terrorismo:** Ricostruire celle operative, identificare facilitatori e reclutatori.

### Capacità Abilitate

*   Trovare attori chiave (tramite metriche di centralità).
*   Scoprire comunità nascoste (tramite community detection).
*   Predire flussi informativi (diffusione su grafi).
*   Identificare vulnerabilità strutturali (ponti, connettori).

### Reti da Social Media

L'analisi di dati da piattaforme come Twitter/X permette di costruire diverse tipologie di rete:
*   **Retweet:** Nodi = Utenti, Archi = Chi retweeta chi. Rivela il flusso di informazione.
    *   *In-degree:* Fonti primarie.
    *   *Out-degree:* Amplificatori o bot.
    *   *Betweenness:* Broker strategici.
*   **Menzioni:** Nodi = Utenti, Archi = Chi menziona chi. Rivela interazioni dirette.
*   **Reply:** Nodi = Utenti, Archi = Chi risponde a chi. Rivela dibattiti e conflitti.
*   **Hashtag:** Nodi = Utenti + Hashtag, Archi = Chi usa quale hashtag. Rete bipartita che rivela narrative e temi.

### Interpretazione del Coordinamento

È fondamentale distinguere il coordinamento organico da quello manipolatorio. Una checklist analitica include:
*   Analisi degli account nel cluster (biografie, storia, comportamento).
*   Valutazione dei contenuti condivisi (qualità, fonte, narrativa).
*   Ricerca di pattern temporali sospetti (picchi, orari, regolarità).
*   Verifica delle caratteristiche di autenticità degli account (età, attività, follower).

## 🔮 Lacune Informative e Prossimi Passi

Nonostante la robustezza teorica, l'applicazione della SNA in OSINT presenta aree di miglioramento:
*   **Dataset reali OSINT:** Necessità di accedere a dataset reali di campagne di disinformazione o reti di bot per la pratica e la validazione delle tecniche.
*   **Metriche avanzate:** Esplorazione di metriche come [[PageRank]], Katz centrality, K-core decomposition per analisi più sofisticate.
*   **Analisi di reti temporali:** Integrazione di tecniche per l'analisi di reti dinamiche, time-series e rilevamento di *burst* per campagne che evolvono nel tempo.
*   **Integrazione con strumenti OSINT:** Sviluppo di workflow che combinino strumenti SNA (es. Gephi, R/igraph) con piattaforme OSINT (es. Maltego, Spiderfoot).
*   **SNA avversaria:** Studio di come attori ostili manipolano le reti sociali (es. reti di sock puppet, farm di amplificazione).
*   **Bias del materiale:** Il materiale attuale si concentra principalmente sulle reti Twitter, che non sono rappresentative dell'intero ecosistema informativo (es. Facebook, Telegram, reti private).

## 🔗 Connessioni e Pattern

- [[Applicazioni osint]]
- [[Community detection]]
- [[Osint]]
- [[Reti bipartite]]
- [[Social network analysis]]
- [[Teoria dei grafi]]


- [[--]]
F/I/H
- [[--]]
