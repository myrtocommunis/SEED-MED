---
title: "Critica — Report 'Accordo di pace intralibico entro le scadenze'"
tags: ["#geopolitica", "#influenza"]
date: 2026-09-08
status: "critique"
tipo: "adversarial-review"
target: "30_reports/Un accordo di pace intralibico entro le scadenze e improbabile i binari verosimili sono diluizione o congelamento non soluzione.md"
nota: "Stress-test inline; logica da .claude/agents/adversary.md. Focus: modi di fallimento del forecasting."
---

# Stress-test avversariale — Report "Pace intralibica entro le scadenze"

## 1. Tesi del report (ricostruita)
Un accordo rispettato nelle scadenze è improbabile (~15%); esiti verosimili: diluizione ~45% (base case),
congelamento ~30%, rottura ~15%, spartizione d'élite ~10%; attuazione piena nei tempi ~5-10% (la meno probabile).

## 2. Critical reading — i difetti di forecasting

**🔴 Gli scenari non sono MECE e le probabilità si sommano male**
- 45+30+15+10 = **100**, ma poi si aggiunge "attuazione piena ~5-10%" e si **ammette** che lo Sc.4 "si
  sovrappone parzialmente" allo Sc.1. Quindi il set **non partiziona** lo spazio degli esiti: doppio conteggio
  e residuo incoerente. Un forecast serio deve avere scenari **esaustivi e mutuamente esclusivi** che sommano
  a 100 — qui non accade.

**🔴 Manca la vista esterna (base rate)**
- Le probabilità sono costruite tutte "dall'interno" (i driver attuali). Ma la domanda ha un **tasso base**
  fortissimo: **ogni** accordo ONU libico (Skhirat 2015, LPDF/Ginevra 2021) è stato **firmato e non attuato**;
  le elezioni del dic 2021 sono saltate. Il report *cita* questo ("il decennio non ha mai prodotto") ma **non lo
  usa** per disciplinare i numeri. La vista esterna spingerebbe il **congelamento (Sc.2) come esito modale**
  (≥45-50%), non la diluizione.

**🟠 Il 45% alla "diluizione" ancora sulla firma fresca del 30 ago (recency bias)**
- Trattare il 4+4 appena firmato come prova che "il processo regge" sovrastima lo Sc.1: una firma in Libia ha
  valore predittivo quasi nullo (Skhirat/Ginevra erano firmati anch'essi). La salienza dell'evento recente
  gonfia il base case.

**🟠 "Pace" confusa con "elezioni/soluzione politica"**
- Il titolo dice "pace improbabile", ma il report misura in realtà l'**accordo politico/unificazione**. Esiste
  già una **tregua dal 2020** (pace *negativa* = assenza di guerra maggiore) che **persiste nella maggioranza
  degli scenari** (1, 2, 4). Quindi la formulazione corretta è: *la soluzione politica nei tempi è improbabile;
  la pace-come-non-guerra è invece l'esito più probabile*. Conflating i due **disallinea il titolo dal
  contenuto**.

**🟠 Rischio-shock cumulato forse sottostimato**
- Lo Sc.3 (~15%) mette in un solo secchio driver **indipendenti** (crisi CBL, guerra milizie, successione
  Haftar, spoiler russo). Su **24 mesi**, la probabilità che **almeno uno** detoni è plausibilmente > 15%.

**🟡 Falsa precisione**
- Probabilità al 5% (45/30/15/10) per un giudizio dichiarato **MEDIUM-LOW**: la granularità suggerisce una
  precisione che la confidenza nega. Meglio bande larghe (es. "alta/media/bassa" o range 40-55%).

## 3. Steel-man inversion (controargomento più forte)

> **"Il forecast è troppo elaborato: sulla vista esterna, la previsione più difendibile è banalmente il
> muddle-through/congelamento come esito modale (~50%), perché ogni accordo libico dal 2015 è stato firmato e
> non attuato, e la tregua 2020 garantisce comunque una pace negativa a prescindere dal 4+4. Lo spread a
> quattro scenari con un 45% alla 'diluizione' sovra-legge una firma recente e sotto-pesa il cimitero degli
> accordi precedenti."**

Non ribalta la conclusione di fondo ("soluzione nei tempi improbabile"), ma **sposta il baricentro** da
diluizione a congelamento e **semplifica** il messaggio.

## 4. Gap matrix

| # | Gap | Tipo | Impatto |
|---|-----|------|---------|
| 1 | Scenari non MECE; +"attuazione piena" fuori dal 100%; Sc.4 sovrapposto a Sc.1 | Coerenza probabilistica | **Alto** |
| 2 | Nessuna vista esterna / base rate (Skhirat, Ginevra) usata per pesare | Inside-view bias | **Alto** |
| 3 | 45% alla diluizione ancora sulla firma del 30 ago | Recency/salience bias | Medio-alto |
| 4 | "Pace" (tregua 2020, probabile) confusa con "soluzione" (improbabile) → titolo disallineato | Definizione | Medio-alto |
| 5 | Rischio-shock cumulato su 24 mesi forse > 15% | Sottostima di coda | Medio |
| 6 | Probabilità al 5% con confidenza MEDIUM-LOW | Falsa precisione | Medio |

## 5. Verdetto

**Punteggio: 6/10** (cap 7). Struttura chiara, driver e indicatori falsificabili solidi, onestà sul fatto che
sono stime. Ma **tre difetti di forecasting** pesano: (a) scenari **non-MECE** con probabilità che si
doppio-contano; (b) assenza di **vista esterna/base rate**, che lascia il 45% alla diluizione dove il tasso
storico favorisce il **congelamento**; (c) **conflazione pace/soluzione** che disallinea il titolo (la tregua
2020 rende la "pace negativa" l'esito *più* probabile, non il meno). Correzioni per salire a 7-8: (1) rendere
gli scenari esaustivi ed esclusivi, sommanti a 100, assorbendo Sc.4 in Sc.1; (2) aggiungere una sezione
**base rate** e ripesare (congelamento ≥ diluizione); (3) **disaggregare** "pace negativa" (probabile) da
"soluzione politica nei tempi" (improbabile) già nel titolo/BLUF; (4) bande di probabilità larghe; (5) alzare
il rischio-shock cumulato. La tesi di fondo regge; va **ricalibrata**, non riscritta.
