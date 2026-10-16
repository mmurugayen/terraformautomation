# MCP governance implementation contract

This policy is shared conceptually by GYSAM Platform and domain-specific MCP adapters. This repository does not become an authorization authority.

## Capability manifest

Each exposed tool must declare:
- Stable tool identifier and schema version
- Read-only or mutating classification
- Explicit tenant, repository, cluster, namespace or target restrictions
- Credential scope and credential owner
- Maximum response size, timeout and output redaction policy
- Evidence/audit correlation identifier

## Mandatory decision flow

1. Authenticate caller using the host product identity boundary.
2. Resolve the concrete target against a static allowlist; never derive an unrestricted URL or filesystem path from tool arguments.
3. For reads, enforce role, tenant and target permissions before dispatch.
4. For writes, require an immutable proposal and a separate, authorized human approval bound to the proposal digest and target.
5. Reject expired, already-used, mismatched or absent approvals; fail closed.
6. Verify postconditions through independent readback, and record uncertainty instead of blindly retrying.
7. Record redacted audit metadata without secrets or raw tool output.

## Integration boundaries

- GYSAM Platform owns central identity, approval policy and audit.
- GYSAM HPC owns Slurm and cluster-specific operations.
- terraformautomation retains the existing diagnostics MCP and can host read-only adapters only after integration tests.
- Never grant an AI agent direct arbitrary shell, Terraform apply, Kubernetes exec or cloud administration privileges.

## Acceptance gates

- Negative tests for unauthorized and cross-tenant targets.
- Tests for stale approvals, duplicate execution and uncertain outcomes.
- Prompt-injection tests treating repository, logs and metrics as untrusted data.
- Bound response size, timeout, redirects, and credentials.
- Site-specific integration and recovery qualification before production.

This contract is not a deployment or production qualification claim.
