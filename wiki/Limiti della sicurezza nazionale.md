---
title: Limiti della sicurezza nazionale
tags:
- OSINT
- processed
- limiti-della-sicurezza-nazionale
date: '2026-05-15'
status: draft
depth: standard
sources: '1'
tipo: concetto
---

# Limiti della sicurezza nazionale

## 🎯 Sintesi Strategica

La [[Sicurezza nazionale]] opera entro una triade di limiti: costituzionali (interni), sovranazionali ([[Cedu]]/UE), e procedurali (standard di referenziazione). Questo quadro è strutturale per l'analista [[Osint]], poiché la sorveglianza e la sicurezza nazionale non sono ambiti extra-legali, ma sono vincolati da quattro pilastri giuridici interconnessi. L'Art. 8 della Convenzione Europea dei Diritti Umani (CEDU) stabilisce il diritto alla [[Privacy]] come limite esterno alla sorveglianza. La Legge 124/2007 Art. 33(9) disciplina i dati acquisiti dal SIS2 italiano. L'[[Ai act]] Art. 4(2) esclude formalmente la sicurezza nazionale dalla sua applicazione. L'Intelligence Community Standard 206-01 (ICS 206-01) è lo standard della Intelligence Community USA su come citare e referenziare PAI, CAI e OSINT. Il nodo cruciale è il vuoto normativo strutturale tra questi livelli: la sorveglianza digitale è tecnicamente possibile globalmente ma giuridicamente frammentata, creando opportunità OSINT dove la normativa è assente o contraddittoria.

## 📚 Contesto e Definizioni

La sicurezza nazionale è un concetto complesso, la cui operatività è intrinsecamente legata a un robusto contesto normativo che ne definisce i confini.

### Art. 8 CEDU: Il Diritto alla Privacy come Limite Globale

L'**Articolo 8 della Convenzione Europea dei Diritti Umani** (CEDU) è fondamentale per la sorveglianza che può violare il diritto alla privacy. Questo articolo è la pietra angolare del diritto alla privacy in Europa:

| Articolo | Diritto | Applicabilità alla Sorveglianza |
|---|---|---|
| **Art. 8(1)** | Diritto al rispetto della vita privata e familiare | Protegge comunicazioni personali, dati, domicilio |
| **Art. 8(2)** | Interferenze solo se: (a) previste dalla legge, (b) perseguono scopi legittimi, (c) necessarie in società democratica | Tre-prong test per qualsiasi sorveglianza |

Il **Principio del "Three-Prong Test"** richiede che, per legittimare un'interferenza con l'Art. 8, lo Stato dimostri che la misura è:
1.  **"Foreseen by law"**: prevista da una norma chiara e accessibile.
2.  **"Legitimate aim"**: persegue un obiettivo legittimo (es. sicurezza nazionale, prevenzione del crimine).
3.  **"Necessary in a democratic society"**: proporzionata al fine perseguito.

Un paradosso fondamentale, rilevato in letteratura, è che l'Art. 4(2) del Trattato sull'Unione Europea (TEU) afferma che «la sicurezza nazionale rimane di esclusiva competenza degli Stati Membri», mentre l'Art. 8 CEDU si applica a *tutti* gli Stati del Consiglio d'Europa, creando un potenziale conflitto gerarchico.

### Giurisprudenza CEDU Sostanziale (2021)

Quattro sentenze fondamentali del 2021 hanno definito il quadro applicativo dell'Art. 8 CEDU:

| Caso | Corte | Data | Principio Cardine | Impatto OSINT |
|---|---|---|---|---|
| **Big Brother Watch v. UK** | ECtHR (Grand Chamber) | 2021-05-25 | La sorveglianza di massa deve avere garanzie contro abusi; il monitoraggio indiscrimiNATO è legittimo SOLO con supervisione giudiziaria e limiti chiari. | Le "leak" di Snowden sono state oggetto di questa causa. |
| **Centrum v. Sverige** | ECtHR (Grand Chamber) | 2021-05-25 | La sorveglianza preventiva indiscriminata non è "necessaria in società democratica". | Nessun programma di sorveglianza generalizzata può essere legalmente blindato. |
| **Claeys e Groeter v. Germania** | ECtHR | 2021-05-07 | Le intercettazioni mirate devono rispettare l'Art. 8; l'equivoco sui limiti di proporzione è una violazione. | Il parallelismo con XKEYSCORE: sorveglianza mirata è legale se proporzionata. |
| **LQdN v. France** | CJEU | 2020-07-06 | La data retention per sicurezza nazionale è soggetta a [[Quadro normativo osint|GDPR]]/EPD se coinvolge ECSPs (Electronic Communications Service Providers). | La "finestra EU" sulla sicurezza: attiva solo attraverso il settore privato. |

