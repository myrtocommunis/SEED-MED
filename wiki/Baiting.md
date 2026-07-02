---
title: "Baiting"
tags: ["OSINT", "processed", "baiting", "ingegneria-sociale", "red-team", "malware"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Baiting

## 🎯 Sintesi Strategica

Il **Baiting (Adescamento)** è una tecnica insidiosa di [[Ingegneria sociale]] che sfrutta la curiosità umana o l'avidità della vittima. Consiste nel lasciare "un'esca" (Bait) infetta – sia fisica che digitale – in un luogo strategico, aspettando che sia la vittima stessa, di sua spontanea volontà, ad innescare l'attacco, facilitando l'ingresso in reti altamente protette dove l'attacco remoto fallirebbe.

## 📚 Contesto e Definizioni

La variante più celebre (impiegata storicamente anche nell'attacco [[Guerra cibernetica]] di Stuxnet) è l'**USB Drop Attack**.
Il [[Red team]] o l'hacker prende alcune chiavette USB, ci applica etichette attraenti come "Salari Dirigenti 2026" o "Licenziamenti", e le lascia (es. tramite un [[Dead drop]]) nei bagni o nel parcheggio dell'azienda bersaglio. L'attacco fa leva sul fatto che il dipendente medio, morso dalla curiosità, inserirà la chiavetta nel computer dell'ufficio per guardarne il contenuto.

## 📊 Dati, Tecnologie e Metriche

Appena inserita, l'USB esegue silenziosamente un [[Trojan]] o un payload di tipo "Rubber Ducky" (una chiavetta che finge di essere una tastiera, digitando migliaia di comandi dannosi in pochi secondi). Il Baiting scavalca tutti i firewall di miliardi di dollari posti a protezione del perimetro aziendale, perché l'[[Insider threat]] involontario (il dipendente) ha portato la minaccia fisicamente oltre le mura. Il [[Blue team]] contrasta questa tecnica disabilitando fisicamente le porte USB o bloccando l'Auto-Run via policy di dominio.

## 🔗 Connessioni e Pattern

- [[Ingegneria sociale]]
- [[Red team]]
- [[Insider threat]]
- [[Dead drop]]
- [[--]]
F/I/H
- [[--]]
