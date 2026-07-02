---
title: "Exif"
tags: ["OSINT", "processed", "exif", "metadati", "imint", "forensics"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Exif

## 🎯 Sintesi Strategica

L'**EXIF (Exchangeable Image File Format)** è lo standard universale che specifica i formati per le immagini e i file sonori utilizzati dalle fotocamere digitali e dagli smartphone. Nell'[[Osint]] e nell'[[Imint]], l'analisi dei dati EXIF è l'equivalente di esaminare il DNA di una fotografia: permette di estrarre [[Metadati]] occulti che la vittima non sapeva nemmeno di aver condiviso, svelando coordinate GPS, orari esatti e tipo di dispositivo utilizzato.

## 📚 Contesto e Definizioni

Quando scatti una foto, lo smartphone non salva solo l'immagine, ma "scrive" invisibilmente nel file una valanga di dati accessori:
1.  **Geotagging:** Latitudine e Longitudine esatte in cui è stata scattata la foto (precisione al metro).
2.  **Timestamp:** Data e ora precisa (indispensabile per smentire un alibi).
3.  **Dati hardware:** Modello del telefono (es. iphone 14 Pro), versione del software, ISO, apertura dell'obiettivo.

## 📊 Dati, Tecnologie e Metriche

Storicamente, l'estrazione degli EXIF tramite tool come Exiftool ha permesso arresti clamorosi (es. l'hacker Higinioochoa, tradito dalla foto del seno della sua fidanzata che conteneva le coordinate GPS della loro casa). Oggi, piattaforme di [[Capitalismo delle piattaforme]] (come Whatsapp, Facebook, Instagram) operano il "Metadata Stripping": quando carichi una foto, cancellano automaticamente gli EXIF per proteggere la [[Privacy]]. Tuttavia, l'analista OSINT cerca le foto inviate tramite canali non sanificati (es. allegati di posta elettronica originali o file caricati su forum del [[Dark web]] o Telegram in formato "File").

## 🔗 Connessioni e Pattern

- [[Metadati]]
- [[Imint]]
- [[Privacy]]
- [[Geoint]]
- [[--]]
F/I/H
- [[--]]
