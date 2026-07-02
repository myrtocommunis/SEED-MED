---
title: "Data preparation"
tags: ["OSINT", "processed", "data-prep", "etl", "dataset", "pulizia"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Data preparation

## 🎯 Sintesi Strategica

La **Data Preparation (Preparazione dei Dati)** è il processo informatico (spesso lungo, noioso ma vitale) di pulizia, formattazione, filtraggio e trasformazione dei dati grezzi disordinati in un formato strutturato e utilizzabile per l'analisi avanzata o l'addestramento del [[Machine learning]]. Nella catena di montaggio dell'[[Osint]], la Data Prep è il ponte obbligatorio che separa l'estrazione caotica dello [[Scraping]] dalla chiarezza del [[Data mining]]. Senza di essa, vige la regola suprema dell'informatica: "Garbage In, Garbage Out" (Spazzatura in entrata produce spazzatura in uscita).

## 📚 Contesto e Definizioni

Quando l'analista raschia (scrapes) 100.000 fatture dal [[Deep web]], i dati sono sporchi. "Milano", "milano", "MIL" e "M1lano" indicano la stessa città, ma il computer li leggerà come 4 entità distinte, distruggendo qualsiasi analisi statistica.
Le fasi della Data Prep:
1.  **Data Cleansing:** Rimozione di righe vuote, caratteri speciali (es. HTML residuo) e duplicati.
2.  **Standardizzazione (Data Wrangling):** Convertire tutte le date nel formato `YYYY-MM-DD` e tutti i nomi in maiuscolo.
3.  **Imputazione:** Gestire i dati mancanti (es. eliminare le righe o calcolarne una media).

## 📊 Dati, Tecnologie e Metriche

Questo processo consuma solitamente l'80% del tempo totale di un analista di intelligence (o Data Scientist). Nelle moderne pipeline OSINT, la Data Preparation viene integrata in architetture automatizzate (pipeline [[Etl]] usando linguaggi come Python o Pandas), in modo che i nuovi leak che entrano nel [[Data lake]] vengano lavati, normalizzati e indicizzati su [[Elasticsearch]] automaticamente senza intervento umano, rendendoli pronti per le query immediate.

## 🔗 Connessioni e Pattern

- [[Scraping]]
- [[Etl]]
- [[Data lake]]
- [[Machine learning]]
- [[--]]
F/I/H
- [[--]]
