# terraformautomation: deployment worksheets

Template date: 2026-09-17. Every TBD field is unfilled; evidence/signoff cells are intentionally blank. Use secret references only, never secret values.

[Backlog](DEPLOYMENT_OPERATIONS_2026-09-17.md) · [Machine-readable criteria](deployment-operations-2026-09-17.json)

This repository implements diagnostic utilities and a scaffold for future infrastructure contracts. No Terraform resources, Ansible deployment or product runtime exists here. Package/module ownership and consumer qualification are documentation responsibilities, not additive product feature counts.

Default decision: **NO-GO**. A justified not-applicable item is not a passed native trial. Missing, failed, stale evidence or blank approval prevents go-live.

## Site, scope and readiness

Related requirement: GYS-DEPLOY-01. Document the diagnostic package and consumer interfaces, host prerequisites and ownership. This repository has no Terraform resource/module catalog or product installer.

| Field | Value | Evidence reference | Reviewer/signoff |
|---|---|---|---|
| Product / site identifier | TBD | | |
| Environment and intended roles | TBD | | |
| Source/configuration revision | TBD | | |
| Supported OS/hardware and capacity | TBD | | |
| Control/data/dependency topology | TBD | | |
| Proposed owner / assigned owner | TBD | | |
| Prerequisite result / evidence | TBD | | |
| Change window / unresolved decisions | TBD | | |

## Network and IP allocation

Related requirement: GYS-DEPLOY-02. Document fixed local log sources and optional backend networking, approved aliases, TLS/DNS/time and redaction; IP allocation belongs to the consuming infrastructure owner.

| Field | Value | Evidence reference | Reviewer/signoff |
|---|---|---|---|
| Role / hostname | TBD | | |
| Interface / purpose | TBD | | |
| Address family / address / prefix | TBD | | |
| Subnet / VLAN / gateway | TBD | | |
| DNS / time sources | TBD | | |
| Static, reservation or pool reference | TBD | | |
| Virtual endpoint / failover owner | TBD | | |
| Port/firewall/route/MTU validation | TBD | | |
| IPAM reviewer / overlap result / evidence | TBD | | |

## Head/control/management installation

Related requirement: GYS-DEPLOY-03. Native head-node installation is not applicable. Qualify the utility package/configuration on an existing host and identify external bootstrap ownership separately.

| Field | Value | Evidence reference | Reviewer/signoff |
|---|---|---|---|
| Role and applicability | TBD | | |
| Host/device inventory reference | TBD | | |
| Firmware/OS/boot/storage profile | TBD | | |
| Verified source/package digest | TBD | | |
| Secret reference only | TBD | | |
| Terraform/OpenTofu/infrastructure mapping | TBD | | |
| Ansible/configuration mapping | TBD | | |
| Clean install / rerun / recovery evidence | TBD | | |
| Operator approval / rollback reference |  | | |

## Availability and failure recovery

Related requirement: GYS-DEPLOY-04. Native HA ownership is not applicable to this utility. Record process availability and bounded evidence; optional backend HA belongs to its external owner.

| Field | Value | Evidence reference | Reviewer/signoff |
|---|---|---|---|
| Supported topology / limitation | TBD | | |
| Stateful dependencies / owner | TBD | | |
| Leadership/quorum / fencing design | TBD | | |
| Endpoint movement / consistency | TBD | | |
| Target RTO / target RPO | TBD | | |
| Observed RTO / observed RPO | TBD | | |
| Failover / partition / failback evidence | TBD | | |
| Active-work safety / unresolved defects | TBD | | |

## Images, packages and provisioning

Related requirement: GYS-DEPLOY-05. Qualify diagnostic package identity and configuration delivery only. No compute images, disk provisioning or Terraform apply exist here; assign a consumer module owner first.

| Field | Value | Evidence reference | Reviewer/signoff |
|---|---|---|---|
| Role / image or package version | TBD | | |
| OS/architecture/kernel/driver profile | TBD | | |
| Integrity/provenance / license reference | TBD | | |
| Identity injection / secret reference | TBD | | |
| Provisioning method / device selection | TBD | | |
| Canary / batch and drain policy | TBD | | |
| Interrupt/resume / rollback evidence | TBD | | |
| Installed identity / drift / retirement | TBD | | |

