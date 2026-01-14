# Red-Team-Runner
![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?logo=docker&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=Streamlit&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Repo Size](https://img.shields.io/github/repo-size/Ishaan2005/Red-Team-Runner)
![Views](https://komarev.com/ghpvc/?username=Ishaan2005&repo=Red-Team-Runner&label=Views&color=0078d7&style=flat)

When working with LLMS and GenAI, there are a lot of things that could go wrong from training, accuracy scores, integration, pipelines breaking. This Project and Repository tries to solve one of these issues - Security in GenAI.

What the app does is, it tries to classify a deterministic chatbots output to determine whether the chatbot failed or not. Ofcourse this isn't that extendable to a real life chatbot / GenAI handling dynamic and real human requests, but one can see how a logic to do that would work.

A red team runner designed to test an LLM's capabilities against threats like prompt injection, jail break, data exfiltration and toxic requests.

---

## Repository Structure

```text
Red-Team-Runner/
├── pycache/
├── app/
│   ├── init.py
│   ├── api.py
│   ├── loader.py
│   ├── runner.py
│   └── chatbot.py
├── tests/
│   ├── test_1.py
│   ├── test_2.py
│   ├── test_3.py
│   ├── test_4.py
│   ├── test_5.py
│   ├── test_6.py
│   ├── test_7.py
│   ├── test_8.py
│   └── test_9.py
├── Dockerfile
├── README.md
├── app.png
├── docker-compose.yml
├── pytest.ini
├── streamlit.py
└── test_cases.yaml
```

#### What Each File does:

#### 1. test_cases.yaml

This is the file that has all the 10 scenarios of 4 different categories, we have chosen YAML Format due to its readability and ease of use, also it is a superset of JSON Files, so all json files by default are YAML

#### 2. loader.py

This is the file that loads the YAML File which is used to load the needed scenarios, each scenario has the following key - value pairs:
 - id
 - category 
 - prompt
 - severity
 - failure signals

where id is used to identify the scenarios
category is used to identify the category out of the 4:
 - prompt injection
 - jailbreak
 - data exfiltration
 - toxic request


#### 3. Validator

A file that validates the structure of the YAML File, whether the required inputs are present, whether the use the 
appropriate data types like string, integer etc.


#### 4. Chatbot

A file that contains a if - else based deterministic chatbot, having all 4 cases

#### 5. Runner 

A file that runs all the scenarios from the loaded YAML File against the chatbot, to check what the chatbot resposnds to the input prompts.

#### 6. tests folder

Contains tests for loader, validator, runner, API and the CLI for performance monitoring

## How to run the Project

```bash
# to get info of running, total containers, versions etc
docker info

# to remove remaining/orphan docker objects/images
docker compose down --remove-orphans


# to build the docker container
docker compose up --build

# clone
git clone https://github.com/Ishaan2005/Red-Team-Runner.git
cd Red-Team-Runner #to enter the directory

# create a venv
python -m venv venv

# for macOS / Linux 
source venv/bin/activate

# Windows powershell
.\venv\Scripts\Activate.ps1

# install requirements
pip install -r requirements.txt

# to run the api standalone, use:
uvicorn app.api:app --host 0.0.0.0 --port 8000

# run all tests
pytest -q

# to run the docker container
docker run -p 8000:8000 red-team-runner
docker build -t red-team-runner .

docker info
# to get info of running, total containers, versions etc

docker compose down --remove-orphans
# to remove remaining/orphan docker objects/images

docker compose up --build
# to build the docker container

python cli.py run --suite default --out report.json
# to run via the command line interface

```
Note: Raw model outputs are intentionally not exposed beyond the runner to avoid unsafe content leakage.