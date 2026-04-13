---
name: xactions
description: Post tweets, get profiles, search Twitter, and automate X/Twitter tasks using XActions. Use when the user wants to tweet, post on Twitter/X, check a Twitter profile, search tweets, or do any Twitter automation.
---

# XActions — X/Twitter Automation

## Setup (if MCP server is not available)

If `mcp__xactions__` tools are not available, walk the user through setup:

1. Clone the repo:
   ```bash
   git clone https://github.com/nirholas/XActions.git ~/projects/XActions
   cd ~/projects/XActions && npm install
   ```

2. Add the MCP server to `~/.claude.json` under the top-level `"mcpServers"` key:
   ```json
   "xactions": {
     "command": "node",
     "args": ["<full-path-to-XActions>/src/mcp/server.js"],
     "env": {
       "XACTIONS_SESSION_COOKIE": "<auth_token>"
     }
   }
   ```

3. To get the `auth_token`: open x.com in browser > DevTools (Cmd+Shift+I) > Application > Cookies > `https://x.com` > copy the `auth_token` cookie value.

4. Ask the user for the token, update `~/.claude.json`, and tell them to restart Claude Code.

## Usage

**Always call `x_login` first before any other XActions tool.** Read the session cookie from `~/.claude.json` at `mcpServers.xactions.env.XACTIONS_SESSION_COOKIE` and pass it to `x_login`.

```
mcp__xactions__x_login({ cookie: "<session_cookie>" })
```

After login, use any of the tools below.

### Common tools

| Tool | Purpose |
|---|---|
| `x_post_tweet` | Post a tweet (max 280 chars) |
| `x_post_thread` | Post a thread (array of tweets) |
| `x_reply` | Reply to a tweet |
| `x_get_profile` | Get user profile info |
| `x_get_tweets` | Get a user's recent tweets |
| `x_search_tweets` | Search tweets by keyword |
| `x_get_followers` | Get followers list |
| `x_get_following` | Get following list |
| `x_like` | Like a tweet |
| `x_retweet` | Retweet |
| `x_get_trends` | Trending topics |
| `x_generate_tweet` | AI-generate a tweet |
| `x_get_analytics` | Engagement analytics |

All tools are prefixed with `mcp__xactions__` when calling them.

### Important notes

- Always confirm tweet content with the user before posting.
- If a tool returns `"success": false`, try logging in again — the session may have expired.
- If the session cookie is expired, the user needs to grab a fresh `auth_token` from their browser and update `~/.claude.json`.
- Twitter rate limits apply — add delays between bulk operations.
- This uses browser automation, not the Twitter API. It can break if Twitter changes their UI.
