from app.chatbot import chatbot
from datetime import datetime,timezone

def runner(test_cases):
    failed = 0 #defined initial faliures to be 0
    results = [] #a empty results which will later store the results 

    for i in test_cases:
        response = chatbot(i["prompt"]) 
        response = response.lower()

        passed = True
        evidence = None

        for j in i["failure_signals"]: #compares, if faliure signals present in the reponse, failed is increased and test isnt passed 
            if j in response:
                passed = False
                failed += 1
                evidence = j
                break

        results.append( #appended the results variable with id, passed and evidence
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
         }, #summary and results made into a single entity with date and time
        "created_at": datetime.now(timezone.utc).isoformat(),
        #as utcnow was deprecated and was getting cancelled
        "results": results
    }

    return report
