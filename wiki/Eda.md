---
title: Eda
tags:
- OSINT
- processed
- eda
- data-science
- machine-learning
- cybersecurity
date: '2026-05-15'
status: draft
depth: standard
sources: '1'
tipo: concetto
---

# Eda

## 🎯 Sintesi Strategica

L'Exploratory Data Analysis (EDA), o Analisi Esplorativa dei Dati, è un approccio fondamentale nell'[[Analisi]] che mira a scoprire pattern, individuare anomalie, testare ipotesi e riassumere le caratteristiche principali di un set di dati, spesso con metodi di visualizzazione. È un passo cruciale prima della Modellazione Predittiva, rivelando insight che guidano le successive fasi di [[Data science]] e [[Machine learning]]. Nel contesto [[Osint]], l'EDA permette di dare senso a grandi volumi di informazioni eterogenee, identificando tendenze e anomalie che potrebbero indicare attività rilevanti o vulnerabilità, fornendo una base solida per l'Intelligence Analysis.

## 📚 Contesto e Definizioni

L'EDA è un processo iterativo e aperto di indagine sui dati, in contrasto con l'[[Analisi]] (Hypothesis Testing) che testa assunzioni specifiche. Il suo obiettivo primario è comprendere la struttura, le relazioni e le peculiarità di un dataset senza formulare ipotesi a priori.

Nel più ampio processo di [[Data science]], l'EDA si colloca tipicamente dopo la fase di [[Data preparation]] e prima della Feature Engineering, del Model Training e della Validazione del Modello.

Le relazioni con altre discipline sono le seguenti:
*   **Statistica**: Si concentra sull'inferenza, il testing di ipotesi e la quantificazione dell'incertezza.
*   **Machine Learning**: Riguarda l'apprendimento dai dati, la generalizzazione e la predizione.
*   **Intelligenza Artificiale (AI)**: Rappresenta un sistema più ampio che include ML, regole, RAGionamento e percezione.

## 📊 Dati, Tecnologie e Metriche

Le tecniche EDA si concentrano sull'analisi di diversi aspetti dei dati:
*   **Distribuzione delle variabili**: Esame della forma (asimmetrica, bimodale, gaussiana, power law).
*   **Relazioni tra variabili**: Studio di correlazioni e visualizzazioni come scatter plot.
*   **Outlier**: Identificazione di punti anomali che possono indicare problemi di qualità dei dati o insight significativi.
*   **Pattern temporali**: Analisi per dati con una dimensione temporale.

Le principali tecniche includono:
1.  **Analisi Univariata**: Esamina una singola variabile e le sue statistiche sommarie.
    *   **Tendenza Centrale**:
        *   **Media**: SENSibile agli outlier.
        *   **Mediana**: Robusta agli outlier.
        *   **Moda**: Il valore più frequente.
    *   **Dispersione**:
        *   **Varianza**: Misura la dispersione dei dati rispetto alla media.
        *   **Deviazione standard**: Radice quadrata della varianza, nella stessa unità dei dati originali.
    *   **Asimmetria e Code**:
        *   **Skewness (Pearson)**: Misura l'asimmetria della distribuzione.
        *   **Kurtosis**: Indica la "pesantezza" delle code, suggerendo la frequenza di outlier.
2.  **Analisi Bivariata/Multivariata**: Studia le relazioni tra due o più variabili.
    *   **Covarianza**: Indica se le variabili si muovono nella stessa direzione (positiva) o in direzioni opposte (negativa).
    *   **Correlazione (r)**: Normalizzazione della covarianza, con un range da -1 a +1. Un valore di +1 indica una perfetta correlazione positiva, -1 una perfetta correlazione negativa e 0 nessuna correlazione lineare. È invariante per cambiamento di scala.
3.  **Clustering e riduzione dimensionale**: Tecniche come la PCA (Principal Component Analysis) per ottenere insight da dati ad alta dimensionalità.

