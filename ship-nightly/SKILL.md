---
name: ship-nightly
description: Put finished Kode work on main and rebuild the Kode (Nightly) desktop app from the K1erans/Kode fork. Use when the user says "put it on main", "rebuild", "ship it", "cut a nightly", or wants their installed nightly app to pick up a change.
---

# Ship a Kode nightly

The installed `/Applications/Kode (Nightly).app` updates itself from prereleases on
`K1erans/Kode` (channel `nightly`, see its `Contents/Resources/app-update.yml`). The
`fork-release.yml` workflow builds those prereleases from `main` on GitHub. So "rebuild"
means: get the commit onto `main`, push it, then dispatch that workflow. Nothing is
installed by hand, and a local `vp run dist:desktop:*` build never reaches the app.

Run everything from the t3code checkout (`origin` is `K1erans/t3code`, which redirects
to `K1erans/Kode`).

## 1. Commit on a branch

If there is uncommitted work the user wants shipped, branch off `main` first, then commit
with a conventional, plain-language title and the attribution line from the session:

```bash
git switch -c <type>/<short-name>
git add <files>
git commit -F - <<'EOF'
feat(web): <what the user can now do>

<The problem in a sentence or two, then the fix.>

Co-Authored-By: <model attribution>
EOF
```

The pre-commit hook runs `vp fmt` on staged files. Skip this step if the work is already
committed.

## 2. Put it on main

```bash
git switch main
git pull --ff-only origin main
git merge --ff-only <branch>
git branch -d <branch>
```

`--ff-only` fails rather than creating a merge commit. If it fails, rebase the branch onto
`main` and retry. Never force-push `main`.

## 3. Push

```bash
git push origin main
```

The build runs from GitHub's `main`, so this push is what puts the change in the build.

## 4. Dispatch the build

```bash
gh workflow run fork-release.yml -R K1erans/Kode --ref main
```

Always pass `-R K1erans/Kode`. Without it `gh` resolves to upstream `pingdotgg/t3code` and
returns 404 for the workflow.

## 5. Wait and confirm

```bash
gh run list -R K1erans/Kode -w fork-release.yml -L 1 --json databaseId,status,headSha,url
```

Check `headSha` matches the pushed commit and give the user the run URL. Then wait in the
background (runs take about 4-5 minutes), not with a polling loop:

```bash
gh run watch <id> -R K1erans/Kode --exit-status --interval 30 > /dev/null 2>&1; \
  gh run view <id> -R K1erans/Kode --json conclusion -q .conclusion
```

On success, report the new release name:

```bash
gh release list -R K1erans/Kode -L 1
```

It looks like `v0.0.42-nightly.20261002.100015`. The installed app offers it on its next
update check.

## When it goes wrong

- **App says it is up to date but a newer release exists:** the private-repo updater only
  reads the first prerelease in `gh api repos/K1erans/Kode/releases --jq '.[].tag_name'`, and
  GitHub orders that list by tag name as text. If the newest build is not first, that is
  the bug. Builds are numbered `100000 + run` so tags stay one width; an older-style tag
  (`.9`) can still outrank newer ones on the same date.

- **Signing or notarization failure:** a repository secret is missing or expired
  (`CSC_LINK`, `CSC_KEY_PASSWORD`, `APPLE_API_KEY`, `APPLE_API_KEY_ID`, `APPLE_API_ISSUER`).
  Tell the user which step failed; you cannot fix secrets.
- **Any other failure:** read the failing step with
  `gh run view <id> -R K1erans/Kode --log-failed` and report it before changing code.
- **A second dispatch while one runs:** it queues behind the first
  (`cancel-in-progress: false`). Don't cancel runs to "speed things up".
