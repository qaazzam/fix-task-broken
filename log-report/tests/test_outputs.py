import json
from pathlib import Path


def test_report_exists_and_valid_json():
    """Criterion 1: /app/report.json exists and is valid JSON."""
    assert Path("/app/report.json").exists(), "no report.json found"
    text = Path("/app/report.json").read_text()
    assert len(text) > 0, "report.json is empty"
    data = json.loads(text)
    assert isinstance(data, dict), "report.json root must be a JSON object"


def test_total_requests():
    """Criterion 2: total_requests is the total number of log lines (6)."""
    data = json.loads(Path("/app/report.json").read_text())
    assert data["total_requests"] == 6, f"expected 6, got {data['total_requests']}"


def test_unique_ips():
    """Criterion 3: unique_ips is the count of distinct client IPs (3)."""
    data = json.loads(Path("/app/report.json").read_text())
    assert data["unique_ips"] == 3, f"expected 3, got {data['unique_ips']}"


def test_top_path():
    """Criterion 4: top_path is the most frequently requested path (/index.html)."""
    data = json.loads(Path("/app/report.json").read_text())
    assert data["top_path"] == "/index.html", f"expected /index.html, got {data['top_path']}"
