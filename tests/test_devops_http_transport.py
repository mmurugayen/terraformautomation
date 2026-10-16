"""Offline HTTP transport tests: bounded responses and read-only requests."""
import json
import sys
from pathlib import Path
from unittest import TestCase
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from devops_http_readers import LIMIT, ReadOnlyHTTP


class _Response:
    def __init__(self, content):
        self.content = content

    def __enter__(self):
        return self

    def __exit__(self, *_args):
        return False

    def read(self, size):
        return self.content[:size]


class TransportContractTests(TestCase):
    def test_get_is_bounded_and_uses_get(self):
        client = ReadOnlyHTTP("https://api.github.com", github=True)
        payload = json.dumps({"full_name": "owner/repo"}).encode()
        with patch.object(client.opener, "open", return_value=_Response(payload)) as mocked:
            result = client.get("/repos/owner/repo")
        self.assertEqual(result["full_name"], "owner/repo")
        request = mocked.call_args.args[0]
        self.assertEqual(request.get_method(), "GET")
        self.assertEqual(mocked.call_args.kwargs["timeout"], 8)

    def test_oversized_response_is_rejected(self):
        client = ReadOnlyHTTP("https://api.github.com", github=True)
        with patch.object(client.opener, "open",
                          return_value=_Response(b"x" * (LIMIT + 1))):
            with self.assertRaisesRegex(ValueError, "response_limit"):
                client.get("/repos/owner/repo")

    def test_invalid_paths_are_rejected(self):
        client = ReadOnlyHTTP("https://api.github.com", github=True)
        for path in ("https://example.com", "repos/owner/repo", None):
            with self.subTest(path=path), self.assertRaises(ValueError):
                client.get(path)


if __name__ == "__main__":
    import unittest
    unittest.main()
