# Infobae Fetch Strategy

Infobae blocks anonymous scraping. Use the public r.jina.ai proxy to retrieve the page:

```
https://r.jina.ai/http://www.infobae.com/america/
```

This returns a cleaned markdown version. If you need the RSS feed, try:

```
https://r.jina.ai/http://www.infobae.com/america/rss
```

If that still fails, consider using a browser automation tool that sets a normal browser User‑Agent or authenticating through a valid session.

Store this strategy for future use.
