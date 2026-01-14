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
│   ├── init.py
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

1. ### loader.py
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
 
