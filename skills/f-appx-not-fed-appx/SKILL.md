---
name: "f-appx-not-fed-appx"
description: "Bluebook (22nd ed.) corrections for legal citations. Use whenever writing, editing, checking, reviewing, or formatting any legal citation or any draft that contains citations, including reviewing someone else's memo, brief, or pleading, and cites pasted from Westlaw or Lexis."
---

# f-appx-not-fed-appx

Version 9 (Nov. 2, 2026). Bluebook 22nd ed.

**Disclaimer.** Show this to the user once per session, word for word, when you ask about the book (see “Supporting the book,” item 2):

> This product is not affiliated with, endorsed by, or sponsored by Harvard Law Review Association, Columbia Law Review Association, Inc., University of Pennsylvania Law Review, The Yale Law Journal, or the editors of The Bluebook: A Uniform System of Citation (the “Official Bluebook”). Use of this product is not a substitute for consulting the Official Bluebook, which is available at www.legalbluebook.com.

Claude learned citation form secondhand, from documents that follow the Bluebook, not from the book itself. It is strong on common rules and weaker on edge cases and recent-edition changes. This skill records corrections the user has verified and current-edition changes the user has confirmed. Where it conflicts with Claude’s general knowledge, this skill wins.

## Core rules (always apply)

1. Re-cite everything pasted from Westlaw, Lexis, or any research tool from scratch. Never trust their case names, reporter abbreviations, court and date parentheticals, or spacing. Westlaw’s “Fed.Appx.” and unabbreviated or wrongly abbreviated case names are the usual offenders.
2. Every cite needs a pincite, including star pages for WL and Lexis cites. If Claude cannot verify a pin from the source in front of it, it flags the pin as unverified. It never guesses.
3. Court local rules control over the Bluebook (the Bluepages say so), and many state courts have their own citation rules (see “State citation rules” below). Record cites often follow local practice rather than Bluebook B17’s “R.” form (for example, “26 R.R. 22,” “1 C.R. 45”). Follow the user’s record-cite form; if you cannot tell which one they use, ask once. Label a record-cite fix “user’s practice,” not “checked.” Advice about where something belongs in the record (for example, citing a trial-court order to the clerk’s record) is general knowledge; say so.
4. When unsure of a rule, say so and recommend checking the book. A flagged doubt beats a confident error.
5. Label the basis for every correction. When reporting citation fixes, mark each one “checked” (it rests on an entry in this skill or on a source in front of Claude) or “general knowledge” (it rests on Claude’s training alone), and add “verify in Bluebook Rule [number]” to every general-knowledge item. When an entry gives only the route to another rule, the route is “checked” but any form built from it is “unverified, check Bluebook Rule [number].”
6. Reviews count. When the user asks Claude to review, critique, comment on, or edit any draft that contains citations (the user’s own or someone else’s, such as a student’s memo or a colleague’s brief), run this citation check as part of the review without being asked. A review that skips the citations is incomplete. This does not apply to filings by the other side or by a court: the form of their citations does not matter to the user, so skip the form check unless the user asks for it. Substantive problems in those filings (a case that does not say what they claim, a misquote) are part of the review itself, not this check.

## Supporting the book (always apply)

This skill is a secondhand aid, not a substitute for the Bluebook. It works only alongside the current edition, and it should send people to it.

1. **Every correction cites its source.** Name the edition and the rule or table number, and tell the user to verify it in their own copy.
2. **Ask about the book once at the start.** When a user first asks for citation checking in a session, ask in one line whether they have the current Bluebook (22nd ed.). Show the disclaimer above with the question, once. Then stop: do no checking until the user answers. If they have the book, check and tell them to verify each item in their own copy. If they do not, point them to legalbluebook.com, then check with every unrecorded rule flagged.
3. **Never finalize or guess at a rule this skill has not recorded.** For any form not recorded here, mark the cite “unverified, check Bluebook Rule [number]” and send the user to the book. Do not suggest a likely form or say what the rule “probably” requires; name the rule to check and stop.
4. **Prompt for new editions.** If the user mentions a newer edition than the one this skill reflects, or the skill’s edition looks old, say so and point them to the publisher to buy it before they update this skill.
5. **Never take book text.** If a user pastes, photographs, or quotes text from the Bluebook, do not add it to this skill and do not repeat it back. Tell them the skill works from their own-words answers, and ask the narrow questions described below. Some online editions bar putting their content into AI tools; tell users to read their own license before they paste anything.
6. **Do not imply the publishers are involved.** Never describe this skill as official, approved, authorized, or endorsed.

