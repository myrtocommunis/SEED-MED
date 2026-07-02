---
title: "Struttura exif"
tags: ["OSINT", "processed", "exif", "imint", "metadati", "standard"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Struttura exif

## 🎯 Sintesi Strategica

La **Struttura EXIF (Exchangeable Image File Format)** definisce tecnicamente il modo in cui i tag dei [[Metadati]] vengono registrati, codificati e incorporati all'interno dei file di immagine (tipicamente JPEG e TIFF) e dei file audio (WAV). Comprendere l'architettura esadecimale (o i Tag EXIF standard) è necessario per l'analista di Digital Forensics quando indaga su file corrotti, manipolati o sottoposti a tentativi di Evasione Forense, dove l'estrazione automatica via software fallisce.

## 📚 Contesto e Definizioni

La Struttura EXIF è organizzata in "IFD" (Image File Directories).
I Tag più rilevanti dal punto di vista investigativo includono:
*   `0x010F` (Make): Produttore della fotocamera (es. Apple).
*   `0x0110` (Model): Modello (es. iphone 14).
*   `0x8825` (GPSInfo): Punta alla directory contenente latitudine, longitudine, altitudine e velocità del dispositivo al momento dello scatto (il Santo Graal della [[Geoint]]).
*   `0x0131` (Software): Se la foto mostra `Adobe Photoshop 2024` invece del firmware originale della macchina fotografica, è un indicatore primario di manipolazione o fotoritocco.

## 📊 Dati, Tecnologie e Metriche

Quando un analista affronta una foto sospetta di essere un [[Deepfake]] o manipolata per scopi di [[Disinformazione]], la Struttura EXIF viene comparata statisticamente con la PRNU (Photo Response Non-Uniformity), ovvero l'impronta digitale invisibile lasciata dai difetti fisici del sensore della fotocamera sull'immagine. Se i dati EXIF dicono "iphone" ma la struttura PRNU appartiene a una fotocamera Canon, la prova viene invalidata in tribunale.

## 🔗 Connessioni e Pattern

- [[Exif]]
- [[Metadati]]
- [[Geoint]]
- [[Disinformazione]]
- [[--]]
F/I/H
- [[--]]
