# HEARTBEAT

You MUST use tools first. Do NOT reply without calling a tool.

## Step 1

Read /Users/openclaw/.openclaw/workspace/TRELLO_PROGRESS.md

## Step 2

Run `~/.openclaw/workspace/scripts/trello-fetch-todo.sh` then read `/Users/openclaw/.openclaw/workspace/TRELLO_TODO.json`

## Step 3

If Status is "started": reply HEARTBEAT_OK
If Status is "idle" and there is a card: update TRELLO_PROGRESS.md with card name, id, status "started", then use sessions_spawn to tell agent "main" to do the task and move the card.
If Status is "idle" and no card: reply HEARTBEAT_OK
If Status is "done": use sessions_spawn to tell agent "main" to move the card to Done list 69aed42be150c114e5790af0, then reset TRELLO_PROGRESS.md to idle.
