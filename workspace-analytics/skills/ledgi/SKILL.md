---
name: ledgi
description: Context about Ledgi — Nelson's UK personal finance tracker (Next.js + FastAPI + Firebase). Project overview, architecture, links, and key concepts for conversation context.
disable-model-invocation: true
---

# Ledgi — Project Context

This skill provides context about Ledgi so you can have informed conversations about it. **You do not code on this project** — delegate all coding tasks to the `coder` subagent.

## What Is Ledgi

A UK-focused personal finance tracker where users manually log accounts, investments, and property to track net worth, ISA allowances, pensions, and portfolio performance. All financial data is field-level encrypted (AES/Fernet). No bank connections — everything is manually entered.

**Monetization:** 60-day free trial, then £2.99/month or £26.99/year via Stripe.

## Links

- **GitHub:** https://github.com/nelsongallardo/planify (repo name is "planify", product name is "Ledgi")
- **Local code:** `~/projects/planify/`
- **CLI repo:** https://github.com/LedgiApp/ledgi-cli (Go/Cobra, separate public repo)
- **Claude Code skill repo:** https://github.com/LedgiApp/skills (AgentSkills standard)

## Tech Stack

| Layer | Tech |
|-------|------|
| Frontend | Next.js 16, React, TypeScript, Tailwind, shadcn/ui (Radix), React Query |
| Backend | Python, FastAPI, Pydantic |
| Database | Cloud Firestore (user-scoped: `users/{userId}/...`) |
| Auth | Firebase Authentication (human UI) + API keys `ledgi_sk_*` (agent/CLI) |
| Payments | Stripe (checkout, portal, webhooks) |
| Prices | Alpha Vantage (stocks/ETFs), CoinGecko (crypto), cached 15min in Firestore |
| CLI | Go binary (`ledgi`), installed via curl script |
| Encryption | Fernet AES, field-level on all financial data |

## Project Structure

```
~/projects/planify/
├── frontend/          # Next.js 16 app (port 3000)
├── api/               # FastAPI backend (port 8000)
├── CLAUDE.md          # Root project instructions
├── TODO.md            # Current tasks
└── plans/             # Architecture plans
```

## Architecture Overview

### Backend (api/)
- **Repository pattern:** all repos extend `BaseRepository[T]` with generic CRUD + auto-encryption
- **User-scoped data:** all docs under `users/{userId}/` in Firestore
- **Two auth systems:** Firebase JWT (human) and API key with scopes (agent/CLI)
- **Agent API** at `/api/v1/agent/` — mirrors human endpoints, uses scope-based access (`accounts:read/write`, `holdings:read/write`, `snapshots:read/write`, `isa:read/write`, `networth:read`)

### Frontend (frontend/)
- **Route groups:** `(auth)/` for login/register, `(app)/` for authenticated pages
- **Key pages:** dashboard, accounts, investments, net-worth, monthly-review, settings
- **Design:** Source Serif 4 (headings) + Inter (body), indigo-navy primary, dark mode supported

### Account Types
Cash, ISAs (Cash/S&S/Lifetime/IF), Pensions (Workplace/SIPP/State), Investments, Crypto wallets, Property, Debt (credit cards, mortgages, loans, student loans).

## Demo Mode

Public demo user (`demo_user_ledgi`) with read-only access. Seed script creates realistic UK financial data. Write endpoints return 403 for demo users.

## Agent/CLI Ecosystem

Ledgi has a full programmatic access layer:
- **API keys** created in Settings UI, format `ledgi_sk_*`, scoped permissions
- **CLI** (`ledgi`) for terminal access: `accounts list`, `holdings list`, `networth summary`, `snapshots create`, etc.
- **Claude Code skill** teaches Claude to use the CLI for read/write operations
- **Discovery files:** `llms.txt` and `.well-known/agent.json` served from frontend

## When Nelson Talks About Ledgi

Common topics you might hear about:
- Net worth tracking and snapshots
- ISA allowance calculations (UK tax year April-April)
- Monthly review flow (batch balance updates)
- Investment holdings and live prices
- The agent/CLI API and API keys
- Stripe subscription and billing
- Demo mode for marketing
- The `/developers` page for CLI/API/skill documentation

## Coding Tasks → Delegate

When Nelson asks to build, fix, or modify anything in Ledgi:

```
sessions_spawn task:"<describe the task> — project is at ~/projects/planify/" agentId:"coder"
```

Do NOT attempt to code yourself. The coder subagent has Claude Code CLI which will read the project's own CLAUDE.md files for detailed coding instructions.
