---
title: "Wallet"
tags: ["OSINT", "processed", "wallet", "crypto", "chiavi-private"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "3"
tipo: "concetto"
---

# Wallet

## 🎯 Sintesi Strategica

Un **Wallet (Portafoglio crittografico)** è un software o un dispositivo hardware che consente a un utente di interagire con una rete [[Blockchain]], gestendo il proprio saldo e autorizzando le transazioni. Nelle indagini [[Osint]] legate alla [[Finint]], identificare il tipo di Wallet (Hot vs Cold, Custodial vs Non-Custodial) è essenziale per determinare se le Forze dell'Ordine possono sequestrare i fondi del criminale tramite un ingiunzione a terzi o se la confisca richiede la compromissione fisica del dispositivo bersaglio.

## 📚 Contesto e Definizioni

Il termine "Portafoglio" è fuorviante: i Wallet non contengono letteralmente "i soldi" (che risiedono pubblicamente sulla blockchain). I Wallet contengono le **Chiavi Private**, le password matematiche che dimostrano la proprietà dei fondi e autorizzano lo spostamento.
Tipologie principali:
1.  **Custodial Wallet:** Gestiti da terzi (es. Coinbase). L'azienda detiene le chiavi. Un tribunale può ordinare all'azienda di congelare i fondi.
2.  **Non-Custodial Wallet (Self-Custody):** L'utente detiene esclusivamente le proprie chiavi (es. Metamask). Nessuna entità governativa al mondo può bloccare i fondi senza accedere al dispositivo della vittima.

## 📊 Dati, Tecnologie e Metriche

L'[[Opsec]] criminale si basa sulla divisione del capitale:
*   **Hot Wallet (Portafoglio Caldo):** Software installato su PC/Smartphone costantemente connesso a internet. Comodo per operare, ma vulnerabile ad attacchi [[Malware]] o trojan.
*   **Cold Wallet (Portafoglio Freddo):** Dispositivi hardware (simili a chiavette USB, es. Ledger) tenuti fisicamente offline in cassaforte. Inviolabili da remoto. Se il Threat Actor usa un Cold Wallet, l'unico vettore d'attacco per il sequestro è l'impiego di HUMINT, perquisizioni fisiche o [[Ingegneria sociale]] per ottenere la [[Seed phrase]].

## 🔗 Connessioni e Pattern

- [[Blockchain]]
- [[Finint]]
- [[Seed phrase]]
- [[Opsec]]
- [[--]]
F/I/H
- [[--]]
