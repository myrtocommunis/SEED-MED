---
title: "Cross-site scripting"
tags: ["OSINT", "processed", "xss", "vulnerabilità", "web", "phishing"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Cross-site scripting

## 🎯 Sintesi Strategica

Il **Cross-Site Scripting (XSS)** è una vulnerabilità web critica in cui un attaccante riesce a iniettare codice maligno (solitamente Javascript) all'interno di una pagina web legittima visualizzata da altri utenti. A differenza dell'[[Sql injection]], che attacca e compromette il Database dell'azienda sul server (Backend), l'XSS colpisce direttamente il Browser dell'utente finale (Frontend), sfruttando la fiducia che l'utente ripone nel sito che sta visitando.

## 📚 Contesto e Definizioni

Si divide in tre categorie principali:
1.  **Stored XSS (Persistente):** Il peggiore. L'hacker scrive un commento in un forum o in un post di un social media contenente uno script invisibile. Il server salva il commento. Chiunque visiti quella pagina eseguirà inavvertitamente il virus sul proprio browser.
2.  **Reflected XSS:** Il codice maligno viene inserito in un link contraffatto (es. via [[Attacco di phishing]]). Quando l'utente clicca il link apparentemente legittimo, il server riflette lo script sul browser della vittima.
3.  **DOM-based XSS:** La vulnerabilità risiede interamente nel codice Javascript del browser, senza mai toccare il server.

## 📊 Dati, Tecnologie e Metriche

L'obiettivo primario di un attacco XSS è il furto dei **Cookie di Sessione**. Rubando il cookie tramite lo script invisibile, l'hacker clona l'identità digitale della vittima (Session Hijacking), accedendo alla sua casella email o al suo conto bancario eludendo l'Autenticazione a Due Fattori (2FA), poiché il server bancario ritiene che il browser in uso sia quello precedentemente autorizzato.

## 🔗 Connessioni e Pattern

- [[Attacco di phishing]]
- [[Sql injection]]
- [[Vulnerability assessment]]
- [[--]]
F/I/H
- [[--]]
