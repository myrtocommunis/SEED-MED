---
title: Regimi di verità
tags:
- OSINT
- processed
- regimi-di-verità
date: '2026-05-15'
status: draft
depth: standard
sources: '1'
tipo: concetto
---

# Regimi di verità

## 🎯 Sintesi Strategica

I "Regimi di verità" rappresentano un framework analitico, ispirato al concetto di potere epistemico di Michel Foucault, per comprendere come l'ordine informativo venga definito e chi detenga l'autorità per etichettare determinati contenuti come "disordine". Questo approccio supera i limiti delle tassonomie tradizionali, come quella di Wardle & Derakhshan, che distinguono tra misinformazione, [[Disinformazione]] e malinformazione basandosi sull'intento. In contesti di [[Osint]] puro, la verifica dell'intento è spesso impraticabile, rendendo la classificazione più politica che tecnica. L'analisi dei regimi di verità si concentra sull'impatto misurabile dei contenuti e sulle dinamiche di potere che modellano la percezione della realtà informativa.

## 📚 Contesto e Definizioni

Il concetto di "Regimi di verità" si inserisce in un quadro teorico che analizza la produzione e la circolazione delle informazioni, in particolare nel contesto della cosiddetta "information disorder".

### Tassonomia Wardle & Derakhshan (2017)

