---
title: [[Waymore]]
tags:
- OSINT
- processed
- [[Waymore]]
date: '2026-05-15'
status: draft
depth: standard
sources: '1'
tipo: concetto
---

# [[Waymore]]

## 🎯 Sintesi Strategica

[[Waymore]] è uno strumento da riga di comando (CLI) scritto in Python, inizialmente sviluppato per la reconnaissance nel contesto del bug-bounty, ma ampiamente adottato dalla comunità [[Osint]] come aggregatore per la scoperta storica di domini. La sua funzione principale è estrarre simultaneamente URL storici da quattro repository pubblici eterogenei: [[Wayback machine]], [[CommonCrawl]], OTX Alienvault e [[urlscan.io]]. Questo approccio consolidato permette di superare le lacune di copertura dei singoli archivi, fornendo un inventario più completo delle versioni storiche e delle sottopagine di un dominio, anche quelle non più attive. A differenza di estrattori di URL puri, [[Waymore]] può scaricare integralmente il contenuto delle risposte archiviate, abilitando un'analisi approfondita di file, configurazioni e pagine rimosse.

## 📚 Contesto e Definizioni

[[Waymore]] si inserisce nella disciplina dell'[[Archiviazione forense]], un campo operativo che mira a trasformare le fonti aperte — intrinsecamente volatili, riscrivibili e deindicizzabili — in evidenze stabili, datate e ricostruibili. Per l'analista OSINT, la sfida non è solo individuare un contenuto, ma anche dimostrare la sua esistenza e forma in una data specifica. [[Waymore]] risponde a questa esigenza agendo come un punto di accesso aggregato a diversi archivi web, fornendo una "superficie storica" di un dominio. La sua adozione da parte della comunità OSINT sottolinea la necessità di strumenti capaci di consolidare dati da fonti disparate per una ricostruzione temporale affidabile, complementare ad altri strumenti di archiviazione come [[Archive.today]] e Save Page Now.

## 📊 Dati, Tecnologie e Metriche

[[Waymore]] è un'applicazione CLI basata su Python, disponibile su Github (xnl-h4ck3r/[[Waymore]]). Opera estraendo dati da quattro fonti principali:
*   **[[Wayback machine]] (web.archive.org)**: Fornisce snapshot HTTP/HTML completi di pagine web.
*   **[[CommonCrawl]]**: Un vasto corpus mensile di crawl globale del web, disponibile in formato [[Archiviazione forense|WARC]].
*   **OTX Alienvault**: Offre URL associati a Indicatori di Compromissione (IoC) e "pulses" di threat intelligence.
*   **[[urlscan.io]]**: Una sandbox per l'analisi di pagine web che produce file HAR e screenshot.

Lo strumento genera un output in formato JSON, contenente URL, timestamp di acquisizione e la fonte archivistica. Supporta il multi-threading per l'efficienza su domini di grandi dimensioni e offre un filtraggio personalizzabile per content-type, status code e response size. La modalità operativa `mode B` consente sia il recupero degli URL che il download integrale del loro contenuto archiviato, permettendo l'analisi di risorse come vecchi file Javascript, directory rimosse o configurazioni esposte.

## 🔍 Analisi Operativa ed Applicazioni OSINT

Il workflow operativo tipico con [[Waymore]] prevede l'identificazione di un dominio target, seguito dall'esecuzione di `[[Waymore]] -i target.tld -mode B` per ottenere un inventario completo di URL storici e il loro contenuto. L'output JSON viene poi sottoposto a triage manuale o integrato in pipeline downstream per ulteriori analisi, ad esempio tramite [[Web scraping]] o Selectors Pivoting.

Un'applicazione chiave è il "pivot [[Waymore]] → Wayback", dove [[Waymore]] agisce come uno scanner orizzontale per identificare la "superficie storica" di un dominio, mentre la [[Wayback machine]] viene utilizzata come "microscopio verticale" per studiare l'evoluzione temporale di specifici contenuti. Questo approccio permette di rispondere a domande cruciali come "quando una certa cosa è apparsa, quando è stata modificata, quando è stata rimossa, e cosa diceva la versione precedente?".

Un esempio operativo significativo, documentato come caso didattico, riguarda l'indagine su un exchange di criptovalute dismesso. Utilizzando [[Waymore]], un analista ha scoperto una pagina "/partners.html" non più presente sul sito live. Tramite la timeline della [[Wayback machine]], è stata recuperata una versione della pagina che elencava partner in giurisdizioni sanzionate (OFAC SDN) e un programma di donazioni collegato a reti di finanziamento estremiste. L'estrazione di wallet address da questa pagina archiviata ha permesso un pivot on-chain tramite [[Blockchain explorers|Etherscan]] e BlockINT, rivelando transazioni sospette e consolidando un'ipotesi investigativa. Questo caso dimostra come [[Waymore]] sia fondamentale per ricostruire evidenze apparentemente perdute e abilitare indagini complesse.

## 🔮 Lacune Informative e Prossimi Passi

[[Waymore]], pur essendo un potente aggregatore, eredita i limiti intrinseci delle sue fonti upstream. Se un contenuto non è stato catturato da nessuno dei quattro archivi integrati, [[Waymore]] non sarà in grado di recuperarlo. Questo sottolinea l'importanza dell'archiviazione preventiva e continuativa, complementare all'approccio retroattivo di [[Waymore]].

Le limitazioni generali dell'archiviazione web, come la difficoltà con i contenuti dietro paywall o login, le Single-Page Application (SPA) fortemente dipendenti da Javascript e il rispetto dei file `robots.txt`, influenzano indirettamente anche l'efficacia di [[Waymore]], poiché le sue fonti primarie sono soggette a tali restrizioni. Per mitigare queste lacune, l'analista deve integrare [[Waymore]] con strumenti di archiviazione locale come Archivebox o formati come [[WACZ]], che offrono maggiore controllo e capacità di cattura di contenuti dinamici o protetti, sebbene con la necessità di gestire autonomamente la [[Catena di custodia]].

## 🔗 Connessioni e Pattern

- [[Applicazioni osint]]
- [[Archiviazione forense]]
- [[Osint]]
- [[Tecnologie]]
- [[Threat intelligence]]
- [[Web scraping]]


- [[--]]
F/I/H
- [[--]]
