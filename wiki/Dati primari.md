---
title: Dati primari
tags:
- OSINT
- processed
- dati-primari
date: '2026-05-15'
status: draft
depth: standard
sources: '1'
tipo: concetto
---

# Dati primari

## 🎯 Sintesi Strategica

La raccolta [[Osint]] non si limita al contenuto visibile, o [[Dati primari]], ma si estende in modo sistematico al livello cruciale dei [[Metadati]] – ovvero, i dati sui dati. Questa distinzione è un fondamento tattico per qualsiasi operazione di intelligence digitale. Mentre il dato primario (ad esempio, un post sui social media, un documento, un articolo) è suscettibile di modifica, falsificazione e manipolazione, i metadati sono generati automaticamente dai sistemi e descrivono il *chi*, *quando*, *dove* e *come* della creazione del dato primario. Sebbene non siano inviolabili, i metadati sono intrinsecamente più difficili da negare e rappresentano un livello di verifica superiore in contesti operativi, dalla validazione di immagini SATellitari alla rilevazione di campagne di [[Ingegneria sociale|Phishing]]. Questa nota analizza la tassonomia dei dati (strutturati, semi-strutturati, non strutturati, multimodali, geodati), la struttura dei metadati in artefatti digitali (EXIF nelle immagini, header di rete ed e-mail) e le loro applicazioni nella Forensia Digitale e nell'analisi OSINT.

## 📚 Contesto e Definizioni

Nel contesto dell'[[Osint]], ogni artefatto digitale esiste simultaneamente su due livelli distinti. Il **dato primario** è il contenuto intenzionale e direttamente percepibile: il testo di un post, un fotogramma di un video, una slide di una presentazione. È la superficie dell'informazione, quella con cui l'utente medio interagisce.

Il **dato secondario**, o [[Metadati]], è l'insieme delle informazioni descrittive generate automaticamente dal dispositivo, dal software o dalla piattaforma che ha prodotto il contenuto primario. Questi dati "sui dati" sono spesso invisibili all'utente comune ma sono persistenti e costituiscono una vera e propria mappa forense per l'analista. Esempi includono la [[Ip-dns|Geolocalizzazione]] nascosta in una foto, l'orario esatto di pubblicazione non visibile nel feed, o l'identificativo utente che rimane invariato anche dopo un cambio di username. Per l'operatore OSINT, la distinzione è cruciale: mentre l'utente si concentra sul dato primario, l'analista opera sui metadati per estrarre informazioni verificabili e difficilmente negabili.

### Schema di classificazione dei dati per tipo di organizzazione

| Categoria             | Definizione OSINT                                      | Accessibilità Umano/Macchina | Esempio Operativo                                | Grado di Manipolazione |
| :-------------------- | :----------------------------------------------------- | :--------------------------- | :----------------------------------------------- | :--------------------- |
| **Dati strutturati**  | Tabelle, matrici, database relazionali con schema rigido | Entrambi                     | CSV da API, censimenti, fogli Excel              | Bassa (schema vincolato) |
| **Dati semi-strutturati** | Variabili nominative senza schema rigido               | Entrambi                     | Profili social (campi non obbligatori vuoti)     | Media                  |
| **Dati non strutturati** | Nessuna organizzazione predefinita                     | Uomo ↑ / Macchina ↓          | Immagini, video, audio, testi liberi             | Alta                   |
| **Dati multimodali**  | Combinazione di diversi tipi sensoriali per codificare | Uomo ↑↑↑                     | Video con audio + tracking geospaziale           | Variabile              |
| **Geodati**           | Dati con componente spaziale/geografica esplicita      | Uomo / Macchina              | Coordinate GPS, immagini SATellitari, checkpoint | Variabile              |

La crescente prevalenza di dati non strutturati, in particolare contenuti visivi e audio, rappresenta sia una sfida per l'elaborazione automatica sia un'opportunità unica per l'estrazione di metadati ricchi da parte di analisti esperti.

## 📊 Dati, Tecnologie e Metriche

I [[Metadati]] variano radicalmente in base al tipo di artefatto digitale. La comprensione di questa architettura è fondamentale per l'estrazione e l'analisi in [[Osint]].

### Mappa dei campi metadati per artefatto digitale

