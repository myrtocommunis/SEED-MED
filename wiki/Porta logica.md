---
title: "Porta logica"
tags: ["OSINT", "processed", "porte", "networking", "cyber", "scansione"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Porta logica

## 🎯 Sintesi Strategica

Nell'informatica di rete, una **Porta Logica** è un endpoint di comunicazione virtuale del sistema operativo. Mentre l'[[Indirizzo ip]] identifica lo specifico computer sulla rete mondiale (simile all'indirizzo del condominio), la Porta identifica lo specifico *servizio o applicazione* in esecuzione su quel computer (simile al numero dell'appartamento). La comprensione delle porte è il prerequisito assoluto per usare scanner come [[Nmap]] o [[Shodan (motore di ricerca)]].

## 📚 Contesto e Definizioni

Esistono 65.535 porte TCP/UDP disponibili. Alcune porte standard universalmente riconosciute:
*   **Porta 80 / 443:** Traffico Web (HTTP / HTTPS).
*   **Porta 22:** Accesso remoto sicuro per server Linux (SSH).
*   **Porta 3389:** Accesso remoto per Windows ([[Rdp]]).
*   **Porta 53:** Servizio di risoluzione nomi ([[Dns]]).

## 📊 Dati, Tecnologie e Metriche

Una porta aperta di per sé non è una vulnerabilità (un server web *deve* avere la porta 443 aperta per funzionare). La vulnerabilità risiede nel **software obsoleto** che risponde dietro quella porta. L'obiettivo del [[Vulnerability assessment]] è determinare quali porte sono superflue e andrebbero chiuse dal firewall (Attack Surface Reduction) e scansionare le restanti per assicurarsi che siano aggiornate contro gli exploit noti.

## 🔗 Connessioni e Pattern

- [[Indirizzo ip]]
- [[Nmap]]
- [[Shodan (motore di ricerca)]]
- [[Rdp]]
- [[--]]
F/I/H
- [[--]]
