---
title: Centralità nelle reti sociali
tags:
- OSINT
- processed
- centralità-nelle-reti-sociali
date: '2026-05-15'
status: draft
depth: standard
sources: '1'
tipo: concetto
---

# Centralità nelle reti sociali

## 🎯 Sintesi Strategica

La centralità nelle reti sociali costituisce un insieme di indicatori quantitativi progettati per misurare l'importanza, l'influenza o la posizione strategica di un nodo all'interno di una topologia relazionale. In ambito OSINT, queste metriche trasformano dati relazionali grezzi in indicatori operativi, distinguendo sistematicamente tra visibilità superficiale e potere strutturale reale. Le quattro metriche canoniche (Degree, Betweenness, Closeness, Eigenvector) rispondono a interrogativi investigativi distinti; il loro incrocio e confronto è indispensabile per mappare con precisione la dinamica informativa, i flussi di controllo e i target prioritari.

## 📚 Contesto e Definizioni

La teoria della centralità, formalizzata nella letteratura sociologica e matematica delle reti, definisce l'importanza di un nodo esclusivamente in relazione alla sua posizione nella struttura del grafo. In un contesto di [[Social network analysis]], la centralità non coincide con l'autorità formale o la popolarità mediatica, ma con la capacità di un nodo di influenzare, mediare o accelerare i flussi di informazione. La normalizzazione dei valori tra 0 e 1 è un requisito operativo fondamentale per confrontare metriche con scale eterogenee e per integrare i risultati in pipeline analitiche o dashboard di intelligence.

## 📊 Dati, Tecnologie e Metriche

Le metriche di centralità si classificano in base al tipo di percorso e alla direzione della rete analizzata:
- **Degree Centrality (Popolarità):** Conta il numero di connessioni dirette di un nodo. Valori elevati indicano hub o nodi periferici a seconda della direzionalità del grafo.
- **Betweenness Centrality (Controllo/Mediazione):** Misura la frequenza con cui un nodo appare sui cammini minimi tra tutte le coppie di nodi. Formula operativa: $BC(v) = \sum_{s \neq v \neq t} \frac{\sigma_{st}(v)}{\sigma_{st}}$. La complessità computazionale è $O(VE)$ per grafi non pesati (algoritmo di Brandes), rendendola critica per reti >100k nodi senza tecniche di sampling o approssimazione.
- **Closeness Centrality (Rapidità):** Basata sull'inverso della somma delle distanze minime da tutti gli altri nodi. Indica la velocità potenziale di diffusione o ricezione delle informazioni.
- **Eigenvector Centrality (Prestigio):** Assegna importanza in base alla qualità delle connessioni. Un nodo è centrale se connesso ad altri nodi centrali. Concettualmente affine al [[PageRank]], ma privo del fattore di damping e della gestione esplicita dei dead-end.
- **Correlazioni e Visualizzazione:** Degree ed Eigenvector mostrano alta correlazione empirica in reti scale-free. La visualizzazione efficace combina dimensione del nodo (Degree) e colore (Betweenness) per distinguere visibilità da controllo strutturale.

## 🔍 Analisi Operativa ed Applicazioni OSINT

Nell'analisi OSINT, la selezione della metrica deve essere guidata dall'obiettivo investigativo:
| Obiettivo Operativo | Metrica Riferimento |
|---|---|
| Identificazione di influencer o hub | Degree Centrality |
| Rilevamento di broker o gatekeeper nascosti | Betweenness Centrality |
| Mappatura di nodi per diffusione rapida | Closeness Centrality |
| Analisi di élite, leadership reale o prestigio | Eigenvector Centrality |
| Valutazione della resilienza e punti di rottura | Betweenness Centrality |

Il takeaway operativo fondamentale è che Degree ≠ potere strategico. La Betweenness identifica attori critici non evidenti alla visibilità superficiale, mentre l'Eigenvector misura l'influenza strutturale reale. La normalizzazione e il confronto incrociato delle metriche sono indispensabili per evitare falsi positivi nell'identificazione di target prioritari.

## 🔮 Lacune Informative e Prossimi Passi

L'analisi basata esclusivamente sulle quattro metriche canoniche presenta limiti strutturali per reti OSINT di larga scala:
- Assenza di valutazione della qualità dei cluster: necessità di integrare la [[Social network analysis]] per validare la segmentazione.
- Limiti nella mappatura dei nuclei strutturati: introduzione della [[K-shell decomposition]] per identificare core strutturati in reti massive.
- Generalizzazione dei percorsi: la Katz Centrality estende l'Eigenvector ponderando i cammini brevi, offrendo maggiore precisione in grafi diretti.
- Vincoli computazionali: le reti OSINT reali (milioni di nodi) richiedono approssimazioni, campionamento stratificato o framework distribuiti (es. NetworkX, igraph, Gephi) per la Betweenness e la Closeness.
- Gestione dei dead-end e damping: l'Eigenvector canonico non gestisce i cicli o i nodi isolati; per applicazioni web-scale è necessario il passaggio al [[PageRank]] o alla [[Persona]].

## 🔗 Connessioni e Pattern

- [[Applicazioni osint]]
- [[Fondamenti matematici]]
- [[Network analysis]]
- [[Network analysis per osint]]
- [[Reti sociali]]
- [[Social network analysis]]


- [[--]]
F/I/H
- [[--]]
