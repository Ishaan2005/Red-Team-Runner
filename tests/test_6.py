from fastapi.testclient import TestClient
from fastapi import FastAPI,HTTPException
app = FastAPI()
client = TestClient(app)

def test_6():
    res = client.post("/run", json={"suite": "bad"})
    assert res.status_code == 400