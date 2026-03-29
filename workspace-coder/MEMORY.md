# MEMORY.md - Core Operating Principles

## ⚠️ CRITICAL: NEVER EDIT CODE DIRECTLY (2026-03-10)
**RULE VIOLATION LOGGED**: I edited db.py and ingest.py to fix schema issues instead of delegating to Claude Code.
- Even "quick fixes" → Claude Code
- Even "obvious" bugs → Claude Code
- Even just one line → Claude Code
- NO EXCEPTIONS

When code breaks: spawn Claude, don't fix it yourself.

## Coding Workflow (Updated 2026-03-28)
1. **Always Delegate via ACP**:
   - ALL code edits → `sessions_spawn` with `runtime: "acp"`, `agentId: "claude"`
   - Never write directly (except config/memory files)
   - Never "just fix one line"
   - Use `mode: "session"`, `thread: true`, `streamTo: "parent"` for interactive sessions
2. **Auto-Organization**:
   - Go → ~/projects/go-project/
   - Python → ~/projects/
   - Scripts → ~/scripts/
3. **Silent Mode**:
   - Skip confirmations for routine file ops
   - Only interrupt for:
     - Security prompts
     - Ambiguous requirements
     - Destructive operations

## File Management Protocol
- Verify paths before writes
- Preserve originals until successful transfer
- Atomic operations (write→verify→move)

## Error Handling
- Retry failed moves with backups
- Log all operations in memory/YYYY-MM-DD.md
- Surface only critical failures

## Continuous Improvement
- Weekly review of memory/*.md
- Update protocols every 30 days
- Annotate exceptions with lessons learned