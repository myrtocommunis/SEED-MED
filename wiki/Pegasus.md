---
title: "Pegasus"
tags: ["OSINT", "processed", "pegasus", "spyware", "nso-group", "zero-click"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "3"
tipo: "concetto"
---

# Pegasus

## 🎯 Sintesi Strategica

**Pegasus** è il più famigerato e sofisticato software di spionaggio (Spyware) di livello militare al mondo, sviluppato dall'azienda israeliana NSO Group. Classificato legalmente come un'arma cibernetica, NSO dichiara di venderlo esclusivamente a governi e agenzie di intelligence statali per la lotta al terrorismo e ai cartelli della droga. Tuttavia, inchieste internazionali ([[Bellingcat]], Amnesty International) hanno dimostrato l'uso sistematico di Pegasus da parte di regimi autoritari per infettare illegalmente giornalisti, dissidenti e oppositori politici.

## 📚 Contesto e Definizioni

A differenza dei [[Malware]] comuni che richiedono un'interazione della vittima (es. un [[Attacco di phishing]] dove devi cliccare un link), le versioni moderne di Pegasus operano tramite vulnerabilità **Zero-Click** (sfruttando bug [[Zero-day]] in imessage, Whatsapp o Facetime). Il telefono della vittima viene compromesso istantaneamente e silenziosamente, senza che l'utente debba toccare lo schermo e senza lasciare tracce visibili o notifiche.

## 📊 Dati, Tecnologie e Metriche

Una volta installato, Pegasus garantisce il controllo in "God-Mode" del dispositivo (iOS o Android):
1. Estrae messaggi crittografati end-to-end (Signal, Whatsapp) *prima* che vengano crittografati dallo schermo.
2. Attiva in remoto microfono e fotocamera per eseguire sorveglianza ambientale continua ([[Sigint]] tattica).
3. Estrae costantemente la cronologia GPS per fornire la [[Geoint]] esatta del bersaglio.

## 🔗 Connessioni e Pattern

- [[Zero-day]]
- [[Sigint]]
- [[Bellingcat]]
- [[Sicurezza nazionale]]
- [[--]]
F/I/H
- [[--]]
