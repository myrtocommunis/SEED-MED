---
title: "Credential stuffing"
tags: ["OSINT", "processed", "credential-stuffing", "cybercrime", "riutilizzo-password", "automazione"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Credential stuffing

## 🎯 Sintesi Strategica

Il **Credential Stuffing (Imbottitura di credenziali)** è l'attacco informatico di gran lunga più diffuso e letale contro le identità digitali. Sfrutta il peccato originale della sicurezza umana: il riciclo della stessa password su siti web diversi. Nel ciclo di vita del cybercrimine, rappresenta l'anello di congiunzione tra l'acquisizione di vecchi database da [[Data breach]] (spesso usati dagli analisti [[Osint]]) e la monetizzazione diretta.

## 📚 Contesto e Definizioni

A differenza del [[Brute-force]] puro (che prova password a caso alla cieca), il Credential Stuffing spara "a colpo sicuro".
La dinamica:
1. Un hacker acquista un file con 50 milioni di email e password rubate nel 2012 da un forum di scarpe (Data Breach).
2. Usa script automatizzati (es. Openbullet) per provare *esattamente quelle stesse email e password* sulla pagina di login di Netflix, Amazon, o della posta aziendale di Microsoft365 (spesso usando pool di [[Proxy]]).
3. Poiché il 30% delle persone usa la stessa password ovunque, l'hacker entra negli account Amazon senza dover "bucare" Amazon, che ha difese formidabili.

## 📊 Dati, Tecnologie e Metriche

L'[[Osint]] difensiva utilizza piattaforme come "Have I Been Pwned" o framework aziendali di Attack Surface Management per eseguire il monitoraggio continuo (Threat Intelligence). Se l'email di un manager aziendale compare in un nuovo database sul [[Dark web]], il team SOC forza il reset immediato della password aziendale del dipendente *prima* che l'hacker possa eseguire lo Stuffing sulla VPN dell'ufficio.

## 🔗 Connessioni e Pattern

- [[Data breach]]
- [[Brute-force]]
- [[Proxy]]
- [[Cyber threat intelligence]]
- [[--]]
F/I/H
- [[--]]
