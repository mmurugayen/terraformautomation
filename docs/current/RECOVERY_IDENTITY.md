# Recovery receipt integrity

Reviewed 16 September 2026 against `d7d3b6b02465178c8fbcb11b07ae88839e4ef707`. This utility reuses the canonical adapter and transport/identity regression tests from [gysam-platform `774cb71a9e68`](https://github.com/mmurugayen/gysam-platform/commit/774cb71a9e6856249c2c5386331103c1b16ef2e4). The configuration and backend API paths are unchanged.

`recovery.apply` first fetches the requested plan. Its ID must exactly equal `plan_id`, its state must be recognized, and its target must be configured. An invalid identity/state returns `invalid_backend_response` before any POST. Only an approved plan is dispatched.

After dispatch, the returned plan must match the original plan ID and exact target and contain a recognized state. Otherwise the utility returns `backend_outcome_unknown`. It does not retry or infer success from HTTP 200 or a different plan's verified receipt. Recognized failed, uncertain, simulated and verification-required states remain explicit; only a matching `verified` state sets `verified: true`.

For an unknown outcome, inspect the original plan through the authorized backend and reconcile its durable action/verification evidence before considering another action. Retain the plan ID and target configuration; do not submit a replacement as an automatic retry. Unknown backend state text is not reflected to the client.

Run `python3 -m unittest discover -s tests -v` and `python3 scripts/check_observability_coverage.py`. The real HTTP regressions cover wrong/missing read IDs, mismatched/missing apply identities and targets, unrecognized states, and recognized terminal outcomes. CI now runs those regressions for every candidate.

[Local validation](../validation/recovery-identity-2026-09-16.json) is source evidence. Required self-hosted CI, configured backend credentials, installed authorization/recovery and deployment acceptance remain separate. GYS-OBS-001 retains its qualification-pending status. Roll back this source change through a reviewed revert if required; no infrastructure resources, state migrations, or application deployment are performed.
