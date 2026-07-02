---
title: Explainable ai
tags:
- OSINT
- processed
- explainable-ai
date: '2026-05-15'
status: draft
depth: standard
sources: '1'
tipo: concetto
---

# Explainable AI

## 🎯 Sintesi Strategica

L'Explainable AI (XAI) è l'insieme di tecniche e metodi volti a rendere interpretabili e comprensibili le decisioni dei modelli di [[Machine learning]] e [[Deep learning]]. Nel contesto [[Osint]], dove ogni output deve essere verificabile e tracciabile, la XAI è fondamentale per garantire che i modelli non operino come "scatole nere" inaffidabili. Essa funge da ponte tra la capacità predittiva di un modello e la necessità operativa di verificarne l'affidabilità per l'uso decisionale, mostrando quali *features* e quali parti dell'input hanno determiNATO un dato output.

## 📚 Contesto e Definizioni

L'Explainable AI (XAI) si riferisce all'insieme di tecniche e metodi per rendere interpretabili e comprensibili le decisioni dei modelli di [[Machine learning]].

### Il Problema della Scatola Nera (Black Box)

I modelli di deep learning hanno RAGgiunto livelli di performance senza precedenti in numerosi domini, ma il loro funzionamento interno è spesso opaco per gli esseri umani. Milioni o miliardi di parametri agiscono in modo combiNATO e non-lineare, rendendo impossibile tracciare la "logica decisionale" del modello. Nel contesto [[Osint]], dove ogni output deve essere **verificabile** e **tracciabile**, l'XAI è un requisito operativo imprescindibile.

### Tecnologie XAI Principali

#### LIME — Local Interpretable Model-Agnostic Explanations

**LIME** (Ribeiro et al., 2016) è una tecnica di *explanation* locale che:
1.  Prende un singolo esempio di input e l'output del modello.
2.  Genera perturbazioni dell'input (es. parole rimosse, frasi modificate).
3.  Osserva come cambiano le predizioni.
4.  Addestra un modello locale interpretabile (tipicamente regressione lineare) sul set di esempi perturbati.
5.  Mostra quali *features* hanno avuto il maggior impatto sulla predizione.

#### SHAP — SHapley Additive explanations

**SHAP** (Lundberg & Lee, 2017) è basato sulla teoria dei giochi cooperativi:
*   Calcola il contributo di ogni *feature* alla predizione attraverso tutte le possibili combinazioni (*Shapley values*).
*   Garantisce proprietà matematiche fondamentali (efficienza, simmetria, additività).
*   Produce *explanations* sia globali (importanza delle *features*) che locali (contributo per singola predizione).

#### Attention Visualization

Per i modelli basati su architetture [[Trasformatore (architettura deep learning)|Transformer]] (come BERT, GPT, ecc.), la visualizzazione dell'attenzione può mostrare:
*   Quali *token* il modello "ha guardato" di più.
*   Come l'attenzione è distribuita tra il contesto corrente e i *token* distanti.
*   Quali relazioni sintattiche e semantiche il modello ha utilizzato.

## 📊 Dati, Tecnologie e Metriche

### Metriche di Valutabilità dei Modelli XAI

| Metrica        | Cosa misura                                                | Applicazione OSINT                                     |
| :------------- | :--------------------------------------------------------- | :----------------------------------------------------- |
| **Stability**  | Quanto le *explanation* cambiano con piccole variazioni nell'input | Affidabilità delle XAI su dati rumorosi                |
| **Fidelity**   | Quanto bene l'*explanation* approssima il modello          | Fedeltà delle spiegazioni al comportamento reale del modello |
| **Interpretability** | Quanto l'*explanation* è comprensibile per l'umano        | Utile per analisti non-tecnici                         |
| **Completeness** | L'*explanation* copre tutte le *feature* rilevanti         | Evita omissioni critiche                               |

### Confronto Tecnologie XAI

