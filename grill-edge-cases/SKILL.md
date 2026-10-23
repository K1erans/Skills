---
name: grill-edge-cases
description: Hunt the edge cases in a plan and decide each one (inputs, time, concurrency, failure, people, change), with a picture for every question. Use when the user asks what could go wrong or wants edge cases grilled.
---

Run a `/grill-show-me` session through the **edge cases** lens. The plan describes the sunny day, and your job is the weather. **Hunt**: each question is one concrete scenario with specific inputs, timing or failure, followed by the options for what should happen.

Sweep every category below against each earlier lens's settled picture:

- **Product flows**: each step and state, for what the user does off-script.
- **Architecture call stacks**: each hop and each boundary, for failure, ordering and races over shared state.
- **Program design signatures**: each value a type allows that the design didn't intend, and each way a signature can fail. Use the seams to give each case its test idea.

If an earlier lens hasn't run, draw its picture from the plan and the codebase first.

When a case's answer changes an earlier decision, show the change as a `diff` to that lens's settled picture.

## Categories

- **Inputs**: empty, one, many, huge; missing, malformed, duplicate; Unicode, whitespace, very long.
- **Time**: slow responses, timeouts, time zones and DST, ordering, stale data.
- **Concurrency**: double submit, two tabs or two users, read/write races, retries and idempotency.
- **Failure**: each dependency down, failure partway through an operation, what gets left behind, how it recovers.
- **People**: permissions, the wrong user, cancelling partway through, the back button, hostile input.
- **Change**: data that existed before this change, migration, rollback, older clients.

## Pictures

- A race or timeout as a Mermaid `sequenceDiagram` with interleaved actors
- A lifecycle that can get stuck as a Mermaid `stateDiagram`
- A proposed guard as pseudocode
- The case table

## Settled picture

A case table with the columns scenario | source (flow / hop / signature) | what happens | how it's tested. Cases ruled out as "can't happen" stay in the table with the reason.

## Done when

Every category has been swept against every flow step, call-stack hop and public signature. Every row in the case table has a decided behaviour and a test idea, or the user's reason it's out of scope. Every change to an earlier decision has been drawn into that lens's picture.
