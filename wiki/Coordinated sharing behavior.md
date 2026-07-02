---
title: "Coordinated sharing behavior"
tags: ["OSINT", "processed", "cib", "disinformazione", "sna", "botnet"]
date: "2026-05-15"
status: "draft"
depth: "deep"
sources: "4"
tipo: "concetto"
---

# Coordinated sharing behavior

## 🎯 Sintesi Strategica

Il **Coordinated Sharing Behavior (CSB)**, spesso sovrapposto alla sigla CIB (*Coordinated Inauthentic Behavior* di meta-iana memoria), indica l'azione sincronizzata e strutturata di reti di account che amplificano artificialmente lo stesso contenuto entro finestre temporali anomale. In ambito [[Osint]], l'individuazione del comportamento coordiNATO è l'arma analitica principale per smascherare le operazioni di [[Disinformazione]] (FIMI). Il CSB sposta l'analisi dal *contenuto* (che potrebbe essere vero o ingannevole) all'esame matematico del *comportamento*, dimostrando l'esistenza di un'orchestrazione malevola sottostante (Troll Farms, Botnets, Sock Puppets gestiti da un unico attore).

## 📚 Contesto e Definizioni

La differenza critica per l'intelligence è quella tra Viralità Organica e Sincronizzazione Artificiale:
*   **Viralità Organica:** Un video scoppia su Tiktok, viene rilanciato a ondate successive da persone normali, con reazioni sparse nel corso di ore o giorni.
*   **Sincronizzazione (CSB):** 500 account pubblicano *esattamente lo stesso URL* con *esattamente la stessa didascalia* entro un lasso di tempo di 60 secondi (Spikes temporali).

È fondamentale l'assunto di cautela: **Coordinamento NON equivale automaticamente a Inautenticità**. Tifoserie o gruppi attivisti reali (autentici) possono coordinarsi su Telegram per spammare un hashtag (es. *K-Pop fans*).

## 📊 Dati, Tecnologie e Metriche

La detection del CSB richiede la modellazione dei dati tramite **[[Reti bipartite]]**:
1.  Si estrae l'elenco degli Account (Nodo A) e dei Link/Hashtag condivisi (Nodo B).
2.  Si "proietta" la rete convertendola in monopartita (Account-Account): due account sono collegati solo se hanno condiviso lo stesso link entro una strettissima finestra temporale (es. `time_window < 1 minuto`).
3.  L'applicazione di algoritmi di *Community Detection* (come il Louvain) sulla [[Social network analysis]] fa emergere graficamente l'isola densa degli account coordinati.

## 🔍 Analisi Operativa ed Applicazioni OSINT

L'utilizzo di pacchetti d'analisi (come il tool accademico in R `coortweet`) trasforma enormi JSON scaricati via API in prove inconfutabili:
*   **Identificazione del Command & Control:** Una volta isolato il cluster coordiNATO, l'analista OSINT esamina il nodo centrale (*Patient Zero*). Spesso le Troll Farm russe usano bot automatizzati per rilanciare immediatamente i tweet pubblicati da un singolo account "Master" gestito da un operatore umano ([[Sock puppet]] ad alto valore).
*   **Automazione e Pattern Matching:** Attraverso piattaforme di [[Automazione]] è possibile monitorare feed [[RSS]] o canali Telegram e lanciare alert automatici quando il volume di condivisione di un link supera la deviazione standard statistica.

## 🔮 Lacune Informative e Prossimi Passi

*   **Normalizzazione e False Positivity:** Gli account dei VIP o delle testate giornalistiche massicce, avendo milioni di follower e bot aggregatori che li rilanciano automaticamente, rischiano di generare continui "Falsi Positivi" algoritmici. I modelli devono essere addestrati a normalizzare in base al numero di follower del nodo sorgente.
*   **Cross-Platform Coordination:** La ricerca accademica e OSINT attuale è debole nell'individuare il coordinamento che avviene "a cavallo" tra piattaforme (es. ordine impartito su Telegram, video caricato su Tiktok, amplificazione eseguita su X/Twitter).

## 🔗 Connessioni e Pattern

- [[Reti bipartite]]
- [[Social network analysis]]
- [[Disinformazione]]
- [[Automazione]]
- [[Algoritmi]]

- [[--]]
F/I/H
- [[--]]