## Scheduler and Slurm applicability

Related requirement: GYS-DEPLOY-06. Native Slurm is not applicable to diagnostic tooling. A selected external integration may supply bounded observations but confers no scheduler administration.

| Field | Value | Evidence reference | Reviewer/signoff |
|---|---|---|---|
| Native scheduler owner | TBD | | |
| Native Slurm / selected adapter / not applicable with reason | TBD | | |
| Scheduler/configuration identity | TBD | | |
| Partitions / resources / account-policy profile | TBD | | |
| Authentication / current health | TBD | | |
| CPU/GPU/job/accounting evidence | TBD | | |
| Denied requests / drain/recovery evidence | TBD | | |
| Load/soak budget and evidence | TBD | | |

## Security hardening

Related requirement: GYS-DEPLOY-07. Qualify fixed-source access, bounded JSON/MCP, secret references, backend authorization and redaction within the existing GYS-OBS-001 boundary.

| Field | Value | Evidence reference | Reviewer/signoff |
|---|---|---|---|
| Threat/trust-boundary review | TBD | | |
| Hardening profile revision | TBD | | |
| Service/admin identity / scope | TBD | | |
| Network exposure / TLS/key lifecycle | TBD | | |
| Update/provenance/security checks | TBD | | |
| Denied access / revocation / redaction evidence | TBD | | |
| Exception owner / expiry / approval |  | | |

## Backup, upgrade and troubleshooting

Related requirement: GYS-DEPLOY-08. Restore utility configuration and retained evidence per operator policy; backend recovery requires separately approved plans and verified receipts without blind replay.

| Field | Value | Evidence reference | Reviewer/signoff |
|---|---|---|---|
| Authoritative state / retention / access owner | TBD | | |
| Backup artifact identity / integrity result | TBD | | |
| Isolated restore evidence | TBD | | |
| Upgrade compatibility / migration evidence | TBD | | |
| Interrupt/resume / rollback evidence | TBD | | |
| Troubleshooting / redaction / escalation reference | TBD | | |
| Recovery objectives / measured results | TBD | | |
| Unresolved incident or defect references | TBD | | |

## Go-live and handover

Related requirement: GYS-DEPLOY-09. Provide package/module-interface handoff with consumer owner, source/configuration identity and N/A reasons; infrastructure deliverables are not new product features.

| Field | Value | Evidence reference | Reviewer/signoff |
|---|---|---|---|
| Required checks complete at reviewed revision | TBD | | |
| Native/site/installed evidence complete | TBD | | |
| Performance / capacity / soak accepted | TBD | | |
| Security exceptions approved | TBD | | |
| Restore / rollback rehearsed | TBD | | |
| Operator readiness / maintenance window | TBD | | |
| Release owner approval / date |  | | |
| Site owner approval / date |  | | |
| Decision: NO-GO until required evidence and approvals complete |  | | |
| Observation window / rollback triggers | TBD | | |
| Handover owner / remaining backlog | TBD | | |

## Acceptance and decision register

