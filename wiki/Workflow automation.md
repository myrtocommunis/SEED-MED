---
title: "Workflow automation"
tags: ["OSINT", "processed", "automazione", "soar", "pipeline", "soc"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Workflow automation

## 🎯 Sintesi Strategica

La **Workflow Automation (Automazione dei Flussi di Lavoro)** è la pratica ingegneristica di concatenare l'esecuzione di compiti analitici sequenziali eliminando l'interazione manuale umana. In ambito [[Cybersecurity]] e investigativo, è il pilastro dei sistemi SOAR (Security Orchestration, Automation, and Response). Consente ai team di intelligence di scalare operativamente: l'automazione esegue il lavoro ripetitivo da "operaio", lasciando all'analista il ruolo di "detective" (il [[Paradigma human-in-the-loop]]).

## 📚 Contesto e Definizioni

Un classico workflow manuale di [[Cyber threat intelligence]]:
1. Arriva una mail di phishing sospetta.
2. L'analista copia a mano l'[[Indirizzo ip]].
3. Apre Virustotal e incolla l'IP.
4. Apre un database OSINT e controlla chi possiede il dominio.
5. Scrive un report.

Con la Workflow Automation (usando piattaforme come Cortex XSOAR o strumenti [[No-code per raccolta dati osint]] come n8n), queste 5 fasi vengono eseguite in 0.3 secondi automaticamente alla ricezione della mail. L'analista riceve direttamente il report pre-compilato con un pulsante "Blocca IP".

## 📊 Dati, Tecnologie e Metriche

Oltre a velocizzare i tempi di reazione (Response Time) di 1000x, l'automazione standardizza le procedure operative (SOP - Standard Operating Procedures). Questo previene la perdita di conoscenze: se l'analista senior si dimette, il modo in cui eseguiva i controlli incrociati rimane codificato nella [[Pipeline osint]], garantendo continuità alla [[Sicurezza nazionale]] o aziendale.

## 🔗 Connessioni e Pattern

- [[No-code per raccolta dati osint]]
- [[Cyber threat intelligence]]
- [[Pipeline osint]]
- [[Paradigma human-in-the-loop]]
- [[--]]
F/I/H
- [[--]]
