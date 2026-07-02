---
title: Citazione delle fonti
tags:
- OSINT
- processed
- citazione-delle-fonti
date: '2026-05-15'
status: draft
depth: standard
sources: '1'
tipo: concetto
---

# Citazione delle fonti

## 🎯 Sintesi Strategica

L'**ICS 206-01** (*Intelligence Community Standard*), emaNATO dal *Director of National Intelligence* (DNI) degli Stati Uniti il 12 dicembre 2024, rappresenta un tentativo ambizioso di professionalizzazione e Standardizzazione della disciplina [[Osint]] a livello normativo internazionale. Questo standard obbliga tutti gli elementi della Intelligence Community (IC) statunitense a citare e referenziare con formati uniformi le Publicly Available Information (PAI), le Commercially Available Information (CAI) e gli [[Osint]] in ogni prodotto analitico dissemiNATO.

Il salto qualitativo rispetto al predecessore del 2017 è triplice:
1.  **Nessuna distinzione di classificazione tra le fonti**: PAI, CAI e OSINT sono integrati con citazioni full-structured (*SRC — Source Reference Citation*).
2.  **Tassonomia dei prodotti OSINT autonomi**: Distinzione netta tra *stand-alone analytic product* (posizione analitica coordinata IC) e *other stand-alone product* (osservazioni fattuali, curation, geolocalizzazione).
3.  **Trasparenza Intelligenza Artificiale (AI)/ML obbligatoria**: Output di AI, sistemi di [[Computer vision]], prompt generativi e dataset di addestramento devono essere citati come elementi dell'SRC.

Questa normativa ha una conseguenza geostrategica significativa, plasmando i framework OSINT di [[NATO]], UE e alleati Five Eyes, rendendo la **tracciabilità delle fonti** un requisito fondamentale.

| Categoria | Definizione ICS 206-01 | Impatto Operativo |
|---|---|---|
| **PAI** | Informazioni pubblicate o trasmesse per il consumo pubblico, accessibili online o via abbonamento, osservabili da chiunque | Copre news, open data governativi, report, social pubblici, blog |
| **CAI** | Dati/informazioni normalmente venduti, affittati o concessi in licenza a membri del pubblico o entità non governative | Copre database commerciali, dataset a pagamento, report di settore premium |
| **OSINT** | Intelligence derivata esclusivamente da PAI/CAI che risponde a priorità/requisiti/lacune specifiche dell'intelligence | Non è "informazione" ma "intelligence" — il valore aggiunto analitico è il discriminante |
| **AI** | Sistema basato su macchine che, per obiettivi definiti dall'uomo, formula previsioni/raccomandazioni/decisioni che influenzano ambienti reali o virtuali (15 U.S.C. § 9401(3)) | Ogni sistema AI utilizzato in un workflow analitico IC va citato nell'SRC come "fonte di valore aggiunto" |

## 📚 Contesto e Definizioni

La standardizzazione della citazione delle fonti nell'Intelligence Community (IC) statunitense, culminata nell'ICS 206-01, si inserisce in un contesto normativo e operativo ben definito.

### Base Gerarchica della Standardizzazione IC

L'ICS 206-01 non emerge nel vuoto, ma è il risultato di una catena di autorità:
*   **1. Statuto**: Il *National Security Act (1947)* definisce la IC e l'autorità del Presidente.
*   **2. Esecutivo**: L'*Executive Order 12333* (*United States Intelligence Activities*) crea il quadro giuridico per direttive e standard IC, fornendo la base per il DNI di emanarli.
*   **3. Direttivo**: L'*Intelligence Community Directive (ICD) 206* conferisce autorità vincolante all'ICS 206-01 sui prodotti analitici IC.
*   **4. Standard**: L'*ICS 206-01* (12 dicembre 2024) fornisce le linee guida operative per la citazione di Publicly Available Information (PAI), Commercially Available Information (CAI) e [[Osint]], sostituendo la versione del 26 settembre 2017.
*   **5. Implementativi**: Le *ICD 501* e *ICD 504* (sulla scopribilità), insieme alle *Functional Manager Guidelines* e ai *NOSC/DOSC*, assicurano l'interoperabilità, la formazione e la conformità annuale.

### Perché Ora?

