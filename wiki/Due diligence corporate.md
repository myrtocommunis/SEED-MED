---
title: Due diligence corporate
tags:
- OSINT
- processed
- due-diligence-corporate
date: '2026-05-15'
status: draft
depth: standard
sources: '1'
tipo: concetto
---

# Due diligence corporate

## 🎯 Sintesi Strategica

La due diligence corporate, supportata dall'[[Osint]] (Open Source Intelligence), è un processo investigativo sistematico e approfondito. Il suo obiettivo primario è valutare i rischi, le opportunità e la conformità di un'entità (azienda, individuo o gruppo) in contesti strategici quali M&A (fusioni e acquisizioni), investimenti, partnership commerciali o indagini interne. Questo processo si avvale di fonti aperte per costruire un profilo completo, coprendo aspetti legali, finanziari, reputazionali, operativi e, in contesti avanzati, anche l'analisi di asset digitali e blockchain.

## 📚 Contesto e Definizioni

La **due diligence corporate** si definisce come l'insieme delle attività di indagine e verifica condotte prima di prendere una decisione strategica o di finalizzare un accordo. La sua finalità è identificare e mitigare potenziali rischi, verificare l'accuratezza delle informazioni fornite e valutare in modo esaustivo gli asset e le passività di un'entità.

Questo processo trova applicazione in diversi ambiti:
*   **[[Business intelligence]]** e **[[Corporate intelligence]]**: per ottenere un [[Vantaggio Competitivo]] e supportare decisioni strategiche.
*   **Fusioni e Acquisizioni (M&A)**: per valutare la salute finanziaria, legale e operativa dell'azienda target.
*   **Valutazione di partner commerciali**: per assicurare l'affidabilità e la reputazione dei collaboratori.
*   **Indagini su frodi e conformità**: per identificare attività illecite o non conformi alle normative.

L'integrazione dell'[[Osint]] è fondamentale, poiché consente di accedere a un vasto spettro di informazioni pubblicamente disponibili, spesso non reperibili attraverso canali tradizionali, fornendo una visione olistica e aggiornata.

## 📊 Dati, Tecnologie e Metriche

La due diligence corporate basata su [[Osint]] si articola tipicamente in un workflow strutturato, sebbene adattabile alle specificità del caso. Un modello comune prevede 8 fasi principali:

