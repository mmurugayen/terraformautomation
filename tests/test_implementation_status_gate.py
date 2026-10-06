import json
import subprocess
import sys
from pathlib import Path

SCRIPT = Path("scripts/implementation_status_gate.py")


def run(tmp_path, payload, *extra):
    path = tmp_path / "status.json"
    path.write_text(json.dumps(payload))
    return subprocess.run(
        [sys.executable, str(SCRIPT), "--file", str(path), *extra],
        capture_output=True,
        text=True,
    )


def test_accepts_evidenced_implemented(tmp_path):
    result = run(tmp_path, {"items": [{"id": "x", "status": "implemented", "evidence": ["tests/test_x.py"]}]})
    assert result.returncode == 0
    assert '"complete": true' in result.stdout


def test_rejects_implemented_without_evidence(tmp_path):
    result = run(tmp_path, {"items": [{"id": "x", "status": "implemented", "evidence": []}]})
    assert result.returncode != 0


def test_native_pending_is_fail_closed_for_release(tmp_path):
    result = run(
        tmp_path,
        {"items": [{"id": "x", "status": "native_pending", "native_required": True, "evidence": []}]},
        "--require-complete",
    )
    assert result.returncode == 2


def test_rejects_native_pending_without_native_flag(tmp_path):
    result = run(tmp_path, {"items": [{"id": "x", "status": "native_pending", "evidence": []}]})
    assert result.returncode != 0
