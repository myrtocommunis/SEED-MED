---
title: [[SAT]]
tags:
- OSINT
- processed
- [[SAT]]
- analisi-intelligence
- metodologia
date: '2026-05-16'
status: validated
depth: deep
sources: '8'
tipo: concetto
---

# [[SAT]] (Structured Analytic Techniques)

## 🎯 Sintesi Strategica

Le **Structured Analytic Techniques ([[SAT)]]** sono protocolli metodologici progettati per rendere esplicito e ispezionabile il RAGionamento analitico. Il loro scopo primario è la mitigazione dei [[Bias cognitivo]] attraverso la scomposizione di problemi complessi in componenti gestibili. Tuttavia, le [[SAT]] non sono una garanzia di accuratezza; la loro efficacia risiede nel migliorare la trasparenza del processo e nel forzare l'analista a considerare alternative che il pensiero intuitivo (Sistema 1) tenderebbe a scartare.

## 📚 Fondamenti e Critiche Epistemologiche

Il canone delle [[SAT]], codificato da [[Metodologia|Richard Heuer]] (1999), si basa sull'assunto che la strutturazione del pensiero prevenga l'errore sistematico. Evoluzioni recenti hanno tuttavia introdotto importanti *caveat*:

1.  **Limiti dell'Efficacia Empirica:** Ricerche condotte da Mandel e Tetlock suggeriscono che l'uso delle [[SAT]] non sempre correla con una maggiore accuratezza previsionale. Esse possono aumentare la *confidenza* dell'analista (overconfidence) senza migliorare necessariamente l'output (Coulthart, 2017).
2.  **Paralisi da Analisi:** In contesti di crisi ad alta velocità, l'applicazione meccanica di tecniche complesse (es. ACH) può rallentare eccessivamente il processo decisionale. La scelta della tecnica deve essere commisurata al tempo disponibile e alla criticità della domanda informativa.
3.  **Il Modello NDM (Naturalistic Decision Making):** In contrapposizione alle [[SAT]], il modello NDM valorizza l'intuizione esperta in situazioni di stress, suggerendo che in certi casi l'esperienza clinica dell'analista senior sia più efficace di una matrice strutturata.

## 🔄 Tecniche Operative e Applicazioni OSINT

Le [[SAT]] si dividono in tre macro-categorie operative:

### 1. Tecniche di Diagnosi
- **Key Assumptions Check:** Mettere a nudo le premesse "date per scontate" che potrebbero invalidare l'intera analisi.
- **Quality of Information Check:** Applicazione sistematica dell'Admiralty Code per pesare l'affidabilità dei dati grezzi.

### 2. Tecniche Contrarian (Sfidare il Consenso)
- **Devil's Advocate:** Incaricare un membro del team di distruggere sistematicamente la tesi dominante.
- **Team A-Team B:** Competizione tra due gruppi indipendenti su ipotesi divergenti.
- **[[Red team|Red Team]]:** Simulare la mentalità dell'avversario per identificare punti ciechi difensivi.

### 3. Tecniche di Scenario (Immaginare il Futuro)
- **Alternative Futures Analysis (AFA 2x2):** Identificazione dei driver critici per generare scenari narrativi.
- **What If - HILP:** Analisi degli eventi a bassa probabilità ma con impatto catastrofico.

## 🤖 Integrazione AI e Rischio di Bias Ricorsivo

L'uso di LLM per supportare le [[SAT]] (es. generazione di scenari o Red Teaming automatizzato) introduce nuove sfide:
- **Complacency Bias:** L'analista potrebbe accettare acriticamente l'analisi strutturata prodotta dall'AI perché appare "formale" e ben organizzata.
- **AI Hallucination:** In tecniche come l'ACH, l'AI potrebbe inventare evidenze plausibili ma false per "riempire" la matrice, inquinando il processo di validazione.
- **Pattern Matching Rigido:** L'AI tende a seguire pattern predefiniti, rischiando di sopprimere proprio quelle "deboli anomalie" che le [[SAT]] umane dovrebbero invece far emergere.

---
## 🔗 Connessioni e Pattern

- [[Analisi strutturata]]
- [[Ciclo dell'intelligence]]
- [[Human-in-the-loop]]
- [[Metodologia]]
- [[Metodologia|Richard Heuer]]

- [[--]]
F/I/H
- [[--]]
- [[*Fatti:** Le [[SAT]] sono obbligatorie in molte comunità di intelligence per garantire l'[[Audit Trail]] analitico.]]
- [[*Interpretazione:** La [[SAT]] non "crea" la verità, ma documenta il percorso logico che ha portato a una conclusione, permettendo di identificare a posteriori dove il RAGionamento si è rotto.]]
- [[*Ipotesi:** Il futuro delle [[SAT]] risiede nell'analisi massiva di Big Data (OSINT), dove l'algoritmo esegue la scomposizione strutturata iniziale e l'umano interviene solo nella fase di interpretazione degli scenari residui.]]

- [[--]]
### Fonti e Bibliografia
- [[Heuer, R. J. (1999). *Psychology of Intelligence Analysis*. CIA CSI.]]
- [[Tetlock, P. E. (2015). *Superforecasting: The Art and Science of Prediction*.]]
- [[Mandel, D. R. (2015). *Instruction in Information Integration Enhances Analysis*.]]
- [[Coulthart, S. J. (2017). *An Evidence-Based Evaluation of 12 Structured Analytic Techniques*.]]
