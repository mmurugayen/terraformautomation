# Documentation audit: terraformautomation

Reviewed **2026-09-14**, default branch `dev`, source commit [`fc5938592c34`](https://github.com/mmurugayen/terraformautomation/commit/fc5938592c347e09e6fbf684bcea3d7affd1d490).

The fetched snapshot contains **31 tracked files**, including **9 text documents** and **0 Office/PDF artifacts**. The [inventory](documentation-inventory.json) records every original document and documentation asset by source blob, review disposition and current content hash where applicable.

## Current corrections

Corrected the review permalink and rendered explicit MCP process, configured log files and optional external backend boundaries. Added a local-only branch to the diagnostic workflow.

The root README and current architecture/workflow review links identify this source snapshot. The main architecture uses explicit containers with nested components; separate workflows describe lifecycle decisions. Editable JSON and SVGs are kept reproducible with `python3 docs/current/diagrams/render.py --check`.

## Freshness method and limits

The live default branch was inventoried, and every materialized file was obtained by matching its Git blob hash. Changes since the preceding recorded documentation review were compared on GitHub. Current READMEs, launchers, application factories, persistence boundaries, adapters and the linked workflow implementations were checked against the source. Existing text documents were scanned for relative file navigation.

Historical roadmaps, dated test records, release snapshots and supplied Office/PDF artifacts retain their original dates and evidence. Their presence does not establish current implementation or qualification. This audit does not recertify every historical design claim or rerun site acceptance. Use the current architecture, product scope and installation guides for operational entry points.

## Navigation

All maintained relative file targets resolve.

Product-map links, where present, target current default branches. External service availability and third-party URLs were not live-tested.

## Recorded source dependencies

| Git dependency | Committed revision |
| --- | --- |
| None | No Git submodule dependency |

Dependency commits are source provenance; they do not imply a running service or include newer upstream main changes. This documentation refresh does not advance a dependency pin.

## Source changes considered

Comparison: [`6bccd25d259b...fc5938592c34`](https://github.com/mmurugayen/terraformautomation/compare/6bccd25d259b89453915c76d70c235eb96af3546...fc5938592c347e09e6fbf684bcea3d7affd1d490). The [refresh record](refresh-validation.json) lists implementation, launcher and CI paths changed since the previous review. Documentation-only source advances retain the existing implementation contract.

## Validation and maintenance

[Validation commands and results](VALIDATION.md) · [Architecture](ARCHITECTURE.md) · [Product workflows](WORKFLOWS.md) · [Repository README](../../README.md).

On the next source change, compare the relevant implementation and update the guide, diagram source, generated SVG and reviewed commit together. Keep past validation dates attached to the revision that produced them.
