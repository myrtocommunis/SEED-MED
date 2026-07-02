---
title: Business intelligence
tags:
- OSINT
- processed
- business-intelligence
date: '2026-05-15'
status: draft
depth: standard
sources: '4'
tipo: concetto
---

# Business intelligence

## 🎯 Sintesi Strategica

La [[Business intelligence]] (BI) è un insieme di processi, metodologie e tecnologie che trasformano dati grezzi in informazioni significative e azionabili, supportando decisioni strategiche e operative. Nata per ottimizzare i processi aziendali, la BI moderna si distingue per la sua capacità di automatizzare e accelerare il processo decisionale, fornendo risposte tempestive a domande operative ("Cosa dobbiamo fare ORA?"). Si integra strettamente con Data Analytics (che spiega "Perché è successo?") e Business Analytics (che predice "Cosa succederà?"), formando una triade analitica fondamentale. In contesti di [[Osint]] (Open Source Intelligence), la BI è cruciale per la mappatura di flussi finanziari, il monitoraggio di indicatori di rischio e il tracciamento di transazioni in reti complesse, inclusa la [[Blockchain]].

## 📚 Contesto e Definizioni

Il concetto di Business Intelligence ha radici negli anni '60, quando i sistemi ERP iniziarono a raccogliere dati aziendali strutturati. Il termine fu formalizzato nel 1989, evolvendo da un semplice repository di informazioni a un sistema attivo per accelerare e automatizzare le decisioni.

L'evoluzione della BI può essere suddivisa in tre fasi principali:
*   **BI 1.0 (1960–1989):** Caratterizzata da sistemi di condivisione di informazioni statici, con limitato feedback e dati spesso isolati in "silos".
*   **BI 2.0 (1989–2010):** Introduzione di data warehouse, OLAP (Online Analytical Processing) e reporting strutturato, sebbene con elaborazione in batch e latenza elevata.
*   **BI 3.0 (Moderna, 2010–oggi):** Si distingue per l'adozione di self-service analytics, integrazione cloud, capacità in tempo reale e funzionalità basate su [[Intelligenza artificiale generativa|intelligenza artificiale]].

Una distinzione operativa fondamentale è quella tra Business Intelligence, Data Analytics e Business Analytics:

| Dimensione           | Business Intelligence      | Data Analytics                     | Business Analytics                      |
| :------------------- | :------------------------- | :--------------------------------- | :-------------------------------------- |
| **Domanda chiave**   | "Cosa dobbiamo fare ORA?"  | "Perché è successo?"               | "Cosa succederà DOPO?"                  |
| **Orizzonte temporale** | Presente                 | Passato                            | Futuro                                  |
| **Output tipico**    | Dashboard, report live     | Pattern, correlazioni, descrizioni | Modelli predittivi, previsioni          |
| **Metodi principali**| Visualizzazione, aggregazione | Esplorazione, statistica descrittiva | Data mining, machine learning, previsione |
| **Utente target**    | Decision-maker operativo   | Analista dati/scienziato dati      | Stratega, pianificatore                 |

Per l'intelligence geopolitico-finanziaria, questa triade è essenziale: la BI fornisce il quadro attuale (es. sanzioni attive), il Data Analytics spiega i pattern storici (es. deviazioni di flussi), e il Business Analytics anticipa scenari futuri.

## 📊 Dati, Tecnologie e Metriche

Il ciclo moderno della [[Business intelligence]] è un framework ciclico e collaborativo che si articola in quattro fasi tecniche principali, culminando nella decisione:
1.  **Raccolta dati:** Acquisizione di dati grezzi da sistemi aziendali (ERP, CRM, log), API pubbliche e dataset open-source (es. Kaggle, Our World in Data, OpenBDAP).
2.  **Lavorazione:** Pulizia, trasformazione e normalizzazione dei dati, spesso realizzata tramite strumenti ETL (Extract, Transform, Load) come Power Query in [[Power BI]].
3.  **Storage:** Archiviazione dei dati in ambienti cloud (Azure, AWS), data warehouse (Snowflake, Bigquery) o file strutturati (CSV, Excel).
4.  **Visualizzazione e Decisione:** Gli utenti accedono ai dati elaborati tramite dashboard e report per rispondere a specifiche domande di business o intelligence.

Lo stack tecnologico abilitante include strumenti come [[Power BI]], [[Dax]] (Data Analysis Expressions) e [[Power Automate]].

### Architettura Power BI

In [[Power BI]], il *workspace* è il contenitore fondamentale che organizza dataset, dashboard e visualizzazioni. La gerarchia è:
*   **Workspace:** Contenitore di dati, report, dashboard (analogia OSINT: "Dossier operationale").
*   **Dataset:** Insieme di tabelle collegate (analogia OSINT: "Base dati strutturata").
*   **Report:** Pagina di visualizzazione multipla (analogia OSINT: "Briefing visivo").
*   **Dashboard:** Pannello di monitoraggio singolo (analogia OSINT: "Situational awareness screen").
*   **Metrica (DAX):** Funzione computazionale su più righe (analogia OSINT: "Indicatore calcolato").

### DAX — Data Analysis Expressions

[[Dax]] è il linguaggio computazionale di [[Power BI]], che permette di creare misure (aggregazioni virtuali), colonne calcolate e sfruttare la Time Intelligence. La sua potenza risiede nel concetto di *contesto di esecuzione*.
*   **Row Context:** La formula è applicata riga per riga (es. calcolare il profitto per ogni transazione).
*   **Filter Context:** La formula è applicata al dataset filtrato (es. analizzare transazioni sanzionate solo per un settore specifico).
Le funzioni di Time Intelligence in DAX (`TOTALYTD`, `SAMEPERIODLASTYEAR`, `DATEADD`, `PARALLELPERIOD`) consentono calcoli temporali complessi per analisi di trend e confronti.

