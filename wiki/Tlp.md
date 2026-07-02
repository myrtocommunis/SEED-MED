---
title: "Tlp"
tags: ["OSINT", "processed", "tlp", "opsec", "classificazione", "disseminazione"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "3"
tipo: "concetto"
---

# Tlp

## 🎯 Sintesi Strategica

Il **TLP (Traffic Light Protocol - Protocollo a Semaforo)** è lo standard globale per la classificazione e la condivisione sicura delle informazioni sensibili nel settore della [[Cybersecurity]] e dell'intelligence investigativa. Creato originariamente nel Regno Unito (NIAC), facilita la condivisione rapida tra agenzie governative, CERT e aziende private (Blue Team), garantendo che l'informazione giunga al destinatario corretto senza mai compromettere le fonti ([[Opsec]]) nella delicatissima fase di [[Disseminazione]].

## 📚 Contesto e Definizioni

A differenza delle classificazioni militari rigide (Top Secret, Secret, Confidential), il TLP è flessibile e basato sulla fiducia. Il creatore del documento vi appone uno dei quattro colori (aggiornati al TLP 2.0):
1.  **TLP:RED** (Rosso): Condivisione strettamente ristretta *solo* ai partecipanti diretti alla riunione. Inoltro severamente vietato.
2.  **TLP:AMBER** (Ambra): Condivisione limitata esclusivamente all'interno della propria organizzazione (o TLP:AMBER+STRICT, solo per la propria unità).
3.  **TLP:GREEN** (Verde): Condivisione consentita con la comunità esterna allargata (partner di settore), ma divieto di pubblicazione pubblica online.
4.  **TLP:CLEAR** (Ex TLP:WHITE): L'informazione può essere diffusa liberamente a livello globale su internet.

## 📊 Dati, Tecnologie e Metriche

Quando un'agenzia OSINT produce un report di [[Cyber threat intelligence]] su una campagna di [[Attacco di phishing]] in corso (es. contenente [[Zero-day]] non ancora patchati), etichetterà il documento con **TLP:AMBER** inviandolo solo ai CISO (Chief Information Security Officer) delle banche bersaglio. Disseminarlo pubblicamente (TLP:CLEAR) avviserebbe i cybercriminali che sono stati scoperti, vanificando le indagini.

## 🔗 Connessioni e Pattern

- [[Disseminazione]]
- [[Opsec]]
- [[Cyber threat intelligence]]
- [[--]]
F/I/H
- [[--]]
