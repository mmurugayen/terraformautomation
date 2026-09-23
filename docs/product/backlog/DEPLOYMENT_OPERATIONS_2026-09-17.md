# terraformautomation: deployment and operations backlog

Requested: 2026-09-17. Source reviewed: dev at d7d3b6b02465178c8fbcb11b07ae88839e4ef707.

Status: **Planned**. Acceptance: **Not run**. Assignees: **Unassigned**. Proposed owner roles require assignment.

Nine shared requirements projected by product. Product projections are not additive top-level features. Preserve all existing feature counts, IDs, states and evidence.

This repository implements diagnostic utilities and a scaffold for future infrastructure contracts. No Terraform resources, Ansible deployment or product runtime exists here. Package/module ownership and consumer qualification are documentation responsibilities, not additive product feature counts.

Diagnostic package/interface only. Assign consuming Terraform/OpenTofu module and Ansible/configuration owners before execution; no such deployment runtime exists here.

[Machine-readable backlog](deployment-operations-2026-09-17.json) · [Blank worksheets](DEPLOYMENT_WORKSHEETS_2026-09-17.md)

This documentation does not authorize deployment, privileged installation, disk erasure or automated remediation. Existing acceptance, IDs, counts and historical evidence remain unchanged.

## Requirement index

| ID | Topic | Priority | Dependencies |
|---|---|---|---|
| GYS-DEPLOY-01 | Architecture and readiness planning | P0 | None |
| GYS-DEPLOY-02 | Network design and IP allocation | P0 | GYS-DEPLOY-01 |
| GYS-DEPLOY-03 | Head-node installation | P0 | GYS-DEPLOY-01, GYS-DEPLOY-02 |
| GYS-DEPLOY-04 | High availability | P1 | GYS-DEPLOY-01, GYS-DEPLOY-02, GYS-DEPLOY-03 |
| GYS-DEPLOY-05 | Software images and compute-node provisioning | P1 | GYS-DEPLOY-01, GYS-DEPLOY-02, GYS-DEPLOY-03, GYS-DEPLOY-07 |
| GYS-DEPLOY-06 | Slurm validation | P1 | GYS-DEPLOY-01, GYS-DEPLOY-02, GYS-DEPLOY-03, GYS-DEPLOY-05, GYS-DEPLOY-07 |
| GYS-DEPLOY-07 | Security hardening | P0 | GYS-DEPLOY-01, GYS-DEPLOY-02 |
| GYS-DEPLOY-08 | Backup, upgrades, recovery, and troubleshooting | P0 | GYS-DEPLOY-01, GYS-DEPLOY-03, GYS-DEPLOY-07 |
| GYS-DEPLOY-09 | Deployment worksheets and go-live checklists | P0 | GYS-DEPLOY-01, GYS-DEPLOY-02, GYS-DEPLOY-03, GYS-DEPLOY-04, GYS-DEPLOY-05, GYS-DEPLOY-06, GYS-DEPLOY-07, GYS-DEPLOY-08 |

## GYS-DEPLOY-01 — Architecture and readiness planning

Priority: P0. Proposed owner: Product and deployment architecture owner; assignee Unassigned. Status Planned; acceptance Not run.

Product scope: Document the diagnostic package and consumer interfaces, host prerequisites and ownership. This repository has no Terraform resource/module catalog or product installer.

Applicability: Adapted to existing product role. Document the diagnostic package and consumer interfaces, host prerequisites and ownership. This repository has no Terraform resource/module catalog or product installer.

Existing local parent IDs: None for this area. No local product catalog covers this area. Use existing source/document contracts below and assign consuming package/module ownership before implementation; no parent ID is invented.

Source contracts: [README.md](../../../README.md) · [docs/current/ARCHITECTURE.md](../../current/ARCHITECTURE.md) · [docs/OBSERVABILITY_MCP.md](../../OBSERVABILITY_MCP.md)

Dependencies: None. Worksheet: Site, scope and readiness.

