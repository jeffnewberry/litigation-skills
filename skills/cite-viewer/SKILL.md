---
name: cite-viewer
description: "Run when the user says “cite viewer,” “viewer,” or “build the viewer”: a local click-through page where each citation in a draft opens the cited passage from the Westlaw source, with a status showing whether the passage supports the sentence."
---

# Cite viewer

The cite viewer is a local HTML page showing the user’s draft (or one section of it). Every citation is a link, underlined in a color for its status. Clicking a citation shows the cited star page from the Westlaw PDF, with the quoted or relied-on language shaded, plus a link that opens the full PDF at that page. The viewer does not replace reading the cases. It makes the reading fast, and it records whether each passage supports the sentence that cites it.

**Requirements.** A Westlaw subscription with Find & Print, a computer (not a phone or tablet) where the PDFs can be saved, and a Claude setup that can use a browser and read files on that computer. The optional docket section uses Bloomberg Law.

## Settings (edit these for your practice)

- **Font for the page:** the user’s brief font first in the font list, then a standard serif fallback. Default: Georgia, serif.
- **Folder name pattern:** default `client-matter-cite-viewer-scope.YYYYMMDD`.
- **Cite-checking tool:** whatever the user runs before the viewer (for example, CoCounsel, KeyCite, or Shepard’s). Default: none named.
- **Westlaw client ID:** if Westlaw asks for one, use the ID the user gives; never invent one.

## Where it sits in the drafting process

1. Co-counsel comments are in, and the text is settled.
2. The user runs a citator (KeyCite or Shepard’s) and any cite-checking tool.
3. The user and Claude discuss that report, and Claude makes only the changes the user approves.
4. **Cite viewer**, built on the revised draft. Tag any citations the cite-checking tool flagged as unsupported that are still disputed; the user reads those first.
5. The user reads every citation, and they fix what the viewer flags.
6. Quick re-check of only the citations changed in step 5.
7. Final formatting.

If the user asks for the viewer before steps 2 and 3, say in one line that it works best after them, then build it if they want it anyway.

## Before starting

Ask, at the top and in one short block:
- Which draft, if the user has not attached or named it. Use the version revised after the cite-check discussion.
- Scope: the whole document, or named claims or sections.
- Whether any cite-checker “does not support” flags are still disputed, and which ones.
- If the draft leans on docket or record cites (ECF entries, orders, judgments, mandates), offer to pull them from Bloomberg Law (step 3A).

Asking for the viewer is the go-ahead to run Find & Print, download the ZIP, and save the viewer folder. Never change the draft itself without a separate go-ahead.

## Steps

### 1. Build the cite table
Convert the draft to text (pandoc, or a Word-reading skill). Walk the scope in order and list every citation: full cites, short cites, *id.*, *supra*, statutes, secondary sources, and record cites (R.R., C.R., exhibits, ECF entries). For each one, record:
- the id (c1, c2, and so on), and the citation exactly as written;
- the authority it resolves to (resolve *id.* and short cites to the full authority);
- the pincite or pincites;
- the proposition, and any quoted language, from the sentence it supports;
- whether the cite refers to specific material in the source (a holding, a test, a quotation) or only names the case as a whole (see step 6);
- whether the cite-checking tool flagged it.

Note any legal statement in the scope that has no citation. The page marks these too.

### 2. Build the Find & Print list
Use one entry per authority: the reporter citation (“466 U.S. 668”), the WL citation for unpublished opinions, the code and section for statutes, and “volume abbreviation first-page” for articles. Separate entries with semicolons, up to 100.

Leave out record cites, books, reports, and anything else Westlaw does not carry. List them for the report. If a docket-style cite (“Order, No. [docket no.] ([Court] [Date])”) turns out to be reported (an F. App’x cite in a later order, for example), add the reporter cite to the list and flag the form in step 6.

If the draft uses a short cite or *supra* with no full cite anywhere, or a full cite missing its volume, do not guess silently. Either supply the cite and label it “general knowledge, unverified,” or leave it out and flag it.

### 3. Run Find & Print
- Have the user sign in to Westlaw. Claude never enters passwords.
- If Westlaw opens on a “Select a client ID” screen, use the client ID the user gives (see Settings), then start a new session and go to Find & Print.
- Open Find & Print and paste the list. Confirm the box actually holds the text (read the textarea value); typing can be lost if the page re-renders.
- Settings: Cases → “Case opinion only (excludes Headnotes)”; Statutes → “Statutory text only”; leave “Substitute with reporter images” unchecked, because the star paging must be text; KeyCite → uncheck all three, including “List of the first 500 Citing References,” which can be on by default; Delivery → Download; Format → PDF; As → Multiple files (ZIP); Layout and limits → turn off “Dual column layout for Cases.”
- Submit. If Westlaw shows an “Invalid Citations” box, take those citations out of the list and continue. Report them and try them later by title. Social-science journals are often not on Westlaw.
- Wait for “The items are ready to download,” then click Westlaw’s Download button. The browser may show its own save window, which Claude cannot press. Tell the user it is coming and ask them to click Save.
- Find & Print requests are charged according to the user’s Westlaw plan. Mention that once in the report, not every time.

