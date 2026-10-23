---
name: anki-flashcards
description: Turn a lesson, notes or topic into a quality-checked Anki deck of atomic, self-contained typed-answer flashcards (a tab-separated .txt plus an importable .apkg). Use when the user asks for flashcards, Anki cards, a deck, or spaced-repetition cards.
---

# Anki flashcards

Make one deck per source (usually one per lesson), written from the source's actual content. Every card uses the note type **Typed answer + Notes**: the learner reads the Front, types the Back, Anki compares what they typed with the Back character by character, and then shows the Notes. So the Back has to be short and exactly retypeable, and the Notes are where the card teaches: why the answer is right, how it fits, a tiny example.

The cards should feel like a good tutor asking a question and then explaining, not a quiz machine barking terms. A bare question with a one-word answer and nothing after it is the failure this skill exists to avoid.

The scripts are in this skill's `scripts/` folder. Below, `$SKILL` means the folder this file is in.

## Workflow

1. **Read the source in full** (strip HTML to text if needed). Note any exclusions the user gave.
2. **Make a coverage list** before drafting: the source's headings, learning outcomes ("you can now..."), self-check questions, glossary terms, tables and named processes. Then list the prerequisites the source takes for granted but never teaches (for a networking lesson: what a network is, bit/byte/binary, client vs server, units such as bits per second).
3. **Draft the cards** following the rules below. Expect roughly 15 to 30 per lesson; the coverage list decides the count, not a target.
4. **Review** the final text with the checklist below.
5. **Quality check** every card and the deck with the section below. Rewrite each card that fails, then test it again.
6. **Write the file** where the user asked, usually the lesson's folder, named like `NNNN-flashcards.txt`.
7. **Validate**: `python3 -I $SKILL/scripts/validate_deck.py <deck.txt>...` and fix every error. Options: `--allow FF,DORA` for tokens that may stay bare, `--exclude assignment` (repeatable) for words the user ruled out. The validator only catches format errors and obvious slips; it does not replace step 4.
8. **Build the `.apkg`**. Anki cannot create a note type from a text import, so the package carries it. Use a venv outside the user's folders (the scratchpad, or `/tmp`):
   ```
   python3 -m venv /tmp/anki-venv && /tmp/anki-venv/bin/pip install -q genanki
   /tmp/anki-venv/bin/python $SKILL/scripts/build_apkg.py <deck.txt>...
   ```
   Each `deck.txt` gets a `deck.apkg` next to it.
9. **Link it** if the folder is an Obsidian vault with lesson notes: link the file from the lesson's note using the vault's rule for non-note files (full vault path).
10. **Report back**: the card count; which cards came from outside the user's notes (the `background` cards, and any definition written from general knowledge) so they can check them; which cards the quality check rewrote or split (one line each, saying why); and how to import: in Anki, File > Import, choose the `.apkg`.

## Card rules

### Each card

1. **One question, one answer.** The front asks exactly one thing with one right answer, and ends in `?`. Split a card when it:
   - joins two questions ("How big is the UDP header, and what does its length field cover?" is two cards);
   - asks "what, and why" where the why could be asked on its own;
   - wants several items or a mapping ("ports 67 and 68", "how do the OSI layers map onto TCP/IP": one card per item);
   - is a multi-part list or "all that apply" question ("name the three fields", "which of these are true?"): never ask for a list; ask about one item per card, or ask "which one..." about a single fact;
   - compares on more than one dimension (one dimension per card).

   The one exception is an ordered sequence whose point is the order and that fits the back (the four DHCP messages in order). When unsure, split.
2. **Stands alone.** It must make sense with no other card and no lesson open, so name the context ("In UDP, ...", "In IPv4 subnetting, ..."). Never "see above", "as before", a lesson number, or anything that needs another card's answer.
3. **Self-explanatory front.** Put every qualifier the answer depends on in the front (units, protocol, direction, "in decimal"), because the learner sees the Notes only after answering. Define every symbol in a formula ("a message of L bits sent over N links of R bits per second"). Give a short parenthetical hint for jargon the card cannot avoid ("slot times (fixed units of waiting time)"). No yes/no cards: ask "which" or "why" instead.
4. **Short, typeable back.** 1 to 12 words of plain text: a term, number, value, command or short phrase. No HTML, no explanation, no full stop at the end. Use the canonical form the learner will actually type (`8`, `MAC address`, `0x0800`). For a "why" card, the shortest reason phrase.
5. **A front that reads like a person asking.** Write a full, natural sentence, and where it helps, one clause of setup that says why the question matters ("A switch receives a frame for a device it has never seen. What does it do with the frame?" rather than "Unknown destination frame action?"). Keep it to one question and two short sentences at most.
6. **Notes that teach.** Every card has Notes: one to three short sentences (60 words at most) that explain why the answer is right or how it works, link it to something the learner already knows, and give a tiny example where one helps. Plain, warm and direct; no "Great job!", no restating the question. HTML is fine here (`<br>`, `<code>`, `<b>`). The Notes follow the same sourcing rules as the card.
7. **Answers a stranger could follow.** These apply to the back and the Notes, and matter most on definition cards. The back still has to be 12 words or fewer, so anything that won't fit goes at the start of the Notes.
   - **Include the one detail that prevents confusion.** If the term is commonly mixed up with something similar, add a short clause that separates them (e.g. "on the same machine, unlike a protocol").
   - **Use the correct technical term** where one exists, even if you also explain it in plain words.
   - **No filler.** Cut "basically", "it is a thing that", examples that don't add meaning, and repeated wording from the question.
   - **Check:** could someone who has never seen the question understand the answer? If not, add the missing context. If it takes more than a breath to say, trim it.