- **GYS-DEPLOY-01-AC1** — Record the intended topology, role boundaries, supported operating systems and hardware, storage/data ownership, environment limits and product-specific exclusions in a versioned architecture worksheet. **Status: Not run.**
- **GYS-DEPLOY-01-AC2** — Record measurable capacity, latency, throughput, concurrency and resource budgets plus workload assumptions before tuning or acceptance; retain baseline evidence and avoid invented measurements. **Status: Not run.**
- **GYS-DEPLOY-01-AC3** — Validate prerequisite identity, DNS/time synchronization, storage capacity, network access, package/driver rights, dependencies and operator authority; fail readiness for missing or inconsistent inputs. **Status: Not run.**
- **GYS-DEPLOY-01-AC4** — Map each installation and operational capability to its existing backlog parent, Terraform/OpenTofu or infrastructure contract, Ansible or configuration contract, and required source/native/site evidence. **Status: Not run.**
- **GYS-DEPLOY-01-AC5** — Record proposed delivery/operations owners, unresolved decisions, dependency order, change window and explicit review gates; a missing approval or failed prerequisite keeps readiness blocked. **Status: Not run.**

Planned documentation/qualification work. Source revision, installed target, reviewer and measured evidence must be recorded; acceptance remains Not run.

## GYS-DEPLOY-02 — Network design and IP allocation

Priority: P0. Proposed owner: Network and infrastructure owner; assignee Unassigned. Status Planned; acceptance Not run.

Product scope: Document fixed local log sources and optional backend networking, approved aliases, TLS/DNS/time and redaction; IP allocation belongs to the consuming infrastructure owner.

Applicability: Adapted to existing product role. Document fixed local log sources and optional backend networking, approved aliases, TLS/DNS/time and redaction; IP allocation belongs to the consuming infrastructure owner.

Existing local parent IDs: None for this area. No local product catalog covers this area. Use existing source/document contracts below and assign consuming package/module ownership before implementation; no parent ID is invented.

Source contracts: [README.md](../../../README.md) · [docs/current/ARCHITECTURE.md](../../current/ARCHITECTURE.md) · [docs/OBSERVABILITY_MCP.md](../../OBSERVABILITY_MCP.md)

Dependencies: GYS-DEPLOY-01. Worksheet: Network and IP allocation.

- **GYS-DEPLOY-02-AC1** — Complete an IPAM worksheet for each applicable interface or virtual endpoint with role, hostname, address family/prefix, subnet, gateway, VLAN, DNS, reservation method and owner; reserve virtual and provisioning addresses separately. **Status: Not run.**
- **GYS-DEPLOY-02-AC2** — Validate address/prefix syntax, subnet and pool overlap, duplicate addresses, static/DHCP exclusions, routing and capacity; use actual site allocations only after operator review. **Status: Not run.**
- **GYS-DEPLOY-02-AC3** — Define required inbound/outbound ports, trust zones, administrative access, routing, DNS and time dependencies; deny unrelated traffic and keep out-of-band management isolated where present. **Status: Not run.**
- **GYS-DEPLOY-02-AC4** — Validate connectivity, name resolution, configured MTU and relevant throughput/latency between each required role, including failure and rollback behavior, without exposing private endpoint values in diagnostic evidence. **Status: Not run.**
- **GYS-DEPLOY-02-AC5** — Version and review address changes, VIP moves and firewall/routing updates; prove conflict detection and rollback before any live allocation, and record unsupported address families explicitly. **Status: Not run.**

Planned documentation/qualification work. Source revision, installed target, reviewer and measured evidence must be recorded; acceptance remains Not run.

## GYS-DEPLOY-03 — Head-node installation

Priority: P0. Proposed owner: Product installation owner; assignee Unassigned. Status Planned; acceptance Not run.

Product scope: Native head-node installation is not applicable. Qualify the utility package/configuration on an existing host and identify external bootstrap ownership separately.

Applicability: Adapted to existing product role. Native head-node installation is not applicable. Qualify the utility package/configuration on an existing host and identify external bootstrap ownership separately.

Existing local parent IDs: None for this area. No local product catalog covers this area. Use existing source/document contracts below and assign consuming package/module ownership before implementation; no parent ID is invented.

Source contracts: [README.md](../../../README.md) · [docs/current/ARCHITECTURE.md](../../current/ARCHITECTURE.md) · [docs/OBSERVABILITY_MCP.md](../../OBSERVABILITY_MCP.md)

