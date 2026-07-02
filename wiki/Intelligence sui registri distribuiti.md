---
title: Intelligence sui registri distribuiti
tags:
- OSINT
- processed
- intelligence-sui-registri-distribuiti
date: '2026-05-15'
status: draft
depth: standard
sources: '1'
tipo: concetto
---

# Intelligence sui registri distribuiti

## 🎯 Sintesi Strategica

L'**Intelligence sui registri distribuiti**, nota anche come **BlockINT**, è una disciplina dell'[[Osint]] che si concentra sull'estrazione, analisi e interpretazione di dati provenienti da [[Blockchain]] pubbliche e altri registri distribuiti. Il suo obiettivo primario è trasformare il [[Pseudonimato]] on-chain in attribuzioni off-chain, collegando indirizzi crittografici a entità o individui reali. Sfruttando la natura pubblica, immutabile e trasparente di queste tecnologie, la BlockINT fornisce prove tecniche irrefutabili, complementando l'OSINT tradizionale per un'attribuzione completa e contestualizzata.

## 📚 Contesto e Definizioni

La **BlockINT** si definisce come l'intelligence applicata alle blockchain e ai registri distribuiti. A differenza dell'OSINT tradizionale, che si basa su fonti off-chain (social media, documenti, immagini), la BlockINT opera esclusivamente su dati on-chain, quali transazioni, smart contract, pattern di wallet e metadati di rete. L'integrazione di BlockINT e OSINT off-chain è cruciale per ottenere un'attribuzione completa, dove la blockchain fornisce la prova tecnica e l'OSINT il contesto umano.

Le **proprietà fondamentali** della blockchain che la rendono una fonte primaria per l'intelligence sono:
*   **Pubblica**: Tutte le transazioni sono visibili e liberamente consultabili.
*   **Immutabile**: I dati sono permanenti e non possono essere alterati retroattivamente.
*   **Distribuita**: L'assenza di un server centrale la rende resistente alla censura e agli attacchi.
*   **Pseudo-anonima**: Gli indirizzi sono visibili, ma il titolare è sconosciuto. Ogni errore di OPSEC (Operational Security) può creare un collegamento permanente e pubblico tra un indirizzo e un'identità reale.
*   **Trasparente**: Transazioni e asset sono visibili, ribaltando il modello bancario tradizionale.

La sfida principale della BlockINT non è la disponibilità del dato, ma la sua interpretazione e la capacità di superare il pseudo-anonimato.

## 📊 Dati, Tecnologie e Metriche

Gli **oggetti analizzabili** nella BlockINT includono:
*   **Indirizzi**: Chiavi pubbliche (es. `0x...`, `bc1...`) che fungono da punti di partenza per le investigazioni.
*   **Transazioni**: Movimenti di valore tra indirizzi, con timestamp e commissioni, essenziali per il tracciamento dei flussi di fondi.
*   **Token**: Asset generati tramite smart contract (es. ERC-20, NFT), rilevanti per il tracciamento di asset specifici o fenomeni come il *wash trading*.
*   **Smart Contract**: Codice eseguibile sulla blockchain, analizzabile per identificare vulnerabilità o comportamenti malevoli.
*   **Wallet Cluster**: Gruppi di indirizzi che si presume appartengano alla stessa entità, ricostruiti tramite euristiche.

Le **tipologie di asset crypto** rilevanti per l'intelligence includono:
*   **Coin**: Asset nativi di una blockchain (es. BTC, ETH), principali per il tracciamento.
*   **Token**: Asset emessi su una blockchain tramite smart contract (es. USDT su Ethereum).
*   **Stablecoin**: Token il cui valore è ancorato a una valuta fiat (es. USDT 1:1 USD), utili per il tracciamento finanziario.
*   **Privacy Coin**: Criptovalute progettate per offrire anonimato completo (es. [[Monero]] (XMR)), rendendo il rilevamento e il tracciamento estremamente difficili.

Le **tecniche di Crypto Attribution** mirano a collegare un indirizzo crypto a un'identità reale:
1.  **Heuristiche di Clustering**:
    *   *Co-spend heuristic*: Indirizzi che spendono gli stessi UTXO (Unspent Transaction Outputs) appartengono allo stesso proprietario.
    *   *Change address heuristic*: Identificazione dell'indirizzo di "resto" in una transazione.
    *   *Common input heuristic*: UTXO usati in una transazione appartengono allo stesso proprietario.
    *   *Behavioral clustering*: Analisi di pattern di timing, importi e policy delle commissioni.
2.  **Tagging di Indirizzi Noti**: Utilizzo di database commerciali come [[Intelligence sui registri distribuiti|Arkham Intelligence]], [[Blockchain explorers|Etherscan]], [[Blockchain explorers|Blockchair]] o liste di sanzioni (es. OFAC SDN list) per etichettare indirizzi noti (exchange, mixer, gruppi criminali).
3.  **Analisi del Flusso**: Tracciamento dei fondi attraverso transazioni successive, inclusi i *bridge cross-chain* e i *DEX (Decentralized Exchanges)*.
4.  **Off-chain Enrichment**:
    *   *[[Aml-cft|KYC]] (Know Your Customer) presso exchange*: Collaborazione con le forze dell'ordine per ottenere l'identità reale associata a un indirizzo.
    *   *[[Ethereum]]*: Nomi leggibili (`.eth`) mappati a wallet, che possono fornire un collegamento identitario.
    *   *Airdrop footprint*: Utenti che pubblicano indirizzi sui social media per partecipare a distribuzioni.
    *   *Google Dorks*: Ricerca di indirizzi su forum, post o documenti pubblici.
    *   *TON+Telegram*: Unico canale di attribuzione che permette di risalire al profilo Telegram associato a un indirizzo TON tramite TON Scan.
    *   *Crypto Dusting*: Tecnica attiva che consiste nell'invio di piccole quantità di criptovaluta a numerosi indirizzi per tracciarne i movimenti e identificare i proprietari.

