---
title: "Geoint"
tags: ["OSINT", "processed", "geoint", "SATelliti", "geolocation", "imint"]
date: "2026-05-15"
status: "draft"
depth: "deep"
sources: "5"
tipo: "concetto"
---

# Geoint

## 🎯 Sintesi Strategica

La **GEOINT (Geospatial Intelligence)** è lo sfruttamento e l'analisi di immagini o di informazioni geografiche per descrivere, valutare e rappresentare visivamente dati fisici relativi alla superficie terrestre. Nell'era dell'[[Osint]], la GEOINT ha subito una democratizzazione senza precedenti: capacità SATellitari e fotogrammetriche che durante la [[Guerra Fredda]] erano esclusive di superpotenze miliardarie, oggi sono accessibili gratuitamente via web browser da investigatori civili (Bellingcat) o agenzie giornalistiche per validare o smentire narrazioni di guerra, movimenti di truppe o disastri ambientali manipolati da campagne di [[Disinformazione]].

## 📚 Contesto e Definizioni

La GEOINT integra storicamente la **IMINT** (Imagery Intelligence, l'analisi del supporto fotografico) e la fonde con layer di dati geografici (GIS).
In OSINT, il flusso di lavoro si declina principalmente in due filoni investigativi:
1.  **Geolocalizzazione (Geolocation):** Determinare le esatte coordinate GPS (Latitudine, Longitudine) del luogo in cui è stata scattata una foto o registrato un video rinvenuto sui social media (UGC - User Generated Content).
2.  **Cronolocalizzazione (Chronolocation):** Stabilire non solo il *dove*, ma il momento esatto nel tempo (*quando*) l'evento si è verificato, smascherando video vecchi riciclati (es. un bombardamento del 2014 spacciato per un attacco odierno).

## 📊 Dati, Tecnologie e Metriche

L'arsenale metodologico non si basa sull'uso miracoloso di software "enhancement", ma sull'incrocio di dettagli ambientali (Landmarks):
*   **Infrastrutture e Topografia:** Tralicci dell'alta tensione, configurazione asimmetrica delle finestre di un palazzo, campanili, andamento di una catena montuosa all'orizzonte o segnaletica orizzontale sull'asfalto.
*   **Analisi SATellitare Commerciale:** Piattaforme come **Sentinel Hub** (ESA) o **Google Earth Pro** forniscono non solo mappe ottiche, ma *Dati Storici* (funzione "Torna Indietro") e bande multispettrali (es. Infrarossi per rilevare incendi o vegetazione mimetica).
*   **Analisi delle Ombre (Shadow Analysis):** Utilizzando strumenti come *Suncalc*, l'analista misura l'angolazione e la lunghezza dell'ombra proiettata da un oggetto visibile nella foto. Conoscendo la geolocalizzazione, la data approssimativa e la posizione geometrica del sole, si può dedurre matematicamente l'ora esatta in cui la foto è stata scattata, o viceversa, calcolare la località conoscendo l'ora esatta.

## 🔍 Analisi Operativa ed Applicazioni OSINT

L'impatto sul [[Fact-checking]] militare è totale:
*   Durante i moderni conflitti ad alta intensità (es. Siria, Ucraina, Gaza), soldati o civili caricano video sfocati su Telegram (SOCMINT). Analisti indipendenti estraggono i frame del video, li confrontano con la vista 3D di Google Street View o Google Earth, triangolano i punti di riferimento e "Pinpointano" le coordinate geolocalizzate, permettendo di confermare il posizionamento e l'avanzamento reale della linea del fronte a dispetto della propaganda governativa ufficiale.

## 🔮 Lacune Informative e Prossimi Passi

*   **Risoluzione e Paywall:** Le immagini gratuite (es. Copernicus Sentinel) offrono una risoluzione di 10-15 metri per pixel (utili per vedere un porto distrutto o una città in fiamme). Le immagini sub-metriche ad altissima risoluzione (es. 30 cm per pixel, sufficienti per identificare un carro armato o i danni a un tetto) fornite da aziende come Maxar o Planet Labs sono coperte da paywall proibitivi per i singoli investigatori, creando un monopolio dell'informazione geospaziale "tattica" (VHR - Very High Resolution).

## 🔗 Connessioni e Pattern

- [[Osint]]
- [[Fact-checking]]
- [[Disinformazione]]
- [[Fonti osint]]

- [[--]]
F/I/H
- [[--]]
