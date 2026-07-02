---
title: "Ocr"
tags: ["OSINT", "processed", "ocr", "estrazione-dati", "computer-vision"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Ocr

## 🎯 Sintesi Strategica

L'**OCR (Optical Character Recognition)** è la tecnologia informatica che identifica e converte testi presenti all'interno di immagini digitali o documenti scannerizzati in stringhe di testo macchina ricercabili ed elaborabili. Nella pipeline [[Osint]], l'OCR elimina il "Blind Spot" (punto cieco) visivo: permette agli algoritmi di ricerca e all'[[Intelligenza artificiale generativa]] di "leggere" le targhe nei video di Youtube, i manifesti propagandistici su Telegram o i PDF finanziari offuscati (fatture o visure camerali).

## 📚 Contesto e Definizioni

Inizialmente basato sul pattern matching geometrico delle lettere, l'OCR moderno (es. Tesseract OCR o Google Cloud Vision) è potenziato dal [[Deep learning]], permettendo il riconoscimento di testi distorti, scritti a mano, o in lingue con alfabeti non latini (Cirillico, Arabo, Mandarino).

## 📊 Dati, Tecnologie e Metriche

Nelle architetture di [[Automazione]] (come [[n8n]]), il nodo OCR è obbligatorio nel workflow di ingestion: ogni immagine raschiata viene passata all'OCR. Se il tool estrae testo malevolo (es. minacce o indicatori di compromissione), scatta l'alert per l'analista. Senza l'OCR, i Threat Actors potrebbero comunicare apertamente postando screenshot di testo che i motori di indicizzazione classici non rileverebbero.

## 🔗 Connessioni e Pattern

- [[Deep learning]]
- [[Automazione]]
- [[Trattamento dell'output]]
- [[--]]
F/I/H
- [[--]]
