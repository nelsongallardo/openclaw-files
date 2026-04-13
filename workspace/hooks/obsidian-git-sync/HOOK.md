---
name: obsidian-git-sync
description: "Auto-commit and push changes whenever OpenClaw sends a message after writing or editing files inside the Obsidian vault. Use to mirror Claude Code's Obsidian vault git auto-sync behavior for /Users/openclaw/Documents/obsidian."
metadata:
  { "openclaw": { "emoji": "🔁", "events": ["message:sent"], "os": ["darwin"], "requires": { "bins": ["git"] } } }
---

# Obsidian Git Sync

Auto-sync the Obsidian vault git repo after OpenClaw work that modifies files inside `/Users/openclaw/Documents/obsidian`.

- Watch for outbound messages as a cheap post-turn trigger.
- If the vault repo has local changes, commit and push them.
- Keep the commit message automatic and short.
- Ignore runs where nothing changed.
