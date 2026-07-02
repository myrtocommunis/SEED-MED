---
title: Decision trees
tags:
- OSINT
- processed
- decision-trees
- machine-learning
- classification
date: '2026-05-15'
status: draft
depth: standard
sources: '1'
tipo: concetto
---

# Decision trees

## 🎯 Sintesi Strategica

I **Decision trees** sono un potente strumento di [[Machine learning]] per la [[Machine learning]] e la regressione, caratterizzati dalla loro intrinseca interpretabilità. Strutturati come diagrammi di flusso, permettono di modellare processi decisionali complessi attraverso una serie di test su attributi, culminando in una predizione di classe o valore. Nel contesto [[Osint]], offrono la capacità di identificare pattern e prendere decisioni basate su dati in modo trasparente, facilitando la comprensione delle logiche sottostanti alle previsioni e l'attribuzione di informazioni.

## 📚 Contesto e Definizioni

La **classificazione** è un compito fondamentale nell'[[Fondamenti di ai|Intelligenza Artificiale]] che mira a predire categorie discrete (es. "alto rischio", "basso rischio"), distinguendosi dalla regressione che predice valori numerici continui. I Decision trees rientrano tra i classificatori non lineari, capaci di definire confini di decisione complessi.

Un Decision tree funziona come un diagramma di flusso:
*   **Nodo interno**: Rappresenta un test su un attributo specifico dei dati.
*   **Ramo**: Corrisponde all'esito di un test.
*   **Foglia**: Contiene l'etichetta di classe o il valore predetto.

**Vantaggi chiave**:
*   **Interpretabilità**: Non sono "black box"; il percorso dalla radice alla foglia è una regola "if-then" leggibile, ideale per spiegare le decisioni a stakeholder non tecnici.
*   **Selezione automatica delle feature**: Identificano e utilizzano automaticamente gli attributi più rilevanti per la classificazione.
*   **Vicinanza al RAGionamento umano**: La loro struttura logica rispecchia processi decisionali intuitivi.
*   **Gestione dati eterogenei**: Possono elaborare sia dati numerici che categoriali senza necessità di normalizzazione estesa.

**Limitazioni**:
*   **Non robustezza**: Piccole variazioni nei dati di input possono portare a cambiamenti significativi nella struttura dell'albero.
*   **Complessità computazionale**: L'ottimizzazione per trovare l'albero migliore è un problema NP-Completo.
*   **Tendenza all'Overfitting**: Se non controllati, possono memorizzare i dati di addestramento, perdendo la capacità di generalizzare su nuovi dati.

## 📊 Dati, Tecnologie e Metriche

La valutazione delle prestazioni di un classificatore, inclusi i Decision trees, si basa su metriche derivate dalla Confusion Matrix.

### Confusion Matrix

Una tabella che riassume le prestazioni di un algoritmo di classificazione, specialmente per problemi binari:

| | Predetto Positivo | Predetto Negativo |
|---|---|---|
| **Reale Positivo** | True Positive (TP) | False Negative (FN) |
| **Reale Negativo** | False Positive (FP) | True Negative (TN) |

### Metriche Derivate

*   **Accuracy**: Percentuale di predizioni corrette totali. `(TP+TN)/(TP+TN+FP+FN)`
*   **Precision**: Proporzione di veri positivi tra tutti i positivi predetti. Utile quando il costo di un Falso Positivo è elevato (es. spam filtering). `TP/(TP+FP)`
*   **Recall (SENSibilità)**: Proporzione di veri positivi tra tutti i reali positivi. Utile quando il costo di un Falso Negativo è elevato (es. rilevamento frodi, diagnosi mediche). `TP/(TP+FN)`
*   **F1-Score**: Media armonica di Precision e Recall, utile quando si cerca un equilibrio tra le due. `2×(P×R)/(P+R)`

La scelta della metrica è cruciale e dipende dal contesto operativo e dal costo associato ai diversi tipi di errore.

### Overfitting e Pruning

I Decision trees sono particolarmente suscettibili all'Overfitting, dove un albero troppo grande memorizza i dati di addestramento (basso bias, alta varianza) ma fallisce su dati nuovi. Al contrario, un albero troppo piccolo può soffrire di Underfitting (alto bias, bassa varianza).

