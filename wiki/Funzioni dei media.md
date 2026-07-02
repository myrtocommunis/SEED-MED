---
title: Funzioni dei media
tags:
- OSINT
- processed
- funzioni-dei-media
date: '2026-05-15'
status: draft
depth: standard
sources: '1'
tipo: concetto
---

# Funzioni dei media

## 🎯 Sintesi Strategica

La [[Propaganda]] è una persuasione sistematica progettata per modellare percezioni, orientare atteggiamenti e indurre comportamenti in pubblici target. Non è sinonimo di [[Disinformazione]], ma opera all'interno di un ecosistema comunicativo strutturato che include mezzi legittimi e illegittimi, fonti riconoscibili e anonime, narrative mainstream e shadow narrative. Il quadro teorico per l'analisi delle funzioni dei media in questo contesto combina due pilastri complementari:

1.  **La tripartizione classica della propaganda** (bianca, grigia, nera) — una griglia di attribuzione che determina la riconoscibilità della fonte.
2.  **Le quattro funzioni sociali dei media di Mcquail** (informazione, correlazione, continuità, mobilitazione) — un quadro che descrive l'azione dei media nell'ambiente strategico contemporaneo.

L'intersezione di questi modelli genera una matrice operativa di 4×3 = 12 slot, fondamentale per classificare campagne di influenza. A questo si aggiunge il [[Propaganda]] (Manufacturing Consent), che introduce una dimensione strutturale-economica attraverso cinque filtri (ownership, advertising, sourcing, flak, ideology), spiegando *perché* i media comunicano in un certo modo. Dinamiche come il *negativity bias* (contenuti con rabbia ottengono maggiore engagement) e la *Goodhart's Law* (quando una metrica diventa un obiettivo, cessa di essere una buona misura) evidenziano come l'ottimizzazione per l'engagement possa compromettere la qualità dell'informazione, portando a fenomeni come il *churnalism* e il *sensazionalismo*.

## 📚 Contesto e Definizioni

### Definizione Operativa di Propaganda
La propaganda non è mera falsità, ma **organizzazione del discorso**. Comprende:
*   **Selezione:** Cosa è incluso nel racconto pubblico.
*   **Omissione:** Cosa è sistematicamente escluso.
*   **Incadratura (framing):** Come è presentato ciò che è incluso.
*   **Ripetizione:** La meccanica della familiarità che genera accettazione.
*   **Emotional priming:** L'attivazione di bias cognitivi (paura, rabbia, orgoglio) prima della presentazione del contenuto.

La distinzione tra propaganda e manipolazione è cruciale:
*   **Propaganda:** Pianificabile, targettizzata, sistematica (non episodica). Nasce in un contesto competitivo e implica [[Propaganda]].
*   **Manipolazione:** Intenzionale, occulta (il pubblico non è pienamente consapevole). Efficace quando l'emittente ha forte controllo sull'informazione o il pubblico ha scarse risorse sociali di filtro. L'elemento chiave è la credibilità dell'emittente e l'effetto di realtà, dove la percezione di veridicità è più importante della verità oggettiva.

### La Tripartizione Propagandistica

| Tipo | Definizione |
|---|---|
| **Bianca** | Fornisce un'immagine positiva senza inganno, con fonte trasparente (es. comunicazione istituzionale, brand). |
| **Grigia** | Implica occultamento e selettività riguardo la verità, con fonte non pienamente attribuibile o ambigua. |
| **Nera** | Altamente ingannevole, utilizzando materiale distorto ed emotivo, con fonte falsificata o attribuita erroneamente. |

### I Modelli di Pubblico (Sorre, 2011)

Il concetto di "pubblico" è fondamentale per comprendere l'efficacia delle tattiche propagandistiche. Sorre (2011) identifica quattro modelli:
1.  **Massa manipolabile:** Pubblico passivo, facilmente influenzabile (modello ipodermico).
2.  **Pubblico cosciente:** In grado di costruire un'opinione pubblica autonoma.
3.  **Insieme di mercati:** Pubblico targettizzato e RAGgruppato (modello marketing).
4.  **Partner interattivi:** Capaci di avere un controllo sui processi comunicativi (modello partecipativo/democratico).
L'implicazione per l'[[Osint]] è che la tipologia di pubblico determina quali tattiche propagandistiche sono efficaci.