La motivazione dichiarata dal DNI per questa revisione è la **crescita esponenziale** delle fonti PAI/CAI e l'utilità crescente dell'Intelligenza Artificiale (AI) nel ciclo intelligence. Tre forze motrici principali:
1.  **Volume**: Oltre 400 MB di dati generati quotidianamente a livello globale, con una quota crescente di fonti PAI e CAI strutturate e semistrutturate.
2.  **Strumentalizzazione**: Attori statali e non statali utilizzano PAI/CAI e [[Intelligenza artificiale generativa]] per [[Disinformazione]] e interferenze, rendendo la tracciabilità delle fonti un'esigenza critica di contro-intelligence.
3.  **Standardizzazione cross-agency**: Fino al 2024, ogni agenzia IC (CIA, NSA, DIA, FBI, NGA, ecc.) utilizzava convenzioni di citazione interne diverse, rendendo difficile garantire riproducibilità e audit tra gli elementi IC.

## 📊 Dati, Tecnologie e Metriche

L'ICS 206-01 introduce requisiti stringenti e dettagliati per la gestione e la citazione delle fonti, con un focus particolare sulle tecnologie emergenti.

### Quattro Pilastri Obbligatori dello Standard

| Pilastro | Obbligo | Sanzione Non Conformità |
|---|---|---|
| **Citazione** (Citation) | PAI, CAI, OSINT citati con SRC uniforme in **tutti** i prodotti analitici disseminati (Appendice B) | Rischio di rigetto del prodotto dal DD/MI (Deputy Director / Management Integration) |
| **Scopribilità** (Discoverability) | Citazioni recuperabili con tag comuni secondo ICD 501 e ICD 504 per interoperabilità | Impossibilità di audit e verifiche annuali da parte IC OSINT Executive |
| **Conservazione** (Preservation) | Sorgenti PAI/CAI dinamiche che influenzano il messaggio chiave conservate ≥ 1 anno (o per orizzonte NIE / 5 anni) | Perdita di tracciabilità per audit e future revisioni analitiche |
| **Formazione** (Training) | Formazione IC secondo Appendice B + requisiti Functional Manager OSINT | Non conformità valutata nei drill annuali di IC OSINT Executive |

### Prodotti OSINT Autonomi: Distinzione Fondamentale

Questa è la separazione operativa più rilevante per gli analisti [[Osint]]:

| Tipo di Prodotto | Descrizione | Esempio |
|---|---|---|
| **Stand-Alone OSINT Analytic Product** | Rappresenta la **posizione analitica coordinata** di un elemento IC, derivata esclusivamente da PAI/CAI/OSINT. Include "we assess", "OSINT reveals", argomenti basati su tesi e giudizi ricercati | NIA (National Intelligence Assessment) basato su OSINT, valutazione coordinata di una minaccia |
| **Other Stand-Alone OSINT Product** | Fornisce **principalmente osservazioni fattuali** e contenuti informativi: geolocalizzazione, traduzione, riassunti, curation, annotazioni. Non è posizione analitica coordinata | Report di geolocalizzazione di immagini SATellitari, database di eventi, curation giornalistica |

### Ruoli e Responsabilità: Chi Fa Cosa

| Ruolo | Entità | Responsabilità Primaria |
|---|---|---|
| **IC OSINT Executive** | ODNI (Office of the Director of National Intelligence) | Implementazione uniforme; analisi annuali sui repository IC per verificare conformità |
| **Capi degli Elementi IC** | CIA, NSA, DIA, FBI, NGA, NRO, DEA, DHS, ecc. | Implementazione nelle aree analitiche e di raccolta; sviluppo formazione e processi interni |
| **Functional Manager per OSINT** | DesigNATO IC | Guida il National Open Source Committee (NOSC); sviluppa apprendimenti per futuri aggiornamenti |
| **NOSC / DOSC** | National Open Source Council / Defense Open Source Council | Promuove conformità IC; DOSC coordina implementazione nella Defense Intelligence Enterprise |
| **Professionisti Intelligence** | Analisti, raccoglitori, curatori | Rispetto ICS, aggiornamento best practice, consapevolezza implicazioni privacy/libertà civili |

### Source Reference Citation (SRC): ANATOmia di una Citazione Uniforme

L'SRC è l'elemento innovativo dell'ICS 206-01. Ogni citazione è un insieme specificato di elementi informativi fattuali su una fonte, presentato in formato uniforme in una nota a piè di pagina, che permette ai lettori di localizzare e recuperare la fonte.

**Struttura tecnica dell'SRC** (Appendice B):

