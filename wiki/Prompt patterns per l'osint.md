---
title: Prompt patterns per l'osint
tags:
- OSINT
- processed
- prompt-patterns-per-l'osint
date: '2026-05-15'
status: draft
depth: standard
sources: '1'
tipo: concetto
---

# Prompt patterns per l'osint

## 🎯 Sintesi Strategica

L'applicazione del [[Prompt engineering]] all'[[Osint]] (Open Source Intelligence) trasforma un [[Large language model]] (LLM) da strumento generico a motore investigativo strutturato. Questo concetto esplora i pattern riutilizzabili — **Persona**, **Template**, **Audience**, **Chain of Verification**, **Flipped Interaction** — e le tecniche di prompting fondamentali (zero-shot, few-shot, meta, generated knowledge) applicate specificamente al contesto investigativo [[Osint]]. La combinazione di un [[Persona]] per la definizione del ruolo investigativo, un [[Template]] per la standardizzazione dell'output e una pipeline di [[Chaining]] per la decomposizione del compito in fasi sequenziali (Raccolta → Estrazione → Correlazione → Verifica → Report) costituisce uno standard operativo per gli analisti [[Osint]] che integrano gli LLM nei workflow d'indagine. La precisione investigativa dipende direttamente dalla struttura del prompt: un prompt generico produce un'analisi generica. Le tecniche strutturate — in particolare il Meta Prompting (astrazione dalla forma al contenuto) e il Generated Knowledge Prompting (due fasi: generazione del contesto e poi task specifico) — riducono le allucinazioni e aumentano la profondità analitica in modo misurabile.

## 📚 Contesto e Definizioni

### La Progressione del Prompting

Le tecniche di prompting si sono evolute per migliorare l'interazione con i [[Large language model]], offrendo maggiore controllo e precisione nell'output.

| Tecnica                 | Definisce                               | Quando Usare                                   | Limiti                                     |
|-------------------------|-----------------------------------------|------------------------------------------------|--------------------------------------------|
| Zero-Shot Prompting | Il task senza esempi                    | Task noti al modello, testing rapido           | Output variabile, meno accurato            |
| Few-Shot Prompting  | Il task + esempi input-output           | Task con formato complesso, standardizzazione  | Consumo elevato di token, contesto limitato |
| Meta Prompting      | La struttura astratta del task          | Ripetibilità cross-dominio, insegnamento       | Richiede astrazione di alta qualità        |
| Generated Knowledge Prompting | Due fasi: contesto → task       | Domini complessi, RAGionamento profondo        | Doppio latency, più token totali           |

*   **Zero-Shot Prompting**: Utilizzo del modello senza alcun esempio specifico. Il modello si affida alla propria conoscenza pre-addestrata.
    *   *Esempio [[Osint]]*: "Classifica il sentiment di questa frase: 'Scommetto che il videogioco è molto più divertente del film.'" → il modello determina "positivo" basandosi su pattern linguistici appresi durante il training.
*   **Few-Shot Prompting**: Presentazione di dimostrazioni di alta qualità (input + output) prima del task target. Permette al modello di comprendere l'intento umano e i criteri di risposta desiderata.
    *   *Esempio [[Osint]]*:
        ```
        Testo: "Lawrence rimbalza su tutto il palco, ballando, correndo, sudando, asciugandosi il viso e mostrando il talento stravagante."
        Sentimento: positivo

        Testo: "Questa schifezza è riuscita a spacciarsi per un vero film, il tipo che fa pagare il biglietto intero e pretende di divertire bambini piccoli."
        Sentimento: negativo

        Testo: "[testo OSINT da classificare]"
        Sentimento: ?
        ```
    Una regola empirica consolidata suggerisce che il Few-Shot Prompting tende a produrre performance superiori rispetto allo Zero-Shot Prompting. Lo svantaggio è il consumo di token, poiché un documento da 500 token con 10 esempi consuma spazio di contesto prezioso per l'analisi vera e propria.
