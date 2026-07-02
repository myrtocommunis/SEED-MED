---
title: Raccolta dati
tags:
- OSINT
- processed
- raccolta-dati
date: '2026-05-15'
status: draft
depth: standard
sources: '2'
tipo: concetto
---

# Raccolta dati

## 🎯 Sintesi Strategica

La raccolta dati in ambito OSINT rappresenta il fondamento tattico dell'intelligence digitale, operando su un duplice livello: l'acquisizione del dato primario (contenuto visibile) e l'estrazione sistematica dei metadati (dati sui dati). Il processo si è evoluto da tecniche manuali a pipeline automatizzate (ETL, scraping, API), gestendo volumi crescenti di dati strutturati, semi-strutturati e non strutturati. La robustezza di qualsiasi analisi dipende dalla corretta tassonomia delle fonti, dalla preservazione della catena di custodia e dalla capacità di distinguere tra segnale informativo e rumore algoritmico. I metadati, spesso trascurati dall'utente medio, costituiscono il livello forense più critico per la geolocalizzazione, l'attribuzione e la verifica dell'autenticità.

## 📚 Contesto e Definizioni

Nel contesto dell'intelligence delle fonti aperte, la raccolta dati è definita come il processo sistematico di acquisizione, classificazione e preservazione di informazioni da fonti digitali pubbliche. La tassonomia operativa classifica le fonti in cinque categorie principali: dati strutturati (database relazionali, CSV con schema rigido), semi-strutturati (JSON, XML, profili social con campi variabili), non strutturati (testo libero, immagini, video, audio), multimodali (combinazioni sensoriali) e geodati (componenti spaziali esplicite). La proliferazione dei dati non strutturati, che rappresentano la maggioranza del flusso informativo globale, richiede l'adozione di paradigmi Big Data basati sui 5 V: Volume, Variety, Velocity, Veracity e Value. La distinzione fondamentale risiede nel dato primario, intenzionale e modificabile, e nel dato secondario o metadato, generato automaticamente dai sistemi e descrittivo del contesto di creazione (CHI, QUANDO, DOVE, COME). La corretta identificazione del tipo di dato (nominali, ordinali, intervallo, ratio) è prerequisito metodologico per evitare distorsioni analitiche.

## 📊 Dati, Tecnologie e Metriche

L'architettura di raccolta moderna si articola in tre regimi operativi: manuale (gold standard per precisione e giudizio contestuale), semi-automatica (bilanciamento scala/contesto) e automatica (scraping, crawling, API per alta scalabilità). Il processo ETL (Extract, Transform, Load) costituisce il collo di bottiglia infrastrutturale, dove la normalizzazione, deduplicazione e arricchimento dei dati determinano la qualità del downstream analitico.
I metadati rappresentano il bersaglio forense primario. Per le immagini, lo standard EXIF fornisce coordinate GPS, timestamp, modello dispositivo e software di elaborazione. Per i documenti, strumenti come FOCA e Metagoofil estraggono percorsi file, autori e cronologie di revisione. Nell'analisi di rete e posta elettronica, l'ispezione degli header SMTP, la geolocalizzazione IP e la verifica dei protocolli SPF/DKIM/DMARC permettono di tracciare l'instradamento e identificare anomalie infrastrutturali.

| Tecnica di Estrazione | Target Principale | Metrica di Valore OSINT |
|---|---|---|
| EXIFTool / Invide | Immagini e video | Geolocalizzazione forense, attribuzione dispositivo |
| FOCA / Metagoofil | Documenti web | Tracciamento filiera, identificazione software |
| Header Analysis / Securitytrails | E-mail e DNS | Tracciamento hop, geolocalizzazione IP, typosquatting |
| API / Web Scraping | Database e pagine | Scalabilità, aggiornamento in tempo reale |
| Maltego / Graph DB | Dataset correlati | Mappatura relazioni, network intelligence |

## 🔍 Analisi Operativa ed Applicazioni OSINT

L'applicazione operativa della raccolta dati si concentra sulla verifica forense e sulla mappatura infrastrutturale. Nell'analisi di campagne di influenza o phishing, l'incrocio tra metadati di rete e timestamp di pubblicazione permette di distinguere tra comunicazioni istituzionali legittime e attacchi mirati, anche quando il contenuto testuale è perfettamente ingannevole. La geolocalizzazione tramite coordinate EXIF o [[IP geolocation]], combinata con l'analisi delle ombre e degli artefatti di compressione, costituisce il gold standard per la verifica di immagini SATellitari e contenuti multimodali.
Il framework operativo richiede l'implementazione rigorosa della [[Catena di custodia]] per ogni artefatto acquisito. Ogni screenshot, estrazione EXIF o record DNS deve essere accompagNATO da hash [[SHA-256]], timestamp certificati e log di accesso. La [[Network intelligence]] integra i metadati di routing con l'analisi whois e [[DNS History]] per mappare l'infrastruttura di attori ostili o asset digitali. La [[Computer vision]] fornisce il contesto per l'elaborazione di segnali visivi non strutturati, dove l'occhio umano addestrato decodifica pattern che gli algoritmi generano come rumore.

## 🔮 Lacune Informative e Prossimi Passi

Nonostante la maturità degli strumenti, permangono lacune critiche. Le piattaforme social e i servizi cloud applicano sempre più aggressivamente la rimozione automatica dei metadati EXIF, rendendo la prova forense dipendente dall'acquisizione dell'originale non processato. La crescente adozione di standard di autenticazione sintetica (es. C2PA, Content Credentials) da parte di modelli generativi introduce metadati indistinguibili da quelli reali, richiedendo protocolli di verifica crittografica avanzata. Inoltre, la geolocalizzazione IP a livello urbano presenta margini di errore significativi e la possibilità di spoofing, mentre la compliance [[GDPR]] richiede un bilanciamento continuo tra legittimo interesse investigativo e minimizzazione dei dati personali. I prossimi passi includono l'automazione della catena di custodia digitale, l'integrazione di pipeline ETL resilienti ai cambi di template e lo sviluppo di modelli di computer vision specializzati nella rilevazione di artefatti generativi.

## 🔗 Connessioni e Pattern

- [[Applicazioni osint]]
- [[Catena di custodia]]
- [[Classificazione]]
- [[Intelligence digitale]]
- [[Modelli generativi]]
- [[Network intelligence]]


- [[--]]
F/I/H
- [[--]]