La soluzione principale per mitigare l'overfitting è il **Pruning (Potatura)**, che consiste nell'accorciare i rami dell'albero convertendo nodi di diramazione in foglie. Questo riduce la complessità del modello e migliora la sua capacità di generalizzazione.

### ENSemble Learning: Bagging e Random Forest

Per superare i limiti del singolo Decision tree, si ricorre spesso all'ENSemble Learning, che combina più modelli per migliorare le prestazioni complessive.

*   **Bagging (Bootstrap Aggregating)**: Crea più campioni bootstrap (con reintroduzione) dal dataset di addestramento, addestra un Decision tree su ciascuno e aggrega le predizioni (voto di maggioranza per la classificazione, media per la regressione). Questo riduce la varianza.
*   **Random Forest**: Un'estensione del Bagging che introduce un'ulteriore randomizzazione. Oltre a campionare il dataset, per ogni split di un nodo, seleziona un **sottoinsieme casuale di feature** da considerare. Questo riduce ulteriormente la correlazione tra gli alberi, portando a una maggiore riduzione della varianza e prestazioni superiori rispetto al singolo albero nella maggior parte dei casi.

## 🔍 Analisi Operativa ed Applicazioni OSINT

Nell'ambito [[Osint]], i Decision trees e, in particolare, i Random Forest offrono capacità significative:

*   **Classificazione di fonti e contenuti**: Identificare se una fonte è affidabile, se un contenuto è disinformazione, o categorizzare documenti in base al loro argomento o sentiment.
*   **Rilevamento di anomalie**: Identificare comportamenti o dati che si discostano dalla norma, potenzialmente indicando attività sospette o minacce.
*   **Attribuzione**: Aiutare nell'attribuzione di attività online a specifici attori o gruppi, analizzando pattern di comportamento o caratteristiche dei dati.
*   **Analisi di sentiment**: Classificare il tono emotivo di testi estratti da social media o forum, per monitorare l'opinione pubblica o reazioni a eventi.
*   **Supporto decisionale**: La natura interpretabile dei Decision trees è fondamentale per spiegare agli analisti OSINT e ai decisori il perché di una certa classificazione o predizione, ad esempio, quali fattori hanno portato a classificare un'entità come "ad alto rischio".
*   **Prioritizzazione delle informazioni**: Classificare l'importanza o l'urgenza di nuove informazioni acquisite, guidando gli analisti su dove concentrare le risorse.

La scelta delle metriche è cruciale: in scenari OSINT, potrebbe essere necessario massimizzare la **Recall** per non perdere informazioni critiche (minimizzare i Falsi Negativi) o massimizzare la **Precision** per evitare di sovraccaricare gli analisti con Falsi Positivi.

## 🔮 Lacune Informative e Prossimi Passi

Nonostante la loro efficacia, l'applicazione dei Decision trees in contesti OSINT presenta sfide:
*   **Gestione di dati non strutturati**: I dati OSINT sono spesso non strutturati (testi, immagini, video), richiedendo fasi di pre-elaborazione complesse per estrarre feature adatte ai Decision trees.
*   **Robustezza al rumore**: La sensibilità dei singoli alberi al rumore e alle piccole perturbazioni nei dati può essere un problema in ambienti OSINT caratterizzati da dati incompleti o fuorvianti.
*   **Scalabilità**: Per dataset estremamente grandi, l'addestramento di foreste casuali può essere computazionalmente intensivo.
*   **Evoluzione dei pattern**: I pattern di interesse OSINT possono evolvere rapidamente, richiedendo un riaddestramento frequente dei modelli.

I prossimi passi includono l'esplorazione di tecniche ibride che combinano Decision trees con modelli di deep learning per la gestione di dati complessi, e lo sviluppo di metodologie per l'aggiornamento continuo dei modelli in ambienti dinamici.

## 🔗 Connessioni e Pattern

- [[Applicazioni osint]]
- [[Classificazione]]
- [[Deep learning]]
- [[Disinformazione]]
- [[Machine learning]]
- [[Osint]]


- [[--]]
F/I/H
- [[--]]
