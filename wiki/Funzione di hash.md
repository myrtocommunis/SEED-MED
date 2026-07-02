---
title: "Funzione di hash"
tags: ["OSINT", "processed", "hash", "crittografia", "integrità", "forensics"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Funzione di hash

## 🎯 Sintesi Strategica

Una **Funzione di Hash** è un algoritmo matematico (es. [[SHA-256]], MD5) che accetta in input un file o un blocco di testo di qualsiasi dimensione e restituisce in output una stringa alfanumerica di lunghezza fissa (L'Hash, o "Impronta Digitale"). Nel settore della [[Cybersecurity]] e dell'Informatica Forense (Digital Forensics), l'Hash è lo strumento supremo per garantire l'**Integrità** del dato e per identificare univocamente il [[Malware]].

## 📚 Contesto e Definizioni

Le regole matematiche di un Hash crittografico sono ferree:
1.  **Deterministico:** Lo stesso file in input produrrà *sempre* lo stesso Hash in output.
2.  **Effetto Valanga (Avalanche Effect):** Se modifichi anche un solo pixel in una foto da 10 Gigabyte, il suo Hash cambierà in modo radicale e irriconoscibile.
3.  **Unidirezionale (One-Way):** È impossibile decodificare o ricreare il file originale partendo solo dal suo Hash.

## 📊 Dati, Tecnologie e Metriche

Quando un investigatore estrae l'hard disk di un sospettato, la prima operazione è calcolare l'Hash dell'intero disco (Hashing Forense). Se durante il processo l'avvocato difensore accusa la polizia di aver manomesso i file per incastrare il cliente, la polizia ricalcola l'Hash in tribunale: se l'Hash combacia con quello originale, è matematicamente impossibile che il disco sia stato alterato. Nella [[Cyber threat intelligence]], l'Hash di un file virale è l'Indicatore di Compromissione (IoC) primario.

## 🔗 Connessioni e Pattern

- [[Crittografia asimmetrica]]
- [[Malware]]
- [[Cyber threat intelligence]]
- [[Blockchain]]
- [[--]]
F/I/H
- [[--]]
