---
title: "Crittografia asimmetrica"
tags: ["OSINT", "processed", "crittografia", "sicurezza", "chiave-pubblica"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Crittografia asimmetrica

## 🎯 Sintesi Strategica

La **Crittografia Asimmetrica** (o a chiave pubblica) è l'invenzione matematica rivoluzionaria che ha reso possibile la sicurezza di Internet, il commercio elettronico e l'esistenza delle [[Blockchain]]. A differenza dei vecchi sistemi crittografici, risolve il "problema dello scambio delle chiavi": permette a due persone che non si sono mai incontrate prima di comunicare in modo totalmente sicuro (crittografia end-to-end) su un canale insicuro come internet.

## 📚 Contesto e Definizioni

L'architettura si basa sull'uso di due chiavi matematicamente collegate, generate dall'utente:
1.  **Chiave Pubblica:** Viene distribuita a tutti liberamente (come l'IBAN di un conto o un indirizzo email).
2.  **Chiave Privata:** Deve rimanere un segreto assoluto nel dispositivo dell'utente.

**Il meccanismo (Cifratura):** Se Alice vuole inviare un messaggio segreto a Bob, Alice usa la Chiave Pubblica di Bob per "chiudere il lucchetto". Una volta chiuso, nemmeno Alice può riaprirlo. Solo Bob, che possiede l'unica Chiave Privata corrispondente, può decifrare il messaggio.

## 📊 Dati, Tecnologie e Metriche

Questo paradigma è alla base dei protocolli HTTPS, PGP (per le email), SSH e dell'autenticazione delle transazioni [[Bitcoin]]. Per le agenzie di intelligence ([[Sigint]]), una crittografia asimmetrica implementata correttamente senza backdoor (es. RSA 4096-bit) è inattaccabile matematicamente. L'unica opzione per l'investigatore è l'uso di spyware come [[Pegasus]] per rubare la Chiave Privata direttamente dal dispositivo (attacco all'endpoint).

## 🔗 Connessioni e Pattern

- [[Firma digitale]]
- [[Blockchain]]
- [[Sigint]]
- [[Pegasus]]
- [[--]]
F/I/H
- [[--]]