Dependencies: GYS-DEPLOY-01, GYS-DEPLOY-02. Worksheet: Head/control/management installation.

- **GYS-DEPLOY-03-AC1** — Record the existing role (Local stdio/MCP utility and explicitly configured external backend; consuming infrastructure/product ownership must be assigned.) and mark native HPC head-node installation not applicable; document supported OS/firmware/storage and recovery prerequisites for the selected role. **Status: Not run.**
- **GYS-DEPLOY-03-AC2** — Verify immutable installation/source/package identities and compatibility before execution, keep credentials out of images and logs, and obtain role-specific authority before destructive or privileged steps. **Status: Not run.**
- **GYS-DEPLOY-03-AC3** — Qualify repeatable bootstrap of required identity, time, storage, database, service configuration, access controls and bounded diagnostics using the existing infrastructure/configuration ownership. **Status: Not run.**
- **GYS-DEPLOY-03-AC4** — Exercise a clean install, idempotent rerun, interrupted/resumed install and failed prerequisite on a supported target; preserve prior working state and produce bounded evidence of the failed stage. **Status: Not run.**
- **GYS-DEPLOY-03-AC5** — Verify service health and authorized administrative access after installation, then record source/configuration identity, operator handoff and tested rollback; source-only installation tests cannot mark installed readiness complete. **Status: Not run.**

Planned documentation/qualification work. Source revision, installed target, reviewer and measured evidence must be recorded; acceptance remains Not run.

## GYS-DEPLOY-04 — High availability

Priority: P1. Proposed owner: Availability and data owner; assignee Unassigned. Status Planned; acceptance Not run.

Product scope: Native HA ownership is not applicable to this utility. Record process availability and bounded evidence; optional backend HA belongs to its external owner.

Applicability: Adapted to existing product role. Native HA ownership is not applicable to this utility. Record process availability and bounded evidence; optional backend HA belongs to its external owner.

Existing local parent IDs: None for this area. No local product catalog covers this area. Use existing source/document contracts below and assign consuming package/module ownership before implementation; no parent ID is invented.

Source contracts: [README.md](../../../README.md) · [docs/current/ARCHITECTURE.md](../../current/ARCHITECTURE.md) · [docs/OBSERVABILITY_MCP.md](../../OBSERVABILITY_MCP.md)

Dependencies: GYS-DEPLOY-01, GYS-DEPLOY-02, GYS-DEPLOY-03. Worksheet: Availability and failure recovery.

- **GYS-DEPLOY-04-AC1** — Declare supported single-instance, active/passive or active/active topology and each stateful dependency; where HA is unsupported, record the limitation and operator-approved recovery approach. **Status: Not run.**
- **GYS-DEPLOY-04-AC2** — Only for a separately approved HA design, specify leadership/quorum, fencing or equivalent ownership exclusion, endpoint movement and data consistency. Otherwise record why these mechanisms are not applicable to the selected topology; no HA pass is implied. **Status: Not run.**
- **GYS-DEPLOY-04-AC3** — Set reviewed RTO, RPO and workload/session safety requirements before trials; define how progress, jobs, commands and durable state survive a role or dependency failure. **Status: Not run.**
- **GYS-DEPLOY-04-AC4** — For the supported single-host/package topology, inject process and host/dependency outages and measure isolated restoration and state/permission outcomes against predeclared objectives; do not label restoration as HA failover. **Status: Not run.**
- **GYS-DEPLOY-04-AC5** — Exercise return to the last qualified single-host/package configuration and verify ownership and unresolved incidents. Record native HA as not applicable with its reason; future HA requires a separately approved design and trials. **Status: Not run.**

Planned documentation/qualification work. Source revision, installed target, reviewer and measured evidence must be recorded; acceptance remains Not run.

## GYS-DEPLOY-05 — Software images and compute-node provisioning

Priority: P1. Proposed owner: Image and provisioning owner; assignee Unassigned. Status Planned; acceptance Not run.

Product scope: Qualify diagnostic package identity and configuration delivery only. No compute images, disk provisioning or Terraform apply exist here; assign a consumer module owner first.

