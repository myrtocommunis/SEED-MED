---
title: Poisoning
tags:
- OSINT
- processed
- poisoning
date: '2026-05-15'
status: draft
depth: standard
sources: '1'
tipo: concetto
---

# Poisoning

## 🎯 Sintesi Strategica

Il **Poisoning** rappresenta una minaccia critica all'analisi intelligence, consistendo nella deliberata contaminazione delle informazioni da parte di attori ostili. L'obiettivo è indurre l'analista a formulare conclusioni errate, distorcendo la percezione della realtà e compromettendo il processo decisionale. Questa strategia di inganno è uno dei limiti fondamentali dell'analisi, poiché la fonte stessa può trasformarsi in un'arma. Si distingue dagli Errori di Interpretazione e dai [[Bias cognitivo]], pur interagendo con essi, in quanto implica un'azione intenzionale esterna. La mitigazione richiede l'adozione di Procedure Strutturate (come il [[Metodo Delphi]] e le [[Tecniche]]), una profonda consapevolezza delle vulnerabilità analitiche e il riconoscimento che ogni raccolta informativa è un'interpretazione, non la realtà oggettiva.

## 📚 Contesto e Definizioni

Il Poisoning si inserisce nella tensione epistemologica tra il desiderio di conoscenza completa e l'inevitabile incompletezza di ogni informazione, come evidenziato da Edgar Morin nel suo PENSiero Complesso. L'analista opera accettando che ogni rappresentazione della realtà è una semplificazione e che l'analisi è un'interpretazione strutturata.

Il **Poisoning** è la contaminazione intenzionale delle informazioni da parte di strategie nemiche, progettate per manipolare la percezione dell'analista e condurlo a conclusioni errate. È una forma di inganno strategico che mira a compromettere l'affidabilità delle fonti stesse. Come affermato da Sun Tzu ne *L'Arte della Guerra*, "gli affari militari seguono la via dell'inganno", sottolineando la natura intrinseca della dissimulazione nelle operazioni avversarie.

Il processo analitico parte dall'individuazione dei Gap Informativi ("cosa non so?"), che definiscono il fabbisogno informativo. Il Poisoning agisce direttamente su questo ciclo, inserendo dati falsi o fuorvianti nella fase di raccolta, alterando così le basi per la formulazione di nuove domande e interpretazioni.

## 📊 Dati, Tecnologie e Metriche

Il Poisoning si manifesta attraverso diverse tecniche di manipolazione informativa:
*   **[[Maskirovka]] russa**: Una dottrina militare che include disinformazione, occultamento e inganno, applicata modernamente tramite social media, falsi flag e operazioni cyber.
*   **Scalata di credibilità**: Strategie per far circolare informazioni manipolate attraverso canali apparentemente indipendenti (es. bot network → influencer → media mainstream), conferendo loro un'aura di legittimità.
*   **Misure attive (KGB)**: Operazioni segrete volte a indebolire l'avversario attraverso la [[Poisoning]], l'interferenza nelle elezioni o la costruzione di narrazioni distorte.

È fondamentale considerare che "ogni notizia è un tentativo di poisoning". Ciò implica una valutazione critica non solo del contenuto, ma anche della fonte, del giornalista e dell'editor, analizzando le loro potenziali motivazioni di manipolazione.

A differenza dei [[Bias cognitivo]] (come il Bias di Conferma, il Bias di Disponibilità o l'Illusione di RAGgruppamento), che sono distorsioni interne al processo mentale dell'analista, il Poisoning è un'aggressione esterna e intenzionale alla validità dei dati. Tuttavia, i bias possono rendere l'analista più vulnerabile al Poisoning.

L'adozione di un Linguaggio Probabilistico Standardizzato, come proposto da [[Sherman Kent]], è cruciale per esprimere le valutazioni di intelligence in termini di probabilità anziché certezze, riducendo lo spazio per l'inganno basato su affermazioni assolute.

## 🔍 Analisi Operativa ed Applicazioni OSINT

Il Poisoning ha un impatto diretto sull'[[Analisi]], dove la vastità e l'accessibilità delle fonti aperte aumentano il rischio di contaminazione. L'analisi, intesa come un processo artigianale che trasforma il caos in significato, richiede pazienza, precisione e contestualizzazione. Il Poisoning mina questi pilastri, introducendo elementi di caos intenzionale.

Nel contesto del [[Ciclo OODA]] di [[John boyd]], il Poisoning colpisce in modo particolarmente insidioso la fase di **Orientamento**. È qui che i dati grezzi (provenienti da [[All-source intelligence]] come [[Humint]], [[Sigint]], [[Imint]], [[Masint]], [[Osint]]) vengono interpretati per costruire "mappe della realtà". Se queste mappe sono basate su informazioni avvelenate, le decisioni successive (Decide, Act) saranno inevitabilmente compromesse.

Per contrastare il Poisoning, l'analista deve mantenere una Consapevolezza Critica costante e adottare Procedure Anti-Bias. Le [[Tecniche]], come il [[Metodo Delphi]] (che riduce il bias di consenso tramite raccolta anonima e iterativa di pareri esperti) e le Structured Analytic Techniques ([[SAT)]] (che stratificano l'analisi per evitare salti logici, come l'analisi concorrente o il devil's advocate), pur essendo primariamente concepite per i bias cognitivi, sono strumenti essenziali anche per identificare e mitigare gli effetti del Poisoning, promuovendo un approccio più robusto e scettico alle fonti.

La vulnerabilità al Poisoning può variare con l'esperienza dell'analista:
*   **Principiante**: Sovraccarico di dati senza filtri, difficoltà a discernere l'affidabilità.
*   **Intermedio**: Rischio di Bias di Conferma che rende l'analista meno propenso a dubitare di informazioni che supportano le sue ipotesi.
*   **Esperto**: Rischio di Bias di Disponibilità e di scorciatoie mentali, che possono portare a sottovalutare nuove forme di inganno o a fidarsi eccessivamente di pattern preesistenti.

## 🔮 Lacune Informative e Prossimi Passi

### Lacune Rilevate

| Gap | Impatto | Prossimi passi |
|---|---|---|
| Casi concreti di bias nell'SISR | Non esistono esempi applicati al SISR specifico | Integrare con casi storici italiani (es. P2, Gladio) |
| Metriche quantitative sui bias | Non quantificata la frequenza di bias specifici | Integrare con studi di psicologia cognitiva applicata |
| Dettagli su [[Metodo Delphi]] | Solo menzioNATO, non spiegato | Integrare con fonte completa sul [[Metodo Delphi]] |
| Caso studio di poisoning reale | Non descritto un caso concreto di successo/insuccesso | Integrare con fonti su operazioni KGB e loro efficacia |
| Efficienza contro-bias [[SAT]] | Non quantificata l'efficacia delle tecniche [[SAT]] | Integrare con studi comparativi sui bias reduction |

### Prossimi Passi Operativi

1.  Integrare con [[Metodo Delphi]] — Origini e Protocollo per dettagli metodologici.
2.  Integrare con Strutture Analytic Techniques (Heuer) per toolkit anti-bias.
3.  Integrare con [[Poisoning]] per esempi storici.
4.  Integrare con Bias cognitivi — Kahneman-Tversky per la base teorica.
5.  Integrare con Morin - PENSiero Complesso per la cornice epistemologica.

## 🔗 Connessioni e Pattern

- [[All-source intelligence]]
- [[Ciclo OODA]]
- [[John boyd]]
- [[Maskirovka]]
- [[Osint]]


- [[--]]
F/I/H
- [[--]]
