# Skills

Skills I use for my agents.

Personal skills live in [`pk/`](pk/).

| Skill | Description |
| --- | --- |
| [`agents-sdk`](agents-sdk/) | Build AI agents on Cloudflare Workers using the Agents SDK. Load when creating stateful agents, durable workflows, real-time WebSocket apps, scheduled tasks, MC |
| [`anki-flashcards`](anki-flashcards/) | Turn a lesson, notes or topic into a quality-checked Anki deck of atomic, self-contained typed-answer flashcards (a tab-separated .txt plus an importable .apkg) |
| [`ask-matt`](ask-matt/) | Ask which skill or flow fits your situation. A router over the skills in this repo. |
| [`batch-grill-me`](batch-grill-me/) | A relentless interview that asks every frontier question at once, round by round. |
| [`brandkit`](brandkit/) | Premium brand-kit image generation skill for creating high-end brand-guidelines boards, logo systems, identity decks, and visual-world presentations. Trained fo |
| [`claude-handoff`](claude-handoff/) | Hand the current conversation off to a fresh background agent that picks up the work immediately. |
| [`cloudflare-email-service`](cloudflare-email-service/) | Send and receive transactional emails with Cloudflare Email Service (Email Sending + Email Routing). Use when building email sending (Workers binding or REST AP |
| [`cloudflare-one-migrations`](cloudflare-one-migrations/) | Plans migrations from Zscaler ZIA/ZPA, Palo Alto, legacy VPN, SWG, or SASE stacks to Cloudflare One. Use for migration assessments, policy mapping, rollout plan |
| [`cloudflare-one`](cloudflare-one/) | Guides Cloudflare One Zero Trust and SASE work across Access, Gateway, WARP, Tunnel, Cloudflare WAN, DLP, CASB, device posture, and identity. Use when designing |
| [`cloudflare`](cloudflare/) | Comprehensive Cloudflare platform skill covering Workers, Pages, storage (KV, D1, R2), AI (Workers AI, Vectorize, Agents SDK), feature flags (Flagship), network |
| [`code-review`](code-review/) | Review the changes since a fixed point (commit, branch, tag, or merge-base) along two axes — Standards (does the code follow this repo's documented coding stand |
| [`codebase-design`](codebase-design/) | Shared vocabulary for designing deep modules. Use when the user wants to design or improve a module's interface, find deepening opportunities, decide where a se |
| [`design-an-interface`](design-an-interface/) | Generate multiple radically different interface designs for a module using parallel sub-agents. Use when user wants to design an API, explore interface options, |
| [`design-taste-frontend-v1`](design-taste-frontend-v1/) | The original v1 taste-skill, preserved for projects depending on its exact behavior. The current default is `design-taste-frontend` (v2 experimental), which is  |
| [`design-taste-frontend`](design-taste-frontend/) | Anti-slop frontend skill for landing pages, portfolios, and redesigns. The agent reads the brief, infers the right design direction, and ships interfaces that d |
| [`diagnosing-bugs`](diagnosing-bugs/) | Diagnosis loop for hard bugs and performance regressions. Use when the user says "diagnose"/"debug this", or reports something broken/throwing/failing/slow. |
| [`domain-modeling`](domain-modeling/) | Build and sharpen a project's domain model. Use when the user wants to pin down domain terminology or a ubiquitous language, record an architectural decision, o |
| [`durable-objects`](durable-objects/) | Create and review Cloudflare Durable Objects. Use when building stateful coordination (chat rooms, multiplayer games, booking systems), implementing RPC methods |
| [`edit-article`](edit-article/) | Edit and improve articles by restructuring sections, improving clarity, and tightening prose. Use when user wants to edit, revise, or improve an article draft. |
| [`full-output-enforcement`](full-output-enforcement/) | Overrides default LLM truncation behavior. Enforces complete code generation, bans placeholder patterns, and handles token-limit splits cleanly. Apply to any ta |
| [`git-guardrails-claude-code`](git-guardrails-claude-code/) | Set up Claude Code hooks to block dangerous git commands (push, reset --hard, clean, branch -D, etc.) before they execute. Use when user wants to prevent destru |
| [`gpt-taste`](gpt-taste/) | Elite UX/UI & Advanced GSAP Motion Engineer. Enforces Python-driven true randomization for layout variance, strict AIDA page structure, wide editorial typograph |
| [`grill-architecture`](grill-architecture/) | Grill a plan through the architecture lens (program layout, state ownership, call stacks, boundaries), with a picture for every question. Use when the user want |
| [`grill-edge-cases`](grill-edge-cases/) | Hunt the edge cases in a plan and decide each one (inputs, time, concurrency, failure, people, change), with a picture for every question. Use when the user ask |
| [`grill-me`](grill-me/) | A relentless interview to sharpen a plan or design. |
| [`grill-product`](grill-product/) | Grill a plan through the product lens (users, scope, flows, states, wording), with a picture for every question. Use when the user wants the product or user exp |
| [`grill-program-design`](grill-program-design/) | Grill a plan through the program design lens (types, method signatures, seams, test approach), with a picture for every question. Use when the user wants a modu |
| [`grill-show-me`](grill-show-me/) | Grill the user with a picture of the options for every question, lens by lens through product, architecture, program design and edge cases, recording ADRs and t |
| [`grill-with-docs`](grill-with-docs/) | A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) as we go. |
| [`grilling`](grilling/) | Grill the user relentlessly about a plan, decision, or idea. Use when the user wants to stress-test their thinking, or uses any 'grill' trigger phrases. |
| [`handoff`](handoff/) | Compact the current conversation into a handoff document for another agent to pick up. |
| [`high-end-visual-design`](high-end-visual-design/) | Teaches the AI to design like a high-end agency. Defines the exact fonts, spacing, shadows, card structures, and animations that make a website feel expensive.  |
| [`image-to-code`](image-to-code/) | Elite website image-to-code skill for Codex. For visually important web tasks, it must first generate the design image(s) itself, deeply analyze them, then impl |
| [`imagegen-frontend-mobile`](imagegen-frontend-mobile/) | Elite mobile app image-generation skill for creating premium, app-native screen concepts and flows. Designed for iOS, Android, and cross-platform mobile product |
| [`imagegen-frontend-web`](imagegen-frontend-web/) | Elite frontend image-direction skill for generating premium, conversion-aware website design references. CRITICAL OUTPUT RULE — generate ONE separate horizontal |
| [`implement`](implement/) | Implement a piece of work based on a spec or set of tickets. |
| [`improve-codebase-architecture`](improve-codebase-architecture/) | Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick. |
| [`industrial-brutalist-ui`](industrial-brutalist-ui/) | Raw mechanical interfaces fusing Swiss typographic print with military terminal aesthetics. Rigid grids, extreme type scale contrast, utilitarian color, analog  |
| [`install-anti-slop`](install-anti-slop/) | Install and configure the anti-slop Oxlint plugin in a local TypeScript or JavaScript repository. Use whenever a user asks to add anti-slop lint rules, copy the |
| [`jrep-reuse`](jrep-reuse/) | Before writing a new function, method, type or helper, run `jrep reuse` to check whether existing code already does it or could be extended to, so you build on  |
| [`jrep`](jrep/) | Find code by what it does with jrep, scoped to the folders most likely to hold it so each search costs less. Use when looking for where a behaviour is implement |
| [`loop-me`](loop-me/) | Grill me about specs for the workflows I want to build, within this workspace. |
| [`migrate-to-shoehorn`](migrate-to-shoehorn/) | Migrate test files from `as` type assertions to @total-typescript/shoehorn. Use when user mentions shoehorn, wants to replace `as` in tests, or needs partial te |
| [`minimalist-ui`](minimalist-ui/) | Clean editorial-style interfaces. Warm monochrome palette, typographic contrast, flat bento grids, muted pastels. No gradients, no heavy shadows. |
| [`obsidian-vault`](obsidian-vault/) | Search, create, and manage notes in the Obsidian vault with wikilinks and index notes. Use when user wants to find, create, or organize notes in Obsidian. |
| [`planetscale-autonomous-execution-mode`](planetscale-autonomous-execution-mode/) | Execute approved PlanetScale changes end-to-end without per-step approval when the operator has explicitly acknowledged the risk. Defines the risk-acknowledgmen |
| [`planetscale-best-practices-matrix`](planetscale-best-practices-matrix/) | A concise feature matrix for deciding which PlanetScale safety, observability, and automation recommendations apply by engine. |
| [`planetscale-change-gates-and-approval-contract`](planetscale-change-gates-and-approval-contract/) | Enforce explicit approval gates for any PlanetScale, database, repository, credential, network, or automation mutation. |
| [`planetscale-codebase-sqlcommenter-instrumentation`](planetscale-codebase-sqlcommenter-instrumentation/) | Inspect an application repository connected to PlanetScale and recommend SQLCommenter-compatible query tagging packages and conventions. |
| [`planetscale-customer-report-template`](planetscale-customer-report-template/) | Produce the final PlanetScale best-practices report after running the inventory and relevant review skills. |
| [`planetscale-mcp-agent-operating-model`](planetscale-mcp-agent-operating-model/) | Configure safe agent behavior around PlanetScale MCP, Insights, schema recommendations, and repository work without autonomous production mutation. |
| [`planetscale-postgres-safety-review`](planetscale-postgres-safety-review/) | Review PlanetScale Postgres for Traffic Control, query tags, roles, pg_strict, backups/PITR, private connectivity, webhooks, branches, and safe agent operation. |
| [`planetscale-pscale-cli-automation`](planetscale-pscale-cli-automation/) | Use the PlanetScale CLI (pscale) from automated agents with --format json, auth check, pscale sql, and per-command --force. Run before other PlanetScale skills |
| [`planetscale-query-insights-and-tags`](planetscale-query-insights-and-tags/) | Use PlanetScale Insights and SQLCommenter-style query tags to attribute database load, identify risky queries, and prepare safe Traffic Control or schema recomm |
| [`planetscale-readonly-inventory`](planetscale-readonly-inventory/) | Collect read-only evidence about PlanetScale org, database, branches, webhooks, backups, roles, Insights, recommendations, and traffic configuration. |
| [`planetscale-safe-orchestrator`](planetscale-safe-orchestrator/) | Master skill that runs the full PlanetScale safe best-practices assessment — inventory, engine review, Insights, Traffic Control, webhooks, schema recommendatio |
| [`planetscale-schema-recommendations-agent-loop`](planetscale-schema-recommendations-agent-loop/) | Safely triage PlanetScale schema recommendations and turn them into reviewed branches, migrations, issues, or pull requests without applying production changes. |
| [`planetscale-traffic-control-recommendations`](planetscale-traffic-control-recommendations/) | Build a safe recommendation plan for PlanetScale Postgres Database Traffic Control budgets and rules without applying them. |
| [`planetscale-vitess-safety-review`](planetscale-vitess-safety-review/) | Review a PlanetScale Vitess database for safe migrations, deploy requests, schema recommendations, Insights, webhooks, and operational safety. |
| [`planetscale-webhook-automation-recommendations`](planetscale-webhook-automation-recommendations/) | Recommend webhook subscriptions and safe automation patterns for PlanetScale alerts, anomalies, schema recommendations, deploy requests, and agent workflows. |
| [`post-pr`](post-pr/) | After a PR is reviewed (Greptile, bots or people), explain each review finding in plain terms: what it means, a concrete scenario of what would go wrong, whethe |
| [`pre-pr`](pre-pr/) | Before opening a PR, check the branch against its issue, run the checks, and open a one-page HTML summary that tells the change as a story: API contracts and ty |
| [`prototype`](prototype/) | Build a throwaway prototype to answer a design question. Use when the user wants to sanity-check whether a state model or logic feels right, or explore what a U |
| [`qa`](qa/) | Interactive QA session where user reports bugs or issues conversationally, and the agent files GitHub issues. Explores the codebase in the background for contex |
| [`redesign-existing-projects`](redesign-existing-projects/) | Upgrades existing websites and apps to premium quality. Audits current design, identifies generic AI patterns, and applies high-end design standards without bre |
| [`request-refactor-plan`](request-refactor-plan/) | Create a detailed refactor plan with tiny commits via user interview, then file it as a GitHub issue. Use when user wants to plan a refactor, create a refactori |
| [`research`](research/) | Investigate a question against high-trust primary sources and capture the findings as a Markdown file in the repo. Use when the user wants a topic researched, d |
| [`resolving-merge-conflicts`](resolving-merge-conflicts/) | Use when you need to resolve an in-progress git merge/rebase conflict. |
| [`sandbox-migrate-to-next`](sandbox-migrate-to-next/) | Use when porting a Cloudflare Sandbox app from stable @cloudflare/sandbox to @cloudflare/sandbox@next (Sandbox SDK 1.0 preview), or when the user asks to migrat |
| [`sandbox-next`](sandbox-next/) | Use when building or changing Cloudflare Sandbox apps on @cloudflare/sandbox@next (Sandbox SDK 1.0 preview)—code execution, AI runners, interpreters, CI-like jo |
| [`sandbox-stable`](sandbox-stable/) | Use when building or changing Cloudflare Sandbox apps on the current stable @cloudflare/sandbox package (default npm tag)—commands, sessions, files, ports, tunn |
| [`scaffold-exercises`](scaffold-exercises/) | Create exercise directory structures with sections, problems, solutions, and explainers that pass linting. Use when user wants to scaffold exercises, create exe |
| [`setup-matt-pocock-skills`](setup-matt-pocock-skills/) | Configure this repo for the engineering skills — set up its issue tracker, triage label vocabulary, and domain doc layout. Run once before first use of the othe |
| [`setup-pre-commit`](setup-pre-commit/) | Set up Husky pre-commit hooks with lint-staged (Prettier), type checking, and tests in the current repo. Use when user wants to add pre-commit hooks, set up Hus |
| [`setup-ts-deep-modules`](setup-ts-deep-modules/) | Wire dependency-cruiser into a TypeScript repo so each package is a deep module — implementation hidden in subfolders, reachable only through its entry-point fi |
| [`ship-nightly`](ship-nightly/) | Put finished Kode work on main and rebuild the Kode (Nightly) desktop app from the K1erans/Kode fork. Use when the user says "put it on main", "rebuild", "ship  |
| [`show-me`](show-me/) | Help the user understand the current topic visually with concise diagrams, code-shape sketches, and focused HTML artifacts. |
| [`stitch-design-taste`](stitch-design-taste/) | Semantic Design System Skill for Google Stitch. Generates agent-friendly DESIGN.md files that enforce premium, anti-generic UI standards — strict typography, ca |
| [`tdd`](tdd/) | Test-driven development. Use when the user wants to build features or fix bugs test-first, mentions "red-green-refactor", or wants integration tests. |
| [`teach`](teach/) | Teach the user a new skill or concept, within this workspace. |
| [`tldraw-offline`](tldraw-offline/) | Operate the user's tldraw offline canvas app, including open .tldraw or .tldr files. Use whenever a task involves inspecting, editing, arranging, connecting, li |
| [`to-questionnaire`](to-questionnaire/) | Turn a decision you can't fully answer into a questionnaire for someone else to fill in. |
| [`to-spec`](to-spec/) | Turn the current conversation into a spec and publish it to the project issue tracker — no interview, just synthesis of what you've already discussed. |
| [`to-tickets`](to-tickets/) | Break a plan, spec, or the current conversation into a set of tracer-bullet tickets, each declaring its blocking edges, published to the configured tracker — ed |
| [`triage`](triage/) | Move issues and external PRs through a state machine of triage roles — categorise, verify, grill if needed, and write agent-ready briefs. |
| [`turnstile-spin`](turnstile-spin/) | Set up Cloudflare Turnstile end-to-end in a project. Scan the codebase, create the widget via the Cloudflare API, embed it where user requests need bot verifica |
| [`ubiquitous-language`](ubiquitous-language/) | Extract a DDD-style ubiquitous language glossary from the current conversation, flagging ambiguities and proposing canonical terms. Saves to UBIQUITOUS_LANGUAGE |
| [`vercel-react-best-practices`](vercel-react-best-practices/) | React and Next.js performance optimization guidelines from Vercel Engineering. This skill should be used when writing, reviewing, or refactoring React/Next.js c |
| [`wayfinder`](wayfinder/) | Plan a huge chunk of work — more than one agent session can hold — as a shared map of decision tickets on your issue tracker, and resolve them one at a time unt |
| [`web-design-guidelines`](web-design-guidelines/) | Review UI code for Web Interface Guidelines compliance. Use when asked to "review my UI", "check accessibility", "audit design", "review UX", or "check my site  |
| [`web-perf`](web-perf/) | Analyzes web performance using Chrome DevTools MCP. Measures Core Web Vitals (LCP, INP, CLS) and supplementary metrics (FCP, TBT, Speed Index), identifies rende |
| [`wizard`](wizard/) | Generate an interactive bash wizard that walks a human through a manual procedure — third-party setup, a one-off migration, an A→B state transition — opening UR |
| [`workers-best-practices`](workers-best-practices/) | Reviews and authors Cloudflare Workers code against production best practices. Load when writing new Workers, reviewing Worker code, configuring wrangler.jsonc, |
| [`wrangler`](wrangler/) | Cloudflare Workers CLI for deploying, developing, and managing Workers, KV, R2, D1, Vectorize, Hyperdrive, Workers AI, Containers, Queues, Workflows, Pipelines, |
| [`writing-beats`](writing-beats/) | Writing, exploit — assemble raw material into a journey of beats, grounding each term before a beat leans on it. |
| [`writing-fragments`](writing-fragments/) | Writing, explore — mine raw fragments, no structure yet. |
| [`writing-great-skills`](writing-great-skills/) | Reference for writing and editing skills well — the vocabulary and principles that make a skill predictable. |
| [`writing-shape`](writing-shape/) | Writing, exploit — shape raw material into an article, paragraph by paragraph. |
