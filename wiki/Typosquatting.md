---
title: "Typosquatting"
tags: ["OSINT", "processed", "typosquatting", "phishing", "dns"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Typosquatting

## 🎯 Sintesi Strategica

Il **Typosquatting** (o URL Hijacking) è la pratica fraudolenta di registrare nomi a dominio internet intenzionalmente simili a siti estremamente popolari o istituzionali, basandosi sui probabili errori di battitura (typo) degli utenti. È la colonna portante infrastrutturale di ogni campagna di [[Attacco di phishing]] o disseminazione di [[Malware]].

## 📚 Contesto e Definizioni

Le tecniche di alterazione semantica per sfuggire al controllo visivo umano includono:
1.  **Omissione/Aggiunta Lettere:** `googel.com` anziché `google.com`.
2.  **Omoglifi (Homograph Attack):** L'utilizzo di caratteri cirillici o greci che appaiono identici a quelli latini (es. usare la 'а' cirillica al posto della 'a' latina in `apple.com`).
3.  **TLD Spoofing:** Registrare `azienda.co` sperando che l'utente scordi la 'm' finale di `.com`.

## 📊 Dati, Tecnologie e Metriche

L'analista [[Osint]] combatte il Typosquatting tramite strumenti di [[Ip-dns intelligence]] (come DNSTwist). Generando proattivamente centinaia di permutazioni matematiche del dominio della propria agenzia, l'analista controlla se i domini sono già stati registrati da server ostili e invia richieste legali di Takedown preventiva (Abuse report) prima che l'attacco di Phishing abbia inizio.

## 🔗 Connessioni e Pattern

- [[Attacco di phishing]]
- [[Ip-dns intelligence]]
- [[Ingegneria sociale]]
- [[--]]
F/I/H
- [[--]]