Applicability: Adapted to existing product role. Qualify diagnostic package identity and configuration delivery only. No compute images, disk provisioning or Terraform apply exist here; assign a consumer module owner first.

Existing local parent IDs: None for this area. No local product catalog covers this area. Use existing source/document contracts below and assign consuming package/module ownership before implementation; no parent ID is invented.

Source contracts: [README.md](../../../README.md) · [docs/current/ARCHITECTURE.md](../../current/ARCHITECTURE.md) · [docs/OBSERVABILITY_MCP.md](../../OBSERVABILITY_MCP.md)

Dependencies: GYS-DEPLOY-01, GYS-DEPLOY-02, GYS-DEPLOY-03, GYS-DEPLOY-07. Worksheet: Images, packages and provisioning.

- **GYS-DEPLOY-05-AC1** — Define versioned image or package profiles with OS/architecture, kernel, drivers, dependencies, hardware requirements, source digests and approved license/redistribution constraints for the applicable product role. **Status: Not run.**
- **GYS-DEPLOY-05-AC2** — Verify provenance and integrity before provisioning, inject unique node/device identity and secret references at deployment time, and reject altered artifacts or images containing reusable credentials. **Status: Not run.**
- **GYS-DEPLOY-05-AC3** — Qualify the selected provisioning mechanism and address/inventory mapping on a canary target; validate disk/device selection and require explicit approval for destructive operations. **Status: Not run.**
- **GYS-DEPLOY-05-AC4** — Exercise repeatable provisioning, bounded batches, partial failure, resume and rollback while preserving existing workloads and prior qualified images; require drain/maintenance where the local role owns active work. **Status: Not run.**
- **GYS-DEPLOY-05-AC5** — Record per-node/device or package deployment identity, observed health, drift and retirement state, and prove compatibility of the installed artifact with the applicable control service before wider rollout. **Status: Not run.**

Planned documentation/qualification work. Source revision, installed target, reviewer and measured evidence must be recorded; acceptance remains Not run.

## GYS-DEPLOY-06 — Slurm validation

Priority: P1. Proposed owner: HPC scheduler owner or selected integration owner; assignee Unassigned. Status Planned; acceptance Not run.

Product scope: Native Slurm is not applicable to diagnostic tooling. A selected external integration may supply bounded observations but confers no scheduler administration.

Applicability: Native Slurm not applicable. Native Slurm is not applicable to diagnostic tooling. A selected external integration may supply bounded observations but confers no scheduler administration.

Existing local parent IDs: None for this area. No local product catalog covers this area. Use existing source/document contracts below and assign consuming package/module ownership before implementation; no parent ID is invented.

Source contracts: [README.md](../../../README.md) · [docs/current/ARCHITECTURE.md](../../current/ARCHITECTURE.md) · [docs/OBSERVABILITY_MCP.md](../../OBSERVABILITY_MCP.md)

Dependencies: GYS-DEPLOY-01, GYS-DEPLOY-02, GYS-DEPLOY-03, GYS-DEPLOY-05, GYS-DEPLOY-07. Worksheet: Scheduler and Slurm applicability.

- **GYS-DEPLOY-06-AC1** — Record native Slurm administration as not applicable to this product, with the product-specific reason and current execution authority. External Slurm integration is opt-in and requires an approved design before adding an adapter. **Status: Not run.**
- **GYS-DEPLOY-06-AC2** — If an external Slurm integration is explicitly selected and approved: For applicable native or integration targets, verify exact scheduler/configuration identity, authentication, node/partition visibility, accounting dependencies and current health; stale or simulated observations cannot satisfy native readiness. Otherwise retain a justified not-applicable disposition; do not report native scheduler trials as passed. **Status: Not run.**
- **GYS-DEPLOY-06-AC3** — If an external Slurm integration is explicitly selected and approved: Exercise authorized CPU and, where supported, GPU/GRES job submission, resource/account/QoS limits, isolation, accounting and completion on the actual target; record unsupported cases explicitly. Otherwise retain a justified not-applicable disposition; do not report native scheduler trials as passed. **Status: Not run.**
- **GYS-DEPLOY-06-AC4** — If an external Slurm integration is explicitly selected and approved: Exercise unauthorized requests, node drain/rejoin, controller or adapter interruption, timeout/cancellation and recovery while preserving active jobs, ownership and bounded diagnostics. Otherwise retain a justified not-applicable disposition; do not report native scheduler trials as passed. **Status: Not run.**
- **GYS-DEPLOY-06-AC5** — If an external Slurm integration is explicitly selected and approved: Measure applicable submission/status/accounting latency and load/soak behavior against predeclared budgets, retain revision/environment-bound evidence, and leave native acceptance open until those trials pass. Otherwise retain a justified not-applicable disposition; do not report native scheduler trials as passed. **Status: Not run.**

