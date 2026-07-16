# Health Check — SEED-MED Vault

> Esecuzione: **2026-07-16 (re-check post-ingest selettivo)** · maintainer (inline) · audit read-only.
> Delta: merge selettivo del dataset `terrorismo_16072026` — ingerita **solo** la storia Africa Corps/Anefis
> (→ `Sahel` 4, `Presenza russa` 7); **escluse** le 2 storie AI-terrorismo (off-domain, sarebbero orfane).
> Scoperta di metodo: la versione BBC Monitoring è **traduzione dello stesso post Telegram**, non fonte
> indipendente → storia a **fonte unica**, trattata come rivendicazione di parte combattente (**Admiralty E5**,
> claim non verificati, N1). Sorgenti grezze in `00_inbox/dataset_terrorismo/`, **gitignored**.
## 🟢 Stato generale: SANO — certificato, nessun finding aperto

| # | Check | Esito |
|---|-------|-------|
| 1 | Wikilink 1:1 (link fantasma) — note + report | ✅ **zero** |
| 2 | Wikilink spezzati da newline | ✅ **zero** |
| 3 | Note orfane | ✅ **zero** |
| 4 | Schema frontmatter (8 campi) | ✅ **completo** |
| 5 | Coerenza depth ↔ fonti (§5): `deep` con <5 fonti | ✅ **zero** |
| 6 | No-Wikipedia (corpi note + report) | ✅ **zero** |
| 7 | Draft marcati `validated` | ✅ **nessuno** |
| 8 | Provenance verso file eliminati | ✅ **zero** |
| 9 | Anglicismo "carve-up" residuo | ✅ **zero** (uniformato a "spartizione") |

## Inventario
- **53 note** (26 validated + 27 draft) — di cui **22 deep** (tutte ≥5 fonti)
- **4 report** prose-as-title · **16 critiche** avversariali
- Versionato su **GitHub privato** (myrtocommunis/SEED-MED), 81 commit, tree sincronizzato

## Cluster Libia-mediazione (lavoro recente)
- Nota `Mediazione statunitense` a **9 fonti** con letture di esperti terzi (Wehry/Carnegie, Talbot/Atlantic Council) e caveat anti-stakeholder coerenti.
- Report di sintesi sottoposto a **due giri di adversary** (6→7/10, soglia di merito), con revisione fino a rev.3; tesi affinata che pesa le forze, confuta il proprio steel-man, distingue convergenza reale (USA-Pakistan) da apparente (Egitto).
- Nodo analitico `Misurata veto-player` formalizzato in nota e report.

## Certificazione
Nessun finding aperto. Il vault è **pienamente coerente, in italiano, versionato e sincronizzato**. Il maintainer certifica lo stato finale come **SANO**.
