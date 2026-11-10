---
name: derivative-docs
description: "Run when the user says “derivative docs” or “derivatives,” or asks for an appendix, stay motion or application, IFP motion, proposed order, or record excerpts for a main pleading: build the companion to match it exactly. Checklists cover Texas and federal capital habeas practice."
---

# Derivative docs

A derivative document is one that travels with a main pleading: an appendix, a separate motion or application for a stay of execution, a motion to proceed in forma pauperis, a proposed order, or record excerpts. This skill builds the companion. It never drafts or edits the main pleading.

**Scope.** The court checklists below cover the courts where Texas capital habeas cases are litigated: the U.S. Supreme Court, the Fifth Circuit, the Texas Court of Criminal Appeals, Texas district courts, and the four federal district courts in Texas. Lawyers elsewhere keep everything above the checklists and replace the checklists with their own courts (see “Adapting this skill”).

**Verify the rules.** Court rules change. Every rule cited in the checklists was current when written; confirm each one against the court’s current rules before relying on it.

## Settings (edit these for your practice)

- **House style:** Oxford comma; no contractions; curly quotation marks; one space after periods; the lawyer’s brief font; left-aligned; no blank pages; no highlighting. Change any of these to match your own filings.
- **Co-signed signature blocks:** default side by side, lead counsel on the left; stacked in the Supreme Court, lead counsel on top. Electronic signatures carry a line between “/s/ Name” and the typed name.
- **File names:** default is the main pleading’s file name with the matter word changed (see Carry-over).
- **Certificates of conference:** default is none in state-court filings, where the local rules do not require one.

## Trigger

Run when the user says “derivative docs” or “derivatives,” or when the user asks for any of the five documents above and a main pleading exists (pasted, attached, or named). If the user asks for one of the five and no main pleading is in the chat, ask for it before doing anything else.

## Intake

1. Read the main pleading in full.
2. Take from it: the court; the caption and every cause, writ, and docket number; the party styling and the client’s name as styled; counsel’s names, addresses, and signature-block layout; the execution date, if any; the exact relief in the prayer; any “capital case” notation; any related-proceedings list; the convicting court and county; and the main pleading’s file name, if shown.
3. Ask only for what the pleading does not show, and ask all missing items in one message: court, execution date, exact prayer, or file name.

## Carry-over

Copy, never reword:
- Caption, cause and docket numbers, party styling, and client’s name.
- Counsel block and signature-block layout, following the Settings above.
- “Capital case” notation and related-proceedings list, where the court uses them.
- The stay request: a stay motion or application asks for the same stay the main pleading’s prayer asks for, in the same words. An IFP motion, proposed order, appendix, or record excerpts asks for no stay.

The one exception: change only words that would misread in the companion (for example, “this application” in the main pleading becomes “his application for a certificate of appealability” in a stay motion), and flag each change in the report for the user’s approval.

File name: the main pleading’s name with the matter word changed (for example, the “-application” segment becomes “-stay” or “-ifp”), lowercase, hyphenated, then “.YYYYMMDD” with today’s date. Show the proposed name and wait for the user’s approval before saving.

## Drafting rules

- House style throughout, as set in Settings.
- State no date or fact the main pleading does not show; bracket it instead. A date in a file name is not a filing date.
- Certificates of conference: follow Settings, and add one wherever the court’s rules require it (see checklists).
- Certificates of service and compliance are paragraphs at the end of a document, not separate documents, except where a court requires a separate document (the Supreme Court’s proof of service). Add them to the companion only where its court requires them (see checklists).
- Cite rules under the Bluebook (and the Greenbook for Texas forms). If a citation-checking skill such as f-appx-not-fed-appx is installed, run every cite through it.
- An appendix opens with a cover page and a table of contents listing each item by letter, in the order the court’s rule requires (see checklists) or, where no rule sets an order, the order the main pleading cites them; long statutes quoted in the main pleading in part appear here in full.

## Court checklists

Each item is what the companion must contain or attach, with the rule. Mark anything missing in the report.

### Supreme Court (8½ × 11 format)
- Cover in the Rule 34.1 order: docket number or blank, Court name, caption, nature of proceeding and court below, title, counsel of record with address, e-mail, and telephone. Sup. Ct. R. 34.1(a)–(f).
- “Capital case” precedes the questions presented. Sup. Ct. R. 14.1(a).
- IFP motion attached in front of the petition; original and 10 copies. Sup. Ct. R. 12.2, 39.2. No affidavit when counsel was appointed below under a federal statute, but the motion must cite the statute. Sup. Ct. R. 39.1.
- Appendix order, in six slots. Sup. Ct. R. 14.1(i)(i)–(vi):
  1. the opinions, orders, findings, and conclusions entered with the judgment under review;
  2. any other relevant opinions, orders, findings, and conclusions in the case;
  3. any order on rehearing;
  4. the judgment, if entered on a different date from the opinion or order in slot 1;
  5. material required by Rules 14.1(f) and 14.1(g)(i): the text of lengthy statutes and constitutional provisions involved, and record material showing where and how the federal question was raised below (these share the slot; neither outranks the other);
  6. anything else essential to understand the petition (affidavits and other evidence go here).
  Each item is captioned with the issuing court, title and number, and date of entry. Appendix table of contents. Sup. Ct. R. 14.1(i), 34.4. If the main pleading’s lettering departs from this order, flag it and name the smallest change that fixes it; do not re-letter without the user’s approval.