*   **Meta Prompting**: Tecnica che enfatizza la **struttura e la sintassi** del task invece di focalizzarsi sul contenuto specifico. Crea un approccio astratto dove la *forma* prevale sul *contenuto dettagliato*.
    *   La struttura tipo del Meta Prompt:
        ```
        Segui questa struttura per qualsiasi domanda:
        1. Introduzione: Definire l'argomento o i termini chiave
        2. Spiegazione Dettagliata: Scomporre i componenti
        3. Esempio Pratico: Applicazione nel mondo reale
        4. Conclusione: Riassunto in una frase Input: [qualunque input]
        ```
*   **Generated Knowledge Prompting**: Il modello genera prima conoscenza contestuale, poi usa quella conoscenza per il task specifico. Due fasi:
    1.  *Generazione della Conoscenza*: "Descrivi [argomento]"
    2.  *Task Specifico*: "Basandoti sulla descrizione, rispondi a [domanda]"
    Questa tecnica è cruciale in [[Osint]] quando il modello deve dimostrare competenza di dominio — ad esempio, prima di analizzare una vulnerabilità specifica, il modello deve "sapere cosa è" quella classe di vulnerabilità.

### I Pattern di Prompt Engineering

I Prompt Pattern sono schemi riutilizzabili che guidano il comportamento del modello per ottenere output specifici e coerenti.

| Pattern                       | Funzione                                | Output                                  | Scenario [[Osint]]                               |
|-------------------------------|-----------------------------------------|-----------------------------------------|--------------------------------------------------|
| [[Persona]]           | Assegna identità/ruolo al modello       | Tono + prospettiva specialistica        | Analista [[Threat intelligence]], Investigatore Finanziario |
| [[Template]]          | Definisce schema output rigido          | Campi fissi, completa sempre i vuoti    | Report intelligence standardizzati               |
| Audience Pattern          | Specifica il lettore target             | Livello gergo + complessità variabile   | Report per CEO vs. report per SOC analyst        |
| Chain of Verification     | Auto-verifica delle affermazioni        | Output auto-critico, correzioni evidenziate | Validazione claim prima di report                |
| Flipped Interaction       | Il modello pone domande                 | Raccolta requisiti interattiva          | Intake investigativo strutturato                 |

## 📊 Dati, Tecnologie e Metriche

### Pattern Dettaglio — Persona, Template, Audience, CoV, Flipped

#### 1. [[Persona]]

Assegnare un **ruolo specifico** al modello definisce implicitamente tono, vocabolario, profondità e prospettiva. La stessa domanda posta senza persona produce una risposta generica; con una persona, la risposta acquisisce terminologia specialistica e inquadramento appropriato.

| Ruolo Persona                      | Competenza Richiesta                 | Framework Applicato               | Output Tipico                               |
|------------------------------------|--------------------------------------|-----------------------------------|---------------------------------------------|
| Analista [[Threat intelligence]] senior | [[Mitre att&ck]], TTPs, IOC          | [[Mitre att&ck]] Framework        | Classificazione attori/stati, TTP mapping   |
| Investigatore Finanziario AML      | [[Aml-cft|FATF]] red flags, beneficial owner | [[Aml-cft|FATF]] 40 Recommendations       | Pattern riciclaggio, network analysis       |
| Analista Geopolitico               | ACH, scenari probabilistici          | Analysis of Competing Hypotheses  | Scenari 6-12 mesi, valutazione attori       |
| SOC Analyst L2                     | CVSS, log analysis, detection    | NIST IR framework             | Incident report, regole di detection        |
| Analista [[Osint]] senior          | Query design, source evaluation      | [[Osint]] methodology standard    | Dossier entità, report due-diligence        |

