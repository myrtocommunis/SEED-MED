---
title: "Ricerca avanzata"
tags: ["OSINT", "processed", "ricerca", "dorking", "query", "metodologia"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Ricerca avanzata

## 🎯 Sintesi Strategica

La **Ricerca Avanzata** è l'insieme di tecniche sintattiche che trasforma l'uso passivo di un database o di un motore di ricerca in uno strumento d'estrazione attivo. Applicata all'[[Osint]], supera la semplice digitazione di parole chiave, impiegando operatori logici (Booleani) per isolare informazioni specifiche all'interno di moli oceaniche di dati (Big Data). È la competenza tecnica base che precede l'utilizzo di qualsiasi tool automatizzato.

## 📚 Contesto e Definizioni

Si basa su regole matematiche di teoria degli insiemi (Logica Booleana):
*   **AND:** (Intersezione). Trova documenti che contengono *entrambe* le parole (es. "Terrorismo" AND "Bitcoin"). Riduce il rumore.
*   **OR:** (Unione). Trova documenti con *almeno una* delle parole (es. "Al-Qaeda" OR "ISIS"). Utile per alias e sinonimi.
*   **NOT (-):** (Esclusione). Rimuove categoricamente i falsi positivi (es. "Apple -fruit", per trovare l'azienda e non il frutto).

Su Google, questa logica si espande nei [[Google dorks]] (uso di `site:`, `filetype:`).

## 📊 Dati, Tecnologie e Metriche

Senza padronanza della Ricerca Avanzata, l'analista è vittima degli [[Algoritmi]] commerciali, che mostrano risultati basati sulla popolarità (SEO) anziché sulla pertinenza investigativa. Usare operatori di prossimità (es. AROUND(3) su Google, per trovare parole distanti massimo 3 termini l'una dall'altra) permette agli investigatori della [[Finint]] di collegare il nome di un CEO alla parola "Bancarotta" in un database di 10.000 pagine giudiziarie, scovando la frode in secondi.

## 🔗 Connessioni e Pattern

- [[Google dorks]]
- [[Finint]]
- [[Algoritmi]]
- [[--]]
F/I/H
- [[--]]
