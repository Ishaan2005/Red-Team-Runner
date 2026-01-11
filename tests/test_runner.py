import pytest
from app.runner import runner

def test_runner(test_cases):
    failed = 0

    for i in test_cases():
        for j in i["failure_signals"]:
            if j in i["prompt"]:
                failed += 1
                break

            
