---
title: "Vector database"
tags: ["OSINT", "processed", "vector-database", "embedding", "[[RAG]]"]
date: "2026-05-15"
status: "draft"
depth: "deep"
sources: "3"
tipo: "concetto"
---

# Vector database

## 🎯 Sintesi Strategica

Il **Vector Database (Database Vettoriale)** è una struttura di archiviazione dati specializzata che permette ai motori di intelligenza artificiale di eseguire ricerche per *significato semantico* e non per corrispondenza esatta di parole chiave (Keyword match). Nella pipeline [[Osint]] moderna, è il cuore pulsante delle architetture [[Rag]]: ospita l'intera base di conoscenza investigativa tradotta nel linguaggio matematico delle macchine ([[Embedding]]), consentendo ricerche impossibili per i database relazionali SQL tradizionali.

## 📚 Contesto e Definizioni

Mentre un database SQL memorizza i dati in righe e colonne, il Vector Database memorizza array di numeri ad alta dimensionalità (vettori).
*   Se un analista cerca "Veicolo blindato", un database SQL fallirà se il documento contiene solo la parola "Carro armato". 
*   Il Vector Database (es. ChromaDB, Pinecone, Milvus) calcola la vicinanza geometrica (Cosine Similarity) tra il vettore della parola "Veicolo blindato" e quello di "Carro armato", comprendendo che i concetti sono vicini nello spazio semantico e restituendo il documento corretto.

## 📊 Dati, Tecnologie e Metriche

Per garantire l'[[Opsec]] in operazioni di polizia o intelligence governativa, l'uso di Vector Database in cloud (come Pinecone) è sconsigliato a causa dell'esposizione del know-how investigativo. Si privilegiano implementazioni *Self-Hosted* open-source (come Qdrant o ChromaDB) eseguibili su [[Macchina virtuale]] isolata, integrati direttamente nei nodi di [[n8n]].

## 🔗 Connessioni e Pattern

- [[Rag]]
- [[Embedding]]
- [[Llm]]
- [[Data warehouse]]
- [[--]]
F/I/H
- [[--]]
