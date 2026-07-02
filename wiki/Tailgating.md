---
title: "Tailgating"
tags: ["OSINT", "processed", "tailgating", "sicurezza-fisica", "ingegneria-sociale", "red-team"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Tailgating

## 🎯 Sintesi Strategica

Il **Tailgating (Accodamento o Piggybacking)** è una tecnica fisica di [[Ingegneria sociale]] impiegata nelle operazioni offensive del [[Red team]] o da attori criminali. Consiste nell'aggirare i controlli di sicurezza fisica (es. porte chiuse elettronicamente, tornelli, guardie giurate) seguendo da vicino un dipendente autorizzato in un'area riservata, senza dover clonare il suo badge aziendale.

## 📚 Contesto e Definizioni

Il Tailgating puro sfrutta la cortesia umana e i condizionamenti sociali. L'attaccante si posiziona vicino alla porta d'ingresso con le mani piene di scatole pesanti o due caffè bollenti. Quando un dipendente legittimo apre la porta col badge, l'attaccante si affretta facendo finta di non avere le mani libere. Il dipendente, per educazione sociale, "terrà la porta aperta" all'intruso, compromettendo istantaneamente l'intera sicurezza dell'edificio (e rendendo la rete interna vulnerabile a un [[Keylogger]] hardware).

## 📊 Dati, Tecnologie e Metriche

Nei complessi test di penetrazione fisica, l'hacker combina l'[[Osint]] passiva al Tailgating: esamina i profili Linkedin dell'azienda per scoprire il fornitore ufficiale delle pulizie o delle pizze. Si veste con l'uniforme corretta (Pretexting) per abbassare il livello di sospetto delle guardie. La difesa architettonica a queste falle OPSEC è l'installazione di porte girevoli a singola persona (Mantrap), dove è fisicamente impossibile per due individui passare con la strisciata di un solo badge.

## 🔗 Connessioni e Pattern

- [[Ingegneria sociale]]
- [[Red team]]
- [[Keylogger]]
- [[--]]
F/I/H
- [[--]]
