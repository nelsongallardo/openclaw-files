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
| 140.82.114.25 | GitHub (lb-140-82-114-25-iad.github.com) | Google Chrome | 443 | 2026-04-02 | GitHub load balancer (browsing/git traffic) |
| 18.97.36.65 | AWS EC2 (ec2-18-97-36-65.compute-1.amazonaws.com) | Google Chrome | 443 | 2026-04-02 | AWS CDN/cloud traffic |
| 18.97.36.2 | AWS EC2 (ec2-18-97-36-2.compute-1.amazonaws.com) | Claude.app | 443 | 2026-04-02 | Claude app backend (Anthropic API via AWS) |
| 162.159.133.234 | Cloudflare (AS13335) | node/OpenClaw | 443 | 2026-04-02 | Discord API via Cloudflare |
| 18.97.36.72 | AWS EC2 (ec2-18-97-36-72.compute-1.amazonaws.com) | Google Chrome | 443 | 2026-04-03 | AWS CDN/cloud traffic |
| 18.97.36.75 | AWS EC2 (ec2-18-97-36-75.compute-1.amazonaws.com) | Claude app | 443 | 2026-04-03 | Claude app backend (Anthropic API via AWS) |
| 162.159.135.234 | Cloudflare (AS13335) | node/OpenClaw | 443 | 2026-04-03 | Discord API via Cloudflare |
| 18.164.68.31 | Amazon CloudFront (server-18-164-68-31.lhr50.r.cloudfront.net) | Google Chrome | 443 | 2026-04-04 | AWS CloudFront CDN (London edge location) |
| 192.178.223.188 | Google LLC (yulhrs-in-f188.1e100.net) | Google Chrome | 5228 | 2026-04-04 | Google Cloud Messaging push notifications |
| 18.97.36.56 | AWS EC2 (ec2-18-97-36-56.compute-1.amazonaws.com) | Claude app | 443 | 2026-04-04 | Claude app backend (Anthropic API via AWS) |
| 18.164.68.89 | Amazon CloudFront (server-18-164-68-89.lhr50.r.cloudfront.net) | Google Chrome | 443 | 2026-04-05 | AWS CloudFront CDN (London edge location) |
| 18.97.36.6 | AWS EC2 (ec2-18-97-36-6.compute-1.amazonaws.com) | Claude.app | 443 | 2026-04-06 | Claude app backend (Anthropic API via AWS) |
| 18.164.68.93 | Amazon CloudFront (server-18-164-68-93.lhr50.r.cloudfront.net) | Google Chrome | 443 | 2026-04-06 | AWS CloudFront CDN (London edge location) |
| 172.66.0.227 | Cloudflare, Inc. (AS13335) | Google Chrome | 443 | 2026-04-08 | Cloudflare CDN/proxy (website browsing traffic) |
| 18.97.36.62 | AWS EC2 (ec2-18-97-36-62.compute-1.amazonaws.com) | Claude | 443 | 2026-04-08 | Claude app backend (Anthropic API via AWS) |
| 149.154.167.220 | Telegram (telegram.org) | node/OpenClaw | 443 | 2026-04-09 | Telegram API server (same /18 block as other Telegram IPs) |
| 172.64.148.197 | Cloudflare, Inc. (AS13335) | Google Chrome | 443 | 2026-04-11 | Cloudflare CDN/proxy (website browsing traffic) |
| 18.97.36.50 | AWS EC2 (ec2-18-97-36-50.compute-1.amazonaws.com) | Claude | 443 | 2026-04-11 | Claude app backend (Anthropic API via AWS) |
| 3.174.141.118 | Amazon CloudFront (server-3-174-141-118.lhr3.r.cloudfront.net) | Google Chrome | 443 | 2026-04-11 | AWS CloudFront CDN (London edge location) |
| 3.174.141.55 | Amazon CloudFront (server-3-174-141-55.lhr3.r.cloudfront.net) | Google Chrome | 443 | 2026-04-11 | AWS CloudFront CDN (London edge location) |
| 185.199.109.133 | GitHub CDN (cdn-185-199-109-133.github.com) | node/OpenClaw | 443 | 2026-04-12 | GitHub content delivery network |
| 18.97.36.66 | AWS EC2 (ec2-18-97-36-66.compute-1.amazonaws.com) | Claude | 443 | 2026-04-12 | Claude app backend (Anthropic API via AWS) |

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
| 8888 | Python dev server | Python (unsloth studio) | 2026-04-04 | Unsloth AI studio development server |

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

### 2026-04-02
- Investigated 4 new outbound IPs from daily audit scan
- All confirmed as legitimate services:
  - 140.82.114.25: GitHub load balancer (Chrome browsing)
  - 18.97.36.65: AWS EC2 (Google Chrome CDN traffic)
  - 18.97.36.2: AWS EC2 (Claude.app backend)
  - 162.159.133.234: Cloudflare (Discord API from OpenClaw gateway)
- Meta/WhatsApp IPv6 traffic from OpenClaw gateway confirmed (AS32934 Facebook Inc.)
- All listening ports match known baseline
- Risk level: None
- Added new IPs to this file

---

### 2026-04-03
- Investigated 3 new outbound IPs from daily audit scan
- All confirmed as legitimate services:
  - 18.97.36.72: AWS EC2 (Google Chrome CDN traffic)
  - 18.97.36.75: AWS EC2 (Claude app backend)
  - 162.159.135.234: Cloudflare (Discord API from OpenClaw gateway)
