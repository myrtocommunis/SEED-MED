---
title: Decision-making
tags:
- OSINT
- processed
- decision-making
date: '2026-05-15'
status: draft
depth: standard
sources: '1'
tipo: concetto
---

# Decision-making

## 🎯 Sintesi Strategica

Il **Decision-making** in contesti complessi e incerti è un processo iterativo fondamentale per la sopravvivenza e il successo di qualsiasi attore, sia esso individuale o istituzionale. Al centro di questo processo vi è la capacità di acquisire un [[Vantaggio decisionale]], ovvero la facoltà di decidere **prima**, **meglio** e **con più opzioni** rispetto agli avversari. Questo concetto è formalizzato nel [[Ciclo OODA]] (Observe-Orient-Decide-Act) di John Boyd, un framework di adattamento competitivo applicabile dalla strategia militare all'[[Analisi]]. L'obiettivo primario è ridurre il gap informativo e aggiornare le mappe mentali in un processo continuo, superando il principale ostacolo: i [[Bias cognitivo]] intrinseci all'analista e al decisore.

## 📚 Contesto e Definizioni

Il pensiero strategico moderno riconosce l'**incertezza** come una proprietà ontologica dei sistemi aperti, non un'anomalia. La conoscenza è intesa come un processo iterativo di distruzione e ricostruzione di modelli mentali, costantemente allineati con la realtà osservata. Questo approccio è cruciale nell'attuale ambiente strategico multipolare, caratterizzato da interdipendenza globale, proliferazione di attori non statali, rapida tecnologizzazione e guerre ibride.

Il termine **[[Intelligence operativa|Intelligence]]** deriva dal latino *«intelligere»* ("guardare dentro"), sottolineando la capacità di dare significato ai dati, connetterli e leggere oltre la superficie. La gerarchia informativa, che si sovrappone al modello DIKW (Data → Information → Knowledge → Wisdom), distingue sei livelli progressivi di processazione:

| Livello | Definizione Operativa | Stato di Processazione | Affidabilità Intrinseca |
|---|---|---|---|
| **Dato** | Insieme di fatti senza spiegazione o analisi | Zero | N/A |
| **Informazione** | Dati interpretati correttamente per dare significato utile in un contesto | Minimo (contesto applicato) | Medio (interpretazione non validata) |
| **Conoscenza** | Combinazione di informazione, esperienza e intuizione acquisita | Medio (sintesi esperienziale) | Alto (validato da esperienza) |
| **Open Source Data** | Dati generici provenienti da fonti pubbliche | Zero (raccolto) | Basso (nessun filtering) |
| **Open Source Information** | Dati conclusivi, filtrati da fonti aperte | Medio (filtrati) | Medio-Alto (filtrati ma non cross-validati) |
| **OSINT** | Informazioni filtrate e designate per uno scopo specifico | Alto (filtrate + distillate + disseminate) | Alto (processazione completa) |
| **Validated OSINT ([[NATO]])** | OSINT confermato da fonte non-OSINT o trusted | Massimo (cross-validazione) | Massimo (triangolazione) |

L'[[Intelligence operativa|Intelligence]] è una funzione sistemica dello Stato, con il compito di trasformare l'informazione in conoscenza, ridurre l'incertezza decisionale e collegare il livello tecnico a quello politico.

## 📊 Dati, Tecnologie e Metriche

Il Decision-making è supportato dall'analisi di dati provenienti da sei domini della guerra moderna, spesso interconnessi in uno schema piramidale (Mare, Terra, Aria, Spazio, Data/Dati, Cognitivo/Informatico):

| Dominio | Caratteristiche | Vettori OSINT Rilevanti | Esempi Operativi |
|---|---|---|---|
| **Terra** | Confini terrestri, movimento truppe, infrastrutture | SATellite imagery, social media geolocalizzati, open data territoriali | Prove SATellitari Ucraina 2022 |
| **Mare** | Rotte commerciali, traffici illeciti, zone economiche esclusive | AIS/shipping data, open port data, corporate registries | Tracciamento petroliere nordcoreane |
| **Aria** | Spazio aereo, movimentazione aerei governativi e militari | ADS-B open data, flight tracking APIs, registri aeronautici | Monitoraggio aerei VIP iracheni/iraniani |
| **Spazio** | SATelliti commerciali e militari, Orbital debris | SATellite imagery (Maxar, Planet), registri orbitali UN COPUOS | Verifica test missilistici nordcoreani |
| **Cyber** | Attacchi informatici, infrastrutture critiche digitalizzate | Shodan/CENSys scans, exploit databases, breach data, dark web monitoring | Attribution attacchi ransomware |
| **Cognitivo/Informativo** | Disinformazione, operazioni psicologiche, narrazioni dominanti | SOCINT, network analysis, cross-platform tracking, bot farm detection | Campagne disinformazione pre-conflitto |

