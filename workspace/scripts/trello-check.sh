#!/bin/bash
source ~/.openclaw/credentials/trello.env
curl -s "https://api.trello.com/1/lists/69aed427ec27f63df5184cc9/cards?key=$TRELLO_API_KEY&token=$TRELLO_TOKEN" | jq '.[0] | {name, id}'
