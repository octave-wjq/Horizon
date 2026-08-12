from datetime import datetime, timezone
from types import SimpleNamespace

from rich.console import Console

from src.models import ContentItem, FilteringConfig, SourceType
from src.orchestrator import HorizonOrchestrator, _deduplication_url_key
from src.storage.manager import StorageManager


def make_item(
    item_id: str,
    score: float,
    category: str | None = None,
    url: str | None = None,
) -> ContentItem:
    metadata = {"category": category} if category is not None else {}
    return ContentItem(
        id=item_id,
        source_type=SourceType.RSS,
        title=item_id,
        url=url or f"https://example.com/{item_id}",
        published_at=datetime.now(timezone.utc),
        ai_score=score,
        metadata=metadata,
    )


def make_orch(filtering: FilteringConfig) -> HorizonOrchestrator:
    orch = HorizonOrchestrator.__new__(HorizonOrchestrator)
    orch.config = SimpleNamespace(filtering=filtering)
    orch.console = Console(record=True)
    return orch


def test_digest_floor_tops_up_papers_and_min_items() -> None:
    filtering = FilteringConfig(
        ai_score_threshold=8.0,
        min_items=3,
        min_paper_items=2,
    )
    orch = make_orch(filtering)
    selected = [make_item("news", 8.5, "ai-news")]
    pool = selected + [
        make_item("p1", 4.0, "med-paper", "https://arxiv.org/abs/1"),
        make_item("p2", 3.5, "ai-research", "https://www.nature.com/articles/x"),
        make_item("other", 3.0, "other"),
        make_item("zero", 0.0, "med-paper"),
    ]
    out = orch._apply_digest_floor(selected, pool, log=False)
    ids = [i.id for i in out]
    assert "p1" in ids and "p2" in ids
    assert len(out) >= 3
    assert "zero" not in ids


def test_is_paper_like_detects_arxiv() -> None:
    item = make_item("x", 5.0, url="https://arxiv.org/abs/2401.0001")
    assert HorizonOrchestrator._is_paper_like(item)


def test_titles_near_duplicate_chinese_rewrites() -> None:
    assert HorizonOrchestrator._titles_are_near_duplicate(
        "Nature 报道可泛化的脑部 MRI 基础模型",
        "可泛化脑部 MRI 基础模型",
    )
    assert HorizonOrchestrator._titles_are_near_duplicate(
        "使用 MCP 执行代码：构建更高效的 AI 智能体 - Anthropic",
        "Anthropic：用 MCP 执行代码构建更高效 AI 智能体",
    )


def test_cross_day_dedup_filters_recent_titles(tmp_path, monkeypatch) -> None:
    data_dir = tmp_path / "data"
    data_dir.mkdir()
    storage = StorageManager(data_dir=str(data_dir))
    storage.save_seen_items(
        [
            {
                "date": "2026-07-20",
                "title": "Google 发布 Med-Gemini 医疗 AI",
                "url": "https://example.com/med-gemini",
                "url_key": str(
                    _deduplication_url_key("https://example.com/med-gemini")
                ),
                "title_key": HorizonOrchestrator._normalize_title_key(
                    "Google 发布 Med-Gemini 医疗 AI"
                ),
                "extra_keys": [],
            },
            {
                "date": "2026-07-21",
                "title": "使用 MCP 执行代码：构建更高效的 AI 智能体 - Anthropic",
                "url": "https://www.anthropic.com/engineering/mcp",
                "url_key": str(
                    _deduplication_url_key(
                        "https://www.anthropic.com/engineering/mcp"
                    )
                ),
                "title_key": HorizonOrchestrator._normalize_title_key(
                    "使用 MCP 执行代码：构建更高效的 AI 智能体 - Anthropic"
                ),
                "extra_keys": [],
            },
        ]
    )

    filtering = FilteringConfig(recent_digest_days=21)
    orch = make_orch(filtering)
    orch.storage = storage
    monkeypatch.chdir(tmp_path)

    items = [
        make_item("dup", 8.0, url="https://example.com/med-gemini"),
        make_item("mcp", 8.0, url="https://news.google.com/rss/articles/abc"),
        make_item("fresh", 7.5, url="https://example.com/new"),
    ]
    items[0].title = "Google 发布 Med-Gemini 医疗 AI"
    items[1].title = "Anthropic：用 MCP 执行代码构建更高效 AI 智能体"
    items[2].title = "Brand new Graph engineering practice"
    kept = orch.filter_recently_covered_items(items, log_label="test")
    assert [item.id for item in kept] == ["fresh"]
