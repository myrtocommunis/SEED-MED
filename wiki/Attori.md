---
title: Attori
tags:
- OSINT
- processed
- attori
date: '2026-05-15'
status: draft
depth: standard
sources: '1'
tipo: concetto
---

# Attori

## 🎯 Sintesi Strategica

Nel contesto dell'ecosistema informativo, gli **Attori** sono entità individuali o collettive che influenzano la produzione, la diffusione e la percezione delle informazioni. L'analisi OSINT rivela che l'ecosistema disinformativo italiano, ad esempio, non è primariamente domiNATO da attori stranieri, ma da una complessa interazione di soggetti domestici, inclusi politici istituzionali, media alternativi/partisan, influencer e reti marginali. L'influenza di attori esterni, come la Russia post-2022, si è significativamente ridotta, operando ora prevalentemente tramite proxy. Il modello semplificato di "attori malintenzionati contro vittime passive" è empiricamente insostenibile, poiché i media tradizionali possono amplificare i contenuti più dei cosiddetti "troll", e le attività di debunking possono inavvertitamente aumentare la portata della [[Disinformazione]] (effetto Streisand).

## 📚 Contesto e Definizioni

Il concetto di "Attori" nell'analisi OSINT si riferisce a qualsiasi entità capace di generare, manipolare o diffondere narrazioni e informazioni, con o senza intenti malevoli. È fondamentale superare un modello semplificato che identifica "attori malintenzionati" (es. stati esteri, troll farms) e "cittadini passivi ingannati", proponendo come soluzione la mera rimozione dei primi. Evidenze empiriche contraddicono questa visione:
*   Phillips & Milner (2017) dimostrano che i media mainstream spesso amplificano i contenuti più dei troll, e il [[Fact-checking]] può aumentare la visibilità di ciò che intende smentire.
*   Marwick & Lewis (2017) suggeriscono che l'ecosistema informativo è manipolabile *by design*, a causa delle logiche delle newsroom (novità, conflitto) e degli algoritmi delle piattaforme, che creano vulnerabilità strutturali.
In questo contesto, "sfruttare" le dinamiche comunicative non equivale necessariamente a "violare" norme, ma riflette una competenza comunicativa che può essere impiegata per fini diversi.

## 📊 Dati, Tecnologie e Metriche

L'identificazione e la categorizzazione degli attori sono cruciali per comprendere le dinamiche informative. L'ecosistema italiano può essere stratificato come segue:

| Tier | Categoria | Utenti/Stima | Threat |
|---|---|---|---|
| TIER 1 | Politici istituzionali | Es. Meloni 1,8M X; Salvini 1,2M FB; Conte 2,5M FB | Polarizzazione, erosione fiducia |
| TIER 2 | Media alternativi/partisan | Es. Byoblu 400k YT; L'Indipendente; Vox | Radicalizzazione di nicchia |
| TIER 3 | Influencer micro-celebrities | 10-100k followers (alto engagement) | Ponte mainstream-fringe |
| TIER 4 | Reti automatizzate | Bot italiani 100-500 stimati | Astroturfing, perception hacking |

L'influenza di attori statali esterni, come la Russia, ha subito significative variazioni:

| Indicatore | Pre-2022 | Post-2022 |
|---|---|---|
| Budget | €5-10M/anno | Opaco (proxy websites, funding opaco) |
| Staff | ~50 persone in Italia | Ridotto + proxy |
| Sputnik | 100-300k unique/mese | Chiuso feb 2022 |
| RT | 50-150k unique/mese | Chiuso feb 2022 |
| Reach diretto | 500k-1M impressions/mese | -70% |
| Reach indiretto (proxy) | N/A | ~30% pre-ban |
| Tattiche | Sputnik, RT | Proxy websites, bot amplification, Telegram infiltration |

