---
title: Case study eda
tags:
- OSINT
- processed
- case-study-eda
date: '2026-05-15'
status: draft
depth: standard
sources: '1'
tipo: concetto
---

# Case study eda

## 🎯 Sintesi Strategica

L'Exploratory Data Analysis (EDA) rappresenta la fase metodologica critica nel ciclo di vita della data science applicata alla cybersecurity, antecedente e propedeutica alla modellazione predittiva. Attraverso l'indagine statistica descrittiva e la visualizzazione, l'EDA identifica pattern, anomalie e relazioni non lineari nei dataset incidentali, ottimizzando la feature engineering e mitigando il rischio di overfitting. Nel contesto della stima dei costi degli incidenti informatici, l'analisi esplorativa rivela distribuzioni fortemente asimmetriche e driver critici come il livello di maturità della sicurezza e i tempi di containment, fornendo le basi per modelli di regressione robusti, interpretabili e allineati alla realtà operativa del Threat Modeling.

## 📚 Contesto e Definizioni

L'Exploratory Data Analysis (EDA) è una metodologia analitica sviluppata per l'indagine aperta dei dataset, volta a scoprire strutture sottostanti, formulare ipotesi e validare assunzioni prima della modellazione formale. A differenza dell'analisi confermativa, che verifica ipotesi predefinite, l'EDA privilegia l'osservazione induttiva. Le tecniche si suddividono in: univariata (distribuzioni, misure di tendenza centrale e dispersione, skewness, kurtosis), bivariata/multivariata (covarianza, correlazione, scatter plots) e di riduzione dimensionale (es. PCA). Nel panorama della [[Data science]] e della [[Cybersecurity]], l'EDA costituisce il ponte tra la raccolta dei dati grezzi e la costruzione di pipeline di [[Machine learning]], garantendo che le variabili di input siano statisticamente coerenti con i requisiti del modello target.

## 📊 Dati, Tecnologie e Metriche

Il case study analizza un dataset strutturato su 5.000 incidenti informatici, con la variabile target `incident_cost_usd`. Le feature operative includono `num_affected_devices`, `num_affected_users`, `data_volume_exposed_gb`, `organization_size`, `industry_sector`, `security_maturity_level`, `incident_type`, `attack_vector`, `time_to_detect_hours` e `time_to_contain_hours`.
L'analisi esplorativa evidenzia:
- Distribuzione della variabile target: fortemente right-skewed con heavy tail, dove media e mediana divergono significativamente.
- Ransomware e violazioni di dati regolamentati concentrano la coda dei costi elevati.
- Relazione costi/dispositivi colpiti: positiva ma non lineare.
- Predittori statistici significativi: `security_maturity_level` e `time_to_contain_hours`.
L'applicazione di regressione lineare standard mostra un R² limitato (0.4-0.5), attribuibile a non linearità intrinseche, interaction effects non catturati, heavy tail distribution e driver latenti. Le ottimizzazioni tecniche prevedono log-transform per la skewness, aggiunta di termini di interazione, feature selection avanzata e regolarizzazione (Lasso/Ridge).

## 🔍 Analisi Operativa ed Applicazioni OSINT

Nell'ecosistema [[Osint]] e threat intelligence, l'EDA applicata ai costi degli incidenti permette di quantificare il rischio finanziario e ottimizzare l'allocazione delle risorse di difesa. L'identificazione di correlazioni tra maturità della sicurezza e tempi di containment supporta la creazione di benchmark settoriali e piani di risposta agli incidenti (IRP) data-driven. I dataset esplorati, spesso aggregati da report di settore e breach notification database, forniscono indicatori di compromissione (IoC) e indicatori di rischio (IoR) per la valutazione proattiva. La capacità di distinguere correlazione statistica da causalità operativa è cruciale per evitare bias decisionali nella pianificazione della continuità operativa.

## 🔮 Lacune Informative e Prossimi Passi

La modellazione attuale presenta limiti strutturali: la regressione lineare non cattura appieno le interazioni non lineari tra vettori di attacco e contesti organizzativi. Mancano dataset longitudinali che traccino l'evoluzione temporale dei costi e l'impatto di framework di compliance sulla variabile target. I prossimi passi includono l'implementazione di modelli ENSemble (Random Forest, XGBoost), l'analisi delle serie temporali per la previsione dei costi cumulativi, e l'integrazione di dati OSINT in tempo reale per aggiornare dinamicamente i pesi delle feature. La validazione incrociata su dataset multi-organizzativi rimane essenziale per generalizzare i risultati e ridurre la varianza residua.

## 🔗 Connessioni e Pattern

- [[Applicazioni osint]]
- [[Data science]]
- [[Machine learning]]
- [[Osint]]
- [[Regressione lineare]]
- [[Threat intelligence]]


- [[--]]
F/I/H
- [[--]]
