---
title: "Data warehouse"
tags: ["OSINT", "processed", "dati", "architettura", "big-data"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Data warehouse

## 🎯 Sintesi Strategica

Il **Data Warehouse (Magazzino Dati)** è l'architettura di storage strutturato progettata specificamente per l'interrogazione e la Business Intelligence. A differenza del [[Data lake]], il Data Warehouse accetta esclusivamente dati già processati, puliti e rigidamente formattati in tabelle relazionali. Nell'[[Osint]], rappresenta l'infrastruttura finale da cui piattaforme come [[Power BI]] attingono per generare le dashboard strategiche.

## 📚 Contesto e Definizioni

Funziona sul principio "Schema-on-Write": il formato e la struttura della tabella (es. Star Schema) devono essere definiti *prima* che il dato vi entri. I JSON grezzi ricavati dallo [[Scraping]] vengono trasformati (ETL tramite [[KNIME]] o Python) e solo i campi utili (ID, Data, Testo, Sentimento) vengono caricati nel Warehouse.

## 📊 Dati, Tecnologie e Metriche

Garantisce altissime prestazioni (High-Performance Querying) su interrogazioni analitiche massive (OLAP), permettendo a un decisore di filtrare milioni di eventi di Cyber Threat Intelligence in frazioni di secondo senza sovraccaricare i server operativi.

## 🔗 Connessioni e Pattern

- [[Data lake]]
- [[Power BI]]
- [[Trattamento dell'output]]
- [[--]]
F/I/H
- [[--]]
