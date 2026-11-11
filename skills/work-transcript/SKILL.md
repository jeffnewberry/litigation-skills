---
name: work-transcript
description: Run when the user asks for a "transcript" of a work session or chat with Claude. Builds a condensed Word document laid out like a court reporter's record, in question-and-answer form, as a record of what was asked and what Claude did.
---

# Work transcript

When the user asks for a "transcript" of a work session, build a condensed document laid out like a court reporter’s record, in question-and-answer form. It is a paper trail: what the lawyer asked, what Claude did, and where Claude got something wrong.

## Settings

Edit these before you rely on the skill.

- **Questioner:** how the lawyer appears in the transcript, for example “Ms. Rivera.” Goes in `QUESTIONER`.
- **Font:** the font for the document, for example “Times New Roman.” Goes in `FONT`. If the font is not installed where the document is opened, Word substitutes another one.

## What the layout gives

- 12-point type, 25 numbered lines per page (line numbers restart on each page).
- A boxed text area: thin oxblood rules on the top, right, and bottom, and a double rule on the left.
- Small-caps headings in oxblood, and a running header with the matter name at left and the page number at right.
- Pages, in order: a cover (“Reporter’s Record, Volume 1 of 1 Volume,” a caption block, the title between two rules, and an opening paragraph); Appearances; an Index with page numbers filled in automatically; a Preliminary Statement; the Proceedings (“CLAUDE, having been first duly prompted, testified as follows:”); an adjournment line; and a Reporter’s Certificate signed “/s/ Claude, Unofficial Court Reporter.”
- Everything left-aligned, ragged right.

This is not a court document, and the certificate says so. It is a record for the lawyer’s own file.

## Before building

Ask how many pages to condense the session to. Wait for the answer. If `QUESTIONER` is not set, ask for that too.

## Building

1. Write a content file (content.py) with these variables:
   - `PRIVILEGED` (True puts “Privileged and Confidential / Attorney Work Product” on the cover; use it for anything touching a client matter), `QUESTIONER`, `FONT`, `HEADER` (running header text), `STYLE` (a list of (left, right) caption lines), `TITLE`, `SUBTITLE`, `OPENING`, `DATE_LINE`, `APPEARANCES` (a list of line lists; *asterisks* make italics), `PRELIM` (one to two pages of paragraphs, no more), and `CERT` (certificate paragraphs).
   - `QA`: a list of entries. `('Q', text)` for the lawyer, `('A', text)` for Claude, `('X', 'ex1', '(Questioner’s Exhibit 1, …, offered.)', 'Short index description')` when the lawyer sends a file, and `('P', '(parenthetical)')` for a stage direction.
2. Condense each side’s remarks to about seven or eight lines.
3. The answers must not flatter Claude. Where Claude got something wrong, the record says so.
4. Follow the user’s house style for punctuation and quotation marks.
5. Save the script below as build_transcript.py and run `python3 build_transcript.py content.py <outfile>.docx`. It renders once with LibreOffice to fill in the index page numbers, then rebuilds. It needs LibreOffice and poppler (pdfinfo, pdftotext).
6. Render to PDF and look at the pages before sending.
7. Name the file the way the user names files.
8. When sending, tell the user to click Yes when Word asks to update fields, so the index page numbers recalculate in their font.

A sample built from a made-up session is in sample-transcript.pdf, with its content file in sample-content.py.

## Build script

