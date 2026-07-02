---
title: "Neo4j"
tags: ["OSINT", "processed", "neo4j", "database", "sna", "grafi"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Neo4j

## 🎯 Sintesi Strategica

**Neo4j** è il principale sistema di gestione di Database a Grafi (Graph Database) nativo sul mercato. Mentre i database relazionali classici (SQL) organizzano i dati in righe e tabelle perfette per l'amministrazione aziendale, Neo4j archivia le informazioni sotto forma di *Nodi* (Entità) e *Archi* (Relazioni). Nell'[[Osint]], e in particolare nella [[Social network analysis]] (SNA), Neo4j è il motore infrastrutturale pesante in grado di trovare percorsi occulti (Pathfinding) all'interno di dataset composti da milioni di punti di contatto.

## 📚 Contesto e Definizioni

Se devi tracciare un gruppo criminale, la domanda non è "Chi è Mario?", ma "Qual è il percorso più breve tra Mario, le aziende offshore a Panama ([[Finint]]) e l'indirizzo IP del server di phishing?". In SQL, una query con 5 salti (Join) impiegherebbe ore paralizzando il server. In Neo4j, il linguaggio di query (Cypher) trova la relazione (es. "Friend of a Friend of a Friend") in millisecondi, perché le relazioni sono memorizzate nativamente come connessioni fisiche nel database.

## 📊 Dati, Tecnologie e Metriche

Neo4j si interfaccia nativamente con piattaforme di visualizzazione come [[Maltego]] o Linkurious. Le agenzie governative lo utilizzano per modellare intere [[Botnet]] o per sbrogliare l'albero genealogico finanziario (Beneficial Ownership) di aziende fantasma create per eludere le sanzioni internazionali, rivelando la centralità e il grado di influenza (Degree Centrality) di singoli operatori nascosti.

## 🔗 Connessioni e Pattern

- [[Social network analysis]]
- [[Finint]]
- [[Maltego]]
- [[Data warehouse]]
- [[--]]
F/I/H
- [[--]]
