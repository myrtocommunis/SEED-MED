---
title: Analisi dei conflitti
tags:
- OSINT
- processed
- analisi-dei-conflitti
date: '2026-05-15'
status: draft
depth: standard
sources: '1'
tipo: concetto
---

# Analisi dei conflitti

## 🎯 Sintesi Strategica

L'analisi dei conflitti e la [[Network analysis]] rappresentano un pilastro operativo dell'[[Osint]] moderna, dalla mappatura di reti criminali transnazionali al monitoraggio di conflitti geografici distribuiti globalmente. Questo approccio integra due framework complementari: la **piattaforma ACLED** (Armed Conflict Location & Event Data) per la raccolta e l'analisi dei dati sui conflitti a livello mondiale, e la **Network Analysis tramite grafi** (con [[Neo4j]] come motore principale) per la visualizzazione di relazioni complesse. ACLED funge da sistema di allerta globale per conflitti armati, raccogliendo dati strutturati su eventi bellici in tempo reale. La Network Analysis, invece, traduce relazioni (sociali, transazionali, infrastrutturali) in modelli visibili che rivelano pattern nascosti di connettività. L'integrazione con strumenti di [[Dashboarding]] basati su intelligenza artificiale eleva questi modelli a un livello operativo superiore.

## 📚 Contesto e Definizioni

L'analisi dei conflitti, nel contesto dell'[[Osint]], si concentra sulla comprensione dinamica delle tensioni, delle violenze e delle instabilità a livello globale. Un elemento centrale è la **piattaforma ACLED (Armed Conflict Location & Event Data)**, che raccoglie dati strutturati sui conflitti in tutto il mondo. Per l'analista [[Geopolitica|geopolitico-finanziario]], ACLED è un dataset fondamentale per:
1.  **Geolocalizzazione precisa** di ogni evento di conflitto (latitudine/longitudine).
2.  **Classificazione standardizzata** del tipo di evento (battaglia, violenza contro civili, proteste, ecc.).
3.  **Identificazione degli agenti** coinvolti (forze governative, ribelli, milizie, forze straniere).
4.  **Conteggio di cause e vittime** per ogni evento.
5.  **Aggiornamento continuo** con dati quasi in tempo reale.

### Dataset Complementari per Intelligence

L'interconnessione tra questi dataset permette la creazione di dashboard geopolitiche integrate, correlare eventi ACLED con indicatori economici o demografici.

| Dataset             | URL                       | Tipo di Dati                                   | Applicazione Strategica                                                              |
| :------------------ | :------------------------ | :--------------------------------------------- | :----------------------------------------------------------------------------------- |
| **ACLED**       | acled.info                | Eventi di conflitto armato con geolocalizzazione | Early warning per escalation geopolitiche, mappatura dei teatri operativi            |
| **Kaggle Datasets** | kaggle.com/datasets       | Dataset crowdsourced multi-tematico            | Complemento a ACLED per dati economici e demografici correlati                  |
| **Our World in Data** | ourworldindata.org        | Indicatori globali aggregati                   | Correlazione conflitti ↔ povertà ↔ migrazioni ↔ instabilità finanziaria              |
| **OpenBDAP**        | openbdap.rgs.mef.gov.it   | Spesa pubblica PA italiana                     | Monitorare come i conflitti esterni impattano la spesa per difesa/esteri italiana |

## 📊 Dati, Tecnologie e Metriche

I **grafici (graph models)** sono modelli matematici usati per rappresentare relazioni tra dati. Un grafo è composto da:

| Elemento            | Definizione                               | Esempio OSINT                                     |
| :------------------ | :---------------------------------------- | :------------------------------------------------ |
| **Nodi (Nodes)**    | Elementi/entità                           | Wallet crypto, soggetti sanzionati, paesi         |
| **Link (Archi/Edges)** | Relazioni tra nodi                        | Transazioni finanziarie, follow social, alleanze militari |
| **Grafo (Graph)**   | Insieme completo di nodi + link           | Intera rete di transazioni illecite               |

### Tipologie di Relazioni (Direzionalità)

| Tipo                     | Definizione                                   | Esempio                                                                |
| :----------------------- | :-------------------------------------------- | :--------------------------------------------------------------------- |
| **Direzionale (Directed)** | Relazione con verso definito (A→B ≠ B→A)      | Richiesta di follow social, transizione outbound di fondi              |
| **Indirezionale (Undirected)** | Relazione bidirezionale mutualmente accettata | Accettazione di richiesta di amicizia (entrambi devono accettare) |

### Tre Metodi di Visualizzazione dei Grafi

La visualizzazione delle reti è cruciale per l'analisi.

| Metodo                  | Descrizione                                                               | Vantaggi                                                              | Limiti per OSINT                                                              |
| :---------------------- | :------------------------------------------------------------------------ | :-------------------------------------------------------------------- | :---------------------------------------------------------------------------- |
| **Node-Link Esplicito** | Nodi = cerchi; link = archi tra cerchi                                    | Più intuitivo, familiare, mostra chiaramente direzionalità            | Diventa illeggibile con oltre 50 nodi (effetto "hairball")                    |
| **Matriciale (Adjacency Matrix)** | Righe = nodi, Colonne = nodi; casella annerita se link esiste; intensità = peso | Compatto, scalabile a centinaia di nodi, mostra pattern di densità    | Meno intuitivo, richiede formazione per lettura rapida                       |
| **Implicito**           | Relazioni non disegnate esplicitamente ma inferite da layout automatico   | Auto-organizzato, rivela cluster senza pre-giudizio                   | Perdita del controllo diretto sull'estetica; meno riproducibile               |

