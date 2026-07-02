---
title: Raccolta osint
tags:
- OSINT
- processed
- raccolta-osint
date: '2026-05-15'
status: draft
depth: standard
sources: '1'
tipo: concetto
---

# Raccolta osint

## 🎯 Sintesi Strategica

La **Raccolta OSINT** è la fase operativa cruciale del [[Osint]], un processo replicabile che converte un requisito informativo in evidenza analitica verificabile. Essa consiste nell'identificazione, acquisizione e aggregazione sistematica di informazioni da fonti aperte e pubblicamente accessibili. Questa fase è intrinsecamente legata alla [[Pianificazione]], che ne definisce gli obiettivi, il contesto e le priorità, e precede l'[[Analisi]] dei dati raccolti. La raccolta efficace richiede l'applicazione di metodologie strutturate, l'utilizzo di strumenti specifici e una costante attenzione alla deperibilità delle fonti e alla sicurezza operativa (OPSEC) dell'analista.

## 📚 Contesto e Definizioni

La raccolta OSINT rappresenta la seconda delle tipiche 5 o 6 fasi progressive del workflow OSINT. In questa fase, le informazioni vengono attivamente ricercate e acquisite da un'ampia gamma di fonti aperte. La sua efficacia è direttamente proporzionale alla qualità della pianificazione iniziale, che stabilisce le domande chiave (le 5W: Who, What, When, Where, Why) e le informazioni mancanti.

Per strutturare la pratica di raccolta, si impiegano framework come:
*   **5W (Who/What/When/Where/Why):** Una griglia per la raccolta e la triangolazione delle informazioni, dove ogni asse viene verificato su fonti indipendenti.
*   **ABC (Accurato/Breve/Chiaro):** Uno standard per la redazione del prodotto finale, volto a contrastare il sovraccarico informativo.
*   **AIA (Impatta/Aggiorna/Approfondisce):** Un test di valore per ogni nuova informazione, valutandone l'impatto sulla comprensione del problema, la modifica delle ipotesi esistenti e la necessità di ulteriori indagini.

La valutazione della credibilità della fonte è un processo a tre livelli:
1.  **Cognitiva:** Accuratezza storica, coerenza interna, metodo di raccolta.
2.  **Normativa:** Reputazione istituzionale, track record, aderenza a standard.
3.  **Affettiva:** Risonanza emotiva con il lettore, che può distorcere la valutazione razionale e segnalare tentativi di manipolazione.

## 📊 Dati, Tecnologie e Metriche

La raccolta OSINT si avvale di un vasto ecosistema di strumenti e tecniche, ciascuno ottimizzato per specifici tipi di dati e contesti:

*   **Pianificazione e Targeting:** Il framework "Chi è / Cosa fa / Cosa usa" è fondamentale per organizzare la raccolta su persone fisiche o entità, mappando i Selectors Pivoting disponibili e identificando i gap informativi. La regola operativa cardine è la priorità delle fonti più deperibili, da preservare immediatamente con strumenti come [[Wayback machine]] e Save Page Now.
*   **Digital Footprint:** La distinzione tra *active footprint* (tracce volontarie) e *passive footprint* (tracce involontarie) guida la scelta dei selector. La footprint passiva è spesso più rivelatrice e accumulativa.
*   **Social Media Intelligence (SOCMINT):** La raccolta da piattaforme social si concentra su profili, contenuti, metadati, reti e pattern temporali. Strumenti come Sherlock e Maigret automatizzano la ricerca di username su centinaia di piattaforme. Le sfide includono profili privati, contenuti effimeri, account falsi, personalizzazione del feed e restrizioni API.
*   **Corporate OSINT (Business/Competitive Intelligence):** Si applica alla ricostruzione del profilo di società e reti aziendali. Strumenti chiave includono registri pubblici (Opencorporates, SEC EDGAR, Companies House, ZEFIX), banche dati commerciali (North Data, Crunchbase, Importyeti) e leak giornalistici (ICIJ Offshore Leaks).
*   **Geo-OSINT e Geolocalizzazione Visuale:** Disciplina che localizza immagini e video. Tecniche includono l'analisi dei metadati EXIF (con cautela), l'identificazione di landmark, il *terrain matching*, e l'uso di modelli AI come Geospy AI, StreetCLIP e ETHAN. L'analisi solare (Sun/Shadow Analysis con Suncalc.org) è un metodo rigoroso per determinare ora e stagione. Le immagini SATellitari (Sentinel-1/2, Planet Labs, Maxar) sono pilastri del [[Geoint]] open-source.
*   **Reverse Image Search:** Tecnica per trovare immagini simili o contestualmente affini a partire da un'immagine data. Motori come Google Images/LENS, Yandex Images, Tineye e Bing Visual Search sono usati in combinazione. È cruciale per verificare l'originalità e il contesto delle immagini.
*   **Google Dorks e Ricerca Avanzata:** Query avanzate che sfruttano operatori speciali (`site:`, `filetype:`, `inurl:`, `intitle:`, `after:`, `before:`, `"..."`, `-`, `OR`) per filtrare i risultati dei motori di ricerca e individuare informazioni specifiche o configurazioni esposte. La [[Google hacking]] (GHDB) è una risorsa di riferimento.
*   **[[RSS]]/Sitemap XML e Monitoring Strutturato:** L'uso di feed [[RSS]]/Atom e Sitemap XML permette un monitoring continuativo, anonimo e a bassa latenza di nuovi contenuti su siti web, identificando modifiche strutturali o l'aggiunta/rimozione di pagine.
*   **Web Scraping e API:** La raccolta automatizzata di dati da siti web tramite parsing HTML o rendering Javascript (Beautifulsoup, [[Web scraping|Playwright]], [[Puppeteer]], [[Selenium]]) è essenziale quando le API non sono disponibili. Le sfide includono sistemi anti-bot (rate limiting, CAPTCHA, Cloudflare, IP blocking) e la conformità legale (es. hiQ Labs v. Linkedin, [[GDPR]]). Le [[Api]] REST sono la via privilegiata quando offerte.
*   **Claim Detection Automatizzata:** Strumenti come Claimbuster assegnano uno score di "check-worthiness" alle frasi, supportando il fact-checking.

