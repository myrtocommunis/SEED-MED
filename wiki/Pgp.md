---
title: "Pgp"
tags: ["OSINT", "processed", "pgp", "crittografia", "email", "sicurezza"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Pgp

## 🎯 Sintesi Strategica

Il **PGP (Pretty Good Privacy)** è un programma storico (e un protocollo standard, OpenPGP) che fornisce privacy e autenticazione crittografica per la comunicazione dei dati. È l'implementazione pratica più famosa della [[Crittografia asimmetrica]] applicata alla protezione delle email, dei testi e dei file. Pur essendo tecnicamente obsoleto nella sua gestione delle chiavi rispetto ai moderni protocolli mobili (come Signal), rimane lo standard aureo per le comunicazioni nei [[Darknet market]] e per i giornalisti investigativi.

## 📚 Contesto e Definizioni

Il funzionamento si basa su una Coppia di Chiavi:
Un utente sul [[Dark web]] pubblica sul proprio profilo forum la propria **Chiave Pubblica** (un blocco di testo incomprensibile). Se un investigatore sotto copertura ([[Sock puppet]]) vuole comprargli un database rubato, cripta il proprio indirizzo di spedizione usando quella chiave pubblica. Solo il venditore, usando la sua password locale per sbloccare la **Chiave Privata**, potrà leggere il messaggio.

## 📊 Dati, Tecnologie e Metriche

Il problema principale del PGP è la totale assenza di *Forward Secrecy* (Segretezza Perfetta in Avanti). Se le Forze dell'Ordine arrestano l'amministratore del forum e sequestrano la sua Chiave Privata oggi, possono usarla per decriptare *tutte* le email storiche intercettate negli ultimi 10 anni (che avevano conservato criptate in un [[Data lake]]). Inoltre, il PGP non nasconde i [[Metadati]] dell'email (Mittente, Destinatario e Oggetto restano sempre in chiaro).

## 🔗 Connessioni e Pattern

- [[Crittografia asimmetrica]]
- [[Darknet market]]
- [[Dark web]]
- [[Metadati]]
- [[--]]
F/I/H
- [[--]]
