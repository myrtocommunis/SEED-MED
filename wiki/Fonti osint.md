---
title: "Fonti osint"
tags: ["OSINT", "processed", "fonti", "valutazione", "[[NATO]]-admiralty"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Fonti osint

## 🎯 Sintesi Strategica

Il catalogo delle **Fonti OSINT** costituisce l'infrastruttura di approvvigionamento grezzo dell'Intelligence a fonte aperta. Diversamente dal senso comune, che equipara l'OSINT ai soli "motori di ricerca", la tassonomia formale si estende su molteplici domini (commerciali, governativi, accademici, underground). Tuttavia, l'accesso a una fonte è proceduralmente secondario rispetto alla sua **Valutazione (Source Evaluation)**. Senza un solido protocollo per misurare l'affidabilità originaria e la validità del dato (es. sistema [[NATO]] Admiralty), l'intero ciclo analitico collassa sotto il peso della [[Disinformazione]] e delle allucinazioni metodologiche.

## 📚 Contesto e Definizioni

La geografia delle fonti si ramifica nei seguenti cluster primari:
1.  **Media Tradizionali e Nuovi (News Intelligence):** Testate giornalistiche (White information), agenzie di stampa, blog iper-partigiani e network radio/televisivi.
2.  **Dati Governativi e Pubblici (Public Records):** Dati catastali, visure camerali societarie, sentenze giudiziarie, bollettini doganali (es. Importgenius), registri di volo marittimi e aerei (es. ADS-B Exchange, Marinetraffic).
3.  **Letteratura Grigia (Grey Literature):** Documenti non pubblicati commercialmente (Tesi di laurea, report aziendali trapelati, archivi accademici, manuali tecnici).
4.  **Social Media Intelligence (SOCMINT):** UGC (User Generated Content) proveniente da X, Tiktok, Facebook, Linkedin, nonché forum specialistici, board anonime (4chan) e canali Telegram.
5.  **Dati Commerciali (Grey/Commercial Info):** Database strutturati accessibili tramite licenza o paywall (Lexisnexis, database di intelligence spaziale, registri di data-broker).

## 📊 Dati, Tecnologie e Metriche

Acquisita l'informazione, l'analista militare e civile utilizza il **Sistema di Valutazione [[NATO]] Admiralty** (Stanag 2022) per pesare il dato, assegnando un codice alfanumerico (da A1 a F6):
*   **Affidabilità della Fonte (Da A a F):** Giudica la "storia" della sorgente. (A = Completamente Affidabile; F = Affidabilità non valutabile).
*   **Validità dell'Informazione (Da 1 a 6):** Giudica il frammento specifico incrociandolo con altri dati già confermati. (1 = Confermata da altre fonti indipendenti; 6 = Veridicità non valutabile).
*Un'informazione marcata "A6" proviene da una fonte storica ineccepibile, ma contiene un dato che non può essere ancora corroborato sul campo.*

## 🔍 Analisi Operativa ed Applicazioni OSINT

La gestione operativa delle fonti richiede pratiche di mitigazione e preservazione:
*   **Triangolazione:** L'obbligo metodologico di corroborare un'informazione critica attraverso almeno tre fonti indipendenti e *non correlate* tra loro. (Se tre giornali citano la medesima agenzia di stampa, si tratta di un'unica fonte, non di tre).
*   **Chain of Custody (Catena di Custodia):** L'acquisizione volatile (una pagina web può essere cancellata in secondi). Gli analisti devono congelare la prova tramite archiviazione forense (es. Wayback Machine, [[Archive.today]], Hunchly) generando hash crittografici per mantenere il valore legale dell'evidenza (soprattutto in ambito di *Human Rights Investigations* o procure legali).

## 🔮 Lacune Informative e Prossimi Passi

*   **Data Decay e Link Rot:** Il rapido decadimento dei link nel web aperto. Si stima che circa il 30% delle fonti aperte citate in documenti istituzionali diventi un "link rotto" (404) entro 5 anni dalla pubblicazione.
*   **Inquinamento Sintetico (Synthetic Poisoning):** Con l'esplosione dell'[[Intelligenza artificiale generativa]], le fonti primarie (come blog, recensioni o articoli accademici minori) vengono sommerse da contenuti generati interamente da AI senza revisione umana, falsando i processi automatizzati di data scraping e analisi semantica.

## 🔗 Connessioni e Pattern

- [[Osint]]
- [[Fact-checking]]
- [[Disinformazione]]
- [[Intelligenza artificiale generativa]]
- [[Dashboarding con ai]]

- [[--]]
F/I/H
- [[--]]
