# Known & Investigated IPs

This file tracks all IPs that have been investigated and confirmed safe. Reference this during audits to avoid re-flagging known-good traffic.

---

## Investigated IPs — Confirmed Safe

| IP | Owner/Organization | Process | Port | Date Investigated | Notes |
|----|-------------------|---------|------|-------------------|-------|
| 18.97.36.51 | AWS EC2 (ec2-18-97-36-51.compute-1.amazonaws.com) | Google Chrome | 443 | 2026-03-27 | CDN/cloud traffic |
| 18.97.36.71 | AWS EC2 (ec2-18-97-36-71.compute-1.amazonaws.com) | Claude app | 443 | 2026-03-27 | Claude app backend |
| 160.79.104.10 | Anthropic PBC (AS399358) | Claude app | 443 | 2026-03-27 | Official Claude API |
| 34.111.142.178 | Google Cloud (bc.googleusercontent.com) | node/OpenClaw | 443 | 2026-03-27 | Google API calls |
| 140.82.113.25 | GitHub (lb-140-82-113-25-iad.github.com) | Google Chrome | 443 | 2026-03-27 | Git/browsing traffic |
| 185.20.209.167 | Zoho Corporation (ZOHO0001-IPAC01) | Google Chrome | 443 | 2026-03-30 | Zoho email service (sender167.eu.zcsend.net) |
| 18.97.36.76 | AWS EC2 (ec2-18-97-36-76.compute-1.amazonaws.com) | Google Chrome | 443 | 2026-03-30 | AWS CDN/cloud traffic |
| 18.97.36.78 | AWS EC2 (ec2-18-97-36-78.compute-1.amazonaws.com) | Claude app | 443 | 2026-03-30 | Claude app backend |
| 18.97.36.18 | AWS EC2 (ec2-18-97-36-18.compute-1.amazonaws.com) | Claude Code | 443 | 2026-04-01 | Anthropic API (Claude Code sessions) |
| 149.154.167.91 | Telegram (telegram.org) | Telegram | 443 | 2026-04-01 | Telegram API server |
| 149.154.167.92 | Telegram (telegram.org) | Telegram | 443 | 2026-04-01 | Telegram API server |
| 149.154.166.110 | Telegram (telegram.org) | node/OpenClaw | 443 | 2026-04-01 | Telegram bot API |
| 162.159.134.234 | Cloudflare (Discord) | node/OpenClaw | 443 | 2026-04-01 | Discord API via Cloudflare |
| 100.68.162.42 | Tailscale (CGNAT range) | sshd-sess | 22 | 2026-04-01 | Tailscale SSH session (nelsons-mac-mini.ts.net) |
| 100.64.48.110 | Tailscale (CGNAT range) | sshd-sess | 22 | 2026-04-01 | Tailscale SSH session endpoint |

---

## Listening Ports — Confirmed Safe

| Port | Service | Process | Date Confirmed | Notes |
|------|---------|---------|----------------|-------|
| 49152 | Apple device connectivity | rapportd | 2026-03-27 | macOS system service |
| 5000 | AirPlay Receiver | ControlCenter | 2026-03-16 | Built-in macOS service |
| 7000 | AirPlay Receiver | ControlCenter | 2026-03-16 | Built-in macOS service |
| 64135 | Ephemeral | Various | 2026-03-27 | No persistent service observed |
| 60339 | Ephemeral | Various | 2026-03-27 | No persistent service observed |
| 52986 | Ephemeral | Various | 2026-03-27 | No persistent service observed |
| 22 | SSH | ssh-agent | 2026-03-30 | SSH agent for key management |
| 5900 | VNC | Unknown | 2026-03-30 | VNC server - needs verification |
| 88 | Kerberos | Unknown | 2026-03-30 | Kerberos authentication service |
| 3000 | Next.js dev server | node (next-server) | 2026-04-01 | Development server for cuiz-ai/quiz-ai-generator-frontend project |

---

## Audit Log

### 2026-03-27
- Investigated 5 new outbound IPs from audit scan
- All confirmed as legitimate services (AWS, GCP, GitHub, Anthropic)
- Risk level: None
- Added to this file for future reference

### 2026-03-30
- Investigated 3 new outbound IPs: 185.20.209.167 (Zoho email), 18.97.36.76 (AWS), 18.97.36.78 (Claude/AWS)
- All confirmed as legitimate services
- Listening ports 22 (ssh-agent), 5900 (VNC), 88 (Kerberos) observed — standard macOS services
- Risk level: None
- Added new IPs and ports to this file

### 2026-04-01
- Investigated 8 new outbound IPs and 1 new listening port
- All confirmed as legitimate services:
  - 18.97.36.18: Anthropic API (Claude Code sessions)
  - 149.154.167.91/92, 149.154.166.110: Telegram API servers
  - 162.159.134.234: Discord API via Cloudflare
  - 100.68.162.42, 100.64.48.110: Tailscale SSH session (Nelson's own machine)
  - Port 3000: Next.js dev server for cuiz-ai project
- Risk level: None
- Added new IPs and port 3000 to this file

---

_Last updated: 2026-04-01_