## 🔍 Analisi Operativa ed Applicazioni OSINT

La raccolta OSINT trova applicazione in svariati contesti:

*   **Indagini su Attori Statali e Non Statali:** Il caso MH17, investigato da Bellingcat, è un esempio paradigmatico di geolocalizzazione visuale e analisi SATellitare per collegare un convoglio missilistico alla 53ª Brigata antiaerea russa. Le indagini sui GRU, sempre di Bellingcat, dimostrano il potere dei Selectors Pivoting nel tracciare soggetti attraverso alias e pattern ricorrenti.
*   **Corporate Intelligence:** La ricostruzione di strutture societarie, investimenti, proprietà intellettuale, supply chain e profili di persone chiave per analisi di mercato, due diligence o indagini su frodi.
*   **Monitoraggio di Campagne di Disinformazione:** L'analisi del panorama mediale, supportata da strumenti come il GDELT Project e il RSF Press Freedom Index, permette di mappare le narrative dominanti, l'ownership dei media e i potenziali choke point informativi.
*   **Prevenzione e Risposta a Crisi:** La raccolta rapida di informazioni da fonti aperte è cruciale in contesti di emergenza, disastri naturali o conflitti, per comprendere la situazione sul campo e supportare le decisioni.
*   **Due Diligence Storica:** L'uso di [[Waymore]] e [[Wayback machine]] permette di ricostruire l'impronta digitale storica di un target, recuperando contenuti rimossi o versioni precedenti di siti web, utile per indagini su frodi o attività illecite passate.
*   **Sicurezza Operativa (OPSEC) dell'Analista:** La raccolta OSINT, se non condotta con rigore, può esporre l'analista. L'applicazione di principi OPSEC, come l'uso di dispositivi e profili dedicati, [[Vpn]], password manager e la creazione di [[Sock puppet]] "stagionati", è fondamentale per proteggere l'identità e l'integrità dell'indagine.

## 🔮 Lacune Informative e Prossimi Passi

Nonostante l'ampiezza delle tecniche e degli strumenti, la raccolta OSINT presenta sfide e aree di miglioramento:

*   **Verifica di Esempi Specifici:** Alcuni esempi operativi, come il "caso Kornvoli", sono citati come interni a contesti formativi e richiedono una verifica indipendente per la loro piena integrazione in un contesto accademico pubblico. Il "caso Badin", pur essendo un'investigazione documentata, necessita di una verifica puntuale dei dettagli specifici.
*   **Evoluzione Normativa:** Il panorama legale e etico dello scraping e dell'uso di dati personali è in continua evoluzione (es. [[GDPR]], AI Act), richiedendo un aggiornamento costante delle pratiche di compliance.
*   **Resilienza agli Anti-Bot:** I sistemi anti-bot delle piattaforme diventano sempre più sofisticati, rendendo lo scraping una sfida tecnica persistente e costosa.
*   **Accesso ai Dati Privati:** La raccolta è per definizione limitata alle fonti *aperte*. L'accesso a dati dietro login, paywall o in archivi privati rimane una lacuna intrinseca.
*   **Principio di Indeterminazione:** L'osservazione stessa può perturbare il sistema, specialmente in contesti social, influenzando il comportamento del target o l'algoritmo della piattaforma.

I prossimi passi includono l'affinamento delle metodologie per la verifica incrociata delle fonti, lo sviluppo di strumenti più resilienti ai sistemi anti-bot e l'integrazione di modelli di intelligenza artificiale per l'analisi e la sintesi dei dati raccolti, sempre nel rispetto dei vincoli etici e legali.

## 🔗 Connessioni e Pattern

- [[Analisi dei metadati]]
- [[Api]]
- [[Applicazioni osint]]
- [[Corporate intelligence]]
- [[Geoint]]
- [[Sock puppet]]


- [[--]]
F/I/H
- [[--]]
