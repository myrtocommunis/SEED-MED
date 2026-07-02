---
title: Xkeyscore
tags:
- OSINT
- processed
- xkeyscore
date: '2026-05-15'
status: draft
depth: standard
sources: '1'
tipo: concetto
---

# Xkeyscore

## 🎯 Sintesi Strategica

Le rivelazioni di [[Rivelazioni snowden|Edward Snowden]] nel giugno 2013 hanno trasformato la comprensione dell'intelligence digitale, spostando il dibattito da un piano speculativo a uno documentale. In questo contesto, [[Network intelligence]] (DNI) emerge come categoria architetturale per lo sfruttamento e l'analisi delle comunicazioni globali. [[Xkeyscore]] è lo strumento più noto di DNI, un motore di ricerca analitico della NSA che permette l'accesso, il filtraggio e l'archiviazione del traffico internet in tempo reale. Questo paradigma, insieme allo standard [[Ics 206-01]] per la referenziazione OSINT, forma una triade strutturale: raccolta massiva (DNI), analisi a valle (Xkeyscore), e standardizzazione della referenziazione. Per l'[[Osint]], le rivelazioni di Snowden hanno dimostrato che i metodi di raccolta dell'intelligence classica sono applicabili alla rete globale e che strumenti simili sono teoricamente replicabili da attori non statuali con accesso a API commerciali e tecniche di scraping.

## 📚 Contesto e Definizioni

Le pubblicazioni di documenti classificati da parte di [[Rivelazioni snowden|Edward Snowden]] attraverso testate giornalistiche come *[[The Guardian]]* e *[[The Washington Post]]* nel 2013 hanno fornito una base empirica per l'analisi delle architetture di sorveglianza. Questi documenti, in particolare la slide interna NSA `DNI101` (2010), definiscono il [[Network intelligence]] (DNI) come l'espressione che rappresenta l'intelligence di rete digitale, un framework che le agenzie utilizzano per catturare, filtrare e indicizzare il traffico internet globale.

[[Xkeyscore]] è il tool cardine di questa categoria, descritto come un "DNI exploitation system / analytic framework". La sua funzione primaria è eseguire selezioni "strong" (es. email) e "soft" (es. contenuto) su qualsiasi attività internet, inclusi email, social media, navigazione web, upload di file, VoIP e chat. Gli analisti accedono a Xkeyscore tramite un'interfaccia web che consente query federate su un cluster globale di siti.

## 📊 Dati, Tecnologie e Metriche

L'architettura di [[Xkeyscore]], basata su documenti trapelati, è robusta e scalabile. Utilizza uno stack tecnologico prevalentemente open source (Linux Red Hat, Apache, MySQL, NFS, ecc.). Nel 2009, contava oltre 100 siti globali, ciascuno un cluster di server, con una capacità di ingestione superiore a 20 TB al giorno per sito e 1.7 miliardi di comunicazioni giornaliere. La retention del contenuto è di 3-5 giorni (buffer rotante), mentre i metadati sono conservati per 30 giorni. Report interni della NSA del 2012 indicavano 41 miliardi di record Xkeyscore in un mese.

Il sistema si avvale di circa 10.000 "Appids" e "Fingerprints" (nel 2009) per classificare il traffico intercettato. Ogni stream di traffico riceve un AppID (es. `mail/yahoo/login`) e molteplici fingerprints (es. `mail/arabic`). I microplugins in C++ estendono le capacità di analisi per casi complessi, come il rilevamento di botnet P2P. È integrato con le Tailored Access Operations (TAO), permettendo di caricare fingerprint per identificare macchine sfruttate in nazioni target, collegando DNI a Computer Network Exploitation (CNE).

La tabella seguente evidenzia le differenze tra Xkeyscore (DNI) e [[Osint]]:

| Aspetto           | XKEYSCORE (DNI)                               | OSINT (ICS 206-01)                          |
| :---------------- | :-------------------------------------------- | :------------------------------------------ |
| **Accesso**       | Classificato, autorizzato                     | Pubblico, nessun'autorizzazione             |
| **Scope**         | Traffico in transito (backbone tap)           | Contenuto pubblico esistente                |
| **Referenziazione** | Interna NSA (non standardizzata)              | [[Ics 206-01]] (standard IC)                |
| **Soglia legale** | FISA Amendments Act (2008)                | Nessun vincolo specifico                    |
| **Analista**      | Con clearance (oper@ account)                 | Chiunque                                    |

