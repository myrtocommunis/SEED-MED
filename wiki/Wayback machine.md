---
title: "Wayback machine"
tags: ["OSINT", "processed", "wayback", "archiviazione", "preservation"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Wayback machine

## 🎯 Sintesi Strategica

La **Wayback Machine** (gestita dall'Internet Archive) è l'infrastruttura di conservazione storica di internet. Esegue continuamente il crawling e lo snapshot (istantanea) di miliardi di pagine web. Nell'ambito [[Osint]], è lo strumento forense fondamentale per la fase di Ricostruzione Storica: permette all'analista di visualizzare una pagina web, un tweet o un sito aziendale esattamente come appariva in una determinata data del passato, anche se l'autore originale ha successivamente cancellato o modificato il contenuto (Data Destruction).

## 📚 Contesto e Definizioni

Quando un Threat Actor tenta di cancellare le proprie tracce (es. un politico che rimuove un tweet imbarazzante o un gruppo terroristico che chiude il sito di reclutamento), i crawler dell'Archive spesso hanno già congelato la pagina. L'uso della Wayback Machine assicura la **Catena di Custodia**: a differenza di uno screenshot locale (facilmente falsificabile con Photoshop), uno snapshot dell'Internet Archive è ospitato da terze parti e universalmente riconosciuto come prova forense in tribunale.

## 📊 Dati, Tecnologie e Metriche

Gli investigatori non si limitano a consultare gli archivi passati. Durante la fase di [[Raccolta]] di un'indagine in corso, un analista [[Osint]] professionista utilizza le estensioni o le [[Api]] dell'Internet Archive (Save Page Now) per forzare il congelamento immediato di una pagina bersaglio *prima* che l'avversario possa accorgersi di essere sotto indagine e oscurare il sito.

## 🔗 Connessioni e Pattern

- [[Raccolta]]
- [[Fact-checking]]
- [[Osint]]
- [[--]]
F/I/H
- [[--]]
