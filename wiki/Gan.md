---
title: "Gan"
tags: ["OSINT", "processed", "gan", "deepfake", "ai", "machine-learning"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Gan

## 🎯 Sintesi Strategica

Le **GAN (Generative Adversarial Networks - Reti Avversarie Generative)** sono una classe rivoluzionaria di algoritmi di [[Machine learning]] (Deep Learning) introdotta nel 2014. Rappresentano il motore tecnologico primario alla base della creazione di volti inesistenti (es. "Thispersondoesnotexist.com") e dei [[Deepfake]] iper-realistici. Nelle mani dell'[[Osint]] difensiva, le GAN sono un vettore estremo di [[Disinformazione]] visiva e creazione di finte identità (Sock Puppetry su scala industriale).

## 📚 Contesto e Definizioni

L'architettura "Avversaria" significa che il sistema è composto da due reti neurali che combattono tra loro:
1.  **Il Generatore:** (Il falsario). Il suo compito è creare immagini finte partendo dal rumore matematico casuale.
2.  **Il Discriminatore:** (Il detective). Il suo compito è esaminare le immagini prodotte dal Generatore mescolate a foto reali e indovinare quali sono false.
Le due reti si addestrano a vicenda in un ciclo continuo, finché il Generatore non diventa talmente abile a creare volti perfetti da ingannare matematicamente il Discriminatore.

## 📊 Dati, Tecnologie e Metriche

I gruppi [[Apt]] statali (es. propaganda russa e cinese) creano enormi [[Botnet]] sui social network (X/Twitter) utilizzando profili con volti generati tramite GAN. A differenza di un tempo (dove il bot usava foto rubate ad altre persone, facilmente rintracciabili via Reverse Image Search nell'[[Imint]]), un volto GAN non è mai esistito prima nella storia umana. Google non troverà riscontri, rendendo la validazione della falsa identità (Fake Persona) quasi impossibile per l'utente medio. L'analista forense deve scovare le microscopiche asimmetrie (es. orecchini sdoppiati o pupille irregolari) che il Generatore sbaglia ancora a renderizzare.

## 🔗 Connessioni e Pattern

- [[Deepfake]]
- [[Machine learning]]
- [[Disinformazione]]
- [[Imint]]
- [[--]]
F/I/H
- [[--]]