Il SISR (Sistema di Informazione per la Sicurezza della Repubblica) è l'attore istituzionale preposto a generare il [[Vantaggio decisionale]] per il decisore politico, attraverso le agenzie DIS, AISE e AISI, operando entro i limiti normativi (es. Legge 124/2007, Legge 150/2000).

Il [[Vantaggio decisionale]] si articola in una triade Boydiana:

| Dimensione | Descrizione | Implicazione OSINT |
|---|---|---|
| **Decidere PRIMA** | Ridurre il tempo tra osservazione e azione rispetto all'avversario | Automation d'analisi, preprocessing dati, alerting proattivo |
| **Decidere MEGLIO** | Accrescere la qualità e accuratezza dell'intelligence | Cross-source validation, tecniche di analisi strutturata, bias mitigation |
| **Decidere con PIÙ OPZIONI** | Offrire alternative di policy non previste dall'avversario | Scenario planning, Devil's Advocate, analisi delle ipotesi alternative |

Il pensiero strategico si può categorizzare in tre "colori":
*   **Verde:** massimizzare l'uso delle risorse disponibili, in assenza di interazione con il dominio.
*   **Blu:** interazione e cooperazione, ricerca di convivenza e alleanze.
*   **Rosso:** conflitto e competizione per le risorse.
La sicurezza nazionale implica la gestione di questi livelli per tutelare lo status quo e il benessere.

## 🔍 Analisi Operativa ed Applicazioni OSINT

Il [[Ciclo OODA]] è un modello dinamico a quattro fasi:

#### FASE 1: Observe — Osservare

Questa fase riguarda la raccolta di dati grezzi e segnali dall'ambiente strategico.

| Sott-fase | Descrizione | Output OSINT | Bias Correlato |
|---|---|---|---|
| Raccolta passiva | Monitoraggio continuo di fonti aperte senza interazione | Feed di dati grezzi | Bias di disponibilità |
| Raccolta attiva | Query mirate, scraping, crawling | Dataset strutturato | Bias di conferma (selezione mirata) |
| Monitoraggio attivo | Sorveglianza di soggetti specifici | Tracking timeline | Illusione di RAGgruppamento |
| Crowdsourcing | Raccolta da fonti collaborative (cittadini, giornalisti) | Dati geolocalizzati, timestampati, verificabili | Bias di conferma (filtraggio comunitario) |

L'efficacia si misura nella copertura degli indicatori rispetto al rumore. I metadati sono una fonte primaria di osservazione, ma possono essere manipolati (stripping, cleaning, spoofing).

#### FASE 2: Orient — Orientare

Questa è la fase più critica, dove i dati grezzi vengono interpretati e trasformati in conoscenza. Implica la decostruzione delle vecchie mappe mentali e la costruzione di nuove, più aderenti alla realtà. È qui che i [[Bias cognitivo]] rappresentano il rischio maggiore.

##### Bias Cognitivi: Tassonomia Completa per l'Analista OSINT

| Bias | Meccanismo Cognitivo | Manifestazione OSINT | Contrasto Strutturato | Impatto su Intelligence |
|---|---|---|---|---|
| **Bias di conferma** | Cercare e valorizzare solo informazioni che confermano le proprie ipotesi | Seleziona dorks e fonti che "confermano" la tesi; ignora contro-evidenza | **Avvocato del Diavolo** | ALTO |
| **Bias di disponibilità** | Giudizio basato su esempi facilmente richiamabili alla memoria | Sovra-rappresenta eventi recenti o emotivamente forti | **[[Metodo Delphi]]** | MEDIO |
| **Illusione di RAGgruppamento** | Percezione di pattern o connessioni anche dove non esistono | Trova "correlazioni" tra eventi casuali | **Diagramma di Ishikawa** | ALTO |
| **Bias di ancoraggio** | Dipendenza eccessiva dalla prima informazione ricevuta | Il primo report condanna le analisi successive | **Premortem** | MEDIO |
| **Bias di gruppo ([[Groupthink]])** | Pressione verso il consenso in gruppo | Dissensi vengono sopressi | **[[SAT]] / Red Team** | ALTO |
| **Bias dell'iper-razionalità** | Sottovalutare fattori umani/emotivi | Analizza solo dati quantitativi | **Analisi multi-dominio** | MEDIO |
| **Bias della narrazione coerente** | Preferenza per storie belle e coerenti | Costruisce narrazioni eleganti ignorando dati contraddittori | **Analisi alternativa** | ALTO |
| **Bias della disponibilità tecnica** | Sovraffidamento sugli strumenti disponibili | Usa dorks per tutto, anche dove non appropriato | **Meta-analisi degli strumenti** | MEDIO |
| **Costi affrontati (sunk cost)** | Persistere in una tesi per gli investimenti già fatti | Ignora nuove evidenze per non invalidare lavoro pregresso | **Revisione periodica delle ipotesi** | MEDIO |
| **Overconfidence** | Sopravvalutare la propria precisione di stima | Presenta stime con eccessiva certezza | **Calibrazione delle probabilità** | MEDIO |
| **Negativity Bias come sistema** | Tendenza algoritmica a privilegiare contenuti negativi | Amplificazione di narrazioni allarmistiche | **Analisi del sentiment e della propagazione** | MEDIO |
| **Goodhart's Law** | "Quando una misura diventa un target, cessa di essere una buona misura." | Metriche di engagement (es. pageviews) distorcono la qualità del contenuto | **Ridefinizione degli indicatori di successo** | ALTO |

