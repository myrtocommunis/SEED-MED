---
title: I 12 news values
tags:
- OSINT
- processed
- i-12-news-values
date: '2026-05-15'
status: draft
depth: standard
sources: '1'
tipo: concetto
---

# I 12 news values

## 🎯 Sintesi Strategica

Il panorama informativo globale è in transizione dal [[Dal gatekeeping al gatewatching|Gatekeeping]] editoriale, basato su filtri umani gerarchici, al [[Dal gatekeeping al gatewatching|Gatewatching]] algoritmico, dove la visibilità dei contenuti è determinata dall'engagement su piattaforme digitali. Questa evoluzione non ha elimiNATO i filtri, ma li ha resi più opachi e orientati commercialmente. Per l'analista OSINT, ciò implica una filiera informativa frammentata e iper-compressa: eventi critici generano rapidamente un'ondata di contenuti non verificati, che solo in un secondo momento vengono filtrati e contestualizzati. La ricostruzione di questa filiera – identificando chi ha origiNATO, verificato e amplificato un'informazione – è un compito fondamentale. I **12 news values di Galtung & Ruge** (1965) rimangono uno strumento interpretativo cruciale per comprendere come i media influenzino non *cosa* pensare, ma *su cosa* pensare. Applicati a scenari geopolitici, essi rivelano come fattori quali la Proximity culturale, il bias delle élite e il framing narrativo determinino asimmetrie nella percezione pubblica e nelle pressioni politiche. Il gatewatching amplifica queste distorsioni, favorendo contenuti che generano rabbia e polarizzazione. L'OSINT moderno deve quindi diagnosticare il Bias di visibilità, identificando quali verità rimangono invisibili non per mancanza di dati, ma per assenza di news value nella cornice culturale dominante.

## 📚 Contesto e Definizioni

Il **[[Dal gatekeeping al gatewatching|Gatekeeping]]**, concetto introdotto da David Manning White nel 1950, descrive il processo attraverso cui giornalisti e redazioni selezionano le notizie da un vasto flusso di informazioni, agendo come "custodi del cancello" attraverso filtri editoriali gerarchici. I media tradizionali hanno storicamente mantenuto questo principio di selezione umana come cardine della loro operatività.

Il **[[Dal gatekeeping al gatewatching|Gatewatching]]**, teorizzato da Axel Bruns (2005-2018), rappresenta un'inversione di questa logica. Non si tratta più di decidere *cosa pubblicare*, ma di *cosa segnalare*. Il ruolo del giornalista si evolve verso quello di curatore di flussi informativi continui, monitorando e rilanciando contenuti generati dagli utenti o da altre fonti online. L'avvento della [[Datificazione]] (Shoshana Zuboff) e la premessa che "ogni utente è un editore" hanno trasformato il panorama, ma hanno anche introdotto una reintermediazione opaca, dove i passaggi intermedi nella diffusione delle notizie sono meno visibili.

L'[[Infosfera]] di Luciano Floridi descrive uno spazio ibrido fisico-digitale in cui tutti i livelli dell'informazione (dati, informazioni, conoscenza, saggezza) coesistono. In questo contesto, il filtro non è più solo editoriale, ma anche algoritmico-economico. L'Economia dell'attenzione ([[Herbert Simon]], 1971) premia contenuti che generano forte engagement emotivo (rabbia, paura, indignazione), spesso a discapito dell'accuratezza. Questo porta a un'Entropia informativa, dove la verità si frammenta e l'analista deve ricostruire l'intera filiera per ottenere una comprensione completa.

## 📊 Dati, Tecnologie e Metriche

### Tabella MECE: Gatekeeping vs Gatewatching

