---
title: "Raccolta"
tags: ["OSINT", "processed", "raccolta", "collection", "intelligence-cycle"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Raccolta

## 🎯 Sintesi Strategica

La **Raccolta (Collection)** è la seconda fase del [[Ciclo dell'intelligence]]. Nell'[[Osint]], rappresenta il momento di attrito tecnico con le fonti esterne: è l'estrazione empirica di informazioni dal web aperto, dai social media ([[Socmint]]), dal Deep Web o da registri commerciali. Si differenzia dalla fase di "Ricerca" perché implica l'acquisizione materiale e la conservazione del dato grezzo (Preservation) per l'analisi successiva.

## 📚 Contesto e Definizioni

L'analista deve calibrare la raccolta per evitare il rumore di fondo. Una raccolta indiscriminata riempie il [[Data lake]] di informazioni inutili.
Metodi principali:
*   **Raccolta Passiva:** Non tocca l'infrastruttura del bersaglio (es. interrogare i DNS storici su [[Ip-dns intelligence]] o usare Wayback Machine). Altissima [[Opsec]].
*   **Raccolta Attiva:** Interazione diretta (es. port scanning o interazione via [[Sock puppet]]). Rischio elevato di allertare il target.

## 📊 Dati, Tecnologie e Metriche

Il paradigma moderno delega la Raccolta all'[[Automazione]]. L'analista programma piattaforme come [[Apify]] per eseguire lo [[Scraping]] notturno, delegando ai bot il bypass dei CAPTCHA, in modo da svegliarsi e trovare il dataset pronto per la vera fase intellettuale: l'[[Analisi]].

## 🔗 Connessioni e Pattern

- [[Ciclo dell'intelligence]]
- [[Scraping]]
- [[Opsec]]
- [[--]]
F/I/H
- [[--]]