### Le Cinque Funzioni dei Media secondo Mcquail

| Funzione | Definizione | Manifestazione nell'ambiente strategico |
|---|---|---|
| **Informazione** | Trasmettere dati e fatti al pubblico. | Reportage, bollettini, fact-checking; ma anche disinformazione mascherata da informazione. |
| **Correlazione** | Interpretare e dare senso ai fatti. | Editoriali, commento, framing, selezione delle notizie. |
| **Continuità** | Trasmettere valori culturali e norme sociali. | Nazionalismo, memoria collettiva, narrazione identitaria. |
| **Mobilitazione** | Indurre azione collettiva verso un obiettivo. | Campagne di reclutamento, boicottaggi, attivismo coordiNATO, radicalizzazione. |
| **Intrattenimento** | Offrire svago e relax. | Distrazione tramite intrattenimento, una forma efficace di propaganda bianca che tiene le masse occupate senza richiedere sforzo cognitivo. |

## 📊 Dati, Tecnologie e Metriche

### Il Quadro Normativo SISR applicato alla Propaganda
La [[Legge 124-2007]] definisce i limiti entro cui l'analisi propagandistica deve operare in Italia. Essa disciplina il Segreto di Stato (con limiti temporali e divieti su fatti eversivi, terrorismo, mafia), il ruolo del COPASIR (Comitato parlamentare per la sicurezza) nella verifica del rispetto costituzionale delle attività di intelligence, e le garanzie funzionali per gli addetti delle agenzie. L'analista [[Osint]] deve distinguere tra propaganda statale legittima (sovranità), propaganda straniera come minaccia agli interessi nazionali, e propaganda interna come indicatore di instabilità sociale.

### Il Quadro FIMI EU/[[NATO]] per la Propaganda Moderna

La tripartizione classica è integrata dal quadro EU [[Foreign Information Manipulation and Interference]] (Foreign Information Manipulation and Interference) e dalla tassonomia [[NATO]] della disinformazione:

**4 blocchi architetturali FIMI (EU EEAS report):**
| Blocco | Definizione | Attribuzione |
|---|---|---|
| Official state channels | Parlano per conto dello stato (presidente, PM, ambasciate, ministeri, istituti culturali). | Manifesta |
| State-controlled outlets | Media statali o privati con ownership statale (broadcast, siti, social). | Overt |
| State-linked channels | Mascherano affiliazione a stato (think tank fittizi, agenzie stampa private con cliente governativo). | Covert |
| State-aligned channels | Nessuna evidenza diretta di affiliazione ma allineamento sistematico. | Non attribuito |

**Framework [[NATO]]/EU Tassonomia Disinformazione:**
| Categoria | Contenuto | Intento | Esempio Operativo |
|---|---|---|---|
| Misinformation | Falso | Nessun intento dannoso | Cittadino condivide una notizia errata credendola vera. |
| Disinformation | Falso | Intento di danneggiare | Attore statale crea informazioni false per destabilizzare. |
| Malinformation | Vero | Intento di danneggiare | Diffusione di documenti classificati per screditare (es. Snowden). |

**Tipologie di contenuti per gravità:**
1.  SATira/Parodia (basso)
2.  Fuorviante cherry-picking (medio)
3.  Impostore (alto)
4.  Fabbricato (alto)
5.  Ingannante (medio)
6.  Falso (alto)
7.  Manipolato/[[Deepfake]] (alto)
8.  Amplificato (alto)

### Il Processo di Sovversione (Krieg, 2023)

La sovversione è lo sfruttamento strategico delle vulnerabilità sociali, psicologiche, infrastrutturali e fisiche nell'ambiente informativo da parte di un avversario esterno per erodere consenso o status quo sociopolitico. Il processo si articola in:
Discorso social → Discorso media tradizionali e società civile → Discorso rilevante per le politiche tra esperti e decisori → Mobilitazione → **Cambiamento strategico del decisore politico**.
Questo funnel rappresenta il processo che l'analista [[Osint]] deve intercettare e analizzare in ogni sua fase.

### Come i Servizi Usano i Media