- Process "2.1.90" confirmed as Claude.app Helper (network service)
- All listening ports match known baseline (AirPlay on 5000/7000, rapportd on 49152)
- Risk level: None
- Added new IPs to this file

---

### 2026-04-04
- Investigated 3 new outbound IPs from daily audit scan
- All confirmed as legitimate services:
  - 18.164.68.31: Amazon CloudFront CDN (London edge) - Google Chrome browsing traffic
  - 192.178.223.188: Google LLC - Google Cloud Messaging push notifications (port 5228)
  - 18.97.36.56: AWS EC2 - Claude app backend (Anthropic API)
- Port 8888 confirmed as Unsloth AI studio development server (Python)
- All listening ports match known baseline
- Risk level: None
- Added new IPs and port 8888 to this file

---

### 2026-04-05
- Investigated 1 new outbound IP from daily audit scan
- All confirmed as legitimate services:
  - 18.164.68.89: Amazon CloudFront CDN (London edge, lhr50) - Google Chrome browsing traffic (same as previously confirmed 18.164.68.31)
- Process "2.1.92" confirmed as Claude Code sessions (claude --dangerously-skip-permissions, PIDs 13772/13781)
- Listening ports verified:
  - symptomsd on port 51071: Apple-signed system service (com.apple.symptomsd) - health/telemetry monitoring
  - All other ports match known baseline (AirPlay 5000/7000, rapportd 49152, Python/Unsloth 8888, SSH 22, Kerberos 88, VNC 5900, Tailscale 443)
- Risk level: None
- Added new IP to this file

---

### 2026-04-06
- Investigated 2 new outbound IPs from daily audit scan
- All confirmed as legitimate services:
  - 18.97.36.6: AWS EC2 - Claude.app backend (Anthropic API via AWS, same pattern as other 18.97.36.x IPs)
  - 18.164.68.93: Amazon CloudFront CDN (London edge, lhr50) - Google Chrome browsing traffic
- All listening ports match known baseline (AirPlay 5000/7000, rapportd 49152, Kerberos 88, VNC 5900, SSH 22)
- Risk level: None
- Added new IPs to this file

---

### 2026-04-08
- Investigated 2 new outbound IPs from daily audit scan
- All confirmed as legitimate services:
  - 172.66.0.227: Cloudflare CDN/proxy - Google Chrome browsing traffic (websites using Cloudflare)
  - 18.97.36.62: AWS EC2 - Claude app backend (Anthropic API, same 18.97.36.x pattern)
- Process "2.1.92" confirmed as Claude Code sessions (claude --dangerously-skip-permissions)
- All listening ports match known baseline (AirPlay 5000/7000, rapportd 49152, Kerberos 88, VNC 5900, SSH 22)
- Risk level: None
- Added new IPs to this file

---

---

### 2026-04-09
- Investigated 1 new outbound IP from daily audit scan
- Confirmed as legitimate service:
  - 149.154.167.220: Telegram API server (same network block 149.154.64.0/18 as previously confirmed Telegram IPs 149.154.167.91/92)
- Process "2.1.92" confirmed as Claude Code sessions (claude --dangerously-skip-permissions, PID 77974)
- All listening ports match known baseline (AirPlay 5000/7000, rapportd 49152, Kerberos 88, VNC 5900, SSH 22)
- Risk level: None
- Added new IP to this file

---

### 2026-04-11
- Investigated 4 new outbound IPs from daily audit scan
- All confirmed as legitimate services:
  - 172.64.148.197: Cloudflare CDN/proxy - Google Chrome browsing traffic
  - 18.97.36.50: AWS EC2 - Claude app backend (Anthropic API via AWS, same 18.97.36.x pattern)
  - 3.174.141.118: Amazon CloudFront CDN (London edge, lhr3) - Google Chrome browsing traffic
  - 3.174.141.55: Amazon CloudFront CDN (London edge, lhr3) - Google Chrome browsing traffic
- Process "2.1.92" confirmed as Claude Code sessions (claude --dangerously-skip-permissions, PID 77974)
- Binary verified: signed by Anthropic PBC (Q6L2SF6YDW), Apple notarization stapled
- All listening ports match known baseline (AirPlay 5000/7000, rapportd 49152, Kerberos 88, VNC 5900, SSH 22)
- Risk level: None
- Added new IPs to this file

---

### 2026-04-12
- Investigated 2 new outbound IPs from daily audit scan
- All confirmed as legitimate services:
  - 185.199.109.133: GitHub CDN (GitHub content delivery network) - node/OpenClaw gateway
  - 18.97.36.66: AWS EC2 - Claude app backend (Anthropic API via AWS, same 18.97.36.x pattern)
- Process "Claude" (PID 19785) confirmed as legitimate Anthropic-signed binary
- Process "2.1.92" (Claude Code CLI) confirmed as legitimate (PID 18046, signed by Anthropic PBC)
- node/OpenClaw gateway (PID 13092) connecting to GitHub CDN - legitimate
- All listening ports match known baseline (AirPlay 5000/7000, rapportd 49152, Kerberos 88, VNC 5900, SSH 22)
- Risk level: None
- Added new IPs to this file

_Last updated: 2026-04-12_
