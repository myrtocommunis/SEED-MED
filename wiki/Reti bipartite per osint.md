---
title: Reti bipartite per osint
tags:
- OSINT
- processed
- reti-bipartite-per-osint
date: '2026-05-15'
status: draft
depth: standard
sources: '1'
tipo: concetto
---

# Reti bipartite per osint

## 🎯 Sintesi Strategica

Le reti bipartite rappresentano uno strumento analitico fondamentale nell'ambito dell'[[Osint]] per la rilevazione di comportamenti coordinati sui social media. Esse consentono di modellare le relazioni tra due distinti insiemi di entità, come account e contenuti, facilitando l'identificazione di schemi di condivisione sincronizzata che possono indicare campagne di [[Disinformazione]], Astroturfing o la presenza di reti di bot. Attraverso la proiezione e l'analisi di comunità, è possibile isolare gruppi di attori che operano in modo coordiNATO, fornendo insight cruciali per l'analisi dell'influenza e della manipolazione informativa.

## 📚 Contesto e Definizioni

Una **rete bipartita** è un tipo di grafo in cui i nodi possono essere divisi in due insiemi disgiunti e indipendenti, con gli archi che connettono solo nodi appartenenti a insiemi diversi. Nel contesto dell'OSINT e della rilevazione di comportamenti coordinati, questi due insiemi sono tipicamente:
1.  **Account**: Gli utenti o entità che condividono contenuti.
2.  **Contenuti**: Gli elementi (es. post, link, immagini) che vengono condivisi.

Un arco esiste tra un account e un contenuto se l'account ha condiviso quel contenuto entro una specifica finestra temporale. Questo modello è cruciale per identificare il **coordinated sharing**, definito come la condivisione degli stessi contenuti da parte di più account in modo sincronizzato. La sua importanza per l'OSINT risiede nella capacità di:
*   Rilevare campagne di disinformazione e propaganda.
*   Identificare fenomeni di astroturfing e manipolazione orchestrata.
*   Scoprire reti di bot o account inautentici che operano in concerto.

## 📊 Dati, Tecnologie e Metriche

L'analisi delle reti bipartite per l'OSINT si avvale di strumenti specifici e di una pipeline analitica strutturata:

*   **Coortweet**: Un pacchetto R progettato per la rilevazione di contenuti coordinati, agnostico rispetto alla piattaforma. Il suo principio di funzionamento si basa sull'identificazione di contenuti condivisi da più account, il calcolo di finestre temporali di condivisione e la creazione di una rete di co-sharing.
    *   **Installazione**: `devtools::install_github("nicolarighetti/coortweet")`
*   **Cuore Operativo**: La creazione di una rete bipartita Account-Contenuto.
*   **Proiezione su Account**: Dalla rete bipartita, si genera una proiezione che connette due utenti se condividono lo stesso contenuto. Il peso dell'arco tra due account rappresenta il numero di contenuti condivisi in comune.
    *   Esempio: `proj <- bipartite.projection(g_bipartite); g_accounts <- proj$proj1`
*   **Filtraggio Statistico**: L'algoritmo `detect_coordinated_sharing` permette di impostare parametri come `time_window` (finestra temporale in minuti), `min_repetition` (minimo di condivisioni per considerazione) e `percentile_edge` (soglia oltre la quale la co-condivisione è considerata anomala).
*   **Community Detection**: Algoritmi come il [[Clustering]] vengono applicati alla rete di co-sharing per identificare cluster di account. Ogni cluster rappresenta un gruppo di account che condividono gli stessi contenuti, nella stessa finestra temporale, con una frequenza anomala.
    *   Esempio: `communities <- cluster_louvain(g_cosharing)`
*   **Visualizzazione**: Strumenti come `ggraph` permettono di visualizzare la rete, dove il colore dei nodi può indicare il cluster di appartenenza e lo spessore degli archi l'intensità del co-sharing.
*   **Coortweetpost**: Un pacchetto complementare per il post-processing, che offre analisi temporali dei cluster, estrazione di contenuti, metriche avanzate e report automatici.
    *   Installazione: `devtools::install_github("massimo-terenzi/Coortweetpost")`

## 🔍 Analisi Operativa ed Applicazioni OSINT

L'applicazione delle reti bipartite nell'OSINT si traduce in una metodologia robusta per l'identificazione e l'analisi di fenomeni di influenza e manipolazione. La pipeline completa prevede:
1.  **Costruzione della Rete Bipartita**: Account ↔ Contenuti.
2.  **Proiezione**: Trasformazione in una rete Account ↔ Account.
3.  **Pesatura degli Archi**: Quantificazione delle co-condivisioni.
4.  **Community Detection**: Identificazione di gruppi coordinati.

Questa metodologia consente agli analisti OSINT di:
*   **Identificare attori coordinati**: Scoprire chi sono gli account che agiscono in concerto.
*   **Analizzare i contenuti**: Comprendere quali messaggi o narrazioni vengono amplificati.
*   **Rilevare pattern temporali**: Individuare finestre di attività sospette.

Una checklist analitica per l'OSINT include:
*   Chi sono gli account all'interno di un cluster?
*   Quali contenuti specifici condividono?
*   Esiste un pattern temporale sospetto nelle loro attività di condivisione?

## 🔮 Lacune Informative e Prossimi Passi

È fondamentale riconoscere che il coordinamento rilevato tramite reti bipartite non implica automaticamente manipolazione o attività malevola. Esistono spiegazioni alternative che devono essere considerate nell'analisi OSINT:
*   Utenti che seguono le stesse fonti di informazione.
*   Eventi di cronaca o notizie che generano condivisioni simultanee e organiche.
*   Comunità organiche con interessi e comportamenti di condivisione naturalmente allineati.

Pertanto, la rilevazione di un cluster coordiNATO è un punto di partenza per ulteriori indagini qualitative e contestuali. I prossimi passi includono l'integrazione di analisi semantiche dei contenuti, l'esame dei metadati degli account e l'incrocio con altre fonti di intelligence per validare le ipotesi di manipolazione. La sfida futura risiede nel distinguere con maggiore precisione il coordinamento organico da quello inautentico.

## 🔗 Connessioni e Pattern

- [[Applicazioni osint]]
- [[Community detection]]
- [[Disinformazione]]
- [[Manipolazione informativa]]
- [[Osint]]
- [[Reti bipartite]]


- [[--]]
F/I/H
- [[--]]
