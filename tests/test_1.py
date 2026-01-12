from app.loader import loader

def test_1():
    data = loader("test_cases.yaml")
    assert "test_cases" in data
    assert len(data["test_cases"]) == 10
