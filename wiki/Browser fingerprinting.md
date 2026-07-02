---
title: "Browser fingerprinting"
tags: ["OSINT", "processed", "fingerprinting", "opsec", "tracciamento"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "3"
tipo: "concetto"
---

# Browser fingerprinting

## 🎯 Sintesi Strategica

Il **Browser Fingerprinting (Impronta digitale del Browser)** è una tecnica avanzata di tracciamento online che identifica univocamente un utente raccogliendo i parametri tecnici del suo browser. Nell'[[Osint]], rappresenta la minaccia più letale per l'[[Opsec]] dell'investigatore: sebbene una [[Vpn]] nasconda l'indirizzo IP, il Fingerprinting permette al bersaglio (o alle piattaforme social) di smascherare un [[Sock puppet]] o capire che un analista sta spiando l'infrastruttura nemica.

## 📚 Contesto e Definizioni

Quando visiti un sito web, il tuo browser fornisce autonomamente al server un set di metadati per "ottimizzare" la visualizzazione:
*   Risoluzione dello schermo, Fuso orario, Lingua del sistema.
*   Font installati nel PC (spesso rivelano se sei un designer, un programmatore o hai software governativo).
*   **Canvas Fingerprinting:** Il sito chiede al browser di disegnare una forma geometrica invisibile a schermo. A causa delle micro-differenze dell'hardware (Scheda Grafica), il disegno risulterà unico a livello di pixel, generando un "Hash" identificativo immutabile, anche in navigazione in Incognito.

## 📊 Dati, Tecnologie e Metriche

Se un analista usa due Sock Puppet (un estremista di destra e un dissidente) dallo stesso computer, Facebook incrocerà il Fingerprint e bannerà entrambi i profili istantaneamente per attività inautentica coordinata ([[Coordinated sharing behavior]]).
La mitigazione richiede "Browser Antidetect" (es. Multilogin, Gologin) o l'uso metodico di distinte [[Macchina virtuale]], che iniettano "rumore" nei Canvas Fingerprint creando identità hardware false ma credibili.

## 🔗 Connessioni e Pattern

- [[Opsec]]
- [[Sock puppet]]
- [[Macchina virtuale]]
- [[Vpn]]
- [[--]]
F/I/H
- [[--]]