```python
# -*- coding: utf-8 -*-
# Usage: python3 build_transcript.py content.py out.docx
# Builds a reporter's-record style transcript of an AI work session. Two passes: renders with LibreOffice to
# fill index page numbers, then rebuilds. Word will also refresh them (updateFields).
import re, os, sys, zipfile, subprocess, tempfile, shutil
C = {}
exec(open(sys.argv[1], encoding='utf-8').read(), C)
OUT = sys.argv[2]
FONT = C.get('FONT', 'Times New Roman'); ACC = '5A1A1A'; LINE = 518; TW = 8496
SC = '<w:smallCaps/><w:spacing w:val="40"/>'
def esc(t): return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
def runs(t, base=''):
    out = ''
    for tok in re.split(r'(\*[^*]+\*)', t):
        if not tok: continue
        rpr = base
        if tok.startswith('*') and tok.endswith('*') and len(tok) > 2:
            rpr += '<w:i/><w:iCs/>'; tok = tok[1:-1]
        out += f'<w:r>{"<w:rPr>"+rpr+"</w:rPr>" if rpr else ""}<w:t xml:space="preserve">{esc(tok)}</w:t></w:r>'
    return out
TAB = '<w:r><w:tab/></w:r>'
def p(inner='', jc=None, ind=None, tabs=None, keep=False, pb=False, extra=''):
    ppr = ('<w:keepNext/>' if keep else '') + ('<w:pageBreakBefore/>' if pb else '')
    if tabs: ppr += '<w:tabs>' + ''.join(f'<w:tab w:val="{v}" w:leader="{l}" w:pos="{pos}"/>' for v, pos, l in tabs) + '</w:tabs>'
    ppr += f'<w:spacing w:before="0" w:after="0" w:line="{LINE}" w:lineRule="exact"/>' + (ind or '') + (f'<w:jc w:val="{jc}"/>' if jc else '') + extra
    return f'<w:p><w:pPr>{ppr}</w:pPr>{inner}</w:p>'
def head(t, size=None, color=True, pb=False):
    rpr = SC + (f'<w:color w:val="{ACC}"/>' if color else '') + (f'<w:sz w:val="{size}"/><w:szCs w:val="{size}"/>' if size else '')
    return p(runs(t, rpr), jc='center', keep=True, pb=pb)
def blank(): return p('')
def rule(): return p('', ind='<w:ind w:left="1440" w:right="1440"/>', extra=f'<w:pBdr><w:bottom w:val="single" w:sz="6" w:space="1" w:color="{ACC}"/></w:pBdr>')
_bid = [100]
def bm(name, inner):
    _bid[0] += 1; i = _bid[0]
    return f'<w:bookmarkStart w:id="{i}" w:name="{name}"/>{inner}<w:bookmarkEnd w:id="{i}"/>'

def build(cache):
    def pageref(name):
        return f'<w:fldSimple w:instr=" PAGEREF {name} \\h "><w:r><w:t>{cache.get(name, "")}</w:t></w:r></w:fldSimple>'
    _bid[0] = 100
    b = []
    if C.get('PRIVILEGED'):
        b.append(p(runs('PRIVILEGED AND CONFIDENTIAL', SC + f'<w:color w:val="{ACC}"/><w:sz w:val="20"/>'), jc='center'))
        b.append(p(runs('Attorney Work Product', SC + '<w:sz w:val="20"/>'), jc='center'))
    b += [blank(), head('Reporter’s Record', size=30, color=False), head('Volume 1 of 1 Volume', color=False), blank()]
    for a, c in C['STYLE']:  # list of (left, right) caption lines; ")" column added automatically
        b.append(p(runs(a) + TAB + runs(')' if (a or c) else '') + TAB + runs(c),
                   tabs=[('left', 4320, 'none'), ('left', 4896, 'none')], ind='<w:ind w:left="288"/>'))
    b += [blank(), rule(), blank(), head(C['TITLE'], size=28), head(C['SUBTITLE'], color=False), rule(), blank()]
    b.append(p(runs(C['OPENING']), ind='<w:ind w:firstLine="720"/>'))
    b.append(p(runs('Proceedings recorded by chat log and summarized by the witness.'), ind='<w:ind w:firstLine="720"/>'))
    # Appearances
    b += [head('A p p e a r a n c e s', pb=True), blank()]
    for blk in C['APPEARANCES']:
        for l in blk: b.append(p(runs(l), ind='<w:ind w:left="720"/>'))
        b.append(blank())
    # Index
    b += [head('I n d e x', pb=True), p(runs('Volume 1', SC), jc='center'), blank()]
    b.append(p(runs(C['DATE_LINE']) + TAB + runs('Page'), tabs=[('right', TW, 'none')]))
    for label, name in [('Preliminary Statement', 'bm_prelim'), ('Examination by ' + C['QUESTIONER'], 'bm_exam'),
                        ('Adjournment', 'bm_adj'), ('Reporter’s Certificate', 'bm_cert')]:
        b.append(p(runs(label) + TAB + pageref(name), tabs=[('right', TW, 'dot')], ind='<w:ind w:left="720"/>'))
    ex = [x for x in C['QA'] if x[0] == 'X']
    if ex:
        b += [blank(), p(runs('Questioner’s Exhibits', SC), jc='center', keep=True)]
        b.append(p(runs('No.') + TAB + runs('Description') + TAB + runs('Offered'), tabs=[('left', 720, 'none'), ('right', TW, 'none')]))
        for i, x in enumerate(ex, 1):
            b.append(p(runs(str(i)) + TAB + runs(x[3]) + TAB + pageref('bm_' + x[1]), tabs=[('left', 720, 'none'), ('right', TW, 'dot')]))
    # Preliminary statement
    b.append(p(bm('bm_prelim', runs('Preliminary Statement', SC + f'<w:color w:val="{ACC}"/>')), jc='center', pb=True, keep=True))
    b.append(blank())
    for para in C['PRELIM']: b.append(p(runs(para), ind='<w:ind w:firstLine="720"/>'))
    # Proceedings
    b.append(p(runs('P r o c e e d i n g s', SC + f'<w:color w:val="{ACC}"/>'), jc='center', pb=True, keep=True))
    b.append(blank())
    b.append(p(runs('CLAUDE,', SC + '<w:b/>'), ind='<w:ind w:left="720"/>', keep=True))
    b.append(p(runs('having been first duly prompted, testified as follows:'), ind='<w:ind w:left="720"/>', keep=True))
    b.append(p(bm('bm_exam', runs('Examination', SC + '<w:b/>')), jc='center', keep=True))
    b.append(p(runs('By ' + C['QUESTIONER'] + ':', SC), keep=True))
    for x in C['QA']:
        if x[0] in ('Q', 'A'):
            b.append(p(f'<w:r><w:t xml:space="preserve">{x[0]}.</w:t></w:r>' + TAB + runs(x[1]),
                       tabs=[('left', 1440, 'none')], ind='<w:ind w:firstLine="720"/>'))
        elif x[0] == 'X':
            b.append(p(bm('bm_' + x[1], runs(x[2])), ind='<w:ind w:left="1440"/>'))
        elif x[0] == 'P':
            b.append(p(runs(x[1]), ind='<w:ind w:left="1440"/>'))
    b.append(p(bm('bm_adj', runs('(Whereupon, the witness prepared this transcript, and the proceedings were concluded.)')), ind='<w:ind w:left="1440"/>'))
    # Certificate
    b.append(p(bm('bm_cert', runs('Reporter’s Certificate', SC + f'<w:color w:val="{ACC}"/>')), jc='center', pb=True, keep=True))
    b += [blank(), p(runs('IN THE CHAT WINDOW')), blank()]
    for c in C['CERT']: b.append(p(runs(c), ind='<w:ind w:firstLine="720"/>'))
    b.append(blank())
    for l in ['/s/ Claude', 'Claude, Unofficial Court Reporter', 'An AI model made by Anthropic', 'No CSR Number']:
        b.append(p(runs(l), ind='<w:ind w:left="4320"/>'))
    sect = ('<w:sectPr><w:headerReference w:type="default" r:id="rIdH"/><w:pgSz w:w="12240" w:h="15840"/>'
            '<w:pgMar w:top="1728" w:right="1440" w:bottom="1152" w:left="2304" w:header="864" w:footer="576" w:gutter="0"/>'
            f'<w:pgBorders w:offsetFrom="text"><w:top w:val="single" w:sz="6" w:space="8" w:color="{ACC}"/><w:left w:val="double" w:sz="4" w:space="10" w:color="{ACC}"/><w:bottom w:val="single" w:sz="6" w:space="8" w:color="{ACC}"/><w:right w:val="single" w:sz="6" w:space="10" w:color="{ACC}"/></w:pgBorders>'
            '<w:lnNumType w:countBy="1" w:distance="576" w:restart="newPage"/><w:cols w:space="720"/></w:sectPr>')
    NS = 'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"'
    doc = f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:document {NS}><w:body>{"".join(b)}{sect}</w:body></w:document>'
    header = (f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:hdr {NS}><w:p><w:pPr><w:tabs><w:tab w:val="right" w:pos="{TW}"/></w:tabs>'
              '<w:spacing w:after="0" w:line="240" w:lineRule="auto"/><w:suppressLineNumbers/></w:pPr>'
              f'<w:r><w:rPr>{SC}<w:color w:val="{ACC}"/><w:sz w:val="18"/></w:rPr><w:t>{esc(C["HEADER"])}</w:t></w:r><w:r><w:tab/></w:r>'
              '<w:fldSimple w:instr=" PAGE "><w:r><w:t>1</w:t></w:r></w:fldSimple></w:p></w:hdr>')
    styles = (f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:styles {NS}><w:docDefaults><w:rPrDefault><w:rPr>'
              f'<w:rFonts w:ascii="{FONT}" w:hAnsi="{FONT}" w:cs="{FONT}" w:eastAsia="{FONT}"/><w:sz w:val="24"/><w:szCs w:val="24"/><w:lang w:val="en-US"/></w:rPr></w:rPrDefault>'
              f'<w:pPrDefault><w:pPr><w:spacing w:after="0" w:line="{LINE}" w:lineRule="exact"/></w:pPr></w:pPrDefault></w:docDefaults>'
              '<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/><w:qFormat/></w:style>'
              '<w:style w:type="character" w:default="1" w:styleId="DefaultParagraphFont"><w:name w:val="Default Paragraph Font"/></w:style>'
              '<w:style w:type="character" w:styleId="LineNumber"><w:name w:val="line number"/><w:basedOn w:val="DefaultParagraphFont"/><w:rPr><w:color w:val="7F7F7F"/><w:sz w:val="20"/></w:rPr></w:style></w:styles>')
    settings = (f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:settings {NS}><w:updateFields w:val="true"/><w:defaultTabStop w:val="720"/>'
                '<w:compat><w:compatSetting w:name="compatibilityMode" w:uri="http://schemas.microsoft.com/office/word" w:val="15"/></w:compat></w:settings>')
    R = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships/'
    ct = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
          '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/>'
          '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
          '<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>'
          '<Override PartName="/word/settings.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.settings+xml"/>'
          '<Override PartName="/word/header1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.header+xml"/>'
          '<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/></Types>')
    rels = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Id="rId1" Type="' + R + 'officeDocument" Target="word/document.xml"/>'
            '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/></Relationships>')
    drels = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
             f'<Relationship Id="rIdS" Type="{R}styles" Target="styles.xml"/><Relationship Id="rIdT" Type="{R}settings" Target="settings.xml"/>'
             f'<Relationship Id="rIdH" Type="{R}header" Target="header1.xml"/></Relationships>')
    core = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/">'
            f'<dc:title>{esc(C["TITLE"])}</dc:title><dc:creator>Claude</dc:creator></cp:coreProperties>')
    with zipfile.ZipFile(OUT, 'w', zipfile.ZIP_DEFLATED) as z:
        for n, d in [('[Content_Types].xml', ct), ('_rels/.rels', rels), ('docProps/core.xml', core), ('word/document.xml', doc),
                     ('word/styles.xml', styles), ('word/settings.xml', settings), ('word/header1.xml', header), ('word/_rels/document.xml.rels', drels)]:
            z.writestr(n, d)

build({})
# Pass 2: find each bookmark's page by rendering and searching for its text
tmp = tempfile.mkdtemp()
subprocess.run(['soffice', '--headless', '--convert-to', 'pdf', OUT, '--outdir', tmp], capture_output=True)
pdf = os.path.join(tmp, os.path.splitext(os.path.basename(OUT))[0] + '.pdf')
cache = {}
if os.path.exists(pdf):
    n = int(re.search(r'Pages:\s+(\d+)', subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout).group(1))
    pages = [subprocess.run(['pdftotext', '-f', str(i), '-l', str(i), pdf, '-'], capture_output=True, text=True).stdout for i in range(1, n + 1)]
    def find(s, start=3):
        k = re.sub(r'\s+', ' ', s)[:40]
        for i in range(start, n):
            if k in re.sub(r'\s+', ' ', pages[i]): return str(i + 1)
        return ''
    cache['bm_prelim'] = find(C['PRELIM'][0])
    cache['bm_exam'] = find('having been first duly prompted')
    cache['bm_adj'] = find('(Whereupon, the witness')
    cache['bm_cert'] = find('IN THE CHAT WINDOW', 4)
    for x in C['QA']:
        if x[0] == 'X': cache['bm_' + x[1]] = find(x[2])
build(cache)
shutil.rmtree(tmp, ignore_errors=True)
print('ok', cache)
```
