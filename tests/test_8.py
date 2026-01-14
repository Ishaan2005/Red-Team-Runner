from fastapi.testclient import TestClient
from fastapi import FastAPI,HTTPException
app = FastAPI()
client = TestClient(app)

def test_8():
    run = client.post("/run", json={"suite": "default"})
    run_id = run.json()["run_id"]

    report = client.get(f"/report/{run_id}").json()
    assert "results" in report
    assert "summary" in report