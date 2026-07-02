---
title: Analisi sna
tags:
- OSINT
- processed
- analisi-sna
date: '2026-05-15'
status: draft
depth: standard
sources: '1'
tipo: concetto
---

# Analisi sna

## 🎯 Sintesi Strategica

L'Analisi delle Reti Sociali (SNA) costituisce un framework metodologico fondamentale per la mappatura strutturale delle interazioni tra attori, entità e flussi informativi. In ambito OSINT, la SNA trasforma dati relazionali grezzi in topologie interpretabili, consentendo l'identificazione di nodi critici, la rilevazione di cluster coordinati e la valutazione della resilienza di sistemi complessi. La disciplina integra formalismi matematici della teoria dei grafi con tecniche computazionali per supportare il triage operativo e la generazione di intelligence predittiva.

## 📚 Contesto e Definizioni

Il fondamento teorico della SNA risiede nella [[Teoria dei grafi]], dove una rete è formalizzata come $G=(V,E)$, con $V$ insieme di vertici (nodi) ed $E$ insieme di archi (relazioni). Le reti possono essere classificate in dirette, non dirette, pesate o non pesate. La rappresentazione matriciale, in particolare la Matrice di adiacenza, codifica le connessioni in forma binaria o continua, abilitando operazioni algebriche per l'analisi strutturale. Concetti cardine includono la densità (rapporto tra archi esistenti e massimi possibili), le componenti connesse (sottoinsiemi di nodi mutualmente RAGgiungibili) e il grado (numero di connessioni dirette per nodo).

## 📊 Dati, Tecnologie e Metriche

L'elaborazione operativa richiede l'implementazione di algoritmi su piattaforme come NetworkX, igraph o ambienti R (`graph_from_edgelist`, `as_adjacency_matrix`). Le metriche di base includono:
- **Grado medio**: $\bar{k} = 2|E|/|V|$ (per grafi non diretti).
- **DENSità**: $\rho = |E|/|E|_{max}$.
- **Backboning**: tecniche di filtraggio (soglia assoluta, proporzionale, gamma min) per isolare connessioni significative da rumore strutturale.
La determinazione dei pesi sugli archi richiede metodologie specifiche (TF-IDF sui contenuti, decadimento temporale, conteggio frequenziale), mentre la rilevazione di attori centrali necessita di estensioni oltre il grado semplice, come Centralità nei grafi (betweenness, closeness, eigenvector).

## 🔍 Analisi Operativa ed Applicazioni OSINT

In contesti di intelligence, la SNA supporta:
- **Rilevazione di disinformazione e bot farm**: pattern di alto out-degree combiNATO a basso in-degree fungono da euristica iniziale, da corroborare con feature temporali (interleaving di pubblicazione) e rapporti follower/following.
- **Mappatura di reti criminali e terroristiche**: identificazione di hub di coordinamento e ponti strutturali attraverso l'analisi delle componenti connesse e della densità locale.
- **Analisi di Cyber-Intelligence Business (CIB)**: utilizzo di [[Reti bipartite]] per correlare attori a infrastrutture digitali, account o domini, superando i limiti delle reti monople.
La validazione operativa richiede sempre la triangolazione con dati contestuali e la consapevolezza che le metriche strutturali da sole non garantiscono classificazione definitiva di entità malevole.

## 🔮 Lacune Informative e Prossimi Passi

La base teorica attuale presenta limiti operativi rilevanti:
- Assenza di implementazione delle metriche di centralità avanzate, essenziali per la priorizzazione degli attori.
- Definizione incompleta dei metodi di calcolo dei pesi in contesti OSINT reali.
- Necessità di formalizzare gli algoritmi di backboning e di integrare feature dinamiche (temporali, comportamentali) per il Bot detection.
- Mancanza di riferimenti alla letteratura di riferimento (Freeman, Wasserman & Faust, Newman) per la validazione accademica dei modelli.
I prossimi passi richiedono l'integrazione di casi studio operativi validati e l'espansione del framework verso modelli dinamici e multilivello.

## 🔗 Connessioni e Pattern

- [[Applicazioni osint]]
- [[Classificazione]]
- [[Disinformazione]]
- [[Infrastrutture]]
- [[Reti bipartite]]
- [[Teoria dei grafi]]


- [[--]]
F/I/H
- [[--]]