**Template Prompt [[Persona]]**:
```
Agisci come [RUOLO SPECIFICO con X anni di esperienza].
Il tuo compito è: [AZIONE INVESTIGATIVA].
Analizza: [DATI IN INPUT].
Risultato atteso: [STRUTTURA OUTPUT].
Livello di dettaglio: [TECNICO/BASE/ESECUTIVO].
Classifica ogni finding secondo [FRAMEWORK].
```
Esempio [[Osint]] operativo:
```
Sei un analista OSINT senior specializzato in indagini finanziarie.
Devo investigare l'azienda "Acmetech Ltd" sospettata di attività fraudolente.
Genera: (1) 10 Google Dorks per documenti ed email leak associati,
(2) Query Shodan per infrastrutture collegate,
(3) Varianti del nome aziendale inclusi abbreviazioni, errori comuni e nomi precedenti.
```

#### 2. [[Template]]

Definisce una **struttura di output rigida** che il modello deve compilare. Elimina la variabilità del formato e garantisce completezza. Il modello non può saltare un campo quando il template lo richiede esplicitamente.

**[[Template]] per Report [[Osint]]**:
```
SUBJECT: [nome soggetto/entità sotto indagine]
CLASSIFICATION: [livello di confidenzialità]
EXECUTIVE SUMMARY: [sintesi max 3 righe]
KEY FINDINGS: [lista numerata evidenze]
ENTITIES IDENTIFIED: [tabella: nome | tipo | ruolo | fonte]
CONNECTIONS MAP: [relazioni tra entità con evidenze]
CONFIDENCE ASSESSMENT: [high/medium/low per finding]
INTELLIGENCE GAPS: [informazioni mancanti]
RECOMMENDED ACTIONS: [prossimi passi investigativi]
```
**[[Template]] per Analisi Vulnerabilità CVE**:
```
Nome della vulnerabilità: [nome]
CVE ID: [CVE-YYYY-NNNNN]
Gravità: [Critica/Alta/Media/Bassa]
Componente interessato: [componente + versioni]
Vettore di attacco: [descrizione tecnica + CVSS v3.1]
Proof of Concept: [payload sintetico]
Regole di detection: [Sigma + Snort]
Remediation: [passaggi ordinati per priorità]
```

#### 3. Audience Pattern

Specifica **chi è il lettore previsto**; il modello adatta complessità, gergo, tono ed esempi. Essenziale quando la stessa conoscenza deve servire stakeholder diversi.

| Stakeholder      | Livello Tecnico | Tono        | Framework Atteso          | Metriche Chiave           |
|------------------|-----------------|-------------|---------------------------|---------------------------|
| CEO / Board      | Basso           | Esecutivo   | Scenari + probabilità     | ROI, rischio finanziario  |
| Director IT/SOC  | Medio           | Tecnico     | [[Mitre att&ck]] + CVSS | MTTR, coverage detection  |
| Analyst [[Osint]] | Alto            | Specialistico | Framework [[Osint]] standard | Sources, confidence levels |
| Team Legale      | Basso/Medio     | Formale     | Quadro normativo          | Compliance, exposure      |
| Client External  | Basso           | Professionale | Sintesi non-classificata  | Findings principali       |

#### 4. Chain of Verification

Chiede al modello di generare una risposta, poi **verificare sistematicamente le proprie affermazioni**. Riduce le allucinazioni trasformando il modello in produttore e critico del proprio output.
```
Dimmi [N] fatti su [argomento].
Dopo averli elencati, verifica ogni affermazione:
- Sono sicuro di questo fatto?
- Potrebbe esserci un errore?
- La fonte è coerente con altre fonti note?
Correggi eventuali inesattezze trovate.
```
Applicazione [[Osint]] per validazione claim prima del report:
```
Per ogni claim nel report, applica:
1. Citazione esatta della fonte originale
2. Cross-reference con almeno un'altra fonte indipendente
3. Valutazione attendibilità della fonte (Scala Admiralty)
4. Flag se il claim non è verificabile
```

#### 5. Flipped Interaction

