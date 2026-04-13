# CLAUDE.md

This is the OpenClaw runtime directory at `~/.openclaw/`.

## What matters

- `openclaw.json` — main config for models, agents, channels, hooks, plugins, and gateway
- `workspace/` — main assistant workspace for Claudillo
- `workspace-coder/` — coder workspace
- `cron/` — scheduled jobs and history
- `logs/` — runtime logs

## Main workspace

`workspace/` contains the assistant bootstrap files and memory:
- `SOUL.md`
- `USER.md`
- `AGENTS.md`
- `TOOLS.md`
- `HEARTBEAT.md`
- `MEMORY.md`
- `memory/YYYY-MM-DD.md`

## Notes

- Claudillo is Nelson’s assistant running on a Mac Mini
- Main channel is Telegram
- Gateway config lives in `openclaw.json`
- Obsidian vault path: `/Users/openclaw/Documents/obsidian`
- Obsidian repo: `https://github.com/nelsongallardo/obsidian`
- Vault edits should auto-commit and push via the `obsidian-git-sync` hook
