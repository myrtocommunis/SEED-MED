---
title: "Nota metodologica"
tags: ["OSINT", "processed", "metodologia", "standard", "qualità", "reportistica"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Nota metodologica

## 🎯 Sintesi Strategica

La **Nota Metodologica** è una sezione obbligatoria nei report di Intelligence e [[Osint]] di alto livello (Strategic Intelligence). È una dichiarazione di trasparenza in cui l'analista descrive in modo esplicito gli strumenti, le tecniche, i database utilizzati, i vincoli temporali e le limitazioni inerenti all'indagine. Il suo scopo è garantire che le conclusioni del report siano scientificamente verificabili, replicabili e prive di manomissioni metodologiche.

## 📚 Contesto e Definizioni

In ambito giuridico o governativo, un report senza Nota Metodologica è considerato "diceria" (Hearsay). La nota deve dichiarare:
*   **Perimetro:** Quali piattaforme sono state raschiate ([[Scraping]]) e quali escluse.
*   **Strumenti:** L'uso di specifici software commerciali (es. Maltego) o modelli [[Llm]] per l'analisi del testo.
*   **Gestione dell'Incertezza:** La dichiarazione esplicita del Margine di Errore (Confidence Level). L'analista ammette: "Valutiamo l'attribuzione di questo attacco con grado di confidenza Medio, perché mancano dati dai log dei server russi".

## 📊 Dati, Tecnologie e Metriche

L'assenza di trasparenza metodologica è la prima vulnerabilità sfruttabile da una squadra di contro-analisi ([[Red team]]). Documentare l'uso di operatori di ricerca avanzati ([[Google dorks]]) o il salvataggio crittografato della prova (Hashing della pagina web via [[Archiviazione forense]]) protegge l'integrità del prodotto di intelligence anche se il sito originale dovesse essere oscurato o rimosso il giorno successivo.

## 🔗 Connessioni e Pattern

- [[Archiviazione forense]]
- [[Red team]]
- [[Google dorks]]
- [[Scraping]]
- [[--]]
F/I/H
- [[--]]
