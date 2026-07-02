---
title: "Kill switch"
tags: ["OSINT", "processed", "kill-switch", "sicurezza", "malware", "emergenza"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Kill switch

## 🎯 Sintesi Strategica

Un **Kill Switch (Interruttore di Emergenza)** è un meccanismo di sicurezza informatica progettato per arrestare, disabilitare o distruggere istantaneamente un sistema hardware o software in caso di emergenza o compromissione. Nell'[[Opsec]] difensiva protegge l'identità dell'utente in caso di attacco; nella programmazione offensiva ([[Malware]]), garantisce agli hacker il controllo "a briglia corta" del virus che hanno scateNATO.

## 📚 Contesto e Definizioni

Applicazioni pratiche principali:
1.  **Kill Switch delle [[Virtual private network]]:** Funzione vitale del software VPN. Se la connessione al server crittografato si interrompe per un nanosecondo a causa di un guasto di rete, il Kill Switch "taglia" fisicamente la connessione internet del computer intero. Evita che l'[[Indirizzo ip]] reale dell'utente venga rivelato in chiaro (Leak) durante il caricamento di una pagina.
2.  **Kill Switch Forense:** I giornalisti (es. con [[Tails]]) usano combinazioni di tasti "Panico" per sovrascrivere la RAM e distruggere le chiavi di decrittazione in caso di irruzione della polizia.

## 📊 Dati, Tecnologie e Metriche

Il caso d'uso offensivo più celebre risale all'attacco [[Ransomware]] globale Wannacry (2017). Il virus possedeva un Kill Switch codificato al suo interno: prima di criptare un PC, il malware provava a connettersi a un dominio web specifico senza senso (es. `iuqerfsodp9...com`). Se la connessione falliva, il virus attaccava. Un ricercatore indipendente (Marcus Hutchins) registrò il dominio. Improvvisamente il virus riuscì a connettersi, attivò il Kill Switch credendo di essere in una [[Sandboxing]] e fermò l'infezione globale.

## 🔗 Connessioni e Pattern

- [[Opsec]]
- [[Virtual private network]]
- [[Ransomware]]
- [[Sandboxing]]
- [[--]]
F/I/H
- [[--]]
