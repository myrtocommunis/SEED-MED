"""
Build "Il futuro dei servizi di intelligence — presentazione.pptx"
11 diapositive: 1 metodologia + 10 conclusioni analitiche
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt
import math

# ── Palette ────────────────────────────────────────────────────────────────────
BG       = RGBColor(0x0D, 0x1B, 0x2A)   # navy scuro
ACCENT   = RGBColor(0x00, 0xB4, 0xD8)   # ciano brillante
GOLD     = RGBColor(0xF4, 0xA2, 0x61)   # ambra
RED      = RGBColor(0xE6, 0x3B, 0x3B)   # rosso allerta
GREEN    = RGBColor(0x2D, 0xC6, 0x7E)   # verde
PURPLE   = RGBColor(0x9B, 0x5D, 0xE5)   # viola
WHITE    = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT    = RGBColor(0xB0, 0xC4, 0xDE)   # steel blue chiaro
DARK2    = RGBColor(0x16, 0x2D, 0x44)   # pannello scuro

W = Inches(13.33)
H = Inches(7.5)


def rgb(r, g, b):
    return RGBColor(r, g, b)


def add_rect(slide, x, y, w, h, fill_color, alpha_hack=None, radius=0):
    shape = slide.shapes.add_shape(
        1,  # MSO_SHAPE_TYPE.RECTANGLE
        Inches(x), Inches(y), Inches(w), Inches(h)
    )
    shape.line.fill.background()
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    return shape


def add_rounded_rect(slide, x, y, w, h, fill_color):
    from pptx.enum.shapes import MSO_SHAPE_TYPE
    shape = slide.shapes.add_shape(
        5,  # MSO_AUTO_SHAPE_TYPE.ROUNDED_RECTANGLE
        Inches(x), Inches(y), Inches(w), Inches(h)
    )
    shape.line.fill.background()
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    shape.adjustments[0] = 0.1
    return shape


def add_circle(slide, cx, cy, r, fill_color, line_color=None, line_width=None):
    shape = slide.shapes.add_shape(
        9,  # OVAL
        Inches(cx - r), Inches(cy - r), Inches(r * 2), Inches(r * 2)
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    if line_color:
        shape.line.color.rgb = line_color
        shape.line.width = Pt(line_width or 2)
    else:
        shape.line.fill.background()
    return shape


def add_textbox(slide, x, y, w, h, text, size, color, bold=False,
                align=PP_ALIGN.LEFT, italic=False):
    txBox = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size = Pt(size)
    run.font.color.rgb = color
    run.font.bold = bold
    run.font.italic = italic
    return txBox


def add_keyword_chip(slide, x, y, text, bg_color, text_color=None):
    text_color = text_color or WHITE
    chip = add_rounded_rect(slide, x, y, len(text) * 0.13 + 0.35, 0.42, bg_color)
    tf = chip.text_frame
    tf.word_wrap = False
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    run = p.add_run()
    run.text = text
    run.font.size = Pt(15)
    run.font.bold = True
    run.font.color.rgb = text_color
    return chip


def set_bg(slide):
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = BG


def add_top_bar(slide, number, title, color=ACCENT):
    # numero slide cerchio
    add_circle(slide, 0.55, 0.42, 0.33, color)
    add_textbox(slide, 0.25, 0.15, 0.62, 0.55,
                str(number), 22, WHITE, bold=True, align=PP_ALIGN.CENTER)
    # titolo
    add_textbox(slide, 1.05, 0.12, 11.8, 0.65,
                title, 22, WHITE, bold=True)
    # linea separatrice
    line = slide.shapes.add_shape(1, Inches(1.05), Inches(0.72), Inches(11.8), Pt(2))
    line.fill.solid()
    line.fill.fore_color.rgb = color
    line.line.fill.background()


def add_panel(slide, x, y, w, h, color=DARK2):
    s = add_rect(slide, x, y, w, h, color)
    return s


# ── VISUAL GENERATORS ──────────────────────────────────────────────────────────

def visual_methodology(slide):
    """5 cerchi colorati = 5 serie geografiche, collegati verso un centro"""
    cx, cy = 9.5, 4.0
    series = [
        ("USA/Int.", rgb(0x00, 0xB4, 0xD8), -1.8, -1.5),
        ("Europa",  rgb(0x2D, 0xC6, 0x7E),  1.8, -1.2),
        ("Asia",    rgb(0xF4, 0xA2, 0x61),   2.2,  0.6),
        ("Cina",    rgb(0xE6, 0x3B, 0x3B),   0.0,  1.8),
        ("Russia",  rgb(0x9B, 0x5D, 0xE5), -2.0,  1.0),
    ]
    # centro
    add_circle(slide, cx, cy, 0.5, ACCENT)
    add_textbox(slide, cx - 0.45, cy - 0.22, 0.9, 0.45, "60", 18, WHITE, bold=True, align=PP_ALIGN.CENTER)

    for label, col, dx, dy in series:
        sx, sy = cx + dx * 0.7, cy + dy * 0.7
        # linea (shape rettangolare sottile orientata manualmente non disponibile,
        # uso cerchio piccolo come nodo)
        add_circle(slide, sx, sy, 0.38, col)
        add_textbox(slide, sx - 0.6, sy - 0.17, 1.2, 0.35,
                    label, 11, WHITE, bold=True, align=PP_ALIGN.CENTER)


def visual_ooda(slide):
    """Ciclo OODA: 4 cerchi in sequenza con frecce"""
    labels = ["Osserva", "Orienta", "Decide", "Agisce"]
    colors = [ACCENT, GOLD, GREEN, RED]
    base_x, base_y = 8.2, 2.8
    positions = [(0, 0), (2.0, 0), (2.0, 2.0), (0, 2.0)]
    for i, (dx, dy) in enumerate(positions):
        add_circle(slide, base_x + dx, base_y + dy, 0.55, colors[i])
        add_textbox(slide, base_x + dx - 0.7, base_y + dy - 0.18,
                    1.4, 0.36, labels[i], 12, WHITE, bold=True, align=PP_ALIGN.CENTER)
    # frecce simulate con rettangoli stretti
    arrow_specs = [
        (base_x + 0.55, base_y - 0.04, 0.9, 0.1),   # destra
        (base_x + 1.9,  base_y + 0.55, 0.1, 0.9),   # giù
        (base_x + 0.55, base_y + 1.9,  0.9, 0.1),   # sinistra (inverso)
        (base_x - 0.1,  base_y + 0.55, 0.1, 0.9),   # su
    ]
    for ax, ay, aw, ah in arrow_specs:
        a = add_rect(slide, ax, ay, aw, ah, LIGHT)
    # etichetta AI
    add_textbox(slide, 8.5, 4.85, 2.0, 0.4,
                "AI: ore → secondi", 13, GOLD, bold=True, align=PP_ALIGN.CENTER)


def visual_eye(slide):
    """OSINT: occhio stilizzato"""
    ex, ey = 9.8, 3.8
    add_circle(slide, ex, ey, 1.2, DARK2)
    add_circle(slide, ex, ey, 1.2, DARK2, line_color=ACCENT, line_width=3)
    add_circle(slide, ex, ey, 0.65, ACCENT)
    add_circle(slide, ex, ey, 0.28, BG)
    # raggio
    add_textbox(slide, ex - 0.5, ey + 1.3, 1.0, 0.4,
                "OSINT", 14, ACCENT, bold=True, align=PP_ALIGN.CENTER)
    # icona saturazione russa
    for i in range(5):
        add_rect(slide, 8.3 + i * 0.45, 5.2, 0.3, 0.3 + i * 0.15,
                 rgb(0xE6, 0x3B, 0x3B))


def visual_shield(slide):
    """Cybersicurezza: scudo composto da shape"""
    sx, sy = 9.6, 2.4
    # scudo (pentagon-like approssimato con rettangolo + triangolo simulato)
    add_rounded_rect(slide, sx - 0.7, sy, 1.4, 2.0, DARK2)
    # contorno
    s = slide.shapes.add_shape(5, Inches(sx - 0.7), Inches(sy),
                                Inches(1.4), Inches(2.0))
    s.fill.background()
    s.line.color.rgb = ACCENT
    s.line.width = Pt(3)
    add_textbox(slide, sx - 0.45, sy + 0.6, 0.9, 0.8,
                "🛡", 40, ACCENT, align=PP_ALIGN.CENTER)
    # cerchi overlap (stato + criminalità)
    add_circle(slide, 9.1, 5.2, 0.55, rgb(0x00, 0xB4, 0xD8))
    add_circle(slide, 10.0, 5.2, 0.55, rgb(0xE6, 0x3B, 0x3B))
    add_textbox(slide, 8.5, 5.8, 1.8, 0.35,
                "Stato ↔ Crimine", 11, LIGHT, align=PP_ALIGN.CENTER)


def visual_bar66(slide):
    """Grafico 66/74 tecnologie critiche"""
    bx, by = 8.1, 2.2
    total = 74
    china = 66
    bar_w = 4.0
    bar_h = 0.55
    gap = 0.2
    add_textbox(slide, bx, by - 0.45, 4.0, 0.4,
                "Tecnologie critiche globali (74)", 12, LIGHT, bold=True)
    # barra totale
    add_rounded_rect(slide, bx, by, bar_w, bar_h, DARK2)
    # barra Cina
    china_w = bar_w * (china / total)
    add_rounded_rect(slide, bx, by, china_w, bar_h, RED)
    add_textbox(slide, bx + china_w / 2 - 0.3, by + 0.05, 0.8, 0.45,
                "66", 22, WHITE, bold=True, align=PP_ALIGN.CENTER)
    add_textbox(slide, bx, by + bar_h + 0.05, china_w, 0.3,
                "Cina", 11, RED, bold=True)
    # anni
    add_textbox(slide, bx, by + 1.2, 4.0, 0.35,
                "Maturità operativa entro il 2030", 13, GOLD, bold=True)
    # vs Russia
    add_rect(slide, bx, by + 1.8, bar_w * (1 - 3/74) * 0.12, bar_h * 0.7,
             PURPLE)
    add_textbox(slide, bx + 0.6, by + 1.8, 3.0, 0.4,
                "Russia: – 2/3 anni (sanzioni)", 12, PURPLE)


def visual_network(slide):
    """Struttura a rete: nodi connessi"""
    nodes = [
        (9.5, 2.5, ACCENT, "Hub"),
        (8.1, 3.8, GREEN, "Cyber"),
        (10.9, 3.8, GOLD, "Geo"),
        (8.5, 5.2, LIGHT, "OSINT"),
        (10.5, 5.2, RED, "AI"),
    ]
    # connessioni (rettangoli sottili)
    hub = (9.5, 2.5)
    for nx, ny, col, lbl in nodes[1:]:
        mx = (hub[0] + nx) / 2
        my = (hub[1] + ny) / 2
        length = math.hypot(nx - hub[0], ny - hub[1])
        add_rect(slide, mx - length / 2, my - 0.04, length, 0.08, DARK2)
    for nx, ny, col, lbl in nodes:
        add_circle(slide, nx, ny, 0.42, col)
        add_textbox(slide, nx - 0.55, ny - 0.17, 1.1, 0.35,
                    lbl, 11, WHITE, bold=True, align=PP_ALIGN.CENTER)


def visual_person(slide):
    """Forza lavoro: icona persona + barre competenze"""
    px, py = 9.5, 2.3
    # testa
    add_circle(slide, px, py, 0.4, ACCENT)
    # corpo
    add_rounded_rect(slide, px - 0.45, py + 0.42, 0.9, 1.1, DARK2)
    s = slide.shapes.add_shape(5, Inches(px - 0.45), Inches(py + 0.42),
                                Inches(0.9), Inches(1.1))
    s.fill.background()
    s.line.color.rgb = ACCENT
    s.line.width = Pt(2)
    # barre competenze
    skills = [("Geopolitica", 0.8, GOLD), ("Data science", 0.55, ACCENT),
              ("AI security", 0.65, GREEN)]
    for i, (label, fill_pct, col) in enumerate(skills):
        by = py + 2.1 + i * 0.6
        add_rect(slide, 8.3, by, 2.4, 0.3, DARK2)
        add_rect(slide, 8.3, by, 2.4 * fill_pct, 0.3, col)
        add_textbox(slide, 8.3, by + 0.3, 2.4, 0.28, label, 10, LIGHT)


def visual_cognitive_war(slide):
    """Guerra cognitiva: precisione vs saturazione"""
    # Cina: mirino
    cx, cy = 9.0, 3.6
    for r in [0.9, 0.6, 0.3]:
        add_circle(slide, cx, cy, r, DARK2,
                   line_color=RED if r == 0.3 else LIGHT,
                   line_width=2)
    add_circle(slide, cx, cy, 0.08, RED)
    add_textbox(slide, cx - 0.7, cy + 1.05, 1.4, 0.35,
                "Cina: precisione", 11, RED, bold=True, align=PP_ALIGN.CENTER)

    # Russia: onde di saturazione
    rx, ry = 11.1, 3.6
    for i, r in enumerate([0.3, 0.65, 1.0, 1.35]):
        add_circle(slide, rx, ry, r, DARK2,
                   line_color=PURPLE, line_width=1)
    add_textbox(slide, rx - 0.8, ry + 1.45, 1.6, 0.35,
                "Russia: saturazione", 11, PURPLE, bold=True, align=PP_ALIGN.CENTER)


def visual_five_eyes(slide):
    """Cooperazione: Five Eyes + espansione"""
    base = [
        (9.3, 2.8, ACCENT, "USA"),
        (10.6, 3.4, ACCENT, "UK"),
        (10.2, 4.8, ACCENT, "AUS"),
        (8.4, 4.8, ACCENT, "CAN"),
        (7.9, 3.4, ACCENT, "NZL"),
    ]
    ext = [
        (9.3, 2.0, GREEN, "JPN"),
        (11.3, 2.9, GREEN, "KOR"),
    ]
    for bx, by, col, lbl in base:
        add_circle(slide, bx, by, 0.42, col)
        add_textbox(slide, bx - 0.55, by - 0.17, 1.1, 0.35,
                    lbl, 11, WHITE, bold=True, align=PP_ALIGN.CENTER)
    for bx, by, col, lbl in ext:
        add_circle(slide, bx, by, 0.35, col)
        add_textbox(slide, bx - 0.55, by - 0.14, 1.1, 0.28,
                    lbl, 10, WHITE, bold=True, align=PP_ALIGN.CENTER)
    add_textbox(slide, 7.5, 5.6, 4.0, 0.35,
                "Five Eyes+ (in costruzione)", 12, GREEN, bold=True, align=PP_ALIGN.CENTER)


def visual_three_models(slide):
    """Governance: 3 colonne = 3 modelli"""
    models = [
        ("UE\nDemocratico\nframmentato", GREEN, 7.9),
        ("Cina\nAutoritario\ncon standard", RED, 9.55),
        ("Russia\nAutoritario\nsenza standard", PURPLE, 11.2),
    ]
    for label, col, bx in models:
        h = 2.8
        add_rounded_rect(slide, bx - 0.55, 2.0, 1.1, h, DARK2)
        s = slide.shapes.add_shape(5, Inches(bx - 0.55), Inches(2.0),
                                    Inches(1.1), Inches(h))
        s.fill.background()
        s.line.color.rgb = col
        s.line.width = Pt(3)
        tf = s.text_frame
        tf.word_wrap = True
        from pptx.util import Pt as uPt
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        for line in label.split("\n"):
            run = p.add_run()
            run.text = line + ("\n" if line != label.split("\n")[-1] else "")
            run.font.size = uPt(11)
            run.font.bold = True
            run.font.color.rgb = col

    add_textbox(slide, 7.5, 5.1, 5.0, 0.4,
                "Chi adotterà quale modello entro il 2030?", 12, GOLD, bold=True, align=PP_ALIGN.CENTER)


# ── SLIDE DATA ─────────────────────────────────────────────────────────────────

SLIDES = [
    {
        "num": "M",
        "color": ACCENT,
        "title": "Metodologia e fonti",
        "subtitle": "Analisi della letteratura grigia e accademica in 3 fasi sequenziali",
        "keywords": [
            ("60 fonti", ACCENT), ("5 serie geografiche", GREEN),
            ("3 criteri di selezione", GOLD), ("10 sfide tematiche", RED),
        ],
        "body": [
            "Fase 1  —  Knowledge base: 60 schede con sintesi in 10 punti",
            "Fase 2  —  Analisi trasversale: ogni sfida da ≥ 3 fonti indipendenti",
            "Fase 3  —  Redazione: citazioni (Org., Anno) · prospettive divergenti esplicitate",
            "Fonti cinesi e russe ufficiali = fonti primarie su dottrina, non analisi indipendente",
        ],
        "visual": visual_methodology,
    },
    {
        "num": 1,
        "color": ACCENT,
        "title": "AI e intelligence: dottrina integrata o frammentazione?",
        "subtitle": "L'AI ridefinisce ogni fase del ciclo, ma l'assenza di strategia unificata produce silos",
        "keywords": [
            ("Super-OODA Loop", ACCENT), ("Fusione militare-civile (Cina)", RED),
            ("AI sovrana (Russia)", PURPLE), ("Frammentazione UE", GOLD),
        ],
        "body": [
            "USA: vantaggio strutturale con programmi federali anticipatori",
            "Cina: opacità — integrazione sistematica non dichiarata (MCF)",
            "Russia: gap misurabile — Glaz/Groza vs. NLP sperimentale (Ucraina)",
            "UE/Asia: investimenti senza dottrina unificante",
        ],
        "visual": visual_ooda,
    },
    {
        "num": 2,
        "color": GREEN,
        "title": "Tradecraft analitico: sopravvivere all'automazione",
        "subtitle": "Il ciclo decisionale scende da ore a secondi — il tradecraft va reingegnerizzato",
        "keywords": [
            ("Human-on-the-loop", GREEN), ("Validatore critico", ACCENT),
            ("Learn-while-fighting", GOLD), ("Super-OODA Loop", RED),
        ],
        "body": [
            "I format tradizionali di reporting sono obsoleti per architetture C2 algoritmiche",
            "L'analista del futuro: valida l'output AI, non lo produce",
            "Russia: modello pragmatico — combattimento reale come addestramento AI",
            "Simulazioni ≠ dati di conflitto: i servizi addestrano su dataset strutturalmente diversi",
        ],
        "visual": visual_ooda,
    },
    {
        "num": 3,
        "color": GOLD,
        "title": "OSINT: disciplina strategica vs. arma di saturazione",
        "subtitle": "Chi estrae valore dall'OSINT e chi lo rende inutilizzabile",
        "keywords": [
            ("Analisi bibliometrica", GOLD), ("DoppelGänger", RED),
            ("FIMI 29% Russia", PURPLE), ("Procurement PLA", ACCENT),
        ],
        "body": [
            "ASPI: brevetti + procurement rivelano capacità avversariali come fonti classificate",
            "CSET: documenti PLA → priorità AI militare con dettaglio operativo",
            "Russia: saturazione — 29% FIMI 2025, obiettivo è confondere non convincere",
            "Europol: crimine organizzato inquina lo spazio OSINT con AI generativa",
        ],
        "visual": visual_eye,
    },
    {
        "num": 4,
        "color": RED,
        "title": "Cybersicurezza: la distinzione Stato–crimine è obsoleta",
        "subtitle": "Cyberattacchi progettati per essere indistinguibili nella motivazione",
        "keywords": [
            ("Continuum cyber-cognitivo", RED), ("FSB + Wagner", PURPLE),
            ("RaaS", GOLD), ("AI security state", ACCENT),
        ],
        "body": [
            "Europol: campagne ibride — motivazione finanziaria e geopolitica indistinguibili",
            "Russia: FSB, GRU, Wagner, hacktivisti — stessa infrastruttura, attributo ambiguo by design",
            "Cina: CAC + Cybersecurity Law → condivisione forzata dati privati → MSS",
            "RaaS democratizza l'offensiva: moltiplicazione attori difficile da monitorare",
        ],
        "visual": visual_shield,
    },
    {
        "num": 5,
        "color": RED,
        "title": "Tecnologie critiche: la Cina guida, la Russia aggira",
        "subtitle": "66 su 74 tecnologie critiche a guida cinese — 2030 è la scadenza strategica",
        "keywords": [
            ("66/74 tecnologie", RED), ("MCF militarizzazione AI", ACCENT),
            ("Export control bypass", PURPLE), ("DeepSeek → PLA", GOLD),
        ],
        "body": [
            "ASPI: Cina dominante in sensori avanzati, quantum, biotecnologie",
            "ChatBIT: Llama/DeepSeek militarizzati via fine-tuning su dati classificati PLA",
            "Russia: sanzioni = – 2/3 anni; cooperazione Cina aggira l'export control USA",
            "Export control richiede il consenso di tutti i fornitori alternativi",
        ],
        "visual": visual_bar66,
    },
    {
        "num": 6,
        "color": GREEN,
        "title": "Struttura organizzativa: dalla gerarchia alla rete",
        "subtitle": "Le architetture verticali non reggono la velocità delle minacce ibride",
        "keywords": [
            ("Rete distribuita", GREEN), ("Silos FSB/GRU/SVR", RED),
            ("Hybrid Centre Helsinki", ACCENT), ("QG AI Cremlino 2025", PURPLE),
        ],
        "body": [
            "ECFR: centri di eccellenza per area geografica, collegati da protocolli di condivisione rapida",
            "SWP: toolbox senza strategia = investimenti senza dottrina",
            "Russia: innovazione bottom-up da Ucraina → istituzione tardiva del QG AI (2025)",
            "Anche i sistemi autoritari soffrono di silos istituzionali",
        ],
        "visual": visual_network,
    },
    {
        "num": 7,
        "color": PURPLE,
        "title": "Forza lavoro: la doppia competenza è il profilo più raro",
        "subtitle": "Geopolitica + data science: i servizi non possono vincere sul prezzo con il privato",
        "keywords": [
            ("Doppia competenza", PURPLE), ("J-AISI (Giappone)", ACCENT),
            ("15.500 specialisti Russia", RED), ("Brain drain", GOLD),
        ],
        "body": [
            "Brain drain verso Big Tech: salari, cultura, visibilità non replicabili",
            "Giappone: J-AISI — 30 specialisti full-time, modello small-but-focused",
            "Cina: fine-tuning su open source → meno dipendenza da élite AI",
            "Russia: target 15.500 in 5 anni; compensazione con reclutamento forzato da Yandex/Sberbank",
        ],
        "visual": visual_person,
    },
    {
        "num": 8,
        "color": RED,
        "title": "Guerra cognitiva: precisione cinese vs. saturazione russa",
        "subtitle": "La guerra cognitiva è già operativa — richiedono risposte diverse",
        "keywords": [
            ("Dominio cognitivo PLA", RED), ("Colonizzazione della mente", PURPLE),
            ("DoppelGänger", GOLD), ("Counter-narrative", ACCENT),
        ],
        "body": [
            "Cina: dottrina PLA — paralizzare la decisione avversariale prima del conflitto fisico",
            "Xinhua Institute: operazione cognitiva attiva in 163 Paesi (Sud globale)",
            "Russia: saturazione — volume massimo, credibilità minima, spazio informativo inutilizzabile",
            "Risposta: attribuzione rapida vs. Cina · resilienza cognitiva vs. Russia",
        ],
        "visual": visual_cognitive_war,
    },
    {
        "num": 9,
        "color": ACCENT,
        "title": "Cooperazione internazionale: Five Eyes+ e il fronte avversariale",
        "subtitle": "Asimmetrie tecnologiche intra-alleate e convergenza Russia–Cina nei forum normativi",
        "keywords": [
            ("Five Eyes+", ACCENT), ("Track II Tsinghua-Brookings", GOLD),
            ("Poliarchia morbida RIAC", PURPLE), ("Norm entrepreneurship Cina", RED),
        ],
        "body": [
            "ECFR: disimpegno USA → standard di attribuzione europei autonomi urgenti",
            "Five Eyes+ (JPN, KOR, AUS) necessario per bilanciare l'AI militare cinese",
            "Cina: formare le norme prima che si cristallizzino — finestra 2024–2027",
            "Russia + Cina: strategie diverse ma complementari — monitorare come processo coordinato",
        ],
        "visual": visual_five_eyes,
    },
    {
        "num": 10,
        "color": GOLD,
        "title": "Governance: tre modelli, nessuna supervisione adeguata",
        "subtitle": "AI Act senza applicazioni militari · CAC 2.0 senza indipendenza · Russia senza standard",
        "keywords": [
            ("AI Act: vuoto militare", GOLD), ("CAC 2.0 (Cina)", RED),
            ("AI sovrana (Russia)", PURPLE), ("Auditing tecnico indipendente", ACCENT),
        ],
        "body": [
            "UE: democrazia frammentata — supervisione parlamentare inadeguata per sistemi algoritmici",
            "Cina: 30+ misure operative (CAC 2.0) ma accountability verticale verso il Partito",
            "Russia: walled garden AI — massimo controllo narrativo, minime performance",
            "Il modello adottato dal Sud globale entro il 2030 → architettura globale 2035",
        ],
        "visual": visual_three_models,
    },
]


# ── BUILD PRESENTATION ─────────────────────────────────────────────────────────

prs = Presentation()
prs.slide_width = W
prs.slide_height = H

blank_layout = prs.slide_layouts[6]  # blank

for data in SLIDES:
    slide = prs.slides.add_slide(blank_layout)
    set_bg(slide)

    num   = data["num"]
    color = data["color"]
    num_display = "M" if num == "M" else str(num)

    # ── Top bar ──────────────────────────────────────────────────────────────
    add_top_bar(slide, num_display, data["title"], color)

    # ── Subtitle ─────────────────────────────────────────────────────────────
    add_textbox(slide, 1.05, 0.82, 7.2, 0.45,
                data["subtitle"], 13, LIGHT, italic=True)

    # ── Keyword chips (row) ───────────────────────────────────────────────────
    kx = 0.25
    ky = 1.42
    for kw_text, kw_color in data["keywords"]:
        chip_w = len(kw_text) * 0.13 + 0.4
        if kx + chip_w > 7.5:
            kx = 0.25
            ky += 0.55
        chip = add_rounded_rect(slide, kx, ky, chip_w, 0.42, kw_color)
        tf = chip.text_frame
        tf.word_wrap = False
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        run = p.add_run()
        run.text = kw_text
        run.font.size = Pt(13)
        run.font.bold = True
        run.font.color.rgb = WHITE
        kx += chip_w + 0.18

    # ── Body bullets ─────────────────────────────────────────────────────────
    panel = add_panel(slide, 0.25, 2.25, 7.1, 3.85)
    bx, by = 0.45, 2.35
    for i, line in enumerate(data["body"]):
        parts = line.split("  —  ", 1)
        if len(parts) == 2:
            label, rest = parts
            bullet = f"·  {label}  —  {rest}"
        else:
            bullet = f"·  {line}"
        add_textbox(slide, bx, by + i * 0.75, 6.75, 0.65,
                    bullet, 13.5, WHITE)

    # ── Source note ───────────────────────────────────────────────────────────
    src_map = {
        "M":  "60 fonti · 5 serie geografiche · decennio 2025–2035",
        1:    "NSCAI 2021 · CSIS/Bondar 2026 · T-invariant 2025 · PLA CMC 2020–25",
        2:    "RSIS/Raska 2025 · Belfer Center 2024 · CSIS/Bondar 2026",
        3:    "ASPI 2025 · CSET 2026 · RUSI/Wallner et al. 2025 · Europol 2025",
        4:    "Europol 2025 · RUSI 2025 · CAC/NPCSC 2025 · CICIR/MSS 2025",
        5:    "ASPI 2025 · MERICS 2025 · PLA AMS/ChatBIT 2024 · CNAS/Bendett 2024",
        6:    "ECFR 2025 · SWP 2022 · Kremlin/Putin 2025–26 · CSIS/Bondar 2026",
        7:    "NSCAI 2021 · J-AISI 2025 · ORF 2026 · Russia/National AI Strategy 2024",
        8:    "PLA CMC 2020–25 · Xinhua Institute 2025 · ICDS/Klyszcz 2026 · RUSI 2025",
        9:    "ECFR 2026 · Tsinghua CISS 2024 · RIAC/Martirosyan 2025 · IISS 2025",
        10:   "EPRS 2025 · CAC/TC260 2025 · ICDS/Klyszcz 2026 · Kremlin/Putin 2026",
    }
    add_textbox(slide, 0.25, 6.9, 7.1, 0.42,
                "Fonti: " + src_map.get(num, ""), 9, LIGHT, italic=True)

    # ── Visual ────────────────────────────────────────────────────────────────
    data["visual"](slide)

    # ── Slide number footer ───────────────────────────────────────────────────
    footer_text = f"Il futuro dei servizi di intelligence  ·  2025–2035"
    add_textbox(slide, 7.6, 7.05, 5.5, 0.38,
                footer_text, 9, LIGHT, italic=True, align=PP_ALIGN.RIGHT)


# ── SAVE ───────────────────────────────────────────────────────────────────────
out = "/Users/privato/Desktop/SEED/SEED/bozze/Il futuro dei servizi di intelligence.pptx"
prs.save(out)
print(f"Salvato: {out}")
