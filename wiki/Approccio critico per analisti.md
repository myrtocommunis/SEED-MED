---
title: Approccio critico per analisti
tags:
- OSINT
- processed
- approccio-critico-per-analisti
date: '2026-05-15'
status: draft
depth: standard
sources: '1'
tipo: concetto
---

# Approccio critico per analisti

## 🎯 Sintesi Strategica

Un approccio critico alla [[Disinformazione]] rifiuta il modello binario "buoni vs cattivi", privilegiando una mappatura dei campi di potere basata sulle teorie di Bourdieu, Foucault ed Entman. Il nucleo argomentativo sostiene che la "disinformation disorder" sia una caratteristica sistemica del [[Capitalismo delle piattaforme]], piuttosto che un'aberrazione. L'intelligence è chiamata a distinguere tra minacce allo Stato e minacce al governo in carica, e a mappare le vulnerabilità domestiche sfruttate, non solo le minacce esterne.

## 📚 Contesto e Definizioni

L'approccio si articola attraverso l'esplorazione di concetti chiave, dalla teoria alla pratica operativa:
1.  **Regimi di verità e potere epistemico**: Analisi della tassonomia di Wardle & Derakhshan (Council of Europe 2017) e dei limiti dell'intento come criterio definitorio.
2.  **Ecosistema disinformativo**: Struttura a livelli (politici, media alternativi, influencer, bot) e dinamiche degli attori statali e non-statali (es. Russia, Cina, movimenti di estrema destra, no-vax), con la matrice di minaccia definita come Capacità × Intent × Opportunità.
3.  **Tecniche [[Osint]] per l'[[Analisi]]**: Utilizzo del framework di Entman (4 funzioni) e strumenti per l'analisi di rete.
4.  **Architettura delle piattaforme e [[Algoritmi]]**: Concetti come l'Actor-Network Theory (Latour) e la "algorithmic governmentality", con riferimento al [[Diritto digitale|DSA (Digital Services Act)]] (Reg. UE 2022/2065).
5.  **Verifica dei contenuti**: Metodologie come la ricerca inversa di immagini, geolocalizzazione, rilevamento di deepfake e la metodologia SIFT.
6.  **[[Bias cognitivo]] nell'analisi**: Esplorazione dei principali bias (es. [[Confirmation bias]], [[Anchoring bias]]) e contromisure come l'Analysis of Competing Hypotheses (ACH) e il red teaming.
7.  **Casi studio comparati**: Analisi di eventi come MH17, Cambridge Analytica, Macron Leaks, Secondary Infektion e l'infodemia COVID.

## 📊 Dati, Tecnologie e Metriche

Alcuni dati e metriche rilevanti per il contesto italiano e internazionale della [[Disinformazione]]:

| Indicatore | Valore |
|---|---|
| Utenti Facebook IT | 35M (60% popolazione) |
| Utenti Whatsapp IT | 33M |
| Sputnik reach pre-2022 | 100-300k unique/mese |
| Budget operativo Russia (Italia) | €5-10M/anno (stima) |
| Reach post-ban Sputnik/RT | -70% diretto, ~30% indiretto via proxy |
| No-vax peak 2021-2022 | Manifestazioni 10-50k, ~200k Telegram subscribers |
| No-vax core 2023-2024 | 5-10k attivisti |
| Cutro vittime | 94 confermati (35 minori) |
| Attori estrema destra IT | Forza Nuova (1-2k core, sciolta 2021), Casapound (~500) |

**Tecnologie per la verifica [[Osint]] (post-API era):**
*   **Scraper**: Apify (costo stimato €50-200/mese).
*   **Messaggistica**: Telethon per Telegram.
*   **Video sharing**: Zeeschuimer per Tiktok.
*   **Verifica immagini**: Google Reverse Image Search, Yandex, Tineye, EXIF metadata, Error Level Analysis (ELA).
*   **Geolocalizzazione**: Analisi delle ombre (Suncalc).
*   **Deepfake detection**: Indicatori specifici.

## 🔍 Analisi Operativa ed Applicazioni OSINT

### 1. Il Framework Critico come Mappa dei Campi di Potere

