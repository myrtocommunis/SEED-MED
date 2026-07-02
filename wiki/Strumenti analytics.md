---
title: Strumenti analytics
tags:
- OSINT
- processed
- strumenti-analytics
date: '2026-05-15'
status: draft
depth: standard
sources: '1'
tipo: concetto
---

# Strumenti analytics

## 🎯 Sintesi Strategica

Gli strumenti analytics moderni, in particolare quelli legati alla [[Business intelligence]] (BI), costituiscono il fulcro operativo delle infrastrutture di intelligence basate sui dati, sia in contesti aziendali che nell'[[Osint]] geopolitico-finanziario. A differenza degli approcci tradizionali, la BI moderna, formalizzata nel 1989, automatizza e accelera il processo decisionale, trasformando dati grezzi in azioni tempestive. Il ciclo BI si articola in tre livelli interconnessi: **BI** (decisioni immediate), **Data Analytics** (comprensione descrittiva del "perché"), e **Business Analytics** (previsione del "cosa succederà"). Strumenti come [[Power BI]], [[Dax]] (Data Analysis Expression) e [[Power Automate]] formano uno stack integrato: Power BI visualizza, DAX computa e Power Automate automatizza i workflow. Per l'analista OSINT, questo stack è cruciale per la mappatura di flussi finanziari opachi, il monitoraggio automatizzato di indicatori di conflitto e il tracing di transazioni crypto. La forza del ciclo BI moderno risiede nella sua natura ciclica e collaborativa, che trasforma dati in decisioni e viceversa.

## 📚 Contesto e Definizioni

La [[Business intelligence]] ha una storia che risale agli anni '60, quando i sistemi ERP iniziarono a raccogliere dati aziendali strutturati. Il termine BI fu formalizzato nel 1989, non più come semplice archivio di informazioni, ma come un sistema attivo per accelerare e automatizzare le decisioni. Da allora, la BI ha attraversato tre fasi evolutive:
*   **BI 1.0 (1960–1989)**: Sistemi di condivisione informazioni statici, con limitazioni dovute all'assenza di feedback e dati isolati.
*   **BI 2.0 (1989–2010)**: Caratterizzata da [[Data warehouse]], OLAP e reporting strutturato, ma con latenza elevata dovuta al batch processing.
*   **BI 3.0 (Moderna, 2010–oggi)**: Distinta per self-service analytics, integrazione cloud, capacità in tempo reale e integrazione con l'[[Fondamenti di ai|Intelligenza Artificiale]].

La BI moderna si caratterizza per:
1.  **Self-service analytics**: Gli utenti accedono direttamente ai dati senza intermediari IT.
2.  **Collaborazione ciclica**: Il processo dati-decisioni è continuo.
3.  **Integrazione cloud**: I dati fluiscono da sistemi aziendali al cloud, al [[Data warehouse]] e infine al consumatore in tempo quasi-reale.

È fondamentale distinguere tra:
*   **Business Intelligence**: Risponde alla domanda "Cosa dobbiamo fare ORA?", con un orizzonte temporale presente, producendo dashboard e report live per decision-maker operativi.
*   **Data Analytics**: Risponde a "Perché è successo?", con un orizzonte temporale passato, identificando pattern e correlazioni tramite esplorazione e statistica descrittiva, rivolto ad analisti e scienziati dei dati.
*   **Business Analytics**: Risponde a "Cosa succederà DOPO?", con un orizzonte temporale futuro, creando modelli predittivi e segmentazioni tramite [[Data mining]] e [[Machine learning]], per strateghi e pianificatori.

Per l'intelligence geopolitico-finanziaria, questa triade è essenziale: la BI fornisce il quadro attuale (es. sanzioni attive), il Data Analytics spiega i pattern storici (es. deviazioni di flussi), e il Business Analytics anticipa scenari (es. contromisure future).

## 📊 Dati, Tecnologie e Metriche

Il ciclo BI moderno è un framework ciclico e collaborativo con quattro fasi tecniche principali:
1.  **Raccolta dati**: Acquisizione di dati grezzi da sistemi aziendali (ERP, CRM, log), API pubbliche e dataset open-source (es. Kaggle, Our World in Data, OpenBDAP).
2.  **Lavorazione**: Pulizia, trasformazione e normalizzazione dei dati, spesso realizzata tramite strumenti ETL integrati come Power Query in [[Power BI]].
3.  **Storage**: Archiviazione dei dati in ambienti cloud (Azure, AWS), [[Data warehouse]] (Snowflake, Bigquery) o file strutturati (CSV, Excel).
4.  **Visualizzazione e Decisione**: Gli utenti accedono ai dati elaborati per rispondere a specifiche domande di business o intelligence.

### Architettura di [[Power BI]]

In Power BI, il **workspace** è il contenitore fondamentale che organizza dataset, dashboard e visualizzazioni. La gerarchia include:
*   **Workspace**: Contenitore di dati, report, dashboard (analogia OSINT: "Dossier operationale").
*   **Dataset**: Insieme di tabelle collegate (analogia OSINT: "Base dati strutturata").
*   **Report**: Pagina di visualizzazione multipla (analogia OSINT: "Briefing visivo").
*   **Dashboard**: Pannello di monitoraggio singolo (analogia OSINT: "Situational awareness screen").
*   **Metrica ([[Dax]])**: Funzione computazionale su più righe (analogia OSINT: "Indicatore calcolato").

