---
title: Catena di custodia
tags:
- OSINT
- processed
- catena-di-custodia
date: '2026-05-15'
status: draft
depth: standard
tipo: concetto
---

title: "Catena di custodia"
tags: ["OSINT", "processed", "catena-di-custodia"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Catena di custodia

## 🎯 Sintesi Strategica

La **Catena di custodia** (Chain of Custody) è il fondamento epistemico, procedurale e giuridico dell'[[Osint]] contemporanea. Mutuata dalla Forensics digitale, rappresenta la documentazione cronologica e ininterrotta dell'acquisizione, conservazione, accesso, trasferimento e analisi di un'evidenza digitale. La sua urgenza nell'OSINT deriva dalla volatilità strutturale delle fonti aperte. Senza una catena di custodia robusta, l'analisi non è ricostruibile, l'evidenza non è ammissibile e il prodotto di intelligence non è credibile. Si articola in quattro pilastri: identificazione, preservazione, documentazione e autenticazione, ed è essenziale per elevare il dato grezzo a prova accountable, anche in contesti di [[Intelligenza artificiale generativa]] applicata alla reportistica.

## 📚 Contesto e Definizioni

La nozione canonica di catena di custodia nasce nella forense fisica, dove la tracciabilità di un campione è cruciale per la sua ammissibilità come prova. In ambiente digitale, la sua applicazione è più complessa a causa dell'infinita duplicabilità e modificabilità delle evidenze. La catena di custodia digitale è la **documentazione strutturata di chi ha toccato cosa, quando, come e perché**, dal momento zero della raccolta fino alla presentazione nel report finale. Il principio cardine è la **ricostruibilità integrale del percorso**, permettendo a un revisore esterno di ripercorrere ogni decisione e replicare ogni operazione.

La *ratio* della catena di custodia si fonda su tre livelli di accountability:
1.  **Epistemico**: Distingue l'evidenza autentica da artefatti introdotti dall'analisi.
2.  **Legale**: Tribunali e autorità richiedono metadati di tracciabilità per l'ammissibilità delle prove (cfr. Discoverability e [[Protocollo di Berkeley|Berkeley Protocol]]).
3.  **Deontologico**: Protegge l'analista da accuse di manipolazione e il soggetto target dalla contaminazione di prove.

Il [[Berkeley Protocol]] on Digital Open Source Investigations, sviluppato da UN-OHCHR e UC Berkeley School of Law, è lo standard internazionale di riferimento che ha elevato le prove OSINT allo stesso standard delle prove fisiche nei procedimenti internazionali, rendendo la catena di custodia un requisito imprescindibile.

## 📊 Dati, Tecnologie e Metriche

Il workflow operativo standardizzato della catena di custodia si articola in **quattro fasi sequenziali**:

1.  **Identificazione**: Registrare l'origine esatta dell'evidenza (URL canonico, account social con ID numerico, piattaforma, metadati originali). Principio di non-contaminazione: nessuna interazione che alteri lo stato dell'evidenza. Strumenti: schede di acquisizione testuali o database con timestamp ISO 8601, browser/OS, IP/VPN utilizzati.
2.  **Preservazione**: Congelare l'evidenza nel tempo. Include archiviazione su servizi di terzi ([[Wayback machine]], [[Archive.today]], Save Page Now), salvataggio locale del file con calcolo dell'[[Archiviazione forense|SHA-256]] hash all'ingestione, e screenshot temporizzato. Regola operativa: "archivia subito, analizza dopo".
3.  **Documentazione**: Costruire il log di ricerca. Documentare chi ha raccolto, come (metodo e tool), quando (timestamp UTC + locale), perché (rilevanza), e la catena di [[Osint]] che ha portato all'evidenza. Rende l'indagine replicabile da terzi. Strumenti: spreadsheet versionati, database, file Markdown in repository Git.
4.  **Autenticazione**: Garantire l'immutabilità a posteriori. Il file scaricato viene hashato con [[Archiviazione forense|SHA-256]]; lo stesso hash sarà ricalcolato in ogni passaggio successivo. Per evidenze con ammissibilità giudiziaria, si aggiungono firma digitale qualificata, timestamping certificato (eIDAS, RFC 3161) e conservazione in storage WORM (Write Once Read Many).

**Otto elementi obbligatori per ogni evidenza**:
1.  **Fonte**: URL canonico, piattaforma, account ID numerico, tipo di contenuto.
2.  **Data e ora con timezone**: Timestamp ISO 8601 di acquisizione, distinto dal timestamp dichiarato dalla fonte.
3.  **Metodo di acquisizione**: Screenshot manuale, scraping automatizzato, API call, download diretto, snapshot di archivio.
4.  **Strumenti e versioni**: Nome esatto e build del tool (es. `yt-dlp 2024.12.13`, `Chrome 130.0.6723.116`).
5.  **Hash [[SHA-256]]**: Del file primario e di eventuali derivati.
6.  **Modifiche effettuate**: Ogni alterazione documentata con timestamp e motivazione (cropping, OCR, traduzione). Regola: mai sovrascrivere l'originale.
7.  **Limiti della verifica**: Dichiarazione esplicita di cosa non è stato possibile verificare (es. EXIF rimosso, audio non originale). Si lega alla Admiralty Scale.
8.  **Confidence Level attribuito**: Secondo standard come [[Ics 206-01]] o scale interne, motivato dai sette punti precedenti.

La **struttura della cartella di progetto** è un dispositivo di catena di custodia. Una struttura disciplinata previene errori e garantisce la tracciabilità. Uno schema canonico prevede:
*   `00_Pianificazione/`: Obiettivi, query, scope.
*   `01_Dati_Grezzi/`: Deposito originale immutabile (es. `2026-05-07T14-32-18Z_tweet-id-12345.json` con `.sha256`).
*   `02_Elaborazione/`: Copie da archivi di terzi (Wayback URL, [[Archive.today]] URL).
*   `03_Analisi/`: Derivati analitici (trascrizioni, OCR, grafi), con hash di input e output.
*   `04_Report/`: Bozze e versioni finali del prodotto di intelligence.
*   `05_Archivio/`: Materiale superato o non rilevante ma da conservare.

## 🔍 Analisi Operativa ed Applicazioni OSINT

### Screenshot vs. Archiviazione di Terzo

Esiste una tensione operativa tra lo **screenshot manuale** e l'**archiviazione di terzo**. Lo screenshot è rapido, protegge l'[[Dalla pianificazione al targeting]] dell'operatore e cattura il rendering esatto, ma è nativamente manipolabile e distrugge metadati. L'archiviazione di terzo (es. [[Wayback machine]], [[Archive.today]]) offre timestamp non manipolabili e conservazione integrale della pagina, ma logga la richiesta (rischio OPSEC) e può fallire su contenuti dinamici. La soluzione pragmatica è la **doppia traccia**: screenshot + archiviazione di terzo + file originale con [[Archiviazione forense|SHA-256]], archiviati in cartelle separate, per coprire diversi vettori di attacco. Strumenti specializzati come Hunchly o FAW (Forensic Acquisition of Websites) sono usati per rigore elevato.

### Catena di Custodia nel Contesto Giudiziario Europeo

Il quadro giuridico europeo è multi-livello:
*   **[[Cedu]] (Art. 6 e 8)**: Richiede che le prove siano accessibili e contestabili dalla difesa, e limita la raccolta di dati pubblici.
*   **[[Quadro normativo osint|GDPR]] (Reg. UE 2016/679)**: Ogni dato personale raccolto richiede una base giuridica (Art. 6); la catena di custodia documenta scopo, base giuridica e minimizzazione.
*   **Giurisprudenza UE**: Sviluppa dottrina sull'utilizzabilità delle prove digitali.
*   **Standard nazionali**: Es. Decalogo Sabra in Italia, per contesti potenzialmente probatori.
*   **Normative settoriali**: [[NIS 2]] (cyber-resilienza), [[DORA]] (finanziario), [[Ai act]] (AI ad alto rischio).

Principi giudiziari pratici includono la Discoverability (accesso della difesa alla catena), la "locked evidence" (immutabilità dimostrata tramite hash) e l'"expert testimony" (l'analista deve difendere la metodologia).

