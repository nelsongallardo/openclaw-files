# Security Agent Workspace

Nightly security auditor running on `chutes/Qwen/Qwen3.5-397B-A17B-TEE`.

## What it does

- Runs at **2:00 AM** via cron (`security-audit-lulu-logs`)
- Executes `scripts/audit-lulu.sh` which collects:
  - Lulu firewall logs via macOS Unified Logging (`log show`)
  - Lulu rules database (`/Library/Objective-See/LuLu/rules.json`)
  - Active outbound connections via `netstat`
  - Process-to-connection mapping via `lsof` (flags non-standard ports and unexpected processes)
- The security agent reads the output and produces a structured report
- Reports are sent to Nelson via Telegram

## Files

| File | Purpose |
|------|---------|
| `SOUL.md` | Agent personality — deterministic, report-only |
| `HEARTBEAT.md` | Report format and audit instructions |
| `scripts/audit-lulu.sh` | Data collection script |
| `security-audit.log` | Persistent audit log (appended nightly) |
| `latest-report.txt` | Most recent report output |

## Prerequisites

- **LuLu** installed: `brew install --cask lulu` (or from [objective-see.org](https://objective-see.org/products/lulu.html))
- **Chutes** API access configured

## Manual run

```bash
~/.openclaw/workspace-security/scripts/audit-lulu.sh
```
