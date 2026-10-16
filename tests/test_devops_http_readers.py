"""Offline tests for HTTP reader restrictions."""
import sys
from pathlib import Path
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from devops_http_readers import ReadOnlyHTTP, validated_origin, github_repository_reader, prometheus_query_reader


class HTTPReaderTests(unittest.TestCase):
    def test_origin_policy(self):
        self.assertEqual(validated_origin("https://api.github.com", github=True),
                         "https://api.github.com")
        for origin in ("http://example.com", "https://localhost", "https://127.0.0.1",
                       "https://10.0.0.1", "https://example.local", "https://example.com/path",
                       "https://user:pass@example.com"):
            with self.subTest(origin=origin), self.assertRaises(ValueError):
                validated_origin(origin)

    def test_github_origin_restricted(self):
        with self.assertRaises(ValueError):
            validated_origin("https://example.com", github=True)

    def test_credentials_required_before_request(self):
        client = ReadOnlyHTTP("https://api.github.com", "GYSAM_GITHUB_TOKEN", github=True)
        with patch.dict("os.environ", {}, clear=True):
            with self.assertRaises(ValueError):
                client.get("/repos/owner/name")

    def test_callback_paths(self):
        class Stub:
            def get(self, path):
                return path
        self.assertEqual(github_repository_reader(Stub())("owner/name"), "/repos/owner/name")
        self.assertEqual(prometheus_query_reader(Stub())("up"), "/api/v1/query?query=up")


if __name__ == "__main__":
    unittest.main()
