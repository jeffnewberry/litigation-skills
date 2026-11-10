# f-appx-not-fed-appx

A Bluebook (22nd ed.) citation checker for Claude, named for the most common error it fixes: Westlaw’s “Fed.Appx.” is wrong; the correct form is “F. App’x.”

## What it does

- Re-cites anything pasted from Westlaw or Lexis from scratch.
- Labels every fix by how sure it is: **checked** (recorded in the skill), **general knowledge** (verify in the book), **unverified** (check the book), or **your practice**.
- Never guesses at a rule it has not recorded. It names the rule and sends you to the book.
- Offers to make fixes as tracked changes in a copy of a Word draft.
- Grows with use: when you confirm a rule in your own copy, Claude adds it in its own words and gives you an updated version to save.

## What it does not do

It does not replace the Bluebook. It works only alongside your own copy of the current edition, and it never copies text from the book. It does not check whether authorities are still good law; use KeyCite or Shepard’s for that.

## State citation rules

This public version records no state-specific rules. If you practice in a state with its own citation manual, the skill will flag those forms as unverified and offer to build entries for your state from your own copy.

## Bluebook disclaimer

This product is not affiliated with, endorsed by, or sponsored by Harvard Law Review Association, Columbia Law Review Association, Inc., University of Pennsylvania Law Review, The Yale Law Journal, or the editors of The Bluebook: A Uniform System of Citation (the “Official Bluebook”). Use of this product is not a substitute for consulting the Official Bluebook, which is available at www.legalbluebook.com.
