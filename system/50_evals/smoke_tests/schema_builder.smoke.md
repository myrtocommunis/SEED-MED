# Smoke Test — Schema Builder

**Input:** ~15 file in `00_inbox/` su temi OSINT misti (es. "OSINT, GEOINT ed elettronica").
**Output atteso:**
- Wisdom-note atomiche VUOTE in `10_drafts/` (`status: schema`, sezioni + criteri, zero contenuto)
- Temi ibridi scissi in note parallele (MECE)
- `20_knowledge/_schema_map.md` con regole "quale file → quale nota"
**Pass se:** nessun contenuto fattuale, naming atomico, nessuna web search, schema_map presente.
