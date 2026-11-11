---
name: final-filing-check
description: Run when the user says "final check," "finish this for filing," or asks to get a finished court document ready to file. Runs the finishing checks on layout, tables, word count, and a clean file, then gives a short report.
---

# Final filing check

These are the last checks on a court document after the writing is done and before it is filed. They catch the small things that make a filing look careless: a heading stranded at the bottom of a page, a signature block split in two, a stale word count, or a reviewer’s comment left in the file.

## Settings

Edit these to match your own practice before you rely on the skill.

- **Font and size:** the font and size you file in.
- **Table layout:** how your table of contents and index of authorities are laid out. If you leave this blank, Claude follows the layout of the last filing you give it, not Word’s defaults.
- **Entry wrapping:** for example, entries wrap with a 0.5" right indent, with page numbers on a dot leader at the right margin.
- **Sub-headings:** for example, each level indents 0.5" further than the one above it.

## Scope

The checks apply to the main document only. Appendices, exhibits, and companion motions are separate documents. Step 1 checks that the main document’s references match the appendix or exhibit list, but this skill does not build or format the appendix itself.

## Steps

1. **Appendix and exhibit references.** Check every reference to an appendix or exhibit against the list the user settled before this check. Flag any letter or number cited but not on the list, any item on the list that is never cited, and, where no court rule sets the order, any item out of order by first citation. Do not re-letter or renumber without the user’s approval. If there is no list yet, stop and ask for it before going on.
2. **Headings.** No heading may be the last thing on a page. Move it to the next page, even if that leaves white space.
3. **Blank pages and the signature block.** After step 2, check for blank pages, and make sure the signature block is not split across pages or alone at the top of one.
4. **Tables.** No entry in the table of contents or the index of authorities may be split across pages.
5. **Table layout.** The table of contents and index of authorities follow the layout in Settings.
6. **Sub-headings.** Sub-headings are indented as Settings says.
7. **Page numbers last.** Fill in the table and index page numbers last, after everything else has settled. If Claude cannot lay the document out in the user’s own copy of Word with the user’s font, it says so and flags the page numbers for the user to confirm.
8. **Word count.** Update the word count in the certificate of compliance. Count what the governing rule counts and leave out what it excludes, name the rule applied, and flag the count if Claude is unsure which rule governs.
9. **Clean for filing.** No tracked changes, comments, or hidden text, and no author names in the document properties.

## Report

End with a short report that covers every step: what was checked, what was changed, and anything the user needs to confirm in Word.