8. **Abbreviations.** In the front, write each abbreviation as "Full Name (AB)" the first time it appears ("Time To Live (TTL)", "Virtual Local Area Networks (VLANs)"; but see quality check 5 when the front gets long). The exception is a card asking what the abbreviation stands for. In the back, use the form the learner would type, usually the bare abbreviation (`MAC address`, `TTL`); never make them type an expansion the question did not ask for. Every abbreviation the deck uses must be expanded somewhere in the deck. Plain words and names ("ID", "Ethernet II") are not abbreviations, and anything inside `<code>` is left alone.
9. **Only what the source supports.** Skip anything it marks unverified; where it corrects its own slides, use the correction. Follow user exclusions completely: "nothing about the assignment" means no scenario, brief, lab task or number from it.
10. **Concepts, not the source's worked examples.** Don't turn the source's own scenario into cards (its named company, its given address and mask, its delay sum); test the rule the example illustrates. Practising a rule with small numbers you invent is good, and so are fixed facts such as header sizes.

### The deck as a whole

11. **Covers the coverage list.** Every item gets at least one card: its definition, its mechanism (how or why), its main rule or number; for a process, one card per step plus one for the whole sequence. Test: could the learner explain each topic aloud using only these cards?
12. **Defines every term it uses.** Any technical word in any front or back (header, payload, octet, hop, port, ...) has its own plain-language definition card, earlier in the file. Prefer the source's or glossary's wording; if you wrote a definition from general knowledge, say so in your reply.
13. **Fills background gaps.** Add plain-language cards for the prerequisites from step 2, tagged `background`, near the top of the file.
14. **Mixes card types**: definition, how/why, comparison on one dimension, rule or number, small invented example, common mistake.
15. **No duplicates**, within the deck or across decks of the same course. Compare by meaning, not wording: "if I knew the other card, would this one add anything?" Name-to-job and job-to-name are one fact; "what" and "why" are two. Keep the better-worded card.

Example card:
- Front: `The User Datagram Protocol (UDP) adds a small header to every message it sends. How many bytes long is that header?`
- Back: `8`
- Notes: `Always 8 bytes: source port, destination port, length and checksum, 2 bytes each. That is why UDP is so lightweight next to TCP, whose header is at least 20 bytes.`

The blunt version of the same card, which this skill should never produce: front `UDP header size?`, back `8`, no notes.

## Review checklist

Print the final fronts and backs, not the draft, and read them as a stranger who has seen nothing but the cards:

- Each front asks one thing in a natural sentence, names its context, and can be answered without any other card.
- Each card's Notes explain the answer instead of repeating it; reading the deck front-back-notes should feel like being taught.
- Each back and its Notes pass rule 7: the detail that separates the term from its look-alike, the correct technical term, no filler, and understandable without the question.
- Every technical word has a definition card, and every abbreviation is expanded somewhere.
- The `background` cards cover what the source assumes.
- Every coverage-list item is ticked off.
- Nothing reads badly: no doubled expansions ("Frame Check Sequence (FCS) (frame check sequence)"), no wrong articles ("an Switched Virtual Interface"), no vague fronts ("what does it do?").
- No two cards test the same fact.

## Quality check

The validator checks the format. This check asks whether a learner can actually answer each card without guessing what it wants. A card fails if any test fails.

### Per card

1. **Cover-the-back test.** Read only the front and write the answer someone who knows the material would type. If it differs from the back in *kind* (a function instead of a number, a name instead of a definition, one item instead of a list), the front is ambiguous. Rewrite it so the kind of answer is obvious.
2. **Ask comes first.** The question word and what it asks for appear early ("What does X do?", "Which layer...?", "What is X called in Y?"). Side facts (another model, a synonym, a related layer) go in the notes, unless the card is about that link.
3. **No answer-shaped clutter.** If the front names something that could itself be taken as the thing being asked for, cut it or give it its own card.
4. **One fact.** If the back joins two facts that could be asked separately, check that the front truly asks for both. If not, split the card.
5. **Front length.** A front over about 20 words usually hides a second question. Shorten it. When spelling out every abbreviation would push the front past 20 words, expand only the main term in the front and give the other expansions in the notes.
6. **Typeable back.** The learner can type the back from memory, and there is one reasonable wording. If several wordings are equally right, narrow the front or list accepted variants in the notes.
7. **Back matches front.** The back answers exactly what the front asks, no more. Extra facts go in the notes.
8. **Not given away.** The back's key word does not appear in the front.
9. **Notes teach the likely miss.** The notes say why the answer is right and name the most likely wrong answer and why it is wrong.

