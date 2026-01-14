from fastapi.testclient import TestClient
from fastapi import FastAPI,HTTPException
app = FastAPI()
client = TestClient(app)


def test_5():
    res = client.post("/run", json={"suite": "default"})
    assert res.status_code == 200
    assert "run_id" in res.json()

