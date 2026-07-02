---
title: Guerra cognitiva
tags:
- OSINT
- processed
- guerra-cognitiva
date: '2026-05-15'
status: draft
depth: standard
sources: '3'
tipo: concetto
---

# Guerra cognitiva

## 🎯 Sintesi Strategica

La **Guerra cognitiva** è una dimensione operativa emergente che mira a manipolare le percezioni, le credenze e i processi decisionali di una popolazione, di élite o di singoli decisori. Definita dalla [[NATO]] ACT come la "sesta dimensione operativa" (dopo terra, mare, aria, spazio e cyberspace), essa identifica la mente umana come il terreno di scontro primario. Non si limita a influenzare "cosa" si pensa, ma agisce su "come" si pensa, integrando neuroscienze, scienze cognitive, design persuasivo e lo sfruttamento sistematico dei [[Bias cognitivo]]. Ingloba e supera concetti come [[Information warfare]], PSYOP e [[Foreign Information Manipulation and Interference]] (Foreign Information Manipulation and Interference), utilizzando tecnologie avanzate come l'intelligenza artificiale generativa e il microtargeting comportamentale per ottenere effetti cognitivi duraturi.

## 📚 Contesto e Definizioni

La Guerra cognitiva è una tattica che combina tecnologie tradizionali ed emergenti, operando sia al di sopra che al di sotto della soglia di guerra per influenzare le popolazioni avversarie e i loro leader politici e militari. La sua ambizione la distingue da concetti affini:
*   **Information Warfare**: manipola il flusso informativo (canali, contenuti).
*   **PSYOP (Psychological Operations)**: influenza comportamenti tramite messaggi mirati.
*   **FIMI (Foreign Information Manipulation and Interference)**: il framework dell'EEAS per attività deliberate e coordinate di attori esteri, finalizzate a manipolare il dibattito pubblico e interferire nei processi democratici. Il suo nucleo dottrinale è olistico, considerando informazioni, comportamenti e infrastrutture.
*   **[[Propaganda]]**: l'uso sistematico di automazione e micro-targeting per l'influenza politica.

La Guerra cognitiva agisce come un *frame integratore*, fornendo una base cognitiva (il "perché" le manipolazioni funzionano) e una base tecnologica (AI generativa, neurotecnologie) che amplificano l'efficacia delle operazioni.

Un concetto correlato è l'**Information Disorder**, un framework analitico che supera la generica "fake news" distinguendo tre tipologie basate su falsità del contenuto e intento di nuocere:
*   **Misinformazione**: informazioni false o imprecise diffuse senza intenzione di nuocere.
*   **Disinformazione**: diffusione deliberata di informazioni false o manipolate con intento di ingannare o danneggiare.
*   **Malinformazione**: uso di informazioni vere estrapolate dal contesto o diffuse con intento dannoso (es. doxxing).

La dottrina russa della [[Maskirovka]] (inganno strategico) e il suo nucleo moderno, il [[Reflexive Control]], rappresentano un approccio classico alla guerra cognitiva, mirando a trasmettere all'avversario informazioni selezionate affinché le sue decisioni siano favorevoli all'attaccante.

## 📊 Dati, Tecnologie e Metriche

I vettori operativi della Guerra cognitiva sono molteplici e in continua evoluzione:
*   **Disinformazione coordinata**: diffusione di narrazioni manipolate attraverso reti orchestrate.
*   **[[Media sintetici]]**: generazione di immagini, audio e video iperrealistici tramite modelli di deep learning. L'effetto [[Liar's Dividend]] rende più facile negare la verità, mentre il Deepfake-as-a-Service (DaaS) democratizza la produzione di tali contenuti.
*   **Microtargeting e profilazione**: sfruttamento di dati comportamentali per messaggi altamente personalizzati.
*   **Exploit di [[Bias cognitivo]]**: manipolazione delle euristiche e dei pregiudizi intrinseci alla mente umana.
*   **Propaganda algoritmica**: ottimizzazione della diffusione dei messaggi tramite algoritmi delle piattaforme.
*   **AI-mediated manipulation**: uso di intelligenza artificiale per generare e distribuire contenuti, inclusi [[Prompt injection]] e [[Prompt injection]].
*   **Influence on decision-making**: alterazione dei processi decisionali per ottenere un [[Vantaggio decisionale]].

