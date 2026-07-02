---
title: Metodologia osint
tags:
- OSINT
- processed
- metodologia-osint
date: '2026-05-15'
status: draft
depth: standard
sources: '1'
tipo: concetto
---

# Metodologia osint

## 🎯 Sintesi Strategica

La metodologia OSINT (Open Source Intelligence) rappresenta l'approccio strutturato per la raccolta, l'elaborazione, l'analisi e la disseminazione di informazioni derivanti da fonti pubblicamente accessibili. Essa integra una tassonomia dei dati che evolve da fatti grezzi a conoscenza validata, un ciclo operativo in sei fasi e tecniche fondamentali come l'analisi della Digital Footprint, l'uso di Selectors e Pivoting e l'applicazione di schemi di targeting. Questi fondamenti costituiscono la base per discipline avanzate e per la produzione di intelligence strategica.

## 📚 Contesto e Definizioni

La metodologia OSINT si fonda su un insieme di principi e processi volti a trasformare dati aperti in intelligence fruibile. Al centro di questo processo vi è una chiara tassonomia delle informazioni e un ciclo operativo ben definito.

### Tassonomia delle Informazioni ([[NATO]] + [[Berkeley Protocol]])

La classificazione delle informazioni è cruciale per comprendere il valore e l'affidabilità dei dati raccolti:

| Livello | Definizione |
|---|---|
| Data | Fatti grezzi, non interpretati. |
| Information | Dati interpretati e contestualizzati, con significato. |
| Knowledge | Informazioni arricchite da esperienza e intuizione. |
| Open Source Data | Dati generici accessibili pubblicamente. |
| Open Source Information | Dati filtrati e conclusivi derivanti da fonti aperte. |
| **OSINT** | Informazioni filtrate e analizzate per uno scopo specifico. |
| **Validated OSINT** ([[NATO]]) | OSINT confermato da fonti non-OSINT o da fonti ritenute affidabili. |

### Ciclo OSINT

Il processo metodologico si articola in sei fasi interconnesse, garantendo un approccio sistematico alla produzione di intelligence:
1.  **Pianificazione e Direzione**: Definizione dei bisogni informativi e degli obiettivi.
2.  **Raccolta**: Acquisizione di dati da fonti aperte, ma anche da altre discipline come HUMINT, SIGINT, IMINT, MASINT.
3.  **Elaborazione/Processing**: Raffinamento e organizzazione dei dati grezzi.
4.  **Analisi**: Interpretazione dei dati elaborati per estrarre significato e contesto.
5.  **Produzione**: Creazione di un output analitico strutturato.
6.  **Disseminazione + Feedback**: Distribuzione dell'intelligence prodotta e raccolta di riscontri per migliorare i processi futuri.

### Digital Footprint

La Digital Footprint rappresenta l'insieme delle tracce digitali lasciate da un'entità. Si distingue in:
*   **Attiva**: Informazioni pubblicate consapevolmente (es. post sui social media, articoli, dichiarazioni pubbliche).
*   **Passiva**: Dati generati senza intervento diretto del soggetto (es. metadati, politiche sulla privacy, dati da violazioni di sicurezza, archivi storici).

## 📊 Dati, Tecnologie e Metriche

L'applicazione della metodologia OSINT si avvale di tecniche specifiche e di un'ampia gamma di strumenti per la raccolta e l'analisi dei dati.

### Selectors e Pivoting

I *selectors* sono identificatori unici o quasi unici (es. nome reale, nickname, email, telefono, username, foto, dominio/URL, indirizzo fisico, azienda). Il *pivoting* è la tecnica di passare da un selector all'altro per espandere la ricerca e costruire un profilo più completo. Un esempio notevole è il "Caso Badin", dove il pivoting da un username ha condotto all'identificazione di un ufficiale GRU attraverso una sequenza di `username → email → breach → nome → social → luogo → azienda`.

### Targeting Schema

Uno schema di targeting aiuta a strutturare la raccolta di informazioni su un soggetto, coprendo diverse dimensioni:

| Dimensione | Domande Chiave |
|---|---|
| Chi è | Identità, paure, affetti, debolezze, cultura, ideologia |
| Cosa fa | Impiego, formazione, hobby, spostamenti, affiliazioni |
| Cosa usa | Dispositivi, social network, nickname, email, telefono |

### Strumenti OSINT Fondamentali

L'efficacia della metodologia è amplificata dall'uso di strumenti specializzati:

| Categoria | Strumenti Esemplificativi |
|---|---|
| Ricerca Persone | Pipl, Epieos, Molfar |
| Ricerca Username | Sherlock, Instant Username |
| Violazioni Dati | Have I Been Pwned, IntelligenceX |
| Immagini | Pimeyes, Yandex, Reverse Search |
| Informazioni Aziendali | Opencorporates, Companies House, SEC EDGAR |

## 🔍 Analisi Operativa ed Applicazioni OSINT

La metodologia OSINT trova applicazione in svariati contesti, dalla sicurezza nazionale all'investigazione aziendale. L'integrazione del ciclo OSINT con tecniche come il pivoting e l'uso di specifici strumenti permette di costruire profili dettagliati e di attribuire azioni a entità specifiche. Il "Caso Badin" illustra come un'applicazione rigorosa del pivoting possa portare a scoperte significative, collegando tracce digitali apparentemente disparate a un individuo. L'analisi operativa si concentra sull'interpretazione dei dati raccolti attraverso il targeting schema, identificando pattern e connessioni che altrimenti rimarrebbero nascoste.

## 🔮 Lacune Informative e Prossimi Passi

Nonostante la sua robustezza, la metodologia OSINT presenta aree di potenziale approfondimento. Attualmente, manca una chiara integrazione della tassonomia [[NATO]] ufficiale come documento primario di riferimento. Inoltre, casi studio emblematici come il "Caso Badin" meriterebbero un'analisi investigativa dedicata per estrarre ulteriori insegnamenti metodologici. Infine, una distinzione più netta tra PAI (Publicly Available Information) e CAI (Commercially Available Information), con esempi di confine, potrebbe arricchire la comprensione delle fonti.

## 🔗 Connessioni e Pattern

- [[Applicazioni osint]]
- [[Classificazione]]
- [[Disseminazione]]
- [[Intelligence strategica]]
- [[Sicurezza nazionale]]
- [[Strumenti osint]]


- [[--]]
F/I/H
- [[--]]
