# Known Safe Traffic Baseline

## Processes with Outbound Connections

- **Port 443, 5228 — Google Chrome**: Normal browser + push notifications
- **Port 443 — Discord**: Connections to Cloudflare (162.159.x.x)
- **Port 443 — Telegram**: Connections to 149.154.x.x
- **Port 443 — node/OpenClaw gateway**: Connections to Telegram/Discord APIs
- **Port 1200 — Ollama**: localhost connections for local LLM
- **Port 18789 — OpenClaw gateway**: localhost service
- **Port 8420 — app.py (Python, ~/projects/observability)**: User's observability project, connects to Tailscale mesh 100.64.x.x
- **Ports 5000 & 7000 — ControlCenter (macOS AirPlay Receiver)**: Built-in macOS service

## Services and System Processes

- **17.x.x.x (Apple services)**: Ports 443, 5223 — iCloud, APNs
- **Tailscale (100.64.0.0/10 range)**: CGNAT private WireGuard mesh addresses
- **Tailscale peer 100.64.48.110**: Internal mesh traffic for user's projects
- **mDNSResponder, trustd, ocspd, apsd, cloudd, nsurlsessiond**: Normal macOS system services
- **LuLu**: The firewall itself — normal

## Listening Ports (Baseline)

- **Port 1200**: Ollama (localhost)
- **Port 18789**: OpenClaw gateway (localhost)

---

_Last updated: 2026-03-16_
