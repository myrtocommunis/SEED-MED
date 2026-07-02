---
title: "Dns"
tags: ["OSINT", "processed", "dns", "networking", "infrastruttura", "spoofing"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Dns

## 🎯 Sintesi Strategica

Il **DNS (Domain Name System)** è la "rubrica telefonica" di Internet. È il sistema gerarchico e distribuito che converte i nomi di dominio umanamente leggibili (es. `google.com`) nei rispettivi indirizzi IP numerici (es. `142.250.180.14`) necessari ai computer per comunicare. Nell'[[Osint]] infrastrutturale, i record DNS pubblici sono una fonte inestimabile per mappare passivamente l'estensione digitale di un'azienda o per svelare i server nascosti di un Threat Actor.

## 📚 Contesto e Definizioni

L'analista interroga i Name Server utilizzando tool come `dig` o DNSDumpster per estrarre:
*   **Record A / AAAA:** L'[[Indirizzo ip]] effettivo del server web.
*   **Record MX:** I server che gestiscono la posta elettronica aziendale (target per il phishing).
*   **Record TXT:** Dati testuali vari. Spesso configurati male, possono rivelare le tecnologie di sicurezza usate (es. SPF) o addirittura password dimenticate dagli amministratori di rete.

## 📊 Dati, Tecnologie e Metriche

La manipolazione di questo sistema è devastante. Nel **DNS Spoofing (o DNS Poisoning)**, l'hacker infetta il router locale o il server DNS, forzandolo ad associare l'URL `banca.it` all'IP del server dell'hacker invece che a quello reale. L'utente digiterà correttamente l'indirizzo nel browser, ma verrà dirottato in modo invisibile su un sito clone perfetto per rubargli i dati (una variante massiva del [[Man in the middle]]).

## 🔗 Connessioni e Pattern

- [[Indirizzo ip]]
- [[Spoofing]]
- [[Man in the middle]]
- [[Porta logica]]
- [[--]]
F/I/H
- [[--]]
