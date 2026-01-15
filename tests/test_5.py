from fastapi import HTTPException
from fastapi.testclient import TestClient
from app.api import app
client = TestClient(app)


def test_5():
    res = client.post("/run", json={"suite": "default"})
    assert res.status_code == 200
    assert "run_id" in res.json()

