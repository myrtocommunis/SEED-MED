---
title: Algoritmi di retrieval
tags:
- OSINT
- processed
- algoritmi-di-retrieval
date: '2026-05-15'
status: draft
depth: standard
tipo: concetto
---

**Nota metodologica**: Il corpus sorgente non contiene riferimenti espliciti al concetto di "Algoritmi di retrieval". La presente nota estrae esclusivamente le informazioni operative, i vincoli e le caratteristiche di recupero delle informazioni direttamente menzionate nel documento, in conformità al principio di rifiuto della fabbricazione.

== Descrizione ==
Nel contesto degli strumenti di ricerca e del corpus OSINT analizzato, i meccanismi di recupero delle informazioni sono governati da un ecosistema domiNATO da motori mainstream e da una rete di motori verticali. La distribuzione del mercato è caratterizzata da una predominanza di Google, che detiene una quota di mercato del 91% (dati Statista 2024). Il recupero delle informazioni è soggetto a limiti strutturali che distinguono la superficie web dalla rete profonda, con una stima tradizionale del 4-5% per la superficie web (riferimento storico Alex 2000, non aggiorNATO al 2026).

== Meccanismi di interrogazione e parsing ==
Il recupero dei risultati avviene attraverso l'elaborazione di operatori di ricerca e combinazioni operative. Il nodo analizzato include una tabella di 12 operatori con funzioni ed esempi, identificata come valore operativo principale per la formulazione delle query. Le combinazioni operative e l'uso del Google Hacking Database (GHDB) sono confermati come strumenti per l'interrogazione mirata. Motori specializzati come Shodan (per la ricerca IoT) e Yandex (con capacità superiori per l'immagine inversa su soggetti russi/europei) utilizzano meccanismi di recupero differenziati rispetto ai motori generalisti.

== Vincoli strutturali e di ranking ==
I risultati di retrieval sono influenzati da fattori che ne modificano la visibilità e l'ordinamento:
* **Deindicizzazione**: rimozione di contenuti dagli indici dei motori, che riduce la superficie recuperabile.
* **Personalizzazione e bias**: algoritmi di ranking adattivi che filtrano e ordinano i risultati in base al profilo utente, introducendo distorsioni sistematiche nel recupero delle informazioni.
* **Limiti di copertura**: la distinzione tra surface web e deep web definisce i confini fisici e tecnici del recupero, con dati storici non aggiornati che ne sottostimano l'evoluzione recente.

== Ecosistema e integrazione ==
I meccanismi di retrieval operano come input fondamentale per pipeline OSINT, integrandosi con strumenti di scraping/API e flussi ETL verso modelli linguistici (LLM). Il corpus cataloga 30 motori verticali (credenziali, DNS, IoT, threat intel, archivi, email, Wifi, dark web, URL, vulnerabilità, codici, accademici, crimine finanziario), ciascuno con protocolli di recupero specifici. La fonte primaria dell'elenco dei 30 motori e la tabella degli operatori (citata come "G. Me, lezione 29/11/2025") risultano non verificabili online, richiedendo cautela nella validazione dei parametri di retrieval associati.

== Verifiche e riferimenti ==
* Quota di mercato Google 91%: Statista 2024 ✓
* Stima surface web ~5%: Alex 2000 "Deep Web" (riferimento storico consolidato) ✓
* GHDB exploit-db: confermato ✓
* Shodan IoT search: confermato ✓
* Yandex reverse image: confermato superiore per ambito geografico russo/europeo ✓
* Fonti "G. Me, lezione 29/11/2025" e "30 engine OSINT from slides": non verificabili online ✓

== Collegamenti ==
* [[Osint nella sicurezza nazionale]]
