---
title: "Sitemap xml"
tags: ["OSINT", "processed", "sitemap", "web-scraping", "ricognizione", "seo"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Sitemap xml

## 🎯 Sintesi Strategica

Il file **Sitemap.xml (Mappa del Sito)** è un file strutturato inserito dai webmaster nella directory principale di un sito web (es. `sito.com/sitemap.xml`) per indicare esplicitamente ai [[Motori di ricerca]] (come Googlebot) l'architettura completa del sito, elencando tutti gli URL che dovrebbero essere indicizzati. Nell'[[Osint]] e nella Ricognizione cibernetica, è una vera e propria mappa del tesoro regalata volontariamente dal bersaglio all'analista.

## 📚 Contesto e Definizioni

Mentre il file `robots.txt` dice ai motori di ricerca "Non guardare qui", la Sitemap dice "Guarda esattamente qui, ecco la planimetria completa".
L'analista [[Osint]] non perde tempo a cliccare manualmente i link sul sito aziendale: scarica l'intera Sitemap XML e la parsifica con uno script di [[Automazione]]. Questo rivela in millisecondi la presenza di migliaia di pagine, incluse quelle "nascoste" o non linkate nell'homepage (es. URL di vecchie promozioni, portali di login per dipendenti `sito.com/admin/login-2022`, o PDF riservati).

## 📊 Dati, Tecnologie e Metriche

Dal punto di vista dell'[[Opsec]] aziendale, una Sitemap configurata male è un vettore di [[Data breach]] accidentale (Data Exposure). Se il CMS aziendale genera automaticamente la sitemap e vi inserisce per errore la cartella dei backup (es. `/database_dump.sql`), un ricercatore (o un criminale) la troverà istantaneamente leggendo l'XML, scavalcando qualsiasi necessità di attacco tecnico.

## 🔗 Connessioni e Pattern

- [[Motori di ricerca]]
- [[Raccolta]]
- [[Automazione]]
- [[Data breach]]
- [[--]]
F/I/H
- [[--]]
