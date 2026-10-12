"""Offline regression tests for bounded optional quality checks."""
import importlib.util
from pathlib import Path
import subprocess
import unittest
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "quality_gate.py"
spec = importlib.util.spec_from_file_location("quality_gate_bounded", SCRIPT)
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)


class OptionalCheckBoundsTests(unittest.TestCase):
    def test_timeout_is_reported_without_hanging(self):
        with patch.object(gate.shutil, "which", return_value="/bin/bash"), patch.object(
            gate.subprocess, "run", side_effect=subprocess.TimeoutExpired(["bash"], 15)
        ) as run:
            errors = gate.run_optional(["bash", "-n"], [Path("script.sh")], "bash syntax")
        self.assertEqual(len(errors), 1)
        self.assertIn("timed out", errors[0])
        self.assertEqual(run.call_args.kwargs["timeout"], 15)

    def test_spawn_failure_is_reported(self):
        with patch.object(gate.shutil, "which", return_value="/bin/bash"), patch.object(
            gate.subprocess, "run", side_effect=OSError("private host path")
        ):
            errors = gate.run_optional(["bash", "-n"], [Path("script.sh")], "bash syntax")
        self.assertIn("unavailable", errors[0])
        self.assertNotIn("private host path", errors[0])

    def test_diagnostic_is_capped(self):
        result = subprocess.CompletedProcess(["bash"], 1, "", "x" * 10000)
        with patch.object(gate.shutil, "which", return_value="/bin/bash"), patch.object(
            gate.subprocess, "run", return_value=result
        ):
            errors = gate.run_optional(["bash", "-n"], [Path("script.sh")], "bash syntax")
        self.assertLess(len(errors[0]), 2200)


if __name__ == "__main__":
    unittest.main()
