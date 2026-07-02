---
title: "Password cracking"
tags: ["OSINT", "processed", "cracking", "password", "hash", "forensics"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Password cracking

## 🎯 Sintesi Strategica

Il **Password Cracking** è il processo computazionale per recuperare le password in chiaro partendo dai loro "Hash" archiviati in un database violato (es. dopo una [[Sql injection]]) o per rimuovere la protezione crittografica da file compressi, PDF protetti o [[Wallet]] di criptovalute. A differenza dell'attacco [[Brute-force]] online (dove tenti il login su un sito web), il cracking è un attacco "Offline": l'hacker ha rubato il file sul proprio computer e può martellarlo con milioni di calcoli al secondo senza che nessun firewall o Rate Limiting lo possa bloccare.

## 📚 Contesto e Definizioni

Quando un'azienda seria salva le password, non le scrive in chiaro, ma le passa in una [[Funzione di hash]] (es. genererà `5e884898...`).
L'hacker usa software specializzati come **Hashcat** o **John the Ripper** che sfruttano la colossale potenza matematica delle schede video da gaming (GPU). Hashcat prenderà la parola "qwerty", ne calcolerà l'Hash e lo comparerà con l'Hash rubato. Se combaciano, l'hacker ha scoperto che la password è "qwerty".

## 📊 Dati, Tecnologie e Metriche

Per proteggersi da questa reverse-engineering offline, le aziende implementano il "Salting". Aggiungono una stringa casuale (il Salt) alla password dell'utente *prima* di farne l'hash. Questo rende totalmente inutili le **Rainbow Tables** (enormi database pre-calcolati di Hash inversi scaricabili dal [[Dark web]]), costringendo l'hacker a ripartire da zero col calcolo del Brute-Force puro per ogni singola password.

## 🔗 Connessioni e Pattern

- [[Brute-force]]
- [[Funzione di hash]]
- [[Sql injection]]
- [[--]]
F/I/H
- [[--]]