### Legge 124/2007: Il Quadro Italiano

La **Legge 3 agosto 2007, n. 124** ha riformato il comparto dell'intelligence italiano, istituendo il Sistema di Informazione per la Sicurezza della Repubblica (SIS), con il Dipartimento delle Informazioni per la Sicurezza (DIS), l'Agenzia Informazioni e Sicurezza Esterna (AISE) e l'Agenzia Informazioni e Sicurezza Interna (AISI).

| Articolo | Oggetto | Impatto per OSINT |
|---|---|---|
| **Art. 1** | Istituisce il Sistema di Informazione per la Sicurezza della Repubblica | Definisce la struttura base del sistema di intelligence italiano. |
| **Art. 31** | Disposizioni sui poteri di intercettazione | Limita i poteri dell'AISI a quanto autorizzato dalla magistratura. |
| **Art. 33(9)** | Utilizzo dei dati acquisiti | I dati raccolti dall'AISI possono essere utilizzati SOLO per gli scopi per cui sono stati acquisiti. |
| **Art. 34** | Controlli parlamentari | Il Comitato Parlamentare per la Sicurezza della Repubblica (COPASIR) rende conto al Parlamento delle attività del Sistema. |
| **Art. 36** | Garante Privacy | Il Garante per la Protezione dei Dati Personali supervisiona l'AISI. |

L'**Art. 33(9)** stabilisce il **principio di destinazione** (purpose limitation) nel contesto intelligence: i dati acquisiti nell'esercizio delle funzioni del Sistema «non possono essere utilizzati per fini diversi da quelli per i quali sono stati acquisiti». Anche quando i dati sono stati acquisiti legittimamente, il loro riuso è vincolato all'autorizzazione del COPASIR, al controllo del Garante Privacy e al rispetto dei vincoli CEDU.

## 📊 Dati, Tecnologie e Metriche

### Mappa Normativa Interlocale

La sicurezza nazionale è soggetta a un complesso intreccio di normative a diversi livelli:

| Livello | Strumento | Ambito | Limite alla Sicurezza Nazionale |
|---|---|---|---|
| **Costituzionale (IT)** | Costituzione Italiana (Art. 15, 13, 24) | Privacy telecomunicazioni, libertà personale, difesa in giudizio | Massimi limiti interni |
| **Legale (IT)** | Legge 124/2007 + Art. 33(9) | AISE/AISI, dati acquisiti, controlli parlamentari | Purpose limitation, controllo parlamentare |
| **Europeo (CEDU)** | Art. 8 CEDU + 4 sentenze 2021 | Sorveglianza di massa e mirata | Three-prong test, proporzionalità |
| **Europeo (UE)** | AI Act Art. 4(2) + [[GDPR]] Art. 23 | AI systems, data protection, deroghe | AI Act *esclude* sicurezza nazionale; [[GDPR]] deroghe limitate |
| **Globale (US)** | ICS 206-01 (DNI) | Standard di citazione e referenziazione OSINT | Procedurale (non sostanziale) — non limita la sorveglianza |

### Contraddizione Fondamentale UE

Esiste una contraddizione intrinseca nell'approccio dell'Unione Europea alla sicurezza nazionale:

| Normativa | Posizione sulla Sicurezza Nazionale | Contraddizione |
|---|---|---|
| **TEU Art. 4(2)** | "Sole responsibility of Member States" — nessuna competenza UE | → |
| **AI Act Art. 4(2)** | "Does not apply to AI systems used exclusively for national security" | → |
| **CJEU LQdN/Privacy International** | "Data retention by ECSPs per security nazionale = soggetta a [[GDPR]]/EPD" | **Conflitto**: il legislatore UE *esclude* la sicurezza nazionale; il tribunale UE *include* le ECSPs coinvolte. |

## 🔍 Analisi Operativa ed Applicazioni OSINT

### 4.1 L'AI Act e il Vuoto Normativo

L'**Art. 4(2) dell'AI Act** (Regolamento UE 2024/1689) stabilisce:
> «This Regulation does not apply to AI systems where and in so far they are placed on the market, put into service, or used with or without modification exclusively for military, defence or national security purposes, regardless of the type of entity carrying out those activities.»

