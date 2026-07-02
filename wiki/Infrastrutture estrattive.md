---
title: Infrastrutture estrattive
tags:
- OSINT
- processed
- infrastrutture-estrattive
date: '2026-05-15'
status: draft
depth: standard
sources: '1'
tipo: concetto
---

# Infrastrutture estrattive

## 🎯 Sintesi Strategica

Le **infrastrutture estrattive** si riferiscono ai meccanismi e alle piattaforme digitali che operano all'interno dell'[[Infosfera]] per monetizzare l'attenzione e i dati comportamentali degli utenti. Questo fenomeno è centrale nel [[Capitalismo della sorveglianza]], dove ogni interazione umana online è trasformata in un dato estraibile e valorizzabile. Le piattaforme, anziché produrre contenuti, fungono da intermediari che estraggono valore dai dati degli utenti, alimentando l'Economia dell'attenzione. Per l'analista OSINT, questa realtà presenta una duplice sfida: l'infosfera è il principale campo di indagine, ma la dipendenza da tali piattaforme crea significative vulnerabilità infrastrutturali, compromettendo la capacità investigativa in caso di modifiche algoritmiche, censure o sospensioni di account.

## 📚 Contesto e Definizioni

L'[[Infosfera]], secondo Luciano Floridi, è un ambiente globale ibrido fisico-digitale dove agenti informativi, proprietà, interazioni e processi coesistono senza dicotomia tra reale e virtuale. All'interno di questo spazio, la [[Datificazione]] trasforma ogni azione umana in un dato online, generando un flusso continuo di big data. Questi dati, spesso definiti "grezzi", sono in realtà "preconfezionati" da meccanismi di raccolta specifici e progettati dalle piattaforme stesse.

