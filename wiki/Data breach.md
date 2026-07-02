---
title: "Data breach"
tags: ["OSINT", "processed", "data-breach", "leak", "privacy", "cybercrime"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Data breach

## 🎯 Sintesi Strategica

Un **Data Breach (Violazione dei Dati)** è un incidente di sicurezza, intenzionale o accidentale, in cui informazioni confidenziali, protette o sensibili vengono copiate, trasmesse, visualizzate, rubate o utilizzate da una persona o un'entità non autorizzata. Nell'ecosistema investigativo, i database frutto di Data Breach (i *Leak*) rappresentano una delle fonti [[Osint]] più controverse, grigie e infinitamente preziose per de-anonimizzare i Threat Actor e risolvere i casi.

## 📚 Contesto e Definizioni

La violazione può avvenire per mano di un hacker esterno ([[Apt]]), di un [[Insider threat]] o a causa di un [[Vulnerability assessment]] fallito (es. un database [[Elasticsearch]] lasciato senza password).
I dati sottratti (comprendenti email, password in chiaro o hash, indirizzi fisici, numeri di carta di credito) vengono solitamente rivenduti sui forum del [[Dark web]] o pubblicati gratuitamente su canali Telegram per distruggere la reputazione dell'azienda vittima.

## 📊 Dati, Tecnologie e Metriche

L'analista di [[Cyber threat intelligence]] usa i Data Breach in modo retroattivo. Se un hacker criminale utilizza l'email anonima `hacker99@proton.me` per registrare il suo server di [[Command and control]], l'analista cerca quell'email in vecchi database rubati (es. il database leakato di un forum di videogiochi del 2012). Se la trova associata a un vecchio IP, al vero nome dell'utente o a una vecchia password, può sfruttare queste briciole per ricostruire la vera identità del criminale.

## 🔗 Connessioni e Pattern

- [[Dark web]]
- [[Insider threat]]
- [[Cyber threat intelligence]]
- [[Quadro giuridico]]
- [[--]]
F/I/H
- [[--]]
