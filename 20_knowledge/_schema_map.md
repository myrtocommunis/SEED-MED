# Schema Map — Mappa Tematica del Corpus

> Generato da `schema_builder` il 2026-07-02. Definisce quali sorgenti alimentano quali
> note atomiche. Naming atomico minimo, splitting MECE dei temi composti.

## Macro-temi rilevati (batch scan: 3 file)

| Wisdom-note atomica | Sorgenti che la alimentano | Stato |
|---------------------|----------------------------|-------|
| `Droni fpv` | report_droni_ucraina.md | draft (curator) |
| `Guerra elettronica` | report_droni_ucraina.md · osint_metodi.md | draft (curator) |
| `Deepfake` | nota_deepfake_disinfo.md | schema |
| `Disinformazione` | nota_deepfake_disinfo.md | schema |
| `Osint` | osint_metodi.md | schema |
| `Geoint` | osint_metodi.md | schema |
| `Admiralty` | osint_metodi.md | schema |
| `Ucraina` | report_droni_ucraina.md (entità geografica) | pending |

## Regole di collocazione
- Temi composti scissi in note parallele: "Droni FPV **e** guerra elettronica" → `Droni fpv` + `Guerra elettronica`.
- "OSINT, GEOINT **ed** elettronica" → `Osint` + `Geoint` + `Guerra elettronica` (merge sul tema condiviso).
- Ogni wisdom-note usa Nome Atomico Minimo; i wikilink puntano solo a note esistenti.
