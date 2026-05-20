#!/usr/bin/env python3
"""Scrape GitHub for AI-tool repos with > MIN_STARS stars; write JSON.

Usage:
    python scrape_ai_projects.py [output_path]

Env:
    GITHUB_TOKEN  Optional. Personal access token (or GITHUB_TOKEN in Actions)
                  raises the Search API rate limit from 10 to 30 req/min.

Schedule externally (cron, GitHub Actions). Example crontab line (daily 06:00):
    0 6 * * *  cd /path/to/repo && GITHUB_TOKEN=ghp_xxx python xenhive/scrape_ai_projects.py
"""
import json
import os
import sys
import time
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import quote_plus
from urllib.request import Request, urlopen

TOPICS = [
    # Core AI / LLM / agents
    "ai",
    "artificial-intelligence",
    "llm",
    "large-language-models",
    "machine-learning",
    "deep-learning",
    "ai-agents",
    "agents",
    # Tooling / infra
    "rag",
    "vector-database",
    "llmops",
    "mlops",
    "prompt-engineering",
    "fine-tuning",
    "embeddings",
    # Frameworks / domains
    "chatbot",
    "computer-vision",
    "nlp",
    "transformers",
    "pytorch",
    "tensorflow",
]
MIN_STARS = 30000
API = "https://api.github.com/search/repositories"
PER_PAGE = 100
MAX_PAGES = 10  # Search API caps results at 1000


def headers() -> dict:
    h = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "xenhive-ai-scraper",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        h["Authorization"] = f"Bearer {token}"
    return h


def search(query: str) -> list[dict]:
    items: list[dict] = []
    for page in range(1, MAX_PAGES + 1):
        url = (
            f"{API}?q={quote_plus(query)}"
            f"&sort=stars&order=desc&per_page={PER_PAGE}&page={page}"
        )
        while True:
            try:
                with urlopen(Request(url, headers=headers()), timeout=30) as resp:
                    data = json.loads(resp.read())
                break
            except HTTPError as e:
                if e.code == 403:
                    # rate-limited; honor reset header if present, else back off
                    reset = e.headers.get("X-RateLimit-Reset")
                    wait = max(1, int(reset) - int(time.time())) if reset else 60
                    print(f"rate-limited, sleeping {wait}s", file=sys.stderr)
                    time.sleep(wait)
                    continue
                raise
        batch = data.get("items", [])
        if not batch:
            break
        items.extend(batch)
        if len(batch) < PER_PAGE:
            break
        time.sleep(2)
    return items


def normalize(item: dict) -> dict:
    return {
        "id": item["id"],
        "full_name": item["full_name"],
        "html_url": item["html_url"],
        "description": item.get("description"),
        "stars": item["stargazers_count"],
        "forks": item["forks_count"],
        "language": item.get("language"),
        "topics": item.get("topics", []),
        "license": (item.get("license") or {}).get("spdx_id"),
        "archived": item.get("archived", False),
        "created_at": item["created_at"],
        "updated_at": item["updated_at"],
        "pushed_at": item["pushed_at"],
    }


def main() -> int:
    out_path = Path(
        sys.argv[1] if len(sys.argv) > 1 else "xenhive/ai-projects.json"
    )
    seen: dict[int, dict] = {}
    for topic in TOPICS:
        query = f"stars:>{MIN_STARS} topic:{topic}"
        results = search(query)
        for item in results:
            seen[item["id"]] = normalize(item)
        print(f"{topic}: +{len(results)} (total unique: {len(seen)})", file=sys.stderr)
        time.sleep(2)

    repos = sorted(seen.values(), key=lambda r: r["stars"], reverse=True)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "min_stars": MIN_STARS,
        "topics": TOPICS,
        "count": len(repos),
        "repos": repos,
    }
    out_path.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {len(repos)} repos to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