L'applicazione della teoria di Bourdieu al campo informativo permette di mappare gli attori in base al loro capitale simbolico:
*   **Campo**: Spazio di lotta per credibilità e autorità.
*   **Dominanti**: Media tradizionali (RAI, Corriere, Repubblica) – basso rischio per la stabilità.
*   **Sfidanti istituzionali**: Figure politiche con ampia presenza sui social (es. Meloni, Salvini, Conte) – rischio medio di polarizzazione.
*   **Marginali**: Canali Telegram no-vax, blog sovranisti – alto rischio di radicalizzazione.
La "doppia posizione" di alcuni partiti (dominanti politicamente ma sfidanti mediaticamente) è cruciale per comprendere le loro strategie comunicative.

### 2. Il Problema Epistemico del "Chi Definisce?"

La tassonomia standard (misinformazione/disinformazione/malinformazione) presuppone un ordine informativo consensuale. Tuttavia, la definizione di "verità" o "disinformazione" è spesso influenzata dal posizionamento politico. L'approccio suggerisce di focalizzarsi sull'**impatto** (misurabile) piuttosto che sull'**intento** (inferito) per valutare la [[Disinformazione]].

### 3. Le Vulnerabilità Domestiche come Target Primario

Gli attori stranieri non creano divisioni, ma sfruttano vulnerabilità preesistenti. L'euroscetticismo o la sfiducia nelle istituzioni, ad esempio, possono essere amplificati. L'analisi per gli [[Osint]] analyst deve quindi includere le vulnerabilità interne, oltre alle minacce esterne.

### 4. I 6 [[Bias cognitivo]] Critici per l'[[Osint]]

*   **[[Confirmation bias]]**: Tendenza a selezionare fonti che confermano le proprie ipotesi. Contromisura: ACH, "devil's advocate".
*   **[[Anchoring bias]]**: La prima informazione ricevuta influenza le analisi successive. Contromisura: "reset" iniziale.
*   **[[Availability heuristic]]**: Sovravalutazione di eventi recenti o drammatici. Contromisura: analisi del "base rate".
*   **Attribution error**: Attribuire malevolenza dove potrebbe esserci incompetenza. Contromisura: Rasoio di Hanlon, analisi strutturali.
*   **[[Groupthink]]**: Conformismo del gruppo che porta a decisioni errate (es. Iraq WMD). Contromisura: analisi parallela, red team.
*   **[[Mirror imaging]]**: Assumere che l'avversario pensi come noi. Contromisura: studio approfondito dell'avversario.

### 5. La Verifica [[Osint]] nell'Era Post-API

Con la restrizione dell'accesso alle API delle piattaforme (es. Twitter, Crowdtangle), gli strumenti [[Osint]] tradizionali sono compromessi. Si propongono soluzioni alternative come scraper dedicati e strumenti specifici per piattaforme come Telegram e Tiktok. La verifica deve essere multimodale, includendo analisi di immagini (reverse image search, EXIF, ELA), geolocalizzazione video e indicatori di deepfake.

## 🔮 Lacune Informative e Prossimi Passi

1.  **Dati reali italiani sulla proxy russa**: Necessità di verificare i dati DIS/Copasir attraverso fonti pubbliche, leak o reportage investigativi.
2.  **Metriche di engagement**: I numeri di follower/reach sono stime. È necessario incrociare con dati pubblici delle piattaforme o dataset accademici per una maggiore accuratezza.
3.  **Evoluzione dei movimenti**: Aggiornare l'analisi con nuovi movimenti emergenti (es. anti-15min cities, anti-CBDC) e dati aggiornati al 2025.
4.  **Enforcement del [[Diritto digitale|DSA (Digital Services Act)]]**: Monitorare le azioni di enforcement e le sanzioni applicate.

**Fonti da verificare per completezza:**
*   Dati reali DIS/Copasir sulle operazioni russe in Italia.
*   Dataset accademici sull'engagement italiano con la [[Disinformazione]] (2023-2025).
*   Status attuale dei siti proxy post-2024.

## 🔗 Connessioni e Pattern

- [[Algoritmi]]
- [[Analysis of competing hypotheses]]
- [[Architettura delle piattaforme]]
- [[Capitalismo delle piattaforme]]
- [[Disinformazione]]
- [[Osint]]


- [[--]]
F/I/H
- [[--]]