Le **infrastrutture operative** che abilitano queste manipolazioni includono:
*   **Bot Networks**: reti automatizzate per amplificazione e engagement artificiale.
*   **[[Sock puppet]]**: account falsi costruiti per influenza e raccolta informazioni.
*   **[[Coordinated sharing behavior]] (CIB)**: coordinazione comportamentale e inautenticità dell'identità dichiarata, rilevata tramite pattern di attività.
*   **[[Propaganda]]**: uso sistematico di automazione e micro-targeting.

L'avvento degli **LLM (Large Language Models)** ha rivoluzioNATO l'economia operativa della disinformazione, permettendo a singoli operatori di gestire centinaia di account con *backstory* coerenti e stili di scrittura personalizzati. Le pipeline LLM multi-agent automatizzano intere campagne, dalla strategia alla distribuzione e ottimizzazione in tempo reale.

L'**[[Information Laundering]]** è una tecnica chiave per offuscare l'origine delle informazioni false, attraverso fasi di *placement*, *layering* e *integration* che ne aumentano progressivamente la credibilità.

I dati operativi del 2024 sulle attività FIMI, secondo l'EEAS, hanno coinvolto almeno 25 piattaforme diverse, oltre 38.000 account, 322 organizzazioni target e incidenti distribuiti in 90 paesi, evidenziando la scala globale del fenomeno.

## 🔍 Analisi Operativa ed Applicazioni OSINT

Per l'analista OSINT, la Guerra cognitiva impone nuove sfide e approcci:
*   **Leggere il segnale, non il rumore**: la CW genera enormi quantità di contenuto a basso valore informativo; la precisione verificata è più importante dell'alta *recall*.
*   **Riconoscere la propria superficie cognitiva**: l'analista è un potenziale target, non solo un osservatore.
*   **Tracciare narrative, non solo eventi**: l'indicatore chiave è la deriva delle narrazioni dominanti.
*   **Cooperazione interdisciplinare**: neuroscienze, psicologia, giuristi e tecnologi devono essere integrati nell'analisi.

I **framework analitici** per l'analisi FIMI si integrano per coprire le campagne end-to-end:
*   **[[Disinformazione]]**: un catalogo standardizzato di TTPs (Tactics, Techniques, Procedures) per attaccanti e contromisure per difensori, adottato da EEAS, [[NATO]] e ONU.
*   **[[Metodologia]]**: classifica le operazioni FIMI su cinque vettori tattici (Dismiss, Distort, Distract, Dismay, Divide).
*   **[[Abcde]]**: un modello concettuale di livello superiore che separa Attore, Comportamento, Contenuto, Distribuzione ed Effetto.

Il **rilevamento e le contromisure FIMI** si basano su tre principi:
*   **Comportamento > Contenuto**: i pattern comportamentali (timing, coordinazione, network di amplificazione) sono più discriminativi della qualità del contenuto (che gli LLM possono rendere perfetta).
*   **Coordinazione come segnale primario**: il CIB è la *signature* operativa primaria di un'operazione orchestrata.
*   **Network analysis sull'amplificazione**: la struttura della rete che amplifica un contenuto è più significativa del contenuto stesso.

