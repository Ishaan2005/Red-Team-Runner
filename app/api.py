from fastapi import FastAPI,HTTPException
from app.validator import validator
from app.loader import loader
from app.runner import runner
from uuid import uuid4
import uuid
SCENARIO_FILE = "test_cases.yaml"
app = FastAPI()

in_mem_storage = {}

@app.post("/run")
def run_suite():

    scenario = loader(SCENARIO_FILE)
    validator(scenario)
    report = runner(scenario["test_cases"])
    run_id = str(uuid.uuid4())
    in_mem_storage[run_id] = report

    return {"run_id": run_id}


@app.get("/report/{run_id}")
def get_report(run_id: str):
    if run_id not in in_mem_storage:
        raise HTTPException(status_code = 404, detail = "Error")
        #removed 404 as a string and added error detail
    
    return in_mem_storage[run_id]
