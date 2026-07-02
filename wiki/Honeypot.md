---
title: "Honeypot"
tags: ["OSINT", "processed", "honeypot", "difesa-attiva", "cybersecurity", "deception"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Honeypot

## 🎯 Sintesi Strategica

L'**Honeypot (Barattolo di miele)** è un meccanismo di sicurezza informatica configurato intenzionalmente per rilevare, deviare o in un certo senso studiare i tentativi di utilizzo non autorizzato dei sistemi. Consiste in un computer o un server fittizio ("esca") che sembra contenere dati di grande valore (es. falsi database clienti o finte credenziali bancarie) per attirare i cybercriminali lontani dai server reali e studiarne passivamente le metodologie d'attacco.

## 📚 Contesto e Definizioni

Fa parte della strategia di **Active Defense (Difesa Attiva)** e Deception cibernetica.
Tutto il traffico diretto verso l'Honeypot è, per definizione, sospetto. Nessun utente o dipendente legittimo ha motivo di connettervisi. Pertanto, i [[Falso positivo]] sono inesistenti: se scatta l'allarme sull'Honeypot, l'azienda sa che un attacco (o una ricognizione interna da parte di un [[Insider threat]]) è certamente in corso.

## 📊 Dati, Tecnologie e Metriche

Gli specialisti di [[Cyber threat intelligence]] collegano intere "Honeynet" (reti di honeypot) sparse per il mondo e le lasciano infettare. Quando un gruppo criminale ci lancia contro un attacco [[Brute-force]] o vi inietta una variante [[Zero-day]] di uno script, l'Honeypot registra la provenienza, i comandi impartiti e gli IP, fornendo agli analisti [[Osint]] le tecniche e le procedure ([[Mitre att&ck]]) aggiornate del nemico senza dover rischiare asset reali dell'azienda.

## 🔗 Connessioni e Pattern

- [[Cyber threat intelligence]]
- [[Insider threat]]
- [[Falso positivo]]
- [[Mitre att&ck]]
- [[--]]
F/I/H
- [[--]]
