---
title: "Maltego"
tags: ["OSINT", "processed", "maltego", "sna", "link-analysis"]
date: "2026-05-15"
status: "draft"
depth: "deep"
sources: "2"
tipo: "concetto"
---

# Maltego

## 🎯 Sintesi Strategica

**Maltego** è la piattaforma software commerciale leader per la "Link Analysis" e la [[Social network analysis]] interattiva in ambito d'intelligence. Sviluppato da Paterva, fornisce un'interfaccia visiva a grafi che permette agli investigatori [[Osint]] di mappare relazioni occulte tra entità disparate (Indirizzi IP, domini, profili social, aziende, numeri di telefono). Il suo potere risiede nella capacità di eseguire "Transforms": script automatizzati che interrogano decine di API esterne restituendo i risultati direttamente sul grafo.

## 📚 Contesto e Definizioni

L'architettura di Maltego si basa su Entità (Nodi) e Trasformazioni (Archi logici):
*   Un analista trascina l'entità "Domain" (es. `target.com`) sul canvas.
*   Esegue la Transform "Resolve to IP" (che interroga i DNS in background). Maltego fa apparire l'entità "IPv4" collegata al dominio.
*   Esegue la Transform "Find other domains on IP" tramite l'API di [[Ip-dns intelligence]], rivelando dozzine di siti di [[Disinformazione]] nascosti sullo stesso server.

## 📊 Dati, Tecnologie e Metriche

Sebbene Maltego non sia un database, le sue potenzialità esplodono quando collegato a *Transform Hub* di terze parti (Shodan, Virustotal, Pipl, Ciphertrace). Un'indagine [[Cyber threat intelligence]] può passare in 3 click da un hash malware al gruppo APT che lo ha creato, semplicemente seguendo le connessioni visive.

## 🔗 Connessioni e Pattern

- [[Social network analysis]]
- [[Cyber threat intelligence]]
- [[Ip-dns intelligence]]
- [[--]]
F/I/H
- [[--]]
