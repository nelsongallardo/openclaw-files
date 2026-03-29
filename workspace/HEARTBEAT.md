# HEARTBEAT

Run through this checklist. Only notify Nelson if something needs attention. If nothing does, reply HEARTBEAT_OK.

## 1. Email Pipeline Results

```
exec command:"ls /Users/openclaw/.openclaw/email-pipeline/results/ 2>/dev/null"
```

If result files exist, read each one and notify Nelson on Telegram based on type:

- **Escalation** (suggested_action = "escalate"): 🚨 prefix, include analysis + notes, say "This needs your personal attention"
- **Reply + PR** (pr_url is not null): 📧 prefix, include PR link, ask "Send reply & merge PR?"
- **Reply only**: 📧 prefix, show draft, ask "Send this reply?"

After notifying, move the result file to `email-pipeline/archive/`.

## 2. Calendar

Check for upcoming events in the next 2 hours. Notify if something's coming up.

## 3. Weather

If it's morning (before 10am), check London weather. Only notify if rain or unusual conditions.

## 4. Quiet Hours

Don't notify between 23:00–08:00 unless it's an escalation.
