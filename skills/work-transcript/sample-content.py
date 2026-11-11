# Sample content for build_transcript.py. Everything here is made up.
PRIVILEGED = False
FONT = 'Times New Roman'
QUESTIONER = 'Ms. Rivera'
HEADER = 'Sample Matter: Record-Citation Check'
STYLE = [
    ('In the Matter of', 'Work Session with'),
    ('a Sample Appellate Brief', 'Claude, an AI Model'),
    ('', ''),
    ('No. 00-0000', 'Sample Only'),
]
TITLE = 'Record-Citation Check'
SUBTITLE = 'Condensed Transcript of a Work Session'
OPENING = 'On the date below, counsel asked Claude to check every record citation in the statement of facts of a draft appellate brief against the reporter’s record.'
DATE_LINE = 'Sample session'
APPEARANCES = [
    ['For the Questioner:', 'Ms. Rivera, appellate counsel (fictional)'],
    ['The Witness:', 'Claude, an AI model made by Anthropic'],
]
PRELIM = [
    'This is a sample. The matter, the people, and the record are invented to show what the skill produces.',
    'Counsel gave Claude the draft statement of facts and three volumes of the reporter’s record. Claude checked each citation, reported one citation that did not support its sentence, and made one mistake of its own, which counsel caught. The record below says so.',
]
QA = [
    ('Q', 'I am attaching the statement of facts and volumes 2 through 4 of the reporter’s record. Check every record citation. Tell me whether the cited page says what the sentence says.'),
    ('X', 'ex1', '(Questioner’s Exhibit 1, draft statement of facts, offered.)', 'Draft statement of facts'),
    ('A', 'There are 31 record citations. Twenty-nine support their sentences. One does not: the sentence says the officer arrived “within minutes,” but 3 R.R. 44 has him arriving “about forty minutes later.” One more is close: 2 R.R. 118 supports the quotation, but the quotation stops mid-sentence and leaves out a qualifier.'),
    ('Q', 'Check 4 R.R. 12 again. I think you missed one.'),
    ('A', 'You are right. I reported 4 R.R. 12 as supporting the sentence. It does not: the testimony is on 4 R.R. 21. I transposed the page number. That makes two citations that need correcting, not one.'),
    ('Q', 'Fix both in a list I can take into Word. Do not change anything else.'),
    ('A', 'Here are the two corrections, with the old and new citation for each, and the qualifier on 2 R.R. 118 flagged for your decision. I changed nothing else.'),
]
CERT = [
    'I, Claude, certify that this transcript is a condensed and summarized account of the work session described above, prepared at the questioner’s request. It is not a verbatim record and not an official court document.',
    'Where I made a mistake during the session, this transcript says so.',
    'WITNESS MY HAND this the __ day of ____, 20__.',
]
