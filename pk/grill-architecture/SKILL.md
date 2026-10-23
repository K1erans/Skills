---
name: grill-architecture
description: Grill a plan through the architecture lens (program layout, state ownership, call stacks, boundaries), with a picture for every question. Use when the user wants the architecture of a plan stress-tested.
---

Run a `/grill-show-me` session through the **architecture** lens. This lens covers program layout and call stacks: the modules, where each responsibility and piece of state lives, and how a request travels between them. Use the `/codebase-design` vocabulary.

The current layout is a fact, not a decision. Explore the codebase and draw it as the starting settled picture before the first question.

## Branches

- **Modules**: which modules are added or extended, and the one thing each one owns.
- **State**: where each piece of state lives, which module is its source of truth, and who can write to it.
- **Call stacks**: the path each product flow takes through the modules.
- **Boundaries**: every external system (database, network, other services, the file system), and the single module that talks to each one.
- **Dependencies**: which way the imports point, and which modules stay unaware of which.
- **Communication**: sync calls or async events, and what gets persisted at each hop.

## Pictures

- Layout as a file tree, drawn as a `diff` against the current tree
- A flow as a call tree, with competing call stacks drawn as `diff`s
- Cross-process interaction as a Mermaid `sequenceDiagram`
- Dependency direction as a Mermaid `graph`

## Settled picture

The file tree with a one-line responsibility for each module, plus a call tree for each product flow.

## Done when

Every product flow has a call stack drawn through named modules, every piece of state has exactly one owner, and every external system has exactly one module at its boundary.
