---
title: "Metadati"
tags: ["OSINT", "processed", "metadati", "exif", "forensics"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "3"
tipo: "concetto"
---

# Metadati

## 🎯 Sintesi Strategica

I **Metadati** sono letteralmente "i dati sui dati". In ambito forense e [[Osint]], costituiscono spesso l'evidenza decisiva (Smoking Gun) perché documentano il *quando*, il *come* e il *chi* di un file digitale, invisibili all'utente comune. Analizzare un documento o una fotografia senza estrarne i metadati equivale a esaminare una scena del crimine senza rilevare le impronte digitali.

## 📚 Contesto e Definizioni

Si dividono per estensione del file:
1.  **EXIF (Exchangeable Image File Format):** Incorporati in JPG/TIFF. Contengono marca e modello della fotocamera, coordinate GPS esatte (se attivate dallo smartphone), data di scatto originale e software di modifica (Photoshop).
2.  **Metadati Documentali (PDF, DOCX):** Contengono l'autore (spesso l'account utente di Windows del criminale), il software di creazione, le revisioni nascoste e il tempo totale di editing.

## 📊 Dati, Tecnologie e Metriche

Sebbene vitali, soffrono di due criticità (che obbligano all'adozione dell'[[Opsec]] passiva):
*   **Stripping delle Piattaforme:** Social network come X, Facebook o Whatsapp cancellano (strippano) deliberatamente tutti i metadati EXIF durante l'upload per privacy e compressione. I metadati vanno cercati in file originali scaricati dal [[Dark web]], forum primitivi, o documenti allegati in email/Telegram.
*   **Manipolazione:** I metadati non sono prove incorruttibili. Possono essere alterati facilmente tramite stringhe di comando (es. `Exiftool`) per disseminare false piste investigative (False Flag).

## 🔗 Connessioni e Pattern

- [[Opsec]]
- [[Geoint]]
- [[Fact-checking]]
- [[--]]
F/I/H
- [[--]]