Westlaw’s screens and labels change. If a setting named here is missing or renamed, stop and describe what the page shows rather than guessing.

### 3A. Docket and record documents from Bloomberg Law (optional)
- Have the user sign in to Bloomberg Law.
- Find the docket through Bloomberg’s search box (docket number plus party name).
- Read the docket entries’ text with JavaScript over the table rows. Entries marked **View** are already on Bloomberg. Entries marked **Request** must be retrieved, which may carry a charge: never click Request. List those entries for the user and let them decide.
- To read a View document, fetch `/product/blaw/document/<ID>/download` inside the page and extract its text with the page’s own `pdfjsLib`. Scanned orders return only the header stamps; for those, render the pages to canvas with pdfjsLib in an overlay, take a screenshot, and read it.
- Saving Bloomberg PDFs to the computer is unreliable: a blob-link download from JavaScript does not land, and a native download waits on a save window. Ask the user to click Save if a window appears. If the file does not arrive, link that excerpt to the Bloomberg document URL (“Open on Bloomberg Law”) instead of a local file, and say so in the report.
- Fifth Circuit mandate packets usually hold the opinion or order, the judgment, and the clerk’s transmittal letter together. Check the file stamp on the judgment against the date the draft gives it: the judgment is often filed with the opinion and only issued as the mandate later.

### 4. Get the PDFs
Find the newest “Westlaw … items from Find And Print.zip” in the user’s downloads and unzip it into a working folder. The files are numbered in the order of the list (“01 - Strickland v Washington.pdf”). With only one or two citations, Westlaw may instead deliver separate PDFs; pick those up the same way. Match each one to its authority, and flag any that did not come back.

### 5. Pull the cited passages
Westlaw PDFs mark star pages in the text: \*688 for the primary reporter, \*\*2055 and \*\*\*… for parallel reporters, and \*1, \*2 for WL cites. Strip the parallel markers, split the text on the single-star markers, and take each pinned page’s text. Also take the last few hundred characters of the page before it, so a sentence that begins on the earlier page reads whole. A one-page memorandum opinion has no star markers; take its text directly.

Find the PDF page (the physical page) where each star marker appears, so the “open full source” link can use #page=N. Strip the Westlaw page headers and footers.

Use the script at the end of this file. When a pin is not a star page (law-review page numbers in some PDFs, or statute subsections), find the passage by searching for the quoted or relied-on language instead. For docket documents, use the document’s own page numbers.

### 6. Check each citation
Read each pinned passage against the sentence it supports. Assign one status:
- **ok — Supported.** The passage says what the sentence says. Any quotation matches exactly, or the brackets account for every change. Also use ok, with no excerpt, for a cite that only names the case as a whole (for example, a case named in a textual sentence as the governing standard, without relying on any particular passage). A citation sentence or clause that supports a proposition always relies on specific material and needs a pin, even when it cites several cases at once. Its note reads “Names the case as a whole; no pin needed.”
- **check — Check.** The quotation does not match, the passage supports only part of the sentence, the pin is wrong, the cite form is wrong in a way that matters (a docket cite to a reported opinion, a judgment given the wrong date or label), or the sentence describes the source inaccurately. Say exactly what is off, and give the fix (the right pin, the right cite, or the bracketed correction).
- **pin — No pincite.** A cite to specific material (a holding, a test, a quotation) with no pin. Show the page that the nearby text relies on. Never use this status for a cite that only names the case as a whole. When it is unclear whether a sentence relies on specific material, use check and say so in the note, so the user decides.
- **none — Source not loaded.** Record cites, books, Bloomberg “Request” entries, and anything missing from the ZIP. Name what the user would need to add. When another loaded source corroborates the point (a later order describing an earlier one), show that passage, labeled “corroboration only.”
- **flagged.** Add a “cite-checker flagged” tag on top of the status for disputed cites.

Notes say only what the passage in the PDF says, and put “Inference:” before anything beyond it. Flag substantive problems only: a misquotation, a wrong pin, a holding that is overstated or mischaracterized. Ignore pure typos and stray punctuation. Shade the exact relied-on words in each excerpt.

### 7. Build the page
Save everything in one folder on the user’s computer, named with the folder pattern in Settings. It holds:
- the HTML file, with the same name plus .html;
- a sources/ folder with all the PDFs (Westlaw and any saved docket documents), renamed in lowercase-hyphenated form, which later sections can reuse.

