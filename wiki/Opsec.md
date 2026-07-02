---
title: "Opsec"
tags: ["OSINT", "processed", "opsec", "sicurezza-operativa", "sock-puppet"]
date: "2026-05-15"
status: "draft"
depth: "deep"
sources: "5"
tipo: "concetto"
---

# Opsec

## 🎯 Sintesi Strategica

L'**OPSEC (Operations Security)** è il processo metodologico per identificare e proteggere informazioni apparentemente innocue (non classificate) che, se aggregate da un avversario, svelerebbero l'esistenza, l'identità o gli obiettivi di un'operazione d'Intelligence. Nell'[[Osint]], l'OPSEC è il primo e più critico strato di difesa: un analista che indaga su reti criminali, troll farm statali o forum del [[Dark web]] senza un'adeguata copertura rischia la "contro-profilazione", esponendo se stesso e la propria agenzia/azienda a ritorsioni fisiche, cyber o legali.

## 📚 Contesto e Definizioni

Il ciclo OPSEC (standard militare USA) consta di cinque fasi: Identificare le info critiche, Analizzare le minacce, Analizzare le vulnerabilità, Valutare i rischi, Applicare le contromisure.
Nel contesto digitale, l'avversario estrae dati (Digital Exhaust) dalla postazione dell'investigatore attraverso:
1.  **Indirizzo IP:** Rivela la posizione geografica e l'ISP (spesso riconducibile a enti governativi o aziende note).
2.  **Browser Fingerprinting:** I siti web tracciano la risoluzione dello schermo, i font installati, l'orologio di sistema e la stringa *User-Agent* per creare un ID univoco della macchina dell'analista, indipendentemente dall'uso dei cookie.
3.  **Leak DNS e WebRTC:** Dati che scavalcano le VPN mal configurate svelando l'IP reale.

## 📊 Dati, Tecnologie e Metriche

L'infrastruttura di base (Must-Have OSINT Toolkit) per mitigare questi vettori di rischio prevede:
*   **Macchina Virtuale (VM):** L'analista non opera *mai* dalla macchina Host personale. Si utilizza una VM (es. Virtualbox, VMware) dedicata esclusivamente alle indagini, che può essere resettata a uno stato pulito (*Snapshot*) dopo ogni sessione per distruggere eventuali malware scaricati accidentalmente.
*   **Isolamento di Rete:** L'utilizzo di VPN professionali a livello di router o macchina host. Per la navigazione profonda (SOCMINT / Dark Web), si aggiunge il routing tramite la rete Tor, compartimentando la sessione investigativa da quella privata.

## 🔍 Analisi Operativa ed Applicazioni OSINT

Il pilastro dell'OPSEC investigativa sui Social Network è il **Sock Puppet** (Account Fittizio/Copertura):
*   Un Sock Puppet investigativo non è un semplice "profilo falso". Richiede un invecchiamento (*aging*), una back-story credibile, un numero di telefono virtuale (spesso non VoIP per bypassare i blocchi) e foto generate sinteticamente (o sottratte ma non reversibili).
*   **Compartimentazione rigorosa:** L'analista non deve mai fare log-in con un account personale sulla VM investigativa, né accedere al Sock Puppet dalla propria connessione Wi-Fi domestica non protetta. L'inquinamento incrociato (Cross-Contamination) distrugge la copertura all'istante, permettendo all'avversario (o alle piattaforme stesse, vedi [[Capitalismo delle piattaforme]]) di collegare l'ID fittizio all'ID reale dell'analista.

## 🔮 Lacune Informative e Prossimi Passi

*   **L'Illusione del "Nessun Rischio":** Spesso gli analisti alle prime armi scambiano la Privacy (non farsi tracciare) con l'Anonimato Assoluto. Contro un *Advanced Persistent Threat (APT)* statale, l'OPSEC è solo una mitigazione del rischio, non un mantello dell'invisibilità.
*   **OPSEC nei tool AI:** Inserire stringhe di testo grezzo (es. indirizzi email target o frammenti di codice) in LLM pubblici (es. ChatGPT) equivale a consegnarli al provider. L'OPSEC impone l'uso di modelli in locale (es. LM Studio) per dati investigativi sensibili.

## 🔗 Connessioni e Pattern

- [[Sock puppet]]
- [[Tassonomia dei tools]]
- [[Osint]]
- [[Vulnerabilità llm]]
- [[Cyber]]

- [[--]]
F/I/H
- [[--]]
