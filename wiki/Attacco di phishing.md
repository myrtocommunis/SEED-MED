---
title: "Attacco di phishing"
tags: ["OSINT", "processed", "phishing", "cyber", "social-engineering"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Attacco di phishing

## 🎯 Sintesi Strategica

L'**Attacco di Phishing** è l'implementazione tecnica e digitale più diffusa dell'[[Ingegneria sociale]]. Consiste nell'invio di comunicazioni fraudolente (tipicamente email, ma anche SMS - *Smishing* - o chiamate vocali - *Vishing*) progettate per apparire come provenienti da una fonte attendibile e legittima (es. banche, istituzioni, colleghi). L'obiettivo finale è l'installazione di malware (es. l'innesco di una catena [[Apt]]) o l'esfiltrazione diretta di credenziali sensibili.

## 📚 Contesto e Definizioni

Si divide in tre livelli di sofisticazione:
1.  **Phishing di Massa (Spray and Pray):** Invio di milioni di email generiche ("Il tuo pacco è bloccato") sperando nella legge dei grandi numeri.
2.  **Spear Phishing:** Attacco altamente mirato contro un individuo o un'azienda specifica, il cui contenuto è costruito sartorialmente su dati estratti tramite [[Osint]] (es. menzionando il vero capo progetto della vittima).
3.  **Whaling:** Spear Phishing mirato ai "Pesci grossi" (CEO, Ministri, decisori), il cui account compromesso garantisce l'accesso totale (God-mode) all'infrastruttura del bersaglio.

## 📊 Dati, Tecnologie e Metriche

L'identificazione forense di campagne di Phishing rientra nella [[Cyber threat intelligence]]. L'analista utilizza l'[[Ip-dns intelligence]] per tracciare i domini "Look-alike" (Typosquatting, es. `micros0ft.com`), esamina gli Header delle email ([[E-mail forensics]]) per validare DKIM/SPF e sfrutta gli archivi pDNS per de-anonimizzare l'infrastruttura d'hosting del criminale prima che questa venga dismessa (Burned).

## 🔗 Connessioni e Pattern

- [[Ingegneria sociale]]
- [[Cyber threat intelligence]]
- [[Apt]]
- [[--]]
F/I/H
- [[--]]