## 🔍 Analisi Operativa ed Applicazioni OSINT

La transizione dal [[Network intelligence]] all'[[Osint]] è un continuum metodologico. Il DNI dimostra che ogni attività online lascia un'impronta indicizzabile. L'analista OSINT, comprendendo i metodi di Xkeyscore, può dedurre che metadati, file caricati e persino metadati di comunicazioni crittografate sono potenzialmente recuperabili tramite API, cache di motori di ricerca o archivi web come la [[Wayback machine]].

I limiti legali della sorveglianza digitale sono stati definiti da sentenze chiave. L'Articolo 8 CEDU è fondamentale per la protezione della privacy. Casi come *Big Brother Watch v. UK* (2021) e *Centrum v. Sverige* (2021) hanno stabilito che la sorveglianza di massa deve avere garanzie adeguate e non può essere indiscriminata. La *Legge 124/2007 Art. 33(9)* in Italia impone limiti sull'utilizzo dei dati acquisiti per la sicurezza nazionale, vincolandone il riuso al principio di finalità e ai controlli parlamentari e del Garante Privacy. Il paradosso normativo è evidente: mentre l'[[Ai act]] esclude la sicurezza nazionale dal suo ambito, la Corte di Giustizia dell'UE ha stabilito che le attività degli ECSPs (Electronic Communications Service Providers) sono soggette al diritto UE anche per la sicurezza nazionale.

L'analista [[Osint]] può replicare i principi concettuali di [[Xkeyscore]] senza la sua infrastruttura:
1.  **Federated query**: Eseguire query unificate su motori di ricerca, archivi web (es. Wayback Machine), API di social media e piattaforme di codice (es. Github).
2.  **Metadata-first**: Archiviare metadati (URL, timestamp, header HTTP) come un "buffer rotante" personale.
3.  **Fingerprint matching**: Classificare il traffico web target con categorie simili a quelle di Xkeyscore (es. `mail/`, `chat/`, `browser/`) ma su fonti aperte.

Le rivelazioni di [[Rivelazioni snowden|Edward Snowden]] costituiscono una fonte primaria di livello A1 per la ricerca [[Osint]], fornendo documentazione diretta sull'architettura della NSA e fungendo da punto di partenza per l'analisi dei programmi di sorveglianza globale.

## 🔮 Lacune Informative e Prossimi Passi

*   **LACUNA 1**: L'architettura e le capacità di [[Xkeyscore]] potrebbero essere state aggiornate significativamente dopo il 2013, specialmente con l'integrazione di tecnologie di [[Fondamenti di ai|Intelligenza Artificiale]] e machine learning.
    *   **Prossimo passo**: Verificare le ultime rivelazioni o documenti congressuali riguardanti l'NSA nel periodo post-Snowden.
*   **LACUNA 2**: La relazione precisa tra lo standard [[Ics 206-01]] (USA) e i framework di referenziazione [[Osint]] europei (es. [[Berkeley Protocol]]) non è stata completamente tracciata.
    *   **Prossimo passo**: Confrontare i due standard sezione per sezione per identificare convergenze e divergenze.
*   **LACUNA 3**: Il ruolo specifico del FISA Amendments Act Section 702 nel contesto della raccolta dati di [[Xkeyscore]] sui non-cittadini statunitensi non è dettagliato.
    *   **Prossimo passo**: Approfondire il quadro giuridico statunitense che autorizza la raccolta di intelligence estera.
*   **LACUNA 4**: Il caso Cambridge Analytica, menzioNATO brevemente, merita un'analisi dedicata come esempio di ponte tra [[Network intelligence]] commerciale e [[Osint]].
    *   **Prossimo passo**: Creare una monade specifica per il caso Cambridge Analytica.

## 🔗 Connessioni e Pattern

- [[Ai act]]
- [[Ics 206-01]]
- [[Intelligence digitale]]
- [[Network intelligence]]
- [[Osint]]


- [[--]]
F/I/H
- [[--]]