| Elemento | Gatekeeping | Gatewatching |
|---|---|---|
| **Chi opera** | Giornalisti, redazioni, media tradizionali | Utenti online, community, citizen journalism |
| **Funzione** | Filtrare, selezionare, decidere cosa diventa notizia | Monitorare, rilanciare, commentare informazioni esistenti |
| **Modello** | Verticale (top-down) | Orizzontale (bottom-up) |
| **Controllo qualità** | Alto (standard editoriali, verifica) | Basso/variabile (dipende dall'utente) |
| **Velocità** | Più lenta, mediata | Rapidissima, in tempo reale |
| **Rischi** | Bias redazionali, esclusione di notizie | Disinformazione, contenuti non verificati |
| **Ruolo nel digitale** | Indebolito | Dominante |
| **Esempio** | Un giornale decide di pubblicare o ignorare una notizia | Su X/Twitter un video viene rilanciato da migliaia di utenti |

### I 12 News Values di Galtung & Ruge (1965)

| # | News Value | Definizione | Effetto OSINT |
|---|---|---|---|
| 1 | Frequenza | Quanto spesso una notizia emerge | Notizie ad alta frequenza SATurano la percezione, occultando altri eventi. |
| 2 | Threshold | Intensità/ampiezza dell'evento | Solo eventi di "grande" portata superano la soglia di attenzione, generando distorsione. |
| 3 | Unambiguity | Chiarezza interpretativa | Eventi ambigui o complessi tendono a rimanere invisibili o a essere semplificati eccessivamente. |
| 4 | Meaningfulness | Rilevanza culturale (prossimità/similarità) | **Distorsione geografica sistematica**: eventi in aree culturalmente o geograficamente vicine ricevono maggiore copertura. |
| 5 | Consonance | Conferma delle aspettative | Notizie che confermano narrazioni preesistenti o stereotipi tendono a essere privilegiate e auto-rafforzate. |
| 6 | Unexpectedness | Elemento sorpresa | Eventi inattesi o contro-intuitivi hanno maggiori probabilità di superare la soglia di attenzione. |
| 7 | Continuity | Se già notizia, continua ad esserlo | Una volta che un evento è diventato notizia, tende a mantenere la sua rilevanza informativa (path dependency). |
| 8 | Composition | Varietà del notiziario | La necessità di bilanciare il notiziario può limitare lo spazio per alcuni temi, comprimendo la copertura. |
| 9 | Elite nations | Coinvolgimento di "paesi importanti" | **Distorsione geopolitica**: eventi che coinvolgono nazioni percepite come influenti ricevono maggiore attenzione, rendendo invisibili quelli in paesi periferici. |
| 10 | Elite people | Presenza di persone di potere | La personalizzazione di eventi complessi attraverso figure di spicco o leader politici. |
| 11 | Personalization | Riducibile a storie individuali | La tendenza a raccontare eventi complessi attraverso narrazioni umane e storie individuali, rendendoli più accessibili. |
| 12 | Negativity | Notizie negative privilegiate | **Bias sistemico** verso minacce, crisi, conflitti e problemi, che generano maggiore engagement. |

## 🔍 Analisi Operativa ed Applicazioni OSINT

### La Frammentazione della Filiera Informativa: Il Caso del Sisma Turchia-Siria

Il terremoto in Turchia e Siria ha evidenziato un ciclo informativo a quattro fasi, divenuto standard per le crisi geopolitiche contemporanee:
1.  **Fase 1 – Eruzioni di Contenuti Generati dagli Utenti (UGC) non verificati:** Video e testimonianze dirette da cittadini emergono in tempo reale su piattaforme come Twitter/X e Tiktok, senza alcun filtro o verifica iniziale.
2.  **Fase 2 – Verifica indipendente:** Organizzazioni come la Syria Civil Defense o gruppi di [[Osint]] come [[Bellingcat]] iniziano a verificare le informazioni open-source, fornendo un primo strato di credibilità.
3.  **Fase 3 – Contestualizzazione da parte dei media tradizionali:** Media come Al Jazeera, Guardian o CNN riprendono i contenuti verificati, integrandoli con il proprio reporting e analisi.
4.  **Fase 4 – Amplificazione algoritmica:** Gli algoritmi delle piattaforme determinano la visibilità dei contenuti basandosi sull'engagement, non sull'accuratezza. L'overload informativo rende la selezione algoritmica predominante rispetto alle capacità cognitive umane.
**Implicazione OSINT:** Non è più sufficiente affidarsi a una singola fonte. La ricostruzione della filiera informativa – *chi ha visto per primo, chi ha verificato, chi ha amplificato* – è essenziale per qualsiasi analisi credibile.

### Il Bias dei News Values: Yemen vs Ucraina

I media influenzano *su cosa* pensare, non *come* pensare. La disparità nella copertura mediatica tra il conflitto in Yemen e quello in Ucraina è un esempio lampante, spiegabile attraverso i news values di Galtung & Ruge:
*   **Meaningfulness:** L'Ucraina, in Europa, gode di maggiore Proximity culturale e quindi di un più alto news value rispetto allo Yemen, percepito come "Medio Oriente periferico".
*   **Elite nations:** Il coinvolgimento di potenze come Russia e [[NATO]] eleva automaticamente il news value del conflitto ucraino, mentre la guerra in Yemen, senza grandi potenze direttamente coinvolte, riceve meno attenzione.
Questo genera un Bias di visibilità asimmetrico: non si tratta di una mancanza di informazioni sullo Yemen, ma di una carenza di news value nella cornice culturale dominante. Lo stesso principio si applica a molte altre crisi "low-salience", dove il bias risiede nella struttura dell'attenzione piuttosto che nel contenuto stesso.

### Gatewatching in Contesti Bellici: La Dittatura della Viralità

Nel contesto bellico contemporaneo, il [[Dal gatekeeping al gatewatching|Gatewatching]] produce un ambiente in cui:
*   Utenti rilanciano video non verificati.
*   Immagini manipolate, anche tramite IA, si diffondono rapidamente.
*   Account anonimi amplificano narrazioni pro o contro specifiche fazioni.
*   Bot e troll che deviano l'attenzione su aspetti specifici.
Le informazioni vengono amplificate senza filtro e diventano virali in pochi minuti. Sebbene le istituzioni (es. Ministeri della Difesa) cerchino di controllare la comunicazione su eventi come bombardamenti o vittime civili, il gatewatching può superare qualsiasi strategia di comunicazione ufficiale in poche ore.

### Il Bias di Visibilità e le Routine Produttive (Stuart Hall, Cultural Studies)

Come evidenziato dagli Cultural Studies di Stuart Hall, l'effetto manipolatorio della notizia non risiede solo nei contenuti, ma anche nelle Routine produttive e nelle dinamiche sottostanti:
1.  **Routine produttive:** Le prassi editoriali e le consuetudini professionali strutturano ciò che viene considerato "notizia".
2.  **Strutture cognitive:** Schemi interpretativi condivisi da produttori e lettori fungono da filtro cognitivo.
3.  **Ideologie implicite:** Il bias delle élite è spesso strutturale e non accidentale.
4.  **Dinamiche di mercato:** Il profitto e l'Economia dell'attenzione guidano la selezione delle notizie, non necessariamente la ricerca della verità.
5.  **Rappresentazione politica:** Chi detiene il potere spesso definisce i confini di ciò che è "pensabile" o degno di attenzione.

## 🔮 Lacune Informative e Prossimi Passi

*   **Dati quantitativi comparativi:** Mancano dati quantitativi specifici sulla differenza di copertura mediatica tra conflitti come Yemen e Ucraina (es. numero di articoli, posizionamento, tempistiche) per quantificare empiricamente il Bias di visibilità.
*   **Validazione empirica dei news values:** Non esistono test empirici recenti che applichino sistematicamente i 12 news values di Galtung & Ruge a set di dati mediatici contemporanei per verificarne la validità e l'applicabilità nell'era digitale.
*   **Caso Facebook vs Australia (2021):** L'episodio del blocco delle notizie da parte di Facebook in Australia nel febbraio 2021, citato come esempio di asimmetria di potere, merita un'analisi dedicata che ne esplori il timing e gli effetti sulla sicurezza pubblica e l'accesso all'informazione.
*   **Evoluzione di X/Twitter post-acquisizione Musk (2022-2026):** La nota fa riferimento a "Twitter Moments" come esempio di gatewatching; è necessario aggiornare l'analisi considerando i cambiamenti algoritmici e di policy avvenuti dopo l'acquisizione da parte di Elon Musk.
*   **Implicazioni per l'OSINT italiano/europeo:** È opportuno mappare la specifica dipendenza dei ricercatori OSINT italiani ed europei da piattaforme come X/Twitter e identificare alternative operative o strategie di mitigazione dei rischi associati.

## 🔗 Connessioni e Pattern

- [[Applicazioni osint]]
- [[Datificazione]]
- [[Disinformazione]]
- [[Geopolitica]]
- [[Infosfera]]
- [[Piattaforme]]


- [[--]]
F/I/H
- [[--]]
