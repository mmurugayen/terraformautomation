# Phase 1: read-only GitHub and Prometheus adapters

This branch scopes two independent adapters for the existing diagnostic MCP transport. No production endpoints are configured.

## GitHub

- Allowlist repository names.
- Expose only repository metadata, pull-request status and workflow-run status.
- Use a short-lived, read-only token supplied externally.
- Reject all writes, unlisted repositories and redirects.

## Prometheus

- Allowlist HTTPS origins and named, fixed PromQL queries.
- Do not permit arbitrary user-supplied PromQL or endpoint paths.
- Bound request duration, response size and returned series.
- Do not expose sensitive label values without filtering.

## Verification gates

- Mock successful reads and denied targets.
- Mock timeouts, redirects, oversized payloads and credential failures.
- Run existing observability unit tests and quality gate.
- Verify actual MCP client integration in a nonproduction environment.

This is a design contract, not a claim of implemented or tested adapters.
