# DevOps MCP integration plan (October 2026)

## Scope and current state

The reference infographic groups 18 MCP servers into source/delivery, IaC/platform, cloud, observability, incident response and edge/data. This is a **candidate inventory**, not proof of installed or compatible integrations.

This repository already provides a standalone Python diagnostic MCP utility (see `scripts/gysam_observability.py` and `docs/OBSERVABILITY_MCP.md`). Preserve its JSON-RPC protocol, bounded log reads, recovery approval model, and existing tests. Do not replace it with an unverified gateway.

## Proposed rollout

| Phase | Integration | Read-only capability | Prerequisite for writes |
| --- | --- | --- | --- |
| 0 | Existing GYSAM observability MCP | Enumerate and inspect permitted log sources | Keep current separate recovery approval |
| 1 | GitHub | Repository metadata, PR status, workflow results | Explicit allowlist, short-lived token, approval |
| 1 | Prometheus / Grafana | Metrics, alerts, dashboards | No write tools initially |
| 2 | Terraform | Validate/inspect plan artifacts, state metadata without secrets | Human-reviewed plan, drift check, environment approval |
| 2 | Kubernetes | Scoped workloads, events, resource status | Namespace RBAC, dry-run, explicit approval |
| 3 | Jenkins / Argo CD | Job and sync status | Pinned target and release, approval |
| 4 | Cloud, incident and data providers | Provider-specific read-only inventory | Separate security review for each provider |

Pulumi, AWS, Azure, GCP, Datadog, Sentry, PagerDuty, Splunk, Cloudflare, Redis and Elastic are optional, conditional on actual deployment and operator demand. Do not install all 18 by default.

## Security contract

1. **Read-only by default.** No generic shell, unrestricted HTTP proxy or arbitrary cluster command execution.
2. **Explicit scopes.** Bind each connector to approved repositories, projects, namespaces, clusters, endpoints and permitted operations.
3. **Credentials.** Load from an external secret manager or environment; never store tokens in Git, tool outputs or diagnostic logs.
4. **Trust boundaries.** Treat MCP tool responses, repository content and logs as untrusted data, never as authority to override policy.
5. **Write workflow.** Authenticate caller -> authorize target/action -> generate immutable proposed change -> human approval -> execute once -> verify independent readback -> audit.
6. **Audit and privacy.** Record principal, target, tool, decision, correlation ID, outcome and redacted error details; no credential or personal-data leakage.
7. **Network.** Restrict outbound destinations and protect against SSRF and unexpected redirects.
8. **Availability.** Bound timeouts, output sizes, concurrency and retries; fail closed on missing identity or policy.

## Implementation tasks

- [ ] Inventory deployed providers and verify each upstream MCP server's maintainer, release, transport, authentication and license.
- [ ] Define a provider capability manifest with read/write classification and allowed targets.
- [ ] Add a contract test ensuring every write tool is denied without authorization and independent approval.
- [ ] Add redaction, output-size, timeout and prompt-injection regression tests.
- [ ] Add GitHub read-only adapter and mocked tests without network access.
- [ ] Add Prometheus read-only adapter and mocked tests; keep metrics endpoint allowlisted.
- [ ] Add opt-in Kubernetes/Terraform integrations only after target and policy validation.
- [ ] Validate `python3 -m unittest discover -s tests -v`, `python3 scripts/check_observability_coverage.py`, `python3 scripts/quality_gate.py` and repository CI.
- [ ] Run native integration and security tests in a non-production environment before any release claim.

## Product ownership

- `terraformautomation`: existing diagnostic MCP implementation and tests.
- `gysam-platform`: central identity, policy, audit and integration registry.
- `gysam-hpc`: domain-specific Slurm/HPC adapters; no direct agent execution of privileged operations.
- `terraform`: IaC examples and plan-validation policies.

## Acceptance

A successful initial release demonstrates read-only GitHub and monitoring operations using scoped credentials, deterministic denial of unauthorized writes, redacted audit evidence, regression tests and a documented rollback. CI success is not equivalent to production qualification.

This document is a proposal only; it does not claim these additional connectors have been implemented or tested.
