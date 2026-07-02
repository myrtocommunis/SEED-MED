---
title: "Firma digitale"
tags: ["OSINT", "processed", "firma-digitale", "crittografia", "autenticazione"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Firma digitale

## 🎯 Sintesi Strategica

La **Firma Digitale** è uno schema matematico utilizzato per dimostrare l'autenticità e l'integrità di un messaggio o di un documento digitale. È l'equivalente crittografico di una firma manoscritta, ma è intrinsecamente molto più sicura e non falsificabile. Rappresenta l'applicazione complementare della [[Crittografia asimmetrica]] combinata con la [[Funzione di hash]], fondamento dei contratti legali elettronici e delle transazioni sulle [[Blockchain]].

## 📚 Contesto e Definizioni

A differenza della cifratura (che nasconde il testo), la firma digitale non nasconde nulla, ma **certifica chi lo ha scritto**.
Il meccanismo (Autenticazione e Non Ripudio):
1.  Alice scrive un documento e ne calcola l'Hash.
2.  Alice usa la sua **Chiave Privata** per criptare solo l'Hash (questa è la Firma Digitale).
3.  Invia il documento in chiaro e la Firma a Bob.
4.  Bob usa la **Chiave Pubblica** di Alice per decriptare la firma e ottenere l'Hash calcolato da Alice. Poi ricalcola lui stesso l'Hash del documento ricevuto. Se i due Hash combaciano, Bob ha la certezza matematica assoluta che il documento è stato inviato da Alice e che nessuno lo ha modificato durante il transito.

## 📊 Dati, Tecnologie e Metriche

Sulla blockchain di [[Bitcoin]], ogni volta che l'utente spende dei fondi, firma la transazione con la propria chiave privata. La rete verifica la validità della firma usando la chiave pubblica (che è l'indirizzo del Wallet). Nel contrasto al cybercrimine, la firma del codice (Code Signing) rubata viene usata dai gruppi [[Apt]] per firmare i propri [[Malware]] facendoli apparire come aggiornamenti legittimi rilasciati da Microsoft o Apple (attacco alla Supply Chain).

## 🔗 Connessioni e Pattern

- [[Crittografia asimmetrica]]
- [[Funzione di hash]]
- [[Blockchain]]
- [[Apt]]
- [[--]]
F/I/H
- [[--]]
