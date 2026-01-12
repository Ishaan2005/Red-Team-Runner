from fastapi.testclient import TestClient
from fastapi import FastAPI,HTTPException
app = FastAPI()
client = TestClient(app)

def test_get_report_returns_saved_report():
    run = client.post("/run", json={"suite": "default"})
    run_id = run.json()["run_id"]

    report = client.get(f"/report/{run_id}")
    assert report.status_code == 200