---
title: Agenti ai
tags:
- OSINT
- processed
- agenti-ai
date: '2026-05-15'
status: draft
depth: standard
sources: '2'
tipo: concetto
---

# Agenti ai

## 🎯 Sintesi Strategica

Gli Agenti AI rappresentano un'evoluzione degli [[Llm|Large language models]], dotati di autonomia, capacità di RAGionamento flessibile e integrazione con strumenti esterni. Operano attraverso un ciclo continuo di percezione, decisione e azione, adattandosi al contesto e perseguendo obiettivi complessi. Nel contesto OSINT, trasformano gli LLM da semplici assistenti a entità proattive, capaci di automatizzare fasi investigative, dalla raccolta dati alla correlazione e verifica. La loro efficacia dipende dalla qualità delle istruzioni (prompt) e dalla capacità di interagire con l'ambiente esterno. Tuttavia, introducono nuove sfide in termini di [[Sicurezza cognitiva]] e governance, richiedendo un'attenta supervisione e l'applicazione di normative come l'EU AI Act.

## 📚 Contesto e Definizioni

Un Agente AI è un sistema che combina un [[Large language model]] con istruzioni operative, strumenti esterni e un ciclo decisionale autonomo. A differenza di un semplice "bot" che esegue chiamate dirette e reattive all'LLM, un agente è proattivo e orientato al RAGgiungimento di un obiettivo complesso attraverso una sequenza di azioni.

*   **Agente Classico vs. Agente AI**:
    | Dimensione | Classico | AI |
    |---|---|---|
    | RAGionamento | Regole fisse | LLM flessibile |
    | Adattamento | Nessuno | Dal contesto |
    | Orientamento | Reattivo | Proattivo |
    | Strumenti | Codice scritto | API, browser, DB, file |
    | Autonomia | Bassa, prevedibile | Alta, non deterministica |

