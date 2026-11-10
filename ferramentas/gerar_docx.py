# Gera o manuscrito em DOCX para o KDP a partir de livros/<slug>/capitulos e livros/<slug>/publicacao.
# Uso: python3 ferramentas/gerar_docx.py livros/<slug> livros/<slug>/publicacao/<arquivo>.docx
# (O título e o autor estão fixos no topo do script; ajuste para outros livros.)
import re, sys, glob, os
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

BASE = sys.argv[1]; OUT = sys.argv[2]
PUB = os.path.join(BASE, 'publicacao')
TITLE = 'Tudo Que Eu Odeio em Você'; AUTHOR = 'Lucio Costa'

doc = Document()
sec = doc.sections[0]
sec.page_width, sec.page_height = Inches(6), Inches(9)
for side in ('left_margin','right_margin'): setattr(sec, side, Inches(0.75))
sec.top_margin = sec.bottom_margin = Inches(0.8)

st = doc.styles['Normal']
st.font.name = 'Georgia'; st.font.size = Pt(11.5)
st.element.rPr.rFonts.set(qn('w:eastAsia'), 'Georgia')
pf = st.paragraph_format
pf.first_line_indent = Inches(0.3); pf.space_after = Pt(0); pf.space_before = Pt(0); pf.line_spacing = 1.2
h1 = doc.styles['Heading 1']
h1.font.name = 'Georgia'; h1.font.size = Pt(18); h1.font.bold = False; h1.font.color.rgb = None
h1.element.rPr.rFonts.set(qn('w:asciiTheme'), 'Georgia') if False else None
h1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
h1.paragraph_format.space_before = Pt(72); h1.paragraph_format.space_after = Pt(12)
h1.paragraph_format.first_line_indent = Inches(0); h1.paragraph_format.page_break_before = True
h1.paragraph_format.keep_with_next = True
# force Georgia on heading (theme fonts override otherwise)
rpr = h1.element.get_or_add_rPr(); rf = rpr.find(qn('w:rFonts'))
if rf is None: rf = OxmlElement('w:rFonts'); rpr.append(rf)
for a in ('w:ascii','w:hAnsi','w:cs','w:eastAsia'): rf.set(qn(a), 'Georgia')
for a in ('w:asciiTheme','w:hAnsiTheme','w:cstheme','w:eastAsiaTheme'):
    if rf.get(qn(a)) is not None: del rf.attrib[qn(a)]
color = rpr.find(qn('w:color'))
if color is not None: rpr.remove(color)

INLINE = re.compile(r'(\*\*[^*]+\*\*|\*[^*]+\*)')
def add_runs(p, text, italic=False):
    for part in INLINE.split(text):
        if not part: continue
        if part.startswith('**') and part.endswith('**'):
            r = p.add_run(part[2:-2]); r.bold = True; r.italic = italic
        elif part.startswith('*') and part.endswith('*') and len(part) > 2:
            r = p.add_run(part[1:-1]); r.italic = not italic
        else:
            r = p.add_run(part); r.italic = italic

def para(text='', indent=True, align=None, size=None, italic=False, space_before=0, space_after=0):
    p = doc.add_paragraph()
    p.paragraph_format.first_line_indent = Inches(0.3) if indent else Inches(0)
    if align is not None: p.alignment = align
    if space_before: p.paragraph_format.space_before = Pt(space_before)
    if space_after: p.paragraph_format.space_after = Pt(space_after)
    add_runs(p, text, italic)
    if size:
        for r in p.runs: r.font.size = Pt(size)
    return p

def page_break():
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)

bm_id = [0]
def bookmark(p, name):
    s = OxmlElement('w:bookmarkStart'); s.set(qn('w:id'), str(bm_id[0])); s.set(qn('w:name'), name)
    e = OxmlElement('w:bookmarkEnd'); e.set(qn('w:id'), str(bm_id[0])); bm_id[0] += 1
    p._p.insert(0, s); p._p.append(e)

def link(p, text, anchor):
    h = OxmlElement('w:hyperlink'); h.set(qn('w:anchor'), anchor)
    r = OxmlElement('w:r'); t = OxmlElement('w:t'); t.text = text
    t.set(qn('xml:space'), 'preserve'); r.append(t); h.append(r); p._p.append(h)

def heading(text, anchor, subtitle=None):
    # Título 1 = entrada do sumário e da navegação do Kindle. O subtítulo fica no mesmo
    # parágrafo, depois de uma quebra de linha, para aparecer junto no sumário.
    p = doc.add_paragraph(style='Heading 1'); p.add_run(text)
    if subtitle:
        r = p.add_run(); r.add_break()
        r2 = p.add_run(subtitle); r2.font.size = Pt(14); r2.italic = False
    bookmark(p, anchor); return p

def fld(p, kind, instr=None):
    r = OxmlElement('w:r')
    if instr is not None:
        t = OxmlElement('w:instrText'); t.set(qn('xml:space'), 'preserve'); t.text = instr; r.append(t)
    else:
        f = OxmlElement('w:fldChar'); f.set(qn('w:fldCharType'), kind); r.append(f)
    p._p.append(r)

