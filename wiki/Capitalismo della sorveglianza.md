---
title: Capitalismo della sorveglianza
tags:
- OSINT
- processed
- capitalismo-della-sorveglianza
date: '2026-05-15'
status: draft
depth: standard
sources: '3'
tipo: concetto
---

# Capitalismo della sorveglianza

## 🎯 Sintesi Strategica

Il [[Capitalismo della sorveglianza]], concetto elaborato da Shoshana Zuboff, descrive un nuovo ordine economico in cui l'esperienza umana è trasformata in dati comportamentali, i quali vengono poi monetizzati. In questo paradigma, ogni azione, emozione o interazione online diventa un "surveillance asset" estraibile e commerciabile. Le piattaforme digitali non si limitano a produrre contenuti, ma operano come infrastrutture estrattive che catturano, trasformano e vendono l'accesso a profili predittivi degli utenti a inserzionisti e altri attori. Questo modello si fonda sull'Economia dell'attenzione, dove la scarsità di attenzione in un ambiente di sovraccarico informativo (il Paradosso della scelta di Schwartz) viene sfruttata per massimizzare l'engagement e, di conseguenza, la raccolta dati. Per l'analista [[Osint]], questa realtà presenta una duplice sfida: se da un lato l'[[Infosfera]] è il principale campo di indagine, dall'altro la dipendenza da queste piattaforme crea significative Vulnerabilità infrastrutturale, potendo compromettere la capacità investigativa in caso di modifiche algoritmiche, censure o sospensioni di account.

## 📚 Contesto e Definizioni

Il [[Capitalismo della sorveglianza]] si radica nell'[[Infosfera]], l'ambiente globale ibrido fisico-digitale teorizzato da Luciano Floridi, dove le dicotomie reale/virtuale e umano/macchina si dissolvono. All'interno di questa infosfera, la [[Datificazione]] è il processo attraverso cui ogni comportamento umano viene tradotto in un dato online, generando un flusso continuo di [[Big data 5v|Big data]]. Questi dati, lungi dall'essere "grezzi", sono sempre strutturati dai meccanismi di raccolta delle piattaforme.

Il modello di business sottostante è il [[Capitalismo delle piattaforme]] (Srnicek), dove servizi apparentemente "gratuiti" attraggono utenti per catturare i loro dati comportamentali. Questi dati vengono poi trasformati in profili predittivi e venduti a terzi. A differenza dei media tradizionali che producono contenuti, le piattaforme estraggono valore dai dati degli utenti.

Il processo di trasformazione dei dati segue idealmente il DIKW Model (Data → Information → Knowledge → Wisdom), ma nel contesto del capitalismo della sorveglianza, il processo si ferma spesso ai livelli di dati e informazioni, poiché la "wisdom" richiede un giudizio etico e strategico umano che le piattaforme non hanno né cercano, privilegiando l'ottimizzazione dell'engagement. Questo porta a una Reintermediazione, dove la promessa di disintermediazione di internet si è tradotta nella creazione di intermediari più potenti e opachi.

## 📊 Dati, Tecnologie e Metriche

Le piattaforme operano come infrastrutture estrattive attraverso diverse fasi:
1.  **Cattura**: Ogni dato comportamentale (click, visualizzazione, tempo di permanenza, interazione) viene registrato automaticamente.
2.  **Trasformazione**: I dati vengono elaborati e correlati per creare profili predittivi dettagliati, rendendo gli utenti "interpretabili e prevedibili".
3.  **Mercificazione**: L'accesso a questi profili e alle capacità di targeting viene venduto a inserzionisti e altri attori.
4.  **Amplificazione**: Gli algoritmi sono progettati per massimizzare l'engagement, amplificando contenuti che generano reazioni emotive intense (es. rabbia, paura, indignazione morale) a scapito di informazioni accurate ma meno coinvolgenti, della complessità e delle posizioni moderate.
5.  **Dipendenza**: Gli utenti e gli analisti diventano dipendenti dall'infrastruttura della piattaforma per l'accesso all'informazione.

