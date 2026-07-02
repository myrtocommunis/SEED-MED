---
title: "Trojan"
tags: ["OSINT", "processed", "trojan", "malware", "infezione", "ingegneria-sociale"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Trojan

## 🎯 Sintesi Strategica

Il **Trojan (o Cavallo di Troia)** è una tipologia di [[Malware]] che si nasconde all'interno di un software apparentemente legittimo e innocuo (es. un aggiornamento di sistema, un gioco piratato o un documento PDF), ingannando l'utente affinché lo esegua volontariamente. A differenza dei Worm, che si auto-replicano e si diffondono attivamente sulla rete, il Trojan richiede sempre l'interazione umana e sfrutta l'[[Ingegneria sociale]] per superare il perimetro difensivo aziendale.

## 📚 Contesto e Definizioni

Nel panorama del Cybercrime, i Trojan sono solitamente il vettore di "Fase 1" (il portatore sano) in una [[Cyber kill chain]].
Le varianti moderne più pericolose sono i **RAT (Remote Access Trojan)**. Una volta che l'utente clicca l'allegato maligno in una mail di [[Attacco di phishing]], il RAT apre una connessione occulta (Backdoor) verso il server di [[Command and control]] dell'hacker, garantendo il controllo remoto completo e in tempo reale del computer infetto.

## 📊 Dati, Tecnologie e Metriche

I RAT permettono all'hacker di scaricare e installare moduli aggiuntivi: possono attivare silenziosamente la webcam, installare un [[Keylogger]] per rubare password bancarie o distribuire lateralmente un [[Ransomware]] sull'intera rete aziendale. Nella [[Cyber threat intelligence]], mappare la firma (Regole [[Yara]]) di noti Trojan bancari storici (come Emotet o Trickbot) è essenziale per disinnescare l'infezione prima che il Threat Actor riesca a monetizzare la compromissione.

## 🔗 Connessioni e Pattern

- [[Malware]]
- [[Attacco di phishing]]
- [[Ingegneria sociale]]
- [[Cyber kill chain]]
- [[--]]
F/I/H
- [[--]]
