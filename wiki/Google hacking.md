---
title: "Google hacking"
tags: ["OSINT", "processed", "dorking", "ricerca-avanzata", "motori-di-ricerca", "raccolta"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "4"
tipo: "concetto"
---

# Google hacking

## 🎯 Sintesi Strategica

Il **Google Hacking (o Dorking)** è la disciplina che trasforma i motori di ricerca generalisti in strumenti di precisione chirurgica tramite l'uso di query avanzate e operatori booleani. Nell'[[Osint]] e nella [[Cyber threat intelligence]], i "Dork" rappresentano il livello zero della [[Raccolta]]: prima di utilizzare qualsiasi tool automatizzato, l'analista interroga l'indice di Google (o Yandex / Bing) per individuare file sensibili esposti accidentalmente (es. backup, log, password), directory aperte o pattern informativi nascosti. Il Dorking è pura *ricerca passiva*; non è un exploit, ma sfrutta le vulnerabilità di configurazione e indicizzazione dei server bersaglio.

## 📚 Contesto e Definizioni

I Dorks si fondano su otto operatori sintattici principali che fungono da filtri:
1.  **`site:`** Restringe la ricerca a un dominio specifico (es. `site:gov.it` o `site:t.me`).
2.  **`filetype:`** Filtra per estensione documentale (es. `filetype:pdf` o `filetype:env`).
3.  **`inurl:`** Cerca parole chiave all'interno del percorso URL (es. `inurl:admin`).
4.  **`intitle:`** Cerca nel tag HTML del titolo (es. `intitle:"index of"`).
5.  **`after:` / `before:`** Applica un filtro temporale (es. `after:2024-01-01`).
6.  **`"..."` (Virgolette):** Impone la corrispondenza di stringa esatta.
7.  **`-` (Meno):** Operatore di esclusione, vitale per eliminare il rumore (es. `-site:youtube.com`).
8.  **`OR`:** Operatore logico per alternative semantiche.

Un classico dork offensivo unisce questi operatori: `site:target.com filetype:env "DB_PASSWORD"` per scovare credenziali dimenticate su repository pubblici.

## 📊 Dati, Tecnologie e Metriche

La libreria globale di riferimento è il **[[Google hacking]] (GHDB)** ospitato su exploit-db, che cataloga migliaia di dork classificati (es. "Files Containing Passwords"). 
L'uso dei Dork non si limita a Google. Yandex è vitale per le indagini in area russa, mentre Duckduckgo garantisce [[Opsec]] evitando la personalizzazione algoritmica dei risultati.
Eticamente, c'è una linea invalicabile dettata dal [[Quadro giuridico]]: trovare un pannello di login scoperto tramite `inurl:admin` è OSINT; tentare di accedere forzando le credenziali (Brute-force) è un reato di accesso abusivo (Exploitation), violando il CFAA e le leggi nazionali.

## 🔗 Connessioni e Pattern

- [[Raccolta]]
- [[Opsec]]
- [[Google hacking]]
- [[Yandex]]
- [[Cyber threat intelligence]]
- [[--]]
F/I/H
- [[--]]