Le tecniche documentate di utilizzo dei media da parte dei servizi di intelligence includono:
*   **Affare Dreyfus:** Caso storico di manipolazione mediatica di stato, un pattern ricorrente.
*   **Agenda cutting:** Omissione sistematica di notizie sgradite, che crea un bias di disponibilità nella narrazione pubblica.
*   **ABC della disinformazione:** Framework di classificazione degli effetti della disinformazione.
*   **Principio di verosimiglianza:** La notizia deve suonare plausibile, non necessariamente vera. Il contrasto richiede cross-validation con fonti primarie.
*   **Carattere indiretto dell'operazione:** La notizia proviene da fonti "neutrali", un pattern di attribuzione nella tripartizione grigia.
*   **Tecnica del diversivo (pseudo-eventi):** Creare fatti artificiali per spostare l'attenzione (pattern Distract della metodologia 5D).
*   **Notizia incartata:** La notizia principale è veicolata "tra le righe", un pattern di correlazione deviata.
*   **Contesto vs attenuazione:** Allarmismo o banalizzazione della notizia, misurabile tramite metriche di framing.
*   **Cyber-squatting:** Tecnica di propaganda nera che sfrutta la registrazione di domini simili a quelli ufficiali per diffondere disinformazione.
*   **AI Act 2024:** La normativa europea impone l'etichettatura obbligatoria dei contenuti generati da [[Fondamenti di ai|Intelligenza Artificiale]], inclusi i [[Deepfake]], per contrastare la disinformazione.

## 🔍 Analisi Operativa ed Applicazioni OSINT

L'analisi operativa delle funzioni dei media in ambito [[Osint]] si concentra sulla decodifica e attribuzione delle campagne di influenza. L'analista utilizza la matrice 4x3 (funzioni di Mcquail x tripartizione propagandistica) per classificare le tattiche persuasive. Le applicazioni includono:
*   **Classificazione delle campagne:** Identificare se una campagna è bianca, grigia o nera e quale funzione mediatica (informazione, correlazione, continuità, mobilitazione, intrattenimento) sta cercando di attivare.
*   **Intercettazione del processo di sovversione:** Monitorare ogni fase del funnel di Krieg, dal discorso sui social media alla mobilitazione e al potenziale cambiamento strategico.
*   **Distinzione tra propaganda legittima e minaccia:** Valutare se una campagna rientra nella sfera della sovranità statale o costituisce una minaccia agli interessi nazionali, come definito dalla [[Legge 124-2007]].
*   **Cross-validation e contrasto:** Utilizzare fonti primarie e tecniche di verifica per contrastare il principio di verosimiglianza e identificare notizie incartate o pseudo-eventi.
*   **Attribuzione:** Rilevare il carattere indiretto delle operazioni e l'uso di canali *state-linked* o *state-aligned* secondo il framework [[Foreign Information Manipulation and Interference]].
*   **Monitoraggio delle tecnologie emergenti:** Identificare e analizzare l'uso di [[Deepfake]] e contenuti generati da [[Fondamenti di ai|Intelligenza Artificiale]], anche in relazione alle normative come l'AI Act 2024.

## 🔮 Lacune Informative e Prossimi Passi

| Lacuna | Importanza | Come Colmare |
|---|---|---|
| **Dati empirici sulla propagazione reale** | Alto | Analisi quantitative di dataset di campagne di influenza documentate. |
| **Efficacia comparata delle tre tipologie di propaganda** | Alto | Studio di casi con metriche di impatto misurabili. |
| **Propaganda 5.0 (AI generativa)** | Medio | Monitoraggio di [[Deepfake]] e contenuti sintetici come nuova frontiera. |
| **Impatto dei social media sulle funzioni di Mcquail** | Medio | Analisi di come i social media hanno riscritto le funzioni classiche. |
| **Quadro legislativo UE su propaganda straniera** | Alto | Monitoraggio dell'applicazione di normative come [[DSA]]/DMA e reporting di EUvsdisinfo. |

## 🔗 Connessioni e Pattern

- [[Deepfake]]
- [[Disinformazione]]
- [[Legge 124-2007]]
- [[Osint]]
- [[Propaganda]]


- [[--]]
F/I/H
- [[--]]
