---
title: "I2p"
tags: ["OSINT", "processed", "i2p", "darknet", "opsec", "anonimato"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "3"
tipo: "concetto"
---

# I2p

## 🎯 Sintesi Strategica

**I2P (Invisible Internet Project)** è una rete overlay parzialmente centralizzata e anonima (una vera e propria [[Darknet]]) progettata per la comunicazione sicura e resistente alla censura. Mentre [[Tor]] è [[NATO]] per consentire agli utenti di navigare sul [[Clear web]] in modo anonimo tramite nodi di uscita (Exit Nodes), I2P è architettato esclusivamente come "rete interna chiusa": ottimizzato per ospitare servizi nascosti (Eepsites) e favorire lo scambio Peer-to-Peer all'interno del suo ecosistema buio.

## 📚 Contesto e Definizioni

I2P utilizza un routing a "Tunnel di aglio" (Garlic Routing), un'evoluzione concettuale dell'Onion Routing di Tor. Nel Garlic Routing, molteplici messaggi vengono crittografati insieme in un singolo pacchetto (come gli spicchi in un bulbo d'aglio), rendendo l'analisi temporale e statistica del traffico (Traffic Analysis) esponenzialmente più difficile per un'agenzia di [[Sigint]] che monitora i nodi di rete.

## 📊 Dati, Tecnologie e Metriche

Nel panorama della [[Cyber threat intelligence]], I2P è considerato il "Rifugio di grado militare" per il cybercrimine avanzato. Quando i [[Darknet market]] su Tor vengono regolarmente smantellati dall'[[Europol]], i Threat Actor trasferiscono i mercati e i server di [[Command and control]] su I2P. L'infiltrazione [[Osint]] è difficilissima: non ci sono proxy pubblici comodi per sbirciare in I2P, forzando l'analista a installare l'infrastruttura client locale e mantenere un'[[Opsec]] perfetta per stabilire una connessione ai siti `.i2p`.

## 🔗 Connessioni e Pattern

- [[Darknet]]
- [[Tor]]
- [[Darknet market]]
- [[Sigint]]
- [[--]]
F/I/H
- [[--]]
