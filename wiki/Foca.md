---
title: "Foca"
tags: ["OSINT", "processed", "foca", "metadati", "forensics"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Foca

## 🎯 Sintesi Strategica

**FOCA (Fingerprinting Organizations with Collected Archives)** è uno strumento open-source storico e fondamentale nell'arsenale [[Osint]] e dell'Ethical Hacking. La sua specialità è l'estrazione e l'analisi massiva dei [[Metadati]] nascosti all'interno dei documenti pubblici (PDF, Microsoft Office, Openoffice) ospitati sul dominio web di un'organizzazione bersaglio. Lo scopo è mappare internamente l'architettura IT dell'azienda senza mai attaccarla direttamente.

## 📚 Contesto e Definizioni

In fase di Reconnaissance (Ricognizione della [[Cyber kill chain]]), FOCA automatizza l'utilizzo delle [[Google dorks]] per scaricare centinaia di documenti aziendali (es. bandi, moduli PDF). Successivamente, ne scansiona i metadati (EXIF, dati di creazione) estraendo le "tracce invisibili" lasciate dai computer dei dipendenti durante la redazione.

## 📊 Dati, Tecnologie e Metriche

Il software correla i dati estratti per generare un report di rete estremamente dettagliato che include:
*   Nomi utente e cartelle di sistema (`C:\Users\mario.rossi\Desktop\documento.docx`).
*   Nomi dei server interni e percorsi delle stampanti di rete.
*   Versioni obsolete del software utilizzato (es. Word 2007, vulnerabile a exploit noti).
*   Indirizzi IP privati (LAN) della rete aziendale.
Questi dati sono il carburante ideale per architettare un successivo [[Attacco di phishing]] di tipo Spear-Phishing ("Ciao Mario, il file sulla stampante di rete 192.168.1.15 è bloccato").

## 🔗 Connessioni e Pattern

- [[Metadati]]
- [[Google dorks]]
- [[Attacco di phishing]]
- [[Cyber kill chain]]
- [[--]]
F/I/H
- [[--]]
