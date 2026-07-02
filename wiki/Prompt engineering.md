---
title: "Prompt engineering"
tags: ["OSINT", "processed", "ai", "prompting", "llm"]
date: "2026-05-15"
status: "draft"
depth: "deep"
sources: "6"
tipo: "concetto"
---

# Prompt engineering

## 🎯 Sintesi Strategica

Il **Prompt Engineering** è la disciplina metodologica che struttura l'interazione tra l'analista umano e un Large Language Model (LLM). Nell'ambito [[Osint]], non si tratta di una semplice "scrittura di comandi", ma di una vera e propria programmazione in linguaggio naturale (NPL) volta a massimizzare l'estrazione di *Intelligence* da dati non strutturati, riducendo drasticamente i tassi di allucinazione. Un prompt mal calibrato produce risposte prolisse e inaffidabili; un prompt ingegnerizzato trasforma l'AI in un *Agente* capace di eseguire complesse [[Tecniche di analisi strutturata]] in modo deterministico.

## 📚 Contesto e Definizioni

Le tecniche di prompting per l'analisi avanzata si dividono per complessità:
1.  **Zero-Shot Prompting:** Richiesta diretta senza fornire esempi (altamente prono a errori in compiti logici).
2.  **Few-Shot Prompting:** Fornire all'LLM 3-5 esempi di "Input $\rightarrow$ Output" desiderati prima della vera richiesta. Questo "ancora" il modello al pattern formale e logico richiesto dall'analista.
3.  **Chain of Thought (CoT):** Obbligare il modello a "RAGionare passo dopo passo" (*Think step by step*). Esplicitando il processo logico, il modello distribuisce il calcolo statistico su più token, abbattendo gli errori di RAGionamento.

## 📊 Dati, Tecnologie e Metriche

Il *Framework Tattico* di un prompt investigativo professionale si compone obbligatoriamente di quattro layer (Modello PTFC):
*   **Persona:** L'assegnazione di un ruolo ("Agisci come un analista di Cyber Threat Intelligence senior..."). Costringe il modello a pescare i token dai vettori semantici più tecnici.
*   **Task:** L'obiettivo preciso ("Estrai tutte le entità geopolitiche e formattale in JSON").
*   **Format/Constraints:** Regole non negoziabili ("Non aggiungere testo discorsivo. Non allucinare dati assenti nel testo originario").
*   **Context:** Il testo grezzo raccolto dall'analista (il payload OSINT).

## 🔍 Analisi Operativa ed Applicazioni OSINT

L'evoluzione del Prompting in OSINT si sta muovendo verso i **Reasoning Patterns** avanzati:
*   **Tree of Thoughts (ToT):** Costringere il modello a esplorare percorsi decisionali multipli e paralleli prima di rispondere, imitando metodologie umane come l'[[Ach]] (Analysis of Competing Hypotheses).
*   **Reflexion (Self-Correction):** Un ciclo in cui il modello genera una risposta, la valuta criticamente ("Trova i bias logici in ciò che hai appena scritto"), e la corregge prima di consegnare l'output finale.

## 🔮 Lacune Informative e Prossimi Passi

*   **FRAGilità Sintattica (Prompt Drift):** Un prompt perfetto per GPT-4 oggi potrebbe produrre spazzatura su GPT-4.5 domani. I modelli vengono continuamente ri-addestrati e allineati dalle aziende produttrici (RLHF), rendendo i prompt altamente deperibili e richiedendo un *versioning* continuo come se fossero codice software.

## 🔗 Connessioni e Pattern

- [[Intelligenza artificiale generativa]]
- [[Vulnerabilità llm]]
- [[Jailbreaking]]
- [[Automazione]]
- [[Llm]]

- [[--]]
F/I/H
- [[--]]
