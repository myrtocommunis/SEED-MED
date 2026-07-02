---
title: Strumenti operativi
tags:
  - osint
  - disinformazione
  - fimi
  - toolkit
status: NEW_HEALED
tipo: sintesi
depth: standard
date: "2026-05-16"

---

# Strumenti Operativi per l'Analisi della Disinformazione

L'analisi OSINT avanzata in ambito di manipolazione informativa e Foreign Information Manipulation & Interference (FIMI) si avvale di una suite di strumenti operativi categorizzati per presidiare tutte le fasi del ciclo intelligence, dall'acquisizione all'analisi semantica e strutturale.

### Classificazione degli Strumenti

1. **Contesto e Dottrina**: Strumenti come le direttive EEAS Counter FIMI o la BBC Media Guide permettono di mappare l'ecosistema mediatico target, riconoscendo le minacce dominanti.
2. **Analisi Fonti**: Tool come *Media Bias/Fact Check* o l'interrogazione DNS/WHOIS identificano il posizionamento politico e l'attribuzione tecnica dell'infrastruttura (host e registrants).
3. **Verifica e Content Laundering**: Sistemi come l'*Information Laundromat* (ASD) rilevano pattern di distribuzione di contenuti illeciti. Misurano similitudini tecniche, condivisione di testo e cross-domain posting per evidenziare reti coordinate. Database come il DBKF velocizzano la verifica.
4. **Monitoraggio Piattaforme**: Cruscotti come l'*Hamilton 2.0 Dashboard* monitorano account affiliati a stati avversari, pur non implicando automaticamente che ogni contenuto sia falso. *Meta Ads Library* aiuta a tracciare sponsorizzazioni statali occulte. Su ecosistemi chiusi come Telegram, si supplisce all'assenza di API tramite tool come *Telegago* e *TGStat*.
5. **Classificazione**: Il framework *DISARM* fornisce un linguaggio comune e strutturato delle TTPs (Tattiche, Tecniche e Procedure) usate nelle campagne di disinformazione, parallelamente all'ATT&CK nel dominio cyber.
6. **Archivio e Disseminazione**: Organismi quali EDMO o EUvsdisinfo costituiscono l'archivio storico essenziale per identificare recidive narrative e modus operandi consolidati.

## 🔗 Connessioni e Pattern

- [[Disinformazione]]
- [[Tassonomia dei tools]]
- [[Ecosistema disinformativo italiano]]
- [[Foreign Information Manipulation and Interference]]

- [[-- F/I/H ---]]
- [[**Fatti (F)**: L'architettura OSINT per la disinformazione unisce attribuzione tecnica (es. WHOIS, DNS) e monitoRAGgio narrativo (es. Telegram Analytics, Hamilton 2.0). Il framework DISARM standardizza il linguaggio analitico.]]
- [[**Interpretazione (I)**: La complessità della FIMI obbliga l'analista a operare su una triplice matrice: verificare il contenuto, investigare l'infrastruttura di distribuzione e comprendere l'intento strategico, incrociando i dati di "content laundering" per svelare network non dichiarati.]]
- [[**Ipotesi (H)**: Con la chiusura progressiva delle API da parte delle piattaforme Big Tech (X, Meta), gli strumenti OSINT per la FIMI dovranno necessariamente basarsi sullo scraping decentralizzato (edge computing) e su inferenze di rete tramite AI, piuttosto che su query dirette.]]
