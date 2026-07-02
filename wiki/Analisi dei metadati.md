---
title: "Analisi dei metadati"
tags: ["OSINT", "processed", "metadati", "forensics", "analisi", "privacy"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Analisi dei metadati

## 🎯 Sintesi Strategica

L'**Analisi dei Metadati** è il processo di estrazione e investigazione dei "dati sui dati" nascosti all'interno di file digitali (documenti Word, PDF, immagini). Se il contenuto di un documento è il "messaggio", il metadato è la "busta" che rivela chi ha spedito il messaggio, quando, da dove e con quale software. Nella [[Cyber threat intelligence]] e nell'[[Osint]], i metadati sono spesso più incriminanti e utili del contenuto del file stesso.

## 📚 Contesto e Definizioni

La fallacia fatale dei criminali inesperti (o degli impiegati disattenti) è credere che salvare un documento Word come PDF cancelli la loro identità.
Un tool come *Exiftool* (o *FOCA*) estrae l'anima del documento:
*   **Nome Utente dell'OS:** Rivela spesso il vero nome del criminale che ha compilato il documento (es. `Author: Giovanni.Rossi_PC`).
*   **Software usato:** Rivela la versione esatta di Microsoft Word, permettendo di pianificare attacchi mirati.
*   **Timestamp di creazione e modifica:** Permette di ricostruire la cronologia esatta (Timeline) di una frode finanziaria.

## 📊 Dati, Tecnologie e Metriche

L'Analisi dei Metadati è la rovina dei finti [[Whistleblower]] e delle campagne di [[Disinformazione]]. Se un governo ostile pubblica un documento in PDF accusando un politico occidentale di corruzione, l'analista OSINT estrae i metadati e scopre che il documento (che dovrebbe risalire al 2018) è stato in realtà creato e modificato in un fuso orario di Mosca solo 48 ore prima della pubblicazione, smascherando istantaneamente il falso storico (Forgery).

## 🔗 Connessioni e Pattern

- [[Metadati]]
- [[Exif]]
- [[Disinformazione]]
- [[Whistleblower]]
- [[--]]
F/I/H
- [[--]]