## 🔍 Analisi Operativa ed Applicazioni OSINT

[[Neo4j]] è un database grafico progettato per gestire dataset enormi di relazioni, scalando sulle connessioni piuttosto che sui dati. È fondamentale per [[Attribution]] e Crypto Tracing.

### Caso Operativo: Cambridge Intelligence + Neo4j su Bitcoin

Un esempio emblematico di utilizzo di [[Neo4j]] per il Crypto Tracing è il seguente scenario:
```
DATASET: Tutte le transazioni Bitcoin (fonte: blockchain public ledger)
↓
ANALISI NEO4J: 336 transazioni su un nodo ad alto rischio (evidenziato in rosso)
↓
SCENARIO: I criminali incassano fondi (nodo blu/banca) → li spostano su varie piattaforme → cercano di nascondere i flussi (nodo orange/bitcoin)
↓
ANALISI DI RETE: Partire dalle piattaforme bancarie → mappare le reti → identificare i nodi ad alto rischio → trovare la rete di riscatto dei Bitcoin
↓
RISULTATO: Identificazione delle wallet dei criminali → attribuzione completa dei flussi illeciti
```
Questo caso dimostra il potere della [[Network analysis]] per il tracing di flussi finanziari illeciti: partendo da un singolo trigger (una transazione sospetta), [[Neo4j]] permette di:
1.  **Tracciare in avanti (forward tracing)**: da wallet sospetta → tutte le recipient wallet → identificare pattern di layering.
2.  **Tracciare indietro (backward tracing)**: da wallet di exchange → tutte le sender wallet → identificare la fonte dei fondi.
3.  **Identificare hub e intermediari**: nodi che connettono multiple reti apparentemente disgiunte.

### Criteri di Visualizzazione dei Grafi — Framework Operativo

I criteri canonici di visualizzazione dei grafi sono fondamentali per garantire la leggibilità e la correttezza analitica in qualsiasi strumento (come Cytoscape, [[Neo4j]] Bloom, Gephi, NetworkX):

| Criterio                     | Principio                                                                 | Errore Comune in OSINT                                                                  |
| :--------------------------- | :------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------- |
| **Minimizzare incroci**      | Meno intersezioni di archi = più leggibilità                              | Grafi con oltre 200 incroci diventano illeggibili per qualsiasi analista                |
| **Nodi connessi vicini**     | La distanza visuale deve riflettere la vicinanza relazionale              | Nodi di stessa rete visualizzati a oltre il 40% della canvas → falsa impressione di disconnessione |
| **Uniformità lunghezza archi** | Se tutti gli archi sono pesati allo stesso modo, la lunghezza visuale deve essere uniforme | Archi di 30px e 300px nello stesso grafo non-ponderato → misleading                     |
| **Simmetria**                | Parti strutturalmente simili del grafo devono apparire strutturalmente simili | Cluster identici visualizzati con layout diversi → analisi comparativa impossibile       |

Cytoscape è un framework open-source ampiamente adottato in [[Osint]] per:
-   Importare dataset da ACLED: mappa eventi di conflitto nel grafo (nodi = paesi/regioni; link = afflussi di rifugiati, scambi militari).
-   Integrare con Kaggle: import di dataset strutturati → generazione automatica di network.
-   Layout algoritmico: force-directed, circular, hierarchical per ottimizzare i 4 criteri canonici.

## 🔮 Lacune Informative e Prossimi Passi

Questa analisi copre gli strumenti ma non la loro integrazione operativa completa in un workflow di intelligence. Lacune identificabili includono:
1.  **Schema dati ACLED completo**: La piattaforma ACLED è menzionata, ma non è descritto il formato dei dati (JSON? CSV? API REST?). È necessaria documentazione ACLED per comprendere come acquisire e automatizzare il pull dei dati.
2.  **Linguaggio di query [[Neo4j]] (Cypher)**: [[Neo4j]] è nomiNATO come strumento, ma non sono mostrati esempi di query Cypher per il Crypto Tracing. Una query Cypher base per il tracing di transazioni a 3-hop è essenziale per l'applicazione operativa.
3.  **Strumenti di [[Dashboarding]] AI (Plotly Studio e Lovable)**: Questi strumenti sono nominati ma non descritti nei parametri di efficacia. È necessario un benchmarking su: qualità dell'output di [[Dashboarding]] AI, costo, limite di dati supportati e privacy dei dati sensibili.
4.  **Interoperabilità ACLED ↔ [[Neo4j]]**: Non è specificato come esportare eventi ACLED come database grafico. È necessario un metodo ETL specifico (ACLED CSV → Python/pandas → [[Neo4j]] import → visualizzazione).

**Prossimi passi consigliati**:
-   Documentare lo schema completo ACLED e costruire una pipeline ETL automatizzata verso [[Neo4j]].
-   Definire una libreria di query Cypher pattern per il Crypto Tracing (3-hop, 5-hop, rilevamento di cluster).
-   Effettuare un benchmarking degli strumenti di [[Dashboarding]] AI (Plotly Studio vs Lovable vs Power BI Copilot) su dataset geopolitici reali.

## 🔗 Connessioni e Pattern

- [[Applicazioni osint]]
- [[Dashboarding]]
- [[Geopolitica]]
- [[Network analysis]]
- [[Osint]]
- [[Visualizzazione dei grafi]]


- [[--]]
F/I/H
- [[--]]
