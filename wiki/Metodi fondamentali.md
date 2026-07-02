---
title: Metodi fondamentali
tags:
  - osint
  - methodology
  - framework
status: NEW_HEALED
tipo: sintesi
depth: standard
date: "2026-05-16"

---

# Metodi Fondamentali e Ciclo OSINT

I metodi fondamentali dell'OSINT si strutturano attorno a una rigorosa tassonomia dell'informazione, definita dagli standard [[NATO]] e dal [[Berkeley Protocol]]. L'elaborazione procede per stadi: dai **Data** (fatti grezzi), all'**Information** (dati interpretati), fino al **Knowledge** (informazione contestualizzata), culminando nella **Validated OSINT**, ossia l'intelligence verificata tramite incroci con altre fonti.

### Il Ciclo OSINT

La metodologia si basa su un ciclo a sei fasi interdipendenti:
1. **Pianificazione e Direzione**: Definizione dei fabbisogni informativi.
2. **Raccolta**: Estrazione da fonti aperte (integrata da HUMINT, SIGINT, ecc.).
3. **Elaborazione**: Processamento e raffinamento dei dati grezzi.
4. **Analisi**: Interpretazione strategica del dato.
5. **Produzione**: Creazione del dossier analitico.
6. **Disseminazione e Feedback**: Distribuzione del prodotto e iterazione in base al riscontro.

### Metodi Investigativi

Un concetto cardine è l'analisi della **Digital Footprint** (impronta digitale), divisa in componente *attiva* (rilasciata volontariamente, come post social) e *passiva* (metadati, registri server). La tecnica del **Pivoting** sfrutta identificatori univoci (selectors come email, username, numeri di telefono) per transitare da un dominio all'altro, ricostruendo l'identità del target (Targeting Schema: chi è, cosa fa, cosa usa).
Strumenti fondamentali includono tool di *People Search* (Pipl, Epieos), verifica *Breach* (Haveibeenpwned), e piattaforme *Corporate* (Opencorporates).

## 🔗 Connessioni e Pattern

- [[Ciclo OODA]]
- [[Tassonomia dei tools]]
- [[Trattamento dell'output]]
- [[Sicurezza nazionale]]
- [[Tecniche di analisi strutturata]]

- [[-- F/I/H ---]]
- [[**Fatti (F)**: Il ciclo OSINT si compone di 6 fasi canoniche (Pianificazione, Raccolta, Elaborazione, Analisi, Produzione, Disseminazione) e utilizza il pivoting sui selector come tecnica d'indagine primaria.]]
- [[**Interpretazione (I)**: La formalizzazione del metodo (Targeting Schema, distinzione tra active/passive footprint) è essenziale per differenziare l'OSINT istituzionale dalla semplice "ricerca web".]]
- [[**Ipotesi (H)**: L'integrazione di LLM nelle prime 3 fasi del ciclo accelererà la transizione dalla raccolta manuale alla generazione di ipotisi, ma renderà l'Analisi umana (fase 4) ancora più critica per la validazione.]]
