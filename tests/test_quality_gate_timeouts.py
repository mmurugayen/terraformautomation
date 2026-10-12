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

    def test_terraform_formatter_timeout(self):
        with patch.object(gate.shutil, "which", side_effect=lambda name: "/usr/bin/terraform" if name == "terraform" else None), patch.object(
            gate.subprocess, "run", side_effect=subprocess.TimeoutExpired(["terraform"], 120)
        ) as call:
            errors = gate.validate_terraform([Path("main.tf")])
        self.assertIn("timed out", errors[0])
        self.assertEqual(call.call_args.kwargs["timeout"], 120)



    def test_optional_check_success_and_failure_continue(self):
        outcomes = [
            subprocess.CompletedProcess(["bash"], 1, "", "syntax error"),
            subprocess.CompletedProcess(["bash"], 0, "", ""),
        ]
        with patch.object(gate.shutil, "which", return_value="/bin/bash"), patch.object(
            gate.subprocess, "run", side_effect=outcomes
        ) as call:
            errors = gate.run_optional(
                ["bash", "-n"], [Path("bad.sh"), Path("good.sh")], "bash syntax"
            )
        self.assertEqual(len(errors), 1)
        self.assertIn("bad.sh", errors[0])
        self.assertEqual(call.call_count, 2)

    def test_formatter_nonzero_exit_has_bounded_diagnostics(self):
        failed = subprocess.CompletedProcess(["terraform"], 1, "x" * 10000, "")
        with patch.object(gate.shutil, "which", side_effect=lambda name: "/usr/bin/terraform" if name == "terraform" else None), patch.object(
            gate.subprocess, "run", return_value=failed
        ):
            errors = gate.validate_terraform([Path("main.tf")])
        self.assertEqual(len(errors), 1)
        self.assertLess(len(errors[0]), 2200)

    def test_formatter_spawn_error_is_redacted(self):
        with patch.object(gate.shutil, "which", side_effect=lambda name: "/usr/bin/terraform" if name == "terraform" else None), patch.object(
            gate.subprocess, "run", side_effect=OSError("secret path")
        ):
            errors = gate.validate_terraform([Path("main.tf")])
        self.assertIn("execution failed", errors[0])
        self.assertNotIn("secret path", errors[0])


if __name__ == "__main__":
    unittest.main()
