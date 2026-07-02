---
title: "Signal"
tags: ["OSINT", "processed", "signal", "e2ee", "opsec", "privacy"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Signal

## 🎯 Sintesi Strategica

**Signal** è un'applicazione di messaggistica istantanea open-source (gestita da una fondazione no-profit) considerata all'unanimità l'attuale Gold Standard per la Sicurezza operativa (OPSEC) e la privacy delle comunicazioni. Utilizza nativamente il protocollo di [[Crittografia end-to-end]] (Signal Protocol, poi adottato anche da Whatsapp e Skype) per cifrare chiamate, messaggi e file multimediali, rendendoli inaccessibili a chiunque non sia il destinatario desigNATO.

## 📚 Contesto e Definizioni

La supremazia di Signal su app commerciali come Whatsapp non risiede tanto nella cifratura del testo, ma nella gestione dei **[[Metadati]]**. Whatsapp è di proprietà di Meta ([[Capitalismo delle piattaforme]]) e registra chi chiami, quando, per quanto tempo e la tua posizione (dati vitali per l'[[Osint]] e vendibili alle autorità). Signal minimizza strutturalmente i metadati: i suoi server non sanno con chi stai chattando e mantengono solo la data di creazione dell'account e l'ultima connessione.

## 📊 Dati, Tecnologie e Metriche

Per proteggere i Whistleblower e gli analisti in territorio ostile, Signal include il **Sealed Sender** (Mittente Sigillato), una tecnologia che cifra anche le identità del mittente e del destinatario, impedendo perfino al server centrale di ricostruire la mappa delle relazioni sociali (SNA) degli utenti. Questa resilienza strutturale la rende l'app preferita (talvolta obbligatoria) per le comunicazioni non classificate negli ambienti di intelligence militare.

## 🔗 Connessioni e Pattern

- [[Crittografia end-to-end]]
- [[Metadati]]
- [[Opsec]]
- [[Whistleblower]]
- [[--]]
F/I/H
- [[--]]
