---
title: "Api"
tags: ["OSINT", "processed", "api", "automazione", "json"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "3"
tipo: "concetto"
---

# Api

## 🎯 Sintesi Strategica

Le **API (Application Programming Interface)** sono protocolli software che permettono a due applicazioni distinte di comunicare e scambiarsi dati in modo strutturato. Per l'analista [[Osint]], le API (specificamente le REST API) sono i "tubi" attraverso i quali transita l'intelligence: permettono l'interrogazione massiva e legale di database pubblici, social network o fornitori di [[Cyber]] Threat Intelligence, superando la limitazione della raccolta manuale tramite browser.

## 📚 Contesto e Definizioni

Un'interazione API tipica si basa su richieste HTTP (GET per scaricare, POST per inviare) e restituisce dati grezzi formattati quasi sempre in **JSON**. L'analista non vede l'interfaccia grafica del sito, ma interroga direttamente il database sottostante.

## 📊 Dati, Tecnologie e Metriche

L'accesso alle API è regolato da API Keys (Chiavi segrete) e da Rate Limits (limiti di chiamate al minuto). Nelle piattaforme di [[Automazione]] come [[n8n]], le API sono il tessuto connettivo: un nodo API riceve un IP, contatta l'API di Virustotal, ottiene il JSON con l'esito dell'analisi, e passa il risultato al nodo successivo.

## 🔗 Connessioni e Pattern

- [[Automazione]]
- [[n8n]]
- [[Trattamento dell'output]]
- [[--]]
F/I/H
- [[--]]
