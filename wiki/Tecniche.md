---
title: "Tecniche"
tags: ["OSINT", "processed", "tecniche", "metodologia", "mitre-attack", "kill-chain"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Tecniche

## 🎯 Sintesi Strategica

Nel glossario della [[Cyber threat intelligence]] (modellato sul framework [[Mitre att&ck]]), le **Tecniche** rappresentano il livello intermedio tra le "Tattiche" (l'obiettivo generale dell'hacker, es. "Rubare credenziali") e le "Procedure" (i comandi esatti digitati sulla tastiera). Comprendere le Tecniche significa capire *come* l'avversario ha intenzione di RAGgiungere il suo scopo, permettendo al difensore di posizionare trappole specifiche lungo il percorso.

## 📚 Contesto e Definizioni

Gerarchia TTPs (Tattiche, Tecniche e Procedure):
*   **Tattica (Il Perché):** Accesso Iniziale. L'hacker vuole entrare nella rete.
*   **Tecnica (Il Come):** Spear-Phishing. Decide di mandare un'email mirata con allegato infetto invece di sfondare il firewall.
*   **Procedura (Il Cosa esatto):** Invia un'email con oggetto "Fattura_Urgente.pdf" contenente un [[Trojan]] della famiglia Emotet.

## 📊 Dati, Tecnologie e Metriche

Gli analisti [[Osint]] e di Threat Intelligence catalogano i gruppi criminali ([[Apt]]) proprio in base alle Tecniche che utilizzano abitualmente (il loro "Stile" o Firma). Se un attacco a una banca sudamericana utilizza la Tecnica dell'iniezione di codice in memoria (Fileless Malware) unita a un attacco Supply chain, l'analista sa, con alta probabilità statistica, che non si tratta di criminali alle prime armi, ma di un gruppo state-sponsored, stringendo il cerchio dell'Attribuzione.

## 🔗 Connessioni e Pattern

- [[Mitre att&ck]]
- [[Cyber threat intelligence]]
- [[Apt]]
- [[--]]
F/I/H
- [[--]]
