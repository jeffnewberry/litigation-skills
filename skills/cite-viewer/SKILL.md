---
name: "cite-viewer"
description: "Run when the user says \"cite viewer\" or \"build the viewer\": a local click-through page where each citation in a draft opens the cited passage from the source, with optional links to the record."
---

# Cite viewer

The cite viewer is a local web page showing the user's draft (or one section of it). Every citation is a link, underlined in a color for its status. Clicking a citation shows the cited page from the source, with the quoted or relied-on language shaded, a note on whether the passage supports the sentence, a link that opens the full source at that page, and a note box where the user can type a fix.

The viewer does not replace reading the cases, and it does not replace a citator (KeyCite or Shepard's). It makes the reading fast, and it records whether each passage supports the sentence that cites it.

## Two rules that never change

- **Never publish the viewer or host it anywhere.** It holds the user's draft, and with record links it points to record material. It stays on the user's computer as a file they open by double-clicking. Never offer to turn it into a shareable link. If the user asks to publish it anyway, warn them about client confidentiality first.
- **Never change the draft.** The viewer reports problems; it does not fix them. Change the draft only when the user separately asks.

## Where it fits

It works best on a draft whose text is settled and whose citations have already been through a cite-check and a citator, and before the final proofread. If the user asks for it earlier, say so in one line, then build it if they want it anyway.

## Before starting

Ask, in one short block, only what the user has not already said:
1. Which draft. Ask them to attach it, or to name the file.
2. Scope: the whole document, or named sections. Ask this even when the draft is short; never decide the scope yourself.
3. Sources: "Should I pull the cases from Westlaw for you, or will you put the PDFs in a folder yourself?" (Westlaw users: see step 3. Lexis or other users: step 3a.)
4. Record cites: "Do you want record cites linked too? If so, which folder on your computer holds the record, and how do you cite it? Give me one example cite from your draft (for example, 12 R.R. 41, ROA.1234, Dkt. 52 at 3, or JA 123)." Any folder works (Dropbox, OneDrive, or a plain folder), because the viewer links the files where they sit and copies nothing. If the user says no, record cites show as "Source not loaded."

Asking for the viewer is the go-ahead to pull the sources and save the viewer folder.

## Steps

### 1. Build the cite table
Convert the draft to text. Walk the scope in order and list every citation: full cites, short cites, *id.*, *supra*, statutes, secondary sources, and record cites. For each one, record:
- an id (c1, c2, and so on), and the citation exactly as written;
- the authority it resolves to (resolve *id.* and short cites to the full authority);
- the pincite or pincites;
- the proposition, and any quoted language, from the sentence it supports;
- whether the cite relies on specific material in the source (a holding, a test, a quotation) or only names the case as a whole (see step 6).

Note any legal statement in the scope that has no citation. The page marks these too.

If the draft uses a short cite or *supra* with no full cite anywhere, do not guess silently. Either supply the cite and label it "general knowledge, unverified," or leave it out and flag it.

### 2. Build the source list
One entry per authority: the reporter citation ("466 U.S. 668"), the WL citation for unpublished opinions, the code and section for statutes, and "volume abbreviation first-page" for articles. Separate entries with semicolons, up to 100. Leave out record cites and anything Westlaw does not carry; list them for the report.

### 3. Pull the sources from Westlaw (Find & Print)
- Open Westlaw in the browser and ask the user to sign in the way they usually do: a firm sign-on, a law school portal, or a Thomson Reuters ID. Tell them that if the page you opened is not the one they normally use, they can go to their usual sign-in page in the same browser window. Never enter passwords; once they are signed in, do the rest.
- Go to Find & Print and paste the list.
- Settings: Cases → opinion only (no headnotes); Statutes → statutory text only; leave "Substitute with reporter images" unchecked, because the star paging must be text; Delivery → Download; Format → PDF; As → Multiple files (ZIP); turn off dual-column layout.
- Submit. If Westlaw rejects some citations, take them out, continue, and report them.
- When the download is ready, click Westlaw's Download button. The browser then shows its own save window, which you cannot press. Tell the user it is coming and ask them to click Save (or Download) in that window. The ZIP lands in their Downloads folder.
- Tell the user once that Find & Print requests may be charged under their Westlaw plan.

### 3a. Sources the user supplies
Ask the user to put one PDF per authority in a folder and tell you which folder. Text PDFs only; if a PDF is a scan with no text, ask for a text version.

### 4. Get the PDFs
Ask for access to the folder where the download landed (or the folder from 3a). Unzip into a working folder outside the downloads folder. Match each PDF to its authority, and flag any that did not come back.

### 5. Pull the cited passages
Westlaw PDFs mark star pages in the text: \*688 for the primary reporter, \*\*2055 and \*\*\* for parallel reporters, and \*1, \*2 for WL cites. Strip the parallel markers, split the text on the single-star markers, and take each pinned page's text, plus the last few hundred characters of the page before it, so a sentence that starts on the earlier page reads whole. Find the PDF page where each marker appears, for the "open full source" link (#page=N). Strip page headers and footers. Use the script at the end of this file. When a pin is not a star page (law-review pages, statute subsections, or PDFs from another service), find the passage by searching for the quoted or relied-on language.

### 5a. Record cites (only if the user chose them)
- From the user's example cite, work out which part of a cite names the file (a volume, a document or docket number, an appendix) and which number names the page (a printed transcript page, a stamped record page such as ROA.1234, a court's header page, or an appendix page). The record may be one file or many.
- List the record files in the user's folder and match each cite to its file (for example, "Vol. 39" or "RR39" to 39 R.R.; "ECF 52" to Dkt. 52; one consecutively stamped record for ROA cites). If the matching is unclear, show the user your mapping and ask before going on.
- Read only the cited pages. Find each cited page by the number the cite uses, as it appears on the page itself, never by the PDF page count; the two rarely match. When a page carries two numbers (a court's header page and the document's own page, say), and the user's example does not settle which the cite means, ask. If you cannot find the number, mark the cite "check" and say so.
- For each record cite, record both numbers: the page number the cite uses and the PDF page it falls on.
- Link each record cite to the file where it sits, with a relative link from the viewer's HTML file to the record file on the user's computer, at the PDF page. For example, when the viewer folder and the record both sit in Downloads: ../volume.pdf#page=N. Build the link from the real paths on the user's computer (as the folder listing shows them), never from paths in your own workspace. Do not use full file:/// addresses; browsers often refuse them. Copy nothing into the viewer folder.
- The record must be text-searchable PDFs on the user's computer. A file stored only online (a cloud file not downloaded, or a document vault reached through a website) cannot be linked; tell the user which ones.

