---
title: Fondamenti unsupervised learning
tags:
- OSINT
- processed
- fondamenti-unsupervised-learning
date: '2026-05-15'
status: draft
depth: standard
sources: '1'
tipo: concetto
---

# Fondamenti unsupervised learning

## 🎯 Sintesi Strategica

I fondamenti dell'[[Unsupervised learning]] rappresentano una metodologia cruciale nell'[[Analisi]] e in [[Osint]] per l'esplorazione e la scoperta di pattern nascosti all'interno di dataset privi di etichette predefinite. A differenza dell'apprendimento supervisioNATO, che si basa su dati etichettati per addestrare modelli predittivi, l'unsupervised learning mira a identificare strutture intrinseche, RAGgruppamenti (come nel [[Clustering]]) o anomalie, fornendo intuizioni preziose senza alcuna conoscenza a priori del risultato desiderato. Questo approccio è fondamentale per trasformare grandi volumi di dati grezzi in informazioni actionable, specialmente in contesti dove l'etichettatura manuale è impraticabile o impossibile.

## 📚 Contesto e Definizioni

L'[[Unsupervised learning]] è una branca del [[Machine learning]] che si occupa di inferire funzioni per descrivere una struttura nascosta da dati non etichettati. Il suo obiettivo principale è modellare la struttura o la distribuzione sottostante nei dati per apprendere di più sui dati stessi.

Il concetto centrale è il **[[Clustering]]**, ovvero il RAGgruppamento di un insieme di oggetti in modo che gli oggetti nello stesso gruppo (chiamato cluster) siano più simili tra loro rispetto a quelli in altri gruppi. È importante notare che il clustering è spesso considerato un "ill-posed problem" secondo Hadamard: una soluzione ideale dovrebbe esistere, essere unica e dipendere continuamente dalle condizioni iniziali. Il clustering, tuttavia, raramente soddisfa tutte queste condizioni, poiché la "migliore" partizione dei dati dipende fortemente dal criterio di similarità scelto e dalla domanda analitica.

Una metafora utile per comprendere questa flessibilità è la "famiglia Simpson": la stessa famiglia può essere partizionata in modi diversi (per ruolo familiare, ruolo scolastico, genere), e tutte le partizioni sono sensate ma rispondono a domande diverse. Analogamente, in [[Osint]], le stesse entità (persone, organizzazioni, domini) possono essere RAGgruppate in molteplici modi a seconda del criterio di analisi, rivelando pattern differenti.

## 📊 Dati, Tecnologie e Metriche

Le tecnologie di unsupervised learning si basano su diversi algoritmi, ciascuno con specificità e applicazioni distinte:

