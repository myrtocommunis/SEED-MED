---
title: "Tor"
tags: ["OSINT", "processed", "tor", "dark-web", "opsec"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "3"
tipo: "concetto"
---

# Tor

## 🎯 Sintesi Strategica

**Tor (The Onion Router)** è un software open-source e una rete overlay concepita per abilitare la comunicazione anonima. Fondamentale per il mantenimento dell'[[Opsec]] da parte dell'analista [[Osint]] o del dissidente politico, Tor impedisce a chiunque monitori la connessione di rete di sapere quali siti vengano visitati, e impedisce ai siti visitati di conoscere la posizione fisica dell'utente.

## 📚 Contesto e Definizioni

L'architettura (Onion Routing) incapsula i pacchetti dati in multipli strati di crittografia.
Il traffico non va direttamente dall'Analista al Server, ma rimbalza (Bouncing) casualmente attraverso tre nodi volontari sparsi per il mondo:
1.  **Entry Node (Guard):** Conosce l'IP dell'analista, ma non sa cosa sta leggendo.
2.  **Middle Node:** Conosce solo chi gli manda il pacchetto e a chi deve passarlo.
3.  **Exit Node:** Decritta l'ultimo strato e lo invia al Server finale. Conosce la richiesta, ma ignora assolutamente chi sia l'analista originario.

## 📊 Dati, Tecnologie e Metriche

Nell'investigazione CTI ([[Cyber]]), l'infrastruttura Tor ospita i cosiddetti *Hidden Services* (indirizzi terminanti in `.onion` non indicizzati dai motori tradizionali). Questo è il reame del [[Dark web]], dove operano i Ransomware Leak Sites, i forum di malware e i mercati illeciti, richiedendo tool di [[Scraping]] specifici capaci di operare sotto protocollo SOCKS5.

## 🔗 Connessioni e Pattern

- [[Dark web]]
- [[Opsec]]
- [[Cyber]]
- [[Vpn]]
- [[--]]
F/I/H
- [[--]]
