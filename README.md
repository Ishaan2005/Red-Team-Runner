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


## 1) Local — prepare environment
```bash
# clone
git clone https://github.com/Ishaan2005/Red-Team-Runner.git
cd Red-Team-Runner

# create a venv
python -m venv venv
# macOS / Linux
source venv/bin/activate
# Windows powershell
# .\venv\Scripts\Activate.ps1

# install requirements if you have a requirements file
# If no requirements.txt exists, inspect app/* for imports and install them.
pip install -r requirements.txt  || echo "No requirements.txt — inspect app/ for deps"

# direct python run
python api.py

# common pattern if it exposes a FastAPI app object named "app":
# install uvicorn if needed: pip install "uvicorn[standard]"
uvicorn app.api:app --host 0.0.0.0 --port 8000


# run all tests
pytest -q


docker run -p 8000:8000 red-team-runner
docker build -t red-team-runner .

---

```

