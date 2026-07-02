---
title: "Scraping"
tags: ["OSINT", "processed", "scraping", "html", "automazione"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "3"
tipo: "concetto"
---

# Scraping

## 🎯 Sintesi Strategica

Il **Web Scraping** è la tecnica automatizzata di estrazione di dati non strutturati (HTML) da pagine web per convertirli in formati strutturati (CSV, Database) pronti per l'analisi. Quando le [[Api]] ufficiali non esistono, sono troppo costose o vengono chiuse (come avvenuto con X/Twitter), lo scraping diviene l'unica via per la raccolta passiva [[Osint]] su larga scala.

## 📚 Contesto e Definizioni

Si divide in due approcci:
1.  **Scraping Statico:** Scarica solo il codice HTML originale (es. Beautifulsoup in Python). Veloce ma inefficace contro siti moderni.
2.  **Scraping Dinamico (Headless Browser):** Utilizza finti browser automatizzati ([[Puppeteer]], [[Selenium]]) per eseguire il Javascript della pagina, cliccare bottoni e superare protezioni base, simulando l'azione umana.

## 📊 Dati, Tecnologie e Metriche

Il [[Capitalismo delle piattaforme]] combatte ferocemente lo scraping con CAPTCHA e blocchi IP. Strumenti in cloud come [[Apify]] ovviano al problema usando reti di rotazione Proxy residenziali. L'aspetto critico è il [[Quadro giuridico]]: lo scraping di dati personali, anche se pubblici, espone l'agenzia a violazioni del [[GDPR]].

## 🔗 Connessioni e Pattern

- [[Apify]]
- [[Api]]
- [[Quadro giuridico]]
- [[--]]
F/I/H
- [[--]]
