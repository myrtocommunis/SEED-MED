---
title: "Persona"
tags: ["OSINT", "processed", "persona", "opsec", "sock-puppet", "copertura"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Persona

## 🎯 Sintesi Strategica

Nell'ambito dell'[[Osint]] e della sicurezza operativa ([[Opsec]]), la **Persona (o Sock Puppet / Profilo d'Ombra)** è un'identità digitale fittizia, meticolosamente ingegnerizzata dall'analista per infiltrarsi in gruppi chiusi (es. forum terroristici, canali Telegram di estrema destra, Dark Web) o per effettuare raschiamento dati ([[Scraping]]) senza rivelare l'identità dell'agenzia o dell'azienda investigatrice al bersaglio. Una Persona non è un semplice "account falso", ma un'infrastruttura operativa complessa.

## 📚 Contesto e Definizioni

Creare una Persona richiede una separazione tecnica e psicologica assoluta (Compartimentazione):
*   **Hardware/Network:** La Persona non usa mai il Wifi o il PC reale dell'analista. Si affida a macchine virtuali (VM), VPN dedicate o connessioni Tor separate per ogni singola identità.
*   **Legend (La Leggenda):** Un background coerente. Se la Persona finge di essere un programmatore russo di 40 anni (per infiltrare un gruppo [[Ransomware]]), deve avere account Github storici credibili, usare slang locale e operare solo nel fuso orario di Mosca.

## 📊 Dati, Tecnologie e Metriche

Il fallimento nella gestione di una Persona porta al de-anonimato dell'analista (Burned Persona), con rischi fisici o ritorsioni cibernetiche (Doxing) da parte dei gruppi criminali ([[Apt]]). L'errore più fatale è l'Inquinamento Incrociato (Cross-Contamination): accedere a due profili d'ombra diversi dalla stessa finestra del browser, permettendo ai tracker (cookies) di collegarli, svelando l'intera rete di infiltrazione dell'agenzia di intelligence.

## 🔗 Connessioni e Pattern

- [[Opsec]]
- [[Apt]]
- [[Scraping]]
- [[Dark web]]
- [[--]]
F/I/H
- [[--]]
