---
title: "Swatting"
tags: ["OSINT", "processed", "swatting", "harassment", "cybercrime", "socmint"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Swatting

## 🎯 Sintesi Strategica

Lo **Swatting** è una forma estrema e letale di molestia cibernetica. Consiste nell'effettuare una falsa segnalazione telefonica ai servizi di emergenza (come il 911 negli Stati Uniti) denunciando una situazione di gravissima crisi in corso (es. un ostaggio armato o una bomba) presso l'indirizzo della vittima. Lo scopo è provocare l'irruzione immediata delle squadre d'assalto armate della polizia (SWAT) in casa del bersaglio ignaro.

## 📚 Contesto e Definizioni

Lo Swatting è il culmine violento del [[Doxing]].
La catena d'attacco richiede un pesante utilizzo dell'[[Osint]]:
1.  L'hacker identifica il vero nome e cognome della vittima (spesso uno streamer su Twitch o un politico) tramite [[Socmint]].
2.  Utilizza database pubblici o leakati ([[Data breach]]) o servizi di [[Data broker]] per trovare l'esatto indirizzo di residenza della vittima.
3.  Utilizza lo [[Spoofing]] telefonico (o proxy VoIP) per chiamare la polizia camuffando la propria voce e mascherando la chiamata come se provenisse dall'interno dell'abitazione della vittima.

## 📊 Dati, Tecnologie e Metriche

Considerato un vero e proprio tentato omicidio (in diversi casi la polizia ha aperto il fuoco contro civili innocenti), le autorità hanno incrementato i database di [[Cyber threat intelligence]] per incrociare i falsi allarmi e arrestare i "Callers". I bersagli ad alto rischio prevengono lo swatting inserendo preventivamente il proprio indirizzo in registri speciali (Anti-Swatting Registry) della polizia locale, allertando le autorità che se ricevono una chiamata da quella specifica casa, è molto probabilmente un falso positivo ostile, richiedendo una verifica (Verification Call) prima di inviare le truppe.

## 🔗 Connessioni e Pattern

- [[Doxing]]
- [[Spoofing]]
- [[Socmint]]
- [[Data breach]]
- [[--]]
F/I/H
- [[--]]
