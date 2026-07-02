---
title: Quattro metriche per l'analisi osint
tags:
- OSINT
- processed
- quattro-metriche-per-l'analisi-osint
- SNA
- network-analysis
date: '2026-05-15'
status: draft
depth: standard
sources: multiple
tipo: concetto
---

# Quattro metriche per l'analisi osint

## 🎯 Sintesi Strategica

Le "Quattro metriche per l'analisi OSINT" rappresentano i pilastri della [[Social network analysis]] (SNA) applicata all'[[Osint|Open Source Intelligence]]. Queste metriche di centralità – Degree, Betweenness, Closeness ed Eigenvector – consentono di quantificare e interpretare diverse sfaccettature dell'importanza e dell'influenza di nodi (individui, organizzazioni, entità) all'interno di una rete. La loro applicazione combinata è fondamentale per identificare [[Social network analysis|Influencer]], mediatori strategici, nodi con capacità di diffusione rapida delle informazioni e attori con reale prestigio o autorità, fornendo una comprensione profonda delle dinamiche relazionali e dei flussi informativi in contesti OSINT.

## 📚 Contesto e Definizioni

Il concetto di centralità nelle reti sociali è stato formalizzato da Linton C. Freeman nel 1978, definendo le quattro metriche canoniche che permettono di valutare l'importanza strutturale di un nodo. In ambito OSINT, l'analisi di queste metriche è cruciale per trasformare dati grezzi su connessioni e interazioni in intelligence azionabile, mappando strutture di potere, flussi di comunicazione e ruoli chiave all'interno di reti complesse. L'obiettivo è andare oltre la semplice visibilità per comprendere il reale impatto e la funzione di ogni attore.

## 📊 Dati, Tecnologie e Metriche

Le quattro metriche di centralità sono:

1.  **Degree Centrality (Popolarità)**
    *   **Definizione**: Misura il numero di connessioni dirette (link) che un nodo possiede.
    *   **Formula**: Semplicemente il conteggio dei link incidenti al nodo.
    *   **Interpretazione**: Un alto valore indica un nodo "hub", molto connesso e visibile. Un basso valore denota un nodo periferico.
    *   **Uso OSINT**: Identificazione di [[Social network analysis|Influencer]], account social con un elevato numero di follower o following, o entità con molte interazioni dirette.

2.  **Betweenness Centrality (Controllo)**
    *   **Definizione**: Quantifica la misura in cui un nodo si trova sui cammini più brevi tra altre coppie di nodi.
    *   **Formula**: $BC(v) = \sum_{s \neq v \neq t} \frac{\sigma_{st}(v)}{\sigma_{st}}$, dove $\sigma_{st}$ è il numero totale di cammini più brevi tra $s$ e $t$, e $\sigma_{st}(v)$ è il numero di quei cammini che passano per $v$.
    *   **Interpretazione**: Un alto valore indica un "broker" o "gatekeeper", un nodo cruciale per il flusso informativo tra diversi gruppi o sottoreti.
    *   **Uso OSINT**: Identificazione di mediatori, nodi strategici nascosti che controllano la diffusione delle informazioni, spesso non evidenti tramite la sola Degree Centrality. È una metrica computazionalmente intensiva, con complessità $O(VE)$ per grafi non pesati, rendendola complessa per reti di [[Big data 5v|Big data]] senza l'uso di algoritmi ottimizzati o tecniche di sampling.

3.  **Closeness Centrality (Rapidità)**
    *   **Definizione**: Misura la distanza media di un nodo da tutti gli altri nodi della rete.
    *   **Formula**: L'inverso della somma delle distanze minime da un nodo a tutti gli altri nodi.
    *   **Interpretazione**: Un alto valore indica che il nodo può RAGgiungere rapidamente tutti gli altri nodi della rete, facilitando una rapida diffusione delle informazioni.
    *   **Uso OSINT**: Analisi di reti comunicative, identificazione di nodi con accesso più rapido all'informazione o capacità di diffusione efficiente.

