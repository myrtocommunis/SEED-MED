---
title: "Sottorete"
tags: ["OSINT", "processed", "subnet", "networking", "infrastruttura", "ip"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Sottorete

## 🎯 Sintesi Strategica

Una **Sottorete (Subnet)** è una suddivisione logica all'interno di una rete IP più grande. È un concetto fondamentale del Networking (Subnetting) vitale per l'[[Osint]] infrastrutturale e per la [[Cybersecurity]]. Permette agli amministratori di rete di frammentare una rete aziendale monolitica in porzioni isolate e gestibili, migliorando le prestazioni e, soprattutto, compartimentando la sicurezza per limitare i danni in caso di infiltrazione di un [[Malware]].

## 📚 Contesto e Definizioni

Senza sottoreti, se un hacker infetta il PC della segreteria con un [[Ransomware]], il virus si propaga istantaneamente a tutti i server dell'azienda in broadcast (Movimento Laterale incontrollato).
Con il subnetting e l'uso delle VLAN, l'azienda isola i dipartimenti. La Sottorete 1 (Risorse Umane) non può comunicare direttamente con la Sottorete 2 (Server R&D) senza passare attraverso un Firewall interno rigidamente configurato (Architettura Zero Trust).

## 📊 Dati, Tecnologie e Metriche

Quando un analista [[Osint]] indaga sull'infrastruttura di un server malevolo, non si limita all'[[Indirizzo ip]] singolo, ma analizza l'intera Sottorete di appartenenza (C-Class o blocco CIDR, es. `192.168.1.0/24`). Spesso, i criminali acquistano server in blocco da provider tolleranti (Bulletproof Hosting). Identificando la Sottorete malevola, il [[Blue team]] può bloccare in massa tutti e 254 gli IP del blocco, sradicando l'infrastruttura dell'attaccante.

## 🔗 Connessioni e Pattern

- [[Indirizzo ip]]
- [[Ransomware]]
- [[Blue team]]
- [[--]]
F/I/H
- [[--]]
