import asyncio
from types import SimpleNamespace as NS
from unittest.mock import AsyncMock
import pytest
from src.ai.client import OpenAIClient
from src.models import AIConfig

class Stream:
    def __init__(self, events): self.events=events; self.closed=False
    async def __aenter__(self): return self
    async def __aexit__(self,*args): self.closed=True
    def __aiter__(self):
        async def gen():
            for e in self.events: yield e
        return gen()

def make_client(monkeypatch):
    monkeypatch.setenv('TEST_API_KEY','test')
    return OpenAIClient(AIConfig(provider='openai',model='gpt-6.1-sol',api_key_env='TEST_API_KEY'))

def events():
    return [NS(type='response.output_text.delta',delta='{"ok":'),NS(type='response.output_text.delta',delta='true}'),NS(type='response.completed',response=NS(status='completed',usage=None,output=[]))]

def test_empty_output_retries_stream_and_remembers_protocol(monkeypatch):
    c=make_client(monkeypatch);a=Stream(events());b=Stream(events())
    c.client.responses.create=AsyncMock(side_effect=[NS(output_text='',output=[],usage=None),a,b])
    async def run():
        assert await c.complete('system','user')=='{"ok":true}'
        assert await c.complete('system','next')=='{"ok":true}'
    asyncio.run(run());calls=c.client.responses.create.call_args_list
    assert len(calls)==3 and 'stream' not in calls[0].kwargs
    assert calls[1].kwargs['stream'] is True and calls[2].kwargs['stream'] is True
    assert a.closed and b.closed

@pytest.mark.parametrize('tail',[[],[NS(type='response.failed')],[NS(type='response.incomplete')],[NS(type='error')]])
def test_partial_stream_is_never_accepted(monkeypatch,tail):
    c=make_client(monkeypatch);s=Stream([NS(type='response.output_text.delta',delta='partial')]+tail)
    c.client.responses.create=AsyncMock(side_effect=[NS(output_text='',output=[],usage=None),s])
    with pytest.raises(ValueError): asyncio.run(c.complete('s','u'))
    assert s.closed
    assert not c._responses_stream_only

def test_empty_completed_stream_still_fails(monkeypatch):
    c=make_client(monkeypatch);s=Stream(events()[-1:])
    c.client.responses.create=AsyncMock(side_effect=[NS(output_text='',output=[],usage=None),s])
    with pytest.raises(ValueError,match='missing completed text'): asyncio.run(c.complete('s','u'))
