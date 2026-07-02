---
title: "Context engineering"
tags: ["OSINT", "processed", "ai", "prompting", "llm", "intelligence"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Context engineering

## 🎯 Sintesi Strategica

Il **Context Engineering (Ingegneria del Contesto)** è la disciplina critica di progettare, strutturare e ottimizzare le informazioni di background (il Prompt o la finestra di contesto) fornite a un [[Llm]] prima che generi una risposta. A differenza del semplice "Prompting" (fare una domanda a ChatGPT), il Context Engineering in ambito [[Osint]] è la vera garanzia di affidabilità: costringe l'Intelligenza Artificiale ad ancorarsi esclusivamente ai documenti investigativi forniti, azzerando le allucinazioni.

## 📚 Contesto e Definizioni

In un'architettura di [[Retrieval-augmented generation]] ([[RAG]]), l'analista non chiede all'AI: "Fai un riassunto delle attività terroristiche in Mali".
Attraverso il Context Engineering, l'analista costruisce un input strutturato:
1.  **Ruolo:** "Agisci come analista di [[Geopolitica]] del [[Dis]]."
2.  **Contesto (Il vero e proprio Payload):** [Iniezione di 50 report ACLED freschi recuperati tramite [[Api]]].
3.  **Vincolo (Constraint):** "Basati **esclusivamente** sui report allegati. Se un dato non è presente, rispondi 'Non disponibile'."

## 📊 Dati, Tecnologie e Metriche

L'uso offensivo è devastante. I gruppi [[Apt]] utilizzano il Context Engineering per industrializzare le frodi: iniettano nel contesto di un LLM le email rubate di un CEO e chiedono all'AI di "clonare esattamente il suo stile di scrittura, il suo lessico aziendale e la sua aggressività" per generare un [[Attacco di phishing]] iper-personalizzato, indistinguibile da un'email reale per il dipendente che la riceve.

## 🔗 Connessioni e Pattern

- [[Llm]]
- [[Retrieval-augmented generation]]
- [[Attacco di phishing]]
- [[Api]]
- [[--]]
F/I/H
- [[--]]