*   **Ciclo Agente AI**: Si articola in Percezione, Decisione (mediata dall'LLM) e Azione. L'output di ogni iterazione diventa l'input per la successiva, in un processo continuo fino al completamento del task o all'intervento umano.

*   **Memoria Agente AI**:
    *   **Episodica**: Cronologia della sessione corrente.
    *   **Semantica**: Fatti, regole e sintesi di conoscenza a lungo termine.
    *   **Archivi Vettoriali ([[Retrieval-augmented generation]])**: Indicizzazione vettoriale per la ricerca di similarità semantica su corpora estesi, superando i limiti della context window dell'LLM.

*   **Generazione autoregressiva**: Il processo in cui l'LLM genera testo token per token, utilizzando l'output precedente come input per predire il token successivo, fino a un token di fine sequenza.

## 📊 Dati, Tecnologie e Metriche

*   **Componenti**: Gli Agenti AI integrano [[Llm|Large language models]] con una varietà di strumenti esterni, tra cui API, browser web, database e sistemi di gestione file, consentendo loro di interagire con l'ambiente digitale.
*   **[[Retrieval-augmented generation]]**: Tecnologia fondamentale che permette agli agenti di accedere e RAGionare su informazioni esterne alla loro conoscenza pre-addestrata. Documenti vengono trasformati in embeddings, archiviati in un database vettoriale, e recuperati semanticamente per arricchire il contesto dell'LLM prima della generazione.
*   **Orchestrazione**: Piattaforme come [[Langflow]] offrono un ambiente low-code per la progettazione e l'orchestrazione di workflow basati su GenAI e agenti, facilitando l'integrazione di diversi nodi (input, LLM, output, strumenti).
*   **[[Sistemi Multi-Agente]]**: Architetture complesse che prevedono un "supervisor" che coordina più agenti specializzati, ciascuno con un ruolo specifico, per affrontare task più ampi e articolati in parallelo.
*   **Regolamentazione (EU AI Act)**: Classifica gli agenti che influenzano decisioni su persone come "alto rischio". Impone requisiti stringenti come la presenza di un [[Human-in-the-loop]], [[Audit Trail]], test per i bias e la documentazione chiara dei confini decisionali. Le sanzioni per non conformità possono RAGgiungere il 7% del fatturato globale.

## 🔍 Analisi Operativa ed Applicazioni OSINT

*   **LLM come Assistente Investigativo Focalizzato**: La potenza investigativa di un LLM, quando integrato in un agente, deriva dalla qualità dei prompt strutturati, che lo trasformano in un assistente specializzato capace di eseguire codice in ambienti sandboxed o interagire con strumenti esterni.
*   **Pipeline OSINT Assistita da LLM (5 Fasi)**:
    1.  **Raccolta**: Generazione di query mirate (es. Google Dorks, multilingua, Shodan).
    2.  **Estrazione**: Structured Data Extraction per ottenere JSON con entità, date, relazioni e confidence score.
    3.  **Correlazione**: Identificazione di connessioni tra entità, con il [[Human-in-the-loop]] come componente obbligatoria per la validazione.
    4.  **Verifica**: Implementazione di una Chain of Verification.
    5.  **Report**: Generazione di report strutturati secondo un Template Pattern standardizzato.
*   **Tecniche Operative**:
    *   **T1**: Generazione di query OSINT avanzate.
    *   **T2**: Structured Data Extraction tramite diverse tecniche di prompt.
    *   **T3/T4**: Anomaly Detection su fonti specifiche come visure camerali o profili Linkedin.
*   **Agente OSINT con [[Motori di ricerca|SearXNG]]**: Esempio di applicazione in cui un agente utilizza un metamotore privacy-oriented per condurre ricerche open-source su entità di interesse, strutturando i metadati estratti.
*   **System message design**: La progettazione accurata dei messaggi di sistema è cruciale per definire il ruolo, il tono, i vincoli e lo stile dell'agente, influenzando direttamente la sua efficacia e sicurezza operativa.

## 🔮 Lacune Informative e Prossimi Passi

*   **Limiti Intrinseci degli LLM**: Gli LLM alla base degli agenti presentano limiti quali una conoscenza fissa (al momento del pre-training), l'assenza di accesso nativo all'esterno (superato parzialmente con strumenti e [[RAG]]), la statelessness (mitigata dalla memoria episodica) e il non determinismo.
*   **[[Sicurezza cognitiva]]**: Rappresenta una nuova superficie d'attacco. Le sfide includono:
    1.  **Superfici d'attacco cognitive**: Payload semantici che bypassano le validazioni tradizionali.
    2.  **Dissoluzione catene di fiducia**: Compromissione della fiducia tra entità (Machine-to-Person, Agent-to-Agent).
    3.  **Autonomia emergente**: Sequenze multi-step non previste o non visibili.
*   **Framework di Attacco (4 Fasi)**: Semantic Infection → Cognitive Compromise → Agency Propagation → Systemic Execution.
*   **Vettori di Attacco Specifici**:
    *   [[Prompt injection]]: Payload nascosti in fonti esterne che l'agente elabora.
    *   [[Poisoning]]: Inserimento di documenti falsi o manipolati nella knowledge base utilizzata per il [[Retrieval-augmented generation]].
*   **Paradigmi di Difesa**:
    *   **Context Auditing**: Verifica dell'integrità degli input.
    *   **Intent Verification**: Coerenza tra l'intento dell'agente e le sue azioni.
    *   **Circuit Breakers**: Meccanismi per limitare l'impatto di una compromissione.
*   **Privacy e Governance**: L'uso di agenti con accesso a strumenti esterni (web, API) richiede ambienti sandbox e audit rigorosi. I dati inviati a provider LLM esterni, spesso extra-europei, sollevano questioni di sovranità e protezione dei dati. I "guardrail" riducono ma non eliminano il rischio di contenuti dannosi o jailbreak. La verifica dei workflow no-code è essenziale prima dell'uso operativo.

## 🔗 Connessioni e Pattern

- [[Database vettoriale]]
- [[Human-in-the-loop]]
- [[Langflow]]
- [[Large language model]]
- [[Llm|Large language models]]
- [[Retrieval-augmented generation]]


- [[--]]
F/I/H
- [[--]]
