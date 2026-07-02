---
title: "Freenet"
tags: ["OSINT", "processed", "freenet", "darknet", "p2p", "censura"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Freenet

## 🎯 Sintesi Strategica

**Freenet** è una piattaforma Peer-to-Peer (P2P) decentralizzata e resistente alla censura, costruita per la distribuzione anonima di informazioni. Appartenente alla famiglia delle [[Darknet]] insieme a [[Tor]] e [[I2p]], Freenet adotta un approccio unico: non è una rete per "navigare" live, ma un vasto e oscuro database distribuito. Gli utenti condividono una porzione del proprio disco rigido e della propria banda per immagazzinare frammenti crittografati di dati, garantendo la persistenza delle informazioni (Freesites) contro qualsiasi tentativo di oscuramento statale.

## 📚 Contesto e Definizioni

L'architettura separa colui che richiede un file da colui che lo invia.
Freenet opera in due modalità:
1.  **Opennet:** L'utente si connette a nodi casuali globali (meno sicuro).
2.  **Darknet (Friend-to-Friend):** L'utente si connette *esclusivamente* ai nodi dei suoi contatti fisicamente fidati, creando una sottorete impenetrabile al monitoraggio esterno, usata dai dissidenti in regimi autoritari o da gruppi criminali compartimentati.

## 📊 Dati, Tecnologie e Metriche

Il paradosso legale (e il problema morale) di Freenet è che i dati sono archiviati in "chunk" crittografati sui dischi degli utenti ignari. Un utente potrebbe ospitare fisicamente sul proprio PC materiale per lo sfruttamento sessuale infantile (CSAM) o manuali terroristici senza poterlo mai sapere o visualizzare. L'analista di [[Cyber threat intelligence]] o la polizia postale fatica immensamente a condurre indagini forensi, poiché il sistema è matematicamente progettato per garantire il Non Ripudio Passivo (l'utente non sa cosa sta ospitando, quindi non è penalmente perseguibile per il semplice possesso del nodo).

## 🔗 Connessioni e Pattern

- [[Darknet]]
- [[I2p]]
- [[Tor]]
- [[Cyber threat intelligence]]
- [[--]]
F/I/H
- [[--]]
