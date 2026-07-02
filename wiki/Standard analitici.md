---
title: Standard analitici
tags:
- OSINT
- processed
- standard-analitici
date: '2026-05-15'
status: draft
depth: standard
sources: '1'
tipo: concetto
---

# Standard analitici

## 🎯 Sintesi Strategica

Gli **Standard analitici** definiscono i criteri e le metodologie per la produzione di intelligence, garantendo coerenza, riproducibilità e affidabilità. L'**ICS 206-01** (*Intelligence Community Standard*), emaNATO dal *Director of National Intelligence* (DNI) degli Stati Uniti il 12 dicembre 2024, rappresenta un'iniziativa cardine per la professionalizzazione e la standardizzazione della disciplina [[Osint]] a livello normativo internazionale. Questo standard impone a tutti gli elementi della U.S. Intelligence Community (IC) di citare e referenziare in modo uniforme le [[Pai]] (*Publicly Available Information*), le [[Cai]] (*Commercially Available Information*) e gli [[Osint]] in ogni prodotto analitico dissemiNATO.

I punti salienti dell'ICS 206-01 includono:
1.  **Integrazione delle fonti**: Eliminazione della distinzione di classificazione tra PAI, CAI e OSINT, ora integrati con citazioni full-structured (*SRC — Source Reference Citation*).
2.  **Tassonomia dei prodotti OSINT**: Distinzione chiara tra *stand-alone analytic product* (posizione analitica coordinata IC) e *other stand-alone product* (osservazioni fattuali, curation, geolocalizzazione).
3.  **Trasparenza AI/ML obbligatoria**: Requisito di citare output di [[Llm|AI]], sistemi di Computer Vision, prompt generativi e dataset di addestramento come elementi dell'SRC.

Questo standard ha un impatto geostrategico significativo, influenzando i framework OSINT di organizzazioni come [[NATO]], UE e alleati Five Eyes.

## 📚 Contesto e Definizioni

L'ICS 206-01 non emerge in un vuoto normativo, ma si inserisce in una catena di autorità che parte dal National Security Act (1947) e dall'Executive Order 12333 (*United States Intelligence Activities*), che fornisce la base giuridica per il DNI di emanare direttive e standard vincolanti. L'Intelligence Community Directive (ICD) 206 conferisce autorità vincolante all'ICS 206-01 sui prodotti analitici IC, sostituendo la versione precedente del 2017.

Le definizioni chiave secondo l'ICS 206-01 sono:

*   **PAI (Publicly Available Information)**: Informazioni pubblicate o trasmesse per il consumo pubblico, accessibili online o via abbonamento, osservabili da chiunque (es. notizie, open data governativi, report accademici, social media pubblici).
*   **CAI (Commercially Available Information)**: Dati o informazioni normalmente venduti, affittati o concessi in licenza a membri del pubblico o entità non governative (es. database commerciali, dataset a pagamento, report di settore premium).
*   **OSINT (Open Source Intelligence)**: Intelligence derivata esclusivamente da PAI/CAI che risponde a priorità, requisiti o lacune specifiche dell'intelligence. Non è mera "informazione" ma "intelligence", con un valore aggiunto analitico distintivo.
*   **AI (Artificial Intelligence)**: Sistema basato su macchine che, per obiettivi definiti dall'uomo, formula previsioni, raccomandazioni o decisioni che influenzano ambienti reali o virtuali (15 U.S.C. § 9401(3)). Ogni sistema AI utilizzato in un flusso di lavoro analitico IC deve essere citato nell'SRC come "fonte di valore aggiunto".

La motivazione per l'introduzione di questo standard risiede nella crescita esponenziale delle fonti PAI/CAI, nell'utilità crescente dell'AI nel ciclo intelligence e nella necessità di contrastare la strumentalizzazione di queste fonti per disinformazione. Fino al 2024, le diverse agenzie IC utilizzavano convenzioni di citazione interne, rendendo difficile la riproducibilità e l'audit tra gli elementi della comunità.

## 📊 Dati, Tecnologie e Metriche

L'ICS 206-01 si fonda su quattro pilastri obbligatori per garantire la conformità e l'integrità dei prodotti analitici:

1.  **Citazione (Citation)**: PAI, CAI e OSINT devono essere citati con un formato SRC uniforme in tutti i prodotti analitici disseminati. La non conformità può comportare il rigetto del prodotto.
2.  **Scopribilità (Discoverability)**: Le citazioni devono essere recuperabili con tag comuni secondo ICD 501 e ICD 504 per garantire l'interoperabilità e permettere audit e verifiche annuali.
3.  **Conservazione (Preservation)**: Le sorgenti PAI/CAI dinamiche che influenzano il messaggio chiave devono essere conservate per almeno un anno (o per l'orizzonte di un NIE / 5 anni), per mantenere la tracciabilità.
4.  **Sviluppo delle competenze (Training)**: È richiesto lo sviluppo delle competenze del personale IC secondo l'Appendice B e i requisiti del Functional Manager OSINT, con la conformità valutata in esercitazioni annuali.

Una distinzione operativa fondamentale per gli analisti OSINT è quella tra:

*   **Stand-Alone OSINT Analytic Product**: Rappresenta la posizione analitica coordinata di un elemento IC, derivata esclusivamente da PAI/CAI/OSINT. Include giudizi analitici e tesi ricercate (es. NIA basato su OSINT).
*   **Other Stand-Alone OSINT Product**: Fornisce principalmente osservazioni fattuali e contenuti informativi, come geolocalizzazione, traduzioni, riassunti o curation. Non costituisce una posizione analitica coordinata (es. report di geolocalizzazione di immagini SATellitari).

I ruoli e le responsabilità per l'implementazione dello standard sono distribuiti tra:

*   **IC OSINT Executive (ODNI)**: Responsabile dell'implementazione uniforme e delle analisi annuali di conformità.
*   **Capi degli Elementi IC (CIA, NSA, DIA, FBI, NGA, ecc.)**: Responsabili dell'implementazione nelle proprie aree e dello sviluppo di processi interni.
*   **Functional Manager per OSINT**: Guida il National Open Source Committee (NOSC) e sviluppa lezioni apprese.
*   **NOSC / DOSC**: Promuovono la conformità IC e coordinano l'implementazione.
*   **Professionisti Intelligence**: Analisti, raccoglitori e curatori, responsabili del rispetto dell'ICS e dell'aggiornamento delle migliori pratiche.

## 🔍 Analisi Operativa ed Applicazioni OSINT

L'elemento più innovativo dell'ICS 206-01 è la **Source Reference Citation (SRC)**, un insieme specificato di elementi informativi fattuali su una fonte, presentato in formato uniforme per consentire ai lettori di localizzare e recuperare la fonte. La struttura tecnica dell'SRC include:

*   **Classificazione e Marcatura**: Classificazione complessiva e marcature di porzione.
*   **Separazione con Pipe**: Elementi separati da `|` per differenziare categorie di metadati.
*   **Source Descriptor**: Caratterizzazione della fonte (qualità, credibilità, affidabilità, stato, strumenti AI).
*   **SRC Descrittiva vs Generica**: Di default descrittiva; generica solo se giustificata da esigenze di sicurezza.

La pratica del **Direct Link** (collegamento ipertestuale diretto) può ridurre l'uso delle note a piè di pagina, ma è soggetta a vincoli di formato per i prodotti di disseminazione IC.

L'ICS 206-01 introduce requisiti di citazione specifici per le tecnologie emergenti, promuovendo una **trasparenza computazionale** senza precedenti:

1.  **Sistemi di Computer Vision (CV)**: Obbligo di citare tipo di sistema, nome del modello, spiegazione non tecnica, precisione e recall, impostazioni, dati di addestramento, versione software, link al repository e data di utilizzo.
2.  **Generative AI (GAI) / LLM**: A causa della stocasticità degli output, è obbligatorio citare piattaforma/modello, prompt completo e parametri rilevanti (es. temperature, top-p).
3.  **Qualità dei Dati AI**: Quando la validazione manuale è impossibile, l'ICS richiede di documentare le caratteristiche di performance e i dati di addestramento per garantire riproducibilità e trasparenza, superando l'etichetta generica di "non valutato".
4.  **Source Descriptor per Strumenti e Servizi AI**: Estensione della catena di citazione a strumenti di raccolta, interfacce di ricerca e servizi di visualizzazione che forniscono analisi a valore aggiunto, specialmente se assistiti da AI/ML/CV.

Lo standard è intrinsecamente **orientato al futuro**, riconoscendo la velocità di evoluzione dell'ecosistema open data. Invece di un catalogo chiuso, stabilisce un *framework di citazione generativo* che permette di "mappare" nuove tecnologie sulle categorie esistenti e segnalarle tramite SRC/Descriptor.

## 🔮 Lacune Informative e Prossimi Passi

Nonostante la sua completezza, la sorgente presenta alcune lacune informative:

*   **Esempi completi di SRC**: L'Appendice B, che dovrebbe contenere il formato SRC Pipe completo, è solo citata e non riprodotta.
*   **ICS analoghi**: Mancano riferimenti a standard simili per altre discipline di intelligence (HUMINT, SIGINT, GEOINT, MEFINT).
*   **Dettagli sulle sanzioni**: Le conseguenze specifiche per la non conformità non sono dettagliate.
*   **Citazione dei social media**: Non è specificato il formato di citazione per post, messaggi diretti o storie sui social media.

Per approfondire la comprensione e l'applicazione degli standard analitici, i prossimi passi includono:

1.  Recuperare il testo completo dell'Appendice B dell'ICS 206-01.
2.  Verificare se la UE (European External Action Service, Europol Intelligence School) ha rilasciato standard analoghi post-2024.
3.  Mappare gli elementi IC e i loro strumenti interni di citazione già in rollout.
4.  Studiare l'impatto sui curricula professionali per l'intelligence, verificando l'integrazione esplicita del modulo di citazione e standard analitici.

## 🔗 Connessioni e Pattern

- [[Applicazioni osint]]
- [[Cai]]
- [[Ciclo intelligence]]
- [[Disinformazione]]
- [[Osint]]
- [[Pai]]


- [[--]]
F/I/H
- [[--]]
