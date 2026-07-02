---
title: Schede di riferimento operativo
tags:
- OSINT
- processed
- schede-di-riferimento-operativo
date: '2026-05-15'
status: draft
depth: standard
sources: '1'
tipo: concetto
---

# Schede di riferimento operativo

## 🎯 Sintesi Strategica

Le Schede di riferimento operativo rappresentano un consolidamento strutturato di [[Framework teorici]] e metodologie pratiche, finalizzato a guidare l'analisi [[Osint]] (Open Source Intelligence). Esse traducono concetti complessi, come quelli derivanti dagli studi di Pierre Bourdieu, l'[[Framing]] di Entman e la [[Tassonomia]] sulla disinformazione, in strumenti applicabili. Il loro scopo è fornire un approccio sistematico per la valutazione delle informazioni, l'identificazione di minacce (tramite [[Threat assessment]]) e la produzione di Intelligence Brief standardizzati, integrando checklist critiche e linee guida per evitare bias analitici.

## 📚 Contesto e Definizioni

Le Schede di riferimento operativo sono strumenti metodologici progettati per facilitare l'applicazione pratica di quadri concettuali avanzati nell'ambito dell'intelligence da fonti aperte. Esse nascono dall'esigenza di trasformare la teoria in prassi operativa, fornendo agli analisti un set di strumenti agili per navigare la complessità del panorama informativo contemporaneo.

Tra i principali quadri concettuali integrati figurano:
*   **Pierre Bourdieu:** La sua sociologia dei campi e dei capitali (simbolico, sociale, culturale, economico) offre una lente per comprendere le dinamiche di potere e influenza all'interno di specifici contesti informativi.
*   **Entman Frame Analysis:** Un modello per analizzare come le informazioni vengono presentate e interpretate, focalizzandosi su quattro domande operative (definire un problema, diagnosticare le cause, formulare giudizi morali, suggerire rimedi).
*   **Wardle Tassonomia:** Una classificazione dei tipi di disinformazione e misinformazione, che aiuta a categorizzare e valutare la gravità e la natura delle narrazioni ingannevoli.

Queste schede includono anche checklist per l'analisi narrativa, indicatori per l'identificazione di attività coordinate (CIB - Coordinated Inauthentic Behavior), diagnostiche specifiche per diverse narrative e un elenco di "anti-patterns" da evitare per mantenere l'integrità analitica.

## 📊 Dati, Tecnologie e Metriche

L'applicazione delle Schede di riferimento operativo si basa sull'analisi strutturata di dati provenienti da fonti aperte, utilizzando metriche e classificazioni specifiche.

### Bourdieu per l'Intelligence OSINT

Questo framework consente di mappare le dinamiche di potere e influenza all'interno di un "campo" informativo o sociale.

| Concetto           | Definizione Operativa                               | Uso OSINT                                     |
| :----------------- | :-------------------------------------------------- | :-------------------------------------------- |
| **Campo**          | Spazio di lotte con regole proprie                  | Mappare il campo di ogni attore coinvolto     |
| **Capitale Simbolico** | Credibilità, autorità percepita                     | Identificare chi detiene autorità epistemica  |
| **Capitale Sociale** | Network, connessioni, relazioni                     | Analizzare chi amplifica chi; identificare Capitale Sociale e account ponte |
| **Capitale Culturale** | Expertise, credenziali, conoscenza specialistica   | Valutare chi è riconosciuto come esperto e da chi |
| **Dominanti/Sfidanti/Marginali** | Posizione relativa degli attori nel campo | Prevedere le prossime mosse e strategie degli attori |

### Wardle-Tassonomia della Disinformazione e Misinformazione

Questa tassonomia classifica i contenuti ingannevoli in base alla loro gravità e alla natura della manipolazione.

