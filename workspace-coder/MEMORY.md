# MEMORY.md - Core Operating Principles

## Coding Workflow (Updated 2026-03-07)
1. **Always Delegate**:
   - All code generation → coding-agent (Claude/Codex)
   - Never write directly (except config/memory files)
2. **Auto-Organization**:
   - Go → ~/projects/go-project/
   - Python → ~/project/
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