---
title: "Macchina virtuale"
tags: ["OSINT", "processed", "vm", "opsec", "sandboxing"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "3"
tipo: "concetto"
---

# Macchina virtuale

## 🎯 Sintesi Strategica

Una **Macchina Virtuale (VM)** è l'emulazione software di un intero sistema informatico indipendente, eseguito all'interno della macchina fisica dell'analista (Host). Nell'ecosistema [[Osint]] e [[Cyber]], la VM costituisce la muraglia di isolamento primario (Sandboxing): permette al ricercatore di navigare nel [[Dark web]], scaricare file sospetti o eseguire malware investigativo senza alcun rischio di infettare o compromettere il proprio disco rigido personale.

## 📚 Contesto e Definizioni

Per mantenere l'[[Opsec]], le unità investigative non operano mai sul sistema operativo base (es. Windows personale dell'analista). Utilizzano hypervisor (Virtualbox, VMware) per creare ambienti "effimeri".
*   Ambienti OSINT standard includono distribuzioni Linux pre-configurate come **Kali Linux**, **Tracelabs OSINT VM** o **CSI Linux**, che contengono già centinaia di strumenti open-source preinstallati (Maltego, Sherlock, Recon-ng).

## 📊 Dati, Tecnologie e Metriche

L'uso delle VM annienta il rischio di contaminazione incrociata. La tecnica aurea è l'uso degli **Snapshots (Istantanee)**:
1. Si crea una VM pulita.
2. Si esegue un'indagine su siti di [[Disinformazione]] (probabilmente infetti da exploit).
3. A fine giornata, si "riavvolge" la VM allo Snapshot pulito del giorno prima, polverizzando qualsiasi traccia di cronologia, cookie traccianti (vedi [[Browser fingerprinting]]) o malware, tornando alla "Tabula Rasa".

## 🔗 Connessioni e Pattern

- [[Opsec]]
- [[Cyber]]
- [[Dark web]]
- [[--]]
F/I/H
- [[--]]
