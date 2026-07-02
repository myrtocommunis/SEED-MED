---
title: "Reti bipartite"
tags: ["OSINT", "processed", "reti-bipartite", "sna", "coordinated-sharing", "coortweet"]
date: "2026-05-15"
status: "draft"
depth: "deep"
sources: "2"
tipo: "concetto"
---

# Reti bipartite

## 🎯 Sintesi Strategica

Nella Social Network Analysis (SNA) applicata all'[[Osint]], le **Reti Bipartite** rappresentano l'architettura matematica d'elezione per modellare e individuare le campagne di manipolazione informativa. A differenza dei grafi monopartiti (che collegano solo account con account), i grafi bipartiti separano strutturalmente gli attori (Utenti) dai contenuti (URL, Hashtag, Immagini). Questa separazione impedisce all'analista di confondere la mera viralità o popolarità di un contenuto con il **coordinamento algoritmico**. Attraverso la procedura di *Proiezione di Rete* e pacchetti statistici come *coortweet*, è possibile rilevare chirurgicamente i cluster di *Coordinated Sharing*, individuando network di account che condividono sistematicamente gli stessi contenuti all'interno di finestre temporali anomale.

## 📚 Contesto e Definizioni

L'architettura dei social media si modella nativamente su grafi bipartiti.

### Tipologia di Grafi Bipartiti

Un grafo bipartito è una rete in cui i nodi appartengono a due insiemi disgiunti (es. `Insieme U` = Utenti; `Insieme C` = Contenuti) e gli archi possono collegare solo un nodo di `U` con un nodo di `C`.
*   **Vantaggio Analitico:** Permette di tracciare esattamente "Chi" sta condividendo "Cosa", senza assumere aprioristicamente un legame diretto tra gli utenti.

### Proiezione (Projection)

È il calcolo matematico che converte una rete bipartita in una rete monopartita "co-sharing". Due nodi `Utente A` e `Utente B` vengono collegati da un arco (con un peso proporzionale alla frequenza) solo se hanno condiviso *lo stesso identico contenuto* `C`.

## 📊 Dati, Tecnologie e Metriche

Il rilevamento di *Coordinated Sharing* si basa su soglie temporali e filtri statistici rigorosi.

### Il Workflow `coortweet`

Il pacchetto in linguaggio R `coortweet` (Righetti et al., 2025) è il toolkit accademico di riferimento per implementare questa analisi:
1.  **Definizione Finestra Temporale (`time_window`):** Di default fissata a 60 minuti, rintraccia gli utenti che condividono lo stesso URL entro un lasso di tempo estremamente breve.
2.  **Soglia di Ripetizione (`min_repetition`):** Fissa il numero minimo di condivisioni coordinate necessarie per formare un arco.
3.  **Filtraggio Statistico Adattivo:** L'uso del `percentile_edge` (es. $0.95$) mantiene solo il 5% degli archi con i legami più pesanti e anomali, evitando l'utilizzo di soglie fisse che verrebbero distorte in dataset virali.
4.  **Community Detection:** Applicazione dell'algoritmo di **Louvain** per RAGgruppare gli account fortemente interconnessi in cluster modulari.

## 🔍 Analisi Operativa ed Applicazioni OSINT

L'applicazione di questi modelli richiede un altissimo livello di prudenza epistemologica da parte dell'analista d'intelligence.

### Coordinamento vs Comportamento Inautentico (CIB)

La regola aurea della *Detection* è: **Coordinamento $\neq$ Manipolazione Inautentica**.
*   **Coordinamento Fisiologico:** Tifoserie calcistiche, fanbase musicali o attivisti politici in tempo di elezioni possono condividere organicamente lo stesso link in pochi minuti (sincronizzazione temporale organica).
*   **Comportamento Inautentico CoordiNATO (CIB):** Gruppi di bot, *troll farms* o sock puppet creati dallo stesso *threat actor* per alterare le metriche di engagement.
*L'algoritmo rileva il primo; l'analista OSINT, tramite indagini qualitative sugli account isolati dal cluster, dimostra il secondo.*

## 🔮 Lacune Informative e Prossimi Passi

L'architettura attuale presenta vulnerabilità metodologiche che l'analista deve compensare:
*   **Assenza di Normalizzazione dei Follower:** La proiezione bipartita standard non differenzia il "peso" di un account bot da zero follower rispetto a un account media da 10 milioni di follower. Questo sbilancia l'influenza del cluster.
*   **Bias dell'Algoritmo Louvain:** Tende a identificare micro-comunità molto frammentate, frammentando le reti di disinformazione che operano in *broadcast* massivo.
*   **Mancanza di Metriche di Validazione:** Nell'OSINT web, dove manca una *ground truth* (ovvero la certezza di chi sia un bot e chi no), metriche rigorose di precisione e *recall* sono difficilmente applicabili per validare il modello.

## 🔗 Connessioni e Pattern

- [[Sna]]
- [[Reti sociali]]
- [[Community detection]]
- [[Coordinated sharing behavior]]
- [[Disinformazione]]
- [[Tassonomia dei tools]]

- [[--]]
F/I/H
- [[--]]
