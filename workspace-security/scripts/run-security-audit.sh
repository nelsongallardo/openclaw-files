#!/bin/bash
# Wrapper: runs audit script, feeds output to security agent, delivers to Telegram
# This is what the cron job should call.

set -euo pipefail

WORKSPACE="$HOME/.openclaw/workspace-security"

# Step 1: Run the audit and capture output
AUDIT_OUTPUT=$("$WORKSPACE/scripts/audit-lulu.sh" 2>&1)

# Step 2: Send output to the security agent with instructions
# The model receives the data directly — no tool use needed
openclaw agent \
  --agent security \
  --deliver \
  --channel telegram \
  --reply-to 8462098656 \
  --timeout 300 \
  --message "$(cat <<EOF
Below is the output of tonight's security audit script. Analyze it and reply with ONLY the report. No explanations, no reasoning, no tool calls.

If everything looks normal, reply with just: HEARTBEAT_OK

If there are findings, reply with ONLY this format:

Security Audit Report — $(date +%Y-%m-%d)

New outbound IPs detected:
- <ip> (<process>, port <port>)

Suspicious activity:
- <description>

Risk level: None/Low/Medium/High/Critical

Recommended actions:
- <action>

KNOWN SAFE (do NOT flag): Google/Chrome on 443/5228, Discord on 443, Telegram on 443 to 149.154.x.x, node/OpenClaw on 443, Apple services on 443/5223, Ollama on 11434, LuLu, mDNSResponder, trustd, ocspd, apsd, cloudd, nsurlsessiond.

--- AUDIT OUTPUT START ---
$AUDIT_OUTPUT
--- AUDIT OUTPUT END ---
EOF
)"