| Elemento SRC | Funzione | Esempio |
|---|---|---|
| **Classificazione e Marcatura** | Classificazione complessiva + marcature di porzione secondo ICD 206 | UNCLASSIFIED // FOUO |
| **Separazione con Pipe** | Elementi separati da `|` per differenziare categorie di metadati | `|` |
| **Source Descriptor** | Caratterizzazione della fonte: qualità, credibilità, affidabilità, stato (valutato/non valutato), strumenti AI | Bias moderato; fonte governativa primaria; CV LATC v2.1 usato |
| **SRC Descrittiva vs Generica** | Default descrittiva; generica solo se giustificata da esigenze di sicurezza basate su prove | URL omesso per sicurezza operativa; giustificazione documentata |

### AI, ML, CV e GAI: La Rivoluzione della Trasparenza Computazionale

L'ICS 206-01 introduce requisiti di citazione specifici per quattro classi di tecnologia emergente:

**1. Sistemi di [[Computer vision]]**

| Campo Obbligatorio | Dettaglio |
|---|---|
| Tipo di sistema | CV, GIOINT, HUMINT-assisted, ecc. |
| Nome del modello | Es. "LATC" (likely "Large Area Target Classifier") |
| Spiegazione non tecnica | Cosa fa il sistema in linguaggio analitico |
| Precisione e Recall (%) | Metriche di performance del modello |
| Impostazioni rilevanti | Threshold, parametri di configurazione |
| Dati di addestramento | Volume, tipologia, provenienza del training set |
| Versione software | Numero di versione del modello |
| Link repository | Github o equivalente per riproducibilità |
| Data di utilizzo | Periodo esatto in cui il sistema è stato applicato |

> **Esempio concreto dall'ICS**: `CV System LATC, trova gru in immagini elettro-ottiche, Precisione 90% – Recall 75%, addestrato su 2.000 immagini, Versione 2.1, usato 1-5 luglio 2024.`

**2. [[Intelligenza artificiale generativa]] / [[Large language model]]**
A causa della stocasticità degli output (la stessa richiesta produce risultati diversi), i requisiti sono:

| Campo Obbligatorio | Dettaglio |
|---|---|
| Piattaforma / modello | Es. "TalkXYZ", ChatGPT, Claude, Gemini |
| Prompt completo | La richiesta esatta inviata al modello |
| Parametri rilevanti | Temperature, top-p, max tokENS, ecc. |

> **Esempio concreto**: `TalkXYZ, prompt: "Genera un rapporto sulla città di Pechino. Scrivi in tono formale. Includi citazioni da National Geographic."`

**3. Qualità dei Dati AI**
Quando il volume di PAI/CAI rende impossibile la validazione manuale di ogni dato, l'ICS richiede di documentare le caratteristiche di performance e i dati di addestramento per garantire riproducibilità e trasparenza — senza etichettare wholesale come "non valutato". Questo è un cambio di paradigma: il "non valutato" diventa l'eccezione giustificata, non la norma.

**4. Source Descriptor per Strumenti e Servizi AI**
L'ICS estende la catena di citazione agli strumenti di raccolta, interfacce di ricerca e servizi di visualizzazione che forniscono analisi a valore aggiunto, raccomandazioni o previsioni, specialmente se assistiti da AI/ML/CV:

| Livello di Citazione | Cosa Citare |
|---|---|
| **Strumenti di Raccolta** | Nome del tool, se assistito da AI/ML/CV, version |
| **Database Commerciali** | Nome, contenuto, se richiede login, provenienza |
| **Fornitori Terzi** | Provenienza, proprietario dati originali, arricchimenti |
| **Dataset Multipli** | Criteri derivazione, keyword, lingua, intervallo temporale, versione, link diretto |

### Tecnologia Emergente e Flessibilità Futura

L'ICS riconosce esplicitamente la velocità di evoluzione dell'ecosistema open data:
> *"L'ambiente tecnologico open data evolve così rapidamente che nuovi tipi di dati, piattaforme e servizi emergeranno senza rientrare perfettamente nelle categorie elencate in questo ICS. Se emerge una nuova tecnologia o fonte, i creatori di contenuti OSINT e i raccoglitori di PAI/CAI devono citare gli aspetti critici della nuova tecnologia attraverso l'SRC, il Source Descriptor e il Source Summary Statement."*
Lo standard è quindi orientato al futuro, istituendo un framework di citazione generativo dove nuove tecnologie vengono "mappate" sulle categorie esistenti e segnalate via SRC/Descriptor.

## 🔍 Analisi Operativa ed Applicazioni OSINT

L'ICS 206-01 ha un impatto profondo sulle operazioni di [[Osint]] e sull'analisi all'interno della Intelligence Community (IC).

### Impatto sugli Analisti OSINT

