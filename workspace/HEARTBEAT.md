# HEARTBEAT

You MUST use tools. Do NOT reply without using tools first.

## Step 1: Read the progress file

Call the read tool with path: /Users/openclaw/.openclaw/workspace/TRELLO_PROGRESS.md

## Step 2: Check Trello for cards

Call web_fetch with this URL (GET request):

https://api.trello.com/1/lists/69aed427ec27f63df5184cc9/cards?key=b5f9b65451e0e2ff1f50ceb7a7161e31&token=ATTAbdff0b4a13cf09e8d847b1c4011e635337b45988a421ce7d316a164856ae04536280A6C3

From the JSON response, take the first card's `name` and `id`.

## Step 3: Act on results

- If the progress file Status is "done" or "completed": move card to Done by calling web_fetch with method PUT to: `https://api.trello.com/1/cards/CARD_ID?key=b5f9b65451e0e2ff1f50ceb7a7161e31&token=ATTAbdff0b4a13cf09e8d847b1c4011e635337b45988a421ce7d316a164856ae04536280A6C3` with body `idList=69aed42be150c114e5790af0` — then write TRELLO_PROGRESS.md with Status "idle" and reply "Completed: CARD_NAME"
- If the progress file Status is "in progress": use sessions_spawn to follow up with agentId "main". Reply HEARTBEAT_OK
- If the progress file Status is "blocked": reply with the question from the Log field.
- If the progress file Status is "idle" AND web_fetch returned a card: move it to InProgress by calling web_fetch with method PUT to: `https://api.trello.com/1/cards/CARD_ID?key=b5f9b65451e0e2ff1f50ceb7a7161e31&token=ATTAbdff0b4a13cf09e8d847b1c4011e635337b45988a421ce7d316a164856ae04536280A6C3` with body `idList=69aed42aa618680fff8a961f` — then update TRELLO_PROGRESS.md with card name and Status "started", use sessions_spawn to delegate to agentId "main", and reply "Started task: CARD_NAME"
- If the progress file Status is "idle" AND web_fetch returned empty array or no cards: reply HEARTBEAT_OK
- If web_fetch returned an error or unexpected output: reply "HEARTBEAT_ERR: Trello API failed — " followed by the first 100 chars of the output

## Rules

Your reply goes directly to Telegram. Keep it under 2 sentences.
Do not narrate. Do not explain what you are doing.
