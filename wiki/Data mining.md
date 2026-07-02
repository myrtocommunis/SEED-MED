---
title: "Data mining"
tags: ["OSINT", "processed", "data-mining", "kdd", "pattern", "analisi"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "3"
tipo: "concetto"
---

# Data mining

## 🎯 Sintesi Strategica

Il **Data Mining** (Estrazione di dati) è il processo computazionale di analisi di insiemi di dati massivi (Big Data) volto a scoprire e identificare automaticamente pattern, anomalie, tendenze o relazioni non evidenti a livello macroscopico. È l'implementazione pratica del processo KDD (Knowledge Discovery in Databases). Nell'[[Osint]], trasforma la fase di [[Raccolta]] caotica del [[Data lake]] in logica ordinata propedeutica all'[[Analisi]] dell'intelligence.

## 📚 Contesto e Definizioni

Si differenzia dalla semplice "Ricerca" informatica:
*   Ricerca è: "Trovami tutte le transazioni di Mario Rossi in questo database bancario".
*   Data Mining è: "Dimmi quali clienti hanno comportamenti di spesa simili a Mario Rossi, e con quale probabilità commetteranno una frode nei prossimi sei mesi" (Analisi Predittiva).

## 📊 Dati, Tecnologie e Metriche

Sfrutta pesantemente il [[Machine learning]] e gli algoritmi di Clustering (RAGgruppare entità con attributi simili) e Classification. Nella [[Finint]] (Anti-Money Laundering), il Data Mining rileva anomalie statistiche: se un conto inattivo per 10 anni riceve improvvisamente 5.000 micro-transazioni da 1 euro da IP russi, l'algoritmo alza una "Red Flag" (Alerting) segnalando all'analista umano l'anomalia per una revisione, prevenendo così i [[Falso positivo]] generalizzati che distruggerebbero la produttività.

## 🔗 Connessioni e Pattern

- [[Machine learning]]
- [[Data lake]]
- [[Analisi]]
- [[Finint]]
- [[--]]
F/I/H
- [[--]]