1.  **Beneficial Owner e struttura societaria**: Identificazione dei titolari effettivi e della complessa architettura societaria tramite Registri commerciali e database globali come Opencorporates, North Data, ICIJ Offshore Leaks (per entità offshore), Companies House (UK) e ZEFIX (Svizzera).
2.  **Finanza, investimenti, brevetti/IP**: Analisi di dati finanziari, investimenti e proprietà intellettuale attraverso piattaforme come Orbis/BvD, SEC Edgar (USA) e Crunchbase.
3.  **Talent intelligence e key people**: Valutazione del capitale umano e delle figure chiave utilizzando strumenti come Theorg, Rocketreach e Linkedin.
4.  **Sanzioni, PEP (Politically Exposed Persons), attività controindicate**: Verifica contro liste ufficiali di sanzioni (UE, OFAC, ONU) e database di persone politicamente esposte, oltre a controlli di conformità (es. ANAC per l'Italia).
5.  **Negative media e segnali deboli**: Ricerca avanzata con identificativi univoci per individuare notizie avverse, controversie legali o "segnali deboli" che possano indicare rischi reputazionali o operativi.
6.  **Supply chain e appalti**: Mappatura della catena di approvvigionamento e analisi degli appalti tramite Importyeti (per dati USA) e portali di appalti pubblici (es. ANAC Portal).
7.  **Sedi operative e infrastrutture**: Geolocalizzazione e verifica delle sedi operative e delle infrastrutture fisiche con strumenti come Google Maps, Wikimapia e l'analisi di immagini SATellitari in tempo reale (es. NASA FIRMS).
8.  **Digital Footprint e tech stack**: Identificazione delle tecnologie utilizzate da un'entità e della sua impronta digitale complessiva con Builtwith.

Per la due diligence avanzata, in particolare per l'analisi di asset o attività finanziarie illecite, si integra l'**[[Blockchain]] e criptovalute**:
*   **Tassonomia degli asset**: Distinzione tra Coin (asset nativo di una blockchain come BTC, ETH), Token (asset generato da smart contract come USDT su Ethereum), Stablecoin (token ancorato a valute fiat) e Privacy coin (es. Monero).
*   **Wallet vs Indirizzo**: Comprensione della differenza tra un wallet (contenitore di chiavi) e gli indirizzi pubblici generati, e la distinzione cruciale tra wallet custodial (gestiti da terze parti come gli exchange) e non-custodial.
*   **[[Blockchain]]**: Utilizzo di strumenti specifici per tracciare transazioni e indirizzi su diverse blockchain (es. [[Arkham]] Intelligence, TONscan, [[Etherscan]], Blockchain.com, Blockchair, Debank, Metasleuth, Walletexplorer, [[BscScan]], [[Solscan]], [[Tronscan]]).
*   **Database frodi**: Consultazione di database collaborativi per identificare indirizzi associati ad attività fraudolente (es. Chainabuse.com, Scamsearch.com).

## 🔍 Analisi Operativa ed Applicazioni OSINT

L'applicazione dell'[[Osint]] nella due diligence corporate richiede un approccio metodologico flessibile, dove l'ordine delle fasi può essere adattato in base alle specificità del caso.

**Casi studio emblematici**:
*   **Bugatti**: Un'indagine ha dimostrato come l'[[Osint]] possa essere impiegata per la corporate intelligence, utilizzando la geolocalizzazione, Wikimapia, trascrizioni di video Youtube e l'analisi di "spotter" per ricostruire attività e asset di interesse.
*   **Nautica Alice / Nautica Number One**: Questo caso ha evidenziato l'importanza di identificare e correlare "segnali deboli" che, sebbene apparentemente insignificanti, possono indicare connessioni con attività di criminalità organizzata.

**Processo di [[Blockchain]] per la due diligence**:
1.  **Identificazione della blockchain**: Determinazione della rete (es. Bitcoin, Ethereum) tramite il prefisso dell'indirizzo.
2.  **Ricerca su explorer**: Utilizzo di [[Blockchain]] specifici per la rete identificata.
3.  **Distinzione custodial vs non-custodial**: Analisi per comprendere se l'indirizzo è controllato direttamente dall'entità o da un intermediario (exchange).
4.  **Verifica fraud DB**: Confronto degli indirizzi con database di frodi note.
5.  **Clustering**: RAGgruppamento di indirizzi che si presume siano controllati dalla stessa entità.
6.  **Attribuzione a entità**: Tentativo di collegare gli indirizzi clusterizzati a entità legali o organizzazioni, mantenendo la consapevolezza che l'attribuzione a individui fisici è complessa e spesso non possibile tramite sole fonti aperte.

**Vincoli legali**: È fondamentale considerare i quadri normativi. Ad esempio, in Italia, la vendita di informazioni commerciali può richiedere un'autorizzazione prefettizia (Art. 134 TULPS), un aspetto cruciale per la conformità. Nei report relativi alle criptovalute, è prassi indicare solo le unità cripto (es. "586 BTC"), evitando conversioni in valuta fiat per mantenere la neutralità e l'accuratezza.

## 🔮 Lacune Informative e Prossimi Passi

Nonostante l'ampia disponibilità di strumenti e metodologie, permangono alcune aree che richiedono ulteriore approfondimento o chiarimento:
*   **Riferimenti normativi**: È necessario precisare il riferimento normativo esatto per l'autorizzazione prefettizia in Italia, specificando l'Art. 134 del Testo Unico delle Leggi di Pubblica Sicurezza (TULPS).
*   **Fonti sanzioni**: Verificare e consolidare le fonti esatte e più aggiornate per i controlli sulle sanzioni internazionali e le liste PEP.
*   **Sintassi di ricerca avanzata**: Approfondire e documentare tecniche di ricerca avanzata specifiche per motori di ricerca e database per l'identificazione di indirizzi e blocchi informativi complessi.
*   **Flessibilità del workflow**: Chiarire ulteriormente le linee guida per l'adattamento dell'ordine delle 8 fasi del workflow di [[Business intelligence]] in base alla natura e agli obiettivi specifici di ciascuna due diligence.

## 🔗 Connessioni e Pattern

- [[Applicazioni osint]]
- [[Business intelligence]]
- [[Corporate intelligence]]
- [[Motori di ricerca]]
- [[Osint]]
- [[Ricerca avanzata]]


- [[--]]
F/I/H
- [[--]]
