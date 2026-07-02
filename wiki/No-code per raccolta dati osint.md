---
title: "No-code per raccolta dati osint"
tags: ["OSINT", "processed", "no-code", "automazione", "scraping", "strumenti"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# No-code per raccolta dati osint

## 🎯 Sintesi Strategica

Il **No-Code per Raccolta Dati OSINT** è un approccio tecnologico che permette ad analisti investigativi, privi di competenze di programmazione (Python/Javascript), di costruire complesse architetture di estrazione dati e [[Automazione]] visiva. Attraverso interfacce "D[[RAG]] and Drop", è possibile orchestrare flussi di lavoro ([[Etl]]) che raschiano pagine web, interrogano API e riversano i risultati in database strutturati in modo completamente automatizzato.

## 📚 Contesto e Definizioni

Tradizionalmente, l'estrazione di dati dai social media o dal [[Deep web]] richiedeva la scrittura di script personalizzati. Oggi, piattaforme No-Code come [[Make]], [[n8n]] (più orientato alla privacy) o [[Apify]] permettono di costruire pipeline di intelligence visive:
1.  **Trigger:** Ogni volta che un nuovo articolo menziona la parola "Ransomware" su un [[Feed rss]].
2.  **Action 1:** Estrai il testo dell'articolo via Web Scraper.
3.  **Action 2:** Invia il testo a un modello [[Llm]] (es. ChatGPT) per estrarre tutti gli [[Indirizzo ip]] e gli Hash presenti.
4.  **Action 3:** Salva i dati strutturati nel database Airtable del team.

## 📊 Dati, Tecnologie e Metriche

L'uso delle piattaforme No-Code abbassa drasticamente il "Time to Value" dell'indagine. Tuttavia, presenta criticità in ambito [[Opsec]]: utilizzare un servizio cloud commerciale come Zapier per processare flussi di dati sensibili su target terroristici significa condividere l'intera indagine con un fornitore terzo. Le unità di intelligence governative adottano soluzioni No-Code Open Source (come n8n) installate su server sicuri e Air-Gapped.

## 🔗 Connessioni e Pattern

- [[Automazione]]
- [[Scraping]]
- [[Etl]]
- [[n8n]]
- [[--]]
F/I/H
- [[--]]
