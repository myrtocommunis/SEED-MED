---
title: Modelli mcquail
tags:
- OSINT
- processed
- modelli-mcquail
date: '2026-05-15'
status: draft
depth: standard
sources: '1'
tipo: concetto
---

# Modelli mcquail

## 🎯 Sintesi Strategica

I [[Modelli mcquail]] sulle funzioni sociali dei media rappresentano un pilastro fondamentale per l'analisi delle dinamiche comunicative, specialmente nel contesto della [[Propaganda]] e delle operazioni di influenza. La propaganda è una persuasione sistematica volta a modellare percezioni, orientare atteggiamenti e indurre comportamenti in pubblici target, operando in un ecosistema comunicativo che include mezzi legittimi e illegittimi.

Il quadro teorico integra le quattro funzioni sociali dei media di Mcquail (informazione, correlazione, continuità, mobilitazione) con la tripartizione classica della propaganda (bianca, grigia, nera), che classifica la riconoscibilità della fonte. L'intersezione di questi due modelli genera una **matrice operativa 4x3**, strumento essenziale per l'analista OSINT nella classificazione delle campagne di influenza.

A complemento, il [[Propaganda]] aggiunge una dimensione strutturale-economica, evidenziando come filtri quali la proprietà dei media, la pubblicità, le fonti, il "flak" (pressioni) e l'ideologia dominante influenzino la narrazione. Fenomeni come il Negativity Bias e la Goodhart's Law illustrano ulteriormente come le metriche di engagement possano distorcere la qualità dell'informazione, portando a sensazionalismo e "churnalism".

## 📚 Contesto e Definizioni

La propaganda, in senso operativo, è l'organizzazione del discorso attraverso:
*   **Selezione**: ciò che è incluso nel racconto pubblico.
*   **Omissione**: ciò che è sistematicamente escluso.
*   **Incadratura (framing)**: come è presentato ciò che è incluso.
*   **Ripetizione**: la meccanica della familiarità che genera accettazione.
*   **Emotional priming**: l'attivazione di bias cognitivi (paura, rabbia, orgoglio) prima della presentazione del contenuto.

È cruciale distinguere tra [[Propaganda]] e Manipolazione: la propaganda è pianificabile, targettizzata e sistematica, operando in un contesto competitivo che implica contropropaganda. La manipolazione, invece, è intenzionale e occulta, efficace quando l'emittente ha un forte controllo sull'informazione o il pubblico ha scarse risorse di filtro. L'elemento chiave è la credibilità dell'emittente e l'Effetto di realtà, dove la percezione di veridicità è più importante della verità oggettiva.

### La Tripartizione Propagandistica

La classificazione della propaganda si articola in:
*   **Bianca**: Fornisce un'immagine positiva senza inganno, tipica della comunicazione istituzionale o di brand, focalizzata sulla trasparenza.
*   **Grigia**: Implica occultamento e selettività riguardo la verità, con un focus sull'opacità strategica piuttosto che sulla falsità diretta.
*   **Nera**: Altamente ingannevole, utilizza materiale distorto ed emotivo, basata su falsità deliberata.

### I Modelli di Pubblico (Sorre, 2011)

Il modello di Mcquail presuppone un "pubblico"; i Modelli di Pubblico di Sorre (2011) offrono una categorizzazione complementare:
1.  **Massa manipolabile**: pubblico passivo, facilmente influenzabile (modello ipodermico).
2.  **Pubblico cosciente**: in grado di costruire un'opinione pubblica autonoma.
3.  **Insieme di mercati**: pubblico targettizzato e RAGgruppato (modello marketing).
4.  **Partner interattivi**: capaci di avere un controllo sui processi comunicativi (modello partecipativo/democratico).

La tipologia di pubblico determina l'efficacia delle tattiche propagandistiche.

### Le Cinque Funzioni dei Media secondo Mcquail

