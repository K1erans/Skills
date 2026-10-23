---
name: grill-program-design
description: Grill a plan through the program design lens (types, method signatures, seams, test approach), with a picture for every question. Use when the user wants a module's interface or test strategy stress-tested.
---

Run a `/grill-show-me` session through the **program design** lens. This lens covers the code a developer will write against: types and method signatures, test approaches and seams. Use the `/codebase-design` vocabulary for interface depth and the `/tdd` vocabulary for tests.

## Branches

- **Types**: the domain types, their fields, and which states they can represent. Make illegal states unrepresentable.
- **Signatures**: for each public function, its name, parameters, return type, whether it's sync or async, and how it fails (throws, returns a Result, or returns null).
- **Depth**: how much each module hides. Aim for a small interface over a large implementation.
- **Seams**: where a test swaps in a fake, which dependencies are injected, and which run for real.
- **Test approach**: for each module, unit, integration or end-to-end; what gets tested through the public interface; and the first test to write.
- **Names**: use the words settled in the product lens.

## Pictures

- Types and signatures as TypeScript blocks: the whole block when it's new, a `diff` when it changes
- Competing signatures side by side, each with one call site that shows how it reads in use
- A call tree with each seam marked
- Tests as a list of `it("...")` names, plus one test body that shows the seam in use

## Settled picture

The public interface of every module as type signatures with seams marked, plus the list of test names.

## Done when

Every module from the architecture lens has its public signatures written, every external dependency has either a seam or an explicit "tested for real", and every flow has at least one named test.
