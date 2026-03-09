# HEARTBEAT.md

## Rules

You MUST complete every task below. Keep it quick and concise.
- If something needs a complex response or action, delegate it:

```
sessions_spawn task:"<describe what you found and what needs doing>" agentId:"main"
```

## Tasks

- Call web_fetch with url "https://www.infobae.com/america/" and extract the top 2 headlines from the result. Reply with ONLY the 2 headlines, nothing else. No HEARTBEAT_OK. Do not try other tools if web_fetch works — just use the result you get.