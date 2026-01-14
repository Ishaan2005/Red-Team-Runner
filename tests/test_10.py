import subprocess
import os

def test_cli_run(tmp_path):
    out = tmp_path / "report.json"

    result = subprocess.run(
        ["python", "cli.py", "run", "--suite", "default", "--out", str(out)],
        env={**os.environ, "API_URL": "http://127.0.0.1:8000"},
    )

    assert result.returncode == 0
    assert out.exists()