Tra gli attori non-statali, si osservano:
*   **Forza Nuova**: 1-2k membri, marginalizzata.
*   **Casapound**: ~500 attivisti, in declino post-2018.
*   **No-vax (picco 2021-22)**: Manifestazioni 10-50k, ~200k Telegram; core 5-10k.
*   **Cina**: Decine di account Twitter IT, focus su élite (BRI/Taiwan/Xinjiang).

## 🔍 Analisi Operativa ed Applicazioni OSINT

L'analisi degli attori e delle loro tattiche è fondamentale per l'[[Osint]].
*   **Il Caso Cutro (26 Feb 2023) come "Battle of Narratives"**: La tragedia ha evidenziato come l'interpretazione degli eventi sia guidata da "valori inconciliabili" (sicurezza vs. diritti umani), piuttosto che da una semplice dicotomia "vero vs. falso". L'[[Analisi strutturata|Frame Analysis]] (Entman) si rivela più utile del tradizionale [[Fact-checking]] per comprendere come diversi attori (Governo, ONG/Opposizione, Media) costruiscano narrazioni distinte (es. "traffico esseri umani" vs. "mancanza SAR").
*   **COVID-19: Laboratorio di Disinformazione (2020-2023)**: La pandemia ha mostrato l'evoluzione delle narrazioni e degli attori. Dalle teorie sull'origine (lab leak, 5G virus) diffuse da complottisti marginali, si è passati a narrazioni sulla "dittatura sanitaria" e "morti sovrastimate" promosse da estrema destra e medici dissidenti. La fase dei vaccini ha visto un picco di narrazioni su "siero genico" e "morti da vaccino" da parte di un mix di no-vax e scettici, amplificate su Telegram.
*   **Il Megafono Involontario dei Media**: L'esempio di "Plandemic" dimostra come il debunking non coordiNATO da parte dei media tradizionali (es. TG1, TG5, La7) possa involontariamente amplificare contenuti disinformativi, trasformando un video con zero visualizzazioni iniziali in milioni di visualizzazioni in poche settimane. Questa è un'implicazione operativa cruciale per la gestione della comunicazione.
*   **[[Fact-checking]] in Italia: Capacità e Limiti**: Organizzazioni come Pagella Politica, Facta.news, Open e Butac.it svolgono un ruolo importante. Tuttavia, affrontano limiti strutturali: reach asimmetrico (la verifica ha un impatto 10-100 volte inferiore rispetto alla bufala), backfire effect, bias percepito e sostenibilità economica.
*   **Deficit Democratico vs. Deficit Cognitivo**: Due letture del voto populista: la visione "popolo inganNATO" (élite) suggerisce una soluzione paternalistica (educazione/censura), mentre la visione "élite sorde" (Mudde & Kaltwasser, 2017) riconosce che i populisti intercettano reali insoddisfazioni. La [[Disinformazione]] è spesso un Sintomo di vulnerabilità domestiche preesistenti, non la causa primaria. La Russia, ad esempio, non crea l'euroscetticismo, ma lo sfrutta.

## 🔮 Lacune Informative e Prossimi Passi

Per un'analisi più completa degli attori, sono necessarie ulteriori ricerche e dati:
1.  **Dati reali sui proxy russi post-2022**: Le informazioni disponibili da fonti come DIS/Copasir sono spesso non pubbliche; sono necessarie verifiche tramite fonti investigative indipendenti.
2.  **Studi sui bot italiani**: Sono meno studiati rispetto a quelli statunitensi; manca un dataset quantitativo disponibile.
3.  **Misurazione dell'impatto**: I numeri di reach/engagement sono spesso stime non verificate indipendentemente.
4.  **Piattaforme emergenti**: Social Media come Tiktok e Telegram sono in rapida evoluzione; è fondamentale verificare la disponibilità attuale di strumenti di monitoring efficaci.

## 🔗 Connessioni e Pattern

- [[Applicazioni osint]]
- [[Disinformazione]]
- [[Ecosistema disinformativo italiano]]
- [[Fact-checking]]
- [[Osint]]
- [[Radicalizzazione]]


- [[--]]
F/I/H
- [[--]]
