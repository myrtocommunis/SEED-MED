---
title: "Man in the middle"
tags: ["OSINT", "processed", "mitm", "intercettazione", "cybersecurity", "sniffing"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Man in the middle

## 🎯 Sintesi Strategica

L'attacco **Man in the Middle (MitM - Uomo nel mezzo)** è una tecnica di spionaggio informatico in cui l'attaccante si interpone segretamente nella comunicazione tra due parti che credono di parlare direttamente tra loro. In ambito [[Osint]] governativo e di [[Sigint]], il MitM è la tecnica regina per l'intercettazione dei dati in transito (es. usando un [[Imsi catcher]] per telefoni o cavi sottomarini per i dati), permettendo di alterare i messaggi o rubare le credenziali.

## 📚 Contesto e Definizioni

Lo scenario classico avviene sulle reti Wi-Fi pubbliche (aeroporti, hotel).
L'hacker crea un Hotspot Wi-Fi falso con lo stesso nome di quello dell'hotel ("Evil Twin"). La vittima si connette. Da quel momento, ogni sito richiesto dalla vittima passa attraverso il computer dell'hacker.
Per sconfiggere questo attacco, l'industria ha imposto la crittografia SSL/TLS (HTTPS su tutto il web), impedendo all'hacker di leggere i dati intercettati.

## 📊 Dati, Tecnologie e Metriche

Tuttavia, i gruppi [[Apt]] più sofisticati eseguono MitM crittografici (SSL Stripping). L'hacker costringe il browser della vittima a caricare la versione HTTP non sicura del sito bancario. Se l'utente non nota l'assenza del "lucchetto" verde nel browser, digita la password e l'hacker la cattura in chiaro (usando tool come [[Wireshark]] o Bettercap). Nel phishing avanzato, si usano server Reverse Proxy (es. Evilginx) che fungono da intermediari trasparenti tra la vittima e il sito reale (Google/Microsoft), aggirando e rubando perfino i token OTP dell'autenticazione a due fattori.

## 🔗 Connessioni e Pattern

- [[Wireshark]]
- [[Attacco di phishing]]
- [[Imsi catcher]]
- [[Oauth]]
- [[--]]
F/I/H
- [[--]]
