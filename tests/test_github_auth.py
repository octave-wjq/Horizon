import asyncio
from datetime import datetime, timezone

import httpx
import pytest

from src.models import GitHubSourceConfig
from src.scrapers.github import GitHubScraper


def test_invalid_token_retries_public_releases_and_events(monkeypatch, caplog):
    monkeypatch.setenv('GITHUB_TOKEN', 'invalid-secret')
    seen = []

    def handle(request):
        seen.append(request.headers.get('Authorization'))
        if len(seen) == 1:
            return httpx.Response(401)
        if '/releases' in request.url.path:
            return httpx.Response(200, json=[dict(id=1, tag_name='v1', html_url='https://github.com/a/b/releases/v1', published_at='2026-11-02T00:00:00Z', author={'login': 'a'})])
        return httpx.Response(200, json=[dict(id='2', type='WatchEvent', created_at='2026-11-02T00:00:00Z', repo={'name': 'a/b'}, payload={})])

    async def run():
        async with httpx.AsyncClient(transport=httpx.MockTransport(handle), headers={'Authorization': 'Bearer inherited-secret'}) as client:
            scraper = GitHubScraper([
                GitHubSourceConfig(type='repo_releases', owner='a', repo='b'),
                GitHubSourceConfig(type='user_events', username='a'),
            ], client)
            return await scraper.fetch(datetime(2026, 11, 1, tzinfo=timezone.utc))

    assert len(asyncio.run(run())) == 2
    assert seen == ['Bearer invalid-secret', None, None]
    assert 'invalid-secret' not in caplog.text
    assert 'inherited-secret' not in caplog.text


@pytest.mark.parametrize('status, expected_calls', [(200, 1), (401, 2), (403, 1), (429, 1)])
def test_retry_is_bounded_and_does_not_bypass_rate_limits(monkeypatch, status, expected_calls):
    monkeypatch.setenv('GITHUB_TOKEN', 'test-token')
    calls = []
    def handle(req):
        calls.append(req)
        return httpx.Response(status, json=[])
    async def run():
        async with httpx.AsyncClient(transport=httpx.MockTransport(handle)) as client:
            scraper = GitHubScraper([GitHubSourceConfig(type='repo_releases', owner='a', repo='b')], client)
            return await scraper.fetch(datetime(2026, 11, 1, tzinfo=timezone.utc))
    assert asyncio.run(run()) == []
    assert len(calls) == expected_calls
