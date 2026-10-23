---
name: post-pr
description: After a PR is reviewed (Greptile, bots or people), explain each review finding in plain terms: what it means, a concrete scenario of what would go wrong, whether it is real, and how to fix it. Use when the user says "post-pr", asks what review comments mean, or wants PR findings explained.
---

1. **Collect the findings.** `gh pr view <N> --json reviews,comments` and `gh api repos/{owner}/{repo}/pulls/<N>/comments`. Include the check status (`gh pr checks <N>`).
2. **Verify each one against the code.** Read the lines it points at and follow the path it describes. Decide: **real**, **partly real** (say which part), or **not real** (say why). Never repeat the reviewer's claim unchecked.
3. **Explain each finding**, most severe first:
   - **What it means**, in one or two plain sentences, with no jargon the user hasn't used.
   - **What would happen**: one concrete scenario, step by step, ending in what the user or a user of the product would actually see or lose.
   - **How likely and how bad**: who can trigger it, how often, and the worst outcome (security, data, UX, none).
   - **Verdict** (real / partly / not), with the evidence: `file:line`.
   - **Fix**: the smallest change that closes it, and what it costs.
4. **End with a recommendation**: which to fix before merging, which can wait, which to push back on. Ask before changing code.
