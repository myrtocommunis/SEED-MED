---
title: Architetture llm
tags:
- OSINT
- processed
- llm-architecture
- moe
- quantization
- multimodal
date: '2026-05-16'
status: validated
depth: deep
sources: '12'
tipo: concetto
---

# Architetture llm

## 🎯 Sintesi Strategica

L'efficacia degli [[Llm]] nel dominio [[Osint]] dipende dalla comprensione delle loro architetture sottostanti e dei relativi vincoli tecnici. Non tutti i modelli sono uguali: la distinzione tra modelli densi (Transformer classici) e sparsi (**MoE - Mixture of Experts**), l'impatto della **quantizzazione** sulla logica analitica e la capacità **multimodale** determinano se un modello è idoneo per un'indagine ad alto rischio o per una sintesi di routine. Per l'analista, la scelta dell'architettura è una decisione di **Opsec** e di **Integrità del Dato**.

## 🏗️ ANATOmia Tecnica: Transformer e MoE

Le architetture moderne si dividono in due paradigmi principali:

1.  **DENSe Transformers:** Ogni parametro del modello viene attivato per ogni token (es. GPT-3). Sono estremamente coerenti ma computazionalmente costosi e lenti.
2.  **MoE (Mixture of Experts):** Il modello è diviso in "esperti" specializzati; per ogni token, vengono attivati solo alcuni esperti (es. Mixtral, GPT-4). 
    - **Vantaggio OSINT:** Maggiore velocità e capacità di gestire domini vasti.
    - **Rischio:** Possibile perdita di coerenza in analisi cross-dominio molto sottili, dove il "routing" tra esperti potrebbe non essere ottimale.

## ⚖️ Quantizzazione e Precisione Analitica

La **Quantizzazione** riduce la dimensione del modello (es. da 16-bit a 4-bit) per permetterne l'esecuzione su hardware locale ([[Postazione di lavoro osint|Postazione di lavoro OSINT]]).
- **Impatto:** Un modello pesantemente quantizzato (inferiore a 4-bit) può mostrare "degradazione logica": pur apparendo fluente, commette errori sottili nel RAGionamento deduttivo o nella gestione di dati numerici (es. coordinate GPS, date).
- **Regola Operativa:** Per analisi di intelligence critica, utilizzare modelli con quantizzazione minima (Q6_K o superiore) o modelli FP16/BF16.

## 🖼️ Multimodalità e Context Window

L'architettura **Multimodale** (es. GPT-4o, Claude 3.5) permette l'analisi nativa di immagini, video e audio senza passare per trascrizioni esterne.
- **OSINT Vision:** Capacità di geolocalizzare una foto analizzando ombre, vegetazione e architettura direttamente nello spazio latente del modello.
- **Context Window:** La "memoria a breve termine". Architetture con finestre ampie (1M+ token) permettono di analizzare interi archivi di documenti (es. dump di leak) mantenendo la coerenza tra l'inizio e la fine del dataset.

## 🛡️ Deployment: Local SLM vs Cloud Foundation

| Tipo | Esempio | Vantaggi | Svantaggi | Opsec |
|---|---|---|---|---|
| **Cloud (Foundation)** | GPT-4o, Claude 3.5 | Potenza massima, reasoning avanzato | Dati escono dall'infrastruttura | Minima |
| **Local (SLM)** | Llama 3, Phi-3, Mistral | Sovranità totale, offline | Richiede hardware potente, meno "intelligente" | Massima |

---
## 🔄 Layer di RAGionamento (Reasoning)

Indipendentemente dall'architettura base, l'accuratezza OSINT viene potenziata da pattern di RAGionamento strutturato:
- **[[Cot]] (Chain of Thought):** Forza il modello a esplicitare i passaggi logici.
- **React:** Permette al modello di usare tool esterni (search, whois) per validare i propri pensieri.
- **[[Self-consistency]]:** Genera più analisi e sceglie la più probabile via voto di maggioranza.

---
## 🔗 Connessioni e Pattern

- [[Ai-assisted analysis]]
- [[Llm]]
- [[Postazione di lavoro osint|Postazione di lavoro OSINT]]
- [[Rag]]
- [[Vector databases]]

- [[--]]
F/I/H
- [[--]]
- [[*Fatti:** I modelli MoE permettono di avere prestazioni da 100B+ parametri con il costo computazionale di un modello da 20B.]]
- [[*Interpretazione:** La sparsità architettonica è l'unica via per portare capacità di intelligence avanzata su dispositivi mobili o in postazioni isolate.]]
- [[*Ipotesi:** Entro il 2026, la distinzione tra "modello" e "tool" svanirà: l'architettura sarà un insieme fluido di agenti-esperti che si attivano on-demand per risolvere task di intelligence specifici.]]

- [[--]]
### Fonti e Bibliografia
- [[Vaswani, A., et al. (2017). *Attention Is All You Need*.]]
- [[Shazeer, N., et al. (2017). *OutRAGeously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer*.]]
- [[Dettmers, T., et al. (2023). *QLoRA: Efficient Finetuning of Quantized LLMs*.]]
- [[Lewis, P., et al. (2020). *Retrieval-Augmented Generation for Knowledge-IntENSive NLP Tasks*.]]
