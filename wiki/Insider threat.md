---
title: "Insider threat"
tags: ["OSINT", "processed", "insider-threat", "cyber", "opsec", "sicurezza"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Insider threat

## 🎯 Sintesi Strategica

L'**Insider Threat (Minaccia Interna)** è il rischio di compromissione alla [[Sicurezza nazionale]] o aziendale causato da una persona che possiede un accesso legittimo e autorizzato all'infrastruttura (dipendenti, ex-dipendenti, appaltatori, partner commerciali). È l'incubo di qualsiasi CISO (Chief Information Security Officer): nessun firewall al mondo può fermare un ingegnere di rete con privilegi di amministrazione (Domain Admin) che decide di estrarre e vendere i brevetti dell'azienda sul [[Dark web]].

## 📚 Contesto e Definizioni

Si suddivide in tre macro-tipologie psicologiche e operative:
1.  **L'Insider Malevolo (Sabotatore/Spia):** Agisce intenzionalmente per profitto (vendendo accessi VPN ai gruppi [[Ransomware]]), per vendetta (un dipendente licenziato) o per motivi ideologici ([[Whistleblower]]).
2.  **L'Insider Negligente:** Causa violazioni di sicurezza ignorando le policy aziendali (es. salvando password su post-it o disabilitando l'antivirus per comodità).
3.  **L'Insider Compromesso:** Il dipendente ignaro che cade vittima di un [[Attacco di phishing]] o di [[Ingegneria sociale]], consegnando involontariamente le chiavi dell'azienda agli hacker.

## 📊 Dati, Tecnologie e Metriche

Il contrasto si basa sul modello **Zero Trust** (Non fidarsi di nessuno) e sulla compartimentazione (Principio del Minimo Privilegio). Le piattaforme SOC utilizzano l'analisi comportamentale (UEBA - User and Entity Behavior Analytics) per rilevare anomalie logiche: se un dipendente delle risorse umane cerca improvvisamente di scaricare 10 GB di codice sorgente dal server R&D alle 3 del mattino, il sistema genera un avviso immediato.

## 🔗 Connessioni e Pattern

- [[Ingegneria sociale]]
- [[Sicurezza nazionale]]
- [[Whistleblower]]
- [[Attacco di phishing]]
- [[--]]
F/I/H
- [[--]]
