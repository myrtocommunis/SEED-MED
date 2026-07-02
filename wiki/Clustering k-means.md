---
title: "Clustering k-means"
tags: ["OSINT", "processed", "clustering", "k-means", "machine-learning", "analisi"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Clustering k-means

## 🎯 Sintesi Strategica

Il **Clustering K-Means** è uno degli algoritmi più celebri e utilizzati nel [[Machine learning]] ad apprendimento [[Non supervisionato]]. Il suo scopo è suddividere automaticamente un enorme set di dati in un numero *K* di gruppi distinti (Cluster), in modo che i dati all'interno di ciascun gruppo siano il più simili possibile tra loro e il più diversi possibile dagli altri gruppi. Nell'[[Osint]], è lo strumento primario per trovare "l'ago nel pagliaio" quando l'analista non sa nemmeno che forma abbia l'ago.

## 📚 Contesto e Definizioni

Come funziona:
1. L'analista decide a priori quanti gruppi vuole trovare (es. K=3).
2. L'algoritmo posiziona 3 punti casuali (Centroidi) nello spazio dei dati.
3. Assegna ogni punto dati al centroide più vicino.
4. Ricalcola la posizione del centroide in base alla media dei punti assegnati, ripetendo il processo finché i gruppi non si stabilizzano.
Se applicato ai log di rete, RAGgrupperà automaticamente il "Traffico normale", il "Traffico notturno" e isolerà un piccolo cluster anomalo: "L'esfiltrazione dati dell'hacker".

## 📊 Dati, Tecnologie e Metriche

Nelle indagini di [[Cyber threat intelligence]], il K-Means si usa per classificare le famiglie di [[Malware]]. Estratti milioni di frammenti di codice virale, il K-Means RAGgruppa matematicamente i virus scritti dallo stesso autore o gruppo criminale ([[Apt]]), anche se sono leggermente diversi, perché l'algoritmo riconosce la "firma statistica" o lo stile di programmazione sottostante.

## 🔗 Connessioni e Pattern

- [[Non supervisionato]]
- [[Machine learning]]
- [[Cyber threat intelligence]]
- [[Fondamenti matematici]]
- [[--]]
F/I/H
- [[--]]
