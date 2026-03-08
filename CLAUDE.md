# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

This is the **OpenClaw / Clawdbot** runtime configuration directory (`~/.openclaw/`). It's not a traditional codebase — it's the home directory for an AI assistant named **Claudillo** that runs on a Mac Mini, serving a user named Nelson via Telegram (and potentially other channels).

OpenClaw is a multi-agent AI assistant platform that routes conversations through configurable LLM providers (OpenRouter, local llama.cpp) and manages agent workspaces, memory, cron jobs, skills, and messaging channels.

## Directory Structure

- **`openclaw.json`** — Main configuration: auth, model providers, agent definitions, channel config (Telegram), gateway settings, hooks, skills, plugins. This is the central config file.
- **`workspace/`** — Main agent workspace (Claudillo). Contains personality files (`SOUL.md`, `IDENTITY.md`, `USER.md`), operational docs (`AGENTS.md`, `TOOLS.md`, `HEARTBEAT.md`), long-term memory (`MEMORY.md`), daily memory files (`memory/YYYY-MM-DD.md`), and skills.
- **`workspace-coder/`** — Coder subagent workspace. Dedicated to coding tasks, delegates to external coding agents (Claude Code CLI, Codex, etc.) rather than writing code itself.
- **`agents/`** — Agent session state directories (`main`, `coder`, `planner`).
- **`cron/`** — Scheduled jobs (`jobs.json`) and run history.
- **`credentials/`** — Channel auth tokens (Telegram pairing, allowlists).
- **`identity/`** — Device identity and auth (`device.json`, `device-auth.json`).
- **`completions/`** — Shell completions (bash, zsh, fish, PowerShell) for the `openclaw` CLI.
- **`telegram/`** — Telegram bot state (update offsets, command hashes).
- **`delivery-queue/`** — Message delivery queue with failed message tracking.
- **`subagents/`** — Subagent run tracking (`runs.json`).
- **`devices/`** — Paired and pending device registrations.
- **`logs/`** — Application logs.

## Architecture

### Agent System

Three agents defined in `openclaw.json` → `agents.list`:

| Agent | Model | Purpose |
|-------|-------|---------|
| `main` (default) | Qwen 3.5 Flash (OpenRouter) | General conversation, Q&A, tool use |
| `planner` | Claude Opus 4.6 (OpenRouter) | Complex planning, architecture, research |
| `coder` | DeepSeek V3 (OpenRouter) | Coding tasks via external coding agents |

Each agent has its own workspace directory with independent personality, memory, and operational docs.

### Model Providers

- **OpenRouter** — Cloud models (Qwen 3.5, Qwen 3.5 Flash, DeepSeek V3, Claude Opus)
- **llama.cpp** — Local models at `http://127.0.0.1:8080/v1` (Qwen3 14B Q4_K_M, GLM-4.7 Flash Q4_K_M)

### Workspace Files (Boot Sequence)

Each agent session reads these files on startup (defined in `AGENTS.md`):
1. `SOUL.md` — Personality and behavioral rules
2. `USER.md` — Info about Nelson (the human)
3. `memory/YYYY-MM-DD.md` — Recent daily context
4. `MEMORY.md` — Long-term curated memory (main session only, not shared in group contexts for security)

### Heartbeat System

Configured in `openclaw.json` → `agents.defaults.heartbeat`:
- Runs every 30 minutes using the local GLM-4.7 Flash model
- Checks `HEARTBEAT.md` for pending tasks
- Can proactively check email, calendar, weather, mentions
- Responds `HEARTBEAT_OK` when nothing needs attention

### Skills

Skills are installed in `workspace/skills/` as packages with `SKILL.md` entry points. Currently installed:
- **`clawddocs`** (v1.2.2) — Documentation expert for Clawdbot itself, with shell scripts for search, fetching, caching, and indexing docs

### Key Config Patterns

- `openclaw.json` uses trailing commas (non-standard JSON) — be aware when editing
- Sensitive tokens are stored directly in `openclaw.json` (`channels.telegram.botToken`, `gateway.auth.token`) and in `credentials/`
- Gateway runs on port 18789, loopback only, with token auth
- Telegram is the active messaging channel with allowlist-based DM/group policies
