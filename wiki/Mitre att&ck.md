---
title: "Mitre att&ck"
tags: ["OSINT", "processed", "mitre", "cti", "framework", "cyber"]
date: "2026-05-15"
status: "draft"
depth: "deep"
sources: "4"
tipo: "concetto"
---

# Mitre att&ck

## 🎯 Sintesi Strategica

Il **MITRE ATT&CK** (Adversarial Tactics, Techniques, and Common Knowledge) è il framework globale e la base di conoscenza fondamentale per la [[Cyber threat intelligence]]. Funge da "Tavola Periodica" degli attacchi informatici: documenta in modo standardizzato e tassonomico le Tattiche e le Tecniche utilizzate dai Threat Actor ([[Apt]]) basandosi su osservazioni del mondo reale. Per l'analista [[Osint]], è la lingua franca per decodificare e comunicare il comportamento di un avversario.

## 📚 Contesto e Definizioni

A differenza della [[Cyber kill chain]] (che è un modello teorico lineare), ATT&CK è una matrice non lineare.
*   **Tattiche (Le Colonne):** Il *Perché* l'attaccante esegue un'azione (es. "Initial Access", "Privilege Escalation", "Exfiltration").
*   **Tecniche (Le Celle):** Il *Come* l'attaccante RAGgiunge quell'obiettivo tattico (es. per l'Initial Access, la tecnica può essere lo "Spearphishing Attachment" o "Valid Accounts").

## 📊 Dati, Tecnologie e Metriche

L'integrazione del MITRE nelle piattaforme di [[Automazione]] OSINT è sistematica. Quando un analista raschia un report tecnico su un nuovo [[Malware]], utilizza script NLP per mappare automaticamente il testo ai codici MITRE (es. T1566 per il Phishing). Questo permette di correlare gruppi criminali apparentemente slegati che utilizzano esattamente la stessa firma comportamentale (TTPs).

## 🔗 Connessioni e Pattern

- [[Cyber threat intelligence]]
- [[Cyber kill chain]]
- [[Apt]]
- [[--]]
F/I/H
- [[--]]
