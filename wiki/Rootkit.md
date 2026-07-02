---
title: "Rootkit"
tags: ["OSINT", "processed", "rootkit", "malware", "persistenza", "stealth"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Rootkit

## 🎯 Sintesi Strategica

Un **Rootkit** è la forma più insidiosa, invisibile e profonda di [[Malware]] esistente. Il suo scopo principale non è fare danni immediati, ma mascherare l'esistenza di altri programmi malevoli o mantenere un accesso occulto continuo (Backdoor/Persistenza) a un computer compromesso, nascondendosi agli occhi del sistema operativo stesso, agli amministratori di rete e agli antivirus tradizionali. È lo strumento prediletto dai gruppi di spionaggio informatico di alto livello ([[Apt]]).

## 📚 Contesto e Definizioni

Il termine deriva da "Root" (l'account amministratore di massimo privilegio su Linux) e "Kit" (il set di strumenti).
Mentre un normale virus (come un [[Ransomware]]) altera i file e fa "rumore" allertando il [[Blue team]], un Rootkit si inietta direttamente nel cuore del sistema operativo (il Kernel). Se un antivirus chiede al sistema operativo: "Fammi la lista dei processi in esecuzione", il Rootkit intercetta la domanda e cancella il proprio nome dalla lista prima che venga mostrata, rendendosi letteralmente invisibile a livello logico.

## 📊 Dati, Tecnologie e Metriche

Nelle indagini di Digital Forensics, rilevare un Rootkit è estremamente complesso (poiché non ci si può fidare delle risposte fornite dal sistema infetto). Gli investigatori e i cacciatori di minacce ([[Cyber threat intelligence]]) devono avviare il computer da una memoria esterna (Live USB) per ispezionare l'hard disk senza eseguire il sistema operativo corrotto, oppure si affidano all'ispezione della memoria RAM tramite dump di memoria. I Rootkit più letali (Firmware/Bootkit) infettano direttamente la scheda madre del PC (BIOS/UEFI), sopravvivendo perfino alla formattazione totale del disco rigido.

## 🔗 Connessioni e Pattern

- [[Malware]]
- [[Apt]]
- [[Blue team]]
- [[--]]
F/I/H
- [[--]]
