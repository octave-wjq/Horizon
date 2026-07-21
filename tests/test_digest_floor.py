from datetime import datetime, timezone
from types import SimpleNamespace

from rich.console import Console

from src.models import ContentItem, FilteringConfig, SourceType
from src.orchestrator import HorizonOrchestrator


def make_item(item_id: str, score: float, category: str | None = None, url: str | None = None) -> ContentItem:
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


def test_cross_day_dedup_filters_recent_titles(tmp_path, monkeypatch) -> None:
    summaries = tmp_path / "summaries"
    summaries.mkdir()
    # yesterday digest
    (summaries / "horizon-2026-07-20-zh.md").write_text(
        "# Horizon\n\n1. [Google 发布 Med-Gemini 医疗 AI](https://example.com/med-gemini)\n",
        encoding="utf-8",
    )
    filtering = FilteringConfig(recent_digest_days=3)
    orch = make_orch(filtering)
    orch.storage = SimpleNamespace(summaries_dir=summaries)
    monkeypatch.chdir(tmp_path)

    items = [
        make_item("dup", 8.0, url="https://example.com/med-gemini"),
        make_item("fresh", 7.5, url="https://example.com/new"),
    ]
    items[0].title = "Google 发布 Med-Gemini 医疗 AI"
    items[1].title = "Brand new GraphRAG framework"
    kept = orch.filter_recently_covered_items(items, log_label="test")
    assert [i.id for i in kept] == ["fresh"]
