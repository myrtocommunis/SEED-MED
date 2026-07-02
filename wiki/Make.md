---
title: Make
tags:
- OSINT
- processed
- make
- automazione
- no-code
- low-code
date: '2026-05-15'
status: draft
depth: standard
sources: '1'
tipo: concetto
---

# Make

## 🎯 Sintesi Strategica

Make (precedentemente noto come Integromat) è una piattaforma di automazione visuale basata su cloud, leader nel settore delle soluzioni no-code. Consente agli utenti di connettere centinaia di servizi web e applicazioni tramite un'interfaccia grafica intuitiva, orchestrando scenari automatizzati complessi senza la necessità di scrivere codice. È particolarmente efficace per la costruzione di pipeline di raccolta dati e notifica nell'ambito [[Osint]], facilitando l'integrazione di trigger, filtri, arricchimenti (anche tramite [[Llm]]) e output verso diverse destinazioni.

## 📚 Contesto e Definizioni

Make si posiziona come uno strumento di automazione visuale cloud, rientrando nella categoria delle piattaforme **no-code**. Questo significa che la creazione di workflow avviene interamente tramite un'interfaccia grafica, dove gli utenti trascinano e connettono blocchi funzionali, configurando i parametri senza scrivere alcuna riga di codice. La sua architettura permette di creare "scenari" che reagiscono a eventi (trigger) e eseguono una serie di azioni sequenziali o condizionali, integrando servizi disparati come fogli di calcolo, sistemi di messaggistica, API web e client di posta elettronica.

## 📊 Dati, Tecnologie e Metriche

Make offre integrazioni native con centinaia di servizi, tra cui Google Sheets, Slack, API web generiche, email, Telegram e feed [[RSS]]. La sua natura esclusivamente cloud implica che tutti i dati elaborati transitano sui server di Make (ubicati negli Stati Uniti), il che rappresenta un [[Opsec]] significativo per operazioni sensibili.
Negli anni 2025-2026, Make ha significativamente espanso le sue capacità integrando nodi dedicati all'Intelligenza Artificiale e ai Large Language Models (LLM), come ChatGPT, Claude e Openrouter. Questo permette l'arricchimento semantico dei dati direttamente all'interno dei workflow no-code, abilitando funzionalità avanzate di classificazione, estrazione di entità (NER) e analisi testuale.

## 🔍 Analisi Operativa ed Applicazioni OSINT

Nell'ambito OSINT, Make è uno strumento potente per la prototipazione rapida e l'implementazione di pipeline di raccolta e notifica. Un workflow tipico potrebbe prevedere:
1.  **Trigger**: Monitoraggio di un feed [[RSS]] o di un'API per nuovi dati.
2.  **Filtraggio**: Applicazione di condizioni per selezionare solo le informazioni rilevanti.
3.  **Arricchimento**: Utilizzo di nodi LLM per classificare il contenuto, estrarre informazioni chiave o riassumere testi.
4.  **Notifica/Archiviazione**: Invio di alert via email, Telegram o Slack, oppure archiviazione dei dati in un database o foglio di calcolo.

La sua facilità d'uso lo rende ideale per analisti senza un background di programmazione, consentendo la creazione di sistemi di monitoraggio complessi in tempi brevi. Tuttavia, la dipendenza dal cloud e il transito dei dati su server esterni richiedono un'attenta valutazione dei rischi [[Opsec]], specialmente in contesti dove la sovranità e la riservatezza dei dati sono critiche. Per scenari che richiedono un controllo completo sull'infrastruttura, alternative self-hostable come [[n8n]] possono essere preferibili.

## 🔮 Lacune Informative e Prossimi Passi

Nonostante la sua versatilità, Make presenta alcune limitazioni. La sua rigidità può emergere in scenari che richiedono:
*   Interazioni complesse con siti web (es. autenticazione avanzata, gestione di CAPTCHA).
*   Logiche di estrazione dati non banali o altamente personalizzate.
*   Integrazioni con sistemi legacy o proprietari non supportati nativamente.

In questi casi, potrebbe essere necessario ricorrere a soluzioni basate su codice. Inoltre, la dipendenza da un fornitore di servizi cloud espone a rischi legati a cambiamenti di pricing, interruzioni del servizio o modifiche delle politiche.
Lacune informative attuali includono una comparazione dettagliata dei costi per pipeline enterprise rispetto a soluzioni self-hosted come n8n, e un'analisi approfondita della conformità [[GDPR]] e della residenza dei dati per operazioni OSINT sensibili.

## 🔗 Connessioni e Pattern

- [[Applicazioni osint]]
- [[Classificazione]]
- [[Llm|Large language models]]
- [[Llm]]
- [[Osint]]
- [[n8n]]


- [[--]]
F/I/H
- [[--]]