## 🔍 Analisi Operativa ed Applicazioni OSINT

La **pipeline operativa BlockINT** si articola in quattro fasi:
1.  **Identificazione e Analisi dell'Indirizzo**: Utilizzo di explorer come [[Intelligence sui registri distribuiti|Arkham Intelligence]] (per attribuzione a entità note), Debank (explorer multichain EVM), Blockscan (esportazione CSV) o Walletexplorer (specifico Bitcoin).
2.  **Address Clustering**: Piattaforme come [[Arkham]] o Walletexplorer per RAGgruppare indirizzi correlati.
3.  **Visualizzazione Flussi**: Strumenti come Metasleuth per grafici visuali delle transazioni.
4.  **Digital Footprint Web**: Database come Chainabuse.com o Scamsearch.io per indirizzi segnalati, e TON Scan per il collegamento Telegram.

**Google Dorks** specifici per indirizzi crypto:
```
"[INDIRIZZO]" -block
site:[dominio].[TLD] "[INDIRIZZO]"
site:*.gov.* "[INDIRIZZO]"
```
L'uso di **REGEX** è fondamentale per estrarre indirizzi da grandi quantità di testo.

**Framework Regolatorio e Implicazioni:**
Il **[[Aml-cft|FATF]] (Financial Action Task Force)** stabilisce standard anti-riciclaggio (AML) e anti-finanziamento del terrorismo (CFT) applicabili alle criptovalute. La **Travel Rule** impone ai VASP (Virtual Asset Service Provider) di trasmettere informazioni su mittente e destinatario per transazioni sopra una certa soglia. I **VASP** (exchange, wallet provider, OTC) sono considerati "choke point" legali, in quanto l'obbligo di [[Aml-cft|KYC]] li rende un pivot per la de-anonimizzazione.
Strumenti di privacy come [[Tornado Cash]], uno smart contract per l'anonimizzazione delle transazioni, sono stati sanzionati dall'OFAC nel 2022, evidenziando la tensione tra privacy e regolamentazione.

**Chain of Custody per BlockINT:**
La raccolta di evidenze on-chain richiede una rigorosa catena di custodia:
*   **Identificazione**: Documentare indirizzo, hash transazione, timestamp (es. tramite explorer).
*   **Preservazione**: Screenshot con timestamp, esportazione dati, hashing.
*   **Documentazione**: Catalogare tutti i passaggi di attribuzione con fonti e data.
*   **Autenticazione**: Verificare l'integrità dei dati on-chain tramite l'hash della transazione sulla blockchain.
Il grado di certezza varia da "Certezza" (prova on-chain + KYC exchange) a "Collegamento debole" (solo pattern senza corroborazione esterna).

**Implicazioni Operative:**
*   La blockchain è una fonte primaria, con dati verificabili indipendentemente e un peso probatorio superiore.
*   Lo pseudo-anonimato non è anonimato; ogni errore di OPSEC crea un link permanente.
*   È cruciale distinguere tra *deposit address* (di un exchange) e *wallet self-hosted*.
*   Gli aggregatori (es. [[Arkham]]) sono spesso più efficaci degli explorer nativi per l'investigazione.
*   Tutte le attribuzioni automatiche devono essere verificate con dati indipendenti.
*   Il binomio TON+Telegram rappresenta un canale di attribuzione unico e sottovalutato.
*   La BlockINT complementa l'OSINT off-chain, non la sostituisce.

## 🔮 Lacune Informative e Prossimi Passi

Nonostante i progressi, l'intelligence sui registri distribuiti presenta diverse lacune e sfide:
*   **Privacy Coin**: Criptovalute come [[Monero]] o le transazioni schermate di Zcash rendono l'analisi on-chain estremamente difficile o impossibile, limitando la capacità di tracciamento.
*   **Mixer e Tumbler**: L'uso sofisticato di mixer (es. Wasabi Wallet, Samourai) può rendere la ricostruzione dei flussi di fondi solo probabilistica, non deterministica.
*   **False Attribuzioni**: Le etichette automatiche nei database di attribuzione sono spesso probabilistiche e non sempre verificate. Un'attribuzione errata può portare a inferenze investigative fuorvianti, rendendo la corroborazione indipendente un passo critico.
*   **Custodial vs. Self-Custody**: I wallet di exchange aggregano migliaia di utenti, e l'attribuzione si ferma all'exchange, non al singolo utente, a meno di procedimenti legali.
*   **Evoluzione del panorama Defi/NFT**: I protocolli di finanza decentralizzata e i token non fungibili introducono nuove complessità e vettori emergenti per il riciclaggio di valore o il *money muling*, richiedendo tecniche analitiche in continua evoluzione.
*   **Vincoli Giuridici**: La natura pseudonima dei wallet solleva questioni sulla qualificazione dei dati come "personali" e sull'ammissibilità giudiziale delle evidenze on-chain, che richiede una formale Chain of Custody.

L'obiettivo della BlockINT è primariamente attribuire un indirizzo a un'entità (exchange, gruppo criminale, organizzazione), mentre l'attribuzione a un singolo individuo fisico rimane spesso compito delle forze dell'ordine con procedimenti penali.

## 🔗 Connessioni e Pattern

- [[Applicazioni osint]]
- [[Blockchain]]
- [[Catena di custodia]]
- [[Criptovaluta]]
- [[Osint]]
- [[Piattaforme]]


- [[--]]
F/I/H
- [[--]]
