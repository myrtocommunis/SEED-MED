---
title: "Falso positivo"
tags: ["OSINT", "processed", "falso-positivo", "bias", "errore"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Falso positivo

## 🎯 Sintesi Strategica

Un **Falso Positivo (False Positive)** (Errore di Tipo I in statistica) si verifica quando un sistema analitico o un investigatore conclude erroneamente che una condizione sia presente o verificata, quando in realtà non lo è. Nell'[[Osint]] e nella [[Cyber threat intelligence]], il falso positivo è una delle cause principali di *Alert Fatigue* (stanchezza da allarme) e spreco di risorse operative, portando a indagare soggetti innocenti o a bloccare traffico di rete legittimo.

## 📚 Contesto e Definizioni

In un sistema di automazione OSINT, due entità omonime rappresentano l'incubo logico:
*   Se un analista configura un nodo di [[Scraping]] per segnalare ogni volta che "Mario Rossi" è menzioNATO in un forum del [[Dark web]], riceverà migliaia di allerte per omonimie (Falsi Positivi).
*   Il caso contrario è il **Falso Negativo (False Negative)**: l'algoritmo non riconosce la minaccia e fallisce nell'avvisare l'analista (es. il target usava il nome in codice "M. Rossi").

## 📊 Dati, Tecnologie e Metriche

Il tuning (calibrazione) dei modelli di [[Machine learning]] e degli scanner (es. [[Shodan (motore di ricerca)]]) è una perenne bilancia tra SENSibilità e Specificità. Nel dubbio operativo (specialmente in contesti antiterrorismo o di [[Sicurezza nazionale]]), le agenzie preferiscono tollerare un alto tasso di falsi positivi pur di abbattere i falsi negativi (il costo di inseguire un fantasma è minore del costo di ignorare un attentatore reale).

## 🔗 Connessioni e Pattern

- [[Analisi]]
- [[Bias cognitivo]]
- [[Machine learning]]
- [[Tecniche di analisi strutturata]]
- [[--]]
F/I/H
- [[--]]