from docx.enum.style import WD_STYLE_TYPE
try:
    toc1 = doc.styles['toc 1']
except KeyError:
    toc1 = doc.styles.add_style('toc 1', WD_STYLE_TYPE.PARAGRAPH)
    toc1.base_style = doc.styles['Normal']
toc1.paragraph_format.first_line_indent = Inches(0)
toc1.paragraph_format.space_after = Pt(4)

def read(name): return open(os.path.join(PUB, name), encoding='utf-8').read().strip()

# ---------- Folha de rosto ----------
para('Tudo Que Eu Odeio', indent=False, align=WD_ALIGN_PARAGRAPH.CENTER, size=26, space_before=160)
para('em Você', indent=False, align=WD_ALIGN_PARAGRAPH.CENTER, size=26)
para(AUTHOR, indent=False, align=WD_ALIGN_PARAGRAPH.CENTER, size=14, space_before=36)
page_break()

# ---------- Créditos ----------
cred = [b.strip() for b in read('creditos.md').split('\n\n')]
first = True
for block in cred:
    for line in block.split('\n'):
        p = para(line, indent=False, size=9.5, space_before=(120 if first else 0))
        first = False
    para('', indent=False)
page_break()

# ---------- Sumário ----------
chapters = sorted(glob.glob(os.path.join(BASE, 'capitulos', '*.md')))
parsed = []
for i, f in enumerate(chapters, 1):
    body = open(f, encoding='utf-8').read()
    body = re.sub(r'<!--.*?-->', '', body, flags=re.S)
    m = re.search(r'^# Capítulo (\d+) — (.+)$', body, flags=re.M)
    num, title = m.group(1), m.group(2).strip()
    rest = body[m.end():].strip('\n')
    parsed.append((int(num), title, rest))

p = para('Sumário', indent=False, align=WD_ALIGN_PARAGRAPH.CENTER, size=16, space_before=48, space_after=18)
bookmark(p, 'TOC')  # o KDP usa o marcador "TOC" para o comando "Ir para: Sumário" do Kindle

# Sumário nativo do Word (campo TOC), ligado aos parágrafos em Título 1.
# As entradas já vêm preenchidas; no Word, "Atualizar campo" regenera tudo sem quebrar.
entries = [(f'Capítulo {n} — {t}', f'_Toc{n:06d}') for n, t, _ in parsed]
entries += [('Agradecimentos', '_Toc000901'), ('Sobre o autor', '_Toc000902')]
for i, (label, anchor) in enumerate(entries):
    q = doc.add_paragraph(style='toc 1')
    if i == len(entries) - 2: q.paragraph_format.space_before = Pt(8)
    if i == 0:
        fld(q, 'begin'); fld(q, None, ' TOC \\o "1-1" \\h \\z \\n "1-1" '); fld(q, 'separate')
    link(q, label, anchor)
    if i == len(entries) - 1:
        fld(q, 'end')

# ---------- Capítulos ----------
CHAT = re.compile(r'^\*\*[^*]{1,30}:\*\*')
def write_body(rest):
    blocks = [b for b in re.split(r'\n\s*\n', rest) if b.strip()]
    after_break = True
    for b in blocks:
        b = b.strip()
        if b == '---':
            para('* * *', indent=False, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=12, space_after=12)
            after_break = True; continue
        lines = b.split('\n')
        if re.fullmatch(r'\*\*(Cecília|Vicente)\*\*', b):
            para(b.strip('*'), indent=False, align=WD_ALIGN_PARAGRAPH.CENTER, italic=True, space_after=24)
            after_break = True; continue
        for ln in lines:
            ln = ln.rstrip()
            if not ln: continue
            special = bool(CHAT.match(ln) or re.match(r'^\d+\. ', ln) or re.match(r'^[-•] ', ln))
            if re.match(r'^[-•] ', ln): ln = '• ' + ln[2:]
            if ln.isupper() and len(ln) < 60 and not ln.startswith('—'):
                para(ln, indent=False, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=6, space_after=6)
            else:
                para(ln, indent=not (after_break or special), space_after=(4 if special else 0))
            after_break = False

for num, title, rest in parsed:
    heading(f'Capítulo {num}', f'_Toc{num:06d}', subtitle=title)
    write_body(rest)

# ---------- Agradecimentos e Sobre o autor ----------
heading('Agradecimentos', '_Toc000901')
first = True
for b in read('agradecimentos.md').split('\n\n'):
    para(b.strip(), indent=not first, space_after=6); first = False
heading('Sobre o autor', '_Toc000902')
first = True
for b in read('sobre-o-autor.md').split('\n\n'):
    para(b.strip(), indent=not first, space_after=6); first = False

doc.core_properties.title = TITLE; doc.core_properties.author = AUTHOR
doc.core_properties.language = 'pt-BR'
doc.save(OUT)
print('ok', len(parsed), 'capítulos')
