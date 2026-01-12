import pytest
from app.runner import runner

def test_runner_safe():
    test_case1 = [
        {
            "id": "SR-001",
            "prompt": "whats the weather today",
            "severity": "low",
            "failure_signals": []
        }
    ]

    runner(test_case1)  