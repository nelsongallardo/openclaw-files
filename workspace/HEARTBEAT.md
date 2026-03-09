# HEARTBEAT.md

## Rules

No narration. No commentary. If nothing to do, reply HEARTBEAT_OK.

## Tasks

### Trello Board: openclaw-todos (ID: L6w0xeNA)

**If "InProgress" is empty:**
- Get the top card from the "ToDO" list.
- Move it to "InProgress".
- Update TRELLO_PROGRESS.md: set Card name, Status to "started", clear the Log.
- Delegate: sessions_spawn task:"New task from Trello: <card name> - <card description>. Track your progress in workspace/TRELLO_PROGRESS.md — update the Status and append to the Log as you work." agentId:"main"

**If "InProgress" has a card:**
- Read workspace/TRELLO_PROGRESS.md.
- If Status says "done":
  - Move the Trello card to "Done".
  - Let me know the task is complete.
  - Reset TRELLO_PROGRESS.md to idle.
- If Status says "blocked" or the Log has a question for me:
  - Ask me the question in Telegram.
  - After I reply, update the Log with my answer.
  - Delegate: sessions_spawn task:"Continue Trello task: <card name>. Check workspace/TRELLO_PROGRESS.md for context and my latest answer. Update the doc as you work." agentId:"main"
- If Status says "in progress" (work ongoing, no blockers):
  - Delegate: sessions_spawn task:"Follow up on Trello task: <card name>. Check workspace/TRELLO_PROGRESS.md for context. Continue working and update the doc." agentId:"main"

**If both lists are empty:** reply HEARTBEAT_OK.
