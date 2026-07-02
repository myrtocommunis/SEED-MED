---
title: Security llm
tags:
- OSINT
- processed
- security-llm
date: '2026-05-15'
status: draft
depth: standard
sources: '1'
tipo: concetto
---

# Security llm

## 🎯 Sintesi Strategica

La sicurezza degli LLM si articola tra lo sviluppo di tecniche per ottimizzare gli output ([[Prompt engineering]]) e la ricerca di metodi per eludere i vincoli di sicurezza ([[Jailbreaking]]). Il Root Prompt e il System Prompt definiscono il comportamento e i guardrail iniziali del modello. Tecniche come il jailbreaking e il [[Prompt injection]] permettono di aggirare questi controlli, facilitando la generazione di contenuti non etici o dannosi, dalla disinformazione alle istruzioni per attività illecite, con una bassa barriera di accesso tecnica. Il Prompt Leaking mira all'estrazione delle istruzioni operative nascoste del modello, compromettendone la configurazione e la privacy.

## 📚 Contesto e Definizioni

Un **prompt** è l'input testuale fornito a un Large Language Model (LLM) per generare una risposta. La sua qualità e specificità sono cruciali per l'efficacia dell'output. Il **Prompt Engineering** è la disciplina dedicata alla progettazione strutturata di tali input per ottenere risposte accurate, pertinenti e di alta qualità. Le sue metodologie si sono evolute da approcci semplici (zero-shot) a tecniche più complesse come il Chain-of-Thought e il role prompting.

**Elementi di un Prompt:**
*   **Instruction:** La direttiva chiara per il modello (es. "Riassumi").
*   **Context:** Informazioni di background supplementari (es. "Usa linguaggio semplice").
*   **Input Data:** I dati o la domanda a cui si cerca risposta.
*   **Output Indicator:** Il formato o tipo di output desiderato (es. "Usa bullet points").

**Root Prompt vs. System Prompt:**
*   Il **Root Prompt** è l'istruzione iniziale che definisce il comportamento generale, lo stile o la personalità dell'IA, spesso impostato dal fornitore del modello.
*   Il **System Prompt** è una porzione di istruzioni **nascoste** fornite all'LLM all'inizio di un'interazione, che definiscono il comportamento, la personalità e i vincoli per l'intera conversazione. Costituisce la prima barriera di sicurezza, incorporando molti dei guardrail del modello.

La progettazione efficace dei prompt enfatizza la chiarezza, la specificità e l'uso di istruzioni positive, concentrandosi su ciò che il modello deve fare piuttosto che su ciò che non deve fare. L'integrazione di Domain Knowledge nel prompt migliora significativamente la precisione e la rilevanza delle risposte.

## 📊 Dati, Tecnologie e Metriche

Il comportamento generativo di un LLM è controllato da specifici parametri:
*   **Temperature:** Regola la casualità e la creatività dell'output. Valori bassi (es. 0.0) rendono le risposte più deterministiche e prevedibili; valori alti (es. 1.5) aumentano la varietà ma possono ridurre la coerenza. Per risposte più sicure e prevedibili, si preferisce una temperatura bassa.
*   **Top-p:** Limita il vocabolario da cui il modello può scegliere le parole, selezionando solo quelle che rientrano in una percentuale cumulativa di probabilità (es. 0.9 seleziona parole che coprono il 90% della probabilità).
*   **Max tokENS:** Definisce la lunghezza massima della risposta generata.

**Contromisure di Sicurezza:**
*   **Guardrail lessici:** Liste di parole proibite, facilmente aggirabili.
*   **Reinforcement Learning from Human Feedback (RLHF):** Un meccanismo di allineamento etico che addestra il modello a produrre risposte desiderabili, efficace contro utenti non intenzionalmente malevoli.
*   **System Prompt:** La prima linea di difesa, sebbene vulnerabile a tecniche di iniezione.
*   **Data Sanitization:** Filtraggio degli input sensibili per prevenire l'elaborazione di dati dannosi.

