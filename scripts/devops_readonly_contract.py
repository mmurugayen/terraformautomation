"""Pure validation and response shaping for read-only DevOps MCP integrations.

Transport, authentication, and deployment are intentionally separate.
"""
import logging
import re

logger = logging.getLogger(__name__)
NAME = re.compile(r"[A-Za-z0-9_.-]{1,100}\Z")


class ReadOnlyCatalog:
    """Explicitly registered resources and named metric expressions."""

    def __init__(self, repositories, metric_queries):
        if not isinstance(repositories, list) or not 1 <= len(repositories) <= 20:
            raise ValueError("invalid_repositories")
        if not isinstance(metric_queries, dict) or len(metric_queries) > 20:
            raise ValueError("invalid_metric_queries")
        for repo in repositories:
            if not isinstance(repo, str) or len(repo.split("/")) != 2 or not all(
                NAME.fullmatch(part) for part in repo.split("/")
            ):
                raise ValueError("invalid_repository")
        for name, expression in metric_queries.items():
            if not isinstance(name, str) or not NAME.fullmatch(name):
                raise ValueError("invalid_metric_name")
            if not isinstance(expression, str) or not 1 <= len(expression) <= 512:
                raise ValueError("invalid_metric_expression")
        self.repositories = frozenset(repositories)
        self.metric_queries = dict(metric_queries)
        logger.info("readonly_catalog_initialized")

    def repository(self, name):
        """Return an approved repository name, never an arbitrary path."""
        if not isinstance(name, str) or name not in self.repositories:
            logger.warning("readonly_repository_denied")
            raise ValueError("repository_denied")
        logger.info("readonly_repository_approved")
        return name

    def metric(self, name):
        """Resolve a pre-approved PromQL expression by stable alias."""
        if not isinstance(name, str) or name not in self.metric_queries:
            logger.warning("readonly_metric_denied")
            raise ValueError("metric_denied")
        logger.info("readonly_metric_approved")
        return self.metric_queries[name]


def github_summary(payload):
    """Reduce GitHub repository metadata to a fixed non-secret schema."""
    if not isinstance(payload, dict):
        raise ValueError("invalid_github_response")
    result = {key: payload.get(key) for key in (
        "full_name", "default_branch", "private", "archived"
    )}
    if not isinstance(result["full_name"], str):
        raise ValueError("invalid_github_response")
    logger.info("readonly_github_summary")
    return result


def prometheus_summary(payload, max_series=20):
    """Bound returned series; do not export arbitrary label values."""
    if not isinstance(payload, dict) or payload.get("status") != "success":
        raise ValueError("invalid_prometheus_response")
    data = payload.get("data")
    if not isinstance(data, dict) or data.get("resultType") != "vector":
        raise ValueError("unsupported_prometheus_result")
    series = data.get("result")
    if not isinstance(series, list) or len(series) > max_series:
        raise ValueError("series_limit")
    values = []
    for item in series:
        if not isinstance(item, dict) or not isinstance(item.get("value"), list):
            raise ValueError("invalid_prometheus_series")
        sample = item["value"]
        if len(sample) != 2 or not isinstance(sample[1], str):
            raise ValueError("invalid_prometheus_sample")
        values.append(sample[1])
    logger.info("readonly_prometheus_summary series_count=%d", len(values))
    return {"series_count": len(values), "values": values}
