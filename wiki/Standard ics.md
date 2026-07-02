---
title: "Standard ics"
tags: ["OSINT", "processed", "ics", "standard", "scada", "cybersecurity", "resilienza"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Standard ics

## 🎯 Sintesi Strategica

Gli **Standard ICS (Industrial Control Systems) / SCADA** rappresentano i protocolli di sicurezza e architettura informatica per le infrastrutture industriali critiche (es. centrali nucleari, dighe idroelettriche, oleodotti). A differenza dei sistemi IT aziendali (dove se si blocca la rete, nessuno muore), nei sistemi ICS una violazione da parte di un [[Malware]] produce un Impatto Cinetico immediato, fondendo turbine o contaminando le acque pubbliche, rendendoli il bersaglio primario della [[Guerra cibernetica]].

## 📚 Contesto e Definizioni

La principale divergenza tra IT classico e ICS è la priorità difensiva (Triade CIA rovesciata):
*   Nell'IT, la **Confidenzialità** è sacra (impedire il furto di database).
*   Nell'ICS, la **Disponibilità** e l'**Integrità** sono assolute. Un reattore nucleare non può "riavviarsi per installare gli aggiornamenti" e un comando di raffreddamento inviato dai sensori non deve mai arrivare in ritardo (Latenza), altrimenti l'impianto esplode.

## 📊 Dati, Tecnologie e Metriche

Gli standard di sicurezza (es. IEC 62443 o NIST 800-82) impongono l'isolamento fisico totale (Air-Gap) per i sistemi di controllo, vietando il collegamento a Internet. Tuttavia, indagini [[Osint]] condotte su motori di ricerca come [[Shodan (motore di ricerca)]] rivelano regolarmente centinaia di migliaia di PLC (Programmable Logic Controllers) esposti al web per "comodità" manutentiva degli operatori, creando colossali [[Gap strutturali]]. Gruppi [[Apt]] statali scansionano queste falle 24/7 per installare payload dormienti a scopo di sabotaggio geostrategico.

## 🔗 Connessioni e Pattern

- [[Guerra cibernetica]]
- [[Shodan (motore di ricerca)]]
- [[Gap strutturali]]
- [[Apt]]
- [[--]]
F/I/H
- [[--]]