Il paradosso è duplice:
1.  **Esclusione totale**: Qualsiasi sistema di [[Fondamenti di ai|intelligenza artificiale]] per sicurezza nazionale è *completamente* escluso dall'AI Act, anche se sviluppato da un fornitore privato UE.
2.  **Qualsiasi entity**: La clausola si applica "regardless of the type of entity" — anche se l'attore è un'azienda privata, se usa l'AI per sicurezza nazionale, l'AI Act non si applica.

**Implicazione OSINT**: Se uno Stato membro utilizza sistemi come Palantir o spyware come Pegasus per sicurezza nazionale, né l'AI Act né il [[Quadro normativo osint|GDPR]] si applicano direttamente. Il **solo controllo** è l'Art. 8 CEDU e i controlli interni dello Stato. Questo rappresenta un vuoto normativo strutturale.

### 4.2 ICS 206-01: Standard Procedurale per OSINT

L'**Intelligence Community Standard 206-01** (DNI.gov) è uno standard pubblicato dal Direttore per l'Intelligenza Nazionale (DNI) USA che stabilisce un approccio comune per citare e referenziare tre tipi di fonti:

| Tipo di Fonte | Definizione ICS 206-01 | Esempio |
|---|---|---|
| **PAI** (Publicly Available Information) | Informazioni accessibili al pubblico senza restrizioni | Notizie, social media, documenti governativi pubblici |
| **CAI** (Commercially Available Information) | Informazioni acquistabili da fonti commerciali | Database a pagamento, report di analisti privati |
| **OSINT** (Open Source Intelligence) | Prodotto analitico derivato da PAI/CAI con metodologia documentata | Intelligence report prodotto con metodi OSINT |

I **5 Pilastri ICS 206-01** sono:
1.  **Common citation format**: standard uniforme per PAI/CAI/OSINT in tutti i prodotti analitici IC.
2.  **Provenance tracking**: tracciabilità completa della fonte alla citazione.
3.  **Credibility assessment**: valutazione dell'affidabilità della fonte su scala standardizzata.
4.  **Product labeling**: etichettatura chiara dei prodotti che utilizzano OSINT.
5.  **Integration with PA/CAI**: integrazione fluida tra PAI, CAI e OSINT nei report finali.

**Implicazione strategica**: l'ICS 206-01 è lo standard più alto di professionalizzazione OSINT. Non limita la *capacità* di raccolta (come fa la CEDU) ma *come* si riferiscono le fonti raccolte. Per l'analista OSINT internazionale, adottare ICS 206-01 significa allinearsi allo standard di citazione più diffuso nel mondo intelligence.

### 4.3 Il Vuoto Normativo Strutturale

La sicurezza nazionale ha limiti interni dati dalla costituzione ed esterni dati dalla CEDU e dall'UE, ma questi limiti sono **asimmetrici**:

| Tipo | Esistenza | Enforceabilità |
|---|---|---|
| **Limiti costituzionali IT** | Sì | Alte (ma auto-limitazione possibile) |
| **Limiti CEDU** | Sì | Alte (per Stati che rispettano la CEDU) |
| **Limiti EU (AI Act)** | No (esclusi) | N/A |
| **Limiti EU ([[GDPR]])** | Sì (solo per ECSPs) | Medio (paradossale) |
| **Standard OSINT (ICS 206-01)** | Procedurale | Volontaria (non legale) |

## 🔮 Lacune Informative e Prossimi Passi

-   **LACUNA 1**: La fonte non specifica il numero di regolamento UE dell'AI Act. È stato verificato in letteratura come **Regolamento UE 2024/1689**.
-   **LACUNA 2**: Mancano i dettagli sul **FISA §702** — il quadro legale USA per la sorveglianza di non-cittadini USA. Questo è necessario per comprendere la legittimità di programmi come XKEYSCORE sulla base legale statunitense.
    -   **Prossimo passo**: Verificare il testo FISA §702 e il rapporto PCLOB sulla sua implementazione.
-   **LACUNA 3**: Non è trattata la relazione tra **ICS 206-01** e i **[[Berkeley Protocol]] on Digital Open Source Investigation** (ONU, 2019).
    -   **Prossimo passo**: Confrontare i due standard per identificare sinergie o divergenze.
-   **LACUNA 4**: Il caso **Cambridge Analytica** è un ponte cruciale tra dati commerciali e OSINT ma non è sviluppato.
    -   **Prossimo passo**: Approfondire il caso come esempio di "sorveglianza privata senza AI Act né CEDU".

## 🔗 Connessioni e Pattern

- [[Ai act]]
- [[Cedu]]
- [[Osint]]
- [[Privacy]]
- [[Sicurezza nazionale]]


- [[--]]
F/I/H
- [[--]]