Page rules:
- The draft goes on the left, the passage panel on the right; on a narrow screen they stack.
- A legend at the top gives the count for each status, plus “Dotted red text = legal statement with no citation.”
- Show the draft text exactly as written. The viewer reports problems; it never fixes them in the text.
- Shade passages light blue. Left-aligned text, serif font, using the font in Settings.
- Make the page work in both light and dark mode.
- Clicking a citation shows: the status badge, the citation as written, the note, and then each pinned excerpt with a header giving the page in both numberings (“466 U.S. at 694 · PDF page 7”) and the link “Open full source at \*N ↗” (sources/FILE#page=N), or “Open on Bloomberg Law ↗” for a docket document that is not saved locally.

**Never publish the viewer as an artifact or host it anywhere.** It holds the client’s pleading, and with record cites it would hold record material. It stays on the user’s computer. If the user asks to publish it anyway, urge caution about client confidentiality, and leave record excerpts out of any hosted version.

### 8. Check the page
Open the HTML in a browser (Playwright, or the user’s browser). Click at least one citation of each status and take a screenshot. Confirm that the excerpts show the shaded language and that the note sits at the top of the panel.

### 9. Report
Keep it short, strongest point first:
- Where the folder is, in plain words, and that the user opens it by double-clicking the HTML file.
- The counts by status.
- Each “check” item in one or two lines, with its fix.
- The “no pincite” cites, uncited statements, and sources not loaded, rejected by Find & Print, or left as Bloomberg Requests.
- One next step: fix what the viewer flagged, re-check only the changed cites, then finish formatting.

## Scripts

star_extract.py: given a PDF and a list of star pages, it returns each page’s text, the tail of the page before it, and the PDF page where each marker appears. It needs poppler-utils (pdfinfo and pdftotext).

```python
import re, subprocess, sys, json

def pdf_pages(pdf):
    info = subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout
    n = int(re.search(r'Pages:\s+(\d+)', info).group(1))
    return [subprocess.run(['pdftotext', '-f', str(i), '-l', str(i), pdf, '-'],
                           capture_output=True, text=True).stdout for i in range(1, n + 1)]

# Westlaw prints a running header on each page that begins "WESTLAW ©" and ends
# with the case name and year in parentheses. The account holder's name and the
# "For Educational Use Only" line vary by subscription, so the pattern allows both.
HEADER = re.compile(
    r'WESTLAW\s*©.*?Works\.\s*\d+\s*(?:[^\n]*?\d{1,2}/\d{1,2}/\d{2,4}\s*)?'
    r'(?:For Educational Use Only\s*)?[^\n]*?\(\d{4}\)\s*[^\n]*\n', re.S)

def clean(t):
    t = HEADER.sub('', t)
    t = re.sub(r'\*\*\*?\d+\s?', '', t)          # drop parallel-reporter markers
    t = re.sub(r'-\n(?=[a-z])', '', t)
    return re.sub(r'\s+', ' ', t)

def segments(pages):
    parts = re.split(r'(?<![\*\w])\*(\d+)\s', clean('\f'.join(pages)))
    seg, cur = {}, 'pre'
    for i, p in enumerate(parts):
        if i % 2: cur = p
        else: seg[cur] = seg.get(cur, '') + p
    return seg

def physical_page(pages, star):
    for i, p in enumerate(pages, 1):
        if re.search(r'(?<![\*\w])\*' + star + r'\s', p):
            return i
    return 1

if __name__ == '__main__':
    pdf, stars = sys.argv[1], sys.argv[2].split(',')
    pages = pdf_pages(pdf); seg = segments(pages)
    out = {s: {'prev_tail': seg.get(str(int(s) - 1), '')[-450:],
               'text': seg.get(s, ''),
               'pdf_page': physical_page(pages, s)} for s in stars}
    print(json.dumps(out))
```

Run scripts that read the downloaded PDFs with `python3 -I`, from a folder separate from the PDFs.

Page structure: one self-contained HTML file. The draft text goes in `<article id="draft">`, with each citation as `<a href="#" class="cite" data-id="cN">…</a>` and each uncited legal statement as `<span class="uncited">…</span>`. The panel goes in `<aside id="panel">`. A JSON object embedded in a script maps each id to `{cite, status, note, excerpts: [{label, file, page, star, html}]}`, where html is the escaped excerpt with the relied-on words in `<mark>`, and file is a sources/ path or a Bloomberg URL. The script sets `data-s=status` on each link, which colors its underline (ok green, check red, pin amber, none gray dashed). On click, it fills the panel and scrolls the panel to the top.
