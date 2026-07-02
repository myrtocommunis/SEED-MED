---
title: "Sql injection"
tags: ["OSINT", "processed", "sqli", "database", "vulnerabilità", "cyber"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Sql injection

## 🎯 Sintesi Strategica

L'**SQL Injection (SQLi)** è una delle vulnerabilità informatiche più antiche, letali e persistenti del Web. Si verifica quando un'applicazione (es. un sito di e-commerce) accetta l'input dell'utente (come la barra di ricerca o la schermata di login) senza "igienizzarlo", permettendo a un hacker di inserire comandi diretti di manipolazione per il database sottostante (in linguaggio SQL). È il vettore primario responsabile della maggior parte dei colossali [[Data breach]] che alimentano l'[[Osint]] offensiva.

## 📚 Contesto e Definizioni

Immagina un form di login dove il codice backend fa: `SELECT * FROM utenti WHERE username = ' [INPUT] ' AND password = ' [INPUT] '`.
Se l'hacker inserisce come username: `admin' OR '1'='1`, il database interpreta la query come:
`SELECT * FROM utenti WHERE username = 'admin' OR '1'='1'`.
Poiché "1 è sempre uguale a 1", la condizione è matematicamente vera. Il database restituisce i dati, facendo accedere l'hacker come amministratore senza aver inserito alcuna password.

## 📊 Dati, Tecnologie e Metriche

I criminali utilizzano tool automatizzati come **SQLMap** per scansionare massivamente il [[Clear web]] alla ricerca di URL vulnerabili (es. `sito.com/page.php?id=1`). Una volta individuata la vulnerabilità, la sfruttano per scaricare silenziosamente intere tabelle contenenti carte di credito, Hash delle password e dati anagrafici, per poi rivenderle sui [[Darknet market]].

## 🔗 Connessioni e Pattern

- [[Data breach]]
- [[Darknet market]]
- [[Vulnerability assessment]]
- [[--]]
F/I/H
- [[--]]
