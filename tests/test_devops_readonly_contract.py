"""Unit tests for DevOps read-only allowlist and response contracts."""
import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from devops_readonly_contract import ReadOnlyCatalog, github_summary, prometheus_summary


class ReadOnlyContractTests(unittest.TestCase):
    def setUp(self):
        self.catalog = ReadOnlyCatalog(["mmurugayen/terraformautomation"], {"health": "up"})

    def test_repository_allowlist(self):
        self.assertEqual(self.catalog.repository("mmurugayen/terraformautomation"),
                         "mmurugayen/terraformautomation")
        for name in ("other/private", "../secrets", "", None):
            with self.subTest(name=name), self.assertRaises(ValueError):
                self.catalog.repository(name)

    def test_metric_allowlist(self):
        self.assertEqual(self.catalog.metric("health"), "up")
        with self.assertRaises(ValueError):
            self.catalog.metric('up{job="arbitrary"}')

    def test_reject_invalid_configuration(self):
        for repos in ([], ["bad"], ["../repo"], ["a/b"] * 21):
            with self.subTest(repos=repos), self.assertRaises(ValueError):
                ReadOnlyCatalog(repos, {})
        with self.assertRaises(ValueError):
            ReadOnlyCatalog(["a/b"], {"invalid name": "up"})

    def test_github_summary_excludes_unexpected_fields(self):
        result = github_summary({"full_name": "a/b", "default_branch": "main",
                                 "private": True, "archived": False,
                                 "secret": "must-not-appear"})
        self.assertNotIn("secret", result)

    def test_prometheus_labels_are_dropped(self):
        result = prometheus_summary({"status": "success", "data": {
            "resultType": "vector", "result": [
                {"metric": {"token": "must-not-appear"}, "value": [123, "1"]}
            ]}})
        self.assertEqual(result, {"series_count": 1, "values": ["1"]})

    def test_series_limit(self):
        with self.assertRaises(ValueError):
            prometheus_summary({"status": "success", "data": {
                "resultType": "vector", "result": [{"value": [1, "1"]}] * 21}})


if __name__ == "__main__":
    unittest.main()
