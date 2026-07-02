---
title: "Botnet"
tags: ["OSINT", "processed", "botnet", "cyber", "ddos", "zombie"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Botnet

## 🎯 Sintesi Strategica

Una **Botnet (Robot Network)** è un'infrastruttura illecita costituita da decine di migliaia (spesso milioni) di dispositivi connessi a internet (Computer, Router, Telecamere IoT) infettati da [[Malware]]. Questi dispositivi, noti come "Zombie", vengono cooptati a insaputa dei legittimi proprietari e telecomandati centralmente da un criminale informatico (il Botmaster) per eseguire attacchi coordinati su vasta scala.

## 📚 Contesto e Definizioni

L'architettura classica prevede un server centrale di [[Command and control]] (C2). Il Botmaster invia il comando al C2, che a sua volta sveglia l'orda di dispositivi silenti e ordina l'attacco. Questa infrastruttura è alla base del mercato del cybercrimine in affitto (Cybercrime-as-a-Service).

## 📊 Dati, Tecnologie e Metriche

Le Botnet (come la famigerata Mirai) vengono utilizzate principalmente per due scopi tattici distruttivi:
1.  **Attacchi [[Ddos]]:** Generare volumi di traffico così massicci da mandare offline infrastrutture governative o piattaforme finanziarie.
2.  **Spam e Phishing Massivo:** Utilizzare gli IP puliti dei cittadini ignari per aggirare i filtri antispam e distribuire milioni di email contenenti [[Attacco di phishing]].
L'analista OSINT utilizza [[Shodan (motore di ricerca)]] per mappare dispositivi vulnerabili su scala globale che potrebbero essere assimilati in una Botnet in via di formazione.

## 🔗 Connessioni e Pattern

- [[Ddos]]
- [[Malware]]
- [[Command and control]]
- [[Shodan (motore di ricerca)]]
- [[--]]
F/I/H
- [[--]]