### Court-admissible vs. Analytic-grade

Una distinzione cruciale è tra catena di custodia **court-admissible** e **analytic-grade**:
*   **Analytic-grade**: Standard per intelligence interna, giornalismo investigativo, ricerca. Richiede documentazione strutturata (8 elementi), hash [[Archiviazione forense|SHA-256]], archiviazione di terzo, struttura di progetto, log replicabile. Adeguato per dimostrare la qualità del lavoro, ma non sufficiente per tribunali ad alto rigore.
*   **Court-admissible**: Richiesto per procedimenti giudiziari. Include tutti i requisiti dell'analytic-grade più timestamping qualificato eIDAS, firma digitale qualificata, conservazione su storage WORM, acquisizione tramite tool certificati (es. FAW, Hunchly), e documentazione della catena tra ogni operatore. Il costo e la complessità sono significativamente maggiori.

La scelta dipende dal contesto e dalle risorse, ma è fondamentale dichiarare esplicitamente il livello adottato nel report.

### Catena di Custodia nei Sistemi [[Rag]] e AI-augmented

Nei sistemi [[Rag]] e negli agenti AI applicati all'OSINT, la catena di custodia si estende all'intera pipeline di retrieval, augmentation e generazione. Il problema centrale è la **citation verification**: un LLM deve dimostrare che ogni claim è derivato da un'evidenza identificabile nel corpus. L'estensione della catena comprende:
*   Tracciabilità del prompt (versione, parametri).
*   Tracciabilità del retrieval (chunk recuperati, embedding model).
*   Tracciabilità della generation (modello, versione, temperature).
*   Citation linking (ogni paragrafo linkato al chunk fonte).

