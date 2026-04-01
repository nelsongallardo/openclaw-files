# HEARTBEAT

Run through this checklist. Only notify Nelson if something actually needs attention.

Your reply goes directly to Telegram. Do not narrate or explain what you are doing. If nothing needs attention, reply with exactly HEARTBEAT_OK and nothing else — this is a system keyword that suppresses delivery, so Nelson won't see it.

## 1. GCP Alerts (CuizAI)

Check for GCP alerting emails in nensol85@gmail.com:

```
exec command:"gog gmail search 'from:alerting-noreply@google.com subject:CuizAI is:unread' -a nensol85@gmail.com --max 5 --json --fail-empty"
```

If the command exits with code 3 (no results), skip this section.

If alerts found, for each message:
1. Get full content: `gog gmail get <id> -a nensol85@gmail.com --json`
2. Write a task file to `/Users/openclaw/.openclaw/email-pipeline/cuiz-ai-alerts/` with this structure:
   ```json
   {
     "created": "<ISO-8601>",
     "source": "gcp-alert",
     "category": "gcp_alert",
     "from": "alerting-noreply@google.com",
     "subject": "<email subject>",
     "message_id": "<gmail message id>",
     "summary": "<1-2 sentence summary of the alert>",
     "priority": "high",
     "requires_code_change": true,
     "project": "cuiz-ai",
     "full_content": "<email body>"
   }
   ```
3. Notify Nelson: `🚨 GCP Alert: <subject>. Routing to coder for investigation.`

Do NOT suppress this with HEARTBEAT_OK — always notify for GCP alerts, even during quiet hours.

## 2. Email Pipeline Results

```
exec command:"ls /Users/openclaw/.openclaw/email-pipeline/results/ 2>/dev/null"
```

If result files exist, read each one and notify Nelson on Telegram based on type:

- **Escalation** (suggested_action = "escalate"): 🚨 prefix, include analysis + notes, say "This needs your personal attention"
- **Reply + PR** (pr_url is not null): 📧 prefix, include PR link, ask "Send reply & merge PR?"
- **Reply only**: 📧 prefix, show draft, ask "Send this reply?"
- **GCP Alert result** (source = "gcp-alert"): Based on action_taken:
  - `fix_and_pr`: ✅ prefix, include PR link + diagnosis summary
  - `no_action`: ℹ️ prefix, include diagnosis + summary (e.g. "False positive — no errors found")
  - `needs_manual`: 🚨 prefix, include diagnosis, say "This needs your attention"

After notifying, move the result file to `email-pipeline/archive/`.

## 3. Calendar

Check for upcoming events in the next 2 hours. Notify if something's coming up.

## 4. Weather

If it's morning (before 10am), check London weather. Only notify if rain or unusual conditions.

## 5. Quiet Hours

Don't notify between 23:00–08:00 unless it's an escalation.
