---
title: "Nft"
tags: ["OSINT", "processed", "nft", "crypto", "riciclaggio", "blockchain"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Nft

## 🎯 Sintesi Strategica

I **NFT (Non-Fungible TokENS - Token Non Fungibili)** sono certificati digitali di proprietà e autenticità archiviati su una blockchain (prevalentemente [[Ethereum]]), che rappresentano un asset digitale o fisico unico (opere d'arte, immagini, oggetti di videogiochi). Nell'ambito della [[Finint]] e dell'[[Osint]], gli NFT sono divenuti rapidamente un veicolo sofisticato per il riciclaggio di denaro (Money Laundering) e il Wash Trading, eludendo le normative AML applicate tradizionalmente alle criptovalute standard.

## 📚 Contesto e Definizioni

A differenza di un [[Bitcoin]] (che è fungibile, ovvero 1 BTC vale esattamente come un altro 1 BTC), ogni NFT è matematicamente distinto e il suo valore è soggettivo (stabilito dal mercato, esattamente come per un dipinto fisico). Questa soggettività del valore è l'elemento chiave della frode.

## 📊 Dati, Tecnologie e Metriche

Il meccanismo di riciclaggio (Wash Trading) opera tramite auto-compravendita:
1. Un criminale detiene 1 milione di euro in fondi illeciti su un wallet anonimo A.
2. Crea un NFT gratuito (raffigurante un'immagine a caso) usando un wallet "pulito" B, a suo nome.
3. Il wallet A acquista l'NFT dal wallet B per 1 milione di euro.
Risultato: il criminale può giustificare il milione di euro sul wallet B all'Agenzia delle Entrate come "profitto derivante dalla vendita di arte digitale", pulendo i soldi illeciti. L'analista [[Blockchain intelligence]] deve mappare i metadati del contratto e la storia dei wallet per dimostrare che A e B appartengono alla stessa persona (Self-Dealing).

## 🔗 Connessioni e Pattern

- [[Blockchain intelligence]]
- [[Finint]]
- [[Ethereum]]
- [[Smart contract]]
- [[--]]
F/I/H
- [[--]]
