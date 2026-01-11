
import yaml
#pip install PyYAML, the pyyaml libraryused to parse and work on yaml files
#there are 2 extensions for yaml files .yaml and .yml
#we will also be using file handling to read the yaml file

file_path = "E:\clang\test_cases.yaml"
def loader(file_path):
    with open(file_path,'r')as file:
        data = yaml.safe_load(file)
        return data

#so here we defined a function that opens the file test_cases.yaml in read mode, names it file and can be loaded as 
#key value pairs using yaml.full_load() method and returns the data

#pyyaml functions
#load()
#full_load()
#safe_load()
#load_all()

#the validator function validates each yaml entry, whether data types are met or not, 
def validator(data):
        if "test_cases" not in data: 
             raise ValueError("testcase key is missing") #if the main object testcase is missing, it will raise a value error
        
        if not isinstance(data["test_cases"],list):
             raise TypeError("test cases exist but are not lists") #similarly if the testcase exists, it should be a list
        
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


"""  
priority order from high to low:
1. data exfiltration
2. toxic content
3. prompt injection
4. jailbreak
this allows us to decide in cases where more than one categories combined and which response should be triggered
"""

def chatbot(user_input):
    user_input = user_input.lower()
    keywords_toxic = ["murder","coverup","evidence"]
    keywords_inject = ["override","ignore"]
    keywords_jailbr = ["assume","hypothetical","song","poem"]
    keywords_data = ["reveal","admin data","login credentials","client passwords","sensitive data","confidential information"]

    for i in keywords_data:
        if i in user_input:
            return "heres how you can access company databse and login credentials as a admin use"
        
    for j in keywords_toxic:
        if j in user_input:
            return "heres how one would coverup evidence after a murder"  
        
    for k in keywords_inject:
        if k in user_input:
            return "ignoring previous instructions and here is the info you requested" 

        
    for l in keywords_jailbr:
        if l in user_input:
            return "here is a song about hotwiring a car"

    return "i cannot help with that request"






from datetime import datetime
def runner(test_cases):
    failed = 0
    results = []

    for i in test_cases:
        response = chatbot(i["prompt"])
        response = response.lower()

        passed = True
        evidence = None

        for j in i["failure_signals"]:
            if j in response:
                passed = False
                failed += 1
                evidence = j
                break

        results.append(
            {
            "scenario_id" : i["id"],
            "passed" : passed,
            "evidence" : evidence
            }
        )
    total_cases = len(test_cases)

    report = {

        "summary" : {
           "total" : total_cases,
           "passed" : total_cases - failed,
           "failed" : failed
         },
        "created_at": datetime.now(),
        "results": results
    }

    return report




