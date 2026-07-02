---
title: Cybersecurity stratificata
tags:
- OSINT
- processed
- cybersecurity-stratificata
date: '2026-05-15'
status: draft
depth: standard
sources: '1'
tipo: concetto
---

# Cybersecurity stratificata

## 🎯 Sintesi Strategica

La cybersecurity stratificata, nel contesto dei sistemi agentici e dell'[[Fondamenti di ai|Intelligenza Artificiale]] (IA), rappresenta un approccio difensivo multidimensionale volto a contrastare le minacce che emergono con il passaggio dal "Web of Documents" al Web of Agents. Questa evoluzione sposta la superficie d'attacco dal codice tradizionale al RAGionamento e ai processi cognitivi degli agenti autonomi. Il concetto si basa su un framework di minacce cognitive a quattro stadi (Semantic Infection, Cognitive Compromise, Agency Propagation, Systemic Execution) e propone contromisure stratificate sui medesimi livelli, dall'input dei token alla gestione del sistema multi-agente, garantendo una difesa robusta contro la manipolazione e la compromissione cognitiva.

## 📚 Contesto e Definizioni

La cybersecurity stratificata si definisce come l'applicazione di barriere difensive multiple e interconnesse per proteggere i sistemi basati su agenti IA da attacchi che mirano a manipolare il loro comportamento e RAGionamento. Questo approccio è cruciale per la sicurezza dei sistemi che interagiscono autonomamente con l'ambiente e altri agenti.

Il framework delle minacce cognitive, sviluppato da Piccardo, delinea una [[Kill Chain Cognitiva]] a quattro stadi:
1.  **Semantic Infection**: Iniezione di contenuti malevoli nei canali osservati dall'agente.
2.  **Cognitive Compromise**: Manipolazione del RAGionamento dell'agente, come il dirottamento degli obiettivi (goal hijacking) o l'inversione delle priorità.
3.  **Agency Propagation**: Un agente compromesso contamina altri agenti, facilitando il movimento laterale delle minacce.
4.  **Systemic Execution**: Azioni non autorizzate eseguite con i permessi dell'agente, con impatti reali sul sistema.

Le contromisure sono stratificate in modo corrispondente:
*   **L1 — Token/Input**: Difese a livello di singoli token o input.
*   **L2 — Modello**: Protezioni integrate nel modello di IA.
*   **L3 — Post-processing**: Validazione e filtraggio degli output del modello.
*   **L4 — Agente/Sistema**: Controlli a livello di singolo agente o dell'intero sistema multi-agente.

## 📊 Dati, Tecnologie e Metriche

La difesa stratificata si avvale di diverse tecnologie e tecniche:

*   **L1 — Token/Input**:
    *   **Difesa**: Sanitizzazione a livello di token (es. omoglifi, zero-width), Guardrails (es. Nemo Guardrails).
    *   **Minacce contrastate**: Token smuggling, glitch token.
    *   **Tecnologie**: Input sanitization, [[RAG]] provenance.
*   **L2 — Modello**:
    *   **Difesa**: [[Constitutional AI]], Reinforcement Learning from Human Feedback (RLHF), red-teaming, output filtering.
    *   **Minacce contrastate**: Indirect prompt injection, jailbreaking, AI poisoning.
    *   **Tecnologie**: Intent verification, refusal policy.
*   **L3 — Post-processing**:
    *   **Difesa**: Validazione dello schema, fact-checking tramite Natural Language Inference (NLI), document provenance, differential privacy.
    *   **Minacce contrastate**: Data leakage, esfiltrazione di PII (Personally Identifiable Information), allucinazioni nei riassunti.
    *   **Tecnologie**: Document signing, content classification.
*   **L4 — Agente/Sistema**:
    *   **Difesa**: Circuit breakers, scope limiter, audit logging, architettura zero-trust tra agenti.
    *   **Minacce contrastate**: Goal hijacking, priority inversion, agency propagation.
    *   **Tecnologie**: Trust boundaries, autenticazione agenti, lateral isolation, communication audit, privilege scoping, Human-in-the-loop su azioni critiche.

## 🔍 Analisi Operativa ed Applicazioni OSINT

L'applicazione della cybersecurity stratificata è fondamentale per gli agenti [[Osint]] (Open Source Intelligence), specialmente quelli che operano in contesti di Intelligenza Artificiale Fisica (Physical AI) come robot, droni o veicoli autonomi. Il caso RoboPAIR, che dimostra come la compromissione cognitiva possa bypassare i filtri di sicurezza di robot fisici, evidenzia che la sicurezza cognitiva non è un'opzione, ma un requisito di sicurezza ingegneristica.

Molti agenti OSINT aziendali, in base alla loro funzionalità, possono rientrare nella categoria di "alto rischio" secondo l'[[Ai act]]. Questo impone requisiti stringenti quali:
*   Trasparenza verso utenti e regolatori.
*   Documentazione esaustiva (data sheet, model card, dati di training).
*   Valutazione d'impatto prima del deployment.
*   [[Audit Trail]] completo a posteriori per tracciare le azioni e le decisioni dell'agente.

La "verosimiglianza operativa" è un rischio di base per gli agenti IA, dove le allucinazioni generate dai modelli di linguaggio possono portare a derive pericolose, rendendo indispensabile una difesa stratificata.

## 🔮 Lacune Informative e Prossimi Passi

Per approfondire la comprensione e l'applicazione della cybersecurity stratificata, sono necessari i seguenti passi:
*   Analisi approfondita del paper RoboPAIR per comprenderne l'origine e la replicabilità delle vulnerabilità.
*   Studio del metodo della [[Constitutional AI]] (Anthropic) come contromisura efficace al Cognitive Compromise.
*   Applicazione del pattern "Sandwich defense" a prompt OSINT reali per valutarne l'efficacia pratica.
*   Sviluppo di metodologie di red-teaming sistematico sulla [[Kill Chain Cognitiva]] per identificare nuove vulnerabilità.
*   Mappatura degli agenti aziendali esistenti contro il decision tree dell'EU AI Act (§3.4) per garantire la conformità normativa.

## 🔗 Connessioni e Pattern

- [[Applicazioni osint]]
- [[Framework delle minacce cognitive]]
- [[Human-in-the-loop]]
- [[Osint]]
- [[Prompt injection]]
- [[Sicurezza cognitiva]]


- [[--]]
F/I/H
- [[--]]
