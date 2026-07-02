---
title: Regressione lineare
tags:
- OSINT
- processed
- regressione-lineare
date: '2026-05-15'
status: draft
depth: standard
sources: '3'
tipo: concetto
---

# Regressione lineare

## 🎯 Sintesi Strategica

La regressione lineare è un algoritmo fondamentale di [[Machine learning]] progettato per modellare la relazione tra una variabile dipendente continua e una o più variabili indipendenti. A differenza dei metodi statistici tradizionali focalizzati sulla verifica di ipotesi, questo approccio è orientato alla [[Analisi]]: stima valori futuri a partire da pattern storici minimizzando l'errore quadratico. Nel contesto dell'intelligence, costituisce un pilastro per la quantificazione di trend, la stima di costi operativi e il monitoraggio di indicatori numerici in scenari dinamici.

## 📚 Contesto e Definizioni

La formulazione matematica di base esprime la variabile target $y$ come combinazione lineare delle feature $x_1, \dots, x_n$ più un termine di bias $\theta_0$ e un errore residuo $\varepsilon$:
$$y = \theta_0 + \theta_1 x_1 + \theta_2 x_2 + \dots + \theta_n x_n + \varepsilon$$
L'ottimizzazione avviene tramite Ordinary Least Squares (OLS), che minimizza la somma dei quadrati dei residui $\sum (y_{\text{true}} - y_{\text{pred}})^2$. Il modello assume una relazione lineare tra input e output e richiede feature numericamente scalabili. Per mitigare la multicollinearità e l'overfitting, vengono impiegate varianti regolarizzate:
- **Ridge Regression**: penalità L2 che contrae i coefficienti verso zero senza annullarli.
- **Lasso Regression**: penalità L1 che forza la sparsità, eseguendo selezione automatica delle feature.
- **Elastic-Net**: combinazione lineare di L1 e L2, ideale per dataset con feature altamente correlate.

## 📊 Dati, Tecnologie e Metriche

La valutazione della performance si basa su metriche specifiche per variabili continue:
- **MAE (Mean Absolute Error)**: media degli errori assoluti. Robusta agli outlier, mantiene la stessa unità di misura del target.
- **RMSE (Root Mean Square Error)**: radice della media degli errori al quadrato. Penalizza fortemente gli errori grandi, rendendola adatta a contesti con asimmetria di rischio.
- **$R^2$ (Coefficiente di Determinazione)**: proporzione di varianza del target spiegata dal modello. Range teorico $(-\infty, 1]$, dove $1$ indica fit perfetto e $0$ corrisponde alla performance della media dei dati.

La generalizzazione viene garantita tramite strategie di Validazione dei Modelli:
- **Single Split**: partizione casuale train/validation. Semplice ma sensibile alla seed.
- **K-Fold Cross Validation**: partizione in $K$ sottoinsiemi; ogni fold funge da validation una volta. Standard $K=5$ o $K=10$.
- **LOOCV (Leave-One-Out)**: caso estremo $K=N$. Massima utilizzazione dei dati, stima a bassa varianza, ma elevato costo computazionale.

## 🔍 Analisi Operativa ed Applicazioni OSINT

Nel dominio della [[Cyber threat intelligence]], la regressione lineare supporta:
- **Stima dei costi incidenti**: previsione di impatti finanziari basata su volumi di allerta, tempo di rilevamento e superficie di attacco.
- **Monitoraggio infrastrutture**: tracciamento della crescita di nodi C2, domini registratati o attività di scanning.
- **Indicatori geopolitici**: forecasting di flussi migratori, prezzi di commodity o volumi di traffico dati anomalo.

In ambito cybersecurity, il **RMSE è preferibile al MAE** poiché un singolo evento critico genera costi ordini di grandezza superiori alla media; la metrica quadratico assicura che il modello non sottostimi sistematicamente le code di rischio. La valutazione finale deve sempre avvenire su un test set non visto durante l'addestramento per evitare stime ottimistiche. I coefficienti descrivono associazioni statistiche, non nessi causali; la presenza di confounders omessi può distorcere l'interpretazione operativa.

## 🔮 Lacune Informative e Prossimi Passi

- **Assunzione di linearità**: il modello non cattura automaticamente relazioni non lineari o interazioni complesse senza feature engineering esplicita o trasformazioni kernel.
- **SENSibilità agli outlier**: nonostante la regolarizzazione, valori estremi possono spostare l'iperpiano di decisione; richiedono preprocessing robusto o loss function alternative (es. Huber).
- **Selezione delle feature**: la regressione non identifica autonomamente le variabili causalmente rilevanti; richiede pipeline di selezione basate su dominio o metodi wrapper/embedded.
- **Prossimi passi**: integrazione con framework di inferenza causale, automazione della selezione delle feature tramite ENSemble methods, e adozione di regressione non lineare (es. spline, kernel ridge) per pattern complessi.

## 🔗 Connessioni e Pattern

- [[Applicazioni osint]]
- [[Automazione]]
- [[Cybersecurity]]
- [[Infrastrutture]]
- [[Machine learning]]
- [[Threat intelligence]]


- [[--]]
F/I/H
- [[--]]
