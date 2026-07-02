---
title: "Webhooks"
tags: ["OSINT", "processed", "webhooks", "automazione", "api"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Webhooks

## 🎯 Sintesi Strategica

I **Webhooks** sono "callback" HTTP definite dall'utente. Mentre con una normale [[Api]] l'analista deve "chiedere" continuamente al server se ci sono novità (Polling), il Webhook è un protocollo passivo: l'analista fornisce un URL "in ascolto". Quando si verifica un evento sul server esterno, è il server a "chiamare" istantaneamente l'URL fornito dall'analista, inviando il payload di dati. Questa architettura "Push" è vitale per la velocità e l'efficienza computazionale in [[Osint]].

## 📚 Contesto e Definizioni

Spesso definiti come "Reverse API". Permettono reazioni in tempo reale. Se un gruppo terroristico pubblica un messaggio su Telegram, un Webhook lo intercetta al millisecondo e lo spinge nel database dell'analista, senza dover interrogare l'API di Telegram ogni 5 secondi.

## 📊 Dati, Tecnologie e Metriche

Nelle piattaforme di orchestrazione come [[n8n]], il **Webhook Node** funge spesso da Trigger (Innesco) iniziale di tutta la pipeline investigativa. Permette, ad esempio, di connettere piattaforme di [[Scraping]] asincrono come [[Apify]]: quando l'estrazione di un milione di tweet finisce dopo ore di lavoro, Apify invia un "colpo" al Webhook di n8n informando che il JSON è pronto per il download e per il processo in [[Power BI]].

## 🔗 Connessioni e Pattern

- [[Api]]
- [[n8n]]
- [[Automazione]]
- [[--]]
F/I/H
- [[--]]
