---
title: "Context window"
tags: ["OSINT", "processed", "llm", "context-window", "memoria"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Context window

## 🎯 Sintesi Strategica

La **Context Window (Finestra di Contesto)** rappresenta il limite biologico-computazionale primario di qualsiasi [[Intelligenza artificiale generativa]]. Nell'architettura degli [[Llm]], definisce la quantità massima di token (unità semantiche equivalenti a frazioni di parola) che il modello può "mantenere in memoria attiva" ed elaborare contemporaneamente in un singolo *prompt*. Per l'analista [[Osint]], questo parametro è il collo di bottiglia fondamentale: stabilisce quanto sia grande il fascicolo investigativo, la conversazione Telegram o il dump di file PDF che può essere fornito all'AI per un'analisi di sintesi prima che il sistema inizi a "dimenticare" i frammenti più vecchi.

## 📚 Contesto e Definizioni

La Context Window opera come la RAM (Random Access Memory) temporanea del cervello dell'LLM:
1.  **Dimensione misurata in Token:** Si calcola sommando i token in ingresso (il prompt dell'utente + i documenti in allegato) con i token generati in uscita dalla risposta. Ad esempio, una finestra di 128.000 token può digerire approssimativamente un libro di 300 pagine.
2.  **Amnesia Temporanea:** Se il totale dell'input e dell'output supera il limite architetturale del modello (es. inserisco un testo da 130k in un modello da 128k), l'LLM "cancella" le prime porzioni del prompt, provocando allucinazioni, fallimenti logici o disallineamenti nelle istruzioni operative (es. l'Agente OSINT dimentica l'istruzione di formattare in JSON data 10 pagine prima).

## 📊 Dati, Tecnologie e Metriche

L'evoluzione tecnologica è una brutale corsa all'allargamento della finestra:
*   I vecchi modelli (es. GPT-3) avevano finestre di 4.000 token (~3000 parole).
*   L'attuale panorama commerciale (es. Claude 3.5, Gemini 1.5 Pro) spinge le finestre oltre 1 Milione o 2 Milioni di token, permettendo l'ingestione analitica di interi codici penali o archivi di indagini di mesi.

Tuttavia, l'efficienza non è lineare ma soffre del **Fenomeno "Lost in the Middle" (Perso nel Mezzo)**:
*   Gli studi dimostrano che, pur accettando 100.000 token, l'LLM presta una soglia di *Attention* elevatissima all'inizio del documento (Primacy Bias) e alla fine (Recency Bias). Le informazioni incastrate esattamente nel centro del documento subiscono un massiccio calo di recall, rendendo il modello inaffidabile per il ritrovamento di aghi nel pagliaio (*Needle in a Haystack testing*).

## 🔍 Analisi Operativa ed Applicazioni OSINT

L'analista combatte i limiti della Context Window tramite architetture di pre-processamento:
*   **Architettura [[RAG]] (Retrieval-Augmented Generation):** Invece di "forzare" tutti i 10.000 file del caso dentro la Context Window, si utilizza un database di [[Embedding]]. Il sistema cerca matematicamente solo i 5 frammenti più rilevanti e passa *soltanto quelli* nella limitata finestra dell'LLM, azzerando il rischio di *Lost in the Middle*.
*   **Chunking (Frammentazione):** Nelle pipeline di [[Automazione]], i mega-documenti vengono tagliati preventivamente in "Chunk" sovrapponibili di 500-1000 token per essere processati in parallelo da cloni dell'agente LLM, e i risultati finali vengono ricompilati al termine dell'operazione.

## 🔮 Lacune Informative e Prossimi Passi

*   **Costi di Inferenza:** Finestre di contesto massicce non sono gratuite. I costi operativi API si calcolano per token processato. Inserire 1 milione di token per chiedere a un modello di estrarre un nome consuma risorse finanziarie che sfondano rapidamente i budget delle unità di indagine OSINT medio-piccole.

## 🔗 Connessioni e Pattern

- [[Llm]]
- [[Intelligenza artificiale generativa]]
- [[Embedding]]
- [[Prompt engineering]]
- [[Automazione]]

- [[--]]
F/I/H
- [[--]]
