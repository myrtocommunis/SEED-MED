---
title: "Non supervisioNATO"
tags: ["OSINT", "processed", "machine-learning", "ai", "clustering", "anomaly-detection"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Non supervisioNATO

## 🎯 Sintesi Strategica

L'**Apprendimento Non SupervisioNATO (Unsupervised Learning)** è una branca del [[Machine learning]] in cui l'algoritmo viene addestrato su un dataset privo di etichette, categorizzazioni o risposte predefinite. A differenza dell'apprendimento supervisioNATO (in cui diciamo all'AI: "Queste 100 foto sono gatti, impara a riconoscerli"), nel Non SupervisioNATO l'AI viene abbandonata in un caotico [[Data lake]] con l'ordine: "Trova una struttura matematica o un pattern in questi dati da sola". 

## 📚 Contesto e Definizioni

Nell'[[Osint]] e nella [[Cybersecurity]], le sue applicazioni principe sono:
1.  **Clustering:** L'algoritmo RAGgruppa entità simili. Ad esempio, RAGgruppa milioni di account social in base al loro vocabolario, rivelando automaticamente una rete di falsi account ([[Botnet]]) usati per [[Disinformazione]], senza che l'analista sapesse a priori cosa cercare.
2.  **Rilevamento delle Anomalie (Anomaly Detection):** In ambito [[Blue team]], l'algoritmo studia per un mese il traffico di rete "normale" dell'azienda. Non sa cosa sia un virus, ma sa cos'è la "normalità". Se un dipendente si connette improvvisamente alle 4 di notte e scarica un Terabyte (comportamento anomalo), l'algoritmo lo blocca.

## 📊 Dati, Tecnologie e Metriche

Il limite operativo del modello non supervisioNATO è l'interpretabilità. L'AI RAGgrupperà perfettamente 500 file [[Malware]] in un cluster isolato, ma non saprà spiegare all'analista *perché* lo ha fatto. Sarà compito dell'intelligenza umana (Reverse Engineering) analizzare il cluster ed etichettarlo formalmente in un report di [[Cyber threat intelligence]].

## 🔗 Connessioni e Pattern

- [[Machine learning]]
- [[Data lake]]
- [[Cyber threat intelligence]]
- [[Botnet]]
- [[--]]
F/I/H
- [[--]]
