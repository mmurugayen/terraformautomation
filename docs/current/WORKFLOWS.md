# terraformautomation: diagnostic workflow

Last source review: **2026-09-14**, default branch `dev`, commit [`fc5938592c34`](https://github.com/mmurugayen/terraformautomation/commit/fc5938592c347e09e6fbf684bcea3d7affd1d490). This records a documentation review of the linked source snapshot.

![Investigation and optional recovery order](diagrams/observability-workflow.svg)

Search configured logs by correlation identifier, inspect truncated/unavailable evidence, and investigate qualified fingerprints. An optional compatible HPC backend can retrieve verified resolution examples. A matching registered action must be proposed and independently approved before a single apply attempt. Unknown outcomes require reconciliation. Learning requires server-verified plan outcomes and a matching local failure; it does not grant execution authority or retry effects automatically.

[Architecture](ARCHITECTURE.md) · [Tool arguments and operational limits](../OBSERVABILITY_MCP.md)

Before dispatch, recovery validates the retrieved plan ID and recognized state. A successful HTTP apply response is accepted only when its plan ID and target exactly match the approved plan and its state is recognized. Malformed or mismatched apply receipts return `backend_outcome_unknown`; reconcile the original plan without automatic replay. See [recovery receipt integrity](RECOVERY_IDENTITY.md).

The optional shared Python diagnostic helper emits one timed terminal event per observed operation. Interrupted stderr writes are counted without storing payloads; a later successful write starts a complete JSON frame, reports a bounded unscoped recovery marker and then emits the current event. [Diagnostic terminal and recovery contract](DIAGNOSTIC_TERMINAL_SINK.md) documents installation, collection and validation limits.

During log investigation, `source_changed_during_read` marks observed file mutation or rotation and prevents a complete-window claim. Captured records remain partial evidence; a later stable configured-source query can recover. [Bounded reader contract](../OBSERVABILITY_MCP.md#bounded-reader-snapshots).
