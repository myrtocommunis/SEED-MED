---
title: "Command and control"
tags: ["OSINT", "processed", "c2", "cyber", "malware"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "3"
tipo: "concetto"
---

# Command and control

## 🎯 Sintesi Strategica

L'infrastruttura di **Command and Control (C2 o C&C)** è il server (o il network di server) operato da un criminale informatico (o da un gruppo [[Apt]]) che serve per mantenere le comunicazioni con i dispositivi infettati all'interno della rete della vittima. Nella [[Cyber kill chain]], la fase C2 è il momento in cui l'impianto malevolo "telefona a casa" per ricevere istruzioni su quali file crittografare o verso dove esfiltrare i dati rubati.

## 📚 Contesto e Definizioni

Neutralizzare il server C2 equivale a decapitare il nemico: i [[Malware]] o la [[Botnet]] sparsi per il mondo divengono istantaneamente inerti, come soldati senza radio. Per sfuggire al blocco da parte dei difensori, i criminali utilizzano tecniche avanzate:
*   **Domain Generation Algorithms (DGA):** Il malware genera matematicamente migliaia di domini fasulli al giorno. L'hacker ne registra solo uno reale. Il difensore non può bloccarli tutti senza disabilitare internet.
*   **Fast Flux:** Continua rotazione di indirizzi IP associati allo stesso nome a dominio.

## 📊 Dati, Tecnologie e Metriche

La [[Cyber threat intelligence]] (CTI) e le analisi [[Osint]] (tramite [[Ip-dns intelligence]] passiva) cercano ossessivamente gli indirizzi dei server C2 (Beaconing) per pubblicarli nei feed di threat intelligence. Se un'azienda rileva traffico di rete in uscita verso uno degli IP segnalati nel feed, ha la prova certa di un'infezione interna in corso.

## 🔗 Connessioni e Pattern

- [[Cyber kill chain]]
- [[Apt]]
- [[Botnet]]
- [[Malware]]
- [[--]]
F/I/H
- [[--]]