### [[Dax]] — Data Analysis Expression

DAX è il linguaggio computazionale di Power BI, simile a Excel ma con una differenza architetturale fondamentale: il **contesto di esecuzione**.
*   **Struttura Sintattica di Base**: `Nomemisura = FUNZIONE(Tabella[Colonna])`.
*   **Contesti DAX**:
    *   **Row Context**: La formula è applicata riga per riga (es. calcolare il P/L per ogni transazione crypto).
    *   **Filter Context**: La formula è applicata al dataset filtrato (es. analizzare transazioni sanzionate solo per un settore specifico).
*   **Time Intelligence in DAX**: Funzioni come `TOTALYTD`, `SAMEPERIODLASTYEAR`, `DATEADD`, `PARALLELPERIOD` consentono calcoli temporali complessi per monitorare volumi cumulativi di sanzioni o confrontare flussi finanziari anno su anno.

### [[Power Automate]] — Automazione per Intelligence Workflow

Power Automate (ex Microsoft Flow) abilita l'automazione di processi ripetitivi tramite tre tipi di flusso:
*   **Automatizzato**: Avviato da un trigger (es. nuova riga in Excel, email ricevuta), utile per alert automatici su liste di soggetti sanzionati.
*   **Istantaneo**: Avviato manualmente (pulsante), per richieste di approvazione ad accesso a dossier.
*   **Pianificato**: Avviato a intervalli di tempo predefiniti (es. ogni 6 ore), per monitoraggio giornaliero di dataset pubblici.
L'uso di **campi dinamici** è cruciale per legare i valori del trigger alle azioni successive, garantendo la coerenza del workflow.

## 🔍 Analisi Operativa ed Applicazioni OSINT

L'interoperabilità dello stack Microsoft (Power BI + DAX + Power Automate) è fondamentale per l'intelligence, grazie alla profonda integrazione nativa:
1.  **Power BI ↔ Power Automate**: Un report Power BI può attivare un flusso quando un KPI supera una soglia. Ad esempio, un alert automatico quando il volume di transazioni verso un wallet sospetto supera una determinata soglia.
2.  **Power BI ↔ DAX**: DAX è il motore computazionale nativo di Power BI, con le sue misure che vivono nel dataset e sono consumate dai report visivi.
3.  **Power Automate ↔ Dati Open-Source**: Tramite connettori nativi, Power Automate può estrarre dati da piattaforme come Kaggle, Our World in Data e API REST pubbliche, trasformandoli in trigger per analisi successive.

### Rilevanza delle Fonti Dati per [[Osint]] Geopolitico-Finanziario

La combinazione di questi strumenti con fonti open-source crea un ciclo di intelligence completo:
*   **Kaggle (kaggle.com/datasets)**: Offre dataset crowdsourced (CSV, JSON) su criminalità, sanzioni, transazioni.
*   **Our World in Data (ourworldindata.org)**: Fornisce indicatori globali aggregati su conflitti, povertà, migrazioni, economia.
*   **OpenBDAP (openbdap.rgs.mef.gov.it)**: Contiene bilanci e dati di spesa della Pubblica Amministrazione italiana, utili per analisi su corruzione e appalti.
Queste fonti, integrate con Power BI per la visualizzazione e Power Automate per il monitoraggio continuo, formano un ciclo di intelligence open-source con costi marginali minimi per l'ingestione dei dati.

## 🔮 Lacune Informative e Prossimi Passi

Sebbene potenti per dati strutturati, gli strumenti BI moderni presentano limiti per l'[[Osint]] geopolitico-finanziario:
1.  **Forma dei dati**: Eccellono con dati strutturati (CSV, SQL, Excel). I dati non strutturati (report di intelligence, documenti PDF) richiedono pre-elaborazione tramite [[Nlp]] prima dell'ingestione.
2.  **Connettività cross-source**: Lo stack Microsoft ha connettori limitati per API OSINT specializzate (es. ACLED, OFAC SDN API, Chainalysis), necessitando integrazioni custom tramite connettori REST.
3.  **Scalabilità computazionale**: Le misure DAX su dataset di grandi dimensioni (>10M righe) possono degradare le performance, richiedendo architetture di pre-elaborazione (es. Power BI Dataset Gateway + Azure Data Lake).

**Prossimi passi operativi raccomandati**:
*   Valutare l'integrazione con [[Neo4j]] (via custom connector) per l'arricchimento e l'analisi di rete dei dati BI.
*   Implementare pipeline **Power Automate → Kaggle API → Power BI** per il monitoraggio automatico giornaliero di dataset rilevanti.
*   Sperimentare **AI-driven dashboarding** (Plotly Studio, Lovable, Power BI Copilot) per ridurre il tempo di creazione delle dashboard.

## 🔗 Connessioni e Pattern

- [[Business intelligence]]
- [[Dax]]
- [[Nlp]]
- [[Osint]]
- [[Power Automate]]


- [[--]]
F/I/H
- [[--]]
