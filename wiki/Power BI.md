---
title: "Power BI"
tags: ["OSINT", "processed", "power-bi", "dashboarding", "data-viz"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "4"
tipo: "concetto"
---

# Power BI

## 🎯 Sintesi Strategica

**Microsoft Power BI** è la piattaforma leader mondiale per la *Business Intelligence* e la visualizzazione analitica. Originariamente progettata per i contesti finanziari aziendali, ha trovato nell'[[Osint]] governativo e investigativo un'applicazione critica formidabile. Power BI funge da hub terminale nella pipeline dei dati investigativi: ingerisce dataset sporchi e disomogenei provenienti dallo scraping, li normalizza attraverso Power Query, li modella in relazioni logiche e ne permette l'interrogazione tramite dashboard interattive. Questo garantisce al decisore politico o militare un *Early Warning System* visuale, compatto e dinamicamente aggiornabile.

## 📚 Contesto e Definizioni

L'architettura di Power BI non è quella di un semplice "creatore di grafici" (come Excel), ma di un vero e proprio ecosistema di data-modeling basato su tre pilastri:
1.  **Power Query (ETL):** Il motore di estrazione e pulizia dati. Permette di unire tabelle diverse (Merge/Append), filtrare anomalie e convertire formati (es. JSON da API in tabelle relazionali) automatizzando i passaggi in linguaggio **M**.
2.  **Modellazione Dati (Star Schema):** La struttura concettuale che separa i dati in *Tabelle dei Fatti* (gli eventi misurabili, es. attacchi missilistici, post su Twitter) e *Tabelle Dimensionali* (i filtri di contesto: Data, Geografia, Autore).
3.  **[[Dax]] (Data Analysis Expressions):** Il motore di calcolo funzionale che elabora le aggregazioni dinamiche al volo a seconda di cosa l'utente seleziona sulla dashboard.

## 📊 Dati, Tecnologie e Metriche

Nel dominio OSINT, Power BI è sfruttato per correlare dataset massivi che un umano non potrebbe leggere sequenzialmente:
*   **Geospatial Intelligence:** Integrazione di mappe (Shapefiles o integrazioni ArcGIS) per visualizzare l'intensità di un conflitto (es. database ACLED - *Armed Conflict Location & Event Data Project*).
*   **Network Intelligence:** Connettori nativi o custom per tradurre database di comunicazione in grafi basilari a supporto della vera e propria [[Social network analysis]].
*   **Time Series Analysis:** Identificazione visiva di picchi anomali in campagne di [[Disinformazione]] (Volume of Posts over Time) per identificare *Coordinated Sharing*.

## 🔍 Analisi Operativa ed Applicazioni OSINT

L'utilizzo professionale prevede la separazione rigorosa tra l'ambiente di sviluppo e quello di disseminazione:
*   **Power BI Desktop:** L'applicativo in locale dove l'analista tecnico OSINT costruisce le query, il modello dati e scrive il codice DAX. Offre garanzie [[Opsec]] totali finché i dati restano in locale.
*   **Power BI Service (Cloud):** Il portale di condivisione dove il decisore può interagire con la dashboard. L'utilizzo di dati OSINT sensibili/targetizzati sul cloud pubblico Microsoft richiede approvazione governativa o architetture *On-Premise* (Power BI Report Server).

## 🔮 Lacune Informative e Prossimi Passi

*   **Staticità Grafica:** A differenza degli strumenti di [[Dashboarding con ai]] puri basati su Python (come Plotly o Streamlit), Power BI è rigido nella personalizzazione visiva spinta, legando l'analista ai moduli grafici preconfezionati del marketplace Microsoft.
*   **Curva di Apprendimento:** L'apparente facilità del "D[[RAG]] and Drop" cela la brutale complessità del motore Vertipaq sottostante. Un modello dati costruito male (es. schema a fiocco di neve caotico) genera interrogazioni DAX errate che produrranno intelligence "verosimile" ma matematicamente falsa.

## 🔗 Connessioni e Pattern

- [[Dax]]
- [[Trattamento dell'output]]
- [[Ciclo bi]]
- [[Dashboarding con ai]]
- [[Automazione]]

- [[--]]
F/I/H
- [[--]]
