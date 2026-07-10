# Health Check — SEED-MED Vault

> Esecuzione: **2026-07-10** · maintainer (inline, subagent non disponibile in sessione) · audit read-only
> Scansione non distruttiva: nessuna nota modificata, nessuno `status` promosso o declassato.

## 🟢 Stato generale: SANO

| Check | Esito |
|-------|-------|
| Note totali | 26 validated (`20_knowledge/`) + 27 draft (`10_drafts/`) + 2 schema_map |
| Wikilink 1:1 (link fantasma) | ✅ **zero** |
| Note orfane (senza backlink entrante) | ✅ **zero** |
| Schema frontmatter (8 campi obbligatori) | ✅ **completo su tutte** |
| Vincolo no-Wikipedia | ✅ **zero occorrenze** |
| Draft marcati `validated` (violazione §3) | ✅ **nessuno** |
| Duplicati draft/knowledge | ✅ **nessuno** |
| Promozioni umane recenti | ✅ `Return hubs`, `Regolamento rimpatri` → `20_knowledge/`, `validated` |

## 🟡 Unico finding: 20 note `deep` sotto la soglia delle 5 fonti

La quality gate §5 richiede **≥5 fonti** per `depth: deep`. Queste 20 note sono etichettate `deep` ma non la raggiungono (retaggio della fase di build del dominio, precedente all'irrobustimento sistematico):

**Validate (`20_knowledge/`):** Egitto (4) · Haftar (3) · Libia (3) · Eni (3) · Algeria (4) · Cipro (4) · Dispute zee (3) · Bilancio libico (3) · Migrazione (3) · Rotta del mediterraneo centrale (4)

**Draft (`10_drafts/`):** Egeo (3) · Gasdotti (4) · Blue homeland (3) · Ucraina (4) · Saif al-islam (4) · Sahel (3) · Libyan investment authority (2) · Opec (3) · Banca centrale libica (3) · Frammentazione interna (3)

### Raccomandazione (decisione umana — il maintainer non modifica)
Due strade, non mutuamente esclusive:
1. **Irrobustire** a 5 fonti le note core più esposte (candidate prioritarie: `Libia`, `Eni`, `Migrazione`, `Haftar` — pilastri del dominio);
2. **Declassare** a `depth: standard` quelle che restano legittimamente a 3-4 fonti (es. `Libyan investment authority`, `Banca centrale libica`, nodi di supporto) per riallineare l'etichetta al contenuto.

Nota: la coerenza è "cosmetica" ma incide sulla fiducia — una nota `deep/3-fonti` promette più di quanto mantenga.

## Prossime azioni suggerite
- Nessun intervento urgente: il grafo è integro e navigabile.
- Al prossimo ciclo di rafforzamento, partire dai 4 pilastri sopra.

---
_Run precedente: 2026-07-09 (vault sano). Delta: +4 note migrazione, +2 promozioni, finding deep/fonti invariato._
