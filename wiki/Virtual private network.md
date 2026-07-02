---
title: "Virtual private network"
tags: ["OSINT", "processed", "vpn", "opsec", "crittografia", "proxy"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Virtual private network

## 🎯 Sintesi Strategica

Una **VPN (Virtual Private Network)** stabilisce un tunnel crittografato e sicuro tra il dispositivo dell'utente e un server remoto gestito dal fornitore della VPN, instradando tutto il traffico Internet attraverso quel tunnel. Nelle operazioni di [[Osint]] e di indagine, è lo strumento di base (il Livello 1) della Sicurezza operativa (OPSEC): impedisce al provider internet locale (es. Fastweb o Telecom) di monitorare quali siti l'analista sta visitando e maschera il vero indirizzo IP agli occhi del server bersaglio.

## 📚 Contesto e Definizioni

A differenza di un [[Proxy]] (che maschera l'IP ma spesso invia i dati in chiaro per una singola applicazione), la VPN cifra a livello di sistema operativo *tutto* il traffico in uscita (browser, email, aggiornamenti in background).
**Il limite strutturale:** La VPN sposta semplicemente la fiducia dall'ISP locale al provider della VPN. Se l'analista sta indagando su criminali russi usando una VPN russa gratuita, o se il server VPN è compromesso, il provider può leggere tutto il traffico o registrarlo (Logging).

## 📊 Dati, Tecnologie e Metriche

Per la [[Cyber threat intelligence]], le credenziali di accesso alle VPN aziendali (VPN aziendali, non commerciali come NordVPN) sono tra i beni più preziosi venduti dai criminali sui [[Darknet market]]. I gruppi [[Ransomware]] acquistano le credenziali dei dipendenti rubate tramite [[Attacco di phishing]], e usano la VPN ufficiale per entrare pacificamente nella rete interna dell'azienda bersaglio, bypassando totalmente i firewall perimetrali.

## 🔗 Connessioni e Pattern

- [[Opsec]]
- [[Proxy]]
- [[Ransomware]]
- [[Attacco di phishing]]
- [[--]]
F/I/H
- [[--]]
