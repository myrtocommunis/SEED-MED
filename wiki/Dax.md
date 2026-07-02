---
title: "Dax"
tags: ["OSINT", "processed", "dax", "power-bi", "data-analysis"]
date: "2026-05-15"
status: "draft"
depth: "deep"
sources: "2"
tipo: "concetto"
---

# Dax

## 🎯 Sintesi Strategica

Il **DAX (Data Analysis Expressions)** è il linguaggio funzionale di formula e interrogazione (query) nativo di [[Power BI]], Power Pivot e SQL Server Analysis Services (SSAS). Per un analista dei dati o un ricercatore [[Osint]] specializzato in data-intelligence, il DAX è l'unico strumento capace di trasformare un modello dati statico (Tabella dei Fatti) in un'infrastruttura d'intelligence reattiva. Non serve a "pulire" i dati (compito affidato a Power Query / linguaggio M), ma a creare calcoli dinamici e KPI (Key Performance Indicators) che si ricalcolano istantaneamente in base ai filtri applicati dal decisore sulla dashboard.

## 📚 Contesto e Definizioni

A differenza delle formule di Excel, che operano su righe e celle specifiche (A1+B1), il DAX opera esplicitamente su **Colonne e Tabelle**. Il suo intero paradigma logico si fonda sulla gestione simultanea di due "Motori di Contesto":
1.  **Row Context (Contesto di Riga):** Esegue il calcolo iterando riga per riga (creando *Colonne Calcolate* o usando funzioni iteratrici come `SUMX`).
2.  **Filter Context (Contesto di Filtro):** *Il cuore del DAX.* È l'insieme dinamico dei filtri applicati a una formula in uno specifico momento (es. quando il decisore clicca su "Russia" e sull'anno "2024" in un grafico). La formula (es. `SUM(Morti)`) restituirà il valore esclusivamente per il sotto-insieme determiNATO dal Filter Context.

## 📊 Dati, Tecnologie e Metriche

L'arsenale DAX si basa sulla potente funzione `CALCULATE`, che permette all'analista di sovrascrivere o manipolare il *Filter Context* origiNATO dalla dashboard:
```dax
Eventi_Critici_Target = 
CALCULATE(
    COUNTROWS('Tabella_Fatti'),
    'Tabella_Fatti'[Severità] = "Alta",
    'Dimensione_Geografica'[Paese] = "Siria"
)
```
Questo garantisce che la metrica restituisca *sempre* gli eventi ad alta severità in quel preciso paese, indipendentemente dai filtri generali esterni che l'utente cerca di applicare inavvertitamente.

## 🔍 Analisi Operativa ed Applicazioni OSINT

L'ambito in cui il DAX brilla assolutamente per le applicazioni di sicurezza e intelligence è la **Time Intelligence (Intelligenza Temporale)**.
*   Tracciare l'evoluzione di una campagna di [[Disinformazione]] o di incidenti cinetici richiede confronti temporali continui.
*   Le funzioni native (come `DATEADD`, `SAMEPERIODLASTYEAR`, `TOTALYTD`) permettono di calcolare automaticamente le variazioni percentuali mese-su-mese (MoM) o anno-su-anno (YoY) dell'attività di un Threat Actor, svelando picchi anomali che indicano l'innesco di una specifica operazione coperta.

## 🔮 Lacune Informative e Prossimi Passi

*   **Complessità Astratta:** Il DAX ha un "muro di apprendimento". La sintassi è facile (simile a Excel), ma la comprensione di come il motore interno (Vertipaq) propaga i filtri attraverso le relazioni tra le tabelle (Star Schema) è estremamente complessa. Errori di DAX non bloccano il programma, ma restituiscono numeri errati (un fallimento critico in ambito d'intelligence).
*   **Sostituzione AI:** L'integrazione di Copilot e dell'[[Intelligenza artificiale generativa]] in Power BI sta iniziando a generare codice DAX a partire da prompt in linguaggio naturale. Tuttavia, come descritto nel [[Dashboarding con ai]], la revisione umana di formule complesse rimane obbligatoria per prevenire allucinazioni matematiche.

## 🔗 Connessioni e Pattern

- [[Power BI]]
- [[Ciclo bi]]
- [[Dashboarding con ai]]
- [[Automazione]]

- [[--]]
F/I/H
- [[--]]
