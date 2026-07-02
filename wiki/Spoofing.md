---
title: "Spoofing"
tags: ["OSINT", "processed", "spoofing", "cybersecurity", "inganno", "phishing"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Spoofing

## 🎯 Sintesi Strategica

Lo **Spoofing (Contraffazione)** è una vasta classe di attacchi informatici in cui una persona o un programma si maschera falsificando i propri dati identificativi per fingere di essere una fonte legittima e fidata. Nel dominio dell'[[Osint]] e dell'[[Ingegneria sociale]], lo Spoofing è il fondamento tecnico su cui si basa l'inganno: se la vittima non crede che il mittente sia autorevole, l'attacco fallisce.

## 📚 Contesto e Definizioni

Esistono diverse varianti operative:
1.  **Email Spoofing:** Alterare il campo "Mittente" (From:) nell'intestazione di una mail. Permette all'hacker di inviare un [[Attacco di phishing]] facendo apparire il messaggio come proveniente dall'indirizzo ufficiale `CEO@azienda.com` invece che da `hacker@gmail.com`.
2.  **Caller ID Spoofing:** Falsificare il numero di telefono mostrato sul display della vittima durante una chiamata, tecnica chiave nel Vishing (Voice Phishing).
3.  **IP/MAC Spoofing:** Nel networking, falsificare l'[[Indirizzo ip]] o il [[Mac address]] sorgente di un pacchetto dati per eludere i firewall basati su liste nere, usato frequentemente negli attacchi [[Ddos]].

## 📊 Dati, Tecnologie e Metriche

Per difendersi dall'Email Spoofing, l'infrastruttura web ha adottato tre protocolli crittografici: SPF, DKIM e DMARC. Configurando correttamente questi record sul [[Dns]] aziendale, il server di posta del destinatario controlla matematicamente se il server che ha inviato la mail era autorizzato a farlo, bloccando in automatico le frodi CEO (Business Email Compromise).

## 🔗 Connessioni e Pattern

- [[Attacco di phishing]]
- [[Ingegneria sociale]]
- [[Dns]]
- [[Indirizzo ip]]
- [[--]]
F/I/H
- [[--]]