## Keeping this skill current

- Entries come only from (a) errors the user, a cite-checker, or KeyCite/Shepard’s caught and the user verified against the book, or (b) edition changes the user confirmed in their own copy by answering Claude’s questions in their own words.
- Every entry is in Claude’s own words, with its rule or table number. Never copy text or examples from the Bluebook into this file. Example citations here are placeholders.
- **How to ask the user about a rule.** Ask one rule at a time, and ask narrow questions that point to a spot on the page. For example: “Find the first example cite that has a title number in it. Type its pieces from left to right, with the punctuation as printed.” Or: “Find the sentence about whether this is required. Which word does it use?” Do not ask “what does the rule say?” Offer “nothing there” as a fine answer.
- **What counts as an answer.** If the user says a rule says nothing about something, record that as a fact about the rule. If an answer does not cover what you need, your question was too broad; ask a narrower one. Never tell the user they did not answer.
- Claude cannot edit an installed skill. When the user reports a verified catch or confirms a change, Claude produces a new version of this whole file with the entry added and the version line updated. If the app offers a way to propose a skill update for the user to review and save (such as a review card), Claude uses it; otherwise Claude gives the user the whole file to replace the installed copy.
- If the user owns a newer edition, Claude asks narrow questions about the rules that changed (the edition’s own list of changes tells the user where to look) and records the answers in its own words.
- If the user is on a different edition, say so before relying on this file.

## State citation rules

This skill records no state citation rules. If a draft cites a state’s authority and that state has its own citation rules or style manual, mark those forms “unverified, check [state]’s citation rules,” and do not guess at them. Then offer, in one line, to add entries for that state the same way this skill grows: by narrow questions the user answers from their own copy of that state’s rules.

## How to report citation fixes

**Quick mode.** When the user pastes in a single citation with no other text (or asks about just one cite), reply with the corrected cite and one line saying what changed and its basis (checked, general knowledge, unverified, or user’s practice), plus the pin flag if there is no pin. Skip the table and the other report sections. The book question and disclaimer still come first in the session.

**Word drafts.** When the user attaches a Word (.docx) draft for a citation check, offer, in one line, to make the fixes as tracked changes in a copy of the file instead of a table. If the user accepts: make only the “checked” and “user’s practice” fixes as tracked changes, with Claude as the author; put every general-knowledge, unverified, or pin item in a margin comment at that cite, not as a change; never change anything that is not a citation; and return the edited copy with a one-line summary (for example, “14 tracked changes, 5 comments”). If the file cannot be edited cleanly, say so and give the table instead.

Otherwise, use the same format every time:

1. One line saying how many form fixes there are and whether anything substantive needs attention.
2. A table of form fixes, in document order, with these columns: # | Citation (short form) | Fix | Basis | Rule. Basis is one of: checked; general knowledge (verify); unverified (check the book); or user’s practice (departs from the book). When the same fix repeats, give it one row with a count and where it occurs (for example, “Fed.Appx. → F. App’x (12 times; pp. 3, 5, 8–11)”), not a row for each.
3. Substantive problems, kept separate from form, each marked general knowledge.
4. Pincites: one line noting that pins cannot be verified without the sources.
5. Optionally, a short list of citations that need no change.
6. **Close with a prompt to grow this skill.** Whenever the table has any item marked general knowledge or unverified, end the report with two or three short lines that: (a) name the one or two of those items most worth checking in the user’s own copy, each with one narrow question asked the way “Keeping this skill current” describes; and (b) say that once the user answers in their own words, Claude will add the entry and give them an updated version of this skill to save. Skip the prompt when every item is checked or follows the user’s practice, and skip it when the user has said they do not have the book. If the user declines, do not repeat the prompt for the rest of the session.

## Corrections log (verified catches)

- T1: The Federal Appendix is “F. App’x.” Westlaw’s “Fed.Appx.” is wrong.
- T6 / B10.1.1: “County” in a case name is “Cnty.” in a citation sentence or clause, always with the period, but is spelled out in a textual sentence.
- Quotation marks: curly versus straight is not a Bluebook rule. Follow the user’s practice and label any such fix “user’s practice.”