Il **modello pone le domande** invece di rispondere. Impedisce al modello di fare assunzioni e rispecchia il modo in cui un esperto umano lavora — raccogliendo i requisiti prima di produrre una soluzione.
```
Voglio [OBIETTIVO]. Non dirmi tu la soluzione:
fai tu le domande a me, una alla volta, per capire
meglio le mie esigenze. Quando avrai abbastanza
informazioni, dammi un consiglio personalizzato.
```

### Volume di Dati e Filtraggio Sistematico

Gli analisti [[Osint]] affrontano enormi quantità di informazioni da fonti eterogenee. I prompt ben strutturati permettono di filtrare, sintetizzare e correlare dati in modo sistematico, trasformando il rumore in intelligence actionable.

| Dimensione [[Osint]] | Sfida                      | Soluzione Prompt Pattern      | Metrica di Successo         |
|----------------------|----------------------------|-----------------------------------|-----------------------------|
| Volume               | Troppi dati, segnale persa | [[Template]] + filtro schema | Precisione extraction >95%  |
| Precisione           | Output generico, inutilizzabile | [[Persona]] + domain specific | Utilizzabilità report       |
| Ipotizzazione        | Piste investigative limitate | Generated Knowledge Prompting + Flipped Interaction | Nuovo numero di piste generate |
| Allucinazioni        | Falso positivo pericoloso  | Chain of Verification         | Error rate < 2%             |

### Generazione di Query di Ricerca con LLM

Un analista [[Osint]] usa un [[Large language model]] per la generazione sistematica di query mirate:

| Tipo Query      | Strumento Target              | Pattern Utilizzato                | Esempio Applicabile                               |
|-----------------|-------------------------------|-----------------------------------|---------------------------------------------------|
| [[Google dorks]] | Google, Bing, Duckduckgo      | Meta Prompting + [[Template]] | `"site:gov filetype:pdf \"confidential\""`        |
| Shodan/CENSys | Motori IoT/infrastructure | [[Persona]] (SOC Analyst) | Hostnames, banner grab patterns                   |
| Social Media    | Twitter/X, Linkedin, Reddit   | Audience Pattern              | Keyword combinations, hashtag research            |
| Name Variants   | Database aziendali            | Few-Shot Prompting            | Abbreviazioni, errori ortografici, alias          |
| Cross-lingual   | Fonti internazionali          | Generated Knowledge Prompting | Traduzione contestuale di termini chiave          |

## 🔍 Analisi Operativa ed Applicazioni OSINT

### Pipeline di Analisi [[Osint]] con [[Chaining]]

Il [[Chaining]] applicato all'[[Osint]] crea una pipeline strutturata in 5 step:
```
┌─────────────┐   ┌──────────────┐   ┌──────────────┐   ┌────────────┐   ┌──────────┐
│   STEP 1    │ → │   STEP 2     │ → │   STEP 3     │ → │   STEP 4   │ → │   STEP 5 │
│  RACCOLTA   │   │  ESTRAZIONE  │   │ CORRELAZIONE │   │  VERIFICA  │   │  REPORT  │
│ Query gen.  │   │ Entità, dati,│   │ Pattern,     │   │ CoV/AV     │   │ TEMPLATE │
│ + Dorks+    │   │ relazioni    │   │ anomalie     │   │ Cross-ref  │   │ Standard │
│ API fetch   │   │              │   │              │   │ Adm.scal   │   │          │
└─────────────┘   └──────────────┘   └──────────────┘   └────────────┘   └──────────┘
```