*   **K-Means (Centroid-Based)**: Algoritmo che divide i dati in `k` cluster (numero definito dall'analista), minimizzando la somma delle distanze al quadrato dei punti dal centroide del proprio cluster (inerzia). È scalabile (O(n·k·i·d)) ma assume cluster convessi e isotropici, fallendo su forme irregolari. `Minibatchkmeans` è una variante per dataset di grandi dimensioni.
*   **[[Clustering]] (Bottom-Up)**: Inizia con ogni osservazione come cluster separato e fonde iterativamente i cluster più vicini. Il `Dendrogramma` visualizza la gerarchia, permettendo di determinare la granularità dei cluster tramite un "taglio". Le strategie di linkage includono Ward, single, average e complete.
*   **DBSCAN (DENSity-Based Spatial Clustering of Applications with Noise)**: Identifica regioni connesse ad alta densità. Definisce `core samples` (punti in aree dense), `periphery samples` (vicini a core ma non core) e `noise samples` (isolati). Richiede due parametri critici: `eps` (RAGgio) e `min_samples` (densità minima), la cui scelta può essere supportata da euristiche come il "knee plot" delle distanze dei vicini più prossimi.
*   **HDBSCAN (Hierarchical DBSCAN)**: Estensione di DBSCAN che non richiede il parametro `eps`, gestendo cluster con densità variabile nello stesso dataset. Si basa sulla costruzione di un Minimum Spanning Tree (MST) e sul taglio degli edge con peso maggiore.
*   **OPTICS (Ordering Points To Identify the Clustering Structure)**: Generalizzazione di DBSCAN che produce un "reachability graph" per scoprire cluster a densità multipla con una singola esecuzione, più efficiente per ripetute analisi a vari `eps`.
*   **Bisecting K-Means**: Variante di K-Means che utilizza un approccio di clustering divisivo, suddividendo iterativamente il cluster più grande o quello con la maggiore inerzia.
*   **Altri Algoritmi**: Includono Mean-Shift (scoperta di "blobs" con numero automatico di cluster), Affinity Propagation (basato su "exemplar"), Spectral Clustering (embedding a bassa dimensione seguito da K-Means), BIRCH (efficiente per dataset enormi tramite CF Tree), Gaussian Mixture (clustering probabilistico).

**Tecniche di Valutazione (senza ground truth)**:
*   **Silhouette score**: Misura la compattezza interna e la separazione esterna dei cluster.
*   **Inertia**: Somma delle distanze al quadrato all'interno del cluster (valori inferiori indicano cluster più compatti, ma assume forme convesse).
*   **Dendrogramma**: Ispezione visiva per piccoli campioni, non quantitativa.
*   **Domain Knowledge**: Giudizio umano sull'interpretabilità e utilità dei risultati.

**Pipeline [[Nlp]] (per analisi testuale non supervisionata)**:
1.  Tokenization
2.  Stopwords removal
3.  Normalization (lowercasing, punteggiatura, spazi bianchi)
4.  Stemming/Lemmatization
5.  POS tagging (opzionale)
*   **Bag of Words**: Rappresentazione documento-termine basata sulla frequenza. Limiti: vocabolario enorme, perdita dell'ordine, frequenza non sempre equivale a rilevanza.
*   **TF-IDF**: Pesa i termini per rilevanza (Term Frequency × Inverse Document Frequency), mitigando i limiti del Bag of Words.

**[[Deep learning]] (per estrazione di feature non supervisionata)**:
*   **Architetture di Reti Neurali (NN)**: Modelli con nodi connessi da edge, organizzati in strati.
*   **Perceptron**: Unità di base di una NN, con input, pesi, sommatoria, bias e funzione di attivazione.
*   **Training**: Processo iterativo che include forward pass (calcolo della loss), backpropagation (propagazione dell'errore all'indietro) e gradient descent (ottimizzazione dei pesi).
*   **[[Cnn]] (Convolutional Neural Networks)**: Reti feed-forward per immagini, con strati convoluzionali (estrazione di feature tramite kernel), ReLU (funzione di attivazione), pooling (riduzione dimensionalità) e strati densi finali. Preservano le relazioni spaziali dei pixel.
*   **Transfer Learning**: Riutilizzo di modelli di [[Fondamenti di ai|Intelligenza Artificiale]] pre-addestrati su un task (es. riconoscimento immagini) per un task simile, personalizzando solo gli strati di output. Vantaggi: minor costo computazionale, efficacia con dati limitati.

## 🔍 Analisi Operativa ed Applicazioni OSINT

L'unsupervised learning è uno strumento potente in [[Osint]] per scoprire strutture e relazioni nascoste in dati non strutturati o semi-strutturati. Le sue applicazioni includono:

*   **Segmentazione di entità sospette**: Utilizzo di algoritmi come K-Means o HDBSCAN per RAGgruppare individui, organizzazioni o domini con comportamenti simili o caratteristiche comuni, facilitando l'identificazione di reti o gruppi di interesse.
*   **Rilevamento di anomalie e pattern di comportamento irregolari**: Algoritmi come DBSCAN o OPTICS sono eccellenti per identificare outlier o punti di dati che non si conformano a nessun cluster, indicando potenziali attività anomale o minacce.
*   **Analisi di hotspot criminali**: L'applicazione di tecniche density-based permette di individuare aree geografiche o contesti digitali con un'alta concentrazione di attività illecite o sospette.
*   **Community detection in social network**: L'unsupervised learning può rivelare comunità o gruppi di utenti con interazioni significative all'interno di reti sociali, anche in presenza di rumore informativo.
*   **Sistemi di raccomandazione**: Sebbene spesso associati all'apprendimento supervisioNATO, tecniche non supervisionate possono identificare pattern di comportamento per suggerire contenuti o connessioni.
*   **Analisi di testi e documenti**: L'uso di [[Nlp]] non supervisioNATO (es. topic modeling con Latent Dirichlet Allocation, non menzioNATO esplicitamente ma implicito nella pipeline) permette di scoprire temi e argomenti principali in grandi corpus di testo senza etichette.

La scelta dell'algoritmo dipende dalla natura dei dati e dalla domanda analitica:
*   **Dati con forma cluster semplice e compatta**: K-Means o Bisecting K-Means.
*   **Dati con densità variabile o forme irregolari**: DBSCAN, OPTICS, HDBSCAN.
*   **Necessità di una gerarchia**: [[Clustering]].

## 🔮 Lacune Informative e Prossimi Passi

Nonostante la sua potenza, l'unsupervised learning presenta diverse sfide e lacune informative:

*   **Scelta dei parametri**: La determinazione del numero ottimale di cluster (`k` per K-Means) o dei parametri di densità (`eps`, `min_samples` per DBSCAN) è spesso arbitraria e richiede euristiche, Domain Knowledge o sperimentazione, influenzando significativamente i risultati. La "Z13 irrisolta" per i parametri di DBSCAN evidenzia questa difficoltà.
*   **Interpretazione dei risultati**: I cluster scoperti non sono proprietà naturali dei dati, ma l'effetto del criterio di RAGgruppamento scelto. L'interpretazione e la validazione dei cluster richiedono un'attenta analisi umana e la conoscenza del dominio per garantirne l'utilità e la significatività in [[Osint]].
*   **Valutazione senza ground truth**: La mancanza di etichette rende difficile una valutazione oggettiva delle performance del modello, affidandosi spesso a metriche interne (Silhouette, Inertia) che possono non riflettere l'utilità pratica.
*   **Scalabilità**: Alcuni algoritmi possono essere computazionalmente intensivi su dataset molto grandi, richiedendo varianti ottimizzate o approcci distribuiti.
*   **Gestione del rumore**: Alcuni algoritmi sono sensibili al rumore nei dati, che può distorcere la formazione dei cluster.

I prossimi passi nella ricerca e applicazione includono lo sviluppo di metodi più robusti per la selezione automatica dei parametri, tecniche di visualizzazione avanzate per facilitare l'interpretazione dei cluster e l'integrazione con approcci semi-supervisionati per sfruttare al meglio anche piccole quantità di dati etichettati.

## 🔗 Connessioni e Pattern

- [[Clustering]]
- [[Cnn]]
- [[Deep learning]]
- [[Nlp]]
- [[Osint]]
- [[Unsupervised learning]]


- [[--]]
F/I/H
- [[--]]