| Criterion | Applicability / reason | Owner | Source / configuration / environment | Result | Evidence reference | Reviewer / signoff |
|---|---|---|---|---|---|---|
| GYS-DEPLOY-01-AC1 | TBD | TBD | TBD | Not run | | |
| GYS-DEPLOY-01-AC2 | TBD | TBD | TBD | Not run | | |
| GYS-DEPLOY-01-AC3 | TBD | TBD | TBD | Not run | | |
| GYS-DEPLOY-01-AC4 | TBD | TBD | TBD | Not run | | |
| GYS-DEPLOY-01-AC5 | TBD | TBD | TBD | Not run | | |
| GYS-DEPLOY-02-AC1 | TBD | TBD | TBD | Not run | | |
| GYS-DEPLOY-02-AC2 | TBD | TBD | TBD | Not run | | |
| GYS-DEPLOY-02-AC3 | TBD | TBD | TBD | Not run | | |
| GYS-DEPLOY-02-AC4 | TBD | TBD | TBD | Not run | | |
| GYS-DEPLOY-02-AC5 | TBD | TBD | TBD | Not run | | |
| GYS-DEPLOY-03-AC1 | TBD | TBD | TBD | Not run | | |
| GYS-DEPLOY-03-AC2 | TBD | TBD | TBD | Not run | | |
| GYS-DEPLOY-03-AC3 | TBD | TBD | TBD | Not run | | |
| GYS-DEPLOY-03-AC4 | TBD | TBD | TBD | Not run | | |
| GYS-DEPLOY-03-AC5 | TBD | TBD | TBD | Not run | | |
| GYS-DEPLOY-04-AC1 | TBD | TBD | TBD | Not run | | |
| GYS-DEPLOY-04-AC2 | TBD | TBD | TBD | Not run | | |
| GYS-DEPLOY-04-AC3 | TBD | TBD | TBD | Not run | | |
| GYS-DEPLOY-04-AC4 | TBD | TBD | TBD | Not run | | |
| GYS-DEPLOY-04-AC5 | TBD | TBD | TBD | Not run | | |
| GYS-DEPLOY-05-AC1 | TBD | TBD | TBD | Not run | | |
| GYS-DEPLOY-05-AC2 | TBD | TBD | TBD | Not run | | |
| GYS-DEPLOY-05-AC3 | TBD | TBD | TBD | Not run | | |
| GYS-DEPLOY-05-AC4 | TBD | TBD | TBD | Not run | | |
| GYS-DEPLOY-05-AC5 | TBD | TBD | TBD | Not run | | |
| GYS-DEPLOY-06-AC1 | TBD | TBD | TBD | Not run | | |
| GYS-DEPLOY-06-AC2 | TBD | TBD | TBD | Not run | | |
| GYS-DEPLOY-06-AC3 | TBD | TBD | TBD | Not run | | |
| GYS-DEPLOY-06-AC4 | TBD | TBD | TBD | Not run | | |
| GYS-DEPLOY-06-AC5 | TBD | TBD | TBD | Not run | | |
| GYS-DEPLOY-07-AC1 | TBD | TBD | TBD | Not run | | |
| GYS-DEPLOY-07-AC2 | TBD | TBD | TBD | Not run | | |
| GYS-DEPLOY-07-AC3 | TBD | TBD | TBD | Not run | | |
| GYS-DEPLOY-07-AC4 | TBD | TBD | TBD | Not run | | |
| GYS-DEPLOY-07-AC5 | TBD | TBD | TBD | Not run | | |
| GYS-DEPLOY-08-AC1 | TBD | TBD | TBD | Not run | | |
| GYS-DEPLOY-08-AC2 | TBD | TBD | TBD | Not run | | |
| GYS-DEPLOY-08-AC3 | TBD | TBD | TBD | Not run | | |
| GYS-DEPLOY-08-AC4 | TBD | TBD | TBD | Not run | | |
| GYS-DEPLOY-08-AC5 | TBD | TBD | TBD | Not run | | |
| GYS-DEPLOY-09-AC1 | TBD | TBD | TBD | Not run | | |
| GYS-DEPLOY-09-AC2 | TBD | TBD | TBD | Not run | | |
| GYS-DEPLOY-09-AC3 | TBD | TBD | TBD | Not run | | |
| GYS-DEPLOY-09-AC4 | TBD | TBD | TBD | Not run | | |
| GYS-DEPLOY-09-AC5 | TBD | TBD | TBD | Not run | | |

## Go/no-go rules

Each applicable criterion requires assigned ownership and revision/environment-bound evidence. Review required CI, installed/native trials, capacity/performance, hardening exceptions, isolated restore, rollback and operator readiness. Documentation merge, mocks and N/A decisions do not establish site acceptance.

| Decision item | Value | Evidence | Accountable approval |
|---|---|---|---|
| Release/site decision | NO-GO | | |
| Maintenance and rollback window | TBD | | |
| Communication / escalation owner | TBD | | |
| Post-deployment observation and rollback triggers | TBD | | |
| Handover owner and unresolved backlog | TBD | | |
