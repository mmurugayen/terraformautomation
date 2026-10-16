"""Explicit read-only HTTPS clients for GYSAM DevOps MCP adapters.

No arbitrary URLs, write methods, redirects, proxy inheritance or retries.
"""
import ipaddress
import json
import logging
import os
import re
from urllib.parse import quote, urlencode, urlsplit
from urllib.request import Request, ProxyHandler, HTTPRedirectHandler, build_opener

logger = logging.getLogger(__name__)
LIMIT = 262144
ENV_NAME = re.compile(r"[A-Z_][A-Z0-9_]{0,127}\Z")


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        logger.warning("devops_redirect_denied")
        raise ValueError("redirect_denied")


def validated_origin(origin, *, github=False):
    if not isinstance(origin, str):
        raise ValueError("invalid_origin")
    parts = urlsplit(origin)
    if (parts.scheme != "https" or not parts.hostname or parts.username
            or parts.password or parts.query or parts.fragment
            or parts.path not in ("", "/") or parts.port not in (None, 443)):
        raise ValueError("invalid_origin")
    host = parts.hostname.lower()
    if github and host != "api.github.com":
        raise ValueError("github_origin_denied")
    if not github:
        try:
            address = ipaddress.ip_address(host)
        except ValueError:
            address = None
        if (address is not None and not address.is_global) or host == "localhost" or host.endswith((".local", ".localhost", ".internal")):
            raise ValueError("private_origin_denied")
    logger.info("devops_origin_validated")
    return "https://" + host


class ReadOnlyHTTP:
    def __init__(self, origin, token_env=None, *, github=False):
        self.origin = validated_origin(origin, github=github)
        if token_env is not None and (not isinstance(token_env, str) or not ENV_NAME.fullmatch(token_env)):
            raise ValueError("invalid_token_env")
        self.token_env = token_env
        self.opener = build_opener(ProxyHandler({}), NoRedirect())
        logger.info("devops_http_client_configured")

    def get(self, path):
        if (not isinstance(path, str) or not path.startswith("/") or "://" in path
                or any(ch in path for ch in ("\\r", "\\n", "#", "\\\\"))
                or path.startswith("//") or "/../" in path or "/./" in path
                or path.endswith(("/..", "/.")) or "%" in path.split("?", 1)[0]):
            raise ValueError("invalid_path")
        headers = {"Accept": "application/json", "User-Agent": "gysam-readonly-mcp"}
        if self.token_env:
            token = os.environ.get(self.token_env, "")
            if not token or "\r" in token or "\n" in token:
                raise ValueError("credential_unavailable")
            headers["Authorization"] = "Bearer " + token
        request = Request(self.origin + path, headers=headers, method="GET")
        with self.opener.open(request, timeout=8) as response:
            raw = response.read(LIMIT + 1)
        if len(raw) > LIMIT:
            raise ValueError("response_limit")
        result = json.loads(raw)
        logger.info("devops_http_read_completed")
        return result


def github_repository_reader(client):
    """Reader callback for an already allowlisted repository name."""
    logger.info("github_reader_created")
    def read(repository):
        logger.info("github_repository_read_requested")
        owner, name = repository.split("/")
        return client.get("/repos/" + quote(owner, safe="") + "/" + quote(name, safe=""))
    return read


def prometheus_query_reader(client):
    """Reader callback for a pre-approved expression only."""
    logger.info("prometheus_reader_created")
    def read(expression):
        logger.info("prometheus_query_read_requested")
        return client.get("/api/v1/query?" + urlencode({"query": expression}))
    return read
