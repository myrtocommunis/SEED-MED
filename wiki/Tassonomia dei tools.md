---
title: "Tassonomia dei tools"
tags: ["OSINT", "processed", "tools", "opsec", "cyber", "geospatial", "socmint"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "1"
tipo: "concetto"
---

# Tassonomia dei tools

## 🎯 Sintesi Strategica

Il toolkit dell'analista [[Osint]] contemporaneo è un ecosistema iper-frammentato e in costante mutazione di strumenti software, API e framework di raccolta. La padronanza professionale non consiste nell'accumulare il maggior numero di tool, bENSì nel classificarli funzionalmente all'interno di una rigorosa architettura metodologica. Il principio dottrinale fondamentale è che **i tool sono strumenti, non metodi**: l'utilizzo di un estrattore dati senza una domanda investigativa (Requirement) o un framework logico produce esclusivamente "rumore informativo", non intelligence. Inoltre, la selezione degli strumenti richiede un'attenzione ossessiva all'[[Opsec]], poiché le piattaforme "gratuite" spesso monetizzano tracciando e profilando gli analisti stessi.

## 📚 Contesto e Definizioni

L'obsolescenza dei tool OSINT è rapidissima (le API vengono chiuse, i servizi cambiano policy di *pricing*). Pertanto, la tassonomia si basa sulla *funzione operativa* e non sul nome commerciale del prodotto, garantendo la resilienza delle indagini.

### Il Paradosso del "Tool Magico"

La proliferazione commerciale dei framework investigativi crea l'illusione cognitiva (Tool-Bias) che la risoluzione di un'indagine dipenda dalla scoperta di uno strumento segreto, celando il fatto che le migliori indagini derivano da *query* manuali raffinate (es. Google Dorks) e dall'analisi umana del *pivot*.

## 📊 Dati, Tecnologie e Metriche

Il panorama funzionale si divide in cinque macro-categorie operative:

### 1. Ricerca Persone e Identità Digitale (SOCMINT)

*   **Whoxy:** Ricerca storica WHOIS inversa per identificare i domini posseduti da una persona/email.
*   **Hunter.io / Phonebook.cz:** Scoperta e verifica di indirizzi email corporate.
*   **Pipl / Spiderfoot / OSINT Industries:** Aggregazione cross-platform di tracce digitali (leak, social, public records).
*   **Sherlock / WhatsmyName:** Enumerazione username (verifica la presenza di un nickname su centinaia di piattaforme simultaneamente).

### 2. Riconoscimento Facciale e Visual OSINT

*   **Pimeyes:** Il motore di ricerca facciale open-source più potente (altissima accuratezza per fisionomie occidentali).
*   **Search4Faces:** Ottimizzato per il blocco ex-sovietico (VKontakte, Odnoklassniki).
*   **Picarta:** AI contestuale per la geolocalizzazione di foto senza metadati GPS.
*   **Tineye / Yandex:** *Reverse Image Search* per l'identificazione della fonte primaria di una foto e il tracciamento delle sue manipolazioni.

### 3. Cyber OSINT e Infrastruttura

*   **Shodan / CENSys:** I motori di ricerca per dispositivi connessi (IoT, SCADA, telecamere non protette, server mal configurati).
*   **DNSdumpster / Securitytrails:** Enumerazione della topologia di rete, sottodomini e [[Ip-dns intelligence]].
*   **Builtwith / Wappalyzer:** Profilazione dello stack tecnologico aziendale (CMS, framework, plugin).
*   **Virustotal / [[urlscan.io]]:** *Sandboxing* e analisi degli indicatori di compromissione (IOC).

### 4. GEO-OSINT e Analisi Spaziale

*   **Sentinel Hub / EO Browser:** Accesso gratuito all'archivio ESA (SATelliti Sentinel-1 e 2) per radar e ottica multi-spettrale.
*   **Google Earth Pro:** Strumento d'elezione per l'analisi cronologica (Historical Imagery) del terreno.
*   **Mapillary:** La controparte *crowdsourced* e open-source di Street View.
*   **Suncalc:** Applicazione di calcolo solare essenziale per la *Shadow Analysis* (stima oraria tramite la proiezione delle ombre).

### 5. Aggregatori e Link Analysis Frameworks

*   **Maltego:** Standard industriale per l'analisi visuale a grafo (Link Analysis).
*   **Recon-ng:** Framework modulare a riga di comando (ispirato a Metasploit) per data-gathering.
*   **Start.me:** Hub di bookmark curati dalla community (da consultare sempre con protezione VPN).

## 🔍 Analisi Operativa ed Applicazioni OSINT

L'applicazione di questi strumenti sul campo richiede una base infrastrutturale sicura.

### Il "Must-Have" OSINT Toolkit (Setup Operativo)

L'analista professionale parte da una configurazione di base non negoziabile:
1.  **Compartimentazione Macchina:** Macchina Virtuale (VM) o ambiente cloud isolato dal disco personale.
2.  **Rete Anonimizzata:** VPN professionale configurata su router (o *kill-switch*) per evitare *leak* DNS.
3.  **Browser Setup:** Firefox *Hardened* o Brave per investigazioni pulite, affiancato da Tor Browser per l'esplorazione profonda.
4.  **Identità Fittizia:** [[Sock puppet]] pluriennali "scaldati" per l'accesso a social e forum senza far scattare allarmi di sicurezza (anti-bot honeypots).
5.  **Exiftool:** Utility da linea di comando standard per l'estrazione spietata di metadati documentali e fotografici.

## 🔮 Lacune Informative e Prossimi Passi

*   **Costi Occulti dell'Automazione:** Strumenti enterprise (es. Maltego Commercial, Spiderfoot HX) impongono costi di licenza insostenibili per ricercatori indipendenti, spingendo verso lo sviluppo casalingo di script Python personalizzati.
*   **Tooling per Modelli Generativi:** La tassonomia attuale manca di una sezione codificata sui tool di rilevamento sintetico (es. classificatori audio per clonazione vocale e rilevatori di testi LLM), settore ancora frammentato e privo di gold standards.

## 🔗 Connessioni e Pattern

- [[Osint basics]]
- [[Ip-dns intelligence]]
- [[Opsec]]
- [[Cyber]]
- [[Strumenti di ricerca]]

- [[--]]
F/I/H
- [[--]]
