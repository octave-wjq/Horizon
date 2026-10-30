"""Curated paper fallback for otherwise empty working-day digests."""
import hashlib
import re
from datetime import datetime, timezone
from urllib.parse import urlsplit

import httpx

from .models import ContentItem, SourceType

REPOSITORIES = (
    'mingze-yuan/Awesome-LLM-Healthcare',
    'AI-in-Health/MedLLMsPracticalGuide',
)


def parse_papers(markdown: str, repository: str) -> list[ContentItem]:
    papers = []
    seen = set()
    markdown = re.sub(r'<!--.*?-->', '', markdown, flags=re.S)
    for line in markdown.splitlines():
        match = re.search(r'\[paper\]\s*\((https?://[^\s)]+)\)', line, re.I)
        if not match:
            continue
        url = match[1]
        if urlsplit(url).hostname in ('arxiv.org', 'www.arxiv.org'):
            ident = re.search(r'(\d{4}\.\d{4,5})', url)
            if ident:
                url = 'https://arxiv.org/abs/' + ident[1]
        if url in seen:
            continue
        seen.add(url)
        title = line[:match.start()].rstrip(' [')
        title = re.sub(r'^\s*[-*]\s*\[[^\]]+\]\s*', '', title)
        if repository == REPOSITORIES[0]:
            bold = re.search(r'\*\*(.+?)\*\*', title)
            if bold:
                title = bold[1]
        title = title.replace('**', '').strip(' .')
        if not title:
            continue
        papers.append(ContentItem(
            id='github:curated:' + hashlib.sha256(url.encode()).hexdigest()[:16],
            source_type=SourceType.GITHUB, title=title, url=url,
            published_at=datetime.now(timezone.utc),
            content=f'Historical reading recommendation from {repository}. '
                    f'The current date is the recommendation date, not publication.\n{line}',
            metadata={'category': 'med-paper', 'curated_fallback': True,
                      'curated_repository': repository, 'publication_date_unknown': True},
        ))
    return papers


async def fetch_papers() -> list[ContentItem]:
    groups = []
    async with httpx.AsyncClient(timeout=30, follow_redirects=True) as client:
        for repo in REPOSITORIES:
            response = await client.get(f'https://raw.githubusercontent.com/{repo}/main/README.md')
            response.raise_for_status()
            papers = parse_papers(response.text, repo)
            if not papers:
                raise RuntimeError(f'No curated paper links found in {repo}')
            groups.append(papers)
    # Interleave so two available repositories each contribute a paper.
    result, seen = [], set()
    for index in range(max(map(len, groups))):
        for group in groups:
            if index < len(group) and str(group[index].url) not in seen:
                result.append(group[index])
                seen.add(str(group[index].url))
    return result
