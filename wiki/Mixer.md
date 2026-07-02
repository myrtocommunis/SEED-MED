---
title: "Mixer"
tags: ["OSINT", "processed", "mixer", "tumbler", "riciclaggio", "crypto"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "3"
tipo: "concetto"
---

# Mixer

## 🎯 Sintesi Strategica

I **Mixer (o Tumbler)** sono servizi crittografici nati per proteggere la privacy, ma massicciamente utilizzati dal cybercrimine per riciclare fondi illeciti sulle blockchain trasparenti (come [[Bitcoin]] o [[Ethereum]]). Il loro scopo è interrompere in modo definitivo il collegamento (Linkability) tra il mittente e il destinatario di una transazione, rendendo inefficace l'analisi forense della [[Blockchain intelligence]].

## 📚 Contesto e Definizioni

L'architettura operativa è concettualmente semplice:
L'Hacker invia i proventi di un attacco [[Ransomware]] in un grande "calderone" (pool) gestito dal Mixer. Contemporaneamente, altre 1.000 persone fanno la stessa cosa. Lo [[Smart contract]] (o l'operatore) mescola tutte le monete e le restituisce ai proprietari su nuovi indirizzi immacolati, trattenendo una piccola commissione (fee). Il criminale ritira quindi fondi "puliti" che non hanno alcuna continuità storica con il crimine originale.

## 📊 Dati, Tecnologie e Metriche

I Mixer si dividono in due generazioni:
1.  **Mixer Centralizzati (Custodial):** Siti sul [[Dark web]] (es. Blender.io). Sono rischiosi perché l'operatore del mixer potrebbe rubare i fondi. Possono essere smantellati dalle forze dell'ordine spegnendo il server e sequestrando i log.
2.  **Mixer Decentralizzati (Non-Custodial):** Servizi basati su [[Smart contract]] (es. [[Tornado Cash]]). Essendo residenti direttamente sulla blockchain, non possono essere "spenti". L'analista [[Osint]] combatte questi Mixer utilizzando algoritmi di tracciamento euristico (es. "Peel Chain Analysis" e analisi dei volumi in entrata/uscita) per identificare i flussi, o attendendo che il criminale compia un errore di [[Opsec]] (es. riutilizzando l'indirizzo pulito su un Exchange identificato).

## 🔗 Connessioni e Pattern

- [[Blockchain intelligence]]
- [[Finint]]
- [[Smart contract]]
- [[Dark web]]
- [[--]]
F/I/H
- [[--]]
