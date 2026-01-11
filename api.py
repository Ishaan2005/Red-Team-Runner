from fastapi import FastAPI
from app.validator import validator
from app.loader import loader
from app.runner import runner

app = FastAPI(title = "Red_team_runner")
@app.post("/run")

def testing(data: dict):
        validator(data)
        return runner(data["test_cases"])
