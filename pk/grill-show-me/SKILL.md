---
name: grill-show-me
description: Grill the user with a picture of the options for every question, lens by lens through product, architecture, program design and edge cases, recording ADRs and the glossary as decisions settle. Use when the user wants a plan grilled visually or end to end, or says "grill and show me".
---

Run a `/grilling` session using the `/domain-modeling` skill, and pair every question with a `/show-me` visual.

## Each question

Put one decision to the user as one sentence, then draw **the options**: the smallest visual that makes them concrete. Draw each option in the same form, side by side, so the decision is the only thing that differs. When the options change something already settled, draw them as a `diff` against the settled picture. Mark your recommended option in the picture and give the one reason that decides it.

Some questions can only be answered once another lens has been settled. **Park** those in a list under the lens that owns them, and bring them up when that lens runs.

## The settled picture

Keep one running picture of everything decided so far, in the form the lens names. After each answer, show what changed as a `diff`. The picture is the shared understanding you can see: a decision isn't settled until it can be drawn in.

When the session ends, show the full settled picture once and ask the user to confirm it.

## Lenses

A lens limits the session to one region of the design tree. If the session started with a lens, stay in it. Otherwise, work through all four in this order, because each one settles decisions the next one depends on:

1. [Product](../grill-product/SKILL.md): what the user sees and does
2. [Architecture](../grill-architecture/SKILL.md): where things live and how a request travels
3. [Program design](../grill-program-design/SKILL.md): types, signatures, seams and tests
4. [Edge cases](../grill-edge-cases/SKILL.md): everything off the happy path

Move to the next lens only when the current lens's completion criterion holds. Carry its settled picture forward as input.
