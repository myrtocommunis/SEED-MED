---
title: "Brute-force"
tags: ["OSINT", "processed", "brute-force", "password", "cracking", "cybercrime"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Brute-force

## 🎯 Sintesi Strategica

L'attacco **Brute-Force (Forza Bruta)** è la più banale e aritmetica tecnica di compromissione delle credenziali. Consiste nel tentare ossessivamente di indovinare una password o un PIN provando sistematicamente *tutte* le combinazioni possibili fino a trovare quella corretta. Richiede zero sofisticazione concettuale, ma si affida esclusivamente alla potenza di calcolo (GPU) dell'attaccante. È il vettore principale per la violazione dei server [[Rdp]] e dei dispositivi IoT mal configurati ([[Botnet]]).

## 📚 Contesto e Definizioni

Un attacco puro (Exhaustive Search) prova `A`, poi `B`, poi `AA`, ecc.
Per ridurre i tempi geologici necessari per forzare password lunghe, gli hacker usano i **Dizionari (Dictionary Attack)**. Piuttosto che generare stringhe casuali, l'attacco pesca da enormi file di testo contenenti le 10 milioni di password più usate al mondo (es. la celebre lista *Rockyou.txt*, recuperata dai database [[Osint]]), includendo variazioni semplici (es. `password123`).

## 📊 Dati, Tecnologie e Metriche

Il contrasto al Brute-Force da parte del [[Blue team]] è elementare:
1.  **Rate Limiting:** Il server viene configurato per bloccare temporaneamente l'indirizzo IP dopo 3 tentativi errati in 1 minuto.
2.  **MFA (Multi-Factor Authentication):** Anche se l'hacker indovina la password corretta, senza il PIN sul telefono dell'utente, l'attacco fallisce irrimediabilmente.
Per aggirare i ban degli IP, i criminali distribuiscono l'attacco affittando migliaia di [[Proxy]] residenziali o tramite una botnet (Distributed Brute Force).

## 🔗 Connessioni e Pattern

- [[Password cracking]]
- [[Credential stuffing]]
- [[Rdp]]
- [[Botnet]]
- [[--]]
F/I/H
- [[--]]
