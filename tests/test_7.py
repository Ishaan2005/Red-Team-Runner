from fastapi import HTTPException
from fastapi.testclient import TestClient
from app.api import app
client = TestClient(app)


def test_7():
    run = client.post("/run", json={"suite": "default"})
    run_id = run.json()["run_id"]

    report = client.get(f"/report/{run_id}")
    assert report.status_code == 200