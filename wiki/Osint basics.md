---
title: Osint basics
tags:
- OSINT
- processed
- osint-basics
date: '2026-05-15'
status: draft
depth: standard
sources: '1'
tipo: concetto
---

# Osint basics

## 🎯 Sintesi Strategica

L'OSINT (Open Source Intelligence) rappresenta la disciplina di raccolta, elaborazione e analisi di informazioni pubblicamente disponibili per generare intelligence azionabile. Non si tratta di semplice raccolta di dati, ma di un processo strutturato che trasforma fatti grezzi in conoscenza contestualizzata e mirata a rispondere a specifiche domande informative. La sua efficacia è amplificata dall'uso di tecniche avanzate come i [[Google dorks]], l'esplorazione di archivi storici come la [[Wayback machine]] e l'impiego di motori di ricerca specializzati come Shodan. L'applicazione dell'OSINT spazia dalla sicurezza nazionale alla prevenzione del riciclaggio di denaro ([[Aml-cft]]), dimostrando la sua versatilità e importanza strategica.

## 📚 Contesto e Definizioni

L'OSINT si fonda su due concetti chiave:

*   **Open Source Information**: Qualsiasi informazione pubblicamente disponibile che un individuo può osservare, acquisire o richiedere senza necessità di status legale speciale o accesso non autorizzato (OHCHR [[Berkeley Protocol]] 2022).
*   **OSINT (Open Source Intelligence)**: Informazione non classificata che viene deliberatamente scoperta, discriminata, distillata e disseminata per rispondere a una domanda specifica di intelligence.

La trasformazione da dato grezzo a intelligence operativa segue una gerarchia precisa:

1.  **Data**: Fatti privi di spiegazione o analisi.
2.  **Information**: Dati interpretati, con significato in un contesto.
3.  **Knowledge**: Informazione arricchita da esperienza e intuizione.
4.  **Open Source Data**: Dati generici pubblicamente accessibili.
5.  **Open Source Information**: Dati conclusivi filtrati da fonti aperte.
6.  **OSINT**: Informazioni filtrate e designate per uno scopo specifico di intelligence.
7.  **Validated OSINT ([[NATO]])**: OSINT confermato da una fonte non-OSINT o ritenuta affidabile.

Il processo di generazione di OSINT è ciclico e si articola in sei fasi interconnesse, note come [[Ciclo]]:
1.  Requisiti informativi
2.  Raccolta
3.  Processazione
4.  Analisi
5.  Disseminazione
6.  Feedback

## 📊 Dati, Tecnologie e Metriche

La raccolta e l'analisi OSINT si avvalgono di una vasta gamma di strumenti e tecniche:

*   **Google Dorks**: Query specializzate che sfruttano operatori avanzati dei motori di ricerca per scoprire informazioni o vulnerabilità. Il Google Hacking Database (GHDB) è un riferimento fondamentale per queste tecniche.
    *   **Operatori Principali**: `intext:`, `inurl:`, `allinurl:`, `intitle:`, `allintitle:`, `filetype:`, `site:`, `cache:`, `related:`.
    *   **Operatori Booleani**: `AND`, `OR`/`|`, `-`, `*`, `~`, `..`.
*   **Wayback Machine e [[Waymore]]**: Strumenti per accedere a versioni storiche di pagine web, utili per recuperare contenuti rimossi o per il profiling digitale. [[Waymore]] integra anche [[Common Crawl]], Alien Vault OTX e URLScan.
*   **Motori di Ricerca Specializzati**: Piattaforme come Dehashed (credenziali leakate), Securitytrails (DNS), ExploitDB, Zoomeye, Shodan (dispositivi IoT), Grayhatwarfare (S3 buckets), Fofa, LeakIX, DNSDumpster, Fullhunt, Alienvault, CENSys, IntelligenceX (Tor/I2P/leaks), CRT.sh, Wigle (Wifi), Hunter (email), Greynoise, URLScan.
*   **Spiderfoot**: Un tool di automazione OSINT per la raccolta di informazioni su un target, impiegato nella ricognizione, threat intelligence e cybersecurity.
*   **Pastebin e Github**: Fonti preziose per la scoperta di contenuti, la rilevazione di fughe di dati, la threat intelligence, la ricerca e l'analisi di codice o script.
*   **Analisi dei Social Media (es. Twitter/X)**: L'analisi della struttura dei tweet (testo, username, timestamp, metriche di engagement, hashtag, menzioni, allegati, link, posizione, ID) e l'applicazione di metriche di [[Reti sociali]] (SNA) come Degree Centrality, Betweenness, Closeness, Eigenvector, Clustering Coefficient, [[PageRank]], Reciprocity e Community Detection, permettono di identificare nodi chiave e pattern in reti di disinformazione o attività illecite.

## 🔍 Analisi Operativa ed Applicazioni OSINT

L'OSINT trova applicazione critica in diversi settori, in particolare nella prevenzione del riciclaggio di denaro e del finanziamento del terrorismo (AML/CFT):

*   **Applicazioni per le FIU (Financial Intelligence Units)**:
    *   **Entity Enrichment**: Validazione di identità e identificazione di società di comodo (shell companies).
    *   **Network Mapping**: Collegamento tra beneficial owners e intermediari per mappare reti complesse.
    *   **Behavioral Profiling**: Confronto tra stile di vita e reddito dichiarato.
    *   **Geospatial Patterns**: Analisi delle transazioni in relazione a zone di conflitto o sanzionate.
*   **Casi Studio Rilevanti**:
    *   **FinCEN Files**: La fuga di oltre 2.100 Suspicious Activity Reports (SAR) ha rivelato transazioni sospette per un valore di 2 trilioni di USD, evidenziando l'ampiezza delle attività illecite e il ruolo dell'OSINT nella loro esposizione.
    *   **Panama Papers**: La divulgazione di 11.5 milioni di documenti da Mossack Fonseca ha svelato l'uso sistematico di società offshore per elusione fiscale e riciclaggio.

## 🔮 Lacune Informative e Prossimi Passi

Nonostante la sua efficacia, l'OSINT presenta aree che richiedono continua attenzione e sviluppo:

*   **Validazione delle Fonti**: La natura "open source" delle informazioni richiede un'attenta validazione per discernere dati affidabili da disinformazione o contenuti manipolati.
*   **Evoluzione Tecnologica**: Il panorama digitale è in costante mutamento; le tecniche e gli strumenti OSINT devono evolvere parallelamente per rimanere efficaci contro nuove minacce e piattaforme.
*   **Integrazione Multidisciplinare**: L'OSINT beneficia enormemente dall'integrazione con altre discipline di intelligence (HUMINT, SIGINT, GEOINT) per fornire un quadro informativo più completo e robusto.
*   **Sfide Etiche e Legali**: L'accesso e l'uso di informazioni pubbliche sollevano questioni etiche e legali complesse, che richiedono un quadro normativo e procedurale chiaro e aggiorNATO.

## 🔗 Connessioni e Pattern

- [[Aml-cft]]
- [[Applicazioni osint]]
- [[Community detection]]
- [[Intelligence operativa]]
- [[Sicurezza nazionale]]
- [[Threat intelligence]]


- [[--]]
F/I/H
- [[--]]
