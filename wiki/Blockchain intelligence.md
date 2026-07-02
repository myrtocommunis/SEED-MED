---
title: "Blockchain intelligence"
tags: ["OSINT", "processed", "blockint", "crypto", "aml", "tracciamento"]
date: "2026-05-15"
status: "draft"
depth: "deep"
sources: "3"
tipo: "concetto"
---

# Blockchain intelligence

## 🎯 Sintesi Strategica

La **Blockchain Intelligence (BlockINT)** è la sotto-disciplina investigativa dell'[[Osint]] e della [[Finint]] focalizzata sulla de-anonimizzazione e il tracciamento dei flussi finanziari illeciti sui ledger distribuiti (criptovalute). Sebbene il senso comune consideri le criptovalute (es. Bitcoin) "anonime", esse sono in realtà "pseudo-anonime": ogni transazione è pubblica, permanente e uditabile da chiunque. L'analista BlockINT sfrutta questa trasparenza strutturale per mappare estorsioni ransomware, finanziamento al terrorismo o aggiramento di sanzioni internazionali, trasformando stringhe alfanumeriche prive di significato in entità giuridiche identificabili.

## 📚 Contesto e Definizioni

Le architetture dei registri impongono approcci investigativi differenti:
1.  **Modello UTXO (Unspent Transaction Output):** Utilizzato da Bitcoin. Traccia non i "saldi" degli account, ma i "frammenti" di moneta (gli output non spesi). Un singolo wallet Bitcoin genera un nuovo indirizzo per ogni ricezione, imponendo all'analista di usare euristiche (es. *Common Input Ownership Heuristic*) per RAGgruppare matematicamente centinaia di indirizzi sotto un'unica entità criminale (Clustering).
2.  **Modello Account:** Utilizzato da Ethereum (ETH) e derivati. Più simile al modello bancario classico. Indirizzi permanenti che detengono saldi e interagiscono con *Smart Contracts*.
3.  **Mixer e Tumblers:** Servizi criminali o di privacy estrema (es. [[Tornado Cash]]) in cui decine di utenti versano fondi in un pool comune. Lo Smart Contract li rimescola e li restituisce a nuovi indirizzi, interrompendo la Catena di Custodia e rendendo il tracciamento OSINT quasi impossibile.

## 📊 Dati, Tecnologie e Metriche

Il tracciamento non avviene "leggendo" il ledger grezzo, ma tramite potenti suite di analisi commerciale (es. Chainalysis, Elliptic, TRM Labs) o tool open-source (Maltego, Graphsense), che sovrappongono al registro pubblico un database proprietario di attribuzioni (Tag).
L'obiettivo metrico dell'indagine è RAGgiungere il **Choke Point (Punto di Soffocamento)**:
*   Un criminale può muovere criptovalute indefinitamente sulla blockchain, ma per spenderle nel mondo reale dovrà convertirle in valuta Fiat (Euro, Dollari).
*   Il *Choke Point* è l'**Exchange Centralizzato (CEX)** (es. Binance, Kraken). Questi scambi sono obbligati dalle normative antiriciclaggio internazionali (AML/KYC) a identificare i propri clienti con passaporto. Se l'analista OSINT dimostra che i fondi del riscatto ransomware sono atterrati su un conto Binance, può fornire un "Target Pack" alle Forze dell'Ordine che emetteranno una *Subpoena* giudiziaria a Binance per farsi consegnare l'identità reale del criminale.

## 🔍 Analisi Operativa ed Applicazioni OSINT

L'intersezione tra SOCMINT e BlockINT è esplosiva:
*   **Deanonymization via Leak:** Spesso l'errore che svela l'identità di un truffatore crypto non è tecnico, ma umano. Il criminale posta inavvertitamente un frammento del suo indirizzo pubblico su un forum (per ricevere una piccola donazione) o usa lo stesso username (Handle) su un account Twitter e su un marketplace del [[Dark web]].

## 🔮 Lacune Informative e Prossimi Passi

*   **Privacy Coins (Monero - XMR):** A differenza di Bitcoin, Monero utilizza protocolli crittografici (Ring Signatures, Stealth Addresses) che nascondono sistematicamente il mittente, il destinatario e l'importo. Tracciare Monero con strumenti OSINT standard è attualmente ritenuto matematicamente impraticabile.
*   **Cross-Chain Bridges:** Il salto di fondi da una blockchain all'altra complica l'indagine costringendo l'analista a monitorare molteplici ledger contemporaneamente.

## 🔗 Connessioni e Pattern

- [[Finint]]
- [[Cyber]]
- [[Opsec]]
- [[Dark web]]
- [[Social network analysis]]

- [[--]]
F/I/H
- [[--]]
