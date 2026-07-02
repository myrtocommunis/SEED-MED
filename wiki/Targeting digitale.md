---
title: Targeting digitale
tags:
- OSINT
- processed
- targeting-digitale
date: '2026-05-15'
status: draft
depth: standard
tipo: concetto
---

title: "Targeting digitale"
tags: ["OSINT", "processed", "targeting-digitale"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "1"
tipo: "concetto"
---

# Targeting digitale

## 🎯 Sintesi Strategica

Il targeting digitale rappresenta una metodologia avanzata nell'ambito dell'[[Osint]] (Open Source Intelligence) che si concentra sull'identificazione, la profilazione e il monitoraggio di individui o entità aziendali attraverso l'analisi sistemica della loro Digital Footprint online. Questa disciplina si è evoluta da una raccolta di dati ampiamente accessibili a un ecosistema dove le informazioni personali sono spesso monetizzate e regolamentate, richiedendo approcci metodologici rigorosi e l'uso di identificatori specifici, noti come *selectors*, per navigare tra diverse fonti e piattaforme. L'obiettivo è costruire un quadro informativo completo e verificabile, partendo sempre da fonti aperte e replicabili.

## 📚 Contesto e Definizioni

Il targeting digitale si fonda sul principio che ogni soggetto lascia tracce online, intenzionalmente o meno. Questo processo investigativo aderisce al principio metodologico "Overt > Covert", privilegiando l'utilizzo di fonti aperte, documentabili e replicabili prima di considerare approcci più complessi.

*   **Targeting Digitale**: L'insieme di tecniche e metodologie volte a identificare, localizzare e raccogliere informazioni su un soggetto (individuo o entità) utilizzando dati disponibili pubblicamente sul web e in altre fonti aperte.
*   **Digital Footprint**: L'insieme di dati e attività che un individuo o un'organizzazione lascia dietro di sé attraverso l'uso di internet e dispositivi digitali. Si distingue in:
    *   **Attiva**: Generata da un comportamento consapevole del soggetto (es. profili social, post, commenti, portfolio online).
    *   **Passiva**: Generata da terzi o dall'infrastruttura tecnologica (es. privacy policy, data breach, metadati, risultati dei motori di ricerca).
*   **Selectors**: Identificatori unici o ricorrenti che consentono di "pivotare" tra diverse fonti di informazione. Esempi includono nomi, varianti di nomi, nickname, indirizzi email, numeri di telefono, username, fotografie, domini, handle social, ID univoci, indirizzi fisici o nomi di aziende. La persistenza e il riutilizzo dei selectors nel tempo sono fondamentali per la costruzione di un profilo coerente.

## 📊 Dati, Tecnologie e Metriche

Il processo di targeting digitale si avvale di una vasta gamma di dati e tecnologie. La raccolta e l'analisi si basano su un workflow strutturato e sull'impiego di strumenti specifici.

**Workflow Operativo OSINT:**
1.  **Definizione dell'Obiettivo**: Chiarire le domande operative e gli scopi dell'indagine.
2.  **Mappatura Informativa**: Identificare le informazioni disponibili e le lacune conoscitive.
3.  **Contestualizzazione**: Analizzare il contesto linguistico, culturale e geografico del target.
4.  **Identificazione Fonti**: Prioritizzare le fonti più rilevanti e quelle con dati deperibili.
5.  **Pianificazione**: Elaborare un piano di raccolta dati e di pivoting tra i selectors.
6.  **Esecuzione**: Applicare tecniche di ricerca avanzata (es. Google Dorks) e strumenti specialistici.
7.  **Documentazione**: Registrare la catena di evidenza per garantire replicabilità e verificabilità.

**Tecniche di Ricerca Avanzata (Google Dorks):**
*   `"username" @Facebook`
*   `"username" site:t.me`
*   `inurl:"username"`
*   `site:dominio filetype:pdf keyword`
*   `after:AAAA-MM-GG`
*   `site:un.org ("topic") after:YYYY-MM-DD filetype:pdf`

**Categorie Strumentali:**
*   **People Search**: Piattaforme per la ricerca di persone (es. Pipl, Epieos, OSINT Rocks, Have I Been Pwned, IntelligenceX, Dehashed).
*   **Username Analysis**: Strumenti per la verifica e la ricerca di username su diverse piattaforme (es. Instantusername, Sherlock, Bellingcat Name Variant Search).
*   **Phone/Email Intelligence**: Servizi per l'analisi di numeri di telefono e indirizzi email (es. Free-HLR, Truecaller, e-mail breach check, conversione di formati come E.164).
*   **Face Recognition**: Tecnologie per il riconoscimento facciale (es. Pimeyes, Search4Faces), da utilizzare con cautela data la distinzione tra similarità e identificazione certa.
*   **Geospatial Intelligence**: Strumenti per l'analisi geografica e SATellitare (es. NASA FIRMS per incendi, Openstreetmap, Wikimapia).

**Strumenti di Corporate Intelligence (BI/CI):**
*   **Openownership**: Registri centrali per la trasparenza proprietaria.
*   **Opencorporates**: Database di entità legali e società.
*   **The Org**: Organigrammi pubblici di aziende.
*   **North Data**: Analisi societaria, con focus su UK.
*   **Crunchbase**: Informazioni su startup, finanziamenti e investitori.
*   **SEC EDGAR**: Documenti aziendali di società quotate negli USA.
*   **Zefix**: Registri commerciali svizzeri.
*   **ICIJ**: Database su fughe di dati offshore (es. Panama Papers).
*   **Importyeti**: Dati su spedizioni e catene di fornitura USA.

## 🔍 Analisi Operativa ed Applicazioni OSINT

Il targeting digitale si applica sia a individui che a entità aziendali, seguendo principi analoghi ma con focus specifici.

**Targeting Individuale: Le Tre Domande Fondamentali:**
1.  **Chi è?**: Indaga l'identità reale o virtuale, le paure, gli affetti, la cultura, l'ideologia.
2.  **Cosa fa?**: Analizza l'impiego, la formazione, gli hobby, le comunità di appartenenza, gli spostamenti, le affiliazioni.
3.  **Cosa usa?**: Rileva i dispositivi, la presenza online, l'esposizione, i nickname, i numeri di telefono, gli indirizzi email, i profili social.

**Applicazioni di Corporate Intelligence (BI/CI):**
L'[[Corporate intelligence]] estende le metodologie OSINT alle entità aziendali. Il workflow tipico include:
*   Identificazione della società.
*   Consultazione di registri ufficiali per beneficial owners e reti societarie.
*   Analisi di amministratori e indirizzi ricorrenti.
*   Ricerca di brochure, fiere, domini e sottodomini.
*   Analisi geospaziale (mappe, SATellite).
*   Verifica di sanzioni e conformità.
*   Mappatura della supply chain e degli organigrammi.

L'efficacia del targeting digitale risiede nella capacità di costruire una "catena di evidenza" robusta, collegando un selector iniziale a piattaforme correlate, alias, email, profili professionali, localizzazioni e competenze, fino a ottenere conferme incrociate.

## 🔮 Lacune Informative e Prossimi Passi

Una sfida costante nel targeting digitale è la **deperibilità degli strumenti**: un tool oggi efficace potrebbe non esserlo domani a causa di cambiamenti nelle API, politiche delle piattaforme o chiusura dei servizi. Pertanto, è cruciale sviluppare un workflow metodologico che sia **replicabile e indipendente dagli strumenti specifici**, concentrandosi sui principi di raccolta e analisi piuttosto che sulla dipendenza da un singolo software. Le lacune informative possono emergere dalla mancanza di selectors univoci, dalla forte compartimentazione della Digital Footprint del target o da restrizioni legali e tecniche all'accesso ai dati. La ricerca futura si concentra sull'integrazione di tecniche avanzate di analisi dei dati e sull'adattamento a nuovi scenari di privacy e regolamentazione.

## 🔗 Connessioni e Pattern

- [[Applicazioni osint]]
- [[Corporate intelligence]]
- [[Motori di ricerca]]
- [[Osint]]
- [[Pianificazione]]
- [[Ricerca avanzata]]


- [[--]]
F/I/H
- [[--]]