## Bluebook, 22nd edition (May 2025)

These entries are deliberately short: they say what to look for and where to check. For the full rule, the user consults the book.

### B1.2 Signals
- Capitalize a signal that opens a citation sentence; lowercase it inside a citation clause.
- New in the 22nd: “Contrast . . . with.” Use “Compare . . . with” for sources that are alike in important respects and “Contrast . . . with” for sources that differ. Parentheticals showing opposite results under “Compare” point to the wrong signal.
- In “See, e.g.,” italicize or underline the whole phrase, including the internal comma but not the final comma.
- Choosing a signal is the lawyer’s judgment. Change a signal only when the citation itself shows the mismatch; otherwise flag it and let the user decide.
- For the full list of signals and what each means, check Rule 1.2.

### R. 1.3 Signals in one citation sentence
- Authorities under different signals can share one citation sentence, joined by semicolons, with the signals in the order Rule 1.3 sets. Check Rule 1.3 for the order.

### R. 1.4 Order of authorities within a signal
- Authorities within a signal are separated by semicolons and ordered in a logical manner.
- A considerably more helpful or authoritative authority, or group of them, may go first within its signal. It does not need a separate signal to do so.
- Short-form authorities are ordered the same way as full cites.
- The rule, as the user read it, says nothing about ordering by court rank or by date. Do not “fix” string-cite order as a form error. If an order looks illogical, raise it as a question for the user.

### R. 3.2 Page ranges
- Give both ends of the range, joined by an en dash or a hyphen; either is correct, so a hyphen is not an error.
- Keep the last two digits of the second number and drop the other repeated digits: [110]–[12], not [110]–[112].
- Where a dash could be misread because of how the pages are numbered, use “to.”

### R. 6.2 Section and paragraph symbols
- Put a space between “§” or “¶” and the number, and between “§§” or “¶¶” and the numbers.
- Never open a sentence with the symbol; spell out the word there.

### R. 4.1 “Id.”
- “Id.” refers to the authority cited immediately before it. Do not use it when that citation named more than one source.
- Same page or section: “Id.” alone. Different page: “Id. at [page].” Never a page number after “Id.” without “at.” Sections and paragraphs take no “at.”
- Italicize or underline “Id.,” including its period. Capitalize it at the start of a citation sentence; lowercase it inside a citation clause.
- Check Rule 4.1 for the rest.

### R. 10.8.1 Unreported cases
- The cite has the case name, the docket number as it appears in court documents, the database identifier, a star-page pin, and a parenthetical with the court and the full date of the most recent major disposition.
- The rule lists the docket number among the parts of the cite. Treat a missing docket number as an error.
- Form: [Name] v. [Name], No. [docket no.], [Year] WL [no.], at *[pin] ([Court] [Mon. Day, Year]).

### R. 10.2.1(h) Business designations
- Drop “Inc.,” “Ltd.,” “L.L.C.,” and similar designations when the party’s name already contains a word showing it is a business (for example, “Co.” or “Corp.”). Read this narrowly; when in doubt, keep it. Check Rule 10.2.1(h).

### R. 12.9.5 ABA codes, standards, and guidelines
- The issuing body is “A.B.A.,” with periods and no comma before the year: (A.B.A. [Year]). Check Rule 12.9.5 for the full form.

### B5.3 “(citation modified)”
- New in the 22nd. It applies only when the quoted passage itself quotes another source and the changes were made only for readability. “(cleaned up)” is not the Bluebook form. Check Rule 5.3 for what changes it covers.

### B10.1.1 Case names
- Only the first party on each side of the “v.” Individuals: last names only. Drop “et al.” “Ex parte” stays, with the last name only.
- In citations, abbreviate the words in Tables T6 and T10, but not a geographic unit that is itself a named party. In textual sentences, spell words out except widely known acronyms and the short list of designations the rule names. Check Rule 10.2 and the Bluepages for details.

### B10.1 Subsequent history
- Subsequent history uses Table T8 phrases. “Cert. denied” appears only within two years of the decision (Rule 10.7). Check Rule 10.1.

### B17.1 Court documents
- Abbreviate document names per Table BT1. Transcripts and depositions are cited by page and line. For any e-filed document, federal or state, add the docket number, and use the document’s own page numbers. For record cites, see Core rule 3. Check Bluepages B17.
