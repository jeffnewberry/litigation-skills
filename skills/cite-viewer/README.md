# cite-viewer

Builds a page on your own computer that shows your draft with every citation as a link. Click a citation and the cited page from the Westlaw source opens beside it, with the relied-on words shaded and a status:

- **Supported** (green): the passage says what your sentence says.
- **Check** (red): a misquote, a wrong pin, or a sentence that overstates the source, with the fix.
- **No pincite** (amber): a cite to specific material with no pin.
- **Source not loaded** (gray): record cites, books, and anything Westlaw did not return.

Legal statements with no citation are marked too.

## What you need

- A Westlaw subscription with Find & Print. Find & Print requests are charged under your plan.
- A computer (not a phone or tablet) where the PDFs can be saved.
- Claude with browser access and access to a folder on your computer.
- Optional: Bloomberg Law, for docket documents.

## How it fits your process

Run it after your citator and any cite-checking tool, once the text is settled. It does not replace reading the cases; it makes the reading fast and records what each passage supports.

## Confidentiality

The viewer holds your draft and, with record cites, record material. It is built to stay on your computer. Do not publish or host it.

## Settings

Edit the Settings section at the top of SKILL.md: your brief font, your folder-naming pattern, and your cite-checking tool. Westlaw’s screens change; if a setting the skill names has moved, the skill is told to stop and describe the page rather than guess.
