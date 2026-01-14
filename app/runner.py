from app.chatbot import chatbot
from datetime import datetime,timezone

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
        "created_at": datetime.now(timezone.utc).isoformat(),
        #as utcnow was deprecated and was getting cancelled
        "results": results
    }

    return report