|                  | LIME                      | SHAP                      | Attention                 |
| :--------------- | :------------------------ | :------------------------ | :------------------------ |
| **Velocità**     | Veloce (approssimato)     | Lento (calcolo completo)  | Integrato (zero-cost)     |
| **Interpretazione** | Intuitiva                 | Matematicamente rigorosa  | Visiva (mappe)            |
| **Local vs Global** | DomiNATO localmente       | Entrambi                  | Entrambi                  |
| **Applicabilità** | Model-agnostic (qualsiasi modello) | Model-agnostic            | Solo modelli con *attention layer* |
| **Rischio**      | Può produrre *explanations* non stabili | Computazionalmente costoso | Può non riflettere causalità |

## 🔍 Analisi Operativa ed Applicazioni OSINT

### LIME nell'Analisi OSINT

**Workflow LIME per NLP in OSINT:**
1.  **Input**: Un testo da un documento sociale classificato come "disinformazione".
2.  **Modello**: Il classificatore produce l'output "disinformazione".
3.  **Generazione**: Vengono create versioni perturbate del testo (es. parole rimosse casualmente).
4.  **Predizione**: Il sistema di classificazione predice per ogni versione perturbata.
5.  **Approssimazione**: Una regressione lineare approssima la relazione tra la presenza di parole e la classificazione.
6.  **Output**: Vengono identificate le parole che hanno contribuito maggiormente alla classificazione "disinformazione".

L'analista può quindi:
*   Verificare se le parole identificate dal modello sono effettivamente indicative di disinformazione o solo pattern superficiali (es. parole politicamente sensibili).
*   Identificare [[Algoritmi]] del modello (es. classifica come "disinformazione" testi che contengono parole specifiche ma sono organici).

### SHAP nell'Analisi OSINT

**Workflow SHAP per NLP in OSINT:**
1.  **Input**: Un *corpus* di documenti etichettati (es. propaganda/organico).
2.  **Calcolo**: SHAP calcola il valore di Shapley per ogni *feature* in ogni documento.
3.  **Output**: Vengono generati i valori di contributo per ogni *feature* in ogni documento.
4.  **Aggregazione Globale**: Vengono identificate le *features* globalmente più importanti per il modello.

L'analista può quindi:
*   Validare che il modello stia usando pattern RAGionevoli (es. "la presenza di 'sanzioni' aumenta la probabilità di classificazione come geopolitico").
*   Identificare *feature* spurie o [[Algoritmi]] sistematici.

### La TENSione XAI — Performance vs Interpretabilità

| Modello           | Performance | Interpretabilità | XAI Viability               |
| :---------------- | :---------- | :--------------- | :-------------------------- |
| Decision Tree     | Media       | Alta             | Intrinsecamente interpretabile |
| Linear Regression | Bassa-Media | Alta             | Intrinsecamente interpretabile |
| Random Forest     | Alta        | Media            | SHAP, *feature importance*  |
| SVM               | Alta        | Bassa            | SHAP, LIME                  |
| Deep Learning     | Altissima   | Molto bassa      | LIME, SHAP, Attention       |

La XAI è un ponte essenziale tra la "black box" del [[Deep learning]] e la necessità [[Osint]] di verificabilità.

## 🔮 Lacune Informative e Prossimi Passi

- [ ] **Approfondimento**: XAI per modelli [[Llm|Large language models]] (LLM) — tecniche specifiche per le architetture generative (saliency maps, counterfactual examples).
- [ ] **Approfondimento**: XAI per il *deployment* in produzione: integrare SHAP/LIME nelle pipeline di classificazione OSINT.
- [ ] **Approfondimento**: [[Algoritmi]] detection sistematico attraverso XAI — come identificare pattern discriminatori nei modelli ML.
- [ ] **Sorgenti aggiuntive**: Metodi XAI per modelli multimodali (testo+immagine) e per NER in contesti multilingue.

## 🔗 Connessioni e Pattern

- [[Applicazioni osint]]
- [[Deep learning]]
- [[Disinformazione]]
- [[Llm|Large language models]]
- [[Osint]]
- [[Regressione lineare]]


- [[--]]
F/I/H
- [[--]]
