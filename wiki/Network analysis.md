---
title: "Network analysis"
tags: ["OSINT", "processed", "network-analysis", "sna", "grafi", "indagini"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Network analysis

## 🎯 Sintesi Strategica

La **Network Analysis (Analisi di Rete o SNA)** è il nucleo matematico dell'intelligence investigativa. Invece di focalizzarsi sui singoli soggetti isolati, studia esclusivamente le *Relazioni* (Edges/Archi) tra di essi (Nodi). È il principio per cui "Il legame tra due criminali vale più delle loro singole identità". Applicata alla [[Finint]], all'antiterrorismo o alla caccia alle [[Botnet]], la Network Analysis permette di far collassare un'intera infrastruttura arrestando/rimuovendo il singolo nodo centrale.

## 📚 Contesto e Definizioni

Le metriche chiave (Centrality Measures) che l'algoritmo calcola:
*   **Degree Centrality:** Chi ha più contatti diretti? (Spesso il capo visibile o il recruiter).
*   **Betweenness Centrality (Intermediazione):** Chi è il "Ponte" tra due gruppi che altrimenti non si parlerebbero? (Es. il contrabbandiere di armi neutrale, vitale per il sistema).
*   **Closeness Centrality:** Chi può RAGgiungere tutti gli altri nel minor tempo possibile? (Il diffusore ideale di [[Disinformazione]]).

## 📊 Dati, Tecnologie e Metriche

Strumenti come [[Neo4j]] o Gephi mappano visivamente le transazioni in Criptovalute. Anche se i membri di un gruppo ransomware ([[Apt]]) usano portafogli multipli ([[Mixer]]) per oscurare il denaro, la Network Analysis studia la topologia temporale dei pagamenti, scoprendo che 500 portafogli apparentemente slegati riversano tutti il 10% di commissione su un singolo Nodo Silenzioso (il vero amministratore del cartello), smascherando l'intera gerarchia nascosta.

## 🔗 Connessioni e Pattern

- [[Neo4j]]
- [[Finint]]
- [[Botnet]]
- [[Disinformazione]]
- [[--]]
F/I/H
- [[--]]
