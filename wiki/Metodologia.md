---
title: Metodologia
tags:
- OSINT
- processed
- metodologia
- intelligence-cycle
- epistemologia
date: '2026-05-16'
status: validated
depth: deep
sources: '12'
tipo: concetto
---

# Metodologia

## 🎯 Sintesi Strategica

La **Metodologia OSINT** è l'architettura logica che trasforma l'abbondanza di dati grezzi in *Vantaggio Decisionale*. Essa non si limita alla padronanza degli strumenti tecnici, ma si fonda su un rigore procedurale che mitiga i [[Bias cognitivo]] e garantisce l'ispezionabilità del giudizio analitico. Il prodotto finale deve aderire alla **Regola ABC** (Accuratezza, Brevità, Chiarezza) per essere realmente azionabile dai decisori.

## 📚 Fondamenti Epistemologici e Metriche di Qualità

In un'infosfera caratterizzata da "povertà di attenzione" (Simon, 1969), la qualità dell'intelligence si misura tramite standard rigorosi:

### La Regola ABC
1.  **Accuratezza:** Ogni affermazione deve essere verificata tramite triangolazione di fonti indipendenti. L'errore fattuale distrugge la credibilità dell'intero apparato analitico.
2.  **Brevità:** L'intelligence deve essere distillata. Il valore non risiede nella lunghezza del report, ma nella densità informativa.
3.  **Chiarezza:** Evitare ambiguità linguistiche. Il decisore deve comprendere immediatamente il significato dell'analisi senza margini di interpretazione soggettiva.

### Il Metodo AIA (Valutazione dell'Impatto)
Ogni monade informativa prodotta deve essere testata contro tre criteri:
- **Impatta:** L'informazione modifica la comprensione dello scenario o la postura del decisore?
- **Aggiorna:** Introduce elementi di novità rispetto alla conoscenza pre-esistente?
- **Approfondisce:** Fornisce un livello di dettaglio superiore che permette di identificare pattern latenti?

## 🔄 Operazionalizzazione del Ciclo e Admiralty Code

La validazione del dato segue il sistema **Admiralty Code** (o Codice [[NATO]]), che separa l'affidabilità della fonte dalla credibilità dell'informazione:

| Grado | Affidabilità Fonte | Credibilità Informazione |
|---|---|---|
| A / 1 | Completamente affidabile | Confermato da altre fonti |
| B / 2 | Solitamente affidabile | Probabilmente vero |
| C / 3 | Abbastanza affidabile | Possibile |
| D / 4 | Non solitamente affidabile | Dubbio |
| E / 5 | Inaffidabile | Improbabile |
| F / 6 | Non valutabile | Non valutabile |

L'analista deve sempre puntare a prodotti con rating **A1** o **B2**. Prodotti con rating inferiore devono essere accompagnati da *caveat* espliciti sui rischi di manipolazione o fallacia.

## ⚖️ Etica e Responsabilità della Raccolta

L'analisi OSINT solleva questioni etiche fondamentali, specialmente nell'uso di CAI (Commercially Available Information) e nella profilazione tramite [[Sock puppet]]:
1.  **Diritto alla Privacy vs Sicurezza:** L'equilibrio tra la necessità di intelligence e il rispetto delle normative ([[GDPR]], CEDU) è il perimetro legale dell'operazione.
2.  **Integrità delle Fonti:** Evitare il "data poisoning" e la diffusione involontaria di disinformazione.
3.  **Responsabilità Sociale:** Consapevolezza che l'intelligence può influenzare politiche pubbliche e vite umane; il rigore metodologico è dunque un imperativo etico, non solo tecnico.

## 🧠 Analisi Strutturata e Mitigazione dei Bias

L'analista deve forzare il passaggio dal **Sistema 1** (intuitivo) al **Sistema 2** (deliberativo) attraverso:
- **Red Teaming:** Sfidare attivamente le proprie conclusioni simulando il punto di vista avversario.
- **Analysis of Competing Hypotheses (ACH):** Testare contemporaneamente più ipotesi escludendo quelle smentite dai dati, piuttosto che cercare conferme per una singola tesi.

---
## 🔗 Connessioni e Pattern

- [[Analisi strutturata]]
- [[Ciclo dell'intelligence]]
- [[Opsec]]
- [[Postazione di lavoro osint|Postazione di lavoro OSINT]]
- [[Metodologia|Richard Heuer]]
- [[Sat]]

- [[--]]
F/I/H
- [[--]]
- [[*Fatti:** L'Admiralty Code è lo standard de facto per la valutazione dell'intelligence nelle agenzie NATO.]]
- [[*Interpretazione:** La separazione tra fonte e informazione impedisce che il pregiudizio su una fonte (positiva o negativa) inquinino la valutazione del dato specifico.]]
- [[*Ipotesi:** L'automazione della valutazione tramite Admiralty Code via AI richiederà modelli di "Self-Correction" estremamente sofisticati per evitare bias ricorsivi.]]

- [[--]]
### Fonti e Bibliografia
- [[Heuer, R. J. (1999). *Psychology of Intelligence Analysis*. Center for the Study of Intelligence.]]
- [[NATO (2020). *AJP-2.1 Intelligence Procedures*.]]
- [[Simon, H. A. (1969). *Designing Organizations for an Information-Rich World*.]]
- [[Kahneman, D. (2011). *Thinking, Fast and Slow*.]]
