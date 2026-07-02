---
title: "Finint"
tags: ["OSINT", "processed", "finint", "antiriciclaggio", "offshore"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Finint

## 🎯 Sintesi Strategica

La **FININT (Financial Intelligence)** è la branca investigativa dedita alla ricostruzione dei flussi finanziari, all'analisi delle strutture societarie e all'identificazione dei beneficiari economici finali (UBO - *Ultimate Beneficial Owner*). Nell'ecosistema dell'Intelligence moderna, in cui il terrorismo, il cybercrimine o la proliferazione di armi di distruzione di massa richiedono massicci capitali per operare, la FININT segue la regola aurea: **"Follow the Money"** (Segui i soldi). Mentre la [[Blockchain intelligence]] si concentra sul mondo crittografico, la FININT tradizionale naviga nel labirinto del sistema bancario globale e dei registri commerciali aperti (Corporate Registries).

## 📚 Contesto e Definizioni

La finalità di molti Threat Actors (es. Oligarchi russi sotto sanzioni o Cartelli del narcotraffico) è il riciclaggio (Money Laundering): trasformare capitale "sporco" in asset legittimi nel mercato occidentale.
L'indagine OSINT FININT combatte contro:
1.  **Scatole Cinesi (Layering):** Strutture in cui l'Azienda A è posseduta dall'Azienda B, che è posseduta da un Trust C con sede alle Isole Vergini Britanniche. L'obiettivo è dilatare la catena di proprietà all'infinito per stancare l'investigatore o fermarlo ai confini giurisdizionali opachi.
2.  **Prestanome (Strawmen / Nominee Directors):** Individui pagati per figurare come amministratori legali di un'azienda, privi di reale potere decisionale, per schermare il vero titolare effettivo.

## 📊 Dati, Tecnologie e Metriche

L'arsenale tecnico dell'analista FININT OSINT si basa sull'interrogazione aggressiva (spesso tramite [[Automazione]]) di banche dati:
*   **Registri Camerali Pubblici:** (es. Companies House in UK, Registro delle Imprese in Italia). Permettono di estrarre bilanci, visure, composizioni dei consigli d'amministrazione e modifiche statutarie.
*   **Offshore Leaks Database (ICIJ):** La fuga di documenti epocale (Panama Papers, PanDORA Papers) che ha svelato l'architettura dei paradisi fiscali. Sebbene siano documenti sottratti, la loro pubblicazione da parte dei giornalisti investigativi li ha resi a tutti gli effetti fonti OSINT primarie per mappare ricchezze occulte.
*   **Sanctions Lists:** Database aperti come la lista OFAC (USA), cruciali per il tracciamento di individui inseriti in liste di sanzioni per terrorismo o gravi violazioni del diritto internazionale.

## 🔍 Analisi Operativa ed Applicazioni OSINT

L'elaborazione delle indagini FININT si risolve quasi sempre nell'applicazione della **[[Social network analysis]]**:
*   Attraverso software di Link Analysis (es. Maltego), l'analista importa migliaia di visure camerali e chiede all'algoritmo di collegare i Direttori in comune tra centinaia di aziende.
*   L'individuazione di pattern come un singolo indirizzo fisico (es. un ufficio vuoto a Cipro) registrato come sede legale per 4.000 aziende diverse è un fortissimo *Red Flag* (indicatore di anomalia) di attività di riciclaggio o società di comodo (Shell Companies).

## 🔮 Lacune Informative e Prossimi Passi

*   **Accessibilità a Pagamento:** L'OSINT finanziario spesso cade nella "Grey Information". Registri di nazioni chiave (come la Svizzera o alcuni stati USA come il Delaware) richiedono pagamenti per ogni singola visura, rendendo il monitoraggio di massa automatizzato estremamente costoso senza licenze governative (es. Orbis di Bureau van Dijk).
*   **Trasparenza in Ritirata:** Recenti sentenze della Corte di Giustizia Europea hanno limitato l'accesso pubblico ai registri dei Titolari Effettivi, invocando il diritto alla privacy dei direttori e ostacolando oggettivamente il lavoro dei giornalisti investigativi e della società civile.

## 🔗 Connessioni e Pattern

- [[Osint]]
- [[Blockchain intelligence]]
- [[Social network analysis]]
- [[Fonti osint]]

- [[--]]
F/I/H
- [[--]]
