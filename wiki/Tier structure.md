---
title: Tier structure
tags:
- OSINT
- processed
- tier-structure
date: '2026-05-15'
status: draft
depth: standard
sources: '1'
tipo: concetto
---

# Tier structure

## 🎯 Sintesi Strategica

La **Tier structure** è un modello analitico che descrive la stratificazione e l'interazione degli attori all'interno di un ecosistema informativo, particolarmente rilevante nell'analisi della [[Disinformazione]]. Questo approccio evidenzia come l'ecosistema disinformativo non sia domiNATO da attori stranieri (la cui influenza è spesso sovrastimata), ma piuttosto da una complessa interazione tra attori domestici: politici istituzionali, media alternativi/partisan, influencer e reti marginali. Il modello tradizionale "bad actors vs. victims" è empiricamente insostenibile, poiché i media mainstream possono involontariamente amplificare le narrative e il debunking non coordiNATO può generare un Effetto Streisand.

## 📚 Contesto e Definizioni

La **Tier structure** offre una cornice per superare il modello semplificato della [[Disinformazione]], che spesso identifica attori malintenzionati (es. troll farms) e cittadini passivi. Questo modello più articolato riconosce la complessità delle dinamiche informative. Studi come quelli di Phillips & Milner (2017) e Marwick & Lewis (2017) dimostrano che i media tradizionali possono amplificare le narrative più dei cosiddetti "troll" e che l'ecosistema è manipolabile "by design" a causa delle logiche delle newsroom e degli algoritmi delle piattaforme. È cruciale distinguere tra lo sfruttamento delle vulnerabilità strutturali dell'informazione e la violazione diretta, riconoscendo che la manipolazione può essere una forma di competenza comunicativa.

## 📊 Dati, Tecnologie e Metriche

L'analisi dell'ecosistema italiano, ad esempio, rivela una chiara stratificazione degli attori:

| Tier | Categoria | Utenti/Stima | Threat |
|---|---|---|---|
| TIER 1 | Politici istituzionali | Meloni 1,8M X; Salvini 1,2M FB; Conte 2,5M FB | Polarizzazione, erosione trust |
| TIER 2 | Media alternativi/partisan | Byoblu 400k YT; L'Indipendente; Vox | Radicalizzazione nicchie |
| TIER 3 | Influencer micro-celebrities | 10-100k followers (engagement alto) | Ponte mainstream-fringe |
| TIER 4 | Reti automatizzate | Bot italiani 100-500 stimati | Astroturfing, Perception hacking |

**Influenza Russa (pre/post 2022):**
L'influenza russa ha subito una significativa contrazione post-2022. Pre-2022, si stimava un budget di €5-10M/anno e circa 50 persone in Italia, con Sputnik e RT che RAGgiungevano centinaia di migliaia di utenti. Post-2022, con la chiusura di Sputnik e RT, il reach diretto è diminuito del 70%, mentre l'influenza opera tramite proxy, RAGgiungendo circa il 30% dei livelli pre-ban attraverso siti web proxy, amplificazione bot e infiltrazione su Telegram.

**Attori Non-Statali:**
Gruppi come Forza Nuova e Casapound hanno visto una marginalizzazione. Il movimento No-vax ha RAGgiunto un picco nel 2021-22 con manifestazioni di decine di migliaia di persone e una forte presenza su Telegram, mantenendo un core di 5-10k. La Cina opera con decine di account Twitter in Italia, focalizzandosi su élite per temi come BRI, Taiwan e Xinjiang.

**Piattaforme Digitali:**
Facebook (35M utenti), Whatsapp (33M, con crittografia che ostacola il monitoraggio OSINT), Telegram (crescita post-COVID) e Tiktok (popolare tra la Gen Z, presenta sfide per il [[Fact-checking]]) sono i principali canali di diffusione.

## 🔍 Analisi Operativa ed Applicazioni OSINT

L'applicazione della Tier structure è fondamentale per l'[[Analisi]] e la comprensione delle "battaglie di narrative" (Battle of Narratives) in eventi critici.

*   **Caso Cutro (26 Feb 2023):** La tragedia ha dimostrato come la verifica dei fatti sulla timeline dei soccorsi sia distinta dall'interpretazione politica ("tempestivo" vs. "ritardato"). L'analisi del frame (Entman) rivela che non si tratta di "vero vs. falso", ma di interpretazioni basate su valori inconciliabili (sicurezza vs. diritti umani).
    *   **Frame del Governo:** Traffico esseri umani, scafisti+ONG pull factor, difesa confini, blocco partenze.
    *   **Frame ONG/Opposizione:** Mancanza SAR, governo ostacola, UE non solidale, diritti internazionali, corridoi umanitari.
    *   **Frame Media:** TRAGedia umanitaria, attribuzione ambigua, shock morale, inchieste giudiziarie.
*   **COVID-19 come Laboratorio di Disinformazione (2020-2023):** Le narrative si sono evolute dall'origine (lab leak, 5G virus) ai lockdown (dittatura sanitaria) e ai vaccini (siero genico, morti da vaccino), coinvolgendo complottisti, estrema destra, medici dissidenti e reti Telegram.
*   **Il Megafono Involontario dei Media:** Il caso "Plandemic" ha illustrato come la copertura mediatica tradizionale, anche se intesa come debunking, possa involontariamente amplificare la disinformazione. Inizialmente con zero visualizzazioni in Italia, la discussione da parte di importanti telegiornali ha portato alla sua traduzione e a milioni di visualizzazioni.
*   **Fact-Checking in Italia:** Organizzazioni come Pagella Politica, Facta.news, Open e Butac.it svolgono un ruolo cruciale. Tuttavia, affrontano limiti strutturali: reach asimmetrico (il fact-check ha 10-100x meno reach della bufala), backfire effect, bias percepito e sostenibilità economica.
*   **Deficit Democratico vs. Deficit Cognitivo:** La disinformazione è spesso un sintomo, non la causa, di vulnerabilità più profonde. La lettura "popolo inganNATO" (élite) suggerisce soluzioni paternalistiche (educazione/censura), mentre la lettura "élite sorde" (Mudde & Kaltwasser, 2017) evidenzia come i populisti intercettino reali lamentele. La Russia, ad esempio, sfrutta l'euroscetticismo preesistente, non lo crea.

## 🔮 Lacune Informative e Prossimi Passi

1.  **Dati reali sui proxy russi post-2022:** Mancano dati pubblici e verificabili indipendentemente da fonti investigative o di intelligence (DIS/Copasir).
2.  **Bot italiani:** Sono meno studiati rispetto a contesti come gli USA; non esistono dataset quantitativi completi e disponibili pubblicamente.
3.  **Misurazione dell'impatto:** Le stime di reach e engagement sono spesso non verificate indipendentemente, rendendo difficile valutare l'efficacia reale delle campagne di disinformazione.
4.  **Piattaforme emergenti (2025):** Tiktok e Telegram sono in rapida evoluzione; è necessaria una verifica continua della disponibilità e dell'efficacia degli strumenti di monitoraggio per queste piattaforme.

## 🔗 Connessioni e Pattern

- [[Applicazioni osint]]
- [[Crittografia]]
- [[Disinformazione]]
- [[Fact-checking]]
- [[Laboratorio]]
- [[Radicalizzazione]]


- [[--]]
F/I/H
- [[--]]
