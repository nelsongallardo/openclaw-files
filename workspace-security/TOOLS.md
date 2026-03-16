# TOOLS.md - Security Tools & References

## Audit Script

- **Path:** `~/.openclaw/workspace-security/scripts/audit-lulu.sh`
- **What it does:** Captures current outbound TCP connections, flags non-standard ports, lists listening ports
- **Output:** Plain text sections for outbound connections, non-standard ports, and listening ports

## Firewall

- **Software:** LuLu (free macOS firewall by Objective-See)
- **Purpose:** Monitors and logs outbound network connections
- **Log location:** Queried live via `lsof` and `netstat` in the audit script

## Known Network Baseline

_Update this section as you learn what's normal on this machine:_

### Expected Processes with Outbound Connections
- Google Chrome (ports 443, 5228)
- Discord (port 443 → Cloudflare 162.159.x.x)
- Telegram (port 443 → 149.154.x.x)
- node/OpenClaw (port 443 → Telegram/Discord APIs)
- Ollama (localhost:11434)
- Apple system services (17.x.x.x on ports 443, 5223)
- mDNSResponder, trustd, ocspd, apsd, cloudd, nsurlsessiond

### Expected Listening Ports
_Document baseline listening ports here as you observe them._

## Audit Schedule

- **Daily:** Automated via cron at 02:30 UTC, delivered to Telegram group topic
- **On-demand:** Nelson can request ad-hoc audits anytime
