#!/usr/bin/env python3
"""Validate Anki tab-separated deck files made with the anki-flashcards skill.

Usage: validate_deck.py [--allow A,B] [--exclude word ...] deck.txt...
Checks the 5-column "Typed answer + Notes" format; older 4-column decks still validate.
"""
import re
import sys

HEADER = ["#separator:tab", "#html:true", "#guid column:1"]
MAX_WORDS = 12
MAX_NOTE_WORDS = 60
NEW_TYPE, OLD_TYPE = "Typed answer + Notes", "Front and back (Typing)"
# Abbreviation: 2+ capitals (IPv4, MAC, CSMA/CD) must first appear as "Full Name (AB)".
ABBREV = re.compile(r"(?<![\w/])(?:[A-Z]{2,}[A-Za-z0-9]*|[A-Z][a-z]+[0-9]+)(?:/[A-Z]{2,}[A-Za-z0-9]*)?(?![\w])")
PAREN = re.compile(r"\(((?:[A-Z]{2,}[A-Za-z0-9]*|[A-Z][a-z]+[0-9]+)(?:/[A-Z]{2,}[A-Za-z0-9]*)?)\)")
ALLOW = {"AND", "ID", "IDs", "II"}  # plain words / names, not abbreviations to expand
EXCLUDE = []


def strip_code(html):
    return re.sub(r"<code>.*?</code>", " ", html, flags=re.S)


def plain_text(html):
    return re.sub(r"<[^>]+>", " ", strip_code(html))


def unexpanded(text):
    """Return abbreviations whose first use in `text` is not inside parentheses."""
    seen, bad = set(), []
    for m in ABBREV.finditer(text):
        tok = m.group(0)
        base = tok[:-1] if tok.endswith("s") and tok[:-1] in seen else tok  # plural of one already seen
        if tok in seen or base in seen or tok in ALLOW:
            continue
        seen.add(tok)
        if m.start() == 0 or text[m.start() - 1] != "(":
            bad.append(tok)
    return bad


def check(path, all_fronts):
    errors, guids = [], set()
    lines = open(path, encoding="utf-8").read().split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    head = [l for l in lines if l.startswith("#")]
    rows = [(i + 1, l) for i, l in enumerate(lines) if not l.startswith("#") and l.strip()]
    new = f"#notetype:{NEW_TYPE}" in head
    if not new and f"#notetype:{OLD_TYPE}" not in head:
        errors.append(f"missing #notetype:{NEW_TYPE}")
    ncols = 5 if new else 4
    for h in HEADER + [f"#tags column:{ncols}"]:
        if h not in head:
            errors.append(f"missing header {h}")
    if not any(h.startswith("#deck:") for h in head):
        errors.append("missing #deck: header")
    parsed = []
    for n, line in rows:
        cols = line.split("\t")
        if len(cols) != ncols:
            errors.append(f"line {n}: expected {ncols} columns, got {len(cols)}")
            continue
        parsed.append((n, cols))
    # Abbreviations expanded as "(AB)" in some front of this deck may stay bare in backs and notes.
    expanded = set()
    for _, cols in parsed:
        expanded |= set(PAREN.findall(strip_code(cols[1])))
    for n, cols in parsed:
        guid, front, back = cols[0], cols[1], cols[2]
        notes = cols[3] if new else ""
        tags = cols[-1]
        words = len(back.split())
        if not back.strip() or words > MAX_WORDS or "<" in back or ">" in back or "&" in back:
            errors.append(f"line {n} ({guid}): typed back must be 1 to {MAX_WORDS} plain words, no < > & ({words})")
        if back.strip().endswith("."):
            errors.append(f"line {n} ({guid}): back ends with a full stop")
        if not guid or guid in guids:
            errors.append(f"line {n}: empty or duplicate guid {guid!r}")
        guids.add(guid)
        if front in all_fronts:
            errors.append(f"line {n} ({guid}): duplicate front (also in {all_fronts[front]})")
        all_fronts[front] = path
        plain = plain_text(front)
        if re.search(r"\band (what|how|why|which|when|where|who)\b", plain, re.I) or plain.count("?") > 1:
            errors.append(f"line {n} ({guid}): front asks more than one question")
        if not front.strip().endswith("?"):
            errors.append(f"line {n} ({guid}): front is not a question")
        if re.search(r"\blesson \d{4}|see above|as above|as before", front + back + notes, re.I):
            errors.append(f"line {n} ({guid}): dependent wording")
        for word in EXCLUDE:
            if re.search(rf"\b{re.escape(word)}", front + " " + back + " " + notes, re.I):
                errors.append(f"line {n} ({guid}): excluded word {word!r}")
        bad_abbr = unexpanded(plain)
        if bad_abbr:
            errors.append(f"line {n} ({guid}): front uses abbreviation without 'Full Name (AB)': {', '.join(bad_abbr)}")
        for field, text in (("back", back), ("notes", plain_text(notes))):
            bad_abbr = [a for a in unexpanded(text) if a not in expanded and a.rstrip("s") not in expanded]
            if bad_abbr:
                errors.append(f"line {n} ({guid}): {field} uses abbreviation never expanded in this deck: {', '.join(bad_abbr)}")
        if new:
            nwords = len(plain_text(notes).split())
            if nwords == 0:
                errors.append(f"line {n} ({guid}): missing notes")
            elif nwords > MAX_NOTE_WORDS:
                errors.append(f"line {n} ({guid}): notes are {nwords} words (max {MAX_NOTE_WORDS})")
        if not tags.strip():
            errors.append(f"line {n} ({guid}): missing tags")
    return len(rows), errors


# --allow A,B,C : abbreviations that may stay bare; --exclude word : repeatable, words the user ruled out
args = sys.argv[1:]
while args and args[0] in ("--allow", "--exclude"):
    if args[0] == "--allow":
        ALLOW |= set(args[1].split(","))
    else:
        EXCLUDE.append(args[1])
    args = args[2:]
bad, fronts = 0, {}
for p in args:
    count, errs = check(p, fronts)
    print(f"{p}: {count} cards, {len(errs)} problems")
    for e in errs:
        print("  -", e)
    bad += len(errs)
sys.exit(1 if bad else 0)