È fondamentale distinguere tra correlazione e causalità: la correlazione indica che due variabili si muovono insieme, mentre la causalità implica che una variabile ne produce un'altra.

L'**inganno attivo** (es. [[Maskirovka]] russa, Content Injection, Malinformation) è una sfida costante, richiedendo cross-validazione e analisi forense.

#### FASE 3: Decide — Decidere

Questa fase implica la formulazione di ipotesi, la valutazione di opzioni e la selezione di un corso d'azione. L'analista produce opzioni, il decisore politico sceglie.

#### FASE 4: Act — Agire

L'azione è l'implementazione della decisione. Nel contesto intelligence, include la disseminazione delle informazioni e il feedback, che a sua volta alimenta la fase di Observe successiva, chiudendo il [[Ciclo OODA]].

##### Tecniche di Analisi Decisionale e Contrasto alla Disinformazione:

*   **[[Metodo Delphi]]**: Protocollo di consensus-building strutturato per scenari di alta incertezza, che evita il [[Groupthink]] tramite cicli di feedback facilitati tra esperti indipendenti.
*   **Diagramma di Fishbone (Ishikawa)**: Schema a lisca per analisi causa-effetto strutturata, utile per mappare le cause profonde dei [[Bias cognitivo]] e delle failure intellettive.
*   **36 Stratagemmi Cinesi**: Repertorio di pattern di inganno strategico, utilizzabile per riconoscere le trame dell'avversario.
*   **Framework EU FIMI (Foreign Information Manipulation and Interference)**: Classifica gli attori in Official State Channels, State-Controlled Outlets, State-Linked Channels e State-Aligned Channels, con il [[Proxy]] come tecnica dominante.
*   **Metodologia [[NATO]] (ABCDE + DISARM + 5D+F)**:
    *   **ABCDE**: Attribuzione (Actor, Behaviour, Content, Degree, Effect).
    *   **DISARM**: Classificazione del comportamento (Planning, Preparation, Execution, Evaluation).
    *   **5D+F**: Analisi degli obiettivi (Dismiss, Distort, Distract, Dismay, Divide, Degrade, Facilitate State Propaganda).
*   **Triangolo della Disinformazione**: Distingue tra Misinformation (falso, nessun intento dannoso), Disinformation (falso, intento dannoso) e Malinformation (vero, intento dannoso).
*   **Tipologie di Contenuti per Gravità**: Classifica i contenuti da SATira a manipolati (deepfake), in base all'intento ingannevole e al rischio.

## 🔮 Lacune Informative e Prossimi Passi

Nonostante la robustezza del framework, permangono alcune lacune:
*   **Applicazioni quantitative dell'OODA**: Mancano metriche misurabili del tempo di completamento del ciclo, rendendo difficile quantificare il "vantaggio decisionale".
*   **Analisi neuroscientifiche dei bias**: I [[Bias cognitivo]] sono elencati ma non approfonditi scientificamente nei loro meccanismi sottostanti.
*   **Integrazione OSINT-SIGINT/HUMINT**: Il quadro delle diverse discipline intelligence è descrittivo ma non offre indicazioni operative concrete sull'integrazione all-source.
*   **Quantum computing e futuro dell'OSINT**: L'impatto della crittoanalisi quantica sulle fonti OSINT crittografate non è stato esplorato.

I prossimi passi includono l'integrazione con metodologie operative concrete, l'arricchimento con casi studio quantificati, il collegamento all'analisi delle [[Osint]] e la validazione cross-domain in scenari ibridi.

## 🔗 Connessioni e Pattern

- [[Ciclo OODA]]
- [[Foreign Information Manipulation and Interference]]
- [[Maskirovka]]
- [[Sistema di informazione per la sicurezza della Repubblica]]
- [[Tecniche di analisi strutturata]]
- [[Vantaggio decisionale]]


- [[--]]
F/I/H
- [[--]]
