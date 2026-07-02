---
title: "Ciclo bi"
tags: ["OSINT", "processed", "business-intelligence", "data-analytics", "power-bi", "dax"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "1"
tipo: "concetto"
---

# Ciclo bi

## 🎯 Sintesi Strategica

Il **Ciclo di Business Intelligence (BI)** moderno applicato all'[[Osint]] rappresenta il passaggio dalla mera raccolta di dati grezzi alla generazione di *Data-Driven Intelligence* automatizzata. Mentre le tecniche OSINT tradizionali faticano a gestire enormi dataset (come registri di sanzioni internazionali, bilanci pubblici o transazioni cripto), l'integrazione di strumenti come **Power BI**, **DAX** e **Power Automate** permette di mappare network opachi e generare *alerting* in tempo reale. Il paradigma moderno non si limita a fotografare il passato, ma connette l'ingestione continua di dati open-source (es. Kaggle, Our World in Data, OpenBDAP) a flussi decisionali automatizzati e dashboard esplorative, fornendo all'analista un vantaggio informativo asimmetrico.

## 📚 Contesto e Definizioni

La Business Intelligence si è evoluta da semplici sistemi statici di reportistica (BI 1.0) a piattaforme self-service cloud integrate con AI (BI 3.0).

### La Triade dell'Intelligence sui Dati

Per evitare confusioni terminologiche, il framework operativo definisce tre domini distinti:
1.  **Business Intelligence:** Focus sul *Presente*. Risponde alla domanda: *"Cosa dobbiamo fare ora?"*. Esempio: Dashboard in tempo reale dei target SDN attivi.
2.  **Data Analytics:** Focus sul *Passato*. Risponde alla domanda: *"Perché è successo?"*. Esempio: Analisi dei pattern di evasione delle sanzioni storiche tramite esplorazione descrittiva.
3.  **Business Analytics:** Focus sul *Futuro*. Risponde alla domanda: *"Cosa succederà dopo?"*. Esempio: Previsione tramite algoritmi di Machine Learning delle prossime *shell companies* che un attore ostile potrebbe utilizzare.

## 📊 Dati, Tecnologie e Metriche

Il motore tecnologico di questo ciclo si basa sull'ecosistema Microsoft per la produttività analitica.

### Architettura del Ciclo Operativo

L'infrastruttura di Power BI organizza le informazioni in una gerarchia rigida:
*   **Workspace (Dossier Operativo):** Il contenitore primario di un'indagine.
*   **Dataset (Base Dati):** Le tabelle strutturate e normalizzate estratte dalle fonti.
*   **Report (Briefing Visivo):** Pagine multi-visualizzazione che sviscerano i dati.
*   **Dashboard (Situational Awareness):** Il pannello unico di monitoraggio con i KPI essenziali in tempo reale.

### DAX (Data Analysis Expression)

Il linguaggio computazionale che anima le dashboard. La sua potenza risiede nella gestione dei contesti di esecuzione:
*   **Row Context (Contesto di Riga):** Esecuzione della formula riga per riga (es. calcolare l'anomalia di ogni singola transazione).
*   **Filter Context (Contesto di Filtro):** Esecuzione della formula su un intero dataset dinamicamente filtrato (es. somma dei volumi transati solo verso la Russia nell'ultimo mese).
*   **Time Intelligence:** Funzioni avanzate (`TOTALYTD`, `SAMEPERIODLASTYEAR`, `DATEADD`) permettono all'analista di calcolare variazioni temporali e studiare pattern comportamentali prima e dopo eventi geostrategici critici (es. l'imposizione di una sanzione economica).

## 🔍 Analisi Operativa ed Applicazioni OSINT

L'elemento di rottura procedurale è costituito da **Power Automate**, che trasforma una dashboard statica in un sistema di intelligence attivo (Early Warning System).

### Automazione dei Flussi (Workflow)

L'analista può implementare tre tipologie di trigger:
1.  **Automatizzato:** Scatta al verificarsi di un evento. *(Esempio: Invia un alert al team investigativo quando l'OFAC aggiorna la lista SDN in un file condiviso).*
2.  **Pianificato:** Esecuzione temporale periodica. *(Esempio: Scarica automaticamente l'ultimo dataset di conflitti ACLED ogni mattina alle 06:00 e aggiorna la Power BI).*
3.  **Istantaneo:** Attivazione manuale a pulsante per generare immediatamente un report PDF di Due Diligence su un target specifico.

## 🔮 Lacune Informative e Prossimi Passi

*   **Gestione dei Dati Non Strutturati:** Il ciclo BI attuale eccelle con database relazionali (CSV, SQL). Sussiste un *gap* tecnologico per l'ingestione nativa di informazioni testuali, report pdf o trascrizioni audio (OSINT non strutturata), che richiedono costosi step di pre-processing NLP prima di poter essere interrogati tramite DAX.
*   **Graph Database Integration:** Power BI non è ottimizzato per la *Network Analysis* profonda. È necessario sperimentare connettori personalizzati verso database a grafo come **Neo4j** per sfruttare algoritmi di centralità e identificare broker nascosti all'interno dei dataset finanziari ripuliti dal ciclo BI.

## 🔗 Connessioni e Pattern

- [[Elaborazione big data]]
- [[Tassonomia dei tools]]
- [[Cyber]]
- [[Intelligence finanziaria]]
- [[Dashboarding osint]]
- [[Machine learning]]

- [[--]]
F/I/H
- [[--]]
