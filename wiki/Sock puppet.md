---
title: "Sock puppet"
tags: ["OSINT", "processed", "sock-puppet", "opsec", "socmint"]
date: "2026-05-15"
status: "draft"
depth: "deep"
sources: "3"
tipo: "concetto"
---

# Sock puppet

## 🎯 Sintesi Strategica

Il **Sock Puppet** è un'identità digitale fittizia, meticolosamente costruita e mantenuta da un analista [[Osint]] o da un operatore cyber, per condurre indagini coperte sui social network (SOCMINT), nei forum del [[Dark web]] o in comunità chiuse (es. canali Telegram terroristici). A differenza del semplice "account falso" (creato in 5 minuti e facilmente bannabile dagli [[Algoritmi]] anti-bot), il Sock Puppet è un asset operativo ad alto valore che richiede mesi di "invecchiamento" (*Aging*), compartimentazione hardware/software e una solida architettura [[Opsec]] per impedire che il bersaglio o la piattaforma scoprano la vera identità dell'investigatore.

## 📚 Contesto e Definizioni

La costruzione di un Sock Puppet si divide in due macro-fasi:
1.  **Backstory (Il Background):** Creazione di una persona credibile. Nome, età, hobby, città di residenza, simpatie politiche. La backstory non deve mai incrociarsi con le vere passioni dell'analista per evitare bias inconsci (se l'analista ama il tennis, il Sock Puppet non dovrebbe amare il tennis).
2.  **Infrastruttura Tecnica (Il Setup):**
    *   *Rete:* Nessun accesso dal Wi-Fi domestico o aziendale. Si utilizza esclusivamente una rete compartimentata (VPN o rete Tor).
    *   *Browser:* Profilo browser vergine, idealmente all'interno di una Macchina Virtuale (VM) usa-e-getta.
    *   *Biometria visiva:* Mai usare foto reali rubate (verrebbero scoperte tramite [[Fonti osint]] di Reverse Image Search come Pimeyes). Si utilizzano volti generati tramite [[Intelligenza artificiale generativa]] (es. *This Person Does Not Exist*), avendo cura di pulire i metadati (EXIF) prima dell'upload.

## 📊 Dati, Tecnologie e Metriche

Il superamento dei "gatekeeper" algoritmici (CAPTCHA, verifiche SMS) richiede investimenti specifici:
*   **Burner Phones (Telefoni Usa e Getta):** Molte piattaforme bloccano i numeri VoIP (es. Google Voice) durante la registrazione. Serve una SIM fisica anonima dedicata o servizi di SMS verification premium ad alto costo.
*   **Warming Up (Invecchiamento):** Un account appena creato che inizia a seguire 500 profili di terroristi viene banNATO istantaneamente. Il Sock Puppet deve prima seguire pagine normali (cucina, sport), mettere like organici e interagire lentamente per guadagnare un "Trust Score" elevato presso l'algoritmo della piattaforma.

## 🔍 Analisi Operativa ed Applicazioni OSINT

L'utilizzo operativo segue la dottrina del **"Look, but don't touch"** (Guarda ma non toccare):
*   L'interazione attiva (es. inviare messaggi privati al target o provocare in un gruppo) trasforma l'operazione da raccolta passiva OSINT a un'operazione di HUMINT o *Undercover* attiva, richiedendo autorizzazioni legali e mandati specifici, pena l'invalidazione della prova in tribunale ([[Quadro giuridico]]).
*   **Burn Protocol:** Se l'analista sospetta che il Sock Puppet sia stato smascherato o tracciato (es. riceve un link di phishing in privato o una richiesta di amicizia da un account governativo avversario), deve eseguire il "Burn": distruzione immediata dell'account, della VM e della SIM associata.

## 🔮 Lacune Informative e Prossimi Passi

*   **Capitalismo della Sorveglianza:** Come evidenziato in [[Capitalismo delle piattaforme]], aziende come Meta e Google incrociano migliaia di data point (Browser Fingerprinting, pattern di digitazione, co-localizzazione Wi-Fi). Mantenere in vita un Sock Puppet senza essere smascherati dagli algoritmi anti-frode sta diventando un'operazione quasi impossibile per investigatori indipendenti privi di coperture istituzionali (come l'Internet Obfuscation fornita dalle agenzie statali).

## 🔗 Connessioni e Pattern

- [[Opsec]]
- [[Socmint]]
- [[Capitalismo delle piattaforme]]
- [[Quadro giuridico]]
- [[Intelligence digitale]]

- [[--]]
F/I/H
- [[--]]
