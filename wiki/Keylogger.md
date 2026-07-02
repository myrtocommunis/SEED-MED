---
title: "Keylogger"
tags: ["OSINT", "processed", "keylogger", "spyware", "malware", "intercettazione"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Keylogger

## 🎯 Sintesi Strategica

Un **Keylogger** è un dispositivo hardware o un programma software progettato per registrare e intercettare clandestinamente ogni singolo tasto premuto (Keystroke) sulla tastiera di un computer o sullo schermo di uno smartphone. Essendo un attacco mirato al dispositivo fisico dell'utente finale (Endpoint), un keylogger neutralizza qualsiasi protezione di rete, bypassando brutalmente i protocolli di [[Crittografia end-to-end]] (poiché cattura il messaggio *prima* che il software lo cifri) e rubando facilmente l'accesso a qualsiasi [[Wallet]] crypto.

## 📚 Contesto e Definizioni

Esistono due macro-categorie:
1.  **Software Keylogger:** Varianti di [[Malware]] o Spyware installati tramite [[Attacco di phishing]]. Spesso si nascondono a livello profondo (kernel) o si agganciano alle API di Windows per registrare l'input e inviare il file di testo rubato al server di [[Command and control]] dell'hacker. Costituiscono la base operativa dei moduli [[Pegasus]].
2.  **Hardware Keylogger:** Piccoli adattatori fisici mascherati da chiavette USB, inseriti silenziosamente tra la tastiera e il computer. Spesso utilizzati per lo [[Spionaggio industriale]] (infilati sul retro del PC in ufficio da un [[Insider threat]]), eludono totalmente i software antivirus perché non c'è alcun programma installato nel sistema operativo.

## 📊 Dati, Tecnologie e Metriche

Per mitigare questa minaccia negli ambienti ad alta [[Opsec]] (o nell'e-banking), vengono implementate tastiere virtuali a schermo (Virtual Keyboards) i cui tasti cambiano posizione a ogni login, o sistemi Anti-Keylogging che crittografano il percorso logico tra il driver della tastiera e il browser, rendendo le intercettazioni incomprensibili.

## 🔗 Connessioni e Pattern

- [[Malware]]
- [[Spionaggio industriale]]
- [[Pegasus]]
- [[Crittografia end-to-end]]
- [[--]]
F/I/H
- [[--]]
