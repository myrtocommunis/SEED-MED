---
title: "Oauth"
tags: ["OSINT", "processed", "oauth", "api", "autenticazione", "cyber"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Oauth

## 🎯 Sintesi Strategica

**OAuth** (Open Authorization) è uno standard aperto (protocollo) utilizzato per l'autorizzazione degli accessi su Internet. È la tecnologia alla base del celebre pulsante "Accedi con Google" o "Accedi con Facebook" ([[Capitalismo delle piattaforme]]). Permette a un'applicazione di terze parti di ottenere un accesso limitato all'account di un utente senza che quest'ultimo debba condividere la propria password. Nel contesto della [[Cyber threat intelligence]], OAuth rappresenta un vettore d'attacco devastante e silenzioso.

## 📚 Contesto e Definizioni

Invece di dare la tua password a un'app per il calendario (che sarebbe disastroso), OAuth genera un "Token di Autorizzazione" (Access Token). L'app mostra questo token a Google, e Google le permette di leggere solo gli eventi in calendario.
Se un utente perde o si fa rubare il Token, l'attaccante può usarlo per impersonare l'utente e interfacciarsi con l'[[Api]] aggirando totalmente anche i controlli più severi, inclusa l'Autenticazione a Due Fattori (2FA).

## 📊 Dati, Tecnologie e Metriche

I criminali utilizzano campagne avanzate di [[Attacco di phishing]] denominate *Consent Phishing* o *Illicit Consent Grant*. Non chiedono all'utente la password falsa di Microsoft, ma gli inviano un link legittimo Microsoft in cui viene richiesto di "concedere i permessi" a una presunta app fidata per leggere le mail. Se la vittima clicca "Accetta", cede legalmente il Token all'hacker, che potrà scaricare silenziosamente l'intera casella di posta per anni senza far scattare allarmi.

## 🔗 Connessioni e Pattern

- [[Api]]
- [[Attacco di phishing]]
- [[Cyber threat intelligence]]
- [[Capitalismo delle piattaforme]]
- [[--]]
F/I/H
- [[--]]
