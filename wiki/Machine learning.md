---
title: "Machine learning"
tags: ["OSINT", "processed", "machine-learning", "ai", "algoritmi"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "3"
tipo: "concetto"
---

# Machine learning

## 🎯 Sintesi Strategica

Il **Machine Learning (ML)** è la sotto-disciplina dell'Intelligenza Artificiale che fornisce ai computer la capacità di apprendere e migliorare automaticamente dai dati e dall'esperienza, senza essere esplicitamente programmati con regole if-then. Nell'[[Osint]], il ML è il motore retrostante all'analisi massiva dei pattern: individua botnet tramite anomaly detection, classifica il sentiment di milioni di tweet o esegue il riconoscimento di target in enormi dataset SATellitari ([[Geoint]]).

## 📚 Contesto e Definizioni

Si suddivide in tre grandi paradigmi operativi:
1.  **SupervisioNATO:** L'algoritmo impara da un dataset etichettato dall'uomo (es. "Queste 100 foto contengono carri armati"). Una volta addestrato, classifica nuovi dati sconosciuti.
2.  **Non SupervisioNATO:** L'algoritmo esplora dati grezzi privi di etichette (es. transazioni finanziarie oscure) e li RAGgruppa in cluster (es. tramite l'algoritmo K-Means in [[KNIME]]), scovando anomalie o frodi invisibili all'uomo.
3.  **Reinforcement Learning:** Apprendimento per tentativi ed errori massimizzando una "ricompensa" (utilizzato per addestrare l'allineamento degli [[Llm]]).

## 📊 Dati, Tecnologie e Metriche

L'adozione del ML classico in intelligence richiede una severa mitigazione dei [[Bias cognitivo]]: se il dataset di addestramento è distorto (es. contiene prevalentemente dati su una specifica etnia), l'algoritmo automatizzerà e nasconderà quel pregiudizio dietro una patina di "oggettività matematica".

## 🔗 Connessioni e Pattern

- [[KNIME]]
- [[Intelligenza artificiale generativa]]
- [[Xai]]
- [[Algoritmi]]
- [[--]]
F/I/H
- [[--]]