Standard emergenti come [[Ics 206-01]] codificano lo schema di citazione minima per output AI. Il non-determinismo degli LLM è un caveat: la replicabilità tradizionale è parzialmente compromessa, richiedendo la documentazione di seed, l'intero output e il context window. La fiducia in un sistema AI è funzione della tracciabilità della sua catena evidenziale.

## 🔮 Lacune Informative e Prossimi Passi

Nonostante la robustezza del concetto, permangono alcune lacune informative e aree di sviluppo:
*   **Soglie quantitative**: Mancano definizioni chiare su tempi di conservazione, numero minimo di backup o strategie di rotazione.
*   **Integrazione enterprise**: Maggiore dettaglio sull'integrazione con strumenti di livello enterprise (storage S3 versioNATO, WORM storage certificato, timestamping eIDAS).
*   **Criteri ICC/CPI**: Non sono pienamente dettagliati i criteri specifici di ammissibilità per la Corte Penale Internazionale.
*   **Formato log di ricerca**: Standardizzazione del formato del log di ricerca per facilitare l'interoperabilità e la revisione.
*   **Scraping massivo**: Linee guida per la gestione della catena di custodia in contesti di acquisizione di migliaia di file.
*   **Fonti effimere**: Approfondimento sulla catena di custodia per contenuti altamente volatili (Stories, messaggi cancellati).
*   **Determinismo AI**: Metodologie avanzate per garantire e documentare il determinismo negli output degli LLM in contesti ad alto rigore.

## 🔗 Connessioni e Pattern

- [[Ai act]]
- [[Cedu]]
- [[Dalla pianificazione al targeting]]
- [[Ics 206-01]]
- [[Osint]]
- [[Retrieval-augmented generation]]


- [[--]]
F/I/H
- [[--]]
