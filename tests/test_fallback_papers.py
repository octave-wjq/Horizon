import asyncio
from unittest.mock import AsyncMock

import pytest

from src.fallback_papers import REPOSITORIES, parse_papers
from src.models import AIConfig, Config, FilteringConfig
from src.orchestrator import HorizonOrchestrator
from src.storage.manager import StorageManager


def test_parser_only_papers_and_normalizes_duplicate_arxiv():
    text = '''<!-- - **hidden** [paper](https://arxiv.org/abs/2301.00001) -->
- [2023/11] **Real title** *Authors* [[paper](https://arxiv.org/pdf/2311.16452v2.pdf)]
- [2023/11] **Real title** [[paper](https://arxiv.org/abs/2311.16452)]
- [code](https://github.com/test/project)
'''
    items = parse_papers(text, REPOSITORIES[0])
    assert len(items) == 1
    assert items[0].title == 'Real title'
    assert str(items[0].url) == 'https://arxiv.org/abs/2311.16452'
    assert items[0].metadata['curated_fallback']


def test_second_repository_title():
    items = parse_papers('* [**Arxiv, 2023**] **MedModel**: Clinical tasks. [paper](https://arxiv.org/abs/2311.16452)', REPOSITORIES[1])
    assert items[0].title == 'MedModel: Clinical tasks'


@pytest.mark.parametrize('normal_score,enabled,expected_fallback', [(None,True,True),(7.5,True,True),(8.0,True,False),(None,False,False)])
def test_empty_digest_fallback_only(tmp_path, monkeypatch, normal_score, enabled, expected_fallback):
    config = Config(sources={}, ai=AIConfig(provider='openai', model='test', api_key_env='TEST', languages=['zh']),
                    filtering=FilteringConfig(curated_fallback_enabled=enabled,ai_score_threshold=7.5,skip_weekends=False,skip_cn_holidays=False))
    orch = HorizonOrchestrator(config, StorageManager(str(tmp_path/'data')))
    items = parse_papers('- **Normal** [paper](https://arxiv.org/abs/2311.16452)', REPOSITORIES[0])
    items[0].metadata.clear()
    items[0].ai_score = normal_score
    fallback = parse_papers('- **Fallback A** [paper](https://arxiv.org/abs/2311.16079)\n- **Fallback B** [paper](https://arxiv.org/abs/2311.05112)', REPOSITORIES[0])
    for x in fallback:x.ai_score=7.0
    select = AsyncMock(return_value=fallback)
    monkeypatch.setattr(orch,'fetch_all_sources',AsyncMock(return_value=items if normal_score else []))
    monkeypatch.setattr(orch,'_analyze_content',AsyncMock(side_effect=lambda x:x))
    monkeypatch.setattr(orch,'merge_topic_duplicates',AsyncMock(side_effect=lambda x,**kw:x))
    monkeypatch.setattr(orch,'_expand_twitter_discussion',AsyncMock())
    monkeypatch.setattr(orch,'_enrich_important_items',AsyncMock())
    monkeypatch.setattr(orch,'_select_fallback_papers',select)
    monkeypatch.chdir(tmp_path)
    asyncio.run(orch.run())
    assert select.await_count == int(expected_fallback)
    if expected_fallback:
        summary=next((tmp_path/'data/summaries').glob('*.md')).read_text()
        assert '历史论文推荐' in summary
        assert 'Fallback A' in summary and 'Fallback B' in summary


def test_fallback_excludes_seen_and_requires_success(tmp_path, monkeypatch):
    config=Config(sources={}, ai=AIConfig(provider='openai',model='test',api_key_env='TEST'), filtering=FilteringConfig())
    orch=HorizonOrchestrator(config,StorageManager(str(tmp_path/'data')))
    items=parse_papers('\n'.join(f'- **Paper {i}** [paper](https://arxiv.org/abs/2311.0000{i})' for i in range(3)),REPOSITORIES[0])
    monkeypatch.setattr('src.orchestrator.fetch_papers',AsyncMock(return_value=items))
    monkeypatch.setattr(orch,'filter_recently_covered_items',lambda x:x[1:])
    async def analyze(x):
        for i in x:i.ai_score=6
        return x
    monkeypatch.setattr(orch,'_analyze_content',analyze)
    assert [x.title for x in asyncio.run(orch._select_fallback_papers())]==['Paper 1','Paper 2']
    items[1].ai_score=0
    monkeypatch.setattr(orch,'_analyze_content',AsyncMock(return_value=items[1:]))
    with pytest.raises(RuntimeError,match='analysis failed'):
        asyncio.run(orch._select_fallback_papers())


def test_webhook_labels_historical_papers_without_fake_publication_date():
    from src.ai.summarizer import DailySummarizer
    items=parse_papers('- **Paper** [paper](https://arxiv.org/abs/2311.16452)',REPOSITORIES[0])
    items[0].ai_score=6.0
    s=DailySummarizer()
    assert '不受当日评分阈值限制' in s.generate_webhook_overview(items,'2026-10-30',0,'zh')
    detail=s.generate_webhook_item(items[0],language='zh',index=1,total=1)
    assert '历史论文推荐' in detail and '6.0/10' in detail
    assert f'{items[0].published_at.month}月{items[0].published_at.day}日' not in detail
