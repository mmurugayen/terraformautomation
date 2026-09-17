# Diagnostic terminal events and sink recovery

Reviewed 17 September 2026. This increment follows recovery-receipt candidate `7fa5c6b2b44754ffe93358a0a36108d8faa7bcb7` and copies the helper and focused regressions verbatim from [canonical Platform `774cb71a9e68`](https://github.com/mmurugayen/gysam-platform/commit/774cb71a9e6856249c2c5386331103c1b16ef2e4). It retains existing configuration and product boundaries.

## Operation and logging contract

An observed synchronous or asynchronous call produces one timed terminal event: returned `{"ok": false}` and ordinary exceptions produce `operation.failed`; cancellation or another `BaseException` propagates with an interrupted outcome; successful completion remains DEBUG unless it reaches the existing one-second warning threshold. Context tokens restore the calling scope and keep concurrent tasks isolated. Arguments, return payloads and exception text are excluded.

All built-in helper loggers share one stderr handler and lock. A write succeeds only when its return value is an exact integer matching the complete character count and flush succeeds. Failed or ambiguous writes increment a saturating JSON-safe counter, without retaining payloads or scope IDs. On the next successful attempt, a leading newline restores framing, then one `diagnostic.sink.recovered` marker reports interrupted attempts before the current event. This is not a count of proven lost records. There is no event replay and logging failure does not replace an operation's result or exception.

The helper remains optional library code. The standalone MCP adapter retains JSON-RPC stdout and its current dispatch behavior; this change does not auto-instrument it or deploy a collector. `GYSAM_LOG_LEVEL` retains its default INFO threshold and valid level behavior. `GYSAM_REVISION`/`GITHUB_SHA` retain the existing exact 40-hex revision filter. No new configuration is required.

## Operator verification

Run `python3 -m unittest discover -s tests -v` and `python3 scripts/check_observability_coverage.py`. Tests cover short/non-integer writes, ambiguous flushes, bounded recovery, cross-service serialization, returned failures, exceptions, cancellation and context restoration. CI executes all those regressions.

When a recovery marker appears, investigate stderr/collector availability and reconcile the affected interval using the operation's authoritative state. Do not infer action success or replay operations from diagnostic gaps. This helper only bounds its own counter and stores no retry queue; installed retention, sustained throughput and collector backpressure remain deployment acceptance checks.

[Validation evidence](../validation/diagnostic-terminal-sink-2026-09-17.json) records the exact source hashes. [Local wrapper measurements](../validation/operation-spans-2026-09-17.json) compare seven alternating batches of 20,000 INFO-filtered no-op calls against the previous identical helper: median per-call time changed by -42.7% synchronously and -41.51% asynchronously. These measurements exclude sink I/O and application work; batch percentiles are not request-latency percentiles or deployment performance acceptance.

## Infrastructure and configuration ownership

This repository contains no Terraform resources or Ansible application deployment. The helper change does not change these existing product-owned responsibilities:

| Product | Infrastructure owner | Configuration owner |
| --- | --- | --- |
| GYSAM | [deploy/terraform](https://github.com/mmurugayen/gysam/tree/main/deploy/terraform) | [deploy/ansible](https://github.com/mmurugayen/gysam/tree/main/deploy/ansible) |
| GYSAM-HPC | [deployment/terraform](https://github.com/mmurugayen/gysam-hpc/tree/main/deployment/terraform) | [deployment/ansible](https://github.com/mmurugayen/gysam-hpc/tree/main/deployment/ansible) |
| GYSAM-REMOTE | [infra/terraform](https://github.com/mmurugayen/gysam-remote/tree/main/infra/terraform) | [infra/ansible](https://github.com/mmurugayen/gysam-remote/tree/main/infra/ansible) |

Those product deployment owners retain installation, permissions, journald/rotation, credentials and configured collectors. Shared source promotion does not advance their deployment acceptance or dependency pins. A reviewed revert restores the prior helper; no database or infrastructure state migration is introduced. Required candidate CI and independent installed qualification remain open.