Gli **strumenti di monitoring narrativo** includono:
*   **Hamilton 2.0 Dashboard**: traccia narrazioni pro-Cremlino, pro-Pechino e pro-Teheran.
*   **EUvsdisinfo**: database di casi documentati di disinformazione pro-Cremlino.
*   **DFRLab (Atlantic Council Digital Forensic Research Lab)**: analisi di campagne specifiche.
*   **Stanford Internet Observatory**: ricerca accademica sull'attribuzione strutturale.
*   **GDELT Project**: sensore quantitativo di sentiment e tono su oltre 100 lingue.
*   **EDMO (European Digital Media Observatory)**: raccoglie casi verificati e analisi di debunking.
*   **EU Disinfo Lab**: analisi di campagne manipolative e reti di disinformazione.
*   **DBKF (Database of Known Fakes)**: raccoglie casi di manipolazione verificati da fact-checkers.
*   **Recorded Future / Insikt Group**: report su reti malevole e influence operations.
*   **Media Bias/Fact Check**: catalogo del bias e della fattualità di media internazionali.
*   **Telegago, TGStat, Telemetr.io**: strumenti per l'OSINT operativo su Telegram.

La **ricostruzione della filiera informativa** applica concetti di *supply chain* alla circolazione delle notizie, identificando origine, mediazione, amplificazione e punti di distorsione. Il **Frame Analysis** di Robert Entman è una tecnica OSINT per decostruire narrazioni, analizzando come definiscono problemi, attribuiscono cause, esprimono giudizi morali e propongono soluzioni. Il **Follow the Meme / Cross-Platform Narrative Tracking** traccia l'origine e la traiettoria di contenuti virali attraverso le piattaforme.

L'**attribuzione di campagne FIMI** si basa su una Triade delle evidenze: tecniche (artefatti digitali, infrastruttura), comportamentali (timing coordiNATO, TTPs ricorrenti) e contestuali (narrativa allineata agli interessi di un attore). I Principi di Cialdini (reciprocità, impegno/coerenza, riprova sociale, autorità, simpatia, scarsità) sono vettori di social engineering sistematicamente usati nelle campagne FIMI.

## 🔮 Lacune Informative e Prossimi Passi

Nonostante l'ampia documentazione, permangono alcune lacune e aree di miglioramento:
*   **Dati specifici**: Alcuni dati numerici (es. numero esatto di casi nel 2° EEAS Report, percentuali di engagement di Pew Research, dettagli del caso Crosetto 2025, Operazione Paperwall, Indian Chronicles) richiedono verifica puntuale su fonti primarie.
*   **Contesto normativo**: L'integrazione delle direttive europee come [[NIS 2]] e [[DORA]], e della Legge 124/2007 italiana, è parziale e necessita di un collegamento esplicito con i moduli dedicati all'etica e alla legalità.
*   **Strumenti di verifica**: L'integrazione sistematica di tool di *browser/image verification* (es. EXIF, ELA, steganalysis) con l'analisi di deepfake e manipolazione è un'area da sviluppare.
*   **Algoritmi e disinformazione**: La trattazione approfondita del ruolo degli algoritmi nella disinformazione è un gap strutturale nella documentazione attuale.
*   **Bias culturali**: I "news values" di Galtung & Ruge, sebbene utili, sono stati derivati da contesti specifici e necessitano di integrazione con studi comparati cross-culturali.
*   **Intento nelle tassonomie**: La tassonomia di Wardle sull'Information Disorder presuppone un intento verificabile, spesso difficile da accertare in OSINT senza HUMINT. È necessario integrare metodi operativi per inferire l'intento (es. analisi del CIB).
*   **Prospettive multiple**: L'analisi delle Active Measures da fonti russe, sebbene informativa, necessita di integrazione con classificazioni complementari di [[NATO]], UE o OSCE per una visione più neutrale.

Per colmare queste lacune, si propone la creazione di nodi specifici come `[[Etica]]`, `[[Deepfake]]` e `legge-124-intelligence-italiana`.

## 🔗 Connessioni e Pattern

- [[Information warfare]]
- [[Maskirovka]]
- [[Prompt injection]]
- [[Sock puppet]]
- [[Vantaggio decisionale]]


- [[--]]
F/I/H
- [[--]]