**Casi di Violazione Documentati:**
| Caso | Anno | Tipo | Impatto |
|---|---|---|---|
| OmniGPT | 2025 | Leak dati | 30.000 email + 34M righe conversazioni utenti esposte |
| Samsung | 2023 | Data leak | Ingegneri inserirono codice sorgente proprietario in ChatGPT; fuga di segreti industriali |
| NYT vs OpenAI | 2023 | Copyright | Causa per uso non autorizzato di articoli per training |
| Mata v. Avianca | 2023 | Allucinazione | Avvocato multato per aver presentato casi legali inventati da ChatGPT |
| Studio Stanford | 2025 | Privacy | 6 grandi provider usano conversazioni utenti per addestramento; conservazione dati indefinita |

## 🔍 Analisi Operativa ed Applicazioni OSINT

La rottura dei vincoli del system prompt si manifesta principalmente in due categorie di attacco:
*   **Jailbreaking:** Un attacco diretto, spesso "psicologico" o "brute-force", all'allineamento etico del modello. L'obiettivo è bypassare i filtri di sicurezza per generare contenuti proibiti, come istruzioni illegali, materiale dannoso o disinformazione.
*   **Prompt Leaking:** Un attacco alla privacy e riservatezza, mirato all'estrazione del system prompt nascosto e delle istruzioni operative o riservate del modello.

**Tecniche di Jailbreaking:**
*   **Role-play adversarial:** Il modello viene "convinto" a interpretare un personaggio privo di vincoli etici.
*   **Leva emotiva:** Sfrutta l'urgenza o l'empatia per disattivare i guardrail.
*   **Omoglifi e Zero-width spaces:** Caratteri Unicode visivamente identici o invisibili usati per bypassare i filtri basati su blacklist.
*   **Prompt Injection negli agenti:** Un attacco indiretto in cui un documento esterno (web, email, file) contiene istruzioni nascoste che reindirizzano il comportamento di un agente AI che lo processa. Questo amplia enormemente la superficie di attacco.

**Implicazioni per l'OSINT:** Il jailbreaking abbassa drasticamente la barriera di accesso alla creazione di contenuti dannosi. Per gli analisti OSINT, ciò significa un aumento potenziale di campagne di disinformazione, produzione di testi di propaganda o istruzioni per attività illecite, che richiedono solo creatività nel framing piuttosto che competenze tecniche avanzate. La capacità di estrarre i system prompt (Prompt Leaking) può inoltre rivelare configurazioni di sicurezza e vulnerabilità sfruttabili.

## 🔮 Lacune Informative e Prossimi Passi

*   **Distinzione tra Direct e Indirect Prompt Injection:** La letteratura attuale non sempre distingue chiaramente tra attacchi in cui l'utente è l'aggressore (Direct Prompt Injection) e quelli in cui un documento esterno veicola l'istruzione malevola (Indirect Prompt Injection), sebbene le superfici di attacco siano significativamente diverse.
*   **Dati Comparativi sui Guardrail LLM:** Mancano dati comparativi robusti sulle percentuali di successo delle diverse tecniche di jailbreaking sui principali modelli LLM (es. GPT-4, Claude, Gemini, Llama 3, Mistral). Questa lacuna impedisce una calibrazione operativa precisa della valutazione del rischio.
*   **Tecniche Avanzate di Prompt Engineering:** Una trattazione più approfondita delle tecniche fondamentali di prompt engineering come Zero-Shot Prompting, Few-Shot Prompting e Few-Shot Chain-of-Thought è necessaria per comprendere appieno come l'efficacia del modello sia influenzata su compiti specifici.
*   **Prossimi Passi di Ricerca:** Mappare sistematicamente le tecniche di jailbreaking contro i principali modelli LLM, integrare le vulnerabilità identificate con la OWASP LLM Top 10 e approfondire l'impatto di tecniche come Chain-of-Thought e Self-Consistency sulla sicurezza e robustezza dei modelli.

## 🔗 Connessioni e Pattern

- [[Applicazioni osint]]
- [[Jailbreaking]]
- [[Large language model]]
- [[Prompt engineering]]
- [[Prompt injection]]
- [[Self-consistency]]


- [[--]]
F/I/H
- [[--]]
