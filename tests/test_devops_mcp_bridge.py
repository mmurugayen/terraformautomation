"""Offline tests for read-only MCP tool registration."""
import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from devops_mcp_bridge import DevOpsReadOnlyMCP


class BridgeTests(unittest.TestCase):
    def test_read_only_tools_and_denial(self):
        config = {
            "product": "terraformautomation",
            "sources": [],
            "devops": {
                "repository_aliases": {"primary": "mmurugayen/terraformautomation"},
                "metric_queries": {"health": "up"},
            },
        }
        app = DevOpsReadOnlyMCP(config, lambda repo: {"full_name": repo},
                                lambda query: {"status": "success", "data": {
                                    "resultType": "vector", "result": []}})
        tools = [item for item in app.tools() if item["name"].startswith("devops.")]
        self.assertEqual(len(tools), 2)
        self.assertTrue(all(item["annotations"]["readOnlyHint"] for item in tools))
        self.assertEqual(app.call("devops.github.repository", {"repository": "primary"})["full_name"],
                         "mmurugayen/terraformautomation")
        with self.assertRaises(ValueError):
            app.call("devops.github.repository", {"repository": "unknown"})


if __name__ == "__main__":
    unittest.main()