### Across the deck

- Easily confused pairs (for example Layer 3 vs Layer 4, TCP vs UDP) have a contrast card (one dimension per card, as in rule 1).
- No front can be correctly answered with another card's back.
- Read the fronts in deck order: background first, and each idea comes before cards that rely on it.

### Worked example

Fails:

- Front: *What is the main job of the Open Systems Interconnection (OSI) network layer, which Transmission Control Protocol/Internet Protocol (TCP/IP) calls the internet layer?*
- Back: *addressing and routing between networks*

Why: the front is 24 words, the ask is buried under expansions, and the extra model name makes it read like "which layer is this?", so a learner types a layer number (fails tests 1, 2, 3 and 5). It also packs in two facts, the function and the TCP/IP name (fails test 4).

Passes, as two cards:

| Front | Back | Notes |
|---|---|---|
| What does the Open Systems Interconnection (OSI) network layer (Layer 3) do? | Addressing and routing between networks | It gives hosts logical (IP) addresses and lets routers pick paths between networks. Not Layer 4, which is transport: it uses ports to reach programs on a host. |
| What is the OSI network layer called in the Transmission Control Protocol/Internet Protocol (TCP/IP) model? | The internet layer | The two models are separate, so their layers correspond rather than match exactly. |

A contrast card must still ask one thing: "What do Layer 3 addresses identify: a host or a program?" and "...Layer 4 ports...?" are two cards, not one.

## File format

Tab-separated UTF-8, one note per line. Columns: `guid`, `front`, `back`, `notes`, `tags`.

```
#separator:tab
#html:true
#guid column:1
#notetype:Typed answer + Notes
#deck:<Course>::<Lesson name>
#tags column:5
<guid>	<front html>	<back plain text>	<notes html>	<space-separated tags>
```

- No tab or newline inside a field. In the front and notes, use `<br>` for line breaks, `<code>` for addresses, commands and hex, and `<b>` for the key term. The back is plain text, so no `<`, `>` or `&`.
- `guid` is stable and unique, e.g. `co5023f-0003-07`. Re-importing an edited deck updates notes with the same guid instead of duplicating them, so edit cards in place, append new cards with new guids, and never renumber. Deleting a row does not delete the note in Anki; the user has to delete it there.
- Use a guid prefix that no older deck with a different note type used, so the notes import as new rather than clashing.
- Older 4-column decks on the note type `Front and back (Typing)` (no notes) still validate and build. To upgrade one, add the notes column, change the two headers, and give every card a new guid prefix; tell the user to delete the old deck in Anki before importing.
- Tags have no spaces inside them, e.g. `networking lesson-0003 ipv4`.
- `::` nests decks, so each lesson becomes a subdeck of the course deck.

## Importing from the command line (only when the user asks)

Usually File > Import is enough. If the user asks you to do it:

1. Close Anki (macOS: `osascript -e 'quit app "Anki"'`, then wait until `pgrep -x Anki` prints nothing; a "User cancelled" error is harmless if Anki closes). Back up the profile folder first.
2. The collection is `<Anki2 folder>/<profile>/collection.anki2`. The Anki2 folder is `~/Library/Application Support/Anki2` on macOS, `~/.local/share/Anki2` on Linux, `%APPDATA%\Anki2` on Windows.
3. In a venv outside the user's folders, `pip install anki==<their Anki version>` (a newer version can upgrade the collection so their Anki can't open it), then:
   ```python
   from anki.collection import Collection, ImportAnkiPackageRequest, ImportAnkiPackageOptions
   col = Collection(collection_path)
   # Only if the user asked to remove old cards, and only their deck. Never find_notes(""), which is the whole collection.
   # col.remove_notes(col.find_notes('deck:"Course::Lesson"'))
   col.import_anki_package(ImportAnkiPackageRequest(package_path=apkg_path, options=ImportAnkiPackageOptions()))
   col.close()
   ```
4. Reopen Anki.

AnkiConnect (add-on `2055492159`) is the alternative when Anki has to stay open.

## Styling

`build_apkg.py` ships CSS for the note type: light and dark mode, a transparent typed-answer box (some themes and add-ons draw it as a white box), a green/red/grey diff, and the Notes in a softer box under the answer. If the user reports a white answer box or a glaring white card in dark mode, re-import the rebuilt `.apkg`, or paste the CSS from the script into Tools > Manage Note Types > Typed answer + Notes > Cards > Styling.
