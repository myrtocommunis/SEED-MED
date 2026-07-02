---
title: "Protonmail"
tags: ["OSINT", "processed", "protonmail", "email", "opsec", "privacy"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Protonmail

## 🎯 Sintesi Strategica

**Protonmail** è un servizio di posta elettronica criptata basato in Svizzera. Fornisce nativamente la [[Crittografia end-to-end]] per le comunicazioni tra utenti Proton e supporta l'integrazione di [[Pgp]] per la comunicazione con servizi esterni. È diventato lo standard di fatto per le comunicazioni sicure, la registrazione di profili anonimi ([[Sock puppet]]) e le operazioni di informazione sia legali (giornalismo) che illegali (cybercrimine).

## 📚 Contesto e Definizioni

La sua forza legale risiede nella giurisdizione svizzera, che è esterna alle alleanze dei servizi segreti (14 Eyes) e richiede un ordine di un tribunale svizzero per fornire dati.
La forza tecnica è l'architettura Zero-Access: anche se il governo svizzero costringe Protonmail a consegnare l'archivio di posta di un criminale, Protonmail consegnerà server interamente crittografati, poiché non possiede la password dell'utente per decriptarli.

## 📊 Dati, Tecnologie e Metriche

Il mito dell'anonimato assoluto è stato sfatato nel 2021 nel caso di alcuni attivisti per il clima in Francia: Protonmail, pur non potendo leggere le email, fu costretta per legge a registrare (Logging) gli indirizzi IP di accesso degli utenti, portando al loro arresto. Questo ha confermato agli analisti di [[Opsec]] che anche i servizi criptati non difendono dall'analisi dei [[Metadati]] o dell'IP, rendendo obbligatorio l'utilizzo combiNATO di una [[Vpn]] o della rete [[Tor]] per mascherare l'impronta di rete durante la registrazione e l'uso dell'account.

## 🔗 Connessioni e Pattern

- [[Crittografia end-to-end]]
- [[Opsec]]
- [[Pgp]]
- [[Tor]]
- [[--]]
F/I/H
- [[--]]