| Tipo Artefatto      | Metadati visibili                               | Metadati nascosti                                                                                                 | Strumento di estrazione               | Valore OSINT                                    |
| :------------------ | :---------------------------------------------- | :---------------------------------------------------------------------------------------------------------------- | :------------------------------------- | :---------------------------------------------- |
| **Immagine/jpeg**   | Dimensioni, formato, orientamento               | EXIF completo (GPS, dispositivo, software, data/ora, esposizione)                                                 | EXIFTool                               | [[Ip-dns|Geolocalizzazione]] forense, attribuzione dispositivo |
| **Documento (PDF/Doc)** | Autore, titolo, pagina                          | Metadati completi (autore, software generatore, revisioni, timestamp, percorsi file)                              | FOCA, Metagoofil                       | Tracciamento filiera documentale, identificazione software |
| **E-mail**          | Mittente, oggetto, corpo                        | Header completi (hops SMTP, IP sorgente, server relay, SPF/DKIM/DMARC authentication)                             | Analisi headers manuale / tool specializzati | Decoyazione [[Ingegneria sociale|Phishing]], attribuzione geografica Mittente |
| **Pagina web**      | URL, contenuto pagina                           | Whois (proprietario dominio), storico DNS, timestamps, sitemap                                                    | Securitytrails, Whois lookups          | Tracciamento asset digitali, mappatura infrastrutture |
| **Post social**     | Testo, immagine, metrics di engagement          | User ID persistente, IP di pubblicazione, timestamp esatto, geotag                                                | Pivoting + API scraping                | Ricostruzione profilo, geolocalizzazione indiretta |
| **Video**           | Durata, risoluzione, codec                      | Metadati camera, stabilizzazione, metadati di editing, metadati di piattaforma                                   | Invide, Weverify, EXIFTool             | Verifica autenticità, attribuzione fonte        |

### Esempio forense: E-mail di phishing decodata dai metadata

In uno scenario di [[Ingegneria sociale|Phishing]], i metadati possono rivelare la falsità di un messaggio apparentemente legittimo, anche quando il testo primario è impeccabile.

| Elemento Forense    | Segnale Legittimo             | Segnale Rivelato                                | Impatto Operativo                                |
| :------------------ | :---------------------------- | :---------------------------------------------- | :----------------------------------------------- |
| **Dominio mittente** | @istituto-banca.it            | @istituto-banca[.]xyz (typosquatting)           | **ALTO** — prova di frode                        |
| **IP sorgente**     | Range bancario certificato    | IP geolocalizzato in Russia                     | **ALTO** — attribuzione geografica               |
| **Server relay**    | Mail server istituzionale     | Server anonimo in Russia                        | **ALTO** — infrastruttura compromessa            |
| **Timestamp**       | Orario Business Europeo       | 03:47 AM GMT+3                                  | **MEDIO** — comportamento anomalo                |
| **SPF/DKIM**        | Authentication pass           | Authentication fail                             | **ALTO** — prova tecnicamente inconfutabile      |

In questo caso, i metadati avrebbero inequivocabilmente smascherato l'inganno, confermando la falsità dell'intero messaggio.

## 🔍 Analisi Operativa ed Applicazioni OSINT

La classificazione e l'analisi dei dati sono passaggi fondamentali nella catena di intelligence [[Osint]]. Ogni fonte deve essere categorizzata per determinare gli strumenti appropriati e la robustezza della verifica.

### 1. La Tassonomia dei Dati nel Flusso OSINT

*   **Dati strutturati**: Formati come CSV sono la spina dorsale dell'analisi automatizzata. In OSINT, si estraggono prevalentemente da API di piattaforme o database governativi aperti. La loro struttura rigida consente analisi rapide e interrogazioni precise.
*   **Dati semi-strutturati**: Esempi includono i profili social (JSON, XML), dove i campi sono nominativi ma non tutti obbligatori. Richiedono pulizia preventiva per l'analisi.
*   **Dati non strutturati**: Immagini, video, audio, testi liberi. Costituiscono la maggioranza assoluta dei dati rintracciabili online. La loro difficoltà di interpretazione automatica li rende paradossalmente ricchi di [[Metadati]] non censurabili dalle piattaforme.

### 2. EXIF — L'ANATOmia dei Metadati Immagine

L'EXIF (Exchangeable Image File Format) è il sistema di metadati integrato nei file immagine, rappresentando una fonte forense cruciale per l'analista di immagini.

### Structura EXIF — Campi Forensi Critici per OSINT

