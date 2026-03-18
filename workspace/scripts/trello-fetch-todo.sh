#!/bin/bash
# Fetches cards from Trello ToDo list and saves to TRELLO_TODO.json
set -euo pipefail
source ~/.openclaw/credentials/trello.env
LIST_ID="69aed427ec27f63df5184cc9"
OUT="/Users/openclaw/.openclaw/workspace/TRELLO_TODO.json"

RESPONSE=$(curl -s -w "\n%{http_code}" "https://api.trello.com/1/lists/${LIST_ID}/cards?key=${TRELLO_API_KEY}&token=${TRELLO_TOKEN}&fields=id,name")
HTTP_CODE=$(echo "$RESPONSE" | tail -1)
BODY=$(echo "$RESPONSE" | sed '$d')

if [ "$HTTP_CODE" = "200" ]; then
  echo "$BODY" > "$OUT"
else
  echo "{\"error\": \"HTTP $HTTP_CODE\", \"body\": \"$(echo "$BODY" | head -c 100)\"}" > "$OUT"
fi
