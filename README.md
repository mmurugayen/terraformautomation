# terraformautomation

Last source review: **2026-09-14**, default branch `dev`, commit [`fc5938592c34`](https://github.com/mmurugayen/terraformautomation/commit/fc5938592c347e09e6fbf684bcea3d7affd1d490). This records a documentation review of the linked source snapshot.

This repository contains a standalone Python diagnostic/MCP utility and repository test material. It does not currently define a deployable domain product or Terraform infrastructure. The diagnostic utility reads operator-configured logs; optional recovery uses a separately deployed, compatible HPC backend.

![Diagnostic utility architecture](docs/current/diagrams/observability-architecture.svg)

[Component architecture](docs/current/ARCHITECTURE.md) · [Investigation and recovery workflow](docs/current/WORKFLOWS.md) · [Documentation audit](docs/current/DOCUMENTATION_AUDIT.md)

## Run the diagnostic utility

Use Python 3.11 or later. Copy `config/observability-mcp.example.json` to a local configuration and supply explicit log paths. Run:

```bash
python3 scripts/gysam_observability.py --config /absolute/path/config.json
```

MCP stdout carries JSON-RPC; capture application diagnostics separately. Read [configuration, limits and optional recovery](docs/OBSERVABILITY_MCP.md) before configuring backend credentials or target aliases. Recovery is gated by the configured backend, registered runbooks and independent approval. There is no implicit application deployment, cloud provisioning or automatic repair.

## Check the source

```bash
python3 -m unittest discover -s tests -v
python3 scripts/check_observability_coverage.py
```

[Observability CI](.github/workflows/observability.yml) runs the utility contracts. [Feature acceptance](docs/product/backlog/GYS-OBS-001.md) tracks scope; [documentation validation](docs/current/VALIDATION.md) records checks actually run for this update.

Current guide maintenance: the [documentation audit](docs/current/DOCUMENTATION_AUDIT.md) records source revisions and historical-document status. Validate editable diagrams with `python3 docs/current/diagrams/render.py --check`.

[Recovery receipt integrity](docs/current/RECOVERY_IDENTITY.md) synchronizes the canonical plan/target/state checks and real HTTP regressions. Current CI and deployed-backend acceptance remain required.

[Diagnostic terminal events and sink recovery](docs/current/DIAGNOSTIC_TERMINAL_SINK.md) synchronizes the canonical helper, documents bounded stderr interruption accounting, and records local wrapper measurements. [Infrastructure ownership](docs/current/DIAGNOSTIC_TERMINAL_SINK.md#infrastructure-and-configuration-ownership) identifies the product-owned deployment paths.

The [bounded reader snapshot contract](docs/OBSERVABILITY_MCP.md#bounded-reader-snapshots) reports observed source changes and keeps malformed newline bursts within the checked allocation budget. Canonical Platform #47 merge and current consumer CI remain required.

[September 2026 source and CI audit](docs/validation/repository-audit-2026-09-19.md) records portable test results and outstanding qualification gates.

## Deployment and operations planning

[Nine shared deployment and operations requirements](docs/product/backlog/DEPLOYMENT_OPERATIONS_2026-09-17.md) and [blank deployment worksheets](docs/product/backlog/DEPLOYMENT_WORKSHEETS_2026-09-17.md) add 45 planned acceptance criteria tailored to this repository. These supplemental delivery/qualification refinements are not additional top-level product features. Existing IDs, counts, statuses and evidence are preserved; installed acceptance is **Not run** and go-live requires separate evidence and approval.
