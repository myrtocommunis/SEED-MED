---
title: "Social engineering toolkit"
tags: ["OSINT", "processed", "set", "phishing", "ingegneria-sociale", "cyber"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Social engineering toolkit

## 🎯 Sintesi Strategica

Il **Social Engineering Toolkit (SET)**, creato da David Kennedy (Trustedsec), è un framework open-source integrato nelle distribuzioni penetration testing (es. Kali Linux). È progettato specificamente per simulare test d'intrusione basati sul fattore umano, automatizzando le complesse fasi di preparazione degli attacchi di [[Ingegneria sociale]] (Phishing, Spear-Phishing, clonazione di siti web). Nella [[Cyber threat intelligence]], studiare il SET permette agli analisti di comprendere e prevedere i vettori di attacco standardizzati impiegati dai criminali informatici di fascia media.

## 📚 Contesto e Definizioni

L'efficacia del SET risiede nell'automazione del "Weaponization".
I moduli principali includono:
*   **Site Cloner:** Inserendo l'URL di un sito legittimo (es. la pagina di login di Microsoft365), il SET clona perfettamente la veste grafica e l'HTML su un server malevolo, pronto per catturare le password.
*   **Mass Mailer:** Un motore integrato per inviare campagne di [[Attacco di phishing]] contraffacendo il mittente (Spoofing).

## 📊 Dati, Tecnologie e Metriche

Mentre i gruppi [[Apt]] statali costruiscono la propria infrastruttura d'attacco su misura da zero, la maggior parte dei cybercriminali opportunisti si appoggia a tool pre-confezionati come il SET. L'analista [[Osint]] può smascherare queste campagne dilettantistiche analizzando le intestazioni HTTP e i pattern dei metadati generati di default dal toolkit, bloccando l'infrastruttura alla fonte.

## 🔗 Connessioni e Pattern

- [[Ingegneria sociale]]
- [[Attacco di phishing]]
- [[Cybersecurity]]
- [[Cyber kill chain]]
- [[--]]
F/I/H
- [[--]]
