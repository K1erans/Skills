---
name: pre-pr
description: Before opening a PR, check the branch against its issue, run the checks, and open a one-page HTML summary that tells the change as a story: API contracts and types first, then the flow, behaviour, key code, caveats and files. Use when the user says "pre-pr", asks if an issue is finished, or wants a review summary before a PR.
---

1. **Check it's done.** Read the issue (`gh issue view <N>`) and the diff against main. Go through each acceptance criterion; list anything missing and ask before building the page.
2. **Run the checks.** Type check, lint, and unit tests (see `package.json` scripts). Report failures as they are; don't hide them.
3. **Build the page.** Copy [template.html](template.html) to the scratchpad as `<branch>-summary.html` and fill it in. The page tells one story, outside in: the edges first, then the types, the journey, the behaviour, the code, and the loose ends. Number each heading (`<span class="num">N</span>`) and open each section with one italic bridge sentence linking it to the one before. Sections, in order:
   1. **Summary**: what it delivers and the check results.
   2. **API contracts**: every boundary the change touches, as a table (contract · direction · outgoing type · incoming type · checked at runtime? · compatible?), then the exact shapes and the type definitions behind each. Flag any payload that crosses untyped or unchecked. Covers the public API, messages between components, requests sent to external services or processes, contributed settings/commands, and persisted state keys. Say explicitly when the public API is unchanged.
   3. **Data types**: every type the change adds or changes (schemas, structs, interfaces, enums), copied exactly, each with its file and one line on what it holds. Mark new or changed fields `// new`.
   4. **How it flows**: one small Mermaid diagram.
   5. **Behaviour** (optional): tables for mappings or per-case rules, with bullets for the non-obvious rows.
   6. **Key code**: every part of the change, grouped by layer in the same order as the flow. Copy the code exactly from the source; cut long functions with `// …` and label them "(excerpt)". Mark **key** the parts that enforce a requirement, would surprise a reviewer, or are where a safety decision is made.
   7. **What changed**, then **Caveats**: include what wasn't tested.
   8. **Important files**: reference at the end, one row per file, new files marked.
4. **Open it** with `open <file>` and give the user a few lines on what's in it.

Don't commit or open the PR unless asked.
