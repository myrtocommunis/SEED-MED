---
title: "Tecnologie"
tags: ["OSINT", "processed", "tecnologie", "stack", "infrastruttura"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Tecnologie

## 🎯 Sintesi Strategica

Il termine **Tecnologie** nel contesto investigativo ([[Osint]] o Penetration Testing) non si riferisce in modo generico all'informatica, ma al cosiddetto **Tech Stack**, ovvero l'infrastruttura software sottostante che alimenta un'organizzazione o un dominio bersaglio. Identificare tempestivamente le Tecnologie utilizzate dal nemico è la fase cruciale del processo di Ricognizione della [[Cyber kill chain]].

## 📚 Contesto e Definizioni

Invece di lanciare attacchi alla cieca, un hacker intelligente o un analista mappa il terreno. Utilizzando estensioni browser passive (come Wappalyzer o Builtwith) o motori come [[Shodan (motore di ricerca)]], esamina gli header HTTP del sito aziendale per estrarne il DNA:
*   "Il sito usa Wordpress versione 5.2" (CMS).
*   "Il backend è in PHP 7.4" (Linguaggio obsoleto).
*   "Il database è esposto su MySQL" ([[Sql injection]]).
*   "Utilizzano Cloudflare come WAF" (Difesa da bypassare).

## 📊 Dati, Tecnologie e Metriche

Conoscere lo Stack Tecnologico azzera i tempi morti. Se l'analista sa che il bersaglio utilizza esclusivamente infrastruttura Microsoft IIS, non perderà tempo a testare exploit Linux o script per Apache. Inoltre, nella [[Cyber threat intelligence]], il monitoraggio delle Tecnologie è vitale per l'Attack Surface Management: se esce una grave vulnerabilità ([[Zero-day]]) su "Log4j", il team di sicurezza interroga immediatamente il proprio inventario delle Tecnologie per sapere se e dove l'azienda lo utilizza, chiudendo la falla in minuti.

## 🔗 Connessioni e Pattern

- [[Cyber kill chain]]
- [[Shodan (motore di ricerca)]]
- [[Zero-day]]
- [[Vulnerability assessment]]
- [[--]]
F/I/H
- [[--]]
