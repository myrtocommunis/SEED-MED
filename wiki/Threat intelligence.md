---
title: Threat intelligence
tags:
- OSINT
- processed
- threat-intelligence
date: '2026-05-15'
status: draft
depth: standard
sources: '1'
tipo: concetto
---

# Threat intelligence

## 🎯 Sintesi Strategica

La **Threat Intelligence (TI)** è un processo basato sull'evidenza che trasforma dati grezzi sulle minacce in informazioni contestualizzate, rilevanti e azionabili. Il suo obiettivo primario è fornire una comprensione approfondita del panorama delle minacce, inclusi attori, motivazioni, capacità e tattiche, tecniche e procedure (TTP), per supportare decisioni strategiche, tattiche e operative in Sicurezza Informatica.

Con l'emergere dell'[[Fondamenti di ai|Intelligenza Artificiale]] agentica, la Threat Intelligence affronta un cambio di paradigma significativo. La superficie d'attacco si sposta dalle tradizionali Vulnerabilità nel codice o nella rete a quelle nel *RAGionamento* e nel *contesto* degli agenti autonomi. Questo richiede un'evoluzione dei framework di TI per includere l'analisi delle infezioni semantiche, del compromesso cognitivo e della propagazione tra agenti, rendendo la comprensione delle minacce AI-driven un pilastro fondamentale della moderna [[Cyber threat intelligence]].

## 📚 Contesto e Definizioni

La Threat Intelligence si definisce come la conoscenza basata su prove, inclusi il contesto, i meccanismi, gli indicatori, le implicazioni e i consigli azionabili, su una minaccia esistente o emergente per le risorse che può essere utilizzata per informare le decisioni relative alla risposta alla minaccia. Tradizionalmente, la TI si concentra su attacchi a sistemi basati su codice e rete.

Tuttavia, con l'avvento del "Web of Agents", dove gli agenti autonomi basati su [[Llm|Large language models]] (LLM) prendono decisioni ed eseguono azioni, i framework di Threat Intelligence tradizionali mostrano lacune significative. Le nuove sfide includono:

| Sfida Tradizionale | Nuovo Vettore Agentic | Impatto |
|:-------------------|:----------------------|:--------|
| Vulnerabilità nel codice | Vulnerabilità nel RAGionamento | Zero-day semantici |
| Lateral movement di rete | Propagazione relazionale tra agenti | Contaminazione a catena |
| Exploit di sistema | Manipolazione cognitiva | Azioni "legittime" ma dannose |
| Credential stuffing | Credential harvesting automatico | Nessun brute-force necessario |
| Privilege escalation | Goal hijacking | Permessi completi, mai sospetti |

Per affrontare queste nuove minacce, la Threat Intelligence si estende a un **Framework Cognitivo in Quattro Fasi di Attacco**, che descrive come gli agenti AI possono essere compromessi:

1.  **Semantic Infection (Observe)**: Iniezione di payload semantici nei canali di input dell'agente (es. [[Prompt engineering]] malevolo, [[RAG]] Poisoning).
2.  **Cognitive Compromise (Orient/Decide)**: Manipolazione del RAGionamento dell'agente, deviandone gli obiettivi o la logica.
3.  **Agency Propagation (Act)**: Propagazione laterale della compromissione attraverso protocolli Agent-to-Agent (A2A).
4.  **Systemic Execution (Impact)**: Realizzazione degli effetti concreti nel mondo reale tramite azioni legittime dell'agente.

I vettori di attacco specifici monitorati dalla TI in questo contesto includono:
*   **Goal Hijacking**: L'agente adotta un nuovo obiettivo introdotto dall'attaccante.
*   **Reasoning Chain Manipulation**: Introduzione di premesse o logiche che portano a conclusioni errate.
*   **Priority Inversion**: Alterazione della gerarchia delle priorità dell'agente per far sembrare urgenti azioni malevole.

## 📊 Dati, Tecnologie e Metriche

La Threat Intelligence nel dominio AI agentica si avvale di nuove tecnologie e metriche per rilevare e mitigare le minacce. I dati analizzati includono messaggi utente, API, file, sensor data, prompt, contesto, memoria (episodica, semantica, vector DB) e chiamate a tool esterni.

Tre paradigmi di sicurezza cognitiva sono fondamentali per la raccolta e l'analisi della TI:

1.  **Context Auditing**: Verifica l'integrità semantica degli input prima che entrino nel contesto dell'agente.
    *   *Tecniche*: Semantic Integrity Verification, Provenance Tracking, Content Anomaly Detection.
    *   *Metriche*: Anomalie rilevate/1000 token, Coverage % fonti verificate, False positive rate.
2.  **Intent Verification**: Monitora la coerenza tra gli obiettivi dichiarati dell'agente e le azioni che sta per compiere.
    *   *Controlli*: Goal Consistency Check, Action-Intent Alignment, Behavioral Anomaly Flag.
    *   *Metriche*: Zero un-flagged hijacking, <1% reasoning errors.
