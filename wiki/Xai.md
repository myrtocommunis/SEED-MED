---
title: "Xai"
tags: ["OSINT", "processed", "xai", "explainable-ai", "algoritmi"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Xai

## 🎯 Sintesi Strategica

L'**XAI (Explainable AI - Intelligenza Artificiale Spiegabile)** è il sotto-campo dell'informatica volto a rendere le decisioni dei modelli di Machine Learning trasparenti e comprensibili per gli esseri umani. Sebbene il Deep Learning e gli [[Llm]] abbiano RAGgiunto capacità predittive sovrumane, operano storicamente come "Black Box" (Scatole Nere): l'analista fornisce un input, ottiene un output accurato, ma ignora il *perché* matematico il modello sia giunto a quella specifica conclusione. In ambito [[Osint]], governativo e legale, la mancanza di spiegabilità rende l'AI inutilizzabile per compiti critici: una prova d'intelligence o un arresto non possono basarsi su un "Me lo ha detto il computer".

## 📚 Contesto e Definizioni

Il dilemma dell'XAI consiste nel compromesso (Trade-off) tra Performance e Trasparenza:
1.  **Modelli Trasparenti (White Box):** Regressioni lineari o Alberi Decisionali (Decision Trees). La loro logica è banale da comprendere e uditare ("Se l'età > 30 e reddito > 50k, allora..."), ma non riescono a modellare problemi estremamente complessi.
2.  **Modelli Black Box:** Reti Neurali Profonde (Deep Learning), Transformer, Random Forests. Offrono performance stellari nell'analisi di immagini o linguaggio naturale, ma la complessità dei loro miliardi di parametri li rende indecifrabili persino ai loro stessi ingegneri creatori.

## 📊 Dati, Tecnologie e Metriche

Per rendere spiegabili i modelli Black Box, l'XAI utilizza algoritmi "Post-hoc" (Applicati dopo l'addestramento):
*   **LIME (Local Interpretable Model-agnostic Explanations):** Genera variazioni minime dell'input per osservare come cambia l'output, creando un "modello proxy" comprensibile per quella singola predizione (es. Evidenzia quali esatti pixel in una foto hanno convinto la rete neurale che si tratti di un carro armato).
*   **SHAP (SHapley Additive explanations):** Basato sulla Teoria dei Giochi, calcola l'esatto peso (contributo percentuale) che ogni variabile ha avuto nel determinare il risultato finale.

## 🔍 Analisi Operativa ed Applicazioni OSINT

Il rigetto della "Black Box" è un pilastro delle [[Tecniche di analisi strutturata]]:
*   **Responsabilità Giuridica:** Il [[Quadro giuridico]] europeo ([[GDPR]] e l'imminente AI Act) prescrive il diritto del cittadino a ottenere "spiegazioni significative sulla logica utilizzata" per decisioni automatizzate che impattano la sua vita (es. profilazione di rischio criminale in aeroporto). Un'AI OSINT che segnala un falso positivo senza poterlo spiegare espone l'agenzia a pesanti cause legali.
*   **Fiducia del Decisore:** I decisori finali ([[Sistema di informazione per la sicurezza della Repubblica]]) ignoreranno regolarmente i report d'intelligence derivati dall'AI se l'analista non è in grado di illustrare la *catena di derivazione* logica della conclusione.

## 🔮 Lacune Informative e Prossimi Passi

*   **Illusioni di Spiegazione negli LLM:** Richiedere a un modello linguistico di "spiegare il proprio RAGionamento" tramite [[Prompt engineering]] (Chain of Thought) non genera vera XAI. L'LLM genera semplicemente una storia statisticamente verosimile a posteriori per giustificare la risposta (Confabulazione razionale), nascondendo la vera natura opaca del proprio calcolo vettoriale.

## 🔗 Connessioni e Pattern

- [[Intelligenza artificiale generativa]]
- [[Quadro giuridico]]
- [[Bias cognitivo]]
- [[Llm]]
- [[Tecniche di analisi strutturata]]

- [[--]]
F/I/H
- [[--]]
