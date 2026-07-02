---
title: "Ach"
tags: ["OSINT", "processed", "ach", "[[SAT]]", "methodology"]
date: "2026-05-15"
status: "draft"
depth: "deep"
sources: "1"
tipo: "metodologia"
---

# Ach (Analysis of Competing Hypotheses)

## 🎯 Sintesi Strategica

L'**Analysis of Competing Hypotheses (ACH)** è la Tecnica di Analisi Strutturata ([[Sat]]) cardine dell'analisi intelligence contemporanea. Codificata da Richards J. Heuer Jr. nel capitolo 8 del fondamentale *Psychology of Intelligence Analysis* (CIA CSI, 1999), l'ACH è un artefatto cognitivo progettato per invertire la logica conferma-centrica del RAGionamento ordinario. Invece di accumulare prove a supporto della prima spiegazione plausibile (pratica del *SATisficing*), l'ACH impone all'analista di valutare simultaneamente un set esaustivo di ipotesi concorrenti, identificando come ipotesi vincente non quella con il maggior numero di conferme, ma **quella con il minor numero di inconsistenze** (paradigma di derivazione falsificazionista popperiana). Costituisce la difesa metodologica più robusta contro il Bias di conferma ed è considerata lo standard di riferimento per indagini OSINT complesse e ad alto impatto decisionale.

## 📚 Contesto e Definizioni

La genesi dell'ACH affonda le radici nei traumi analitici della [[Guerra Fredda]] (come il fallimento valutativo del Team B sulle capacità sovietiche nel 1976) e nel trauma storico di Pearl Harbor (Wohlstetter, 1962). Heuer trapianta l'epistemologia falsificazionista di Karl Popper dal laboratorio scientifico alla scrivania dell'analista per esternalizzare e rendere tracciabile, criticabile e riproducibile il processo logico di stima.

### Il Framework Cognitivo: Sistema 1 vs Sistema 2

Applicando il modello duale di [[Daniel Kahneman]] (*PENSieri lenti e veloci*), l'ACH funge da contromisura meccanica all'architettura cerebrale:
*   **Sistema 1 (Intuitivo):** Tende a saltare alle conclusioni sulla base delle sole informazioni immediatamente visibili (WYSIATI - *What You See Is All There Is*), cercando conferme alla prima storia coerente.
*   **Sistema 2 (Riflessivo):** È pigro e costoso. L'ACH forza meccanicamente l'attivazione del Sistema 2 costringendo l'analista a compilare una matrice riga per riga, superando le scorciatoie mentali euristiche.

## 📊 Dati, Tecnologie e Metriche

Il nucleo procedurale dell'ACH si articola nella costruzione della **Matrice Ipotesi × Evidenze**.

### Il Concetto di Diagnosticità

L'elemento epistemico centrale che distingue l'ACH dalla semplice catalogazione è la **Diagnosticità delle evidenze**. Un'evidenza è diagnostica solo nella misura in cui possiede il potere di discriminare tra le diverse ipotesi.

| Tipo di Evidenza | Scenario Applicativo | Valore Diagnostico | Azione Consigliata |
| :--- | :--- | :--- | :--- |
| **Non Diagnostica / Tautologica** | Evidenza compatibile con tutte le ipotesi enumerate (es. "il target compie esercitazioni di routine"). | Nullo / Rumore di fondo | **Scartare** dal calcolo decisionale per evitare SATurazione. |
| **Diagnostica** | Evidenza compatibile con un'ipotesi e fortemente inconsistente con un'altra (es. "esercitazioni notturne al confine mai avvenute prima"). | Massimo / Elevato | **Conservare** e pesare come elemento discriminante primario. |

Ogni evidenza catalogata in matrice viene preventivamente valutata tramite la **Admiralty Scale** (da A1 a F6) per definirne scientificamente l'affidabilità della fonte e la credibilità del dato primario.

## 🔍 Analisi Operativa ed Applicazioni OSINT

L'applicazione dell'ACH segue un rigido protocollo in 4 step operativi principali:

1.  **Enumerazione Esaustiva:** Identificazione di tutte le spiegazioni alternative possibili (da 2 a N), includendo deliberatamente scenari controintuitivi, scomodi o apparentemente bizzarri. L'esclusione precoce di un'ipotesi ne decreta la morte analitica.
2.  **Catalogazione delle Evidenze:** Inventario di tutte le prove disponibili, ma anche delle assenze significative, anomalie o assunzioni di base.
3.  **Compilazione della Matrice:** Incrocio logico in cui ogni cella riceve un rating: Consistent (`C`), Inconsistent (`I`), o Not Applicable (`N/A`).
4.  **Selezione per Esclusione:** Riorganizzazione della matrice concentrandosi sull'inconsistenza. La migliore stima è l'ipotesi meno smentita dalle evidenze disponibili.

### Casi Studio Storici di Analisi Mancata

*   **Iraq WMD (2003):** Il clamoroso fallimento sull'esistenza delle armi di distruzione di massa in Iraq derivò dalla mancata applicazione dell'ACH. La comunità d'intelligence non prese in esame l'ipotesi alternativa: *"Saddam Hussein non possiede un programma WMD attivo, ma finge di averlo per mantenere la deterrenza regionale e domestica"*. Se inserita in matrice, le scarse prove diagnostiche avrebbero rivelato l'estrema fragilità dell'ipotesi del programma attivo.
*   **Pearl Harbor (1941) & Ottobre 2023:** Casi tipici di *[[Failure of Imagination]]*, dove la minaccia reale non era assente nei dati, ma era assente dallo spazio delle ipotesi ritenute plausibili dai decisori.

## 🔮 Lacune Informative e Prossimi Passi

*   **Costo Cognitivo-Temporale:** L'ACH è un metodo estremamente oneroso in termini di ore-lavoro. Richiede l'integrazione con tecniche di generazione rapida per non congestionare i workflow operativi.
*   **Automazione AI-Augmented (2025-2026):** Integrazione guidata di Modelli Linguistici di Grandi Dimensioni ([[Llm]]) per l'assistenza nella costruzione delle matrici, l'identificazione di evidenze tautologiche e la generazione di scenari *What If* per mitigare ulteriormente il rischio di *[[Groupthink]]*.
*   **Triangolazione Dinamica (ACH-CD):** Sviluppo di matrici evolute in grado di gestire le diagnosi conflittuali senza collassarle in un semplice valore aggregato, valorizzando l'incoerenza informativa stessa come segnale di *deception*.

## 🔗 Connessioni e Pattern

- [[Bias cognitivo]]
- [[Sat]]
- [[Admiralty Scale]]
- [[Ciclo intelligence]]
- [[Metodologia]]
- [[Red team]]

- [[--]]
F/I/H
- [[--]]