### Power Automate — Automazione per Intelligence Workflow

[[Power Automate]] (precedentemente Microsoft Flow) automatizza processi ripetitivi attraverso tre tipi di flusso:
*   **Automatizzato:** Avviato da un trigger (es. nuova riga in un database, email ricevuta). Utile per alert automatici su liste di sanzioni.
*   **Istantaneo:** Avviato manualmente (es. pulsante).
*   **Pianificato:** Avviato a intervalli di tempo predefiniti (es. monitoraggio giornaliero di dataset pubblici).
L'uso di *campi dinamici* è cruciale per collegare i valori del trigger alle azioni successive, rendendo i workflow reattivi ai dati sorgente.

## 🔍 Analisi Operativa ed Applicazioni OSINT

La [[Business intelligence]] è un'infrastruttura critica per l'[[Osint]] e l'applicazione di normative come le Sanzioni Internazionali e l'AML (Anti-Money Laundering). L'interoperabilità dello stack Microsoft (Power BI, DAX, Power Automate) consente di costruire cicli di intelligence open-source completi.

### Strumenti e Fonti Dati per OSINT

*   **Database Commerciali Globali:**
    *   **Orbis (Bureau van Dijk):** Principale database commerciale globale con milioni di entità.
    *   **Opencorporates:** Il più grande database open di società, utilizzato nel giornalismo investigativo.
    *   **North Data:** Aggregatore di dati societari europeo, con funzionalità AI.
    *   **Crunchbase:** Database leader per startup e investimenti.
*   **Registri Ufficiali:**
    *   **SEC Edgar:** Registro ufficiale per società quotate e registrate negli Stati Uniti.
    *   **ZEFIX:** Registro centrale svizzero per i dati identificativi delle aziende.
    *   **Companies House:** Registro ufficiale delle aziende nel Regno Unito.
*   **Database per Indagini Specializzate:**
    *   **ICIJ Offshore Leaks (Panama/PanDORA Papers):** Database di società offshore per ricerche investigative.
    *   **ANAC (Italia):** Autorità Nazionale Anticorruzione, per dati su appalti e spesa pubblica.
    *   **Importyeti:** Dati di import/export.
*   **Fonti Dati Pubbliche per Analisi Geopolitico-Finanziaria:**
    *   **Kaggle:** Dataset crowdsourced per analisi criminali, sanzioni, transazioni.
    *   **Our World in Data:** Indicatori globali aggregati su conflitti, economia, migrazioni.
    *   **OpenBDAP:** Bilanci e dati di spesa della Pubblica Amministrazione italiana.

### Convergenza BI e [[Blockchain]]

Entrambi i domini condividono l'obiettivo di seguire i flussi di valore attraverso reti complesse.
*   **Reti:** Societarie per la BI, [[Blockchain]] per le criptovalute.
*   **Attribuzione:** Identificazione del *beneficial owner* per la BI, attribuzione di indirizzi crypto a entità per la [[Blockchain]].
*   **Anonimato/[[Pseudonimato]]:** Sfida comune in entrambi i contesti.
*   **Open Source:** Registri pubblici e database per la BI, [[Blockchain]] explorer per la [[Blockchain]].

Le differenze includono il regime giuridico (Art. 134 TULPS per investigazioni private vs. assenza di regime specifico per analisi di blockchain pubbliche), la permanenza dei dati (mutabili vs. immutabili) e gli strumenti specifici (Orbis vs. [[Arkham]], [[Etherscan]]).

### Aspetti Etici e Legali

In Italia, l'Art. 134 del Testo Unico delle Leggi di Pubblica Sicurezza (TULPS) richiede una licenza prefettizia per la raccolta di informazioni commerciali per conto di terzi. L'analisi di dati pubblicamente disponibili su [[Blockchain]] è una delle poche aree in cui tale autorizzazione non è generalmente richiesta, data la natura permissionless e trasparente della fonte.

## 🔮 Lacune Informative e Prossimi Passi

Nonostante la sua potenza, il ciclo BI moderno presenta alcune lacune operative per l'[[Osint]] avanzata:
1.  **Gestione Dati Non Strutturati:** Strumenti come [[Power BI]] e [[Dax]] eccellono con dati strutturati. I dati non strutturati (es. report di intelligence, documenti PDF) richiedono un pre-processing tramite tecniche di [[Intelligenza artificiale generativa|NLP]] prima dell'ingestione.
2.  **Connettività Cross-Source:** Lo stack Microsoft ha connettori limitati per API OSINT specializzate (es. ACLED, OFAC SDN API, Chainalysis). È spesso necessaria un'integrazione personalizzata tramite connettori REST.
3.  **Scalabilità Computazionale:** Le misure DAX su dataset molto grandi (>10 milioni di righe) possono degradare le performance. Sono necessarie architetture di pre-processing più robuste (es. Power BI Dataset Gateway + Azure Data Lake).

**Prossimi passi operativi raccomandati:**
*   Valutare l'integrazione con database a grafo come Neo4j (tramite connettori custom) per l'arricchimento e l'analisi di rete dei dati BI.
*   Implementare pipeline [[Power Automate]] → Kaggle API → [[Power BI]] per il monitoraggio automatico giornaliero di dataset rilevanti.
*   Sperimentare dashboarding basato su [[Intelligenza artificiale generativa|AI]] (es. Power BI Copilot) per ridurre il tempo di creazione delle dashboard.

## 🔗 Connessioni e Pattern

- [[Blockchain]]
- [[Dax]]
- [[Osint]]
- [[Power Automate]]


- [[--]]
F/I/H
- [[--]]
