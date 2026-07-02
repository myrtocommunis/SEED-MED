---
title: "Nmap"
tags: ["OSINT", "processed", "nmap", "port-scanning", "cyber", "ricognizione"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Nmap

## 🎯 Sintesi Strategica

**Nmap (Network Mapper)** è lo scanner di porte e lo strumento di esplorazione di rete open-source più diffuso e rispettato al mondo. Sebbene esuli dall'[[Osint]] passiva pura (poiché invia fisicamente pacchetti verso l'infrastruttura bersaglio), è il passo zero della fase di ricognizione attiva in qualsiasi operazione di [[Cybersecurity]], Penetration Testing o mappatura di Threat Actors nella [[Cyber threat intelligence]].

## 📚 Contesto e Definizioni

La sua funzione primaria è identificare quali host sono attivi su una rete (Host Discovery) e, soprattutto, quali "porte logiche" (da 1 a 65535) sono aperte e in ascolto. Il suo vero potere risiede però nell'**OS Fingerprinting** e nel **Version Detection**: analizzando le risposte TCP/UDP a livello di pacchetto, Nmap deduce con precisione il sistema operativo del bersaglio (es. Linux Kernel 4.15) e il servizio esatto in esecuzione su quella porta (es. Apache 2.4.49, noto per vulnerabilità critiche).

## 📊 Dati, Tecnologie e Metriche

Un errore comune per gli analisti novizi è usare Nmap senza precauzioni di [[Opsec]]. Essendo uno scanner aggressivo ("Rumoroso"), l'invio di un Port Scan intensivo verso un server scatena immediatamente gli allarmi dei firewall aziendali (IDS/IPS), svelando l'indirizzo IP dell'investigatore. Gli analisti avanzati utilizzano tecniche di scansione "Stealth" (es. SYN Scan) o delegano la scansione a motori di ricerca IoT terzi come [[Shodan (motore di ricerca)]] per mantenere l'invisibilità tattica.

## 🔗 Connessioni e Pattern

- [[Cybersecurity]]
- [[Opsec]]
- [[Shodan (motore di ricerca)]]
- [[Cyber kill chain]]
- [[--]]
F/I/H
- [[--]]
