#!/usr/bin/env python3
"""Fail-closed implementation/qualification status gate."""
import argparse
import logging,json,logging
from pathlib import Path

LOG = logging.getLogger(__name__)
LOG=logging.getLogger(__name__);VALID={"implemented","partial","not_implemented","native_pending"}
def _load(path: Path):
 items=json.loads(path.read_text(encoding="utf-8")).get("items",[])
 if not items: LOG.error("implementation status empty");raise SystemExit("items must be non-empty")
 seen=set()
 for x in items:
  i,s=x.get("id"),x.get("status")
  if not i or i in seen or s not in VALID: LOG.error("invalid status id=%r status=%r",i,s);raise SystemExit("invalid record")
  seen.add(i)
  if s=="implemented" and not x.get("evidence"): LOG.error("missing evidence id=%s",i);raise SystemExit(f"{i}: implemented requires evidence")
  if s=="native_pending" and x.get("native_required") is not True: LOG.error("missing native flag id=%s",i);raise SystemExit(f"{i}: native_pending requires native_required=true")
 LOG.info("validated items=%d",len(items));return items
def _main():
 logging.basicConfig(level=logging.INFO);p=argparse.ArgumentParser();p.add_argument("--file",default="implementation-status.json");p.add_argument("--require-complete",action="store_true");a=p.parse_args()
 items=_load(Path(a.file));counts={s:sum(x["status"]==s for x in items) for s in sorted(VALID)};complete=all(x["status"]=="implemented" for x in items);print(json.dumps({"counts":counts,"complete":complete},sort_keys=True))
 if a.require_complete and not complete: LOG.error("release incomplete counts=%s",counts);raise SystemExit(2)
 LOG.info("status gate passed complete=%s",complete)
if __name__=="__main__":_main()