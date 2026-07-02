---
title: "Social network analysis"
tags: ["OSINT", "processed", "sna", "grafi", "community-detection"]
date: "2026-05-15"
status: "draft"
depth: "deep"
sources: "5"
tipo: "concetto"
---

# Social network analysis

## 🎯 Sintesi Strategica

La **Social Network Analysis (SNA)** è la trasposizione sociologica e operativa della Teoria dei Grafi applicata alle reti relazionali umane e digitali. In ambito [[Osint]], la SNA abbandona l'analisi testuale o semantica per concentrarsi esclusivamente sulla **topologia dei legami**: chi è connesso a chi, con quale intensità e secondo quale struttura. È la metodologia definitiva per mappare organizzazioni criminali, reti di disinformazione (*Troll Farms*), influenze politiche e strutture societarie occulte, convertendo masse caotiche di dati in grafici visivi (Network Graphs) computabili matematicamente.

## 📚 Contesto e Definizioni

Un grafo di SNA è composto da due elementi essenziali:
1.  **Nodi (Vertici / Actor):** Le entità (es. account Twitter, indirizzi IP, aziende, individui).
2.  **Archi (Edges / Ties):** I legami tra i nodi (es. "segue", "ha ritwittato", "è azionista di"). Possono essere **diretti** (unidirezionali, come un bonifico) o **indiretti** (bidirezionali, come un'amicizia su Facebook), nonché **pesati** (basati sulla frequenza dell'interazione).

Una variante avanzata essenziale per il contrasto alle [[Disinformazione]] è costituita dalle **[[Reti bipartite]]**, che separano esplicitamente i nodi "Attori" dai nodi "Contenuti".

## 📊 Dati, Tecnologie e Metriche

Il "potere" o l'importanza di un nodo non si misura in base ai suoi follower, ma in base alla sua posizione topologica nella rete. Le metriche centrali sono:
*   **Degree Centrality:** Il numero puro di connessioni dirette. (Chi ha più legami? Identifica i *Broadcaster*).
*   **Betweenness Centrality (Centralità di Intermediazione):** Quante volte un nodo si trova sul percorso più breve tra altri due nodi. Nodi con alta Betweenness sono i *Broker* (ponti di collegamento tra due community isolate). Se eliminati, la rete si frammenta.
*   **Closeness Centrality (Vicinanza):** Misura quanto un nodo può RAGgiungere velocemente tutti gli altri nodi. Ideale per tracciare il propagatore ottimale di un virus informatico o di una Fake News.
*   **Eigenvector Centrality:** Valuta l'influenza del nodo basandosi sull'influenza dei nodi a cui è collegato (il principio alla base dell'algoritmo [[PageRank]] di Google). "Non conta quanti amici hai, ma quanto sono importanti i tuoi amici".

## 🔍 Analisi Operativa ed Applicazioni OSINT

L'elaborazione pratica della SNA richiede l'uso di tool dedicati (come **Gephi**, Maltego o librerie Python come NetworkX) all'interno della fase di [[Trattamento dell'output]]:
*   **Community Detection:** Algoritmi (come Louvain) permettono all'analista di RAGgruppare automaticamente milioni di nodi in cluster (comunità) strettamente interconnessi, svelando le macro-fazioni all'interno di un dibattito politico ([[Algoritmi]] ed Echo Chambers).
*   **Identificazione di Botnet:** Reti altamente dense e artificialmente sincronizzate (es. migliaia di account creati nello stesso giorno che retwittano gli stessi URL nel giro di pochi secondi) appaiono visivamente nel grafo come densissimi agglomerati anomali, svelando operazioni di manipolazione inautentica (*Coordinated Sharing Behavior*).

## 🔮 Lacune Informative e Prossimi Passi

*   **Reti Dinamiche Temporali:** I network grafici tradizionali sono scatti statici (fotografie). L'evoluzione moderna richiede l'analisi *longitudinale* (video), che mostra come i legami si formano, muoiono o si modificano nel tempo, richiedendo però enormi capacità di calcolo computazionale.

## 🔗 Connessioni e Pattern

- [[Reti bipartite]]
- [[Disinformazione]]
- [[Tassonomia dei tools]]
- [[Trattamento dell'output]]
- [[Osint]]

- [[--]]
F/I/H
- [[--]]
