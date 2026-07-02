---
title: "Tree of thoughts"
tags: ["OSINT", "processed", "tot", "llm", "ai", "prompting", "logica"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Tree of thoughts

## 🎯 Sintesi Strategica

Il **Tree of Thoughts (ToT - Albero dei PENSieri)** è una tecnica avanzata di interazione e [[Context engineering]] progettata per massimizzare le capacità di RAGionamento logico dei [[Llm|Large language models]] (LLM). Supera la tecnica lineare del "Chain of Thought" permettendo all'intelligenza artificiale di esplorare simultaneamente rami multipli di RAGionamento, valutare le diverse ipotesi, compiere marce indietro (Backtracking) su deduzioni errate e convergere verso la soluzione analitica ottimale, replicando il framework metodologico umano dell'[[Analysis of competing hypotheses]].

## 📚 Contesto e Definizioni

In uno scenario [[Osint]] complesso: "Identifica se il politico X è stato corrotto dall'entità Y basandoti su questi 50 documenti frammentari".
Invece di chiedere all'LLM una singola risposta immediata (Zero-Shot) che rischia la produzione di [[Allucinazioni]], il prompt ToT struttura il processo:
1. Genera 3 ipotesi iniziali distinte sul flusso di denaro.
2. Per ogni ipotesi, valuta l'evidenza documentale pro e contro.
3. Assegna un punteggio di verosimiglianza a ogni ramo.
4. Scarta i rami incompatibili con la cronologia e prosegui l'indagine sul ramo vincente.

## 📊 Dati, Tecnologie e Metriche

L'integrazione del Tree of Thoughts nei sistemi automatizzati di [[Workflow ai]] trasforma gli LLM da semplici riassuntori di testo in veri e propri assistenti analitici. Costringendo matematicamente il modello a giustificare ogni step logico intermedio lungo l'albero decisionale, le agenzie governative aumentano l'affidabilità dell'output e garantiscono un grado superiore di [[Trasparenza ai nella intelligence community]].

## 🔗 Connessioni e Pattern

- [[Llm|Large language models]]
- [[Context engineering]]
- [[Analysis of competing hypotheses]]
- [[Workflow ai]]
- [[--]]
F/I/H
- [[--]]
