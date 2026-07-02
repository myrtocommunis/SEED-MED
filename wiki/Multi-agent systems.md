---
title: Multi-agent systems
tags:
- OSINT
- processed
- multi-agent-systems
date: '2026-05-15'
status: draft
depth: standard
sources: '1'
tipo: concetto
---

# Multi-agent systems

## 🎯 Sintesi Strategica

I [[Sistemi Multi-Agente]] rappresentano un'evoluzione significativa nel campo dell'[[Fondamenti di ai|Intelligenza Artificiale]], trasformando i modelli linguistici di grandi dimensioni (LLM) da semplici generatori di testo a entità autonome capaci di percepire, RAGionare e agire. Questo paradigma agentico si basa sul ciclo universale Percezione-Decisione-Azione (P-D-A) e abilita la creazione di un "Web of Agents", un ecosistema di agenti interconnessi che interagiscono con il mondo esterno tramite API e strumenti specifici. Per l'[[Osint]], ciò implica la possibilità di automatizzare e orchestrare compiti complessi di raccolta, analisi e sintesi informativa, ma introduce anche nuove sfide in termini di sicurezza cognitiva e controllo.

## 📚 Contesto e Definizioni

Un **sistema multi-agente** (MAS) è un sistema composto da più agenti intelligenti che interagiscono tra loro e con l'ambiente per RAGgiungere obiettivi comuni o individuali. L'emergere dell'[[Agenti]] e dei MAS è il risultato della convergenza di tre fattori chiave:
1.  **Capacità di RAGionamento e pianificazione degli LLM**: I modelli linguistici hanno RAGgiunto una sofisticazione tale da permettere un'autonomia decisionale.
2.  **Infrastrutture API e tool-calling**: La disponibilità di interfacce programmatiche e la capacità degli agenti di richiamare strumenti esterni consentono l'interazione con il mondo digitale e fisico.
3.  **Transizione al "Web of Agents"**: L'idea di un'interconnessione di agenti autonomi che sostituisce o affianca il tradizionale "Web of Documents".

Il **ciclo Percezione-Decisione-Azione (P-D-A)** è il fondamento operativo di ogni agente, descrivendo il processo iterativo attraverso cui un agente raccoglie informazioni dall'ambiente (Percezione), elabora tali informazioni per formulare una strategia (Decisione/RAGionamento) e interviene sull'ambiente (Azione), ricevendo feedback per il ciclo successivo.

## 📊 Dati, Tecnologie e Metriche

I [[Sistemi Multi-Agente]] si basano su architetture e concetti specifici:
*   **Ciclo P-D-A**: Schema operativo universale (Percezione → RAGionamento/Decisione → Azione → Feedback).
*   **Tre tipologie di memoria**:
    *   **Episodica**: Corrisponde alla finestra di contesto (context window) dell'agente, per la gestione delle interazioni recenti.
    *   **Semantica**: Rappresentata da un [[Knowledge Graph]], per la conoscenza a lungo termine e le relazioni concettuali.
    *   **Vettoriale/[[RAG]]**: Implementata tramite [[Database vettoriali]] e tecniche di [[Retrieval Augmented Generation]], per l'accesso e l'integrazione di informazioni esterne.
*   **Quattro stadi della [[Kill Chain Cognitiva]]**: Un framework per analizzare e mitigare le minacce alla sicurezza cognitiva nei sistemi agentici:
    1.  **Semantic Infection**: Infiltrazione di informazioni fuorvianti o dannose.
    2.  **Cognitive Compromise**: Alterazione dei processi decisionali dell'agente.
    3.  **Agency Propagation**: Diffusione del comportamento compromesso ad altri agenti.
    4.  **Systemic Execution**: Esecuzione di azioni dannose a livello di sistema.
*   **Quadro normativo**: L'[[Ai act]] classifica i sistemi di IA in quattro categorie di rischio (inaccettabile, alto rischio, limitato, minimo), fornendo un contesto regolatorio per lo sviluppo e l'implementazione dei MAS.
*   **Casi studio**: Esempi come RoboPAIR illustrano la capacità di bypassare filtri di sicurezza in sistemi robotici fisici, evidenziando vulnerabilità operative.

## 🔍 Analisi Operativa ed Applicazioni OSINT

Per l'OSINT, i [[Sistemi Multi-Agente]] offrono capacità avanzate per l'automazione e l'orchestrazione di attività complesse:
*   **Raccolta e aggregazione dati**: Agenti specializzati possono monitorare fonti aperte, estrarre informazioni rilevanti e aggregarle in modo strutturato, superando i limiti dei singoli LLM.
*   **Analisi cross-dominio**: Un MAS può integrare dati da diverse fonti (testuali, immagini, video, social media) e applicare modelli analitici specifici per identificare pattern, anomalie e connessioni nascoste.
*   **Valutazione della sicurezza cognitiva**: L'analisi della [[Kill Chain Cognitiva]] diventa cruciale per l'OSINT, sia per identificare tentativi di manipolazione informativa (es. disinformazione) sia per proteggere i propri sistemi agentici da attacchi.
*   **Simulazione e previsione**: I MAS possono essere impiegati per simulare scenari complessi, prevedere comportamenti di attori ostili o valutare l'impatto di determinate informazioni.
*   **Ricerca di vulnerabilità**: L'esempio di RoboPAIR suggerisce come agenti autonomi possano essere utilizzati (eticamente) per testare la robustezza di sistemi di sicurezza, identificando punti deboli che potrebbero essere sfruttati.

## 🔮 Lacune Informative e Prossimi Passi

Per una comprensione completa e un'applicazione robusta dei [[Sistemi Multi-Agente]], sono necessarie ulteriori ricerche e verifiche:
*   **Analisi approfondita del caso RoboPAIR**: È fondamentale esaminare la letteratura accademica e i report tecnici relativi a casi come RoboPAIR per comprenderne le implicazioni operative e le contromisure.
*   **[[Constitutional AI]]**: Esplorare l'efficacia della [[Constitutional AI]] come meccanismo per prevenire il Cognitive Compromise e garantire l'allineamento degli agenti con principi etici e di sicurezza.
*   **Confronto tra framework multi-agente**: Valutare e comparare le capacità, i vantaggi e gli svantaggi di framework come Autogen, [[CrewAI]] e Langgraph per l'implementazione di soluzioni OSINT.
*   **Testing di Semantic Infection**: Sviluppare metodologie e strumenti per testare la vulnerabilità dei sistemi agentici a tecniche di Indirect Prompt Injection e altre forme di Semantic Infection.

## 🔗 Connessioni e Pattern

- [[Applicazioni osint]]
- [[Disinformazione]]
- [[Manipolazione informativa]]
- [[Osint]]
- [[Prompt injection]]
- [[Sicurezza cognitiva]]


- [[--]]
F/I/H
- [[--]]
