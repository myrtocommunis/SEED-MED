---
title: "Power Automate"
tags:
  - OSINT
  - automation
  - power-automate
  - workflow
  - low-code
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "1"
tipo: "concetto"
---

# Power Automate

## 🎯 Sintesi Strategica

Power Automate è la piattaforma low‑code di Microsoft per orchestrare workflow che collegano servizi cloud, API e strumenti on‑premise. All’interno di un ecosistema OSINT, permette di **automatizzare la raccolta, l’ETL, l’enrichment e la distribuzione dell’intelligence** con pochi click, riducendo la necessità di script personalizzati e accelerando la produzione di report e alert.

## 📚 Contesto e Definizioni

- **Flow**: sequenza di azioni (trigger → azioni) definita attraverso il designer grafico.
- **Trigger**: evento che avvia il flow (es. nuovo file su Onedrive, messaggio su Teams, webhook HTTP).
- **Azione**: operazione eseguita (es. chiamata HTTP, parsing JSON, invio email, aggiornamento su Sharepoint).
- **Connettori**: plugin predefiniti per servizi popolari (Twitter, Azure Blob, Google Sheets, API REST, Shodan, Virustotal, ecc.).

## 📊 Dati, Tecnologie e Metriche

| Elemento | Descrizione |
|---|---|
| **Integrazione OSINT** | Connettori HTTP per endpoint di scraping, API di threat‑intel, feed [[RSS]]/Atom. |
| **Gestione ETL** | Azioni `Parse JSON`, `Select`, `Compose` per trasformare i dati in forma normalizzata. |
| **Output** | Invio di messaggi a Slack/Telegram, scrittura di righe in Excel/Google Sheets, pubblicazione su Power BI. |
| **Governance** | Versionamento dei flow, audit log centralizzato per tracciabilità delle attività. |
| **Sicurezza** | Policy di runtime, connessioni tramite Azure AD, gestione token OAuth per API sensibili. |

## 🔍 Analisi Operativa ed Applicazioni OSINT

1. **Raccolta dati** – Trigger su nuovo file CSV in Onedrive → HTTP GET da API di feed [[RSS]] → archiviazione raw. 
2. **Normalizzazione** – Azione `Parse JSON` → mapping dei campi, rimozione duplicati, aggiunta timestamp. 
3. **Enrichment** – Chiamata a servizi di geolocalizzazione IP, lookup WHOIS via connettore HTTP. 
4. **Distribuzione** – Inserimento in tabella Sharepoint per revisione manuale; notifica su Teams con sintesi dei nuovi indicatori. 
5. **Alert** – Condizione `If` sulla soglia di anomalie → invio immediato a canale Telegram per risposta rapida. 

## 🔮 Lacune Informative e Prossimi Passi

* **Rate‑limit**: la versione gratuita limita a 6000 esecuzioni al mese; per operazioni ad alta frequenza valutare piani premium o Azure Logic Apps. 
* **Debugging**: la diagnostica di errori di parsing è spesso poco dettagliata; aggiungere step di `Compose` per loggare payload intermedi. 
* **Privacy**: i dati sensibili dovrebbero attraversare un gateway on‑premise, evitando di inviare PII a servizi cloud non certificati. 
* **Scalabilità**: per pipeline continue su grandi volumi, considerare l’integrazione con Azure Data Factory o Snowflake come back‑end di storage.

## 🔗 Connessioni e Pattern

- [[Trattamento dell'output]]
- [[Tassonomia dei tools]]
- [[Cyber]]
- [[Dashboarding con ai]]
- [[Power BI]]
- [[Opsec]]

- [[--]]
F/I/H
- [[--]]