4.  **Eigenvector Centrality (Prestigio)**
    *   **Definizione**: Un nodo è considerato importante se è connesso a nodi importanti. La sua centralità è proporzionale alla somma delle centralità dei suoi vicini.
    *   **Formula**: Iterativa, dove la centralità di un nodo è una funzione lineare della centralità dei suoi vicini. Logica analoga all'algoritmo [[Network analysis|PageRank]] di Google, sebbene l'Eigenvector Centrality non gestisca direttamente il damping factor o i dead-end come fa [[PageRank]].
    *   **Interpretazione**: Un alto valore indica prestigio, autorità o influenza reale all'interno della rete.
    *   **Uso OSINT**: Mappatura di strutture di potere, élite, leadership e attori con influenza significativa.

Per un confronto significativo, le metriche vengono spesso **normalizzate** su una scala da 0 a 1. La **visualizzazione** può beneficiare della combinazione di metriche, ad esempio usando la dimensione del nodo per la Degree Centrality e il colore per la Betweenness Centrality per evidenziare contemporaneamente popolarità e controllo dei flussi.

## 🔍 Analisi Operativa ed Applicazioni OSINT

L'applicazione delle metriche di centralità in OSINT permette di rispondere a domande operative specifiche, guidando l'analista verso una comprensione più profonda della struttura e delle dinamiche della rete:

| Obiettivo OSINT | Metrica Consigliata |
| :---------------- | :------------------ |
| Identificare la popolarità o visibilità | Degree Centrality |
| Rilevare mediatori e gatekeeper | Betweenness Centrality |
| Mappare la capacità di diffusione rapida | Closeness Centrality |
| Valutare prestigio e influenza reale | Eigenvector Centrality |
| Analizzare la resilienza della rete | Betweenness Centrality |

È cruciale utilizzare e confrontare tutte le metriche, poiché rispondono a domande diverse e offrono prospettive complementari. Ad esempio, un nodo con alta Degree Centrality (un hub popolare) non è necessariamente un attore strategicamente potente; la Betweenness Centrality può rivelare [[Attori]] o nodi chiave che, pur non essendo popolari, controllano passaggi vitali di informazione. La correlazione tra Degree ed Eigenvector Centrality è spesso elevata in reti reali, mentre la Betweenness Centrality tende ad essere più indipendente, identificando ruoli unici.

Queste metriche sono impiegate per:
*   Identificare i nodi più influenti in campagne di disinformazione.
*   Mappare le gerarchie e le interconnessioni in reti criminali o terroristiche.
*   Comprendere la diffusione di notizie o malware.
*   Valutare la vulnerabilità di una rete alla rimozione di nodi specifici (resilienza).

## 🔮 Lacune Informative e Prossimi Passi

Per un'analisi OSINT avanzata, è necessario integrare le metriche canoniche con considerazioni aggiuntive e strumenti specifici:

*   **Formule Operative**: Per un'implementazione pratica, è essenziale disporre delle formule matematiche complete e degli algoritmi sottostanti.
*   **Limiti Computazionali**: La Betweenness Centrality, in particolare, è computazionalmente costosa. Per reti di milioni di nodi, tipiche dell'OSINT su larga scala, sono indispensabili tecniche di sampling, approssimazione o l'uso di architetture di calcolo distribuito.
*   **Metriche Complementari**:
    *   **[[Modularità]]**: Essenziale per valutare la qualità delle comunità o cluster identificati all'interno della rete, spesso rilevati tramite Betweenness o Closeness.
    *   **[[K-shell decomposition]]**: Utile per identificare i nuclei strutturati e le gerarchie interne in reti di grandi dimensioni.
    *   **[[Centralità di Katz]]**: Una generalizzazione dell'Eigenvector Centrality che considera anche i cammini brevi, attribuendo importanza ai nodi che sono RAGgiungibili tramite molti percorsi, anche se non i più brevi.
*   **Strumenti e Piattaforme**: L'applicazione pratica richiede l'uso di librerie di analisi di rete come NetworkX (Python), igraph (R/Python), o software di visualizzazione e analisi come Gephi.
*   **Damping e Dead-ends**: È importante notare che l'Eigenvector Centrality, a differenza di algoritmi più sofisticati come [[Network analysis|PageRank]], non include meccanismi per gestire il "damping factor" o i "dead-ends" (nodi senza link in uscita), che possono influenzare la sua applicabilità in certi contesti di rete.

## 🔗 Connessioni e Pattern

- [[Applicazioni osint]]
- [[Big data 5v|Big data]]
- [[Centralità nelle reti sociali]]
- [[Disinformazione]]
- [[Network analysis]]
- [[Social network analysis]]


- [[--]]
F/I/H
- [[--]]
