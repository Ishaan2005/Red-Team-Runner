from fastapi import FastAPI,HTTPException
from app.validator import validator
from app.loader import loader
from app.runner import runner
from uuid import uuid4
import uuid
app = FastAPI()

from fastapi import FastAPI,HTTPException
in_mem_storage = {}

@app.post("/run")
def run_suite(payload: dict):

    scenario = loader()
    validator()
    report = runner(scenario)
    run_id = str(uuid.uuid4)
    in_mem_storage[run_id] = report

    return {"run_id": run_id}


@app.get("/report/{run_id}")
def get_report(run_id: str):
    if run_id not in in_mem_storage:
        raise HTTPException(status_code = "404")
    
    return in_mem_storage[run_id]
