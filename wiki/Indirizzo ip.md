---
title: "Indirizzo ip"
tags: ["OSINT", "processed", "ip", "networking", "tracciamento", "privacy"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Indirizzo ip

## 🎯 Sintesi Strategica

L'**Indirizzo IP (Internet Protocol Address)** è l'identificativo numerico logico assegNATO in modo univoco a ciascun dispositivo connesso a una rete informatica (che usi lo standard IP). Nella cyber-investigazione e nell'[[Osint]], l'IP è il "Codice Fiscale" transitorio di un nodo sulla rete. Consente di geolocalizzare la connessione ([[Geoint]]), identificare il provider internet (ISP) responsabile e tracciare le attività criminali a livello internazionale.

## 📚 Contesto e Definizioni

Esistono due versioni principali:
*   **IPv4:** (es. `192.168.1.1`), composto da 32 bit, attualmente in via di esaurimento globale.
*   **IPv6:** Il nuovo standard, composto da 128 bit, che garantisce un numero di indirizzi virtualmente infinito.
Gli IP si dividono in Pubblici (esposti e visibili sull'Internet globale) e Privati (usati solo all'interno della rete di casa o della [[Sottorete]] aziendale).

## 📊 Dati, Tecnologie e Metriche

A causa della scarsità degli IPv4, i provider usano il **NAT (Network Address Translation)**: un intero palazzo o quartiere potrebbe affacciarsi su internet usando un singolo IP pubblico condiviso. Di conseguenza, conoscere solo l'IP del criminale in tribunale oggi non è più sufficiente per un arresto in garanzia; l'indirizzo IP deve essere sempre incrociato temporalmente con l'assegnazione dei log DHCP del provider (richiedendo la precisa coordinazione del [[Quadro giuridico]]) e con l'analisi dei [[Metadati]].

## 🔗 Connessioni e Pattern

- [[Dns]]
- [[Sottorete]]
- [[Mac address]]
- [[Geoint]]
- [[--]]
F/I/H
- [[--]]
