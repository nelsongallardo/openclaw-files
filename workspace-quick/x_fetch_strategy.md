# X.com Tweet Fetch Strategy

When fetching a tweet directly from `https://x.com/...` you may encounter anti‑scraping blocks or generic error pages.

**Fallback approach:**
1. Use the public `r.jina.ai/http://URL` endpoint, which fetches the page and returns a clean markdown/text representation.
2. Example: `https://r.jina.ai/http://x.com/bcherny/status/2032578639276159438`.
3. If the first fetch fails, try adding `?format=text` or using a third‑party reader like `https://r.jina.ai/http://`.
4. Keep the strategy in this file for future reference.

This should reliably provide the tweet text without the site’s bot‑blocking layers.