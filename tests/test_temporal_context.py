import asyncio
import json
from datetime import date, datetime, timezone
from types import SimpleNamespace

from src.ai.analyzer import ContentAnalyzer
from src.ai.enricher import ContentEnricher
from src.ai.temporal_context import temporal_context
from src.models import ContentItem, SourceType


def test_runtime_date_reaches_analysis_enrichment_and_translation(monkeypatch):
    monkeypatch.setattr('src.ai.temporal_context.shanghai_today', lambda: date(2026, 11, 2))
    item = ContentItem(id='paper', title='ICU trajectories', url='https://arxiv.org/abs/2610.42126', source_type=SourceType.RSS, published_at=datetime(2026, 10, 30, 20, tzinfo=timezone.utc))
    prompts = []
    async def complete(**kwargs):
        prompts.append(kwargs['system'])
        return json.dumps(dict(score=8, reason='Relevant', summary='Summary', tags=[], queries=[], title_zh='论文'))
    client = SimpleNamespace(complete=complete)
    async def run():
        await ContentAnalyzer(client)._analyze_item(item)
        enricher = ContentEnricher(client)
        await enricher._enrich_item(item)
        await enricher._translate_item(item)
    asyncio.run(run())
    assert len(prompts) == 4
    for prompt in prompts:
        assert 'Runtime current date (Asia/Shanghai): 2026-11-02' in prompt
        assert '2026-10-31T04:00:00+08:00' in prompt
        assert 'Correct stale current-date claims' in prompt
    item.metadata['publication_date_unknown'] = True
    assert 'unknown (historical recommendation' in temporal_context(item)
    assert '2026-10-31' not in temporal_context(item)