| Gravità | Tipo Wardle                 | Capacità Richiesta                               |
| :------ | :-------------------------- | :----------------------------------------------- |
| **Rosso** | Contenuto fabbricato (4)    | Verifica dell'origine e della provenienza        |
| **Rosso** | Deepfake (7)                | Analisi forense di media digitali                |
| **Rosso** | Contenuto impostore (3)     | Verifica dell'identità e dell'autenticità        |
| **Giallo** | Contesto falso (6)          | Ricerca inversa di immagini/video, analisi timeline |
| **Giallo** | Connessione ingannevole (5) | Comparazione tra titolo e corpo del contenuto    |
| **Giallo** | Contenuto fuorviante (2)    | Fact-checking di dati e affermazioni             |
| **Verde** | SATira/parodia (1)          | Verifica del contesto e del genere comunicativo |

### Indicatori CIB (Coordinated Inauthentic Behavior)

La "Golden Rule" per l'attribuzione di attività coordinate o botnet stabilisce che non si deve etichettare nulla come tale senza almeno tre indicatori primari convergenti. I falsi positivi possono gravemente compromettere la credibilità dell'analisi.

## 🔍 Analisi Operativa ed Applicazioni OSINT

Le Schede di riferimento operativo trovano applicazione diretta in diverse fasi dell'analisi OSINT:

*   **Mappatura del Contesto:** L'applicazione del framework di Bourdieu permette di identificare gli attori chiave, le loro relazioni e la distribuzione di capitale (simbolico, sociale, culturale) all'interno di un ecosistema informativo, prevedendo potenziali conflitti o alleanze.
*   **Valutazione della Credibilità:** La Tassonomia di Wardle è fondamentale per classificare e valutare la natura e la gravità di contenuti potenzialmente ingannevoli, guidando l'analista nella scelta delle tecniche di verifica più appropriate.
*   **Identificazione di Campagne di Influenza:** Gli indicatori CIB e le checklist per l'analisi narrativa sono essenziali per rilevare e attribuire attività di disinformazione o manipolazione coordinate.
*   **Mitigazione dei Bias:** La lista degli "Anti-Patterns da Evitare" funge da promemoria critico per gli analisti, aiutandoli a riconoscere e correggere errori comuni come la gerarchia della credibilità invertita, il paternalismo epistemico o la sovrastima delle interferenze esterne.
*   **Produzione di Intelligence:** Le schede culminano nella fornitura di un "Template Intelligence Brief Standard", che garantisce coerenza e completezza nella presentazione dei risultati analitici. La struttura include: Executive Summary (max 150 parole), Contesto (1/2 pagina), Analisi (1-2 pagine), Assessment, Implicazioni, Limitazioni Metodologiche e Fonti strutturate.

## 🔮 Lacune Informative e Prossimi Passi

Nonostante la loro utilità, le Schede di riferimento operativo sono strumenti dinamici e in continua evoluzione. Le lacune informative attuali e i prossimi passi includono:

*   **Aggiornamento Continuo:** La rapidità con cui evolvono le tattiche di disinformazione e le tecnologie (es. AI generativa) richiede un aggiornamento costante dei framework e delle checklist.
*   **Integrazione di Nuovi Framework:** Esplorare l'integrazione di ulteriori quadri concettuali per arricchire l'analisi, ad esempio modelli di psicologia sociale o di teoria della comunicazione.
*   **Sviluppo di Metriche Quantificabili:** Migliorare la quantificazione di alcuni indicatori, specialmente per l'attribuzione di CIB, per ridurre la soggettività nell'analisi.
*   **Formazione e Standardizzazione:** Sviluppare moduli di studio e pratiche per garantire una comprensione e un'applicazione uniforme delle schede tra gli analisti.
*   **Analisi degli "Anti-Patterns":** Approfondire la ricerca su come mitigare attivamente gli "anti-patterns" identificati, trasformando le avvertenze in strategie proattive.

## 🔗 Connessioni e Pattern

- [[Analisi strutturata]]
- [[Applicazioni osint]]
- [[Disinformazione]]
- [[Framework teorici]]
- [[Osint]]
- [[Threat assessment]]


- [[--]]
F/I/H
- [[--]]
