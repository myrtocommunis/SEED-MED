---
title: Osint operativo
tags:
- OSINT
- processed
- osint-operativo
date: '2026-05-15'
status: draft
depth: standard
tipo: concetto
---

# Osint operativo

L'**OSINT operativo** (dall'inglese *Open Source Intelligence*) è una disciplina dell'intelligence dedicata alla raccolta, analisi e sfruttamento strategico di informazioni derivanti da fonti aperte, documentabili e replicabili. Nata come approccio basato su dati personali ampiamente accessibili, si è evoluta in un ecosistema commercializzato in cui i dati personali sono diventati asset monetizzati, con l'accesso progressivamente limitato da normative sulla privacy come il [[GDPR]].

## Principi metodologici

Il principio fondante dell'OSINT operativo è la preferenza metodologica per le fonti *overt* (aperte) rispetto a quelle *covert* (coperte), garantendo tracciabilità e replicabilità delle indagini. La metodologia si basa sulla consapevolezza che ogni soggetto lascia tracce digitali, sia attraverso un comportamento consapevole (*digital footprint active*) sia in modo involontario (*digital footprint passive*).

## Componenti fondamentali

### Digital footprint
Le tracce digitali si classificano in due categorie:
- **Attive**: generate dal comportamento consapevole del target, come profili social, post, foto, commenti, portfolio e contenuti video.
- **Passive**: generate da terze parti o infrastrutture, tra cui policy sulla privacy, data breach, metadati e indici dei motori di ricerca.

### Selectors e pivoting

I *selector* sono identificatori chiave che permettono il *pivoting* (spostamento) tra diverse fonti. Tra questi figurano nome, varianti, nickname, indirizzo email, numero di telefono, username, foto, dominio, handle social, ID, ICQ, Skype, indirizzo fisico, azienda di riferimento e schema lessicale. La persistenza di questi elementi nel tempo, unita alla tendenza dei soggetti a riutilizzare identificatori riconoscibili, costituisce la base teorica del targeting OSINT.

### Targeting individuale

L'analisi operativa si articola attorno a tre domande operative:
- **Chi è**: identità reale e virtuale, paure, affetti, cultura e ideologia.
- **Cosa fa**: impiego, formazione, hobby, comunità di appartenenza, spostamenti e affiliazioni.
- **Cosa usa**: dispositivi, presenza online, livello di esposizione, nickname, contatti e piattaforme social.

## Workflow operativo

Il processo di raccolta e analisi segue un flusso strutturato:
1. Definizione dell'obiettivo e delle domande operative.
2. Mappatura delle informazioni disponibili rispetto ai gap conoscitivi.
3. Definizione del contesto linguistico, culturale e geografico.
4. Identificazione delle fonti prioritarie e deperibili.
5. Pianificazione della strategia di raccolta e pivoting.
6. Applicazione di query avanzate (*Google dorks*) e strumenti di categoria.
7. Documentazione della catena di evidenza.

Il *pivoting* consiste nel passaggio sequenziale da un selector all'altro (es. username → email → data breach → nome → social → localizzazione → azienda), garantendo la continuità investigativa.

## Strumentazione e categorie

L'OSINT operativo utilizza strumenti specializzati suddivisi per ambito:
- **People search**: piattaforme per la ricerca di persone e incrocio di dati (es. Pipl, Epieos, Have I Been Pwned, IntelligenceX, Dehashed).
- **Username**: tool per la verifica della disponibilità e delle varianti degli username (es. Instantusername, Sherlock, Bellingcat Name Variant Search).
- **Phone/Email**: servizi per la validazione di contatti e la verifica di data breach (es. Free-HLR, Truecaller, format conversion E.164).
- **Face recognition**: algoritmi di riconoscimento facciale (es. Pimeyes, Search4Faces), da utilizzare con cautela poiché la similarità non equivale all'identificazione.
- **Geospaziale**: strumenti per l'analisi territoriale e SATellitare (es. NASA FIRMS, Openstreetmap, Wikimapia).

La deperibilità degli strumenti è un fattore critico: il workflow deve essere progettato per essere replicabile e indipendente da piattaforme specifiche.

## Corporate Intelligence (BI/CI)

La Corporate Intelligence estende le metodologie dell'OSINT operativo alle entità aziendali, analizzando catene di ownership, beneficiari effettivi, reti societarie, esposizioni reputazionali e compliance alle sanzioni. L'analisi si avvale di registri ufficiali e database pubblici (es. Openownership, Opencorporates, The Org, North Data, Crunchbase, SEC EDGAR, Zefix, ICIJ, Importyeti) per tracciare filiere, organigrammi, documenti societari e movimenti finanziari.

## Concetti correlati

L'OSINT operativo si integra con pratiche di sicurezza operativa (OPSEC), checklist di targeting digitale, fondamenti di raccolta OSINT, valutazione dei rischi OWASP nell'integrazione di tool e servizi AI, e campagne di intelligence finanziaria e infrastrutturale (FIMI).

## Voci correlate

* [[Osint nella sicurezza nazionale]]

- [[--]]
[F] Footer: ARIANNA | Intelligenza Narrativa | Vault OSINT_CORE
[I] Input: Sorgente grezza fornita dall'utente
[H] Header: ---

## 🔗 Connessioni e Pattern

- [[Corporate intelligence]]
- [[Infrastrutture]]
- [[Motori di ricerca]]
- [[Pianificazione]]
- [[Sicurezza nazionale]]
- [[Targeting digitale]]