La standardizzazione imposta dall'ICS 206-01 obbliga ogni analista [[Osint]] che opera nel perimetro IC o che produce intelligence per consumatori IC a conoscere e, possibilmente, adattare i propri prodotti a questo standard. Ciò significa che la mera raccolta di informazioni non è più sufficiente; la metodologia di citazione e la trasparenza diventano parte integrante del processo analitico.

### Trasparenza AI/ML Obbligatoria

L'introduzione di requisiti specifici per la citazione di Intelligenza Artificiale (AI), Machine Learning (ML), [[Computer vision]] e [[Intelligenza artificiale generativa]] è rivoluzionaria. Non si tratta più di una "best practice" ma di un obbligo vincolante. L'analista non può più utilizzare la "scatola nera" AI come un black box e presentare i suoi output come se fossero il proprio giudizio esclusivo. Ogni contributo algoritmico deve essere esplicitamente documentato, inclusi i prompt, i parametri e le metriche di performance dei modelli. Questo garantisce che il valore aggiunto dell'AI sia compreso e che le sue limitazioni siano riconosciute, migliorando la fiducia e la riproducibilità dell'analisi.

### OSINT come Disciplina Autonoma

La distinzione netta tra "Stand-Alone OSINT Analytic Product" e "Other Stand-Alone OSINT Product" è la prima volta che la Intelligence Community (IC) distingue formalmente il peso analitico del lavoro [[Osint]]. Le posizioni analitiche coordinate basate su OSINT acquisiscono lo stesso status di prodotti all-source, elevando il riconoscimento e l'importanza strategica dell'OSINT.

### Riproducibilità e Audit con SRC

La *Source Reference Citation (SRC)*, con la sua anatomia uniforme, è fondamentale per la riproducibilità e l'audit. Permette ai lettori di localizzare e recuperare le fonti originali, consentendo verifiche indipendenti e rafforzando la credibilità dell'analisi. La pratica del *Direct Link*, che collega ipertestualmente parole e frasi alla fonte sottostante, può ridurre l'uso delle note a piè di pagina pur mantenendo la tracciabilità.

### Applicazioni Reali

Le applicazioni operative includono:
*   **Valutazioni coordinate di minacce**: Basate esclusivamente su [[Osint]] con piena tracciabilità delle fonti.
*   **Report di geolocalizzazione**: Di immagini SATellitari o altri dati visivi, con citazione dettagliata dei sistemi di [[Computer vision]] utilizzati.
*   **Database di eventi e curation giornalistica**: Con metadati completi sulla provenienza e l'elaborazione delle informazioni.
*   **Analisi di [[Disinformazione]]**: Dove la tracciabilità delle fonti e degli strumenti AI impiegati per l'analisi è cruciale per smascherare campagne di influenza.

## 🔮 Lacune Informative e Prossimi Passi

Nonostante la completezza dell'ICS 206-01, la sorgente primaria rivela alcune lacune informative che meritano approfondimento.

### Lacune nella Sorgente

| Lacuna | Impatto | Azione Raccomandata |
|---|---|---|
| Non sono forniti esempi completi di SRC nel formato Pipe (Appendice B solo citata, non riprodotta) | MEDIO | Integrare con documentazione ufficiale ODNI o documenti Five Eyes per una comprensione pratica |
| Nessun riferimento a ICS analoghi per HUMINT/SIGINT/GEOINT/MEFINT | MEDIO | Verificare se esiste una "famiglia" di ICS 206 o se il 206-01 è uno standard autonomo per l'OSINT |
| Dettagli su sanzioni/conseguenze per non conformità non specificati | BASSO | Cercare la ICD 206 completa o la guida dell'IC OSINT Executive per comprendere le implicazioni |
| Nessun riferimento a formato di citazione per social media post/direct messages/stories | MEDIO | Verificare se rientra in PAI o richiede una categoria ad hoc, data la prevalenza di tali fonti nell'[[Osint]] |

### Prossimi Passi Analitici

1.  Recuperare il testo completo dell'**Appendice B** dell'ICS 206-01 per ottenere il formato SRC Pipe completo e gli esempi dettagliati.
2.  Verificare se la **UE** (European External Action Service, Europol Intelligence School) ha rilasciato standard analoghi post-2024, in linea con l'[[Ai act]] e il potenziale "bridging normativo".
3.  Mappare gli elementi IC e i loro **tool interni di citation** già in rollout, considerando che il 2025 è la fase di implementazione.

## 🔗 Connessioni e Pattern

- [[Ai act]]
- [[Applicazioni osint]]
- [[Disinformazione]]
- [[Intelligenza artificiale generativa]]
- [[Large language model]]
- [[Osint]]


- [[--]]
F/I/H
- [[--]]
