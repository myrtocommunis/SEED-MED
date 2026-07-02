---
title: "Google dorks"
tags: ["OSINT", "processed", "dorking", "google", "ricerca-avanzata"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "3"
tipo: "concetto"
---

# Google dorks

## 🎯 Sintesi Strategica

Il **Google Dorking** (o Google Hacking) è l'impiego di operatori di ricerca avanzata sintattici (Dorks) per interrogare i motori di ricerca in modo da rivelare informazioni sensibili, file di configurazione, database esposti o vulnerabilità non intenzionalmente resi pubblici su internet, ma erroneamente indicizzati dai crawler. È la primissima fase passiva dell'[[Osint]] e della ricognizione informatica ([[Cyber kill chain]]).

## 📚 Contesto e Definizioni

Invece di cercare una parola chiave, l'analista restringe chirurgicamente l'obiettivo.
Operatori classici:
*   `site:target.com` (Restringe la ricerca a uno specifico dominio).
*   `filetype:pdf` (Cerca solo estensioni specifiche).
*   `intitle:"index of"` (Scoperta di directory aperte sui server, spesso zeppe di backup).
*   Esempio combiNATO: `site:governo.it filetype:xls intext:"password"` restituisce file Excel governativi contenenti la parola password.

## 📊 Dati, Tecnologie e Metriche

Il *Google Hacking Database (GHDB)* (ospitato da Exploit-DB) è il repository globale che archivia migliaia di Dork letali, aggiornate quotidianamente. Permettono di localizzare telecamere di sicurezza senza password, portali di login amministrativi, o log di errori SQL contenenti architetture del database. Essendo un'interrogazione diretta a Google e non al server bersaglio, l'operazione garantisce un'assoluta [[Opsec]] passiva.

## 🔗 Connessioni e Pattern

- [[Osint]]
- [[Opsec]]
- [[Raccolta]]
- [[Cyber kill chain]]
- [[--]]
F/I/H
- [[--]]
