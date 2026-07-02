---
title: "Cyber kill chain"
tags: ["OSINT", "processed", "kill-chain", "cyber", "lockheed-martin"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "3"
tipo: "concetto"
---

# Cyber kill chain

## 🎯 Sintesi Strategica

La **Cyber Kill Chain** (sviluppata da Lockheed Martin) è un modello militare adattato alla [[Cybersecurity]] che descrive le fasi sequenziali di un attacco informatico mirato. Il concetto fondamentale è che l'attacco non è un evento isolato, ma una catena di anelli interdipendenti. Per i difensori (Blue Team) e gli analisti di [[Cyber threat intelligence]], "spezzare" la catena in un qualsiasi punto (es. bloccando la mail di phishing o isolando il malware) neutralizza l'intero attacco.

## 📚 Contesto e Definizioni

Il modello classico prevede 7 fasi rigide:
1.  **Reconnaissance (Ricognizione):** Il Threat Actor usa l'[[Osint]] per mappare i bersagli.
2.  **Weaponization:** Crea il payload infetto.
3.  **Delivery:** Invia l'arma (es. [[Attacco di phishing]]).
4.  **Exploitation:** Il malware sfrutta la vulnerabilità (es. un [[Zero-day]]).
5.  **Installation:** Il malware si insedia nel sistema.
6.  **Command and Control (C2):** Apre un canale di comunicazione con l'hacker.
7.  **Actions on Objectives:** Esfiltrazione dati o distruzione.

## 📊 Dati, Tecnologie e Metriche

Sebbene fondamentale storicamente, il modello Lockheed è oggi criticato per la sua rigidità. Gli attacchi moderni (come gli insider threat o il phishing cloud-to-cloud) spesso bypassano intere fasi della Kill Chain classica, spingendo la comunità ad affidarsi a matrici flessibili come il [[Mitre att&ck]].

## 🔗 Connessioni e Pattern

- [[Cyber threat intelligence]]
- [[Mitre att&ck]]
- [[Apt]]
- [[Command and control]]
- [[--]]
F/I/H
- [[--]]
