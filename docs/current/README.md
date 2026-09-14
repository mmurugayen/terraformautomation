# Current documentation: terraformautomation

Last source review: **2026-09-14**, default branch `dev`, commit [`fc5938592c34`](https://github.com/mmurugayen/terraformautomation/commit/fc5938592c347e09e6fbf684bcea3d7affd1d490). This records a documentation review of the linked source snapshot.

The source contains a diagnostic utility; no domain product or Terraform resources are declared.

- [Architecture](ARCHITECTURE.md)
- [Workflow](WORKFLOWS.md)
- [Audit and complete inventory](DOCUMENTATION_AUDIT.md)
- [Validation](VALIDATION.md)
- [Repository README](../../README.md)

## Maintaining the diagrams

Edit [diagrams.json](diagrams/diagrams.json), then run `python3 docs/current/diagrams/render.py`. Commit sources and generated SVGs together.

Check reproducibility with `python3 docs/current/diagrams/render.py --check`. Architecture `units` contain components; workflow `nodes` describe actions and alternatives. Refresh the source commit after comparing implementation changes.
