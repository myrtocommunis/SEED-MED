---
title: "Evasione forense"
tags: ["OSINT", "processed", "evasione-forense", "anti-forensics", "malware", "opsec"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Evasione forense

## 🎯 Sintesi Strategica

L'**Evasione Forense (Anti-Forensics)** è l'insieme delle tecniche utilizzate dai cybercriminali, sviluppatori di [[Malware]] e operatori coperti per eludere la rilevazione, ostacolare le indagini informatiche e distruggere le prove (Tracce Digitali) prima o dopo un crimine. È il contro-spionaggio applicato alla Digital Forensics: se l'analista [[Osint]] o il perito di polizia cerca di ricostruire i fatti, l'Evasione Forense rende i dati illeggibili, fuorvianti o assenti.

## 📚 Contesto e Definizioni

Le tecniche Anti-Forensi si dividono in diverse metodologie:
1.  **Distruzione dei dati (Wiping):** Sovrascrittura sicura dei settori dell'hard disk per rendere impossibile il recupero dei file cancellati.
2.  **Cancellazione dei Log (Log Tampering):** I gruppi [[Apt]], dopo aver rubato i dati dal server, cancellano chirurgicamente le righe di log di [[Elasticsearch]] in cui appariva il loro [[Indirizzo ip]], accecando il [[Blue team]].
3.  **Mascheramento (Obfuscation):** L'uso intensivo della [[Crittografia asimmetrica]], di [[Tor]] e della [[Steganografia]] per camuffare i dati in transito.
4.  **Armatura del Malware:** I virus rilevano se stanno girando dentro un ambiente di [[Sandboxing]] usato dai ricercatori; se se ne accorgono, non si eseguono, fingendosi software innocui.

## 📊 Dati, Tecnologie e Metriche

L'adozione di massa di sistemi amnesici come [[Tails]] è la forma di Anti-Forensics preventiva (Evasione a zero-impronta) più democratizzata. Non essendoci mai stata una scrittura fisica sul disco rigido della macchina, la polizia non troverà alcun Hash o cronologia del browser da analizzare durante un sequestro informatico. L'unico contrasto a queste tattiche per l'intelligence è catturare il dispositivo mentre è ancora acceso (Live Forensics) per estrarre la RAM in tempo reale.

## 🔗 Connessioni e Pattern

- [[Malware]]
- [[Tails]]
- [[Sandboxing]]
- [[Blue team]]
- [[--]]
F/I/H
- [[--]]
