import json
from pathlib import Path


def test_report_exists():
    """The agent produced a report file."""
    assert Path("/app/report.json").exists(), "no report.json found"


def test_report_valid_json():
    """The report file is valid JSON."""
    text = Path("/app/report.json").read_text()
    assert len(text) > 0, "report.json is empty"
    data = json.loads(text)
    assert isinstance(data, dict), "report.json root must be a JSON object"


def test_total_requests():
    """total_requests equals the number of log lines."""
    data = json.loads(Path("/app/report.json").read_text())
    assert data["total_requests"] == 6, f"expected 6, got {data['total_requests']}"


def test_unique_ips():
    """unique_ips equals the number of distinct client IPs."""
    data = json.loads(Path("/app/report.json").read_text())
    assert data["unique_ips"] == 3, f"expected 3, got {data['unique_ips']}"


def test_top_path():
    """top_path is the most frequently requested path."""
    data = json.loads(Path("/app/report.json").read_text())
    assert data["top_path"] == "/index.html", f"expected /index.html, got {data['top_path']}"
