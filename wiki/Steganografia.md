---
title: "Steganografia"
tags: ["OSINT", "processed", "steganografia", "crittografia", "opsec", "occultamento"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Steganografia

## 🎯 Sintesi Strategica

La **Steganografia** (dal greco "Scrittura nascosta") è la tecnica che consente di nascondere un file, un'immagine, o un messaggio segreto *all'interno* di un altro file (vettore) apparentemente innocuo. A differenza della crittografia, che nasconde il *contenuto* del messaggio rendendolo illeggibile, la steganografia nasconde l'*esistenza stessa* del messaggio, permettendo ai Threat Actor di comunicare in chiaro sotto gli occhi degli analisti di rete senza destare sospetti.

## 📚 Contesto e Definizioni

La tecnica digitale più comune è la LSB (Least Significant Bit). Se un'immagine innocua del formato BMP o PNG è composta da milioni di pixel colorati, il software steganografico (es. Openstego o Steghide) altera matematicamente l'ultimo bit (il meno significativo) di ogni pixel per inserirvi le lettere del messaggio segreto. All'occhio umano e ai filtri antispam, l'immagine risulterà identica all'originale.

## 📊 Dati, Tecnologie e Metriche

Nell'ecosistema della [[Cyber threat intelligence]], i gruppi [[Apt]] e i distributori di [[Malware]] usano la steganografia per nascondere porzioni di codice virale all'interno di loghi aziendali innocui scaricati durante la fase di infezione, bypassando le difese perimetrali (Stegomalware). L'[[Osint]] la contrasta con la **Steganalisi**: utilizzando script che comparano algoritmicamente l'immagine sospetta (estratta dai social media) con l'immagine originale immacolata, cercando le firme statistiche dell'alterazione.

## 🔗 Connessioni e Pattern

- [[Crittografia asimmetrica]]
- [[Malware]]
- [[Apt]]
- [[Opsec]]
- [[--]]
F/I/H
- [[--]]
