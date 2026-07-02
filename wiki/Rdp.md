---
title: "Rdp"
tags: ["OSINT", "processed", "rdp", "cyber", "ransomware", "accesso-remoto"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Rdp

## 🎯 Sintesi Strategica

Il **Protocollo RDP (Remote Desktop Protocol)** è uno strumento proprietario sviluppato da Microsoft che fornisce a un utente un'interfaccia grafica per connettersi a un altro computer su una connessione di rete (solitamente porta 3389). Pensato per permettere ai dipendenti di lavorare da casa e agli amministratori IT di riparare i server a distanza, l'RDP è ironicamente diventato la vulnerabilità strutturale numero uno nello spionaggio industriale ([[Apt]]) e nel dispiegamento di [[Ransomware]].

## 📚 Contesto e Definizioni

I criminali non hanno bisogno di scrivere virus sofisticati se l'azienda lascia la porta d'ingresso aperta e documentata. Quando i firewall non sono configurati correttamente e la porta RDP è esposta sull'Internet pubblico ([[Clear web]]), i Threat Actor utilizzano strumenti automatizzati per scansionare massivamente la rete (es. [[Nmap]] o [[Shodan (motore di ricerca)]]). Una volta trovato un server RDP aperto, eseguono attacchi di forza bruta (Brute-Force) provando milioni di password finché non entrano nel sistema come utenti legittimi.

## 📊 Dati, Tecnologie e Metriche

Gli "Initial Access Broker" (IAB) sono cybercriminali specializzati in [[Osint]] offensivo: la loro unica occupazione è identificare server RDP vulnerabili tramite Shodan, bucare la password e poi rivendere l'accesso "chiavi in mano" alle gang di Ransomware sul [[Darknet market]] per cifre che variano da 10 a 50.000 dollari in base all'importanza dell'azienda vittima.

## 🔗 Connessioni e Pattern

- [[Ransomware]]
- [[Shodan (motore di ricerca)]]
- [[Apt]]
- [[Nmap]]
- [[--]]
F/I/H
- [[--]]
