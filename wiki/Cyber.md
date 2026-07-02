---
title: "Cyber"
tags: ["OSINT", "processed", "cyber", "threat-intelligence", "vulnerability"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "1"
tipo: "concetto"
---

# Cyber

## 🎯 Sintesi Strategica

Nel perimetro metodologico dell'[[Osint]], il dominio **Cyber** non riguarda l'attacco o la penetrazione attiva di sistemi informatici (attività da Red Team o illegale se non autorizzata), bENSì la **raccolta passiva, l'analisi e la correlazione di tracce digitali** e vulnerabilità esposte pubblicamente. Attraverso la mappatura della superficie d'attacco, la Cyber Threat Intelligence (CTI) e l'intersezione con l'[[Intelligenza artificiale generativa]], l'analista ricostruisce le infrastrutture, identifica gli indicatori di compromissione (IOC) e profila i *Threat Actors* senza mai instaurare un contatto diretto con i server target.

## 📚 Contesto e Definizioni

*   **Cyber Threat Intelligence (CTI):** L'acquisizione e l'analisi di informazioni sulle minacce cibernetiche (Tattiche, Tecniche e Procedure - TTP) per supportare decisioni di mitigazione.
*   **Superficie d'Attacco (Attack Surface):** L'insieme totale delle vulnerabilità e degli endpoint di un'organizzazione (IP esposti, porte aperte, domini dimenticati) visibili dall'esterno.
*   **Indicator of Compromise (IOC):** Firme digitali o artefatti forensi (Hash di file malware, indirizzi IP di server Command & Control, pattern di traffico) che indicano un'infezione o un attacco in corso.

## 📊 Dati, Tecnologie e Metriche

Il workflow dell'OSINT applicato al dominio Cyber si affida a strumenti di scansione dell'infrastruttura di rete globale, i quali scansionano Internet per conto dell'analista:
1.  **[[Shodan (motore di ricerca)]] e CENSys:** I principali motori per la mappatura dell'IoT, server mal configurati e database aperti, che forniscono *banner grabbing* senza toccare direttamente il bersaglio.
2.  **DNS Intelligence:** Strumenti come Securitytrails o DNSdumpster per la risoluzione passiva, l'enumerazione dei sottodomini e l'analisi temporale dei record ([[Passive DNS]]).
3.  **Sandboxing & IOC Analysis:** Virustotal, [[urlscan.io]] o Any.Run per analizzare la reputazione dei file e il comportamento dei link malevoli in ambienti sicuri.

## 🔍 Analisi Operativa ed Applicazioni OSINT

La rivoluzione recente nel campo Cyber-OSINT è determinata dai LLM:
*   **Vulnerabilità LLM:** I modelli generativi non sono solo strumenti di supporto, ma sono diventati vettori d'attacco tramite il *Prompt Injection*, o vengono utilizzati dai cybercriminali per scalare le campagne di phishing personalizzato e per generare codice malevolo elusivo.
*   **Automazione Difensiva:** L'integrazione tra piattaforme low-code come n8n o [[Power Automate]] permette la validazione rapida degli IOC ricevuti su Telegram e l'estrazione automatizzata tramite agenti AI.

## 🔮 Lacune Informative e Prossimi Passi

*   **Attribuzione:** Stabilire con assoluta certezza "chi" ha sferrato un attacco è quasi impossibile tramite la sola analisi tecnica (a causa del *false flag* e dei *proxy*). Spesso l'attribuzione definitiva richiede HUMINT o SIGINT ad altissimo livello.
*   **Frequenza dei dati:** I motori di scansione IoT possono contenere dati vecchi di giorni o settimane, riducendo l'utilità tattica per minacce zero-day dinamiche.

## 🔗 Connessioni e Pattern

- [[Intelligenza artificiale generativa]]
- [[Ip-dns intelligence]]
- [[Tassonomia dei tools]]
- [[Opsec]]
- [[Threat intelligence]]

- [[--]]
F/I/H
- [[--]]
