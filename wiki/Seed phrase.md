---
title: "Seed phrase"
tags: ["OSINT", "processed", "seed-phrase", "crypto", "opsec", "forensics"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Seed phrase

## 🎯 Sintesi Strategica

La **Seed Phrase (Frase Seme)**, nota anche come Recovery Phrase, è una sequenza leggibile dall'uomo di 12 o 24 parole inglesi casuali generata dal [[Wallet]] crittografico al momento della creazione. Dal punto di vista della [[Cyber threat intelligence]] e della [[Finint]], la Seed Phrase rappresenta l'obiettivo supremo (il "Master Key"): chiunque possieda queste 12 parole ha il controllo assoluto e irreversibile di tutti i fondi contenuti in quel Wallet, indipendentemente dal dispositivo fisico o dalle password utilizzate.

## 📚 Contesto e Definizioni

Matematicamente, la Seed Phrase (standard BIP-39) è la rappresentazione mnemonica della chiave privata master. Se un criminale perde la chiavetta USB (Cold Wallet) o rompe lo smartphone, può acquistare un nuovo dispositivo, inserire le 12 parole e riottenere l'accesso ai fondi. Viceversa, se dimentica le parole e perde il dispositivo, i fondi sono bloccati per l'eternità. Il protocollo decentralizzato della [[Blockchain]] non ha alcun servizio di "Reset Password".

## 📊 Dati, Tecnologie e Metriche

Il sequestro informatico di criptovalute illecite (es. proventi di Silk Road o di ransomware) da parte della polizia postale si conclude quasi sempre con il ritrovamento della Seed Phrase:
*   I criminali spesso commettono errori fatali di [[Opsec]], salvando le parole in chiaro su file di testo sul desktop, inviandosele via email o fotografandole con lo smartphone (esponendole così all'estrazione cloud o all'identificazione via [[Ocr]]).
*   Gli attacchi di [[Ingegneria sociale]] e [[Attacco di phishing]] più letali nel settore crypto non rubano password, ma truffano l'utente facendogli inserire le 12 parole su finti siti di supporto.

## 🔗 Connessioni e Pattern

- [[Wallet]]
- [[Blockchain intelligence]]
- [[Opsec]]
- [[Ocr]]
- [[--]]
F/I/H
- [[--]]
