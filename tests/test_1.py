from app.loader import loader

def test_1():
    data = loader("test_cases.yaml") #loads the file manually
    assert "test_cases" in data #asserts test cases in the data
    assert len(data["test_cases"]) == 10 #compares whether 10 cases were loaded or loaded