Questa classificazione, adottata da enti come la Commissione Europea e [[NATO]] Stratcom, distingue tre tipologie di "information disorder":
*   **Misinformazione**: Contenuto falso, diffuso senza intento dannoso (es. un individuo che condivide una notizia errata credendola vera).
*   **Disinformazione**: Contenuto falso, creato e diffuso con intento dannoso (es. un attore statale che elabora una narrativa falsa per destabilizzare).
*   **Malinformazione**: Contenuto vero, ma diffuso con intento dannoso (es. la divulgazione di documenti classificati per screditare un'istituzione).

### Tassonomia Wardle (7 sottotipi per gravità)

Una classificazione più granulare identifica sette sottotipi di "information disorder", ordinati per gravità:
1.  SATira o parodia.
2.  Contenuto fuorviante (selezione selettiva di dati reali).
3.  Connessione ingannevole (titolo non corrispondente al contenuto).
4.  Contenuto impostore (impersonificazione di una fonte fidata).
5.  Contesto falso (contenuto reale inserito in un contesto ingannevole).
6.  Contenuto fabbricato (interamente falso).
7.  Contenuto manipolato (alterazioni come [[Deepfake]] o media sintetici).
I tipi 4 e 7 sono considerati di massima priorità per l'intelligence, richiedendo spesso competenze forensi.

### Il Disinformation Order (Farkas & Schou, 2020)

Questo approccio concettualizza la [[Disinformazione]] non come un'aberrazione, ma come una **caratteristica sistemica** del [[Capitalismo delle piattaforme]]. Secondo Farkas e Schou, la disinformazione:
*   Opera *attraverso* gli algoritmi delle piattaforme, non contro di essi.
*   È profittevole per le piattaforme, generando engagement e revenue.
*   È prevedibile e strutturale, sfruttando le regole esistenti piuttosto che violarle.

## 📊 Dati, Tecnologie e Metriche

L'analisi dei regimi di verità richiede un approccio pragmatico alla classificazione dei contenuti, specialmente in [[Osint]], dove l'intento è difficilmente accertabile.

| Classificazione (Wardle) | Esempio Operativo | Priorità OSINT |
| :----------------------- | :---------------- | :------------- |
| SATira/parodia           | Non prioritizzare | Basso          |
| Contenuto fuorviante     | Monitorare        | Medio          |
| Connessione ingannevole  | Monitorare        | Medio          |
| Contenuto impostore      | Prioritizzare     | Alto           |
| Contesto falso           | Prioritizzare     | Alto           |
| Contenuto fabbricato     | Massima priorità  | Alto           |
| Contenuto manipolato     | Massima priorità (forensics) | Alto |

**Caso Snowden (2013)**: La vicenda di [[Edward Snowden]] illustra come la stessa evidenza possa essere classificata diversamente a seconda del regime di verità dominante e del posizionamento politico dell'analista:
*   **US Intelligence Community**: Malinformazione (vero ma dannoso per la sicurezza nazionale).
*   **Attivisti per le libertà civili**: Whistleblowing (nell'interesse pubblico).
*   **Analisti**: Possibile operazione di intelligence straniera (per il tempismo della fuga in Russia).

## 🔍 Analisi Operativa ed Applicazioni OSINT

In [[Osint]], la sfida principale è la verifica dell'intento, che spesso richiede [[Humint]] o [[Sigint]]. Senza queste fonti, la distinzione tra [[Disinformazione]] e misinformazione può diventare una questione politica. La soluzione operativa proposta è focalizzarsi sull'**impatto misurabile** piuttosto che sull'intento inferito. Questo implica:
*   Tracciare la diffusione dei contenuti (non la loro genesi).
*   Mappare le reti di amplificazione (non le motivazioni degli attori).
*   Quantificare l'impatto e la risonanza (non giudicare l'intento).

### Il Potere Epistemico e il "Lexicon of Lies" (Jack, 2017)

Il linguaggio stesso è uno strumento di potere. Il "Lexicon of Lies" evidenzia come la nomenclatura sia un'arma nel dibattito pubblico:
*   "[[Propaganda]]" è spesso un termine riservato alle comunicazioni del nemico, mentre le proprie sono definite "informazione" o "diplomazia pubblica".
*   Esempi storici includono la "propaganda sovietica" contrapposta alla "US public diplomacy" durante la [[Guerra Fredda]], o l'uso di "fake news media" da parte di Donald Trump per delegittimare la stampa.
*   In contesti autoritari, termini come "agenti stranieri" (Putin) o "rumours" (Xi) sono usati per delegittimare il dissenso.
**Insegnamento operativo**: Prima di classificare un contenuto, è cruciale chiedersi: *chi sta usando questa parola, con quale autorità, e quale interesse ne deriva?*

### Mappatura del Campo Informativo Italiano (Bourdieu)

L'analisi del campo informativo italiano, attraverso la lente di Pierre Bourdieu, rivela dinamiche complesse tra attori con diversi capitali e strategie:

| Posizione                  | Capitale                  | Strategie                               | Esempi                      | Threat |
| :------------------------- | :------------------------ | :-------------------------------------- | :-------------------------- | :----- |
| Dominanti                  | Economico + Simbolico     | Agenda-setting, gatekeeping             | RAI, Corriere, Repubblica   | Basso  |
| Sfidenti istituzionali     | Politico + Sociale        | Bypass media, social diretto            | Meloni, Salvini, Conte      | Medio  |
| Aspiranti                  | Culturale                 | Investigazione, esposizione             | Il Fatto, Fanpage           | Basso-Medio |
| Marginali                  | Sociale (tight community) | Viralità estrema, provocazione          | Telegram no-vax, blog sovranisti | Alto |

**Insight operativo chiave**: Partiti come Lega e Fratelli d'Italia, pur essendo dominanti politicamente, agiscono spesso come sfidanti mediaticamente. Questa dualità spiega le loro strategie comunicative "antisistema", che mirano a bypassare i media tradizionali per comunicare direttamente con le proprie basi.

## 🔮 Lacune Informative e Prossimi Passi

1.  **Dati quantitativi sulla tassonomia**: Mancanza di un dataset sistematico di contenuti italiani classificati secondo la tassonomia Wardle, con validazione inter-coder.
2.  **Status post-2024 dei proxy russi**: Necessità di fonti aggiornate (leak o report investigativi) per verificare lo stato delle operazioni di influenza russa, non verificabile tramite fonti pubbliche.
3.  **Cross-validation frameworks**: La tassonomia Wardle, sebbene ampiamente adottata, necessita di validazione empirica su ecosistemi informativi non anglofoni.
4.  **Enforcement del [[Diritto digitale|Dsa]]**: Monitoraggio dell'applicazione del Digital Services Act (Reg. UE 2022/2065) e delle sue implicazioni, come le sanzioni pecuniarie per le piattaforme.

## 🔗 Connessioni e Pattern

- [[Capitalismo delle piattaforme]]
- [[Deepfake]]
- [[Disinformazione]]
- [[Osint]]
- [[Propaganda]]


- [[--]]
F/I/H
- [[--]]