L'Economia dell'attenzione quantifica il valore di ogni interazione: un "like" o una condivisione non è solo un'espressione di gradimento, ma un dato che arricchisce le metriche di engagement, alimenta i profili utente e contribuisce alla creazione di inserzioni mirate, chiudendo il cerchio del profitto.

## 🔍 Analisi Operativa ed Applicazioni OSINT

Il [[Capitalismo della sorveglianza]] impone sfide significative all'analisi [[Osint]]. L'Information Overload, combiNATO con il Paradosso della scelta, porta a una paralisi decisionale e a una dipendenza dai filtri algoritmici delle piattaforme. Questo genera un'entropia informativa dove nessuna piattaforma offre una verità completa, ma solo una frammentazione della realtà.

Il caso Facebook vs Australia del febbraio 2021 ha dimostrato la Vulnerabilità infrastrutturale e l'asimmetria di potere: in risposta a una legge che imponeva il pagamento per i contenuti giornalistici, Facebook ha bloccato tutte le notizie in Australia, inclusi servizi essenziali e informazioni sanitarie durante la pandemia. Questo evento ha evidenziato come le piattaforme siano di fatto Custodians of the Internet (Gillespie), con un potere di blocco totale che supera la giurisdizione degli stati sovrani. La Self-regulation è fallita, e la State regulation è spesso incompleta o troppo lenta.

Per l'analista OSINT, la dipendenza da singole piattaforme crea vulnerabilità strategiche:
*   **Twitter/X**: La sospensione di account di ricercatori (come accaduto a [[Bellingcat]]) può causare la perdita di strumenti di intelligence cruciali.
*   **Google**: Modifiche non divulgate agli algoritmi possono alterare radicalmente il campo di indagine e la visibilità delle informazioni.
*   **Tiktok/Youtube**: La rimozione di account o video può eliminare interi repository di contenuti generati dagli utenti (UGC) o fonti video aperte.

La strategia operativa per mitigare questi rischi include la Diversificazione delle fonti e la [[Triangolazione]]. È imperativo ricostruire la Filiera informativa e analizzare gli incentivi ("Cui bono") e la proprietà delle fonti per contrastare il [[Algoritmi]] e la monocultura informativa.

## 🔮 Lacune Informative e Prossimi Passi

*   **Dati quantitativi**: Mancano dati precisi e verificabili sul volume esatto di dati comportamentali catturati dalle principali piattaforme (es. Google, Meta, Amazon, Tiktok) su base pro-utente o aggregata.
*   **Verifica fonti primarie**: Il caso Facebook vs Australia meriterebbe un'analisi più approfondita basata su fonti dirette (documenti legislativi, comunicazioni ufficiali delle piattaforme, analisi indipendenti) per quantificare l'impatto e le implicazioni legali.
*   **Mappatura alternative OSINT**: È necessaria una mappatura aggiornata delle piattaforme alternative e decentralizzate (es. Plausible, Peertube, Mastodon, Nostr) che possano offrire maggiore resilienza e diversificazione per l'analisi OSINT, riducendo la Vulnerabilità infrastrutturale.
*   **Impatto normativo**: Identificare e analizzare documenti normativi specifici (es. leggi, executive orders) relativi a proposte di verifica dei profili social per l'ingresso in paesi specifici, per comprendere le implicazioni sulla privacy e sull'accesso alle informazioni.
*   **Dati sulla concentrazione infrastrutturale**: Quantificare con precisione la concentrazione geografica dei data center e delle infrastrutture chiave che supportano il capitalismo della sorveglianza.

## 🔗 Connessioni e Pattern

- [[Big data 5v|Big data]]
- [[Datificazione]]
- [[Infosfera]]
- [[Osint]]


- [[--]]
F/I/H
- [[--]]