Planned documentation/qualification work. Source revision, installed target, reviewer and measured evidence must be recorded; acceptance remains Not run.

## GYS-DEPLOY-07 — Security hardening

Priority: P0. Proposed owner: Product security and operations owner; assignee Unassigned. Status Planned; acceptance Not run.

Product scope: Qualify fixed-source access, bounded JSON/MCP, secret references, backend authorization and redaction within the existing GYS-OBS-001 boundary.

Applicability: Adapted to existing product role. Qualify fixed-source access, bounded JSON/MCP, secret references, backend authorization and redaction within the existing GYS-OBS-001 boundary.

Existing local parent IDs: GYS-OBS-001. Existing local tasks remain authoritative; this projection refines qualification without changing their acceptance.

Source contracts: [README.md](../../../README.md) · [docs/current/ARCHITECTURE.md](../../current/ARCHITECTURE.md) · [docs/OBSERVABILITY_MCP.md](../../OBSERVABILITY_MCP.md)

Dependencies: GYS-DEPLOY-01, GYS-DEPLOY-02. Worksheet: Security hardening.

- **GYS-DEPLOY-07-AC1** — Document a threat and trust-boundary review for installation, administration, application traffic, stored data, agents/workers and dependencies; map findings to existing security requirements and assigned remediation roles. **Status: Not run.**
- **GYS-DEPLOY-07-AC2** — Qualify least-privilege service identities, administrative authentication, role/tenant or device scope, secure remote access, certificate/key lifecycle and secret-reference handling on the supported installation. **Status: Not run.**
- **GYS-DEPLOY-07-AC3** — Apply reviewed host/service hardening and minimal network exposure using existing configuration ownership; verify updates, dependency provenance and relevant vulnerability/secret checks without disabling required protections. **Status: Not run.**
- **GYS-DEPLOY-07-AC4** — Exercise denied access, revoked credentials/certificates, unauthorized configuration, malformed inputs and private-data redaction; diagnostics must remain bounded and must not contain secrets or customer payloads. **Status: Not run.**
- **GYS-DEPLOY-07-AC5** — Record hardening profile identity, evidence, residual exceptions, accountable approval and remediation expiry; failed checks or unapproved exceptions block go-live. **Status: Not run.**

Planned documentation/qualification work. Source revision, installed target, reviewer and measured evidence must be recorded; acceptance remains Not run.

## GYS-DEPLOY-08 — Backup, upgrades, recovery, and troubleshooting

Priority: P0. Proposed owner: Operations and recovery owner; assignee Unassigned. Status Planned; acceptance Not run.

Product scope: Restore utility configuration and retained evidence per operator policy; backend recovery requires separately approved plans and verified receipts without blind replay.

Applicability: Adapted to existing product role. Restore utility configuration and retained evidence per operator policy; backend recovery requires separately approved plans and verified receipts without blind replay.

Existing local parent IDs: GYS-OBS-001. Existing local tasks remain authoritative; this projection refines qualification without changing their acceptance.

Source contracts: [README.md](../../../README.md) · [docs/current/ARCHITECTURE.md](../../current/ARCHITECTURE.md) · [docs/OBSERVABILITY_MCP.md](../../OBSERVABILITY_MCP.md)

Dependencies: GYS-DEPLOY-01, GYS-DEPLOY-03, GYS-DEPLOY-07. Worksheet: Backup, upgrade and troubleshooting.

