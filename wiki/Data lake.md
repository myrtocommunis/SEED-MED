---
title: "Data lake"
tags: ["OSINT", "processed", "dati", "architettura", "big-data"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Data lake

## 🎯 Sintesi Strategica

Il **Data Lake (Lago di Dati)** è un'architettura di archiviazione centralizzata che permette alle agenzie di intelligence e corporative di stoccare enormi volumi di dati **grezzi e non strutturati** nel loro formato nativo (JSON, immagini SATellitari, log di rete, dump HTML). Nell'[[Osint]], funge da immenso bacino di raccolta indifferenziata prima che si sappia esattamente quale sarà la domanda investigativa finale.

## 📚 Contesto e Definizioni

A differenza del [[Data warehouse]] (che accetta solo dati puliti e incolonnati), il Data Lake opera sul principio "Schema-on-Read": il dato viene buttato nel lago così com'è. La struttura logica gli viene applicata (tramite ETL o AI) solo nel momento in cui l'analista lo estrae per interrogarlo.

## 📊 Dati, Tecnologie e Metriche

Consente la conservazione economica a lungo termine di terabyte di dati da [[Scraping]]. Tuttavia, se privo di catalogazione severa e metadati strutturati, il Data Lake si trasforma rapidamente in una *Data Swamp* (Palude di Dati), rendendo impossibile il ritrovamento delle informazioni quando necessario.

## 🔗 Connessioni e Pattern

- [[Data warehouse]]
- [[Trattamento dell'output]]
- [[Automazione]]
- [[--]]
F/I/H
- [[--]]