### 6. Check each citation
Read each passage against the sentence it supports. Assign one status:
- **ok — Supported.** The passage says what the sentence says. Any quotation matches exactly, or brackets account for every change. Use ok, with no excerpt, only for a cite that names a case as a whole in a textual sentence, as part of the sentence itself, without relying on any particular passage (Bluebook R. 3.2(a)). A citation sentence or clause that supports a proposition always relies on specific material and needs a pin, even when it cites several cases at once. A whole-case cite's note reads "Names the case as a whole; no pin needed (Bluebook R. 3.2(a))."
- **check — Check.** The quotation does not match, the passage supports only part of the sentence, the pin is wrong, or the sentence describes the source inaccurately. Say exactly what is off, and give the fix (the right pin, or the bracketed correction).
- **pin — No pincite.** A cite to specific material with no pin. Show the page the nearby text relies on. When it is unclear whether the sentence relies on specific material, use check and say so, so the user decides.
- **none — Source not loaded.** Anything not in the PDFs or the record folder. Name what the user would need to add.

Notes say only what the source says. Put "Inference:" before anything beyond it. Flag substantive problems only: a misquotation, a wrong pin, a holding overstated or mischaracterized, a fact the record page does not support. Ignore pure typos. Shade the exact relied-on words in each excerpt.

### 7. Build the page
Save a folder in the user's Downloads folder (or wherever they ask), named for the draft plus "cite-viewer" and the date. It holds:
- the HTML file;
- a sources/ folder with the case PDFs. (Record files stay where they are.)

