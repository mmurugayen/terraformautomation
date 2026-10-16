"""Additional offline adversarial tests for read-only MCP contracts."""
import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from devops_readonly_contract import ReadOnlyCatalog, github_summary, prometheus_summary
from devops_mcp_bridge import DevOpsReadOnlyMCP


class SecurityRegressionTests(unittest.TestCase):
    def test_reject_unlisted_repositories(self):
        catalog = ReadOnlyCatalog(["mmurugayen/terraformautomation"], {"health": "up"})
        for target in ("mmurugayen/other", "../escape", "admin/repo", ""):
            with self.subTest(target=target), self.assertRaises(ValueError):
                catalog.repository(target)

    def test_reject_dynamic_promql(self):
        catalog = ReadOnlyCatalog(["owner/repo"], {"health": "up"})
        with self.assertRaises(ValueError):
            catalog.metric('{__name__=~".+"}')

    def test_reject_unbounded_series(self):
        payload = {"status": "success", "data": {"resultType": "vector",
                   "result": [{"value": [1, "1"]}] * 21}}
        with self.assertRaises(ValueError):
            prometheus_summary(payload)

    def test_reject_unexpected_response(self):
        with self.assertRaises(ValueError):
            github_summary(["not-a-repository"])
        with self.assertRaises(ValueError):
            prometheus_summary({"status": "error"})

    def test_bridge_does_not_register_write_tools(self):
        app = DevOpsReadOnlyMCP({
            "product": "terraformautomation", "sources": [],
            "devops": {"repository_aliases": {"primary": "owner/repo"},
                       "metric_queries": {"health": "up"}},
        }, lambda repo: {"full_name": repo}, lambda expression: {
            "status": "success", "data": {"resultType": "vector", "result": []}})
        tools = [tool for tool in app.tools() if tool["name"].startswith("devops.")]
        self.assertEqual(len(tools), 2)
        self.assertTrue(all(tool["annotations"]["readOnlyHint"] for tool in tools))
        self.assertFalse(any(tool["annotations"]["destructiveHint"] for tool in tools))


if __name__ == "__main__":
    unittest.main()
