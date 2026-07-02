---
title: Bias
tags:
- OSINT
- processed
- bias
- cognizione
- analisi
date: '2026-05-15'
status: draft
depth: standard
sources: '5'
tipo: concetto
---

# Bias

## 🎯 Sintesi Strategica

I **bias cognitivi** rappresentano deviazioni sistematiche dal RAGionamento logico e razionale, intrinseche alla cognizione umana. Essi costituiscono una delle principali minacce all'accuratezza dell'[[Analisi]], distorcendo la percezione, il giudizio e l'interpretazione dei dati. Non derivano da scarsa competenza, ma dall'attivazione automatica di euristiche mentali (Sistema 1) che, se non mitigate, possono condurre a conclusioni errate e decisioni subottimali. La loro identificazione e mitigazione sono cruciali per la validità delle [[Azioni]] e per contrastare strategie avversarie come il [[Poisoning]] informativo.

## 📚 Contesto e Definizioni

Il concetto di bias cognitivo trova la sua fondazione scientifica nel modello duale della cognizione umana, elaborato da [[Daniel Kahneman]] e Amos Tversky. Questo modello distingue due modalità operative del cervello:
*   **Sistema 1**: Veloce, automatico, intuitivo, emotivo e a basso consumo energetico. È responsabile delle risposte immediate e delle euristiche.
*   **Sistema 2**: Lento, riflessivo, logico, sequenziale e ad alto consumo computazionale. È deputato all'analisi critica e alla verifica.

