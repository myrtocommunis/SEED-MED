---
title: "[[RAG]]"
tags: ["OSINT", "processed", "[[RAG]]", "ai", "architettura"]
date: "2026-05-15"
status: "draft"
depth: "deep"
sources: "4"
tipo: "concetto"
---

# [[RAG]]

## 🎯 Sintesi Strategica

Il **[[RAG]] (Retrieval-Augmented Generation)** è un'architettura ibrida di intelligenza artificiale che risolve il problema delle allucinazioni e dei limiti di memoria ([[Context window]]) dei modelli linguistici ([[Llm]]). Nell'[[Osint]], il [[RAG]] è il Sacro Graal dell'automazione analitica: permette all'investigatore di interrogare privatamente un immenso archivio di documenti classificati o leakati (es. 50.000 pagine di chat Telegram), costringendo l'LLM a basare le sue risposte *esclusivamente* sui documenti forniti, citando la fonte esatta per ogni affermazione e garantendo la validità in sede legale.

## 📚 Contesto e Definizioni

Invece di affidarsi alla "conoscenza generale" pre-addestrata dell'LLM (che è obsoleta o inventata), il [[RAG]] si scompone in due fasi:
1.  **Retrieval (Recupero):** Quando l'analista pone una domanda, il sistema non interroga l'LLM, ma esegue una ricerca semantica in un [[Vector database]] per trovare i 5 paragrafi più rilevanti all'interno dell'archivio aziendale.
2.  **Generation (Generazione):** Il sistema inietta quei 5 paragrafi direttamente nel prompt dell'LLM, istruendolo: *"Rispondi alla domanda usando SOLO il testo qui sotto. Se la risposta non c'è, dichiara che non lo sai"*.

## 📊 Dati, Tecnologie e Metriche

Costruire un [[RAG]] OSINT sicuro richiede orchestrazione (es. [[LangChain]] o Llamaindex) ed esecuzione in locale per mantenere l'[[Opsec]]. 
La criticità tecnica risiede nel **Chunking**: i documenti lunghi devono essere tagliati in segmenti (Chunk) da circa 500-1000 token prima di essere vettorializzati tramite [[Embedding]]. Se il Chunking è configurato male, il [[RAG]] taglierà a metà le frasi cruciali, perdendo il contesto e fallendo il Retrieval.

## 🔗 Connessioni e Pattern

- [[Intelligenza artificiale generativa]]
- [[Llm]]
- [[Vector database]]
- [[Embedding]]
- [[Context window]]
- [[--]]
F/I/H
- [[--]]
