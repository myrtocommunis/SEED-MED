---
title: "Shodan (motore di ricerca)"
tags: ["OSINT", "processed", "shodan", "iot", "cyber", "banner-grabbing"]
date: "2026-05-15"
status: "draft"
depth: "deep"
sources: "4"
tipo: "concetto"
---

# Shodan (motore di ricerca)

## 🎯 Sintesi Strategica

**Shodan** è il motore di ricerca di riferimento per il dominio [[Cyber]] e l'Internet of Things (IoT). A differenza di Google, che indicizza il contenuto testuale ospitato sui server web (Porte 80/443), Shodan indicizza i **dispositivi fisici** connessi a Internet: telecamere di sicurezza, router, sistemi di controllo industriale (SCADA/ICS), semafori e database cloud. Per l'analista [[Osint]], Shodan è lo strumento primario per mappare la "Superficie d'Attacco" (Attack Surface) di un target o per profilare l'infrastruttura di Threat Actors statali, il tutto in modalità passiva (senza inviare un singolo pacchetto diretto al bersaglio).

## 📚 Contesto e Definizioni

Shodan opera scansionando continuamente l'intero spazio IPv4 globale (circa 4 miliardi di indirizzi IP) eseguendo una tecnica chiamata **Banner Grabbing**:
*   *Banner:* Il messaggio di testo che un dispositivo o un servizio restituisce quando gli si chiede di identificarsi. Contiene metadati preziosi come la versione del software operativo, il nome del dispositivo, il protocollo crittografico in uso e l'orario di sistema.
*   Indicizzando questi Banner, Shodan permette ricerche iper-specifiche come: "Trovami tutti i server in Russia che eseguono la versione vulnerabile di Apache Tomcat sulla porta 8080".

## 📊 Dati, Tecnologie e Metriche

L'estrazione del valore OSINT avviene tramite la rigorosa sintassi di ricerca (Dorking) di Shodan:
1.  **Filtri Geografici ed Organizzativi:** `country:"IT"`, `city:"Rome"`, `org:"Ministero della Difesa"`.
2.  **Filtri di Servizio e Vulnerabilità:** `port:"3389"` (Ricerca di Remote Desktop Protocol lasciati aperti), `has_vuln:"True"` (Restituisce dispositivi con CVE confermate).
3.  **Filtri IoT/SCADA:** Ricerca di diciture specifiche nei banner per individuare centrali elettriche o impianti di purificazione dell'acqua connessi sbadatamente alla rete pubblica senza password.

## 🔍 Analisi Operativa ed Applicazioni OSINT

Shodan è al centro della *Network Defense* e dell'intelligence offensiva:
*   **Leak Detection:** Ricerca di database Elasticsearch o MongoDB non protetti da autenticazione. Spesso le aziende subiscono data breach colossali non a causa di hacker, ma perché un ingegnere ha lasciato un database di produzione indicizzabile pubblicamente.
*   **OPSEC Investigation:** Shodan permette di scoprire se un sito di [[Disinformazione]] (FIMI) è protetto dietro Cloudflare. Se lo sviluppatore ha commesso un errore di configurazione, Shodan può rivelare l'Indirizzo IP originario reale del server (bypassando la CDN), permettendo di identificare l'hosting provider in Russia o Iran.

## 🔮 Lacune Informative e Prossimi Passi

*   **Latenza del Dato:** Shodan scansiona Internet in modo ciclico. Il banner di un IP potrebbe essere vecchio di settimane. Un attaccante scaltro potrebbe aver già chiuso la porta vulnerabile o cambiato server. Per la Threat Intelligence tattica real-time, i dati di Shodan devono essere integrati con scanner attivi mirati (es. Nmap), assumendosi però il rischio di allertare le difese del target.

## 🔗 Connessioni e Pattern

- [[Cyber]]
- [[Network intelligence]]
- [[Opsec]]
- [[Osint]]
- [[Ip-dns intelligence]]

- [[--]]
F/I/H
- [[--]]
