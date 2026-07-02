---
title: "Llm"
tags: ["OSINT", "processed", "llm", "ai", "machine-learning", "automazione"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Llm

## 🎯 Sintesi Strategica

I **LLM (Large Language Models)**, come GPT-4 o Claude, sono sistemi di intelligenza artificiale basati su reti neurali ad architettura Transformer, addestrati su corpus di testo colossali estratti dal Web. Nell'[[Osint]], l'avvento dei LLM segna il passaggio dall'era della "Ricerca per Parole Chiave" all'era della "Ricerca Semantica Computazionale". Permettono di riassumere, tradurre ed estrarre entità ([[Data mining]]) da migliaia di documenti non strutturati in pochi secondi.

## 📚 Contesto e Definizioni

A differenza di un database relazionale, un LLM non "cerca" un dato salvato, ma calcola la probabilità statistica della parola successiva in una frase. Questo meccanismo probabilistico genera il problema delle **Allucinazioni**: il modello, se interrogato su un bersaglio di nicchia, può inventare dati biografici estremamente plausibili ma del tutto falsi (es. attribuire falsi crimini a una persona). Pertanto, un LLM non può *mai* essere usato come fonte autorevole, ma solo come motore di processamento per dati forniti dall'analista (vedi architettura [[Retrieval-augmented generation]]).

## 📊 Dati, Tecnologie e Metriche

Dal punto di vista offensivo, i LLM hanno abbattuto la barriera d'ingresso per il cybercrimine. I criminali usano LLM "Jailbroken" (privi di filtri etici, come FraudGPT sul [[Dark web]]) per generare campagne di [[Attacco di phishing]] perfette, prive di errori grammaticali in qualsiasi lingua, e per scrivere [[Malware]] polimorfici, accelerando vertiginosamente il ciclo della [[Cyber kill chain]].

## 🔗 Connessioni e Pattern

- [[Fondamenti di ai|Intelligenza artificiale]]
- [[Attacco di phishing]]
- [[Data mining]]
- [[Retrieval-augmented generation]]
- [[--]]
F/I/H
- [[--]]
