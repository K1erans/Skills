---
name: grill-product
description: Grill a plan through the product lens (users, scope, flows, states, wording), with a picture for every question. Use when the user wants the product or user experience of a plan stress-tested.
---

Run a `/grill-show-me` session through the **product** lens. This lens covers the change as the user experiences it, from the outside in. If a question depends on how the change is built, park it for architecture.

## Branches

- **Who and why**: who the user is, what job they're trying to get done, and what they do today instead.
- **Scope**: what's in, what's out, and what's later.
- **Flows**: the entry point, each step, and where the flow ends. Settle the happy path first.
- **States**: for each screen or output, what it shows when empty, loading, partial, in error, and done.
- **Words**: the names, labels and messages the user will read.
- **Done**: the observable outcome that shows the change worked.

## Pictures

- A flow as a Mermaid `flowchart`, with competing flows drawn side by side
- A screen as an ASCII wireframe or a component tree
- Competing layouts as a single HTML mockup, one option per column
- Scope as three lists: in, out, later

## Settled picture

The user flows, with the states decided for each step, plus the in/out/later scope lists.

## Done when

Every step in every flow has its states decided, every scope item is filed under in, out or later, and the user could explain the feature to a customer using only the picture.
