#!/usr/bin/env python3
"""Build an Anki .apkg from a typed-answer deck .txt (5 columns: guid, front, back, notes, tags).

Older 4-column decks (guid, front, back, tags) still build with the old note type.
Needs genanki:  python3 -m venv v && v/bin/pip install genanki && v/bin/python build_apkg.py deck.txt
The note type is created inside the .apkg, because Anki cannot create a note type from a text import.
"""
import hashlib
import sys

import genanki

CSS = """
.card { font-family: -apple-system, Arial, sans-serif; font-size: 20px; line-height: 1.45;
  text-align: left; color: #1c1c1e; background: #ffffff; }
.nightMode.card, .night_mode.card { color: #e8e8ea; background: #1e1e20; }
code { background: rgba(127,127,127,.18); padding: 0 4px; border-radius: 4px; font-size: .92em; }
hr#answer { border: none; border-top: 1px solid rgba(127,127,127,.35); margin: 14px 0; }
input#typeans, code#typeans { background: transparent !important; color: inherit !important;
  font-family: inherit !important; font-size: inherit !important; border: none !important;
  border-bottom: 1px solid rgba(127,127,127,.5) !important; padding: 2px 0 !important; width: 100%; }
.typeGood { background: transparent !important; color: #2e9e4f !important; }
.typeBad { background: transparent !important; color: #d64545 !important; }
.typeMissed { background: transparent !important; color: #8e8e93 !important; }
.notes { margin-top: 14px; padding: 10px 14px; border-radius: 8px; font-size: 17px;
  background: rgba(127,127,127,.12); color: inherit; opacity: .92; }
"""

NEW = genanki.Model(
    1607392321,
    "Typed answer + Notes",
    fields=[{"name": "Front"}, {"name": "Back"}, {"name": "Notes"}],
    templates=[{
        "name": "Typed answer",
        "qfmt": "{{Front}}<br><br>{{type:Back}}",
        "afmt": "{{Front}}<hr id=answer>{{type:Back}}<div class=notes>{{Notes}}</div>",
    }],
    css=CSS,
)

OLD = genanki.Model(
    1607392320,
    "Front and back (Typing)",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{
        "name": "Typed answer",
        "qfmt": "{{Front}}<br><br>{{type:Back}}",
        "afmt": "{{Front}}<hr id=answer>{{type:Back}}",
    }],
    css=CSS,
)

for path in sys.argv[1:]:
    deck_name, rows, new = None, [], False
    for line in open(path, encoding="utf-8").read().split("\n"):
        if line.startswith("#deck:"):
            deck_name = line[len("#deck:"):]
        elif line.startswith("#notetype:"):
            new = line[len("#notetype:"):] == "Typed answer + Notes"
        elif line and not line.startswith("#"):
            rows.append(line.split("\t"))
    deck_id = int(hashlib.sha1(deck_name.encode()).hexdigest()[:8], 16)
    deck = genanki.Deck(deck_id, deck_name)
    for row in rows:
        if new:
            guid, front, back, notes, tags = row
            deck.add_note(genanki.Note(model=NEW, fields=[front, back, notes], tags=tags.split(), guid=guid))
        else:
            guid, front, back, tags = row
            deck.add_note(genanki.Note(model=OLD, fields=[front, back], tags=tags.split(), guid=guid))
    out = path.rsplit(".", 1)[0] + ".apkg"
    genanki.Package(deck).write_to_file(out)
    print(f"{out}: {len(rows)} notes")