- **GYS-DEPLOY-08-AC1** — Inventory authoritative state, configuration, keys via secret references, required evidence and ephemeral data; assign backup/retention/access ownership and reviewed RPO/RTO for each recoverable component. **Status: Not run.**
- **GYS-DEPLOY-08-AC2** — Produce integrity-verified backups and rehearse restoration into an isolated target, including missing/corrupt data and ownership/permission checks; a successful backup command is not restore acceptance. **Status: Not run.**
- **GYS-DEPLOY-08-AC3** — Qualify preflight, compatibility/migration checks, staged or canary upgrade, interrupted execution and rollback against immutable old/new artifacts; preserve supported data and active-work invariants. **Status: Not run.**
- **GYS-DEPLOY-08-AC4** — Exercise representative outages and recovery runbooks with bounded correlated diagnostics, symptom-to-check guidance, escalation roles and safe collection/redaction; retain unresolved outcomes instead of auto-closing them. **Status: Not run.**
- **GYS-DEPLOY-08-AC5** — Record measured restore/recovery outcomes, upgrade/rollback source identities, operator review and follow-up defects; repeat required recovery/soak gates before go-live or after material change. **Status: Not run.**

Planned documentation/qualification work. Source revision, installed target, reviewer and measured evidence must be recorded; acceptance remains Not run.

## GYS-DEPLOY-09 — Deployment worksheets and go-live checklists

Priority: P0. Proposed owner: Release and site acceptance owner; assignee Unassigned. Status Planned; acceptance Not run.

Product scope: Provide package/module-interface handoff with consumer owner, source/configuration identity and N/A reasons; infrastructure deliverables are not new product features.

Applicability: Adapted to existing product role. Provide package/module-interface handoff with consumer owner, source/configuration identity and N/A reasons; infrastructure deliverables are not new product features.

Existing local parent IDs: None for this area. No local product catalog covers this area. Use existing source/document contracts below and assign consuming package/module ownership before implementation; no parent ID is invented.

Source contracts: [README.md](../../../README.md) · [docs/current/ARCHITECTURE.md](../../current/ARCHITECTURE.md) · [docs/OBSERVABILITY_MCP.md](../../OBSERVABILITY_MCP.md)

Dependencies: GYS-DEPLOY-01, GYS-DEPLOY-02, GYS-DEPLOY-03, GYS-DEPLOY-04, GYS-DEPLOY-05, GYS-DEPLOY-06, GYS-DEPLOY-07, GYS-DEPLOY-08. Worksheet: Go-live and handover.

- **GYS-DEPLOY-09-AC1** — Provide versioned worksheets for site/role inventory, network/IP allocations, installation/configuration identity, availability topology, image/package rollout, applicable scheduler validation, hardening and recovery. **Status: Not run.**
- **GYS-DEPLOY-09-AC2** — For every applicable requirement record proposed/assigned owner, acceptance evidence reference, revision/environment identity, result and unresolved defect; explicitly justify non-applicable items rather than treating them as passing. **Status: Not run.**
- **GYS-DEPLOY-09-AC3** — Define go/no-go rules covering completed required CI, current reviewed source/configuration, installed/native acceptance, security exceptions, capacity/performance, backup restore, rollback and operator readiness. **Status: Not run.**
- **GYS-DEPLOY-09-AC4** — Require accountable release/site approval, a maintenance and rollback window, communication/escalation ownership and post-deployment observation criteria; blank approvals or missing/failed/stale evidence mean no-go. **Status: Not run.**
- **GYS-DEPLOY-09-AC5** — Record post-go-live health, retained evidence, unresolved backlog and handover ownership; merge/closure of this documentation change must not close unvalidated implementation or product-acceptance requirements. **Status: Not run.**

Planned documentation/qualification work. Source revision, installed target, reviewer and measured evidence must be recorded; acceptance remains Not run.

## Completion boundary

Documentation completion requires valid IDs/dependencies, Markdown/JSON parity, same-repository links and inventory updates. It does not satisfy installed acceptance. Blank approval, missing/failed/stale evidence, material defects or unsupported topology means NO-GO. Original feature acceptance and issue states remain separate.