I bias emergono quando il Sistema 1 produce risposte coerenti ma incomplete, e il Sistema 2 non interviene con un vaglio critico sufficiente. Nel contesto dell'intelligence, i bias sono errori di interpretazione che disallineano la "mappa della realtà" dell'analista dalla realtà oggettiva. Tra i più rilevanti si annoverano:
*   **Bias di Conferma**: La tendenza a cercare, interpretare e valorizzare solo le informazioni che confermano le proprie ipotesi preesistenti, ignorando quelle contrarie.
*   **Bias di Disponibilità**: La propensione a basare i giudizi su esempi facilmente richiamabili alla memoria, sovrastimando eventi recenti o emotivamente salienti.
*   **Illusione di RAGgruppamento**: La percezione di connessioni o pattern dove in realtà non esistono, spesso tra dati scollegati.
*   **[[Mirror imaging]]**: La proiezione dei propri schemi di valore, credenze e intenzioni sull'avversario, assumendo che agisca con la stessa logica.
*   **Anchoring (Effetto Ancoraggio)**: La tendenza a fare eccessivo affidamento sulla prima informazione ricevuta (l'ancora) nel prendere decisioni.
*   **Sunk Cost Fallacy**: L'insistenza su un'ipotesi o un'azione fallimentare a causa delle risorse (tempo, denaro, impegno) già investite.

## 📊 Dati, Tecnologie e Metriche

La misurazione e l'identificazione dei bias non sono dirette, ma avvengono attraverso l'analisi degli esiti e l'applicazione di metodologie strutturate.
*   **Linguaggio Probabilistico Standardizzato**: Proposto da [[Sherman Kent]], l'uso di termini probabilistici standardizzati (es. "probabile", "improbabile") mira a ridurre la falsa certezza e la soggettività nelle valutazioni, rendendo esplicito il grado di incertezza.
*   **[[Brier Score]]**: Sebbene non misuri direttamente i bias, il [[Superforecasting|Brier Score]] è una metrica utilizzata nel [[Superforecasting]] per valutare l'accuratezza delle previsioni probabilistiche. Un punteggio elevato può indirettamente segnalare la presenza di bias che distorcono la calibrazione delle probabilità.
*   **Tracciabilità e [[Audit Trail]]**: Le Structured Analytic Techniques ([[SAT)]] generano un percorso documentato ([[Audit Trail]]) del processo analitico, rendendo ispezionabile il giudizio e facilitando l'identificazione retrospettiva di potenziali distorsioni.
*   **AI-assisted Analysis**: L'[[Fondamenti di ai|Intelligenza Artificiale]] (AI), in particolare i [[Llm|Large language models]], può supportare la mitigazione dei bias generando alternative, critiche o scenari diversi, costringendo l'analista a considerare prospettive multiple. Tuttavia, l'AI stessa può introdurre nuovi bias (es. bias algoritmici) o amplificare quelli esistenti se non gestita con un approccio [[Human-in-the-loop]].

## 🔍 Analisi Operativa ed Applicazioni OSINT

Nell'[[Osint]] e nell'analisi intelligence, i bias rappresentano una vulnerabilità critica, specialmente nella fase di "Orient" del [[Ciclo OODA]]. La mitigazione richiede l'adozione di [[Metodologie Strutturate per la Riduzione dei Bias Cognitivi]] che forzano l'attivazione del Sistema 2 e smontano le euristiche automatiche:
*   **[[Analysis of competing hypotheses]]**: Sviluppata da Richards Heuer, questa tecnica prevede l'enumerazione di tutte le ipotesi plausibili, la catalogazione delle evidenze e la selezione dell'ipotesi *meno smentita*, piuttosto che la più confermata, contrastando il bias di conferma.
*   **Tecniche Contrarian**:
    *   **Devil's Advocate**: Un analista o un team viene incaricato di sfidare attivamente il consenso dominante, cercando falle logiche e argomenti contrari, per combattere il [[Bias|Groupthink]].
    *   **[[Red team]]**: Un team simula il punto di vista e le azioni dell'avversario per identificare vulnerabilità nell'analisi o nei piani propri, mitigando il [[Mirror imaging]].
*   **[[Metodo Delphi]]**: Un protocollo di consensus-building che previene le degenerazioni del pensiero di gruppo. Attraverso cicli iterativi di questionari anonimi tra esperti, si mira a una convergenza progressiva e calibrata di probabilità o scenari, neutralizzando le dinamiche di potere e l'egemonia oratoria.
*   **Tecniche di Scenario**:
    *   **Premortem**: Immaginare che l'analisi sia fallita prima della sua consegna per identificare proattivamente vulnerabilità e potenziali bias che potrebbero averla compromessa.
    *   **Scenario Analysis (es. PEST/PESTLE, AFA 2x2)**: L'esplorazione sistematica di futuri possibili, probabili e preferibili aiuta a sfidare le assunzioni implicite e a ridurre il bias di conferma.

## 🔮 Lacune Informative e Prossimi Passi

Nonostante l'ampia ricerca sui bias, permangono lacune significative nell'applicazione e nella quantificazione:
*   **Casi Concreti di Bias in Contesti Specifici**: Mancano esempi dettagliati e declassificati di come i bias abbiano influenzato decisioni cruciali in contesti di intelligence specifici, come quelli del Sistema Intelligence Italiano (SISR).
*   **Metriche Quantitative sull'Incidenza dei Bias**: La frequenza e l'impatto quantitativo di specifici bias nell'analisi operativa non sono pienamente quantificati, rendendo difficile valutare l'efficacia delle contromisure.
*   **Efficienza delle Tecniche Anti-Bias**: Sono necessari studi comparativi sull'efficacia delle diverse Structured Analytic Techniques ([[SAT)]] nella riduzione dei bias in scenari operativi reali.
*   **Ruolo dell'AI nella Mitigazione e Introduzione di Nuovi Bias**: Ulteriori ricerche sono necessarie per comprendere appieno come l'AI possa non solo mitigare i bias umani, ma anche introdurne di nuovi (es. bias nei dati di addestramento degli LLM) e come gestirli efficacemente.

**Prossimi Passi Operativi:**
1.  Integrare con [[Poisoning]] per analizzare l'interazione tra bias e manipolazione esterna.
2.  Approfondire Bias cognitivi — Kahneman-Tversky per una base teorica più dettagliata.
3.  Esplorare Strutture Analytic Techniques (Heuer) per un toolkit anti-bias completo.
4.  Analizzare il [[Metodo Delphi]] — Origini e Protocollo per dettagli metodologici sulla riduzione del [[Groupthink]].

## 🔗 Connessioni e Pattern

- [[Ciclo OODA]]
- [[Human-in-the-loop]]
- [[Osint]]
- [[Poisoning]]
- [[Superforecasting]]


- [[--]]
F/I/H
- [[--]]
