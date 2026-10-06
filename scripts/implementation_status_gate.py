#!/usr/bin/env python3
"""Fail-closed implementation/qualification status gate."""

import argparse
import json
import logging
from pathlib import Path

LOG = logging.getLogger(__name__)
VALID = {"implemented", "partial", "not_implemented", "native_pending"}


def _load(path: Path):
    data = json.loads(path.read_text(encoding="utf-8"))
    items = data.get("items", [])
    if not isinstance(items, list) or not items:
        LOG.error("implementation status empty")
        raise SystemExit("implementation-status: items must be non-empty")
    seen = set()
    for item in items:
        ident = item.get("id")
        status = item.get("status")
        if not ident or ident in seen or status not in VALID:
            LOG.error("invalid implementation status record id=%r status=%r", ident, status)
            raise SystemExit("implementation-status: invalid record")
        seen.add(ident)
        if status == "implemented" and not item.get("evidence"):
            LOG.error("implemented item lacks evidence id=%s", ident)
            raise SystemExit(f"{ident}: implemented requires evidence")
        if status == "native_pending" and item.get("native_required") is not True:
            LOG.error("native pending item lacks native flag id=%s", ident)
            raise SystemExit(f"{ident}: native_pending requires native_required=true")
    LOG.info("validated implementation status items=%d", len(items))
    return items


def _main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s %(message)s")
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", default="implementation-status.json")
    parser.add_argument("--require-complete", action="store_true")
    args = parser.parse_args()
    items = _load(Path(args.file))
    counts = {status: sum(item["status"] == status for item in items) for status in sorted(VALID)}
    complete = all(item["status"] == "implemented" for item in items)
    print(json.dumps({"counts": counts, "complete": complete}, sort_keys=True))
    if args.require_complete and not complete:
        LOG.error("release completeness gate failed counts=%s", counts)
        raise SystemExit(2)
    LOG.info("implementation status gate passed complete=%s", complete)


if __name__ == "__main__":
    _main()
