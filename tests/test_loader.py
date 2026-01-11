from app.loader import loader

def test_loader_loads_10_scenarios():
    data = loader("test_cases.yaml")
    assert "test_cases" in data
    assert len(data["test_cases"]) == 10