3.  **Circuit Breakers**: Meccanismi che limitano l'impatto anche a fronte di una compromissione dell'agente.
    *   *Meccanismi*: Execution Throttling, Scope Limitation, Human Escalation Trigger, Kill Switch.
    *   *Metriche*: Zero false urgency, Zero contamination propagation, Zero credential exposure.

La matrice seguente illustra la relazione tra vettori di attacco, difese primarie e metriche di successo:

| Vettore di Attacco | Difesa Primaria | Contromisura Secondaria | Metrica di Successo |
|:-------------------|:----------------|:------------------------|:--------------------|
| Indirect Prompt Injection | Context Auditing | Content provenance | >95% payload rilevati |
| [[RAG]] Poisoning | Context Auditing | Source integrity check | >90% poisoned docs filtered |
| Goal Hijacking | Intent Verification | Goal consistency monitoring | Zero un-flagged hijacking |
| Reasoning Chain Manipulation | Intent Verification | Logic chain validation | <1% reasoning errors |
| Priority Inversion | Circuit Breakers | Priority integrity checks | Zero false urgency |
| Cross-Agent Contamination | Circuit Breakers | A2A trust verification | Zero contamination propagation |
| Credential Harvesting | Circuit Breakers + Scope | Credential rotation limits | Zero credential exposure |

## 🔍 Analisi Operativa ed Applicazioni OSINT

La Threat Intelligence, in particolare quella derivata dall'[[Osint]], è cruciale per comprendere e contrastare le minacce emergenti nel panorama AI. L'analisi operativa si concentra sull'identificazione di TTP, attori e impatti reali.

**Incidenti Reali come Casi di Studio per la TI:**
*   **GTG-1002 (Novembre 2025)**: La prima campagna di cyber-spionaggio orchestrata quasi interamente da un agente AI. Questo incidente ha confermato la minaccia degli agenti autonomi operativi e ha fornito dati preziosi sulle TTP AI-driven, con l'AI che ha condotto autonomamente l'80-90% dell'attacco contro 30 organizzazioni globali.
*   **Moltbook (Gennaio 2026)**: La compromissione di un social network di agenti AI, con oltre 1,6 milioni di account agente e 1,5 milioni di API key esposte. Questo evento ha dimostrato la realtà della propagazione agentica e la prima osservazione di prompt injection bot-to-bot.

Questi incidenti evidenziano la necessità per l'[[Osint]] di monitorare non solo le attività umane ma anche quelle generate e propagate dagli agenti AI, analizzando i loro comportamenti, le interazioni A2A e le tracce digitali lasciate dalle loro azioni.

**Strumenti Operativi Derivati dalla TI:**
I principi della Threat Intelligence informano lo sviluppo di strumenti di sicurezza per gli agenti AI, come:
*   **Template di Security Assessment per Agenti**: Valuta i canali di input, la coerenza degli obiettivi, le violazioni di scope e le azioni che richiedono approvazione umana.
*   **Template di Prompt Difensivo (Hardened System Prompt)**: Istruzioni di sicurezza incorporate direttamente nel prompt dell'agente per imporre verifiche di integrità, gestione delle anomalie e requisiti di human-in-the-loop.

## 🔮 Lacune Informative e Prossimi Passi

Nonostante i progressi, la Threat Intelligence nel campo dell'AI agentica presenta ancora diverse lacune informative e aree di sviluppo:
*   **Framework di testing quantitativo**: Mancano metodologie standardizzate per il penetration testing e il benchmarking dei sistemi agentici.
*   **Implementazione tecnica dei Circuit Breakers**: Necessità di architetture specifiche, soglie e sistemi di monitoraggio dettagliati per i meccanismi di interruzione.
*   **Standard di sicurezza MCP e A2A**: Mancano specifiche tecniche di sicurezza nei protocolli di comunicazione tra modelli e tra agenti.
*   **Dati post-Moltbook**: È fondamentale analizzare l'evoluzione della minaccia bot-to-bot nei mesi successivi all'incidente di Moltbook per comprendere le nuove TTP.

Gli scenari di evoluzione della Threat Intelligence includono una potenziale "Arms Race Semantica" tra attaccanti e difensori AI, la standardizzazione dei protocolli con sicurezza integrata, l'adozione di un paradigma di "Agent Isolation" (zerotrust agentic) e la diffusione di infrastrutture "Dual-Use" con capacità offensive e difensive.

## 🔗 Connessioni e Pattern

- [[Applicazioni osint]]
- [[Llm|Large language models]]
- [[Osint]]
- [[Prompt engineering]]
- [[Sicurezza cognitiva]]
- [[Strumenti operativi]]


- [[--]]
F/I/H
- [[--]]