## 🔍 Analisi Operativa ed Applicazioni OSINT

L'EDA è un pilastro per la comprensione di fenomeni complessi, come illustrato nel caso studio sulla previsione dei costi degli incidenti cyber.

**Caso Studio: Previsione dei Costi degli Incidenti Cyber**
*   **Problema**: Gli incidenti di [[Cybersecurity]] generano costi altamente eterogenei, rendendo difficile per le organizzazioni stimare le perdite potenziali ex-ante.
*   **Obiettivo**: Predire e spiegare il costo degli incidenti utilizzando Data Analytics.
*   **Insight dall'EDA**:
    *   I costi sono fortemente right-skewed: la maggior parte degli incidenti ha costi bassi, ma pochi hanno costi enormi (heavy tail), con la media significativamente maggiore della mediana.
    *   Incidenti legati a [[Ransomware]] e dati regolamentati dominano la coda dei costi elevati.
    *   La preparazione alla sicurezza (es. `security_maturity_level`) e la velocità di risposta (`time_to_contain_hours`) sono fattori significativi.
    *   È necessaria una [[Regressione]] per spiegare il fenomeno in modo più completo.

**Applicazioni in ambito OSINT**:
L'EDA è cruciale per dare senso ai dati raccolti tramite [[Tecniche]]. Permette di:
*   **Identificare pattern e trend**: Rilevare tendenze in dati aperti, come la diffusione di narrazioni specifiche o l'evoluzione di minacce.
*   **Rilevare anomalie**: Individuare picchi insoliti in menzioni di un argomento, attività sospette su piattaforme o deviazioni da comportamenti attesi.
*   **Comprendere relazioni**: Stabilire correlazioni tra entità (es. attori, eventi, località) per costruire un quadro più completo.
*   **Valutare la qualità dei dati**: Identificare lacune, incoerenze o bias nei dati raccolti, guidando ulteriori attività di raccolta.
*   **Formulare ipotesi investigative**: Gli insight derivanti dall'EDA possono orientare le indagini, suggerendo aree di approfondimento o nuove piste.

## 🔮 Lacune Informative e Prossimi Passi

Sebbene l'EDA sia indispensabile, presenta delle lacune e non può fornire da sola un modello predittivo completo o una spiegazione causale definitiva. I problemi complessi spesso richiedono ulteriori passaggi:
*   **Non linearità**: I fenomeni reali, come i costi cyber, possono crescere in modo non lineare.
*   **Interaction effects**: Le variabili possono interagire tra loro in modi complessi che un'analisi superficiale non rivela.
*   **Heavy tail**: Distribuzioni con code pesanti indicano eventi rari ma di grande impatto, difficili da modellare.
*   **Fattori non osservabili o stocastici**: Alcuni driver del costo o del fenomeno in esame possono essere intrinsecamente non misurabili o casuali.

Per migliorare la modellazione dopo l'EDA, si possono adottare strategie come:
*   **Log-transform**: Applicare trasformazioni logaritmiche a variabili target e predittori asimmetrici per normalizzare le distribuzioni e migliorare le performance della regressione.
*   **Termini di interazione**: Includere nel modello termini che catturano le interazioni tra variabili.
*   **Feature Selection e regolarizzazione**: Ridurre il rumore e prevenire l'overfitting.
*   **Interpretazione cauta**: I coefficienti di correlazione o regressione indicano associazioni statistiche, non necessariamente effetti causali diretti.

È importante notare che un R² basso (es. 0.4-0.5) in domini ad alta variabilità, come la [[Cybersecurity]], può comunque rappresentare un buon risultato, riflettendo la complessità intrinseca e la componente stocastica del fenomeno.

## 🔗 Connessioni e Pattern

- [[Applicazioni osint]]
- [[Cybersecurity]]
- [[Data preparation]]
- [[Data science]]
- [[Osint]]
- [[Previsione dei costi degli incidenti cyber]]


- [[--]]
F/I/H
- [[--]]
