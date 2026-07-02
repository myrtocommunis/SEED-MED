---
title: "Wireshark"
tags: ["OSINT", "processed", "wireshark", "sniffing", "pcap", "network-intelligence"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Wireshark

## 🎯 Sintesi Strategica

**Wireshark** è l'analizzatore di protocolli di rete (Packet Sniffer) definitivo. Permette di intercettare, catturare e ispezionare visivamente il traffico dati in tempo reale a livello microscopico (pacchetto per pacchetto) che transita su un'interfaccia di rete. Strumento vitale per la Network Forensics e la [[Cyber threat intelligence]], consente agli analisti di dissezionare le comunicazioni in entrata e in uscita, estraendo file, credenziali non crittografate e payload malevoli direttamente dal flusso dei dati.

## 📚 Contesto e Definizioni

Invece di osservare la rete a livello macroscopico ("Questo computer sta parlando con questo server"), Wireshark cattura il file **PCAP** (Packet Capture), decodificando l'effettiva conversazione. Si posiziona al confine tra la [[Cybersecurity]] difensiva (scoprire quale dipendente sta scaricando file anomali) e la [[Sigint]] tattica su cavo.

## 📊 Dati, Tecnologie e Metriche

L'adozione universale della crittografia HTTPS (TLS) ha limitato parzialmente le capacità di "intercettazione del contenuto testuale" di Wireshark (non si possono più leggere le email intercettate in chiaro su reti pubbliche). Tuttavia, l'analista estrae comunque i **metadati di rete**: analizzando l'Handshake crittografico, i certificati e gli indirizzi di destinazione, si può mappare la cadenza ritmica del "Beaconing" (il battito cardiaco) di un [[Malware]] che comunica con il suo server di [[Command and control]], confermando l'infezione del sistema.

## 🔗 Connessioni e Pattern

- [[Sigint]]
- [[Cyber threat intelligence]]
- [[Command and control]]
- [[Malware]]
- [[--]]
F/I/H
- [[--]]
