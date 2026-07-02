---
title: "Hadoop"
tags: ["OSINT", "processed", "hadoop", "big-data", "data-lake", "database"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Hadoop

## 🎯 Sintesi Strategica

**Apache Hadoop** è un framework software open-source progettato specificamente per l'archiviazione distribuita e l'elaborazione massiva (Big Data) di set di dati talmente enormi da non poter risiedere su un singolo computer. È l'infrastruttura fondamentale che rende possibile la creazione di un [[Data lake]] su scala governativa o per le grandi corporazioni. Nell'ambito [[Osint]], Hadoop fornisce la "cisterna" in cui vengono scaricati petabyte di dati grezzi, strutturati e non strutturati, raccolti tramite [[Scraping]] dal [[Clear web]] e dal [[Dark web]].

## 📚 Contesto e Definizioni

Invece di comprare un singolo supercomputer costosissimo, Hadoop permette di collegare (Clusterizzare) migliaia di computer commerciali economici.
Si basa su due moduli centrali:
1.  **HDFS (Hadoop Distributed File System):** Il sistema che spezzetta i file enormi (es. un leak da 5 Terabyte di email) e ne salva copie multiple su decine di computer diversi per prevenire la perdita dei dati (Fault Tolerance).
2.  **Mapreduce:** Il motore logico che assegna l'analisi dei dati direttamente al computer dove il dato è fisicamente archiviato, evitando colli di bottiglia di rete.

## 📊 Dati, Tecnologie e Metriche

L'integrazione tra Hadoop e i tool d'intelligence è indiretta. Hadoop conserva il dato grezzo, freddo. Quando l'analista di [[Cyber threat intelligence]] o l'operatore [[Finint]] ha bisogno di trovare un "ago nel pagliaio" (es. un singolo indirizzo IP in 10 anni di log di rete), motori sovrastanti come [[Elasticsearch]] o Spark si interfacciano con il cluster Hadoop per estrarre l'informazione in tempo reale.

## 🔗 Connessioni e Pattern

- [[Data lake]]
- [[Elasticsearch]]
- [[Data mining]]
- [[--]]
F/I/H
- [[--]]
