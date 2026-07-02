---
title: "Network intelligence"
tags: ["OSINT", "processed", "sigint", "network-intelligence", "cyber"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "3"
tipo: "concetto"
---

# Network intelligence

## 🎯 Sintesi Strategica

La **Network Intelligence (DNI - Digital Network Intelligence)** rappresenta il dominio analitico in cui l'architettura tecnica di Internet incontra l'intelligence strategica. Nata storicamente in ambito SIGINT (Signals Intelligence), oggi la DNI e l'[[Osint]] convergono massicciamente grazie alla disponibilità di dati aperti sull'infrastruttura di rete globale (BGP, DNS, certificati SSL). Non si concentra sul *contenuto testuale* dei messaggi (chi dice cosa), ma sull'**infrastruttura di trasmissione** (come viaggia l'informazione, dove risiedono i server, quali percorsi di routing vengono alterati).

## 📚 Contesto e Definizioni

La topologia di Internet non è neutrale, ma è un terreno di scontro geopolitico. L'analista OSINT mappa i seguenti layer:
1.  **Level 1-3 (Infrastruttura Fisica e di Rete):** Analisi dei cavi sottomarini, degli Autonomous System Numbers (ASN) governativi e del protocollo di routing BGP (Border Gateway Protocol).
2.  **Level 4-7 (Trasporto e Applicazione):** Enumerazione delle porte aperte, validazione dei certificati crittografici X.509, e mappatura dei domini ([[Ip-dns intelligence]]).
3.  **Il Contesto Snowden:** Nel 2013, le rivelazioni di [[Edward Snowden]] hanno svelato programmi SIGINT massivi come **XKEYSCORE** della NSA, dimostrando che l'accesso ai nodi di dorsale (Backbone) permette l'intercettazione globale non mirata, alterando per sempre l'equilibrio tra privacy e [[Sicurezza nazionale]].

## 📊 Dati, Tecnologie e Metriche

Strumenti commerciali OSINT/Cyber permettono oggi indagini che dieci anni fa erano esclusiva delle agenzie a tre lettere:
*   **BGP Hijacking:** Il monitoraggio open-source delle tabelle di routing permette di scoprire se un attore statale (es. Cina o Russia) sta deviando illegalmente il traffico Internet occidentale verso i propri server per ispezionarlo prima di re-instradarlo a destinazione.
*   **CENSys e [[Shodan (motore di ricerca)]]:** L'analisi storica della rotazione dei certificati SSL permette di rintracciare i server *Command & Control* (C2) di gruppi APT anche quando cambiano continuamente indirizzo IP per eludere la detection.

## 🔍 Analisi Operativa ed Applicazioni OSINT

L'infrastruttura è "più lenta" dei dati che la attraversano: un account Twitter si crea in secondi, ma affittare server, registrare domini e configurare CDN (Content Delivery Networks) lascia una vasta impronta burocratica (Digital Exhaust) che l'analista DNI può inseguire:
*   Un sito di [[Disinformazione]] FIMI si finge una testata giornalistica locale americana indipendente, ma l'analisi dell'ASN e dei record DNS storici ([[Passive DNS]]) svela che l'IP risiede in un data center di San Pietroburgo e condivide lo stesso server fisico con altri 50 siti di disinformazione (Hosting condiviso).

## 🔮 Lacune Informative e Prossimi Passi

*   **Crittografia Pervasiva (Dark/Going Dark):** L'adozione massiccia dell'End-to-End Encryption (E2EE) su Whatsapp/Signal e del protocollo TLS 1.3 costringe l'intelligence a spostarsi dall'analisi del *Payload* (i testi) all'esclusiva analisi dei *Metadati di Rete* (peso del pacchetto, tempistiche di connessione, volume di traffico).

## 🔗 Connessioni e Pattern

- [[Ip-dns intelligence]]
- [[Cyber]]
- [[Osint]]
- [[Sicurezza nazionale]]
- [[Tassonomia dei tools]]

- [[--]]
F/I/H
- [[--]]
