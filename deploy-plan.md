# Plan: Host on GitHub Pages under datatrove-edu

## Context
The Hugo site at `/Users/enriqueacosta/Dropbox/hugo-datasets-portal` is not yet a git repo. The goal is to publish it under a new GitHub account/org named `datatrove-edu`, with automatic re-deployment on every push to `main`. The current CI workflow (`peaceiris/actions-hugo` + `peaceiris/actions-gh-pages`) already handles this pattern well.

---

## Decision 1: GitHub account type

| | Personal account | Organization |
|---|---|---|
| Create | Sign up new GitHub account as `datatrove-edu` | Create org from your existing account |
| Control | Only `datatrove-edu` account can push | You (enriqueacosta) remain owner, can add collaborators |
| Cost | Free | Free |
| **Recommendation** | Simpler if solo | Better if you want to collaborate or keep it separate from your personal GitHub |

---

## Decision 2: URL structure (most important)

### Option A — User/Org Pages: `https://datatrove-edu.github.io/` ✅ Recommended
- **Repo name must be** `datatrove-edu.github.io` (GitHub convention for root pages)
- `baseURL = "/"` in `config.toml` — **no change needed**
- Clean, professional URL
- Tradeoff: repo name is `datatrove-edu.github.io`, not `datatrove-edu`

### Option B — Project Pages: `https://datatrove-edu.github.io/datatrove-edu/`
- Repo name is `datatrove-edu` (matches your preference)
- `baseURL` must change to `"/datatrove-edu/"` in `config.toml`
- URL has awkward repeated segment (`/datatrove-edu/datatrove-edu` is not a thing, but the path is still redundant-feeling)
- Tradeoff: requires a `baseURL` change; all asset/link paths shift

### Option C — Custom domain: `https://datatrove-edu.com/` (or similar)
- Any repo name works; `baseURL` = your domain
- Requires purchasing and configuring a domain + DNS CNAME record
- Adds a `CNAME` file to repo

---

## Decision 3: CI/CD workflow

The existing `.github/workflows/build.yml` works as-is in the new repo — no changes needed. It:
1. Validates tags with Python
2. Builds with Hugo 0.128.1
3. Pushes built output to a `gh-pages` branch via `peaceiris/actions-gh-pages`
4. GitHub Pages serves from that branch

The only alternative is GitHub's newer native Pages Actions (`actions/upload-pages-artifact` + `actions/deploy-pages`) — no `gh-pages` branch, cleaner — but it's extra work for no meaningful benefit here.

---

## What needs to happen (regardless of option chosen)

1. `git init` the local repo, add remote pointing to the new GitHub repo
2. Update `baseURL` in `config.toml` if using Option B or C
3. Add a `CNAME` file if using Option C
4. In the new repo's **Settings → Pages**: set source to the `gh-pages` branch (Actions will create it on first push)
5. Push `main` — the workflow fires automatically and publishes the site

**Note:** This repo currently lives in Dropbox. That's fine for source — Dropbox syncs the source files, git tracks changes, GitHub Pages hosts the output. No conflict.
