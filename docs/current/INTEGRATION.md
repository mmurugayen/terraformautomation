# Documentation integration

Reconciled documentation PR #2 with `dev` commit [`6bccd25d259b`](https://github.com/mmurugayen/terraformautomation/commit/6bccd25d259b89453915c76d70c235eb96af3546) on 2026-09-14.

The original documentation revision is [`c3424ef2f190`](https://github.com/mmurugayen/terraformautomation/commit/c3424ef2f19003c302b1b5eb67503c0b2e3c9f3b). Its inventory and validation records describe that earlier snapshot and remain historical evidence.

## Preserved behavior

All runtime source, workflows, dependency pins and existing default-branch files outside documentation are retained byte-for-byte. README navigation includes the merged [diagnostics and MCP investigation](../OBSERVABILITY_MCP.md), [coverage inventory](../OBSERVABILITY_COVERAGE.json) and [feature backlog](../product/backlog/GYS-OBS-001.md). Diagnostics use fixed source configuration and existing authorization; documentation does not grant recovery or execution authority.

The README describes the current source rather than the earlier placeholder state. Original architecture diagrams remain scoped to the product components they depict; diagnostic setup is described by the linked guide.

## Validation scope

See [merge-reconciliation.json](merge-reconciliation.json) for source preservation and documentation checks. Original product acceptance records retain their dates. Local documentation checks do not substitute for current-head CI, installed clients, collector connectivity, matching server migrations or site-qualified recovery handlers. Review and normal merge controls remain required.
