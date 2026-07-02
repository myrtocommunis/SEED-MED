---
title: Template
tags:
- OSINT
- processed
- template
date: '2026-05-15'
status: draft
depth: standard
sources: '1'
tipo: concetto
---

# Template

## 🎯 Sintesi Strategica

Il [[Template]] è una tecnica fondamentale nel [[Prompt engineering]] per i [[Llm|Large language models]] (LLM), progettata per imporre una struttura di output rigida e predefinita. Questa metodologia elimina la variabilità del formato, garantendo la completezza e la coerenza delle risposte generate. Nel contesto OSINT, l'applicazione di template è cruciale per standardizzare report, analisi e processi di estrazione dati, trasformando output generici in intelligence strutturata e immediatamente utilizzabile. La sua efficacia è massimizzata quando combiNATO con altri pattern, come il [[Persona]], per produrre risultati specialistici e formattati.

## 📚 Contesto e Definizioni

Un "Template Pattern" in [[Prompt engineering]] definisce uno schema di output fisso che un Large Language Model è obbligato a compilare. Questo schema può includere campi specifici, sezioni predefinite o formati di dati strutturati (es. JSON, tabelle). L'obiettivo primario è standardizzare il formato dell'informazione generata, rendendola prevedibile, completa e facilmente processabile da sistemi automatizzati o da altri analisti. A differenza dei prompt a forma libera, che lasciano al modello ampia discrezionalità sulla presentazione, i template guidano l'LLM a riempire slot specifici, riducendo l'ambiguità e la probabilità di omissioni critiche.

## 📊 Dati, Tecnologie e Metriche

Il Template Pattern è intrinsecamente legato all'uso di [[Llm|Large language models]] (LLM) e si manifesta attraverso la definizione esplicita di strutture di output all'interno dei prompt.
*   **Tecnologia**: Viene implementato come parte integrante del [[Prompt engineering]] per guidare il comportamento degli LLM.
*   **Dati**: È applicato per strutturare l'output di diverse tipologie di dati, inclusi report testuali, dati strutturati (es. JSON, XML, tabelle) e riassunti analitici.
*   **Metriche di Successo**:
    *   **Schema Compliance**: Misura la percentuale di output che aderisce rigorosamente alla struttura del template definito (es. >95% per l'estrazione di dati strutturati).
    *   **Completezza**: Valuta se tutti i campi richiesti nel template sono stati compilati, evitando omissioni o valori `null` non intenzionali.
    *   **Consistenza**: Garantisce l'uniformità del formato di output attraverso generazioni multiple per input simili.
*   **Esempi di Template Operativi**:
    *   **Template per Report OSINT**:
        ```
        SUBJECT: [nome soggetto/entità sotto indagine]
        CLASSIFICATION: [livello di confidenzialità]
        EXECUTIVE SUMMARY: [sintesi max 3 righe]
        KEY FINDINGS: [lista numerata evidenze]
        ENTITIES IDENTIFIED: [tabella: nome | tipo | ruolo | fonte]
        CONNECTIONS MAP: [relazioni tra entità con evidenze]
        CONFIDENCE ASSESSMENT: [high/medium/low per finding]
        INTELLIGENCE GAPS: [informazioni mancanti]
        RECOMMENDED ACTIONS: [prossimi passi investigativi]
        ```
    *   **Template per Analisi Vulnerabilità CVE**:
        ```
        Nome della vulnerabilità: [nome]
        CVE ID: [CVE-YYYY-NNNNN]
        Gravità: [Critica/Alta/Media/Bassa]
        Componente interessato: [componente + versioni]
        Vettore di attacco: [descrizione tecnica + CVSS v3.1]
        Proof of Concept: [payload sintetico]
        Regole di detection: [Sigma + Snort]
        Remediation: [passaggi ordinati per priorità]
        ```
    *   **Template per Estrazione Dati Strutturati (JSON)**:
        ```
        Schema:
        entities: [{name, type (person/org/location), role, attributes, confidence}]
        events: [{description, date, location, actors: [], type, confidence}]
        relationships: [{entity1, entity2, relationship_type, evidence}]
        financial_data: [{amount, currency, date, from, to, purpose}]
        metadata: {source, date_published, author, reliability_assessment}
        ```

## 🔍 Analisi Operativa ed Applicazioni OSINT

L'applicazione del Template Pattern in [[Osint]] è trasformativa, consentendo agli analisti di gestire e presentare l'intelligence in modo altamente strutturato:
*   **Standardizzazione dei Report**: Assicura che i report OSINT, le sintesi di [[Threat intelligence]] o le analisi di vulnerabilità mantengano un formato coerente, facilitando l'integrazione in database, dashboard o altri strumenti analitici.
*   **Estrazione Dati Strutturati**: Permette di convertire grandi volumi di testo non strutturato (es. pagine web, post sui social media, documenti) in dati strutturati (es. JSON, CSV) che possono essere facilmente interrogati, analizzati e correlati. Questo è fondamentale per l'Data Extraction automatizzata.
*   **Integrazione in Pipeline di Analisi**: I template sono un componente chiave nelle pipeline di [[Chaining]], in particolare nella fase di "Report" (Step 5) per garantire che l'output finale sia in un formato standard e azionabile. Possono anche essere impiegati nella fase di "Estrazione" (Step 2).
*   **Riduzione della Variabilità**: In un dominio come l'OSINT, dove le informazioni provengono da fonti eterogenee e spesso caotiche, i template impongono un ordine sull'intelligence generata, aumentandone l'affidabilità e la fruibilità.
*   **Casi d'Uso Specifici OSINT**:
    *   Generazione di dossier su entità o individui.
    *   Creazione di analisi strutturate di vulnerabilità (es. per CVE).
    *   Estrazione di entità, eventi e relazioni da testi grezzi in formati leggibili da macchina.
    *   Garantire la coerenza negli output di [[Threat intelligence]].

## 🔮 Lacune Informative e Prossimi Passi

Nonostante la sua efficacia, l'implementazione del Template Pattern presenta alcune aree che richiedono ulteriore ricerca e sviluppo:
*   **Benchmarks Quantitativi**: Mancano benchmark quantitativi specifici sulla performance dei template pattern (es. miglioramento dell'accuratezza rispetto a tecniche zero-shot su dataset OSINT reali).
*   **Prompt Injection Difensivo**: Strategie per rafforzare i template contro attacchi di [[Prompt injection]], che potrebbero manipolare la struttura o il contenuto dell'output desiderato.
*   **Ottimizzazione dei Token**: Gestione delle limitazioni della finestra di contesto degli LLM ("avalanche di token") quando template complessi sono combinati con input di grandi dimensioni.
I prossimi passi dovrebbero includere un'analisi comparativa approfondita su dataset OSINT reali, misurando l'accuratezza, la latenza e il consumo di token delle diverse combinazioni di pattern che includono i template.

## 🔗 Connessioni e Pattern

- [[Large language model]]
- [[Llm|Large language models]]
- [[Pipeline di analisi]]
- [[Prompt engineering]]
- [[Prompt injection]]
- [[Threat intelligence]]


- [[--]]
F/I/H
- [[--]]
