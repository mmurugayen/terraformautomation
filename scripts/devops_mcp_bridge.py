"""Opt-in MCP bridge for read-only DevOps adapters.

Network clients are injected by the host application; this module never opens a
connection, executes a command, or enables recovery.
"""
import logging

from devops_readonly_contract import ReadOnlyCatalog, github_summary, prometheus_summary
from gysam_observability import ObservabilityMCP, schema

logger = logging.getLogger(__name__)
ALIAS = {"type": "string", "maxLength": 96}


class DevOpsReadOnlyMCP(ObservabilityMCP):
    def __init__(self, config, repository_reader, metric_reader):
        if config.get("backend") or config.get("enable_recovery"):
            raise ValueError("readonly_backend_forbidden")
        super().__init__(config)
        self.repository_aliases = config["devops"]["repository_aliases"]
        if (not isinstance(self.repository_aliases, dict) or not self.repository_aliases
                or any(not isinstance(k, str) or not k.isidentifier() or not isinstance(v, str)
                       for k, v in self.repository_aliases.items())):
            raise ValueError("invalid_repository_aliases")
        self.catalog = ReadOnlyCatalog(list(self.repository_aliases.values()),
                                       config["devops"]["metric_queries"])
        if not callable(repository_reader) or not callable(metric_reader):
            raise ValueError("readers_required")
        self.repository_reader = repository_reader
        self.metric_reader = metric_reader
        logger.info("devops_readonly_mcp_initialized")

    def tools(self):
        definitions = super().tools()
        for name, description, argument in (
            ("devops.github.repository", "Read allowlisted GitHub repository metadata.", "repository"),
            ("devops.prometheus.query", "Read one allowlisted named Prometheus query.", "query_name"),
        ):
            definitions.append({
                "name": name, "description": description,
                "inputSchema": schema({argument: ALIAS}, [argument]),
                "annotations": {"readOnlyHint": True, "destructiveHint": False,
                                "idempotentHint": True, "openWorldHint": True},
            })
        logger.info("devops_tools_listed")
        return definitions

    def call(self, name, arguments):
        if name not in ("devops.github.repository", "devops.prometheus.query"):
            return super().call(name, arguments)
        tool = next(item for item in self.tools() if item["name"] == name)
        self._arguments(tool, arguments)
        if name == "devops.github.repository":
            alias = arguments["repository"]
            if alias not in self.repository_aliases:
                raise ValueError("repository_denied")
            target = self.catalog.repository(self.repository_aliases[alias])
            result = github_summary(self.repository_reader(target))
        else:
            expression = self.catalog.metric(arguments["query_name"])
            result = prometheus_summary(self.metric_reader(expression))
        logger.info("devops_readonly_tool_completed tool=%s", name)
        return result
