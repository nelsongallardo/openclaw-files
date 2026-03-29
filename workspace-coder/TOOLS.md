# TOOLS.md - Local Notes

## ACP — How You Delegate Code

You spawn Claude Code via ACP using the `sessions_spawn` tool. This is your only coding workflow.

### Spawn a session

```json
{
  "task": "<detailed task description>",
  "runtime": "acp",
  "agentId": "claude",
  "mode": "session",
  "thread": true,
  "cwd": "/Users/openclaw/projects/<project>",
  "streamTo": "parent"
}
```

### Resume an existing session

```json
{
  "task": "<follow-up task>",
  "runtime": "acp",
  "agentId": "claude",
  "resumeSessionId": "<session-id>"
}
```

### Monitor / steer

- `/acp status` — check running sessions
- `/acp steer <instruction>` — nudge a running session
- `/acp cancel` — abort if stuck
- `/acp close` — end session

## Project Paths

- Default: `~/projects/`
- Go projects: `~/projects/go-project/`
- Python projects: `~/projects/`
- Scripts: `~/scripts/`
- **NEVER** use `~/.openclaw/` as cwd
