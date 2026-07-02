---
title: "Network analysis con gephi"
tags: ["OSINT", "processed", "gephi", "sna", "grafi", "strumenti"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Network analysis con gephi

## 🎯 Sintesi Strategica

**Gephi** è un software open-source per l'analisi esplorativa e la visualizzazione di reti e sistemi complessi. Mentre database come [[Neo4j]] immagazzinano e interrogano i grafi, Gephi è il "microscopio" visivo che permette all'analista [[Osint]] di caricare fino a centinaia di migliaia di nodi (es. account Twitter, transazioni [[Bitcoin]]) e applicare algoritmi matematici di spazializzazione per rivelare a colpo d'occhio la struttura nascosta di un'organizzazione criminale o di una botnet.

## 📚 Contesto e Definizioni

Il potere di Gephi risiede nei suoi algoritmi di layout (es. Forceatlas2). Questi algoritmi simulano forze fisiche: i nodi fortemente interconnessi si attraggono magneticamente formando un ammasso denso (Clustering), mentre i nodi isolati vengono respinti verso i margini. 
Ciò permette di rilevare visivamente:
*   **Echo Chamber:** Gruppi isolati che comunicano solo tra loro.
*   **Hub:** Un individuo estremamente centrale (es. il riciclatore di denaro principale di una rete [[Finint]]).

## 📊 Dati, Tecnologie e Metriche

Nella [[Social network analysis]] applicata alla [[Disinformazione]], i ricercatori estraggono via [[Api]] 50.000 retweet su un hashtag polarizzante e li importano in Gephi. Se l'algoritmo visualizza la rete non come un fluido naturale ma come un perfetto "Falso Amplificatore" (un singolo nodo centrale che spara migliaia di tweet verso nodi periferici inattivi), l'analista ha matematicamente smascherato una [[Botnet]] automatizzata di manipolazione politica.

## 🔗 Connessioni e Pattern

- [[Social network analysis]]
- [[Neo4j]]
- [[Disinformazione]]
- [[Botnet]]
- [[--]]
F/I/H
- [[--]]