- Stay application: addressed to the Circuit Justice; original and two copies; shows why relief is unavailable elsewhere; identifies the judgment; appends the opinion and order below and the order denying the stay; states specific reasons. Sup. Ct. R. 22.2–22.3, 23.3.
- Proof of service: draft it as a separate document with every stay application, IFP motion, and appendix, with the statement that all parties required to be served have been served and the list of counsel served, with addresses, telephone numbers, and the party each represents. Sup. Ct. R. 29.5.
- Page limits for 33.2 documents: 40 pages for a petition or extraordinary-writ petition; 15 for a reply. Sup. Ct. R. 33.2(b). No word-count certificate for a 33.2 document.
- Table of authorities lists every page; no “passim.” Sup. Ct. R. 34.2.

### Fifth Circuit
- Stay motion in a § 2254 death-penalty case attaches, in order: (a) the district-court petition; (b) every brief or memorandum both parties filed below; (c) the district court’s opinion; (d) its judgment; (e) the stay application below; (f) the stay order and reasons; (g) the COA or the order denying it; (h) every state or federal opinion or judgment on any issue presented, or the relevant transcript pages. A statement substitutes for any document that cannot be attached. 5th Cir. R. 8.1(a)–(h). If the State does not oppose and the motion says so, the attachments may follow within 14 days. 5th Cir. R. 8.1.1.
- Reasons for any issue not raised below or not exhausted. 5th Cir. R. 8.1.2.
- Brief account of prior applications to this or any other court. 5th Cir. R. 8.4.
- Certificate of interested persons and the statement that opposing counsel was contacted and whether opposition will be filed. 5th Cir. R. 27.4, 28.2.1.
- Filed at least 7 days before the execution, or a sworn explanation of the delay is attached. 5th Cir. R. 8.10.
- Record excerpts with a brief: docket sheet, notice of appeal, judgment, orders reviewed, any report and recommendation, the supporting opinion, and certificate of service; optional contents capped at 40 pages; tabbed, numbered table of contents, “RECORD EXCERPTS” cover. 5th Cir. R. 30.1.4–30.1.7.
- Format and length per Fed. R. App. P. 32(a) and 5th Cir. R. 32. 5th Cir. R. 22.

### Court of Criminal Appeals
- Companions are the appendix and a separate stay motion; no proposed order.
- A motion states its grounds with particularity and the relief sought, with a certificate of service at the end; no certificate of conference. Tex. R. App. P. 9.5, 10.1(a).
- The PDR appendix carries the court of appeals opinion. Tex. R. App. P. 68.4(j).

### Texas district court
- Companions are the appendix of exhibits and, with an art. 11.071 application, a separate stay motion. An art. 46.05 motion attaches its affidavits and records inside the motion, not as a companion. Tex. Code Crim. Proc. art. 46.05(c).

### Federal district court (Texas)
- Stay timing in every district: where no local rule sets a deadline, file the district-court stay motion more than 7 days before the execution so any appeal can still meet 5th Cir. R. 8.10. (Practice, not a district rule.)
- Every proposed stay order, in every district, ends with a clerk-notice paragraph directing the Clerk to send the order by e-mail and fax to the Director of TDCJ-CID; the Warden of the Huntsville Unit; the presiding judge and the District Clerk of the convicting court; and the district attorney of the convicting county. Fill in the court and county from the main pleading. (Practice, not a rule.)
- IFP motion with the § 1915 affidavit. Rules Governing § 2254 Cases 3(a)(2).

#### Southern District
- Stay application: separate proposed order; averment that the movant conferred and the parties cannot agree. S.D. Tex. LR 7.1(C)–(D).
- Stay application includes every state-court opinion and judgment; a description of relief sought from any federal court with action number and court; each court’s reasons for denying relief; and why any unexhausted issue was not raised in state court. S.D. Tex. Supp. Habeas R. 1(A)(1)–(4).
- No capital page limit in the local rules; check the judge’s procedures.

#### Northern District
- Capital page limits: petition plus any supporting brief, 100 pages total; answer, 100; reply, 25; tables of contents and authorities excluded. N.D. Tex. LR 7.5.
- Stay motion: separate proposed order. N.D. Tex. LR 7.1(c). A brief and a certificate of conference stating opposed or unopposed, the date, and who conferred. N.D. Tex. LR 7.1(b), (h).

#### Eastern District
- Capital page limits: petition and answer, 100 pages; replies, sur-replies, and every other motion, 30; attachments, tables, and certificates excluded; tables of contents and authorities for any document over ten pages. E.D. Tex. LR CV-3(b).
- Stay motion filed at least 7 days before the execution or reciting good cause for the late filing. E.D. Tex. LR CV-3(c).
- Proposed order: separate, searchable and editable PDF, styled with the cause number, no date line, no signature block. E.D. Tex. LR CV-7(a).
- Certificate of conference at the end, after the certificate of service. E.D. Tex. LR CV-7(i).
- Paper copy to the judge’s chambers for any filing over ten pages, attachments included, with the Notice of Electronic Filing on top, unless the judge has opted out. E.D. Tex. LR CV-5(a)(9).

#### Western District
- No capital page limit; motions, a stay motion included, capped at 20 pages excluding caption, signature, certificates, and attachments. W.D. Tex. LR CV-7(c)(2).
- Authority goes in the motion, not a separate brief. W.D. Tex. LR CV-7(c)(1).
- No proposed order required for a stay motion. W.D. Tex. LR CV-7(f).
- Conference statement in the body of any nondispositive motion. W.D. Tex. LR CV-7(g).

## Report

End with two short tables: (1) each carried-over field and where in the main pleading it came from, with any flagged wording change; (2) each checklist item for the court, marked present, missing, or needing the user’s confirmation. List every checklist item for the court that bears on the filing package, not only items about the companion itself (for example, stay deadlines and paper-copy rules). Then list anything the user must confirm in Word.

## Adapting this skill

Keep everything above the checklists and replace the checklists with the courts you file in. Write each item as what the companion must contain, followed by the rule that requires it. Nothing in this file names a client, case, or cause number, and nothing should be added that does.