Page rules:
- Draft on the left, passage panel on the right; on a narrow screen they stack.
- A legend at the top gives the count for each status, plus "Dotted red text = legal statement with no citation."
- Show the draft text exactly as written.
- Shade passages light blue. Left-aligned text, serif font.
- Works in light and dark mode.
- Clicking a citation shows the status badge, the citation as written, the note, each excerpt with its page header and an "Open full source ↗" link, and then the note box.
- Every excerpt header names the page in both numberings, so the user can confirm the page without opening the file: for a case, "466 U.S. at 694 · PDF page 7"; for the record, "12 R.R. 45 · PDF page 10."
- Uncited legal statements are clickable too. Clicking one shows a "No citation" badge, the statement as written, a one-line note (for example, "States a legal rule; add a cite or cut it"), and the note box.

**Note box.** Under every flag's panel (citations and uncited statements alike), a text box labeled "Your note (for example, the fix you want)." Notes save automatically in the browser for this file. Wrap every save and load in try/catch, so the page still works if the browser blocks storage. A flag with a note gets a small dot in the draft. A "Copy all notes" button at the top copies every note as a numbered list in draft order, each line starting with the citation as written (or "Uncited:" and the first words of the statement), so the user can paste the list into Claude or keep it beside Word. Tell the user once that notes live only in that browser on that computer; the copied list is the safe copy.

### 8. Check the page
Open the page and click at least one citation of each status, and one uncited statement. Confirm that the excerpts show the shaded language and both page numbers, the note sits at the top of the panel, every flag has a note box, and "Copy all notes" works.

Record links need a separate check, because you cannot click a link on the user's computer. For each record link, work out where it points from the viewer's HTML file on the user's computer and confirm, by listing that folder, that the file is there. Then ask the user to click one record link and tell you whether it opened at the right page. Until they confirm, do not report the record links as working; report them as "linked, not yet confirmed."

### 9. Report
Short, strongest point first:
- Where the folder is, and how to open the viewer: "Open the viewer in Google Chrome (right-click the HTML file, choose Open With, then Google Chrome). We have tested it on a Mac with Chrome, and it works there. Safari blocks the record links. We have tested record links with Texas-style record cites (12 R.R. 41) but not yet with other formats. We have not tested it on a Windows PC. Chrome should work there too, and Microsoft Edge may, but we have not tried either."
- Counts by status.
- Each "check" item in one or two lines, with its fix.
- The "no pincite" cites, uncited statements, sources not loaded or rejected, and any record files that could not be linked.
- Whether the record links are confirmed (see step 8).
- Two ways to work through it: talk through each flag with Claude, which keeps a list and makes the changes after the user approves them; or work in Word with the viewer open beside it, typing fixes in the note boxes. Say that "Copy all notes" is a button in the viewer that only the user can press, and that they can paste the copied list back into this chat.

## Script

star_extract.py: given a PDF and a list of star pages, it returns each page's text, the tail of the page before it, and the PDF page where each marker appears.

```python
import re, subprocess, sys, json

def pdf_pages(pdf):
    info = subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout
    n = int(re.search(r'Pages:\s+(\d+)', info).group(1))
    return [subprocess.run(['pdftotext', '-f', str(i), '-l', str(i), pdf, '-'],
                           capture_output=True, text=True).stdout for i in range(1, n + 1)]

def clean(t):
    t = re.sub(r'WESTLAW\s*©.*?For Educational Use Only[^\n]*\n', '', t, flags=re.S)
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

Run scripts that read downloaded PDFs with python3 -I, from a folder separate from the PDFs.

Page structure: one self-contained HTML file. The draft goes in <article id="draft">, each citation as <a href="#" class="cite" data-id="cN">…</a> and each uncited legal statement as <span class="uncited">…</span>. The panel goes in <aside id="panel">. Each uncited statement is <span class="uncited" data-id="uN" tabindex="0">…</span>. A JSON object in a script maps each id to {cite, status, note, link, excerpts: [{label, html, pdfpage}]}, where label carries both page numbers, html is the escaped excerpt with the relied-on words in <mark>, and link is sources/FILE or the record file's relative path (for example, ../volume.pdf). The script sets data-s=status on each link (ok green, check red, pin amber, none gray dashed). On click, it fills the panel, loads that citation's saved note, and scrolls the panel to the top.
