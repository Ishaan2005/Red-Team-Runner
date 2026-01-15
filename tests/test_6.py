from fastapi import HTTPException
from fastapi.testclient import TestClient
from app.api import app
client = TestClient(app)

def test_6():
    res = client.post("/run", json={"suite": "bad"})
    assert res.status_code == 400