| Campo EXIF              | Cosa Rivela                                | Valore Operativo OSINT                                    | Falsificabilità                      |
| :---------------------- | :----------------------------------------- | :-------------------------------------------------------- | :----------------------------------- |
| **GPSLatitude/GPSLongitude** | Coordinate geografiche esatte              | [[Ip-dns|Geolocalizzazione]] forense di foto/contenuti           | Media (app possono resettare GPS)    |
| **Datetimeoriginal**    | Momento esatto di scatto                   | Cronolocalizzazione di eventi                             | Bassa (clock hardware del dispositivo) |
| **Make/Model**          | Dispositivo che ha generato il file        | Attribution tecnologica, profilazione                     | Bassa (firmware integrato)           |
| **Software**            | Software di editing post-raccolta          | Rilevazione manipolazione                                 | Bassa                                |
| **GPSAltitude**         | Quota rispetto al livello del mare         | Verifica geografica (montagna vs piano)                   | Media                                |
| **GPSProcessingmethod** | Come le coordinate sono state acquisite    | GPS hardware vs app vs inserimento manuale                | Bassa                                |
| **Compression/Resolution** | Grado di compressione, DPI                 | Valutazione originale vs screenshot                       | Bassa                                |
| **InteropIM**           | Informazione di interoperabilità           | Cross-referencing tra dispositivi                         | Bassa                                |

### 3. Network Headers e Metadati Web — Tracciamento dell'Infrastruttura

I metadati di rete sono legati all'indirizzo IP, alla [[Ip-dns|Geolocalizzazione]], al proprietario del dominio e alla cronologia delle modifiche DNS, fondamentali per la [[Network intelligence]].
*   **Whois intelligence**: Registra proprietario del dominio, data di creazione, data di scadenza, provider. Un dominio creato di recente con privacy protection attiva è un segnale rosso immediato.
*   **[[DNS History]]**: Registra tutte le modifiche ai record DNS di un dominio nel tempo, permettendo di tracciare migrazioni di siti o cambiamenti di hosting, strategico per mappare l'infrastruttura di un attore ostile.
*   **IP geolocalization**: L'indirizzo IP di pubblicazione di un post o di un'e-mail può essere geolocalizzato con precisione variabile. CombiNATO con l'orario di pubblicazione, crea un profilo comportamentale.

### 4. E-mail Forensics — Protocollo di Verifica Forense delle E-mail

L'analisi forense delle e-mail è una competenza critica per l'analista [[Osint]], poiché le tecniche di [[Ingegneria sociale|Phishing]] e di operazioni di influenza si affidano spesso a e-mail apparentemente legittime che i metadati smascherano immediatamente.

### Protocollo di Analisi Forense E-mail — Step Operativi

| Step                    | Azione                                        | Strumento                                   | Output Atteso                                |
| :---------------------- | :-------------------------------------------- | :------------------------------------------ | :------------------------------------------- |
| **1. Header extraction** | Estrazione full headers dell'e-mail           | Client mail (Visualizza Origine), tool      | Raw header text                              |
| **2. Path tracing**     | Tracciamento degli hop SMTP dal destinatario all'origine | Analisi manuale headers (Received: fields)  | Timeline dell'instradamento                  |
| **3. IP geolocalization** | Geolocalizzazione IP sorgente e di ogni relay | Securitytrails, Shodan, BGP tools           | Mappa geografica dei nodi                    |
| **4. SPF/DKIM/DMARC**   | Verifica dei protocolli di autenticazione DNS | MXToolbox, Dmarcian                         | Pass/Fail + dettagli                         |
| **5. Domain comparison** | Confronto dominio mittente con dominio legittimo | Eyeo, [[urlscan.io]]                            | Identificazione typosquatting                |
| **6. Correlation**      | Incrocio timestamp IP geografia comportamento | Spreadsheet forense / Maltego               | Profilo dell'attaccante                      |

### 5. Catena di Custodia — Chain of Custody nel Contesto OSINT

La [[Catena di custodia]] è il principio forense che documenta ogni passaggio di un elemento di prova dalla scoperta all'analisi alla presentazione. In [[Osint]], si applica agli artefatti digitali recuperati. Ogni screenshot, ogni estrazione EXIF, ogni record DNS deve accompagnare una documentazione di: cosa è stato prelevato, da dove, quando, con quale strumento, e da chi.

### Framework operativo chain of custody digitale

