---
title: Network analysis per osint
tags:
- OSINT
- processed
- network-analysis-per-osint
date: '2026-05-15'
status: draft
depth: standard
tipo: concetto
---

# Network analysis per osint

La *network analysis per osint*, nel contesto delle fonti operative fornite, si riferisce all'analisi strutturale delle infrastrutture di rete e dei pivot tecnici (IP, DNS, ASN, SSID/BSSID) come base per la correlazione investigativa. A differenza delle metodologie basate su grafi sociali, l'approccio descritto privilegia la tracciabilità infrastrutturale, la raccolta passiva e la validazione degli indicatori tecnici per ricostruire pattern operativi senza interazione diretta con il target.

## Principi operativi

Il fondamento metodologico è la **correlazione**, non l'attribuzione immediata. Un indicatore tecnico (IP, dominio, MAC address) viene trattato come un pivot riconducibile a layer successivi: `IP → ASN → hosting → [[DNS History]] → blacklist`. La logica operativa impone di distinguere tra:
- **Indicatore tecnico e attore umano:** un IP può essere condiviso, storico, dietro proxy/Tor o mobile; non identifica direttamente un soggetto.
- **Correlazione ≠ Attribuzione:** la ricostruzione filiera informativa richiede triangolazione multipla e verifica incrociata prima di qualsiasi conclusione operativa.
- **Passività come strategia:** la raccolta passiva ([[DNS History]], [[Passive DNS]], WHOIS history) è prioritaria per ridurre la visibilità dell'indagine e preservare l'OPSEC.

## Pivot infrastrutturali

### IP e ASN
L'IP funge da strato di astrazione che permette l'interoperabilità tra reti fisiche diverse (Wi-Fi, fibra, mobile, data center). L'ASN (Autonomous System Number) consente il passaggio dall'indirizzo puntuale alla rete che lo annuncia, abilitando geolocalizzazione, identificazione del provider e valutazione della reputation. La stabilità degli IP è limitata: possono cambiare dinamicamente o essere riutilizzati.

### DNS e [[Passive DNS]]

Le tecniche DNS includono lookup, enumerazione record (A, AAAA, MX, NS, SOA, TXT, CNAME, SRV, PTR), reverse DNS e WHOIS. La **[[DNS History]]** ricostruisce l'evoluzione temporale dei record, risultando essenziale per:
- Identificare cambiamenti infrastrutturali o domini "burner".
- Analizzare domini dietro reverse proxy.
- Supportare incident response con dati storici.
Il **[[Passive DNS]]** permette il recupero di sottodomini e record senza interagire con il target, riducendo il footprint investigativo.

### Wi-Fi e localizzazione

SSID (nome rete) e BSSID (MAC address dell'access point) costituiscono pivot geografici persistenti. Database crowdsourced come WiGLE permettono lookup per localizzazione access point. La trilaterazione richiede almeno tre access point per triangolazione GPS. I dati EXIF incorporati nelle immagini originali (modello fotocamera, timestamp, coordinate GPS, informazioni ottiche) integrano la geolocalizzazione visiva.

## Raccolta passiva e OPSEC

La strategia di raccolta privilegiata è la passività. L'interazione diretta con il target (active DNS, WHOIS live, scansione attiva) aumenta il rischio di rilevamento e alterazione degli indicatori. La raccolta passiva si basa su:
- Archivi storici e [[Passive DNS]].
- Lookup WHOIS/Reverse WHOIS non interattivi.
- Monitoraggio di reputation e blacklist senza ping o probe diretti.
Questa impostazione è considerata prerequisito operativo per indagini su target sensibili o infrastrutture critiche.

## Ecosistema degli strumenti

La validazione degli strumenti è un requisito fondamentale. Tutti i tool elencati nelle fonti operative sono verificati come reali e funzionali:

| Categoria | Strumenti verificati |
|-----------|----------------------|
| IP/ASN/Reputation | ipinfo.io, bgpview.io, Virustotal |
| DNS/[[Passive DNS]] | viewdns.info, Securitytrails, RiskIQ Passivetotal, CENSys, Farsight DNSDB, Domaintools |
| Enumerazione/Recon | sublist3r, recon-ng, dnspython, dig, nslookup, whois |
| Geolocalizzazione/Wi-Fi | WiGLE, Google Maps/Street View, EXIF extraction (Exiftool) |
| Reverse Search/Media | Google Images/LENS, Tineye, Yandex Images, Pimeyes, aperisolve.com |
| Pipeline CLI | FFMPEG, Pocketsphinx, Tesseract OCR, Translate Shell |

La validazione incrociata elimina il rischio di tool fantasma o trascrizioni errate (es. correzione di "naingdot.com" in `9gag.com`, verifica di BGPview.io e web-check.as93.net).

## Limiti e considerazioni

### Gap di attribuzione
L'OSINT tecnico non può collegare un'identità umana a un IP senza intelligence aggiuntiva (log ISP, procedure legali, HUMINT/SIGINT). L'analisi si ferma alla correlazione infrastrutturale e operativa.

### Manipolazione e bias

- Le immagini possono essere riutilizzate, manipolate o steganografiche.
- Il facial/object detection è esposto a bias demografici e rischi di misidentification.
- La [[DNS History]] e i passive record sono temporali, non statici.

### Etica e privacy

L'uso di EXIF, Wi-Fi crowdsourcing e [[Passive DNS]] solleva questioni di privacy e consenso. L'OSINT richiede report espliciti su metodologia, tecnica, risultati e limiti, con controllo umano sui risultati generati da acceleratori IA.

## Voci correlate

- [[Social network analysis]]
- [[Passive DNS]]
- [[DNS History]]
- [[IP geolocation]]
- [[OPSEC in OSINT]]