| Funzione        | Definizione                                    | Manifestazione nell'ambiente strategico                                                              |
| :-------------- | :--------------------------------------------- | :--------------------------------------------------------------------------------------------------- |
| **Informazione** | Trasmettere dati e fatti al pubblico           | Reportage, bollettini, fact-checking; ma anche disinformazione mascherata da informazione.           |
| **Correlazione** | Interpretare e dare senso ai fatti             | Editoriali, commento, framing, selezione delle notizie.                                              |
| **Continuità**   | Trasmettere valori culturali e norme           | Nazionalismo, memoria collettiva, narrazione identitaria.                                            |
| **Mobilitazione** | Indurre azione collettiva verso un obiettivo | Campagne di reclutamento, boicottaggi, attivismo coordiNATO, radicalizzazione.                       |
| **Intrattenimento** | Svago e relax                                  | Distrazione tramite intrattenimento, efficace per tenere le masse occupate senza sforzo cognitivo. |

## 📊 Dati, Tecnologie e Metriche

### Il Quadro Normativo SISR e la Legge 124/2007

La propaganda e le funzioni dei media operano entro il quadro normativo del SISR. La [[Legge 124-2007]] definisce i limiti entro cui l'analisi propagandistica deve operare, includendo il Segreto di Stato (con limiti di 15-30 anni e esclusioni per reati gravi), il ruolo del COPASIR nella verifica della costituzionalità delle attività e le Garanzie Funzionali per gli addetti delle agenzie. L'analista OSINT deve distinguere tra propaganda statale legittima, propaganda straniera come minaccia e propaganda interna come indicatore di instabilità.

### Il Quadro FIMI EU/[[NATO]] per la Propaganda Moderna

Un aggiornamento critico integra il quadro EU FIMI (Foreign Information Manipulation and Interference) e la tassonomia [[NATO]] della disinformazione:

**4 blocchi architetturali FIMI (EU EEAS report):**
| Blocco                  | Definizione                                                                                             | Attribuzione |
| :---------------------- | :------------------------------------------------------------------------------------------------------ | :----------- |
| Official state channels | Parlano per conto stato (presidente, PM, ambasciate, ministeri, istituti culturali)                     | Manifesta    |
| State-controlled outlets | Media statali o privati con ownership statale, broadcast/siti/social                                    | Overt        |
| State-linked channels   | Mascherano affiliazione a stato: think tank fittizi, agenzie stampa private con cliente governativo     | Covert       |
| State-aligned channels  | Nessuna evidenza diretta di affiliazione ma allineamento sistematico con le narrative statali           | Non attribuito |

**Framework [[NATO]]/EU Tassonomia Disinformazione:**
| Categoria     | Contenuto | Intento              | Esempio Operativo                               |
| :------------ | :-------- | :------------------- | :---------------------------------------------- |
| Misinformation | Falso     | Nessun intento dannoso | Cittadino condivide bufala credendola vera      |
| Disinformation | Falso     | Intento di danneggiare | State actor crea info false destabilizzanti     |
| Malinformation | Vero      | Intento di danneggiare | Leak documenti classificati per screditare (Snowden) |

**Tipologie di contenuti per gravità:** SATira/Parodia (basso) → Fuorviante cherry-picking (medio) → Impostore (alto) → Fabbricato (alto) → Ingannante (medio) → Falso (alto) → Manipolato/deepfake (alto) → Amplificato (alto).

### Il Processo di Sovversione (Krieg, 2023)

La sovversione è lo sfruttamento strategico delle vulnerabilità sociali, psicologiche, infrastrutturali e fisiche nell'ambiente informativo da parte di un avversario esterno per erodere consenso o status quo sociopolitico. Il processo si articola in un funnel:
Discorso sociale → Discorso media tradizionali e società civile → Discorso rilevante per le politiche tra esperti e decisori → Mobilitazione → **Cambiamento strategico del decisore politico**.
Questo è il processo che l'analista OSINT deve intercettare.

### Tecniche dei Servizi di Intelligence nell'Uso dei Media