Il processo di trasformazione dei dati in comprensione segue il DIKW Model (Data → Information → Knowledge → Wisdom). Tuttavia, nello scenario delle piattaforme, il giudizio umano necessario per elevare i dati a conoscenza e saggezza è sempre più delegato ad algoritmi che ottimizzano l'engagement a discapito dell'accuratezza. La presunta "disintermediazione" di internet si è tradotta in una Reintermediazione, dove nuovi e più potenti intermediari digitali controllano i flussi informativi attraverso meccanismi di filtraggio spesso opachi. Questo modello di propagazione si allinea al [[Propaganda]] di Herman & Chomsky, dove i filtri, sebbene primariamente commerciali (orientati all'engagement), producono effetti analoghi sulla selezione e presentazione delle informazioni.

## 📊 Dati, Tecnologie e Metriche

Le piattaforme digitali operano come infrastrutture estrattive attraverso un ciclo continuo di cattura, trasformazione, mercificazione e amplificazione dei dati.

### I 4 Layer dell'Informazione (Floridi) nell'Infosfera e Rischi OSINT

| Layer        | Elemento                 | Trasformazione                       | Filtro Dominante                               | Rischio OSINT                                                               |
| :----------- | :----------------------- | :----------------------------------- | :--------------------------------------------- | :------------------------------------------------------------------------ |
| **Dati**     | Grezzi, non contestualizzati | Raccolta comportamentale automatizzata | Progettazione della piattaforma (data capture)  | I "dati grezzi" sono sempre strutturati e preconfezionati.                 |
| **Informazioni** | Dati contestualizzati    | Associazione significato-contestuale | Algoritmo di correlazione                      | Il contesto è generato per massimizzare l'engagement, non la neutralità. |
| **Conoscenza** | Informazioni strutturate | Pattern recognition, aggregazione    | ML/AI predittivo (profili utente)              | I profili predittivi rendono gli utenti prevedibili e manipolabili.       |
| **Wisdom**   | Conoscenza + giudizio etico-strategico | Decisione consapevole                | Giudizio umano                                 | Raramente presente; la saggezza è sacrificata all'engagement e al profitto. |

### Piattaforme come Infrastrutture Estrattive: Fasi e Impatto OSINT

| Fase di Estrazione | Cosa Accade                                       | Chi Ottiene Valore             | Impatto OSINT                                                               |
| :----------------- | :------------------------------------------------ | :----------------------------- | :-------------------------------------------------------------------------- |
| **Cattura**        | Ogni dato comportamentale viene registrato.       | Piattaforma                    | L'analista OSINT non ha controllo sulla raccolta iniziale.                  |
| **Trasformazione** | Dati grezzi convertiti in profili predittivi.     | Piattaforma + inserzionisti    | I dati sono già interpretati e modellati, influenzando l'analisi.           |
| **Mercificazione** | Vendita di accesso a inserzionisti basata su profili. | Piattaforma                    | L'accesso ai dati è mediato da interessi commerciali.                       |
| **Amplificazione** | Contenuti che generano forte engagement (es. rabbia, paura) vengono potenziati. | Piattaforma                    | Distorsione della visibilità e della rilevanza delle informazioni.          |
| **Dipendenza**     | L'analista perde accesso se la piattaforma decide. | Piattaforma                    | Perdita immediata di capacità investigativa in caso di blocco o sospensione. |

### L'Economia dell'Attenzione: Il Valore delle Interazioni

L'Economia dell'attenzione, teorizzata da [[Herbert Simon]], identifica l'attenzione dell'utente come la vera merce in un ambiente di abbondanza informativa. Ogni interazione, come un "like", si trasforma in valore economico attraverso un processo che include:
1.  Visibilità del contenuto nel feed dell'utente.
2.  Arricchimento delle metriche di engagement del contenuto.
3.  Raccolta di dati aggregati su engagement e caratteristiche demografiche del pubblico.
4.  Utilizzo di questi dati per inserzioni mirate.
Il mercato si basa quindi sull'attenzione concessa a un contenuto online, che diventa la risorsa primaria monetizzata.

## 🔍 Analisi Operativa ed Applicazioni OSINT

Il **Paradosso Simon-Schwartz** evidenzia come l'abbondanza di informazioni porti a una scarsità di attenzione (Simon) e come troppa scelta possa paralizzare l'utente (Schwartz, Paradosso della scelta). Questo meccanismo è sfruttato dal [[Capitalismo della sorveglianza]]: più contenuti generano più paralisi, aumentando la dipendenza dai filtri delle piattaforme. L'entropia dell'overload informativo impedisce una comprensione complessiva, presentando una realtà frammentata.

### Il Caso Facebook vs Australia

Nel febbraio 2021, in risposta a una legge australiana che imponeva il pagamento ai publisher per i contenuti giornalistici, Facebook ha bloccato tutte le notizie in Australia, inclusi servizi essenziali durante la pandemia di COVID-19. Questo evento ha dimostrato il potere delle piattaforme come Custodians of the Internet (Tarleton Gillespie), evidenziando l'asimmetria di potere e il fallimento della self-regulation. La mancanza di una regolamentazione statale completa e l'opacità degli algoritmi e delle policy interne creano un disordine normativo globale.

### Vulnerabilità Infrastrutturale per OSINT

La dipendenza dalle piattaforme digitali introduce significative vulnerabilità strategiche per l'analisi OSINT:
*   **Twitter/X:** La sospensione di account di ricercatori OSINT (come nel [[Bellingcat]]) può comportare la perdita di strumenti e fonti di intelligence cruciali.
*   **Google:** Modifiche agli algoritmi di ricerca possono alterare radicalmente il campo di indagine e la reperibilità delle informazioni.
*   **Tiktok/Youtube:** La rimozione di account o video può eliminare interi repository di contenuti generati dagli utenti (UGC) o fonti video aperte.

Per mitigare queste vulnerabilità, è imperativo per gli analisti OSINT diversificare gli strumenti e le piattaforme, adottando metodologie di **triangolazione multi-piattaforma** e **ricostruzione della filiera informativa** per garantire la credibilità e la resilienza delle analisi.

## 🔮 Lacune Informative e Prossimi Passi

*   **Mancano dati quantitativi** sul volume esatto di dati comportamentali catturati dalle principali piattaforme (es. Facebook, Google, Amazon, Tiktok) su base pro-utente giornaliera. È necessario quantificare il "dato grezzo" estratto.
*   Il caso Facebook vs Australia — Block of News 2021 meriterebbe una verifica approfondita con fonti primarie (legislazione australiana, comunicati ufficiali delle piattaforme, analisi indipendenti) per una comprensione completa.
*   Il riferimento a "Mattia Zunino" nella fonte grezza è isolato e privo di contesto sufficiente; necessita di identificazione e verifica per comprenderne la rilevanza.
*   Non è quantificato il disproporzionamento dei data center a livello globale, in particolare la concentrazione negli USA. È necessario un dato percentuale verificato.
*   La proposta di verifica dei profili social per l'ingresso negli USA non è associata a un documento normativo specifico (es. Executive Order, policy DHS/DOJ). È fondamentale identificare la fonte legislativa.
*   È necessaria una mappatura delle piattaforme alternative e decentralizzate (es. Plausible, Peertube, Mastodon, Nostr) per l'OSINT, utile per la diversificazione strategica e la riduzione della dipendenza dalle infrastrutture estrattive dominanti.

## 🔗 Connessioni e Pattern

- [[Applicazioni osint]]
- [[Datificazione]]
- [[Infosfera]]
- [[Infrastrutture]]
- [[Legislazione]]
- [[Triangolazione]]


- [[--]]
F/I/H
- [[--]]
