---
title: "Mac address"
tags: ["OSINT", "processed", "mac-address", "hardware", "networking", "forensics"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Mac address

## 🎯 Sintesi Strategica

Il **MAC Address (Media Access Control Address)** è l'identificativo fisico (Hardware) bruciato a livello di fabbrica all'interno della scheda di rete (NIC) di ogni computer, smartphone o router. A differenza dell'[[Indirizzo ip]], che è logico e cambia continuamente quando ci si sposta da una rete all'altra, il MAC Address è concepito per essere un identificatore permanente e inalterabile del dispositivo fisico, fondamentale per la Digital Forensics e il tracciamento fisico.

## 📚 Contesto e Definizioni

L'indirizzo MAC è composto da 48 bit, scritti in esadecimale (es. `00:1A:2B:3C:4D:5E`). La prima metà (OUI - Organizationally Unique Identifier) rivela l'azienda produttrice del chip (es. Apple, Cisco, Intel).
Il MAC Address non viaggia su internet. Se invii un'email da Milano a New York, il tuo IP fa il giro del mondo, ma il tuo MAC Address viaggia solo dal tuo telefono fino al tuo router Wi-Fi domestico e si ferma lì, sostituito dal MAC del router.

## 📊 Dati, Tecnologie e Metriche

Dal punto di vista dell'[[Opsec]], i MAC Address sono un grave rischio di sorveglianza urbana. Camminando in città con il Wi-Fi acceso sul telefono, il dispositivo invia costantemente richieste radio (Probe Requests) contenenti il MAC Address per cercare reti. Centri commerciali e agenzie di intelligence catturano questi segnali per tracciare il movimento delle persone. I moderni OS difendono gli utenti utilizzando il "MAC Randomization", generando un MAC Address falso ([[Spoofing]]) finché non si connettono a una rete fidata.

## 🔗 Connessioni e Pattern

- [[Indirizzo ip]]
- [[Spoofing]]
- [[Opsec]]
- [[--]]
F/I/H
- [[--]]
