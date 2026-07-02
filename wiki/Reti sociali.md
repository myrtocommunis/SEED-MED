---
title: "Reti sociali"
tags: ["OSINT", "processed", "reti-sociali", "sna", "community-detection", "coordinated-sharing"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Reti sociali

## 🎯 Sintesi Strategica

L'analisi delle reti sociali (Social Network Analysis, SNA) applicata all'[[Osint]] e ai social media costituisce il ponte operativo per trasformare moli enormi di interazioni online in intelligence strutturata. Costruendo grafi a partire da retweets, mention, o interazioni utente-contenuto, l'analista è in grado di mappare le architetture invisibili del discorso pubblico online. Tecniche avanzate come la *Community Detection* e la *Coordinated Sharing Detection* permettono di isolare *echo chambers*, identificare attori centrali e scoprire reti di amplificazione artificiale o coordinata, distinguendo in modo critico tra il coordinamento organico (fisiologico) e i Comportamenti Inautentici Coordinati (CIB) tipici delle operazioni di manipolazione informativa.

## 📚 Contesto e Definizioni

Le piattaforme social non sono meri aggregatori di testo, ma strutture topologiche complesse mappabili attraverso l'astrazione a grafi (nodi e archi).

### Tipologie di Reti 

1.  **Rete Monopartita:** Reti in cui i nodi sono della stessa tipologia (es. Utente segue Utente, o Utente menziona Utente).
2.  **Rete Bipartita:** Reti contenenti due classi distinte di nodi, dove gli archi possono esistere solo tra classi diverse (es. classe Utenti e classe Hashtag; oppure classe Account e classe URL/Contenuto).
3.  **Proiezione di Rete Bipartita:** Procedura matematica che trasforma una rete bipartita in monopartita. Ad esempio, proiettando una rete Utente-Hashtag, si ottiene una rete in cui due utenti sono collegati se hanno utilizzato lo stesso hashtag (peso dell'arco basato sulla co-occorrenza).

## 📊 Dati, Tecnologie e Metriche

L'individuazione di cluster e camere d'eco (echo chambers) avviene tramite algoritmi specifici e metriche di polarizzazione.

### Algoritmo di Louvain e [[Modularità]]

L'**Algoritmo di Louvain** è uno standard euristico e randomizzato per la *Community Detection* (implementato ad es. in pacchetti come `igraph`). Operando tramite ottimizzazione golosa (greedy modularity optimization), RAGgruppa i nodi in sotto-reti densamente connesse al loro interno e debolmente connesse all'esterno.
*   **Metrica Chiave:** La **[[Modularità]] (Modularity)**. Valori superiori a `0.3` indicano la presenza di una struttura comunitaria significativa e non casuale all'interno del network.

### MP-MPAS e Insularity Score

Il modello **MP-MPAS** (Multi-Party Partisan Attention Score, introdotto da Giglietto et al., 2019) stima la polarizzazione dell'attenzione del pubblico verso fonti mediatiche in un sistema multipartitico.
*   **Insularity Score:** Oscilla da `0` (fonte *cross-partisan*, letta da diverse fazioni politiche) a `1` (fonte *altamente insulare*, consumata esclusivamente da una specifica fazione o "echo chamber", tipica della disinformazione o propaganda polarizzante).

## 🔍 Analisi Operativa ed Applicazioni OSINT

Il focus dell'intelligence digitale contemporanea è il rilevamento delle operazioni di amplificazione strategica.

### Coordinated Sharing Detection

L'identificazione di *Coordinated Sharing* mira a scoprire gruppi di utenti che compiono azioni identiche (es. condividere lo stesso URL) all'interno di una ristretta finestra temporale (time window).
*   **Strumenti:** Il pacchetto R **`Coortweet`** (Righetti et al., 2025) è la pipeline standard per individuare questi comportamenti. Calcola la probabilità di condivisione simultanea e genera network di account coordinati.
*   **La Distinzione Critica:** È imperativo per l'analista OSINT separare il *Coordinated Sharing* dal **CIB (Coordinated Inauthentic Behavior)**. Il coordinamento indica solo sincronizzazione temporale e può essere **organico e legittimo** (es. comunità di attivisti che twittano durante un evento live, fan base, breaking news). L'autenticità non può essere delegata all'algoritmo: richiede indagine umana manuale (sock-puppeting, account creati lo stesso giorno, pattern di automazione anomali).

## 🔮 Lacune Informative e Prossimi Passi

*   **Modelli di Rilevamento Semantico:** Necessità di chiarire tecnicamente le metodologie di rilevamento della similarità semantica per contenuti testuali parafrasati ma ideologicamente identici (utilizzo di tecniche NLP vs Hashing visivo/testuale).
*   **Formula MP-MPAS:** Assenza della documentazione e del codice sorgente completo per la validazione indipendente e la replica matematica dell'algoritmo MP-MPAS e della generazione dell'Insularity Score.
*   **Aggiornamento API:** Transizione delle metodologie di *community detection* in seguito alle restrizioni delle API di X/Twitter e analisi comparata su piattaforme alternative o decentralizzate (es. Mastodon, Bluesky).

## 🔗 Connessioni e Pattern

- [[Sna]]
- [[Tassonomia dei tools]]
- [[Community detection]]
- [[Coordinated sharing behavior]]
- [[Disinformazione]]
- [[Echo chamber]]

- [[--]]
F/I/H
- [[--]]
