---
title: "Imsi catcher"
tags: ["OSINT", "processed", "imsi-catcher", "intercettazione", "mobile", "stingray"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "3"
tipo: "concetto"
---

# Imsi catcher

## 🎯 Sintesi Strategica

L'**IMSI Catcher** (noto commercialmente come *Stingray*) è un dispositivo di sorveglianza tattica telefonica utilizzato dalle forze di polizia e dalle agenzie di intelligence ([[Sigint]]). Funziona ingannando i telefoni cellulari all'interno del suo RAGgio d'azione: il dispositivo simula di essere una torre cellulare (BTS) legittima dell'operatore telefonico, forzando tutti i cellulari nelle vicinanze a connettersi ad esso invece che all'antenna reale (attacco Man-in-the-Middle).

## 📚 Contesto e Definizioni

Il nome deriva dalla sua funzione primaria: catturare l'**IMSI (International Mobile Subscriber Identity)**, il codice univoco di 15 cifre memorizzato nella SIM card che identifica globalmente quell'abboNATO.
*   **Funzione di tracciamento:** Sfruttando la triangolazione del segnale, la polizia può localizzare un latitante con un margine d'errore di pochissimi metri.
*   **Downgrade Attack:** I modelli avanzati forzano il telefono della vittima a disabilitare la crittografia (es. passando dal 4G al 2G non crittografato), permettendo all'operatore di intercettare SMS e chiamate vocali in chiaro.

## 📊 Dati, Tecnologie e Metriche

L'uso prolungato degli IMSI Catcher solleva enormi controversie in tema di [[Privacy]] e [[Quadro giuridico]]. Poiché il dispositivo è "indiscrimiNATO", per localizzare un singolo latitante in una piazza, la polizia intercetta illegalmente gli identificativi di migliaia di cittadini innocenti di passaggio. Gli investigatori [[Osint]] specializzati in infrastrutture rilevano la presenza di IMSI Catcher ostili utilizzando app come Snoopsnitch o analizzando picchi anomali di torri cellulari tramite database aperti (es. OpencelliD o Wigle).

## 🔗 Connessioni e Pattern

- [[Sigint]]
- [[Privacy]]
- [[Quadro giuridico]]
- [[--]]
F/I/H
- [[--]]
