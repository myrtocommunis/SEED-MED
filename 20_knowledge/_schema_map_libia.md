# Schema Map — Dataset Libia (corpus news 2025-2026)

> Generato da `schema_builder` il 2026-07-02. Fonte: `00_inbox/dataset_libia/` (21 MD leggibili
> + CSV QIC; 177 PDF NON ancora estratti). Nessuna web search (mappatura strutturale).

## Macro-temi rilevati (batch scan: 21 headline + CSV QIC codificato)

| Wisdom-note atomica | Segnale (headline ricorrenti) | Stato |
|---------------------|-------------------------------|-------|
| **`Bilancio libico`** | Cluster dominante: primo bilancio unificato in oltre un decennio (Reuters, US DOS, Boulos) | schema |
| **`Mediazione statunitense`** | Massad Boulos, "US uniting Libyan rivals", Flintlock 26 | schema |
| **`Presenza russa`** | WSJ "squeeze out Russia" | schema |
| **`Petrolio`** | Asta esplorativa dopo 18 anni, +1M barili/giorno, boom da guerra Iran, TotalEnergies Waha | schema |
| **`Haftar`** | Saddam/Bilgassem/Khalifa Haftar, budget, Flintlock | schema |
| `Migrazione` *(esiste)* | EU return hubs, Return Regulation, Economist | riuso |
| `Turchia` *(esiste)* | Mandato truppe esteso, capo di SM libico morto in Turchia | riuso |
| `Libia` *(esiste)* | Nodo-arena; frammentazione politica | riuso |
| `Eni` *(esiste)* | Petrolio/energia (via PDF da estrarre) | riuso |

## Metodo sorgente (dalla Sezione 1 - QIC)
Il CSV `1.1_...QIC_PESTL_SM_v12.csv` (80 news) è codificato con: Eventi · Tema · **Affidabilità
fonte (A-F)** · **Attendibilità info (1-6)** [scala Admiralty] · Nota QIC · Valutazioni ·
Previsioni · Fattori · **Categoria PESTLE-SM**. Riusabile come ground-truth per l'Admiralty delle note.

## Regole di collocazione / prossimi passi
- Splitting MECE già applicato ai temi ibridi (es. "budget **e** Flintlock" → `Bilancio libico` + `Mediazione statunitense`).
- I 177 PDF restano da estrarre: il `curator` li processerà in un secondo passo (nuovo Pre-Flight Gate).
- Naming atomico minimo; wikilink solo a note esistenti.
