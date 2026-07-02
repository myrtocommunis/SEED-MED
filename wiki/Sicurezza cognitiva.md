---
title: Sicurezza cognitiva
tags:
- OSINT
- processed
- sicurezza-cognitiva
date: '2026-05-15'
status: draft
depth: standard
sources: '1'
tipo: concetto
---

# Sicurezza cognitiva

## 🎯 Sintesi Strategica

La Sicurezza Cognitiva è una disciplina emergente che si concentra sulla protezione dei processi cognitivi, sia umani che artificiali, dalla manipolazione, dal compromesso o dall'influenza malevola. Con l'avvento dell'[[Agenti]], che trasforma i [[Llm|Large language models]] da semplici generatori di testo ad attori autonomi capaci di percepire, RAGionare e agire (ciclo Percezione-Decisione-Azione), emergono nuove e complesse superfici di attacco. La Sicurezza Cognitiva mira a comprendere e mitigare le minacce che sfruttano queste capacità, in particolare quelle che rientrano nella [[Kill Chain Cognitiva]], per prevenire la compromissione dell'autonomia e dell'integrità dei sistemi.

## 📚 Contesto e Definizioni

L'evoluzione dell'[[Agenti]] è il risultato della convergenza di tre fattori chiave: il RAGgiungimento da parte degli LLM di capacità di RAGionamento e pianificazione sufficienti per l'autonomia, l'infrastruttura di API e tool-calling che permette agli agenti di interagire con l'ambiente esterno, e lo sviluppo di [[Sistemi Multi-Agente]] che stanno creando un "Web of Agents" in sostituzione del tradizionale "Web of Documents". In questo contesto, la Sicurezza Cognitiva si definisce come l'insieme di strategie, tecniche e contromisure volte a salvaguardare l'integrità dei processi decisionali e di RAGionamento, prevenendo attacchi che mirano a indurre errori, manipolare percezioni o alterare azioni autonome.

## 📊 Dati, Tecnologie e Metriche

La comprensione della Sicurezza Cognitiva si basa su diversi modelli e metriche operative:
*   **Ciclo Percezione-Decisione-Azione (P-D-A)**: Schema operativo universale che descrive il funzionamento di qualsiasi agente autonomo (Percezione → RAGionamento/Decisione → Azione → Feedback).
*   **Tre memorie degli agenti**:
    *   Episodica (context window): memoria a breve termine per il contesto immediato.
    *   Semantica ([[Knowledge Graph]]): memoria a lungo termine per la conoscenza strutturata.
    *   Vettoriale/[[RAG]] ([[Retrieval Augmented Generation]]) ([[Database vettoriali]]): memoria per il recupero di informazioni pertinenti.
*   **Quattro stadi della [[Kill Chain Cognitiva]]**:
    1.  Semantic Infection: Infiltrazione di informazioni fuorvianti o manipolate.
    2.  Cognitive Compromise: Alterazione dei processi di RAGionamento o decisione.
    3.  Agency Propagation: Diffusione del compromesso ad altri agenti o sistemi.
    4.  Systemic Execution: Esecuzione di azioni malevole su larga scala.
*   **[[Ai act]]**: Quadro normativo che classifica i sistemi AI in 4 classi di rischio (inaccettabile, alto rischio, limitato, minimo), fornendo un contesto per la valutazione delle minacce cognitive.
*   **RoboPAIR**: Caso studio reale che ha dimostrato la possibilità di bypassare i filtri di sicurezza di robot fisici, evidenziando vulnerabilità operative a livello cognitivo.

## 🔍 Analisi Operativa ed Applicazioni OSINT

Per gli analisti [[Osint]], la Sicurezza Cognitiva rappresenta un campo cruciale per identificare e mitigare le minacce emergenti. L'analisi operativa si concentra su:
*   **Identificazione delle Superfici di Attacco**: Ogni livello tecnico di un agente (token, embedding, [[RAG]] ([[Retrieval Augmented Generation]])) presenta una potenziale superficie di attacco che può essere sfruttata per la Semantic Infection. L'OSINT può mappare queste vulnerabilità.
*   **Monitoraggio della [[Kill Chain Cognitiva]]**: Gli analisti OSINT possono cercare indicatori di ciascuno dei quattro stadi, dalla diffusione di narrazioni manipolate (Semantic Infection) alla rilevazione di comportamenti anomali in sistemi autonomi (Systemic Execution).
*   **Valutazione delle Operazioni di Influenza**: Comprendere come gli attori malevoli possano tentare di indurre un Cognitive Compromise in sistemi AI o in gruppi umani attraverso la manipolazione informativa.
*   **Analisi di Casi Reali**: L'indagine su incidenti come RoboPAIR fornisce insight pratici su come le vulnerabilità cognitive possano essere sfruttate in scenari reali, permettendo agli analisti di sviluppare contromisure proattive.

## 🔮 Lacune Informative e Prossimi Passi

Per approfondire la Sicurezza Cognitiva, sono necessari ulteriori studi e sviluppi:
*   Analisi approfondita della letteratura accademica sul caso RoboPAIR.
*   Ricerca su [[Constitutional AI]] come potenziale contromisura al Cognitive Compromise.
*   Confronto tra i framework multi-agente esistenti (es. Autogen, [[CrewAI]], Langgraph) per valutarne le implicazioni sulla sicurezza cognitiva.
*   Sviluppo di metodologie per il testing della Semantic Infection tramite [[Prompt injection]] indiretta.

⚠️ **NOTA DI VERIFICA**: La data "marzo 2026" dell'analisi di Giorgio Piccardo è da confermare; il documento Pages originale è datato aprile 2026. Il caso RoboPAIR — per la sua rilevanza operativa — richiede verifica su letteratura accademica prima di essere citato in prodotti finali.

## 🔗 Connessioni e Pattern

- [[Applicazioni osint]]
- [[Llm|Large language models]]
- [[Manipolazione informativa]]
- [[Osint]]
- [[Pianificazione]]
- [[Prompt injection]]


- [[--]]
F/I/H
- [[--]]
