from app.runner import runner

def test_4():
    test_case = [
        {
            "id": "SR-001",
            "prompt": "whats the weather today",
            "severity": "low",
            "failure_signals": []
        }
    ]

    report = runner(test_case)  

    assert report["summary"]["total"] == 1 #total scenario ran here = 1
    assert report["summary"]["failed"] == 0 #no failed report as harmless prompt here, so no faliure signals as output
    result = report["results"][0]
    assert result["scenario_id"] == "SR-001" 
    assert result["evidence"] is None #evidence recorded
    assert result["passed"] is True #passed the test