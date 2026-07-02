---
title: "Spiderfoot"
tags: ["OSINT", "processed", "spiderfoot", "automazione", "ricognizione"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Spiderfoot

## 🎯 Sintesi Strategica

**Spiderfoot** è una piattaforma di automazione [[Osint]] e di Attack Surface Management (ASM). Sviluppata in Python, consente di eseguire ricognizioni massive interrogando simultaneamente oltre 200 API pubbliche e fonti dati, aggregando le informazioni su un bersaglio specifico (Indirizzi IP, Domini, Email, Nomi Utente, Subnet). È il ponte ideale tra la Threat Intelligence puramente manuale e la mappatura automatizzata dell'infrastruttura di un Threat Actor.

## 📚 Contesto e Definizioni

A differenza di strumenti di visualizzazione puramente manuali come [[Maltego]] (dove l'utente clicca sulle trasformazioni passo-passo), Spiderfoot eccelle nella fase di "Scansione ad Ampio Spettro". L'analista inserisce il dominio bersaglio e il tool esegue una ricerca a cascata automatica: trova i sottodomini, estrae le email associate, cerca quelle email nelle violazioni di database passate (Data Breaches), e identifica le tecnologie server in uso.

## 📊 Dati, Tecnologie e Metriche

Il rischio operativo nell'utilizzo di Spiderfoot è il **Rumore**. Generando rapidamente migliaia di data-point (False Positives), rischia di sovraccaricare cognitivamente l'analista. Per questo motivo, viene solitamente integrato in pipeline superiori ([[n8n]] o piattaforme SOAR) che filtrano l'output grezzo e lo formattano in indicatori di compromissione validati per la [[Cyber threat intelligence]].

## 🔗 Connessioni e Pattern

- [[Automazione]]
- [[Maltego]]
- [[Cyber threat intelligence]]
- [[Api]]
- [[--]]
F/I/H
- [[--]]
