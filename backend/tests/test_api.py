import os
import sys
import pytest
from httpx import AsyncClient, ASGITransport

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.extend([
    os.path.join(ROOT_DIR, 'backend', 'app'),
    ROOT_DIR
])
from api import app  # noqa: E402

@pytest.mark.asyncio
async def test_search(monkeypatch):
    async def fake_search(q, price=None):
        return {"results": []}

    monkeypatch.setattr("api.ml_search", fake_search)
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        resp = await ac.get("/search", params={"q": "test"})
        assert resp.status_code == 200
        assert resp.json() == {"results": []}
