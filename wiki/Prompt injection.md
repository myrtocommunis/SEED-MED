---
title: Prompt injection
tags:
- OSINT
- processed
- prompt-injection
date: '2026-05-15'
status: draft
depth: standard
sources: '1'
tipo: concetto
---

# Prompt injection

## 🎯 Sintesi Strategica

La prompt injection è una vulnerabilità critica nei [[Large language model]] (LLM) che permette a input malevoli di manipolare il comportamento del modello, sovrascrivendo istruzioni predefinite o inducendolo a eseguire azioni non intenzionali. Riconosciuta come una minaccia strutturale, ha implicazioni significative per la [[Sicurezza cognitiva]] e l'integrità dei sistemi basati su AI, con casi documentati di abuso su larga scala e un emergente mercato di jailbreak sul dark web.

## 📚 Contesto e Definizioni

La prompt injection si manifesta quando un utente o un'entità esterna inserisce istruzioni non autorizzate all'interno di un prompt, che vengono poi interpretate ed eseguite dal [[Large language model]] (LLM) con priorità sulle direttive originali del sistema. Questa manipolazione può portare il modello a divulgare informazioni sensibili, generare contenuti inappropriati o eseguire azioni dannose. È considerata una vulnerabilità strutturale, evidenziata anche nell'OWASP Top 10 per le vulnerabilità dei LLM. Esistono due forme principali:
*   **Prompt Injection Diretta**: L'attaccante inserisce istruzioni malevole direttamente nel prompt fornito al modello.
*   **Prompt Injection Indiretta**: Il modello viene esposto a dati esterni (es. documenti, pagine web) che contengono istruzioni malevole nascoste, le quali vengono poi elaborate e seguite dal modello.

## 📊 Dati, Tecnologie e Metriche

La vulnerabilità della prompt injection è ampiamente documentata e confermata da diversi incidenti e analisi:
*   **Casi Noti**:
    *   **Moltbook**: Un caso di iniezione bot-to-bot su scala industriale che ha coinvolto 1.6 milioni di account e 1.5 milioni di API key esposte, dimostrando la capacità di abuso su vasta scala.
    *   **GTG-1002**: Un incidente di cyber-spionaggio sponsorizzato da uno stato, che ha utilizzato un agente autonomo basato su Claude Code con un'efficacia dell'80-90% tramite iniezione.
*   **Mercato del Jailbreaking**: Esistono marketplace documentati sul dark web dedicati al jailbreak degli LLM, facilitando l'accesso a modelli manipolati per scopi illeciti.
*   **Contromisure**: Le strategie di difesa includono il Reinforcement Learning from Human Feedback (RLHF), il safety training e la standardizzazione dei protocolli di red-teaming. Organizzazioni come OpenAI e Anthropic hanno richiesto un'azione concertata per contrastare l'escalation di queste minacce.
*   **Vettori di Attacco**: L'iniezione indiretta tramite fonti esterne, come file HTML o documenti, è un vettore di attacco documentato (es. GPT-4o System Card, Arstechnica).

## 🔍 Analisi Operativa ed Applicazioni OSINT

Per gli analisti [[Osint]], la comprensione della prompt injection è cruciale. L'integrazione dell'AI nei processi di raccolta e analisi delle informazioni espone a nuovi vettori di attacco. Un analista deve essere consapevole che i dati elaborati da un LLM, specialmente se provenienti da fonti esterne non controllate, potrebbero contenere istruzioni di prompt injection. Questo implica la necessità di:
*   **Validazione Critica**: Esercitare un giudizio critico sulla plausibilità degli output generati dall'AI, riconoscendo che l'AI funge da interlocutore e non da decisore finale.
*   **Monitoraggio dei Dati**: Prestare attenzione ai documenti e alle fonti esterne che vengono forniti agli LLM, poiché possono essere veicoli per iniezioni indirette.
*   **Pratiche di Sicurezza**: Adottare pratiche che minimizzino la contaminazione della memoria tra sessioni di interazione con l'AI, come l'uso di chat anonime per l'analisi di scenari.

## 🔮 Lacune Informative e Prossimi Passi

Nonostante la crescente consapevolezza, permangono alcune lacune informative:
*   **Vulnerabilità dei Modelli Più Piccoli**: La tesi che i modelli più piccoli siano intrinsecamente più vulnerabili alla prompt injection non è ancora supportata da fonti primarie specifiche e richiede ulteriore verifica.
*   **Dettagli Operativi di Attacchi Specifici**: Alcune dimostrazioni operative o dettagli specifici di attacchi (es. l'iniezione su una "ricetta di cucina" menzionata in alcune analisi) rimangono parzialmente documentate o incomplete, limitando la piena comprensione delle loro dinamiche.
*   **Standardizzazione delle Difese**: Sebbene siano stati richiesti standard per il red-teaming, l'implementazione e l'efficacia su larga scala di tali protocolli sono ancora in evoluzione.

## 🔗 Connessioni e Pattern

- [[Applicazioni osint]]
- [[Jailbreaking]]
- [[Large language model]]
- [[Osint]]
- [[Sicurezza cognitiva]]
- [[Tecnologie]]


- [[--]]
F/I/H
- [[--]]
