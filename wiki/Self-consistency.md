---
title: Self-consistency
tags:
- OSINT
- processed
- self-consistency
date: '2026-05-15'
status: draft
depth: standard
sources: '1'
tipo: concetto
---

# Self-consistency

## 🎯 Sintesi Strategica

La **Self-consistency** è una tecnica avanzata di [[Prompt engineering]] per i [[Llm|Large language models]] che estende il Chain of Thought (CoT). Il suo obiettivo è migliorare l'affidabilità e la robustezza delle risposte generate, specialmente in contesti complessi come l'[[Osint]]. Questo si ottiene generando multiple catene di RAGionamento indipendenti per lo stesso problema e selezionando la risposta più comune attraverso un meccanismo di voto di maggioranza.

## 📚 Contesto e Definizioni

I [[Llm|Large language models]], pur essendo potenti, generano il prossimo token probabilisticamente e non RAGionano causalmente in modo intrinseco. Questo può portare a salti logici, omissioni di passaggi intermedi e allucinazioni. La Self-consistency affronta queste limitazioni fornendo una struttura che permette al modello di "pensare" più attentamente e di validare le proprie inferenze.

Il principio fondamentale è che, sebbene percorsi di RAGionamento diversi possano commettere errori diversi, la risposta corretta tenderà ad apparire con maggiore frequenza tra le diverse iterazioni. Questo conferisce robustezza statistica all'output finale, trasformando un'inferenza probabilistica in un risultato più strutturato e verificabile.

## 📊 Dati, Tecnologie e Metriche

Il meccanismo della Self-consistency si articola in due fasi principali:
1.  **Generazione di Percorsi Multipli**: Si campionano *N* percorsi di RAGionamento indipendenti, ciascuno utilizzando la tecnica Chain of Thought (CoT). Per massimizzare la diversità dei percorsi, si imposta una temperatura non-zero nel campionamento del modello.
2.  **Voto di Maggioranza**: Una volta generati i *N* percorsi e le relative risposte finali, si identifica la conclusione che appare più frequentemente. Questa conclusione, supportata dalla maggioranza dei percorsi, viene selezionata come risposta definitiva.

**Parametri Operativi Chiave:**

| Parametro          | Valore Minimo | Valore Consigliato | Quando Aumentare                               |
| :----------------- | :------------ | :----------------- | :--------------------------------------------- |
| N (num. percorsi)  | 3             | 5-10               | Problemi critici, alto rischio operativo       |
| Temperature        | 0.7           | 0.8-0.9            | Per massimizzare la diversità dei RAGionamenti |
| Threshold accordo  | 60%           | 80%+               | Per decision-making operativo e alta confidenza |

L'efficacia della Self-consistency è dimostrata nel miglioramento delle performance dei [[Llm|Large language models]] su task complessi:

| Capacità                  | LLM Base | + CoT    | + Self-Consistency | + ToT    |
| :------------------------ | :------- | :------- | :----------------- | :------- |
| Math word problems        | 60-75%   | 85-90%   | 90-94%             | 92-96%   |
| Logical puzzles           | 40-55%   | 70-80%   | 78-85%             | 82-90%   |
| Multi-step planning       | 30-50%   | 55-72%   | 60-75%             | 68-82%   |
| Counterfactual reasoning  | 20-35%   | 45-60%   | 50-65%             | 58-75%   |

## 🔍 Analisi Operativa ed Applicazioni OSINT

Nel campo dell'[[Osint]], dove l'accuratezza del RAGionamento è critica per evitare falsi positivi con conseguenze operative reali, la Self-consistency offre un significativo vantaggio.

**Applicazioni OSINT della Self-consistency:**

| Scenario OSINT                | N Percorsi | Criticità | Output                                          |
| :---------------------------- | :--------- | :-------- | :---------------------------------------------- |
| Attribuzione stato-attore     | 10         | Alta      | Consenso >80% = attribuzione affidabile         |
| Classificazione threat level  | 5          | Media     | Maggioranza come classificazione finale         |
| Analisi sentiment multi-fonte | 3          | Bassa     | Triangolazione automatica del sentiment         |
| Valutazione affidabilità fonte | 5          | Alta      | Conflitto segnalato se <80% di accordo tra fonti |

Un esempio pratico consiste nel chiedere a un LLM di analizzare un problema verbale complesso, campionando poi 5 risposte Chain of Thought (CoT) separate. Se 3 risposte convergono su "42", mentre le altre due indicano "38" e "45", la Self-consistency identificherà "42" come la risposta più affidabile.

## 🔮 Lacune Informative e Prossimi Passi

Nonostante la sua efficacia, l'implementazione della Self-consistency presenta alcune aree di miglioramento e ricerca futura:
*   **Benchmark quantitativi reali**: Mancano benchmark specifici su dataset [[Osint]] per misurare l'effettivo miglioramento dell'accuratezza in task come l'attribuzione o la ricostruzione di timeline.
*   **Ottimizzazione costi**: La generazione di *N* percorsi di RAGionamento aumenta il costo computazionale. Sono necessarie strategie per ridurre questo onere, come la distillazione del modello o l'early stopping dei percorsi meno promettenti.
*   **Architetture ibride**: Esplorare combinazioni ottimali con altre tecniche di RAGionamento avanzato (es. React + Self-consistency o [[Tree of thoughts]] + Self-consistency) per creare framework di agenti [[Osint]] ancora più robusti.

## 🔗 Connessioni e Pattern

- [[Applicazioni osint]]
- [[Decision-making]]
- [[Llm|Large language models]]
- [[Osint]]
- [[Prompt engineering]]
- [[Tree of thoughts]]


- [[--]]
F/I/H
- [[--]]