| Step           | Input                 | Processo Prompt Pattern                               | Output                                      |
|----------------|-----------------------|-----------------------------------------------------------|---------------------------------------------|
| 1 - Raccolta   | Target investigation  | Generated Knowledge Prompting + Meta Prompting    | Query list, source map                      |
| 2 - Estrazione | Fonti raccolte         | [[Template]] + Few-Shot Prompting [[Json]] schema | Entità, date, relazioni in formato strutturato |
| 3 - Correlazione | Entità estratte       | [[Persona]] (analista correlazione)               | Pattern, anomalie, network map              |
| 4 - Verifica   | Correlazioni trovate  | Chain of Verification                                 | Claim validati / confutati                  |
| 5 - Report     | Analisi verificate    | [[Template]] (report intelligence)                | Report [[Osint]] completo in formato standard |

### LLM come [[Threat intelligence]] Multi-Use

| Use Case [[Osint]]           | Prompt Pattern                | Output Operativo                                  |
|------------------------------|-----------------------------------|---------------------------------------------------|
| Log Analysis (SOC L2)        | [[Persona]] + [[Template]] | IOC table, CVSS severity, mitigation steps    |
| CVE Parsing                  | Generated Knowledge Prompting + Meta Prompting | Exploitability analysis, detection rules          |
| Log4Shell Deep Dive          | Few-Shot Prompting domain knowledge | PoC payload, Sigma/Snort rules                    |
| Cross-source event correlation | [[Persona]] + [[Chaining]] | Timeline + network map, confidence score          |
| Social engineering analysis  | Audience Pattern + [[Template]] | Phishing indicators + training scenarios          |

### Estrazione Dati Strutturata per [[Osint]] — Schema e Template Operativo

L'estrazione di dati strutturati è uno degli usi più potenti degli LLM per [[Osint]]: trasformare testo non strutturato in dati machine-readable.

**[[Template]] Estrazione Dati [[Osint]]**:
```
Analizza il seguente testo ed estrai in JSON: Schema:
entities: [{name, type (person/org/location), role, attributes, confidence}]
events: [{description, date, location, actors: [], type, confidence}]
relationships: [{entity1, entity2, relationship_type, evidence}]
financial_data: [{amount, currency, date, from, to, purpose}]
metadata: {source, date_published, author, reliability_assessment} Regole:
- Usa null per campi non presenti, NON inventare dati
- Confidence score 0.0-1.0 per ogni entità e evento
- Cita il passaggio esatto come 'evidence' per ogni relazione
- Date in ISO 8601 (YYYY-MM-DD)
- Distingui fatti espliciti da inferenze del modello
```
**Tecniche per Massimizzare la Qualità di Estrazione**:

| Tecnica                 | Implementazione             | Impatto                     | Metrica                     |
|-------------------------|-----------------------------|-----------------------------|-----------------------------|
| Definire schema rigido  | [[Json]] schema esplicito   | Consistenza output          | Schema compliance > 95%     |
| Few-Shot Prompting example | 1-2 esempi completi         | Riproduzione pattern        | Extraction accuracy         |
| Gestione incertezza     | null + confidence score     | Trasparenza                 | Confidence distribution     |
| Chain of Verification | Post-extraction check       | Riduzione allucinazioni     | Error rate -60-80%          |

## 🔮 Lacune Informative e Prossimi Passi

Questo concetto copre il panorama completo dei Prompt Pattern per [[Osint]] ma non affronta:

*   **Benchmarks quantitativi** della performance dei pattern (ad esempio, accuracy improvement del [[Persona]] rispetto allo Zero-Shot Prompting su dataset [[Osint]] reale).
*   **[[Prompt injection]] difensivo** nei pattern (come rafforzare i template contro la manipolazione).
*   **Avalanche di token**: strategie di ottimizzazione del contesto quando i prompt combinati superano le finestre di contesto (4K/8K/32K).

I prossimi passi dovrebbero includere un'analisi comparativa su dataset [[Osint]] reali delle diverse combinazioni di pattern, misurando accuracy, latenza e consumo token.

## 🔗 Connessioni e Pattern

- [[Json]]
- [[Large language model]]
- [[Osint]]
- [[Prompt engineering]]
- [[Prompt injection]]
- [[Threat intelligence]]


- [[--]]
F/I/H
- [[--]]
