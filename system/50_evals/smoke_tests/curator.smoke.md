# Smoke Test — Curator

**Input:** `00_inbox/test_source.md` con contenuto: "L'analisi OSINT dei droni FPV e della
guerra elettronica in Ucraina."

**Output atteso:**
- DUE note atomiche: `10_drafts/Droni fpv.md` e `10_drafts/Guerra elettronica.md`
- Ciascuna con backlink `[[Ucraina]]`
- Frontmatter completo, `status: draft`, `admiralty` <= C3
- Nessun titolo composto

**Pass se:** splitting MECE eseguito, wikilink risolvibili, nessun claim inventato.