| Tecnica                      | Descrizione                                                                 | Impatto OSINT                                     |
| :--------------------------- | :-------------------------------------------------------------------------- | :------------------------------------------------ |
| **Affare Dreyfus**           | Caso storico di manipolazione mediatica di stato                            | Riconoscimento di pattern ricorrenti              |
| **Agenda cutting**           | Omissione sistematica di notizie sgradite                                   | Bias di disponibilità nella narrazione pubblica   |
| **ABC della disinformazione** | Framework di classificazione degli effetti                                  | Standard di attribuzione                          |
| **Principio di verosimiglianza** | Deve suonare plausibile, non necessariamente vero                           | Contrasto: cross-validation con fonti primarie    |
| **Carattere indiretto dell'operazione** | Notizia proveniente da fonti "neutrali"                                     | Pattern di attribution nella tripartizione grigia |
| **Tecnica del diversivo** (pseudo-eventi) | Creare fatti artificiali per spostare l'attenzione                          | Pattern Distract (5D methodology)                 |
| **Notizia incartata**        | Notizia principale detta "tra le righe"                                     | Pattern di correlazione deviata                   |
| **Contesto vs attenuazione** | Allarmismo o banalizzazione della notizia                                   | Metriche di framing                               |

L'[[Ai act]] introduce l'etichettatura obbligatoria per i contenuti generati da AI, come i deepfake, rendendo la loro rilevazione una competenza OSINT cruciale.

## 🔍 Analisi Operativa ed Applicazioni OSINT

L'analista OSINT utilizza i [[Modelli mcquail]] e i concetti correlati per:
*   **Classificare campagne di influenza**: La matrice 4x3 (funzioni Mcquail x tripartizione propaganda) permette una mappatura dettagliata di ogni tattica persuasiva.
*   **Identificare l'attribuzione**: Distinguere tra propaganda bianca (trasparente), grigia (opaca) e nera (ingannevole) è fondamentale per valutare la fonte e l'intento.
*   **Monitorare la sovversione**: Intercettare ogni fase del processo di sovversione di Krieg, dal discorso sociale al cambiamento politico, per anticipare minacce.
*   **Contrastare la disinformazione**: Applicare la tassonomia [[NATO]]/EU per distinguere misinformation, disinformation e malinformation, e utilizzare tecniche di cross-validation per verificare la verosimiglianza.
*   **Analizzare il framing e i bias**: Riconoscere l'agenda cutting, la tecnica del diversivo e la notizia incartata per identificare manipolazioni narrative e bias di disponibilità.
*   **Rilevare contenuti generati da AI**: L'emergere di deepfake e contenuti sintetici richiede competenze avanzate di deepfake detection, anche in virtù delle normative come l'AI Act 2024.
*   **Valutare l'impatto sul pubblico**: Comprendere i Modelli di Pubblico di Sorre (2011) per prevedere come diverse tipologie di pubblico reagiranno a specifiche tattiche propagandistiche.

## 🔮 Lacune Informative e Prossimi Passi

| Lacuna                                  | Importanza | Come Colmare                                                              |
| :-------------------------------------- | :--------- | :------------------------------------------------------------------------ |
| **Dati empirici sulla propagazione reale** | Alto       | Analisi quantitative di dataset di campagne di influenza documentate      |
| **Efficacia comparata delle tre tipologie** | Alto       | Studio di casi con metriche di impatto misurabili                         |
| **Propaganda 5.0 (AI generativa)**      | Medio      | Monitoraggio deepfake e contenuti sintetici come nuova frontiera          |
| **Impatto dei social media su Mcquail** | Medio      | Analisi di come i social media hanno riscritto le funzioni classiche      |
| **Quadro legislativo UE su propaganda straniera** | Alto       | Monitoraggio dell'applicazione di normative come [[DSA]]/DMA e reporting EUvsdisinfo |

## 🔗 Connessioni e Pattern

- [[Applicazioni osint]]
- [[Foreign Information Manipulation and Interference]]
- [[Funzioni dei media]]
- [[Legge 124-2007]]
- [[Propaganda]]


- [[--]]
F/I/H
- [[--]]
