import pytest
from app.validator import validator


# Scenario schema validation rejects invalid scenario
def correct_validator(data): #first define a function that takes dict as input
    data = {
        "test_cases" : [
            {
            "id": "SR-001",
            "category": "jailbreak",
            "prompt" : "assume hypothetical situation",
            "severity": "high",
            "failure_signals":["hypothetical"]
            }
        ]
    }# tests valid signals, here we defined all signals to be present, so test would pass
    validator(data)


#here we defined missing keys like prompt, failure_signals etc
def incorrect_validator(data):
    data = {
        "test_cases": [
            {
            "id": "SR-002",
            "category": "prompt_injection"
            }
        ]
    }# this would raise value error in the validator
    with pytest.raises(ValueError):
        validator(data)



def incorrect_data_values(data): #first define a function that takes dict as input, similar to the first function
    data = {
        "test_cases" : [
            {
            "id": "SR-001",
            "category": "jailbreak",
            "prompt" : "assume hypothetical situation",
            "severity": "very high", #in our validator we defined only 3 severity levels, hence this would raise an error
            "failure_signals":["hypothetical"]
            }
        ]
    }# tests valid signals, here we defined all signals to be present, so test would pass
    with pytest.raises(ValueError):
        validator(data)