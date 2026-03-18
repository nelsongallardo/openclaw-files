#!/bin/bash
# Usage: trello-move.sh <card_id> <list_id>
set -euo pipefail
source ~/.openclaw/credentials/trello.env
curl -s -X PUT "https://api.trello.com/1/cards/$1?key=${TRELLO_API_KEY}&token=${TRELLO_TOKEN}&idList=$2"
