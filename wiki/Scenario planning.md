---
title: Scenario planning
tags:
- OSINT
- processed
- scenario-planning
date: '2026-05-15'
status: draft
depth: standard
tipo: concetto
---

title: "Scenario planning"
tags: ["OSINT", "processed", "scenario-planning", "foresight", "futures-literacy"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "4"
tipo: "concetto"
---

# Scenario planning

## 🎯 Sintesi Strategica

Lo **Scenario planning** è una metodologia strategica che, anziché prevedere un futuro singolare, esplora e costruisce molteplici futuri plausibili. Il suo obiettivo primario non è la predizione, ma l'espansione del "repertorio di non-sorpresa" del decisore, migliorando la resilienza organizzativa e la flessibilità strategica. In un contesto di sovraccarico informativo e crescente complessità, dove la distinzione tra contenuto umano e sintetico si affievolisce e i [[Bias cognitivo]] possono offuscare il giudizio, lo scenario planning fornisce un quadro strutturato per navigare l'incertezza. Si basa sulla Futures Literacy, una disciplina che riconosce l'interconnessione bidirezionale tra presente e futuro, dove l'immagine che ci si fa del futuro influenza l'azione presente.

## 📚 Contesto e Definizioni

Lo scenario planning si inserisce in un ambiente informativo caratterizzato da un volume di dati in costante crescita (proiezioni di oltre 394 zettabyte entro il 2028) e da un'accelerazione nella generazione di contenuti, inclusa una quota significativa prodotta da sistemi di intelligenza artificiale. Questo porta a un "sovraccarico informativo" che può generare una "povertà di attenzione" ([[Herbert Simon]], 1969) e favorire la diffusione di informazioni non valutate criticamente.

Il concetto di "Intelligence" deriva dal latino *intelligere* (comprendere, "leggere tra le righe"), sottolineando la necessità di discernere e selezionare. L'[[Osint]] (Open Source Intelligence) è un processo duplice di problem solving e comunicazione, ma è vulnerabile a distorsioni sistematiche come semplificazioni, integrazioni e ristrutturazioni del contenuto.

Epistemologicamente, lo scenario planning si confronta con due concezioni-limite del futuro: l'Orologio di Pierre Laplace (futuro deterministico e calcolabile) e la Nuvola di Edward Lorenz (futuro intrinsecamente non calcolabile per sensibilità alle condizioni iniziali, o Caos Deterministico). L'analista deve distinguere quali variabili seguono dinamiche orologio-simili e quali nuvola-simili.

Cruciale è la distinzione tra Segreti vs Misteri di [[Gregory Treverton]]: i segreti sono conoscibili in linea di principio, mentre i misteri riguardano dinamiche fluide e non ancora cristallizzate, intrinsecamente non conoscibili. Lo scenario planning è lo strumento per esplorare i misteri.

La disciplina identifica tre tipi di futuri:
*   **Futuri possibili**: tutto ciò che non viola leggi fisiche o logiche.
*   **Futuri probabili**: il sottoinsieme con probabilità non trascurabile, dominio del [[Metodi di forecasting|Forecasting]].
*   **Futuro preferibile**: il piano normativo, dipendente dai valori del decisore.
Lo scenario planning si concentra sull'esplorazione dei futuri possibili e probabili, evitando di confondere l'analisi con le preferenze normative.

## 📊 Dati, Tecnologie e Metriche

L'era digitale è definita da una crescita esponenziale dei dati:
*   **2022**: enormi quantità di dati generate ogni minuto.
*   **2025**: proiezione di ~175 zettabyte di dati globalmente prodotti.
*   **2028**: proiezione di oltre 394 zettabyte.
*   **2025**: si prevede che più della metà dei nuovi articoli online sarà generata da sistemi di IA, rendendo la distinzione tra contenuto umano e sintetico una sfida analitica fondamentale.

Le tecnologie emergenti, in particolare i Large Language Models (LLM), stanno ridefinendo le capacità di [[Foresight]]:
*   **Performance LLM**: Studi recenti indicano che i migliori LLM possono superare le performance umane in compiti di classificazione e valutazione (es. 79% di accuratezza per LLM vs 60% per analisti umani in alcuni benchmark).
*   **[[Foresight]]**: Gli LLM possono essere impiegati per generare *raw material* per scenari, controllare la coerenza interna, produrre varianti narrative, agire come "avvocato del diavolo" e supportare la generazione di indicatori di monitoraggio.
*   **Roleplay AI**: Tecnica complementare che permette ai modelli di adottare punti di vista specifici per simulazioni avversarie o esplorazione di prospettive non familiari.
*   **AI-assisted vs AI-generated**: L'approccio metodologicamente accettabile è l'AI-assisted, dove l'analista progetta, valida e decide, utilizzando l'AI come supporto. La delega completa del giudizio (AI-generated) è sconsigliata.
*   **Metriche**: Il [[Superforecasting|Brier Score]] è una metrica utilizzata per valutare l'accuratezza delle previsioni probabilistiche nel forecasting.

## 🔍 Analisi Operativa ed Applicazioni OSINT

Lo scenario planning si integra con le [[Sat]] (Structured Analytic Techniques) e i principi fondamentali dell'[[Osint]] per una comprensione approfondita e proattiva dell'ambiente strategico.

**Framework Universali OSINT:**
*   **Le 5 W (Who, What, When, Where, Why)**: Principio di acquisizione e disseminazione. L'assenza di un elemento informativo è di per sé un'informazione che innesca ulteriori ricerche.
*   **La regola dell'ABC (Accuratezza, Brevità, Chiarezza)**: Guida la qualità del prodotto informativo, essenziale per decisori con tempo limitato.
*   **Il metodo AIA (Impatta, Aggiorna, Approfondisce)**: Valuta l'utilità del prodotto informativo, massimizzando il valore per il decisore.

**Metodologie di Scenario Planning:**
1.  **AFA (Alternative Futures Analysis) 2x2**: Identifica due driver critici (alta incertezza, alto impatto) e li incrocia per generare quattro scenari narrativi coerenti. Per ogni scenario, si definiscono narrative plausibili e Indicatori di Early Warning.
2.  **PESTLE (Political, Economic, Social, Technological, Legal, Environmental)**: Scansione sistematica dei driver ambientali esterni. Per l'OSINT, si raccomanda l'estensione **Military/Adversarial** (PESTLE-M o PESTLE-A) per includere posture militari, capacità avversarie e contromosse strategiche.
3.  **[[Backcasting]]**: Inverte la direzione temporale dell'analisi.
    *   **Positivo**: Parte da un futuro preferibile per ricostruire la roadmap necessaria.
    *   **Negativo**: Parte da un futuro indesiderabile per identificare i *risk tipping points* da monitorare.
4.  **Strategic Foresight 5-step**: Workflow integrato che include:
    *   Analisi dei trend strutturali.
    *   Horizon Scanning per segnali deboli ed emergenti.
    *   Scenario planning (AFA 2x2).
    *   Backcasting.
    *   Creative thinking per rompere le assunzioni e esplorare scenari "fuori distribuzione".
5.  **HILP Analysis (High Impact / Low Probability)**: Metodo strutturato in 6 passi per scenari catastrofici a bassa probabilità percepita ma impatto estremo. Si concentra sulla definizione precisa dell'esito, l'ideazione di percorsi plausibili, l'identificazione di trigger specifici, il brainstorming su fattori scatenanti imprevedibili, la definizione di indicatori osservabili e l'individuazione di fattori strutturali.

L'analista OSINT, attraverso la Metariflessione Analitica (come suggerito da Perelman e Freud), deve essere consapevole del proprio ruolo nel ciclo informativo e delle proprie [[Bias cognitivo]] (es. bias di conferma, overconfidence, euristica della disponibilità), che possono essere mitigati dall'applicazione strutturata di queste metodologie.

## 🔮 Lacune Informative e Prossimi Passi

Nonostante la robustezza metodologica, lo scenario planning presenta limiti intrinseci e aree che richiedono ulteriore sviluppo o verifica:
*   **Limiti Strutturali**:
    *   Il [[Cigno Nero]] ([[Nassim Nicholas Taleb]], 2007): eventi ad impatto estremo, imprevedibili *ex ante*. È cruciale distinguerlo dal [[Rinoceronte Grigio]], minacce probabili ma ignorate.
    *   La [[Failure of Imagination]]: incapacità strutturale di concepire *ex ante* esiti che si materializzano, non per mancanza di dati ma per assenza di un frame interpretativo adeguato (es. Pearl Harbor, 7 Ottobre 2023).
    *   **Scenari domesticati**: scenari che ripetono il presente con varianze marginali, non sfidando assunzioni profonde. La CLA (Causal Layered Analysis) di [[Sohail Inayatullah]] è una contromisura per esplorare livelli più profondi (Worldview, Myth).
*   **Verifiche e Attribuzioni**:
    *   Alcune citazioni (es. Harari, Perelman) e proiezioni di dati (es. Statista 394 ZB 2028) richiedono verifica con fonti primarie o correzione.
    *   L'attribuzione specifica di metodologie (es. HILP Analysis di Valeriani) necessita di riferimenti accademici indipendenti.
*   **Integrazione con altre discipline**: È necessario esplorare ulteriormente l'integrazione dello scenario planning con tecniche come la Social Network Analysis (SNA) per contrastare il sovraccarico informativo e migliorare la rilevazione di segnali deboli.
*   **Sviluppo AI-assisted**: Continuare a definire best practice per l'integrazione degli LLM, inclusi il confronto multi-modello, la citazione formale degli strumenti AI e la separazione documentale tra output AI-assisted e umani per audit.

## 🔗 Connessioni e Pattern

- [[Backcasting]]
- [[Foresight]]
- [[Llm|Large language models]]
- [[Osint]]
- [[Sat]]
- [[Social network analysis]]


- [[--]]
F/I/H
- [[--]]
