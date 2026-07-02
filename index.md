---
title: "Index — Knowledge Catalog"
date: "2026-05-16"
tipo: "index"
tags: ["system", "index", "persistenza"]
---

# Index — Knowledge Catalog

## Stato del Vault

| Metrica | Valore |
|---|---|
| Note totali `wiki/` | 681 |
| Sorgenti in `bozze/sorgenti/` | 0 |
| Analisi in `bozze/analisi/` | 0 |
| Ultimo aggiornamento | 2026-05-16 |
| Seed version | 7.0 |

## Struttura Filesystem

```
SEED/
├── index.md              ← questo file
├── log.md                ← cronologia operazioni
├── wiki_unitario.md      ← indice flat generato (681 voci)
├── bozze/
│   ├── sorgenti/         ← fonti grezze non modificabili
│   └── analisi/          ← output prodotti dagli agenti
└── wiki/                 ← 681 note atomiche (conoscenza vault)
```

## Per Dominio (`wiki/`)

| Dominio | Voci | Stato |
|---|---|---|
| AI & Machine Learning | 133 | wiki |
| Concetti & Varie | 195 | wiki |
| Cybersecurity & Cyber Threat Intelligence | 98 | wiki |
| Disinformazione & Influenza Cognitiva | 46 | wiki |
| Geopolitica & Conflitti | 11 | wiki |
| Normativa, Legale & Compliance | 7 | wiki |
| OSINT & Metodologie Intelligence | 68 | wiki |
| Privacy, OPSEC & Crittografia | 46 | wiki |
| Sicurezza Nazionale & Difesa | 13 | wiki |
| Strumenti & Tecnologie | 64 | wiki |

## Agenti Attivi

| Agente | Ruolo | Path | Status |
|---|---|---|---|
| Architect | Meta-agente compilatore vault | `.claude/agents/architect.md` | active |

## Note Pinned

*(da compilare manualmente — note validate di riferimento assoluto per il dominio)*

---
*Aggiornare a ogni sessione tramite rituale **Persist**.  
Formato riga: `| [[nome-nota]] | dominio | status |`*
