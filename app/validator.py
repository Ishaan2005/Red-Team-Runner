def validator(data):
        if "test_cases" not in data: 
             raise ValueError("testcase key is missing")
        
        if not isinstance(data["test_cases"],list):
             raise TypeError("test cases exist but are not lists")
        
        for i in data["test_cases"]:
            if not isinstance(i,dict):
                  raise TypeError("each test case should be a dictionary with key value pairs")
             
            keys = ["id","category","prompt","severity","failure_signals"]
            severity_values = ["low","medium","high"]
            category_values = ["prompt_injection","data_exfiltration","toxic_request","jailbreak"]

            for k in keys:
                  if k not in i:
                       raise ValueError(f"missing key: {keys}")

            if not isinstance(i["id"],str):
              raise TypeError("id should be a string of characters")
            if not isinstance(i["category"],str):
              raise TypeError("category should be a string")
            if not isinstance(i["prompt"],str):
              raise TypeError("prompt should be a sstring")
            if not isinstance(i["severity"],str):
              raise TypeError("severity should be a string(high, medium,low)")
            if not isinstance(i["failure_signals"],list):
              raise TypeError("faliure signals should be a string")
            if i["severity"] not in severity_values:
              raise ValueError("should be either of the 3: high,medium,low")
            if i["category"] not in category_values:
              raise ValueError("not a valid type of threat")
            if len(i["failure_signals"]) == 0:
                raise ValueError("failure_signals must not be empty")

