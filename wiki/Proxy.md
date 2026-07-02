---
title: "Proxy"
tags: ["OSINT", "processed", "proxy", "networking", "opsec", "scraping"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Proxy

## 🎯 Sintesi Strategica

Un **Server Proxy** è un intermediario di rete che funge da ponte tra il computer dell'utente (Client) e il resto di Internet. Invece di connettersi direttamente al sito bersaglio, l'utente si connette al Proxy, che effettua la richiesta per conto suo e gli restituisce i dati. Nell'[[Osint]] e nell'esecuzione dello [[Scraping]] massivo, i proxy sono fondamentali per aggirare i ban degli indirizzi IP, per bypassare i filtri geografici e per proteggere (in parte) l'[[Opsec]] oscurando la reale origine della richiesta.

## 📚 Contesto e Definizioni

Esistono diverse architetture e livelli di anonimato:
1.  **Datacenter Proxy:** IP forniti da server cloud (es. AWS, Digitalocean). Sono economici e veloci, ma i sistemi di sicurezza li riconoscono e li bloccano istantaneamente perché sanno che provengono da un server e non da un utente reale.
2.  **Residential Proxy:** Indirizzi IP legati a normali connessioni domestiche (forniti dagli ISP locali come Tim o Vodafone). Molto costosi, sono vitali per operazioni di [[Socmint]] furtive, poiché la piattaforma bersaglio vede la richiesta come proveniente da un normale "computer casalingo", diminuendo le probabilità di bloccare il [[Sock puppet]].

## 📊 Dati, Tecnologie e Metriche

A differenza di una [[Vpn]] (che cifra l'intero traffico di sistema), un Proxy solitamente instrada solo il traffico di una singola applicazione (es. il Browser) e spesso non utilizza crittografia. Questo significa che l'ISP dell'utente o un attore ostile in mezzo alla rete (tramite [[Wireshark]]) può intercettare il contenuto non sicuro. Per l'automazione, strumenti come [[Apify]] gestiscono pool rotanti di proxy per evitare che un singolo IP faccia troppe richieste e venga banNATO.

## 🔗 Connessioni e Pattern

- [[Scraping]]
- [[Opsec]]
- [[Vpn]]
- [[Socmint]]
- [[--]]
F/I/H
- [[--]]
