---
title: "Bitcoin"
tags: ["OSINT", "processed", "bitcoin", "crypto", "utxo"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "4"
tipo: "concetto"
---

# Bitcoin

## 🎯 Sintesi Strategica

**Bitcoin (BTC)** è la prima criptovaluta decentralizzata, introdotta nel 2008 dallo pseudonimo SAToshi Nakamoto. È progettata per consentire transazioni finanziarie peer-to-peer senza l'intermediazione di banche o governi. Dal punto di vista della [[Blockchain intelligence]], Bitcoin è il veicolo principale per i pagamenti di [[Ransomware]] e l'acquisto di beni sul [[Dark web]], costringendo le unità investigative a specializzarsi nel tracciamento del suo specifico modello contabile (UTXO).

## 📚 Contesto e Definizioni

L'architettura di Bitcoin si basa sull'UTXO (Unspent Transaction Output). A differenza dei conti bancari tradizionali (modello Account), un [[Wallet]] Bitcoin non ha un singolo "saldo". Il saldo è calcolato sommando i "resti" (gli input non spesi) provenienti da transazioni precedenti. Per mantenere l'[[Opsec]], il protocollo genera un nuovo indirizzo pubblico per ogni singola transazione in entrata (Address Reuse è considerato un errore grave per la privacy).

## 📊 Dati, Tecnologie e Metriche

L'analista [[Osint]] combatte la proliferazione di indirizzi usando euristiche matematiche (es. *Common Input Ownership Heuristic*). Se in una transazione Bitcoin vengono spesi contemporaneamente fondi provenienti dall'Indirizzo A e dall'Indirizzo B, l'algoritmo di clustering deduce con quasi assoluta certezza che A e B appartengono alla stessa entità umana (o allo stesso [[Wallet]]), de-anonimizzando parzialmente la rete.

## 🔗 Connessioni e Pattern

- [[Blockchain intelligence]]
- [[Wallet]]
- [[Ransomware]]
- [[Mixer]]
- [[--]]
F/I/H
- [[--]]