| Elemento Chain of Custody | Descrizione OSINT                                  | Requisito Tecnico                       |
| :------------------------ | :------------------------------------------------- | :-------------------------------------- |
| **Identificazione artefatto** | Cosa è stato acquisito (file, URL, post)           | Hash [[SHA-256]] del file                   |
| **Data/ora acquisizione** | Quando è stato catturato il dato                   | Timestamp certificato                   |
| **Metodo di acquisizione** | Come è stato ottenuto (screenshot, API, EXIF)      | Strumento + versione + configurazione   |
| **Conservazione**         | Dove è memorizzato l'artefatto                     | Vault/replica criptata                  |
| **Trasferimento**         | Chi ha gestito l'artefatto e come                  | Log accessi con firma                   |
| **Verifica integrità**    | Il file non è stato alterato                       | Hash [[SHA-256]] ripetuto post-conservazione |

### 6. Strumenti Professionali di Estrazione Metadati

| Strumento             | Funzione Principale                               | Target                                | Output Forense                      |
| :-------------------- | :------------------------------------------------ | :------------------------------------ | :---------------------------------- |
| **EXIFTool**          | Estrazione completa metadati EXIF/XMP/IPTC        | Immagini, PDF                         | Report dettagliato metadati         |
| **FOCA**              | Analisi metadati documenti PDF/Word               | Documenti scaricati da siti web       | Autore, software, percorsi file     |
| **Metagoofil**        | Estrazione metadati da siti web                   | File PDF, DOC, PPT su domini target   | Lista documenti e loro metadati     |
| **Invide / Weverify** | Plugin browser per verifica visiva                | Immagini e video online               | Verifica autenticità, reverse-image |
| **Maltego**           | Visualizzazione relazioni tra entità              | Dataset completi [[Osint]]             | Graph analysis (IP, domini, persone, organizzazioni) |

## 🔮 Lacune Informative e Prossimi Passi

L'efficacia dell'analisi dei [[Metadati]] è un campo in continua evoluzione, soggetto a limiti strutturali e nuove sfide.

### ⚖️ Ipotesi Alternative sull'Analisi dei Metadati

1.  **Manipolazione dei metadati**: Sebbene i metadati possano essere una prova robusta, possono essere manipolati con strumenti di scripting (es. `exiftool --modify all`) o app con funzionalità specifiche. La falsificazione richiede competenze tecniche ma è fattibile.
2.  **Falsi positivi nella [[Ip-dns|Geolocalizzazione]]**: La geolocalizzazione basata su IP a livello città può avere margini di errore (es. ±20km). Lo spoofing GPS su dispositivi mobili è tecnicamente semplice con app dedicate.
3.  **Rimozione progressiva dalle piattaforme**: Piattaforme come Meta, X, Telegram e Whatsapp rimuovono automaticamente i metadati EXIF quando gli utenti caricano immagini. Ciò significa che la prova risiede solo nell'originale non processato dalla piattaforma.

### 📜 Cronologia Evolutiva Metadati e Forensia

| Epoca     | Evento                                            | Impatto sull'Analisi dei Metadati                                   |
| :-------- | :------------------------------------------------ | :------------------------------------------------------------------ |
| **1990s** | Standard EXIF 2.1 definito da JEIDA               | Prima standardizzazione metadati immagine                           |
| **2000s** | Diffusione smartphone con GPS integrato           | Metadati geospaziali disponibili per tutti                          |
| **2010s** | Snowden revelations su metadata collection        | Consapevolezza pubblica sulla sorveglianza metadata                 |
| **2016+** | Piattaforme social rimuovono EXIF                 | La Forensia Digitale richiede sempre l'originale, non il post-platform |
| **2023+** | AI generativa inserisce metadati sintetici (C2PA) | Nuovi protocolli di autenticazione dei metadati generati da IA      |

### 🧠 Note Metodologiche

Questa analisi è stata elaborata a partire da una fonte primaria, integrata con ricerca supplementare sui protocolli EXIF, gli strumenti forensi citati e i meccanismi di manipolazione dei metadati. Il framework della [[Catena di custodia]] è stato allineato con framework forensi standardizzati (NIST, ISO 27037). La tassonomia dei dati è standard nel campo dell'information science e corrisponde alla classificazione ISO/IEC 11179.

## 🔗 Connessioni e Pattern

- [[Catena di custodia]]
- [[Intelligence digitale]]
- [[Metadati]]
- [[Network intelligence]]
- [[Osint]]


- [[--]]
F/I/H
- [[--]]
