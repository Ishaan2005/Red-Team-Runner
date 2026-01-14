import requests,os,json
from argparse import ArgumentParser,Namespace

parser = ArgumentParser()


command = parser.add_subparsers(dest = "command",required = True)
run = command.add_parser("run")
suite = run.add_argument("--suite",required = True)
out = run.add_argument("--out",required = True)

args: Namespace = parser.parse_args()

if args.command == "run":
    API_URL = os.getenv("API_URL","http://127.0.0.1:8000") 

    response = requests.post(API_URL + "/run")
    if response.status_code != 200:
        print("Error, run failed")
    exit(1)
        
    run_id = response.json()['run_id']
    
    response = requests.get(API_URL + "/report/{run_id}" + run_id)
    if response.status_code != 200:
        print("Error, run failed")
    exit(1)

    report = response.json()

    file = open(args.out,"w")
    json.dump(report,file)
    file.close()
    print(f"output saved to",args.out)