---
title: "Crittografia end-to-end"
tags: ["OSINT", "processed", "e2ee", "crittografia", "privacy", "comunicazione"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Crittografia end-to-end

## 🎯 Sintesi Strategica

La **Crittografia End-to-End (E2EE)** è un paradigma di comunicazione in cui solo gli utenti che comunicano (i due "capi" o endpoint) possono leggere i messaggi. Garantisce che i dati siano cifrati sul dispositivo del mittente e decifrati esclusivamente sul dispositivo del destinatario. Nessun intermediario (nemmeno l'azienda che fornisce il servizio, come Whatsapp o il provider Internet) possiede le chiavi per decodificare il traffico, rendendo impossibile l'intercettazione massiva (Wiretapping) da parte della polizia o di agenzie di [[Sigint]].

## 📚 Contesto e Definizioni

A differenza della cifratura "in transito" (Transport Layer Security - TLS), usata per esempio dai siti bancari, dove la banca può leggere i tuoi dati una volta arrivati sui suoi server, l'E2EE è "Zero-Knowledge". Se un giudice emette un mandato per ottenere i messaggi di un criminale, il fornitore dell'app restituirà solo un blocco di testo crittografato e inutilizzabile.

## 📊 Dati, Tecnologie e Metriche

L'introduzione dell'E2EE come standard di massa (es. su Whatsapp e [[Signal]]) ha causato il fenomeno del "Going Dark" (Oscuramento) per le agenzie governative, che hanno perso la loro principale fonte di intercettazione passiva. Per aggirare l'E2EE, l'unico metodo tecnico rimasto all'intelligence è l'uso di spyware di Stato (es. [[Pegasus]]) per infettare direttamente il telefono della vittima e leggere il messaggio dallo schermo *prima* che venga cifrato o *dopo* che è stato decifrato (attacco all'endpoint).

## 🔗 Connessioni e Pattern

- [[Pegasus]]
- [[Sigint]]
- [[Signal]]
- [[Crittografia asimmetrica]]
- [[--]]
F/I/H
- [[--]]
