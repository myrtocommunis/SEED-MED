---
title: Inchieste blockchain cross-domain
tags:
- OSINT
- processed
- inchieste-blockchain-cross-domain
date: '2026-05-15'
status: draft
depth: standard
tipo: concetto
---

**Inchieste blockchain cross-domain** è un approccio analitico che integra le metodologie della Business Intelligence (BI) corporativa con le tecniche di investigazione su blockchain pubbliche, focalizzandosi sul tracciamento dei flussi di valore (capitali, informazioni e potere) attraverso reti apparentemente anonime o pseudonime. Il concetto emerge dalla convergenza tra due domini tradizionalmente distinti: l'intelligence aziendale per il settore privato e l'analisi delle criptovalute, unificati da un requisito metodologico comune: l'attribuzione di attività a entità controllanti piuttosto che a persone fisiche.

== Fondamenti concettuali ==
Le inchieste blockchain cross-domain si basano sul principio che l'anonimato o [[Pseudonimato]] non impedisce l'analisi, ma ne definisce la sfida principale. Il focus investigativo si sposta dalla ricerca dell'identità fisica diretta all'identificazione dell'entità giuridica o operativa che controlla un indirizzo o una rete. Questo approccio richiede un metodo strutturato che privilegi la logica investigativa rispetto alla disponibilità degli strumenti tecnici.

== Convergenza con la Business Intelligence ==
Il quadro analitico evidenzia una forte convergenza tra BI corporativa e blockchain investigation:
* **Reti di riferimento**: le BI operano su reti societarie, mentre le inchieste cross-domain analizzano reti blockchain.
* **Attribuzione**: il concetto di *beneficial owner* nella BI corrisponde all'attribuzione di un indirizzo crypto a un'entità controllante.
* **Sfida analitica**: entrambi i domini affrontano l'anonimato/[[Pseudonimato]] come ostacolo da superare tramite correlazione di dati.
* **Fonti primarie**: l'open source è la base comune (registri pubblici e open corporates per la BI; blockchain explorer per le crypto).
* **Primato del metodo**: in entrambi i contesti, la struttura investigativa prevale sugli strumenti specifici.

== Caratteristiche strutturali ==
Le differenze tra i due domini integrati sono definite da:
* **Regime giuridico**: la BI è soggetta a normative come il TULPS (art. 134), [[GDPR]] e AI Act, mentre l'analisi di blockchain pubbliche non prevede un regime normativo specifico dedicato.
* **Natura della fonte**: i registri commerciali possono essere modificati o rimossi, mentre i dati su blockchain sono intrinsecamente immutabili.
* **Identità**: le reti societarie nascondono persone reali dietro entità registrate, mentre le blockchain operano con indirizzi pseudonimi senza legame diretto con l'identità fisica.
* **Strumenti**: la BI utilizza piattaforme come Orbis, North Data e Crunchbase, mentre le inchieste cross-domain impiegano explorer e tool di clustering come [[Arkham]], [[Etherscan]], Blockchair e [[BscScan]].

== Metodologia analitica ==
Il workflow investigativo si articola su tre pivot concettuali:
1. **Attribuzione dell'entità**: analogo al *beneficial owner* corporate, mira a identificare il controllo effettivo dietro un indirizzo o un wallet.
2. **Correlazione di segnali deboli**: i *weak signals* della BI (es. variazioni societarie, assunzioni) corrispondono ai pattern di transazione blockchain (movimenti tra exchange, clustering temporale), dove segnali individualmente inconcludenti formano un quadro diagnostico collettivo.
3. **Analisi dell'infrastruttura**: il *tech stack fingerprinting* aziendale è concettualmente parallelo all'analisi degli smart contract, rivelando intenti operativi e vulnerabilità attraverso l'infrastruttura tecnica sottostante.

== Quadro normativo ed etico ==
Un punto critico delle inchieste cross-domain è la distinzione tra fattibilità tecnica e liceità giuridica. In Italia, la raccolta di informazioni a nome di terzi nel settore privato richiede un'autorizzazione prefettizia ex art. 134 del TULPS. Le inchieste blockchain, tuttavia, operano su fonti pubbliche e permissionless, rappresentando una delle rare aree in cui l'analisi OSINT non richiede autorizzazioni preventive, purché si rispetti la distinzione tra PAI, CAI e OSINT. La permanenza dei dati on-chain e la loro accessibilità permessiva ne fanno un dominio a basso rischio normativo per l'investigazione open source.

== Strumenti e tecniche ==
L'ecosistema tooling si divide tra:
* **Registri e database**: Opencorporates, ZEFIX, Companies House, SEC Edgar, Orbis, North Data, Crunchbase.
* **Blockchain explorer e clustering**: [[Arkham]], [[Etherscan]], [[Solscan]], Debank, Blockchair, [[BscScan]], Metasleuth.
* **Tecniche operative**: address analysis, wallet clustering, attribution, negative media search, analisi di pattern transazionali e smart contract.

== Collegamenti correlati ==
* [[Tecniche]]
* [[Blockchain]]
* [[Blockchain]]
* [[Strumenti]]
* [[Etica]]
* [[Bias cognitivo]]
* [[Tracciamento blockchain]]
* [[Investigazione indirizzi crypto]]
* [[Analisi]]
