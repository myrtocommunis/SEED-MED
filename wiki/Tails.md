---
title: "Tails"
tags: ["OSINT", "processed", "tails", "opsec", "amnesico", "tor"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "3"
tipo: "concetto"
---

# Tails

## 🎯 Sintesi Strategica

**Tails (The Amnesic Incognito Live System)** è una distribuzione Linux orientata alla sicurezza, progettata con l'unico scopo di preservare la privacy e l'anonimato assoluto dell'utente. Utilizzata sistematicamente da giornalisti investigativi, whistleblower (es. [[Edward Snowden]]) e operatori [[Osint]] ad alto rischio, Tails funge da scudo impenetrabile contro la sorveglianza statale, la censura e l'analisi forense del dispositivo hardware.

## 📚 Contesto e Definizioni

Si fonda su due pilastri architetturali:
1.  **Amnesia:** Si avvia (Live Boot) esclusivamente da una chiavetta USB e lavora interamente nella memoria RAM. Allo spegnimento del computer, la RAM viene azzerata, non lasciando assolutamente alcuna traccia magnetica o log sul disco rigido del computer ospite. È impossibile dimostrare cosa l'utente abbia fatto.
2.  **Incognito Forzato:** Forza *tutte* le connessioni in uscita attraverso la rete [[Tor]]. Se un'applicazione tenta di connettersi in chiaro rivelando il vero IP (es. deanonimizzazione accidentale), Tails blocca il pacchetto a livello di firewall.

## 📊 Dati, Tecnologie e Metriche

Rispetto all'uso di una classica [[Macchina virtuale]] su Windows (che lascia enormi impronte forensi sul disco host), Tails protegge l'[[Opsec]] fisica. Se un analista in territorio ostile viene improvvisamente perquisito, il semplice distacco della chiavetta USB arresta il sistema e distrugge irreversibilmente l'intero contesto operativo in una frazione di secondo.

## 🔗 Connessioni e Pattern

- [[Opsec]]
- [[Macchina virtuale]]
- [[Tor]]
- [[Dark web]]
- [[--]]
F/I/H
- [[--]]
